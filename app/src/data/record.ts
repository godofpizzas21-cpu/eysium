/**
 * Record retrieval for the Record Drawer.
 *
 * The eager index carries only what search and navigation need. When a person
 * asks to see the record, this fetches the entity's own dataset and finds it,
 * so the drawer shows the entry as it actually exists in canon rather than a
 * summary of it.
 */
import { loadDataset } from "./loader.js";

export interface EntityRecord {
  id: string;
  dataset: string;
  dataVersion: string;
  /** Bible document ids that canonize this entity. */
  sources: string[];
  /** The entry exactly as it appears in the dataset. */
  raw: Record<string, unknown>;
}

/** Depth-first search for an entity by id anywhere inside a dataset. */
function findEntity(node: unknown, id: string): Record<string, unknown> | null {
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
}

export async function loadRecord(id: string, dataset: string): Promise<EntityRecord | null> {
  const data = await loadDataset<Record<string, unknown>>(dataset);
  const raw = findEntity(data, id);
  if (!raw) return null;

  return {
    id,
    dataset,
    dataVersion: typeof data.dataVersion === "string" ? data.dataVersion : "unknown",
    sources: Array.isArray(raw.sources) ? (raw.sources as string[]) : [],
    raw,
  };
}
