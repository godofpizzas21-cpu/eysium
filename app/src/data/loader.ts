/**
 * Dataset loading.
 *
 * The eager set is fetched before first paint; everything else is fetched by
 * the layer that needs it and cached. See `eng.data-pipeline` section 4.
 */
import type { EntityIndex, IndexEntry } from "./generated/index.js";
import type { CalendarShape } from "../lib/calendar.js";

const BASE = `${import.meta.env.BASE_URL}data`;
const cache = new Map<string, unknown>();

/** Fetch a canon dataset once and cache it. */
export async function loadDataset<T = unknown>(file: string): Promise<T> {
  const cached = cache.get(file);
  if (cached) return cached as T;

  const response = await fetch(`${BASE}/${file}`);
  if (!response.ok) {
    // Errors state what happened and what to do. They do not apologise.
    throw new Error(`Could not load ${file} (${response.status}). Reload to try again.`);
  }
  const data = (await response.json()) as T;
  cache.set(file, data);
  return data;
}

export interface Canon {
  index: IndexEntry[];
  byId: Map<string, IndexEntry>;
  planet: PlanetPhysical;
  continents: ContinentsData;
  cities: CitiesData;
  calendar: CalendarShape;
}

export interface City {
  id: string;
  name: string;
  summary: string;
  tags?: string[];
  population: number;
  polity: string;
  coordinates: { lat: number; lon: number };
  seatOf?: string;
}

export interface CitiesData {
  cities: City[];
}

export interface PlanetPhysical {
  planet: {
    meanRadiusKm: number;
    landFraction: number;
    siderealDayHours: number;
    solarDayHours: number;
    axialTiltDeg: number;
  };
}

export interface ContinentFeature {
  id: string;
  name: string;
  summary: string;
  type: string;
  labelPoint?: { lat: number; lon: number };
}

export interface Continent {
  id: string;
  name: string;
  summary: string;
  areaMkm2: number;
  /** Derived at build time from the biomes canon places on this continent. */
  derivedPalette?: string;
  outline?: [number, number][];
  islandOutlines?: { featureId: string; outline: [number, number][] }[];
  features: ContinentFeature[];
}

export interface ContinentsData {
  continents: Continent[];
}

/** Load the eager set: everything needed before the globe can be drawn. */
export async function loadCanon(): Promise<Canon> {
  const [indexFile, planet, continents, cities, calendar] = await Promise.all([
    loadDataset<EntityIndex>("entity-index.json"),
    loadDataset<PlanetPhysical>("planet-physical.json"),
    loadDataset<ContinentsData>("continents.json"),
    loadDataset<CitiesData>("cities.json"),
    loadDataset<CalendarShape>("calendar.json"),
  ]);

  const byId = new Map<string, IndexEntry>();
  for (const entry of indexFile.entities) byId.set(entry.id, entry);

  return { index: indexFile.entities, byId, planet, continents, cities, calendar };
}
