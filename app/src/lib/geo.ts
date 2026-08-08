/**
 * Geographic conversion.
 *
 * Canon stores degrees; the renderer needs vectors. All conversion happens
 * here and nowhere else, per `charter.canonical-units` section 5: the planet is
 * one render unit in radius, and angles are converted at the Three.js boundary
 * by these functions rather than ad hoc.
 */
import { Vector3 } from "three";

/** Planet radius in render units. Canon fixes this at 1.0. */
export const PLANET_RADIUS = 1;

export interface LatLon {
  lat: number;
  lon: number;
}

const DEG = Math.PI / 180;

/**
 * Convert a canonical point to a position on the sphere.
 *
 * `altitude` is a multiple of the planet radius, so 0 sits on the surface and
 * 0.02 floats a marker just above it.
 */
export function toVector3(point: LatLon, altitude = 0, target = new Vector3()): Vector3 {
  const phi = (90 - point.lat) * DEG;
  const theta = (point.lon + 180) * DEG;
  const r = PLANET_RADIUS + altitude;
  return target.set(
    -r * Math.sin(phi) * Math.cos(theta),
    r * Math.cos(phi),
    r * Math.sin(phi) * Math.sin(theta),
  );
}

/** Convert a position back to canonical degrees. */
export function toLatLon(position: Vector3): LatLon {
  const r = position.length();
  return {
    lat: 90 - Math.acos(position.y / r) / DEG,
    lon: ((Math.atan2(position.z, -position.x) / DEG) % 360) - 180,
  };
}

/**
 * Normalise a ring's longitudes so consecutive vertices never jump more than
 * 180 degrees.
 *
 * `charter.data-schema` section 5 permits rings crossing the antimeridian to
 * exceed +/-180 for continuity, and requires normalisation at render time.
 */
export function unwrapRing(ring: readonly (readonly [number, number])[]): [number, number][] {
  const out: [number, number][] = [];
  let previous: number | undefined;
  for (const [lon, lat] of ring) {
    let value = lon;
    if (previous !== undefined) {
      while (value - previous > 180) value -= 360;
      while (previous - value > 180) value += 360;
    }
    out.push([value, lat]);
    previous = value;
  }
  return out;
}

/** Great-circle distance in kilometres, given the planet's real radius. */
export function greatCircleKm(a: LatLon, b: LatLon, planetRadiusKm: number): number {
  const dLat = (b.lat - a.lat) * DEG;
  const dLon = (b.lon - a.lon) * DEG;
  const h =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(a.lat * DEG) * Math.cos(b.lat * DEG) * Math.sin(dLon / 2) ** 2;
  return planetRadiusKm * 2 * Math.asin(Math.sqrt(h));
}

/**
 * Subdivide a polygon ring so its edges follow the sphere rather than cutting
 * through it. Long edges on a coarse outline would otherwise sink below the
 * surface.
 */
export function densifyRing(
  ring: readonly [number, number][],
  maxSegmentDegrees = 4,
): [number, number][] {
  const out: [number, number][] = [];
  for (let i = 0; i < ring.length; i += 1) {
    const start = ring[i]!;
    const end = ring[(i + 1) % ring.length]!;
    const span = Math.max(Math.abs(end[0] - start[0]), Math.abs(end[1] - start[1]));
    const steps = Math.max(1, Math.ceil(span / maxSegmentDegrees));
    for (let step = 0; step < steps; step += 1) {
      const t = step / steps;
      out.push([start[0] + (end[0] - start[0]) * t, start[1] + (end[1] - start[1]) * t]);
    }
  }
  return out;
}
