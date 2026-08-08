/**
 * Space mode.
 *
 * Elysium, its two moons, and the orbital shells, all at true relative scale
 * against the planet's own radius: one render unit is 6,510 km. Kalyra really
 * does sit 61.75 radii out, and Vesper really is small and fast.
 *
 * The Tyrran Belt is not drawn. At 2.3 AU it lies about 52,800 render units
 * away — four orders of magnitude beyond Kalyra — and any diagram placing it in
 * view would be a lie about distance. It is reported in the panel instead.
 */
import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import { BufferGeometry, type Group, Vector3 } from "three";

import type { CalendarShape, ElysianDate, ElysianTime } from "../lib/calendar.js";
import { dayOfYear, fractionFromTime } from "../lib/calendar.js";
import { useAtlas } from "../state/store.js";

function token(name: string): string {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || "#ffffff";
}

export interface Moon {
  id: string;
  name: string;
  meanRadiusKm: number;
  orbitalDistanceKm: number;
  orbitalPeriodElysianDays: number;
}

/** A circle in the equatorial plane, drawn as a line. */
function OrbitRing({ radius, colour, opacity }: { radius: number; colour: string; opacity: number }) {
  const geometry = useMemo(() => {
    const points: Vector3[] = [];
    for (let i = 0; i <= 128; i += 1) {
      const angle = (i / 128) * Math.PI * 2;
      points.push(new Vector3(Math.cos(angle) * radius, 0, Math.sin(angle) * radius));
    }
    return new BufferGeometry().setFromPoints(points);
  }, [radius]);

  return (
    <line>
      <primitive object={geometry} attach="geometry" />
      <lineBasicMaterial color={colour} transparent opacity={opacity} />
    </line>
  );
}

/** Elapsed Elysian days since EY 0, used to place the moons in their orbits. */
function elapsedDays(date: ElysianDate, time: ElysianTime, shape: CalendarShape): number {
  return (
    date.year * shape.year.solarYearDays + dayOfYear(date, shape) + fractionFromTime(time, shape)
  );
}

function MoonBody({
  moon,
  planetRadiusKm,
  days,
}: {
  moon: Moon;
  planetRadiusKm: number;
  days: number;
}) {
  const group = useRef<Group>(null);
  const select = useAtlas((s) => s.select);
  const hover = useAtlas((s) => s.hover);
  const selectedId = useAtlas((s) => s.selectedId);

  const distance = moon.orbitalDistanceKm / planetRadiusKm;
  // Bodies are drawn at true relative size, with a floor so Vesper stays
  // clickable rather than becoming a pixel.
  const radius = Math.max(moon.meanRadiusKm / planetRadiusKm, 0.05);
  const active = selectedId === moon.id;

  useFrame(() => {
    if (!group.current) return;
    const angle = (days / moon.orbitalPeriodElysianDays) * Math.PI * 2;
    group.current.position.set(Math.cos(angle) * distance, 0, Math.sin(angle) * distance);
  });

  return (
    <group ref={group}>
      <mesh
        onPointerOver={(event) => {
          event.stopPropagation();
          hover(moon.id);
          document.body.style.cursor = "pointer";
        }}
        onPointerOut={() => {
          hover(null);
          document.body.style.cursor = "";
        }}
        onClick={(event) => {
          event.stopPropagation();
          select(moon.id);
        }}
      >
        <sphereGeometry args={[radius * (active ? 1.3 : 1), 32, 32]} />
        <meshStandardMaterial color={token("--sirocc")} roughness={0.95} metalness={0} />
      </mesh>
    </group>
  );
}

export function OrbitalSystem() {
  const load = useAtlas((s) => s.load);
  const date = useAtlas((s) => s.date);
  const time = useAtlas((s) => s.time);
  const bundle = useAtlas((s) => s.activeLayer());

  const isSpace = bundle?.manifest.view === "space";

  const moons = useMemo<Moon[]>(() => {
    if (!bundle) return [];
    const physical = bundle.data["planet-physical.json"] as { moons?: Moon[] } | undefined;
    return physical?.moons ?? [];
  }, [bundle]);

  const stationary = useMemo(() => {
    if (!bundle || load.status !== "ready") return null;
    const space = bundle.data["space.json"] as
      | { orbitalMechanics?: { stationaryOrbitAltitudeKm: number } }
      | undefined;
    const altitude = space?.orbitalMechanics?.stationaryOrbitAltitudeKm;
    if (!altitude) return null;
    const radiusKm = load.canon.planet.planet.meanRadiusKm;
    return (altitude + radiusKm) / radiusKm;
  }, [bundle, load]);

  if (!isSpace || load.status !== "ready") return null;

  const planetRadiusKm = load.canon.planet.planet.meanRadiusKm;
  const shape = load.canon.calendar;
  const days = elapsedDays(date, time, shape);

  return (
    <group>
      {/* The Low Ring: habitats and industry in low orbit. Drawn as a shell
          rather than 3,400 objects, which would be noise at this scale. */}
      <mesh scale={1.06}>
        <sphereGeometry args={[1, 48, 48]} />
        <meshBasicMaterial color={token("--shelf")} wireframe transparent opacity={0.06} />
      </mesh>

      {stationary && <OrbitRing radius={stationary} colour={token("--shelf")} opacity={0.4} />}

      {moons.map((moon) => (
        <group key={moon.id}>
          <OrbitRing
            radius={moon.orbitalDistanceKm / planetRadiusKm}
            colour={token("--ice")}
            opacity={0.18}
          />
          <MoonBody moon={moon} planetRadiusKm={planetRadiusKm} days={days} />
        </group>
      ))}
    </group>
  );
}
