/**
 * Contrast audit.
 *
 * `eng.design-system` section 7 requires 4.5:1 for body text and 3:1 for large
 * text and interface borders, "measured on the actual dark surfaces rather than
 * assumed". This measures them.
 */
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const TOKENS = resolve(HERE, "..", "src", "styles", "tokens.css");

type RGB = [number, number, number];

function parseHex(hex: string): RGB {
  const value = hex.replace("#", "");
  return [
    parseInt(value.slice(0, 2), 16),
    parseInt(value.slice(2, 4), 16),
    parseInt(value.slice(4, 6), 16),
  ];
}

/** WCAG relative luminance. */
function luminance([r, g, b]: RGB): number {
  const channel = (raw: number) => {
    const c = raw / 255;
    return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  };
  return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b);
}

function contrast(a: RGB, b: RGB): number {
  const [light, dark] = [luminance(a), luminance(b)].sort((x, y) => y - x) as [number, number];
  return (light + 0.05) / (dark + 0.05);
}

/** Composite a colour over a background at a given alpha. */
function mix(top: RGB, bottom: RGB, alpha: number): RGB {
  return top.map((value, i) => Math.round(value * alpha + bottom[i]! * (1 - alpha))) as RGB;
}

const css = readFileSync(TOKENS, "utf8");
const tokens = new Map<string, RGB>();
for (const [, name, hex] of css.matchAll(/(--[a-z-]+):\s*(#[0-9A-Fa-f]{6})/g)) {
  tokens.set(name!, parseHex(hex!));
}

const get = (name: string): RGB => {
  const found = tokens.get(name);
  if (!found) throw new Error(`Token ${name} is missing from tokens.css.`);
  return found;
};

// Surfaces are colour-mixed in CSS; reproduce them here so the audit measures
// what is actually painted.
const surface = mix(get("--abyss"), get("--void"), 0.72);
const surfaceRaised = mix(get("--abyss"), get("--ice"), 0.96);
const textDim = mix(get("--sirocc"), get("--abyss"), 0.62);

const CHECKS: { label: string; fg: RGB; bg: RGB; min: number }[] = [
  { label: "body text on surface", fg: get("--sirocc"), bg: surface, min: 4.5 },
  { label: "body text on raised surface", fg: get("--sirocc"), bg: surfaceRaised, min: 4.5 },
  { label: "body text on void", fg: get("--sirocc"), bg: get("--void"), min: 4.5 },
  { label: "strong text on surface", fg: get("--ice"), bg: surface, min: 4.5 },
  { label: "strong text on raised surface", fg: get("--ice"), bg: surfaceRaised, min: 4.5 },
  { label: "dim text on surface (large only)", fg: textDim, bg: surface, min: 3 },
  { label: "focus ring on surface", fg: get("--ice"), bg: surface, min: 3 },
  { label: "anomaly border on raised surface", fg: get("--anomaly"), bg: surfaceRaised, min: 3 },
  { label: "accent edge on raised surface", fg: get("--shelf-edge"), bg: surfaceRaised, min: 3 },
  { label: "accent edge on surface", fg: get("--shelf-edge"), bg: surface, min: 3 },
];

let failed = 0;
console.log("Contrast audit");
for (const check of CHECKS) {
  const ratio = contrast(check.fg, check.bg);
  const ok = ratio >= check.min;
  if (!ok) failed += 1;
  console.log(
    `  ${ok ? "ok  " : "FAIL"}  ${check.label.padEnd(34)} ${ratio.toFixed(2)}:1 ` +
      `(needs ${check.min}:1)`,
  );
}

if (failed) {
  console.error(`\n${failed} contrast requirement(s) not met.`);
  process.exit(1);
}
console.log("\nall contrast requirements met");
