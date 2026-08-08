/**
 * The Elysium Atlas data pipeline.
 *
 * Canon flows one way: `../data` -> `app/public/data`. This script never writes
 * to the canon directory. See `eng.data-pipeline`.
 *
 *   1. Canon lint        run tools/lint_canon.py
 *   2. Schema validation validate every dataset
 *   3. Reference check   resolve every cross-dataset id reference
 *   4. Emit              copy datasets, build the entity index and manifests
 *   5. Types             generate TypeScript from the schemas
 *
 * Any failure exits non-zero, so a canon error fails the deploy rather than
 * shipping a broken atlas.
 */
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { z } from "zod";

import { DatasetHeader, Entity, ID_DOMAINS } from "./schemas/common.js";
import { STRICT_SCHEMAS } from "./schemas/datasets.js";
import { LAYERS } from "./layers.js";

const HERE = dirname(fileURLToPath(import.meta.url));
const APP = resolve(HERE, "..");
const REPO = resolve(APP, "..");
const CANON = join(REPO, "data");
const OUT = join(APP, "public", "data");
const GENERATED = join(APP, "src", "data", "generated");

type Json = Record<string, unknown>;

const problems: string[] = [];
const fail = (message: string) => problems.push(message);

/* ------------------------------------------------------------------ stage 1 */

function lintCanon() {
  const linter = join(REPO, "tools", "lint_canon.py");
  if (!existsSync(linter)) {
    fail("tools/lint_canon.py is missing; canon cannot be verified");
    return;
  }
  try {
    const output = execFileSync("python3", [linter], { cwd: REPO, encoding: "utf8" });
    const summary = output.trim().split("\n").pop() ?? "";
    console.log(`  canon lint: ${summary.trim()}`);
  } catch (error) {
    const shown = (error as { stdout?: string }).stdout ?? String(error);
    fail(`canon lint failed:\n${shown}`);
  }
}

/* ------------------------------------------------------------------ stage 2 */

function readDatasets(): Map<string, Json> {
  const datasets = new Map<string, Json>();
  for (const file of readdirSync(CANON).filter((file) => file.endsWith(".json")).sort()) {
    datasets.set(file, JSON.parse(readFileSync(join(CANON, file), "utf8")) as Json);
  }
  return datasets;
}

function describe(error: unknown): string {
  if (error instanceof z.ZodError) {
    return error.issues
      .slice(0, 6)
      .map((issue) => `      ${issue.path.join(".") || "(root)"}: ${issue.message}`)
      .join("\n");
  }
  return `      ${String(error)}`;
}

/** Walk every object in a dataset and validate anything that looks like an entity. */
function validateEntities(file: string, node: unknown, path: string[] = []) {
  if (Array.isArray(node)) {
    node.forEach((child, index) => validateEntities(file, child, [...path, String(index)]));
    return;
  }
  if (node === null || typeof node !== "object") return;

  const record = node as Json;
  if (typeof record.id === "string" && typeof record.name === "string") {
    const result = Entity.safeParse(record);
    if (!result.success) {
      fail(`${file} at ${path.join(".") || "(root)"}\n${describe(result.error)}`);
    }
  }
  for (const [key, value] of Object.entries(record)) {
    validateEntities(file, value, [...path, key]);
  }
}

function validateSchemas(datasets: Map<string, Json>) {
  let strict = 0;
  for (const [file, data] of datasets) {
    const header = DatasetHeader.safeParse(data);
    if (!header.success) fail(`${file} header\n${describe(header.error)}`);

    const schema = STRICT_SCHEMAS[file];
    if (schema) {
      const result = schema.safeParse(data);
      if (!result.success) fail(`${file}\n${describe(result.error)}`);
      else strict += 1;
    }
    validateEntities(file, data);
  }
  console.log(`  validated ${datasets.size} datasets (${strict} against strict schemas)`);
}

/* ------------------------------------------------------------------ stage 3 */

/**
 * Reference fields are defined once, in `../../tools/reference-fields.json`, and
 * read by both this pipeline and `tools/lint_canon.py`. Keeping two lists in two
 * languages is exactly the duplication `charter.canon-rules` section 2 forbids.
 */
const referenceConfig = JSON.parse(
  readFileSync(join(REPO, "tools", "reference-fields.json"), "utf8"),
) as { fields: string[]; symbolic: string[]; datasetFields: string[] };

const REFERENCE_KEYS = new Set(referenceConfig.fields);
const DATASET_KEYS = new Set(referenceConfig.datasetFields);
const SYMBOLIC = new Set(referenceConfig.symbolic);

function collectEntities(node: unknown, into: Map<string, Json>) {
  if (Array.isArray(node)) {
    node.forEach((child) => collectEntities(child, into));
    return;
  }
  if (node === null || typeof node !== "object") return;
  const record = node as Json;
  if (typeof record.id === "string" && typeof record.name === "string") {
    into.set(record.id, record);
  }
  Object.values(record).forEach((value) => collectEntities(value, into));
}

function checkReferences(datasets: Map<string, Json>, entities: Map<string, Json>) {
  const domains = new Set<string>(ID_DOMAINS);

  const walk = (file: string, node: unknown) => {
    if (Array.isArray(node)) return node.forEach((child) => walk(file, child));
    if (node === null || typeof node !== "object") return;
    for (const [key, value] of Object.entries(node as Json)) {
      if (DATASET_KEYS.has(key)) {
        for (const candidate of Array.isArray(value) ? value : [value]) {
          if (typeof candidate === "string" && !datasets.has(candidate)) {
            fail(`${file}: dataset '${candidate}' in field '${key}' does not exist`);
          }
        }
      } else if (REFERENCE_KEYS.has(key)) {
        for (const candidate of Array.isArray(value) ? value : [value]) {
          if (typeof candidate !== "string" || SYMBOLIC.has(candidate)) continue;
          const domain = candidate.split(".")[0] ?? "";
          if (!domains.has(domain)) continue; // prose, not a reference
          if (!entities.has(candidate)) {
            fail(`${file}: unresolved reference '${candidate}' in field '${key}'`);
          }
        }
      }
      walk(file, value);
    }
  };

  for (const [file, data] of datasets) walk(file, data);
  console.log(
    `  resolved references across ${entities.size} entities ` +
      `(${REFERENCE_KEYS.size} reference fields, shared with the canon linter)`,
  );
}

/* ------------------------------------------------------------------ stage 4 */

/**
 * The eager index deliberately omits `summary`.
 *
 * Summaries are ~44 kB across 1,071 entities and are only needed once an entity
 * is selected, at which point its dataset is already loaded. Carrying them here
 * would breach the eager-data budget in `eng.design-system` section 6 to no
 * benefit. Search runs on name and tags.
 */
interface IndexEntry {
  id: string;
  name: string;
  tags?: string[];
  dataset: string;
  lat?: number;
  lon?: number;
  population?: number;
}

function emit(datasets: Map<string, Json>, entities: Map<string, Json>) {
  rmSync(OUT, { recursive: true, force: true });
  mkdirSync(OUT, { recursive: true });

  /*
   * Continent colours, derived at build time from the biomes canon says occupy
   * them. Each biome in biomes.json names the regions it covers, so a
   * continent's colour is the area-weighted blend of its own biomes, lifted
   * until it reads clearly against the ocean.
   *
   * This is derived data on the emitted artifact, never on canon itself.
   */
  const biomes = datasets.get("biomes.json");
  if (biomes) {
    const parse = (hex: string): [number, number, number] => [
      parseInt(hex.slice(1, 3), 16),
      parseInt(hex.slice(3, 5), 16),
      parseInt(hex.slice(5, 7), 16),
    ];
    const toHex = (c: [number, number, number]) =>
      `#${c.map((v) => Math.round(Math.min(255, Math.max(0, v))).toString(16).padStart(2, "0")).join("")}`;

    const terrestrial = biomes.terrestrialBiomes as Json[];
    const continents = datasets.get("continents.json")?.continents as Json[] | undefined;

    for (const continent of continents ?? []) {
      const own = terrestrial.filter((biome) => {
        const regions = (biome.regions as string[] | undefined) ?? [];
        if (regions.includes(continent.id as string)) return true;
        // A biome may name a feature of the continent rather than the continent.
        const features = ((continent.features as Json[] | undefined) ?? []).map((f) => f.id);
        return regions.some((region) => features.includes(region));
      });

      const source = own.length ? own : terrestrial;
      let weight = 0;
      const blend: [number, number, number] = [0, 0, 0];
      for (const biome of source) {
        const area = Number(biome.areaMkm2 ?? 1);
        const rgb = parse(String(biome.palette));
        blend[0] += rgb[0] * area;
        blend[1] += rgb[1] * area;
        blend[2] += rgb[2] * area;
        weight += area;
      }
      const mean: [number, number, number] = [blend[0] / weight, blend[1] / weight, blend[2] / weight];
      // Lift toward light so land separates from the ocean beneath it.
      const lifted: [number, number, number] = [
        mean[0] * 0.78 + 228 * 0.22,
        mean[1] * 0.78 + 237 * 0.22,
        mean[2] * 0.78 + 240 * 0.22,
      ];
      continent.derivedPalette = toHex(lifted);
      continent.derivedFromBiomes = source.map((biome) => biome.id);
    }
  }


  for (const [file, data] of datasets) {
    writeFileSync(join(OUT, file), JSON.stringify(data));
  }

  // Which dataset each entity came from, for the Record Drawer.
  const origin = new Map<string, string>();
  for (const [file, data] of datasets) {
    const local = new Map<string, Json>();
    collectEntities(data, local);
    for (const key of local.keys()) if (!origin.has(key)) origin.set(key, file);
  }

  const index: IndexEntry[] = [];
  for (const [entityId, entity] of entities) {
    const point = (entity.coordinates ?? entity.labelPoint) as
      | { lat: number; lon: number }
      | undefined;
    index.push({
      id: entityId,
      name: String(entity.name),
      ...(Array.isArray(entity.tags) && entity.tags.length
        ? { tags: entity.tags as string[] }
        : {}),
      dataset: origin.get(entityId) ?? "unknown",
      ...(point ? { lat: point.lat, lon: point.lon } : {}),
      ...(typeof entity.population === "number" ? { population: entity.population } : {}),
    });
  }
  index.sort((a, b) => a.id.localeCompare(b.id));
  writeFileSync(join(OUT, "entity-index.json"), JSON.stringify({ entities: index }));

  /** Read a dot path such as `biomes.terrestrialBiomes` out of the datasets. */
  const resolveSource = (source: string): Json[] => {
    const [key, ...rest] = source.split(".");
    let cursor: unknown = datasets.get(`${key}.json`);
    for (const step of rest) {
      if (cursor === null || typeof cursor !== "object") return [];
      cursor = (cursor as Json)[step];
    }
    return Array.isArray(cursor) ? (cursor as Json[]) : [];
  };

  /** Fields through which an entity names the places it belongs to. */
  const REGION_FIELDS = ["regions", "bestRegions", "deposits", "biome", "polity"];

  /** What each geometry kind requires of its source entities. */
  const REQUIRES: Record<string, (entry: Json) => boolean> = {
    arc: (entry) => Array.isArray(entry.path) && entry.path.length >= 2,
    "latitude-band": (entry) =>
      Array.isArray(entry.latitudeBandDeg) && entry.latitudeBandDeg.length === 2,
    point: (entry) => Boolean(entry.coordinates ?? entry.labelPoint),
    orbit: (entry) => typeof entry.orbitalDistanceKm === "number",
    // Canon names places through several fields; region-point accepts any.
    "region-point": (entry) =>
      REGION_FIELDS.some((field) => {
        const value = entry[field];
        return typeof value === "string" || (Array.isArray(value) && value.length > 0);
      }),
  };

  const manifests = LAYERS.map((layer) => {
    for (const file of layer.datasets) {
      if (!datasets.has(file)) fail(`layer ${layer.id}: dataset ${file} does not exist`);
    }
    for (const indicator of layer.indicators ?? []) {
      if (!entities.has(indicator)) fail(`layer ${layer.id}: indicator ${indicator} does not exist`);
    }

    // A layer may not promise geometry the data cannot provide.
    for (const geometry of layer.geometry) {
      const source = resolveSource(geometry.source);
      if (!source.length) {
        fail(`layer ${layer.id}: geometry source '${geometry.source}' resolves to nothing`);
        continue;
      }
      const test = REQUIRES[geometry.kind];
      if (!test) {
        fail(`layer ${layer.id}: unknown geometry kind '${geometry.kind}'`);
        continue;
      }
      const usable = source.filter(test).length;
      if (usable === 0) {
        fail(
          `layer ${layer.id}: no entity in '${geometry.source}' carries what ` +
            `'${geometry.kind}' geometry needs`,
        );
      } else if (usable < source.length) {
        console.log(
          `  note: ${layer.id} ${geometry.kind} covers ${usable}/${source.length} ` +
            `of ${geometry.source}`,
        );
      }
    }
    return layer;
  });
  writeFileSync(join(OUT, "layer-manifests.json"), JSON.stringify({ layers: manifests }));

  const located = index.filter((entry) => entry.lat !== undefined).length;
  console.log(
    `  emitted ${datasets.size} datasets, ${index.length} indexed entities ` +
      `(${located} located), ${manifests.length} layer manifests`,
  );
}

/* ------------------------------------------------------------------ stage 5 */

function generateTypes(datasets: Map<string, Json>) {
  mkdirSync(GENERATED, { recursive: true });
  const names = [...datasets.keys()].sort();

  const header = "// Generated by tools/build-data.ts. Do not edit.\n\n";

  const datasetUnion = names.map((n) => `  | ${JSON.stringify(n)}`).join("\n");
  writeFileSync(
    join(GENERATED, "datasets.ts"),
    `${header}/** Every canon dataset shipped with the Atlas. */\nexport type DatasetFile =\n${datasetUnion};\n\nexport const DATASET_FILES: readonly DatasetFile[] = [\n${names
      .map((n) => `  ${JSON.stringify(n)},`)
      .join("\n")}\n] as const;\n`,
  );

  writeFileSync(
    join(GENERATED, "index.ts"),
    `${header}export * from "./datasets.js";\nexport * from "./entities.js";\n`,
  );

  writeFileSync(
    join(GENERATED, "entities.ts"),
    `${header}import type { DatasetFile } from "./datasets.js";\n\n` +
      `/** A lightweight record of every canonical entity, loaded before first paint. */\n` +
      `export interface IndexEntry {\n` +
      `  id: string;\n  name: string;\n  tags?: string[];\n` +
      `  dataset: DatasetFile | "unknown";\n  lat?: number;\n  lon?: number;\n  population?: number;\n}\n\n` +
      `export interface EntityIndex {\n  entities: IndexEntry[];\n}\n`,
  );

  console.log(`  generated types for ${names.length} datasets`);
}

/* --------------------------------------------------------------------- run */

console.log("Elysium Atlas — data pipeline");

console.log("[1/5] canon lint");
lintCanon();

console.log("[2/5] schema validation");
const datasets = readDatasets();
validateSchemas(datasets);

console.log("[3/5] reference resolution");
const entities = new Map<string, Json>();
for (const data of datasets.values()) collectEntities(data, entities);
checkReferences(datasets, entities);

if (problems.length) {
  console.error(`\n${problems.length} problem(s):\n`);
  for (const problem of problems) console.error(`  - ${problem}`);
  process.exit(1);
}

console.log("[4/5] emit");
emit(datasets, entities);

console.log("[5/5] types");
generateTypes(datasets);

if (problems.length) {
  console.error(`\n${problems.length} problem(s) during emit:\n`);
  for (const problem of problems) console.error(`  - ${problem}`);
  process.exit(1);
}

console.log("\ndata pipeline complete");
