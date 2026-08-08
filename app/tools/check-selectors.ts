/**
 * Selector safety check.
 *
 * A zustand selector that builds a new value returns a new reference on every
 * read. React sees a change, reads again, and the application enters an
 * infinite render loop — React error #185, which is invisible to typechecking
 * and to any test that does not run a browser.
 *
 * This caught nothing at build time and everything at deploy time, so it is
 * now checked here: selectors may call store methods that return existing
 * references, but may not construct arrays or objects.
 */
import { readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = resolve(HERE, "..", "src");

function walk(dir: string): string[] {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name);
    return statSync(path).isDirectory() ? walk(path) : path.endsWith(".tsx") || path.endsWith(".ts") ? [path] : [];
  });
}

/** Store methods known to return an existing reference rather than a new one. */
const SAFE_METHODS = new Set([
  "activeLayer",
  "selectedEntity",
  "selectedCity",
  "selectedSummary",
]);

let failed = 0;
console.log("Selector safety");

for (const file of walk(SRC)) {
  const source = readFileSync(file, "utf8");
  const short = file.slice(SRC.length + 1);

  for (const [, body] of source.matchAll(/useAtlas\(\s*\((?:s|state)\)\s*=>\s*([^)]*)\)/g)) {
    const selector = body!.trim();

    // A selector building a literal is always unsafe.
    if (/^[[{]/.test(selector)) {
      console.error(`  FAIL  ${short}: selector builds a literal — ${selector.slice(0, 48)}`);
      failed += 1;
      continue;
    }

    // A selector calling a method must call one known to be reference-stable.
    const call = /\bs(?:tate)?\.([a-zA-Z]+)\s*\(/.exec(selector);
    if (call && !SAFE_METHODS.has(call[1]!)) {
      console.error(
        `  FAIL  ${short}: selector calls ${call[1]}() which may build a new value. ` +
          `Compute it in useMemo instead, or add it to SAFE_METHODS if it returns an existing reference.`,
      );
      failed += 1;
    }
  }
}

if (failed) {
  console.error(`\n${failed} unsafe selector(s). These cause React error #185 at runtime.`);
  process.exit(1);
}
console.log("  ok    no selector constructs a new value");
console.log("\nall selectors safe");
