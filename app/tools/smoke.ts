/**
 * Smoke tests for the data layer's behaviour, not just its shape.
 *
 * These run against the emitted output and check the things the Atlas assumes
 * at runtime: that search finds real places, that focusable entities have
 * coordinates, and that every marker sits where canon says it does.
 */
import { existsSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const DATA = resolve(HERE, "..", "public", "data");

const read = <T>(name: string): T => JSON.parse(readFileSync(join(DATA, name), "utf8")) as T;

interface IndexEntry {
  id: string;
  name: string;
  tags?: string[];
  dataset: string;
  lat?: number;
  lon?: number;
}

const index = read<{ entities: IndexEntry[] }>("entity-index.json").entities;
const cities = read<{ cities: { id: string; name: string; coordinates: { lat: number; lon: number } }[] }>(
  "cities.json",
).cities;
interface Manifest {
  id: string;
  datasets: string[];
  indicators?: string[];
  geometry?: { kind: string; source: string; colour: string }[];
}
const manifests = read<{ layers: Manifest[] }>("layer-manifests.json").layers;

let failures = 0;
const check = (label: string, condition: boolean, detail = "") => {
  if (condition) {
    console.log(`  ok    ${label}`);
  } else {
    failures += 1;
    console.error(`  FAIL  ${label}${detail ? ` — ${detail}` : ""}`);
  }
};

console.log("Smoke tests");

check("index is populated", index.length > 1000, `${index.length} entities`);
check("index entries are unique", new Set(index.map((e) => e.id)).size === index.length);
check("every entry names its dataset", index.every((e) => e.dataset && e.dataset !== "unknown"));

// Search must find things a person would actually type.
const search = (needle: string) =>
  index.filter((e) => e.name.toLowerCase().includes(needle.toLowerCase()));
for (const term of ["Kessandra", "Sennary", "Alcyon", "Cindral", "Veydra"]) {
  check(`search finds "${term}"`, search(term).length > 0);
}

// Anything the camera can fly to must be locatable.
const located = index.filter((e) => e.lat !== undefined);
check("located entities exist", located.length > 100, `${located.length} located`);
check(
  "coordinates are in range",
  located.every((e) => e.lat! >= -90 && e.lat! <= 90 && e.lon! >= -180 && e.lon! <= 180),
);

// Every city in the dataset must be reachable through the index.
const byId = new Map(index.map((e) => [e.id, e]));
check(
  "every city is indexed with its coordinates",
  cities.every((city) => {
    const entry = byId.get(city.id);
    return entry?.lat === city.coordinates.lat && entry?.lon === city.coordinates.lon;
  }),
);

check("layer manifests exist", manifests.length > 0, `${manifests.length} layers`);

// Every layer's datasets must actually be emitted, or the layer cannot load.
for (const layer of manifests) {
  for (const dataset of layer.datasets) {
    check(
      `${layer.id} can load ${dataset}`,
      existsSync(join(DATA, dataset)),
    );
  }
}

// metric.system section 2: an indicator liable to gaming may not be published
// without its counterweight. The Atlas pairs them in data/layers.ts; this
// verifies both halves of every pair actually exist.
const metrics = read<{ indicators: { id: string }[] }>("metrics.json").indicators;
const metricIds = new Set(metrics.map((m) => m.id));
const COUNTERWEIGHTS: Record<string, string> = {
  "metric.custody-rate": "metric.reoffending",
  "metric.reserve-margin": "metric.islanding-failure",
  "metric.land-protected": "metric.extinction-debt",
  "metric.rd-intensity": "metric.replication",
  "metric.gcp-per-capita": "metric.income-gini",
  "metric.energy-demand": "metric.beryllium-horizon",
};
for (const [indicator, counterweight] of Object.entries(COUNTERWEIGHTS)) {
  check(
    `counterweight pair ${indicator.split(".")[1]} / ${counterweight.split(".")[1]} exists`,
    metricIds.has(indicator) && metricIds.has(counterweight),
  );
}

// Every layer's geometry must be drawable: each declared kind needs its
// source entities to carry the fields the renderer reads.
const REGION_FIELDS = ["regions", "bestRegions", "deposits", "biome", "polity"];
const readSource = (source: string): Record<string, unknown>[] => {
  const [key, ...rest] = source.split(".");
  let cursor: unknown = read<Record<string, unknown>>(`${key}.json`);
  for (const step of rest) {
    if (cursor === null || typeof cursor !== "object") return [];
    cursor = (cursor as Record<string, unknown>)[step];
  }
  return Array.isArray(cursor) ? (cursor as Record<string, unknown>[]) : [];
};

for (const layer of manifests) {
  for (const geometry of layer.geometry ?? []) {
    const entries = readSource(geometry.source);
    const usable = entries.filter((entry) => {
      if (geometry.kind === "arc") return Array.isArray(entry.path);
      if (geometry.kind === "latitude-band") return Array.isArray(entry.latitudeBandDeg);
      if (geometry.kind === "point") return Boolean(entry.coordinates ?? entry.labelPoint);
      if (geometry.kind === "orbit") return typeof entry.orbitalDistanceKm === "number";
      return REGION_FIELDS.some((field) => {
        const value = entry[field];
        return typeof value === "string" || (Array.isArray(value) && value.length > 0);
      });
    }).length;
    check(
      `${layer.id} can draw ${geometry.kind} from ${geometry.source}`,
      usable > 0,
      `${usable}/${entries.length} usable`,
    );
  }
}

// Layers painting from `palette` must have swatches to show, and every colour
// must be a real hex value — the legend is the canon palette shown directly.
for (const layer of manifests) {
  for (const geometry of layer.geometry ?? []) {
    if (geometry.colour !== "palette") continue;
    const entries = readSource(geometry.source);
    const coloured = entries.filter(
      (entry) => typeof entry.palette === "string" && /^#[0-9A-Fa-f]{6}$/.test(entry.palette),
    );
    check(
      `${layer.id} swatches from ${geometry.source}`,
      coloured.length > 0,
      `${coloured.length}/${entries.length} carry a hex palette`,
    );
  }
}

// Every indicator a layer surfaces must exist.
for (const layer of manifests) {
  for (const indicator of layer.indicators ?? []) {
    check(`${layer.id} indicator ${indicator} exists`, metricIds.has(indicator));
  }
}

/* --------------------------------------------------------------- record */

// The Record Drawer promises that any indexed entity can show its own entry.
// That requires every entity's named dataset to actually contain it.
const findEntity = (node: unknown, id: string): Record<string, unknown> | null => {
  if (Array.isArray(node)) {
    for (const child of node) {
      const found = findEntity(child, id);
      if (found) return found;
    }
    return null;
  }
  if (node === null || typeof node !== "object") return null;
  const record = node as Record<string, unknown>;
  if (record.id === id) return record;
  for (const value of Object.values(record)) {
    const found = findEntity(value, id);
    if (found) return found;
  }
  return null;
};

const datasetCache = new Map<string, unknown>();
const loadOnce = (name: string) => {
  if (!datasetCache.has(name)) datasetCache.set(name, read<unknown>(name));
  return datasetCache.get(name);
};

// Sample across the index rather than all 1,071, which would reparse endlessly.
const sample = index.filter((_, i) => i % 37 === 0);
const missing = sample.filter((entry) => !findEntity(loadOnce(entry.dataset), entry.id));
check(
  "every sampled entity can produce its own record",
  missing.length === 0,
  missing.length ? `missing: ${missing.slice(0, 3).map((e) => e.id).join(", ")}` : `${sample.length} sampled`,
);

// Every dataset must declare a version, since the drawer shows it.
const datasetsSeen = new Set(index.map((entry) => entry.dataset));
const unversioned = [...datasetsSeen].filter((name) => {
  const data = loadOnce(name) as Record<string, unknown>;
  return typeof data.dataVersion !== "string";
});
check("every dataset declares a version", unversioned.length === 0, unversioned.join(", "));

/* ---------------------------------------------------------------- space */

// Space mode draws the moons at true relative distance, so the numbers it
// renders from must be the ones canon holds.
const physical = read<{
  planet: { meanRadiusKm: number };
  moons: { id: string; name: string; meanRadiusKm: number; orbitalDistanceKm: number; orbitalPeriodElysianDays: number }[];
}>("planet-physical.json");
const space = read<{ orbitalMechanics: { stationaryOrbitAltitudeKm: number } }>("space.json");

const planetRadius = physical.planet.meanRadiusKm;
check("two moons are canonized", physical.moons.length === 2);
check(
  "every moon carries orbit geometry",
  physical.moons.every(
    (moon) => moon.orbitalDistanceKm > 0 && moon.orbitalPeriodElysianDays > 0,
  ),
);
check(
  "moons orbit outside the planet",
  physical.moons.every((moon) => moon.orbitalDistanceKm > planetRadius),
);
check(
  "the stationary ring sits inside Vesper's orbit",
  space.orbitalMechanics.stationaryOrbitAltitudeKm + planetRadius <
    Math.min(...physical.moons.map((moon) => moon.orbitalDistanceKm)),
);
check(
  "Kalyra orbits beyond Vesper and more slowly",
  (() => {
    const kalyra = physical.moons.find((moon) => moon.name === "Kalyra");
    const vesper = physical.moons.find((moon) => moon.name === "Vesper");
    if (!kalyra || !vesper) return false;
    return (
      kalyra.orbitalDistanceKm > vesper.orbitalDistanceKm &&
      kalyra.orbitalPeriodElysianDays > vesper.orbitalPeriodElysianDays
    );
  })(),
);

/* ------------------------------------------------------------- calendar */

// The Elysian calendar is implemented in src/lib/calendar.ts and must agree
// with calendar.json in every particular. No JavaScript Date object appears
// anywhere in the application, so these are the only checks on it.
const calendar = read<{
  clock: { hoursPerDay: number; minutesPerHour: number; beatsPerMinute: number; solarDaySeconds: number };
  year: {
    civilYearDays: number;
    daysPerMonth: number;
    monthsPerYear: number;
    daysPerWeek: number;
    weeksPerYear: number;
    solarYearDays: number;
    leapRule: { everyNYears: number; exceptDivisibleBy: number; meanCivilYearDays: number };
  };
  months: { index: number; name: string }[];
  weekdays: { index: number; name: string; rest: boolean }[];
  referenceDate: { year: number; month: number; day: number };
}>("calendar.json");

const { year: yr, clock } = calendar;

check("12 months of 32 days make 384", yr.monthsPerYear * yr.daysPerMonth === yr.civilYearDays);
check("384 divides into 8-day weeks", yr.civilYearDays / yr.daysPerWeek === yr.weeksPerYear);
check("the calendar is perpetual", Number.isInteger(yr.civilYearDays / yr.daysPerWeek));
check("months are indexed 1..12", calendar.months.every((m, i) => m.index === i + 1));
check("weekdays are indexed 1..8", calendar.weekdays.every((d, i) => d.index === i + 1));
check("two rest days per week", calendar.weekdays.filter((d) => d.rest).length === 2);

// The leap rule must produce the solar year over a century.
const leapsPerCentury =
  Math.floor(100 / yr.leapRule.everyNYears) - Math.floor(100 / yr.leapRule.exceptDivisibleBy);
const meanYear = yr.civilYearDays + leapsPerCentury / 100;
check(
  "the leap rule yields the solar year",
  Math.abs(meanYear - yr.solarYearDays) < 0.005,
  `${meanYear} vs ${yr.solarYearDays}`,
);

// Civil units are fractions of the solar day, not SI units.
const civilHourSeconds = clock.solarDaySeconds / clock.hoursPerDay;
check(
  "a civil hour is a fraction of the solar day",
  Math.abs(civilHourSeconds - 3586.15) < 0.1,
  `${civilHourSeconds.toFixed(2)} s`,
);
check("a civil hour is not an SI hour", Math.abs(civilHourSeconds - 3600) > 1);

// The reference date must be the one the whole Bible is written against.
check(
  "the reference date is EY 412, Calenth 16",
  calendar.referenceDate.year === 412 &&
    calendar.referenceDate.month === 8 &&
    calendar.referenceDate.day === 16,
);
check(
  "month 8 is Calenth",
  calendar.months.find((m) => m.index === 8)?.name === "Calenth",
);

if (failures) {
  console.error(`\n${failures} smoke test(s) failed.`);
  process.exit(1);
}
console.log("\nall smoke tests passed");
