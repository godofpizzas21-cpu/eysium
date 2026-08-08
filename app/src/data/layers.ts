/**
 * Layer loading.
 *
 * A layer names its datasets in the manifest generated from the registry. This
 * module fetches them on first use and caches them, so switching back to a
 * layer is instant. See `eng.data-pipeline` section 5.
 */
import { loadDataset } from "./loader.js";

export type GeometryKind =
  | "arc"
  | "latitude-band"
  | "point"
  | "region-point"
  | "orbit";

export interface LayerGeometry {
  kind: GeometryKind;
  source: string;
  colour: string;
  /** For `point`, a numeric field that scales the symbol. */
  scaleBy?: string;
}

export interface LayerManifest {
  id: string;
  name: string;
  summary: string;
  datasets: string[];
  geometry: LayerGeometry[];
  selectable: string[];
  indicators?: string[];
  eager?: boolean;
  /** `space` widens the camera envelope to hold the moons. */
  view?: "surface" | "space";
  phase: string;
}

export interface LayerBundle {
  manifest: LayerManifest;
  /** Each named dataset, keyed by filename. */
  data: Record<string, unknown>;
}

export async function loadManifests(): Promise<LayerManifest[]> {
  const file = await loadDataset<{ layers: LayerManifest[] }>("layer-manifests.json");
  return file.layers;
}

export async function loadLayer(manifest: LayerManifest): Promise<LayerBundle> {
  const entries = await Promise.all(
    manifest.datasets.map(async (file) => [file, await loadDataset(file)] as const),
  );
  return { manifest, data: Object.fromEntries(entries) };
}

/** Read a dot path such as `biomes.terrestrialBiomes` out of a loaded bundle. */
export function resolveSource(bundle: LayerBundle, source: string): unknown[] {
  const [datasetKey, ...rest] = source.split(".");
  const file = `${datasetKey}.json`;
  let cursor: unknown = bundle.data[file];
  for (const key of rest) {
    if (cursor === null || typeof cursor !== "object") return [];
    cursor = (cursor as Record<string, unknown>)[key];
  }
  return Array.isArray(cursor) ? cursor : [];
}

/** Indicators a layer surfaces, resolved against metrics.json. */
export interface Indicator {
  id: string;
  name: string;
  summary: string;
  value: number;
  unit: string;
  trend: string;
  domain: string;
  sourceDataset?: string;
  derivation?: string;
}

/**
 * Counterweight pairs, from `metric.system` section 2.
 *
 * "Indicators liable to gaming are published alongside an indicator that would
 * move the wrong way if the first were being gamed... an indicator may not be
 * published without its counterweight."
 *
 * The Atlas enforces this at the data level rather than in a component, so no
 * view can show one half of a pair by accident.
 */
export const COUNTERWEIGHTS: Record<string, string> = {
  "metric.custody-rate": "metric.reoffending",
  "metric.reserve-margin": "metric.islanding-failure",
  "metric.land-protected": "metric.extinction-debt",
  "metric.rd-intensity": "metric.replication",
  "metric.gcp-per-capita": "metric.income-gini",
  "metric.energy-demand": "metric.beryllium-horizon",
};

/** An indicator, with its counterweight attached where canon pairs one. */
export interface PairedIndicator extends Indicator {
  counterweight?: Indicator;
}

export async function loadIndicators(ids: string[]): Promise<PairedIndicator[]> {
  if (!ids.length) return [];
  const metrics = await loadDataset<{ indicators: Indicator[] }>("metrics.json");
  const byId = new Map(metrics.indicators.map((indicator) => [indicator.id, indicator]));

  const paired: PairedIndicator[] = [];
  for (const id of ids) {
    const indicator = byId.get(id);
    if (!indicator) continue;
    const counterweightId = COUNTERWEIGHTS[id];
    const counterweight = counterweightId ? byId.get(counterweightId) : undefined;
    paired.push(counterweight ? { ...indicator, counterweight } : indicator);
  }
  return paired;
}
