/**
 * Shared schema primitives for the Elysium Atlas data layer.
 *
 * These encode the rules in `charter.data-schema` and `charter.canon-rules`
 * directly, so a dataset that violates the charter fails the build rather than
 * reaching the application.
 */
import { z } from "zod";

/** Registered ID domains, from `charter.data-schema` section 3. */
export const ID_DOMAINS = [
  "charter", "planet", "region", "ocean", "climate", "biome", "clade",
  "species", "resource", "hist", "cal", "demo", "lang", "cult", "gov",
  "polity", "law", "econ", "ind", "energy", "env", "edu", "res", "health",
  "city", "route", "agri", "mil", "ai", "space", "dipl", "metric", "eng",
] as const;

export type IdDomain = (typeof ID_DOMAINS)[number];

const SLUG = "[a-z0-9]+(?:-[a-z0-9]+)*";

/**
 * A canonical namespaced identifier: `<domain>.<kebab-slug>`.
 *
 * Optionally constrained to particular domains, so a field that must hold a
 * city cannot be given a route.
 */
export const id = (...domains: IdDomain[]) => {
  const allowed = domains.length ? domains : ID_DOMAINS;
  const pattern = new RegExp(`^(${allowed.join("|")})\\.${SLUG}$`);
  return z
    .string()
    .regex(
      pattern,
      `must be a canonical id in ${
        domains.length ? domains.join(" or ") : "a registered domain"
      }`,
    );
};

/** Any canonical identifier, unconstrained by domain. */
export const AnyId = id();

/**
 * The standard entity envelope from `charter.data-schema` section 2.
 *
 * Every entity in every dataset carries these fields. Datasets extend it;
 * nothing replaces it.
 */
export const Entity = z.object({
  id: AnyId,
  name: z.string().min(1),
  summary: z.string(),
  sources: z.array(z.string().min(1)).min(1),
  tags: z.array(z.string()).optional(),
});

export type Entity = z.infer<typeof Entity>;

/** A point in decimal degrees. Latitude is clamped; longitude is not, because
 *  antimeridian-spanning geometry may exceed +/-180 for ring continuity. */
export const LatLon = z.object({
  lat: z.number().min(-90).max(90),
  lon: z.number(),
});

export type LatLon = z.infer<typeof LatLon>;

/** A path: an ordered list of points, already great-circle interpolated in the
 *  dataset so the renderer lifts and draws rather than re-interpolating. */
export const Path = z.array(LatLon).min(2);

/** A polygon ring in GeoJSON `[lon, lat]` order — the one deliberate exception
 *  to the object form, per `charter.data-schema` section 5. */
export const Ring = z
  .array(z.tuple([z.number(), z.number()]))
  .min(3);

/** Every dataset file carries this header. */
export const DatasetHeader = z.object({
  schemaVersion: z.string().regex(/^\d+\.\d+\.\d+$/),
  dataVersion: z.string().regex(/^\d+\.\d+\.\d+$/),
  id: AnyId,
  name: z.string().min(1),
  summary: z.string().min(1),
  sources: z.array(z.string().min(1)).min(1),
  asOf: z.string().optional(),
  units: z.record(z.unknown()).optional(),
});

/** A percentage share. */
export const Share = z.number().min(0).max(100);

/** Extend the dataset header with dataset-specific fields. */
export const dataset = <T extends z.ZodRawShape>(shape: T) =>
  DatasetHeader.extend(shape).passthrough();
