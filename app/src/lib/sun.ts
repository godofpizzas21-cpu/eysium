/**
 * The sun.
 *
 * Where Helia stands over Elysium at a given date and time, derived from canon
 * rather than approximated: the 19.4-degree axial tilt, the 384.24-day year
 * beginning at the northward equinox, and the 25.9-hour solar day.
 */
import { Vector3 } from "three";

import type { CalendarShape, ElysianDate, ElysianTime } from "./calendar.js";
import { dayOfYear, fractionFromTime } from "./calendar.js";
import { toVector3 } from "./geo.js";

const DEG = Math.PI / 180;

export interface SubsolarPoint {
  lat: number;
  lon: number;
}

/**
 * The point on the surface directly beneath Helia.
 *
 * Declination follows from the tilt and the position in the year: canon fixes
 * the year's start at the northward equinox (`hist.calendar` section 4), so
 * declination is zero on Verane 1 and peaks a quarter-year later.
 */
export function subsolarPoint(
  date: ElysianDate,
  time: ElysianTime,
  shape: CalendarShape,
  axialTiltDeg: number,
): SubsolarPoint {
  const yearFraction = dayOfYear(date, shape) / shape.year.solarYearDays;
  const declination = axialTiltDeg * Math.sin(2 * Math.PI * yearFraction);

  // Midday at longitude 0 means the subsolar longitude runs from +180 at
  // midnight through 0 at midday.
  const dayFraction = fractionFromTime(time, shape);
  const longitude = 180 - dayFraction * 360;

  return { lat: declination, lon: ((longitude + 540) % 360) - 180 };
}

/** A unit vector toward Helia, for lighting the globe. */
export function sunDirection(point: SubsolarPoint, target = new Vector3()): Vector3 {
  return toVector3(point, 0, target).normalize();
}

/**
 * Length of daylight at a latitude, in civil hours.
 *
 * Elysium's gentle 19.4-degree tilt makes seasonal swing mild: the polar night
 * is short and the tropics wide (`planet.climate` section 1).
 */
export function daylightHours(
  latitude: number,
  declination: number,
  shape: CalendarShape,
): number {
  const phi = latitude * DEG;
  const delta = declination * DEG;
  const cosH = -Math.tan(phi) * Math.tan(delta);
  if (cosH <= -1) return shape.clock.hoursPerDay;
  if (cosH >= 1) return 0;
  return (Math.acos(cosH) / Math.PI) * shape.clock.hoursPerDay;
}
