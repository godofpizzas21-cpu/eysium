/**
 * Application state.
 *
 * Zustand rather than Context because the render loop reads this outside
 * React's render cycle at 60 fps — see `eng.architecture` section 2.2.
 */
import { create } from "zustand";
import type { Canon, City } from "../data/loader.js";
import type { LayerBundle, LayerManifest, PairedIndicator } from "../data/layers.js";
import type { ElysianDate, ElysianTime } from "../lib/calendar.js";
import type { IndexEntry } from "../data/generated/index.js";

export type LoadState =
  | { status: "loading" }
  | { status: "ready"; canon: Canon }
  | { status: "failed"; message: string };

/** Where the camera has been asked to look, in canonical degrees. */
export interface CameraTarget {
  lat: number;
  lon: number;
  /** Distance from the planet centre in render units. */
  distance: number;
  /** Bumped on every request so a repeat selection re-triggers the flight. */
  issued: number;
}

interface AtlasState {
  load: LoadState;
  setLoad: (load: LoadState) => void;

  /** The focused entity, or null. Selection is shared by both interfaces. */
  selectedId: string | null;
  select: (id: string | null) => void;

  /** Hover is render-loop state and deliberately separate from selection. */
  hoveredId: string | null;
  hover: (id: string | null) => void;

  autoRotate: boolean;
  setAutoRotate: (on: boolean) => void;

  cameraTarget: CameraTarget | null;
  flyTo: (point: { lat: number; lon: number }, distance?: number) => void;

  query: string;
  setQuery: (query: string) => void;

  /** Civil date and time. The Atlas opens at the Bible's reference date. */
  date: ElysianDate;
  time: ElysianTime;
  setDate: (date: ElysianDate) => void;
  setTime: (time: ElysianTime) => void;
  /** Whether the clock advances on its own. */
  running: boolean;
  setRunning: (running: boolean) => void;

  /** Layer manifests, loaded once with the eager set. */
  manifests: LayerManifest[];
  setManifests: (manifests: LayerManifest[]) => void;

  activeLayerId: string | null;
  /** Loaded layer bundles, keyed by layer id. Switching back is instant. */
  layers: Record<string, LayerBundle>;
  layerStatus: "idle" | "loading" | "ready" | "failed";
  layerError: string | null;
  indicators: PairedIndicator[];
  setLayerState: (patch: Partial<{
    activeLayerId: string | null;
    layerStatus: "idle" | "loading" | "ready" | "failed";
    layerError: string | null;
    indicators: PairedIndicator[];
  }>) => void;
  cacheLayer: (id: string, bundle: LayerBundle) => void;
  activeLayer: () => LayerBundle | null;
  /** Injected at start-up so the store does not import the loader. */
  showLayer: (id: string | null) => Promise<void>;
  setShowLayer: (fn: (id: string | null) => Promise<void>) => void;

  selectedEntity: () => IndexEntry | null;
  selectedSummary: () => string | null;
  selectedCity: () => City | null;
  /** Canonical coordinates for an entity, if it has any. */
  locate: (id: string) => { lat: number; lon: number } | null;
  results: (limit?: number) => IndexEntry[];
}

export const useAtlas = create<AtlasState>((set, get) => ({
  load: { status: "loading" },
  setLoad: (load) => set({ load }),

  selectedId: null,
  select: (selectedId) => {
    set({ selectedId, autoRotate: false });
    if (selectedId) {
      const point = get().locate(selectedId);
      if (point) get().flyTo(point);
    }
  },

  hoveredId: null,
  hover: (hoveredId) => set({ hoveredId }),

  autoRotate: true,
  setAutoRotate: (autoRotate) => set({ autoRotate }),

  cameraTarget: null,
  flyTo: (point, distance = 2.1) =>
    set({
      cameraTarget: { lat: point.lat, lon: point.lon, distance, issued: Date.now() },
      autoRotate: false,
    }),

  query: "",
  setQuery: (query) => set({ query }),

  // EY 412, Calenth 16 — the reference date of the whole Bible.
  date: { year: 412, month: 8, day: 16 },
  time: { hour: 13, minute: 0, beat: 0 },
  setDate: (date) => set({ date }),
  setTime: (time) => set({ time }),
  running: false,
  setRunning: (running) => set({ running }),

  manifests: [],
  setManifests: (manifests) => set({ manifests }),

  activeLayerId: null,
  layers: {},
  layerStatus: "idle",
  layerError: null,
  indicators: [],
  setLayerState: (patch) => set(patch),
  cacheLayer: (id, bundle) => set((state) => ({ layers: { ...state.layers, [id]: bundle } })),
  activeLayer: () => {
    const { activeLayerId, layers } = get();
    return activeLayerId ? (layers[activeLayerId] ?? null) : null;
  },
  showLayer: async () => {},
  setShowLayer: (showLayer) => set({ showLayer }),

  selectedEntity: () => {
    const { load, selectedId } = get();
    if (load.status !== "ready" || !selectedId) return null;
    return load.canon.byId.get(selectedId) ?? null;
  },

  selectedSummary: () => {
    const { load, selectedId } = get();
    if (load.status !== "ready" || !selectedId) return null;
    const city = load.canon.cities.cities.find((c) => c.id === selectedId);
    if (city) return city.summary;
    for (const continent of load.canon.continents.continents) {
      if (continent.id === selectedId) return continent.summary;
      for (const feature of continent.features) {
        if (feature.id === selectedId) return feature.summary;
      }
    }
    return null;
  },

  selectedCity: () => {
    const { load, selectedId } = get();
    if (load.status !== "ready" || !selectedId) return null;
    return load.canon.cities.cities.find((c) => c.id === selectedId) ?? null;
  },

  locate: (id) => {
    const { load } = get();
    if (load.status !== "ready") return null;

    const indexed = load.canon.byId.get(id);
    if (indexed?.lat !== undefined && indexed.lon !== undefined) {
      return { lat: indexed.lat, lon: indexed.lon };
    }
    const city = load.canon.cities.cities.find((c) => c.id === id);
    if (city) return city.coordinates;

    // Continents have no single point; use the mean of their labelled features.
    const continent = load.canon.continents.continents.find((c) => c.id === id);
    if (continent) {
      const points = continent.features
        .map((feature) => feature.labelPoint)
        .filter((point): point is { lat: number; lon: number } => Boolean(point));
      if (points.length) {
        return {
          lat: points.reduce((sum, p) => sum + p.lat, 0) / points.length,
          lon: points.reduce((sum, p) => sum + p.lon, 0) / points.length,
        };
      }
    }
    return null;
  },

  results: (limit = 12) => {
    const { load, query } = get();
    if (load.status !== "ready") return [];
    const needle = query.trim().toLowerCase();
    if (needle.length < 2) return [];

    const scored: { entry: IndexEntry; score: number }[] = [];
    for (const entry of load.canon.index) {
      const name = entry.name.toLowerCase();
      let score = -1;
      if (name === needle) score = 0;
      else if (name.startsWith(needle)) score = 1;
      else if (name.includes(needle)) score = 2;
      else if (entry.id.includes(needle)) score = 3;
      else if (entry.tags?.some((tag) => tag.toLowerCase().includes(needle))) score = 4;
      if (score >= 0) scored.push({ entry, score });
    }
    scored.sort((a, b) => a.score - b.score || a.entry.name.localeCompare(b.entry.name));
    return scored.slice(0, limit).map((hit) => hit.entry);
  },
}));

export const prefersReducedMotion =
  typeof window !== "undefined" &&
  window.matchMedia("(prefers-reduced-motion: reduce)").matches;
