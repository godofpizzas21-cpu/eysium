/**
 * Performance budget enforcement.
 *
 * `eng.design-system` section 6 sets budgets and says they are checked in CI,
 * "because a rule nobody measures is a rule nobody keeps". This is that check.
 *
 * Initial JS is what the browser must fetch before the application is usable.
 * The renderer is excluded because it is lazy: the accessible interface — the
 * real document — paints without it.
 */
import { gzipSync } from "node:zlib";
import { readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const DIST = resolve(HERE, "..", "dist");
const DATA = join(DIST, "data");

/** Budgets in kilobytes, gzipped. From eng.design-system section 6. */
const BUDGETS = {
  initialJs: { target: 220, hardFail: 300 },
  initialCss: { target: 20, hardFail: 40 },
  eagerData: { target: 40, hardFail: 60 },
};

/**
 * Chunks fetched before the application is usable. Everything else is behind
 * the lazy renderer boundary in `src/scene/Stage.tsx`.
 */
const INITIAL = /(^|\/)(index|vendor|rolldown-runtime)-/;

const gzipKb = (path: string) => gzipSync(readFileSync(path)).length / 1024;

function assets(): string[] {
  const dir = join(DIST, "assets");
  return readdirSync(dir)
    .map((name) => join(dir, name))
    .filter((path) => statSync(path).isFile());
}

let failed = false;

function report(label: string, actual: number, budget: { target: number; hardFail: number }) {
  const verdict =
    actual > budget.hardFail ? "OVER BUDGET" : actual > budget.target ? "over target" : "ok";
  if (actual > budget.hardFail) failed = true;
  console.log(
    `  ${label.padEnd(14)} ${actual.toFixed(1).padStart(7)} kB  ` +
      `(target ${budget.target}, hard fail ${budget.hardFail})  ${verdict}`,
  );
}

console.log("Performance budget");

const files = assets();

const initialJs = files
  .filter((path) => path.endsWith(".js") && INITIAL.test(path))
  .reduce((total, path) => total + gzipKb(path), 0);
report("initial JS", initialJs, BUDGETS.initialJs);

const initialCss = files
  .filter((path) => path.endsWith(".css"))
  .reduce((total, path) => total + gzipKb(path), 0);
report("initial CSS", initialCss, BUDGETS.initialCss);

// The eager set, kept in step with loadCanon() in src/data/loader.ts.
const eagerData = [
  "entity-index.json",
  "planet-physical.json",
  "continents.json",
  "cities.json",
  "calendar.json",
]
  .map((name) => join(DATA, name))
  .reduce((total, path) => total + gzipKb(path), 0);
report("eager data", eagerData, BUDGETS.eagerData);

const lazyJs = files
  .filter((path) => path.endsWith(".js") && !INITIAL.test(path))
  .reduce((total, path) => total + gzipKb(path), 0);
console.log(`  ${"renderer".padEnd(14)} ${lazyJs.toFixed(1).padStart(7)} kB  (lazy, not counted)`);

if (failed) {
  console.error("\nBudget exceeded. Reduce the payload or change the budget deliberately.");
  process.exit(1);
}
console.log("\nwithin budget");
