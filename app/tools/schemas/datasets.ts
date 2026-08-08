/**
 * Schemas for the datasets the Atlas renders directly.
 *
 * Datasets not listed here are still validated: every file must satisfy
 * `DatasetHeader`, and every entity found anywhere inside any file must satisfy
 * the `Entity` envelope. These schemas add the stricter, geometry-aware checks
 * that the renderer depends on.
 */
import { z } from "zod";
import { Entity, LatLon, Path, Ring, Share, dataset, id } from "./common.js";

/* ------------------------------------------------------------------ planet */

export const PlanetPhysical = dataset({
  planet: z
    .object({
      meanRadiusKm: z.number().positive(),
      landFraction: z.number().min(0).max(1),
      siderealDayHours: z.number().positive(),
      solarDayHours: z.number().positive(),
    })
    .passthrough(),
});

/* -------------------------------------------------------------- continents */

const ContinentFeature = Entity.extend({
  type: z.string(),
  labelPoint: LatLon.optional(),
});

const IslandOutline = z.object({
  featureId: id("region"),
  outline: Ring,
});

export const Continents = dataset({
  continents: z
    .array(
      Entity.extend({
        areaMkm2: z.number().positive(),
        landShare: z.number().min(0).max(1),
        outline: Ring.optional(),
        islandOutlines: z.array(IslandOutline).optional(),
        features: z.array(ContinentFeature),
      }),
    )
    .min(1),
});

/* ------------------------------------------------------------------ oceans */

export const Oceans = dataset({
  oceans: z.array(Entity).min(1),
  currents: z.array(Entity.extend({ path: Path })).min(1),
  features: z.array(Entity.extend({ labelPoint: LatLon.optional() })).optional(),
});

/* ------------------------------------------------------------------ cities */

export const Cities = dataset({
  settlement: z
    .object({
      urbanPopulation: z.number().positive(),
      urbanSharePct: Share,
      largestCity: id("city"),
    })
    .passthrough(),
  cities: z
    .array(
      Entity.extend({
        population: z.number().int().positive(),
        polity: id("polity"),
        coordinates: LatLon,
        seatOf: id("gov", "econ").optional(),
      }),
    )
    .min(1),
});

/* ------------------------------------------------------------------ routes */

export const Routes = dataset({
  routes: z
    .array(
      Entity.extend({
        mode: z.string(),
        serviceSpeedKmh: z.number().positive(),
        lengthKm: z.number().positive(),
        stops: z.array(id("city")).min(2),
        path: Path,
        travelTimeCivilHours: z.number().positive().optional(),
      }),
    )
    .min(1),
  launchRanges: z
    .array(Entity.extend({ coordinates: LatLon, capacitySharePct: Share }))
    .min(1),
});

/* ------------------------------------------------------------------ biomes */

const Hex = z.string().regex(/^#[0-9A-Fa-f]{6}$/, "must be a hex colour");

const BiomeEntry = Entity.extend({
  areaMkm2: z.number().nonnegative(),
  palette: Hex,
});

export const Biomes = dataset({
  totals: z
    .object({
      landAreaMkm2: z.number().positive(),
      oceanAreaMkm2: z.number().positive(),
      surfaceAreaMkm2: z.number().positive(),
    })
    .passthrough(),
  terrestrialBiomes: z.array(BiomeEntry).min(1),
  marineRealms: z.array(BiomeEntry).min(1),
  flagshipSpecies: z.array(Entity).min(1),
});

/* ----------------------------------------------------------------- regions */

export const Regions = dataset({
  tiers: z
    .array(Entity.extend({ count: z.number().int().positive() }))
    .length(4),
  regions: z
    .array(
      Entity.extend({
        population: z.number().int().positive(),
        councilSeats: z.number().int().positive(),
        governingForm: id("gov"),
        delegateSelection: id("gov"),
        labelPoint: LatLon.optional(),
      }),
    )
    .min(1),
});

/* ----------------------------------------------------------------- metrics */

export const Metrics = dataset({
  principles: z.array(Entity).min(1),
  indicators: z
    .array(
      Entity.extend({
        value: z.number(),
        unit: z.string(),
        trend: z.string(),
        domain: z.string().min(1),
        sourceDataset: z.string().endsWith(".json").optional(),
        derivation: z.enum(["survey", "composite"]).optional(),
      }).refine(
        (m) => Boolean(m.sourceDataset) !== Boolean(m.derivation),
        "an indicator declares either a sourceDataset or a derivation, never both",
      ),
    )
    .min(1),
  unmeasuredRegister: z
    .object({ entries: z.array(z.string()).min(1) })
    .passthrough(),
});

/* ------------------------------------------------------------------ energy */

export const Energy = dataset({
  demand: z.object({ meanPlanetaryTW: z.number().positive() }).passthrough(),
  generationMix: z
    .array(Entity.extend({ sharePct: Share, outputTW: z.number().nonnegative() }))
    .min(1),
});

/** Datasets with a strict schema, keyed by filename. */
export const STRICT_SCHEMAS: Record<string, z.ZodTypeAny> = {
  "planet-physical.json": PlanetPhysical,
  "continents.json": Continents,
  "oceans.json": Oceans,
  "cities.json": Cities,
  "routes.json": Routes,
  "biomes.json": Biomes,
  "regions.json": Regions,
  "metrics.json": Metrics,
  "energy.json": Energy,
};
