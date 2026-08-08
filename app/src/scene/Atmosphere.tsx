/**
 * Atmosphere and the day/night terminator.
 *
 * The globe is lit by Helia's actual position for the current Elysian date and
 * time, so the terminator tilts with the season and sweeps at the planet's own
 * 25.9-hour rate rather than an Earth day's.
 *
 * The glare rule applies: no bloom, no lens flare, no rim glow. Elysian cities
 * glow rather than glare, and so does this.
 */
import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import { AdditiveBlending, BackSide, type DirectionalLight, Vector3 } from "three";

import { subsolarPoint, sunDirection } from "../lib/sun.js";
import { prefersReducedMotion, useAtlas } from "../state/store.js";

function token(name: string): string {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || "#ffffff";
}

export function Atmosphere() {
  const load = useAtlas((s) => s.load);
  const date = useAtlas((s) => s.date);
  const time = useAtlas((s) => s.time);

  const light = useRef<DirectionalLight>(null);
  const direction = useRef(new Vector3(1, 0, 0));

  const shape = load.status === "ready" ? load.canon.calendar : null;
  const tilt = load.status === "ready" ? load.canon.planet.planet.axialTiltDeg : 19.4;

  const colours = useMemo(
    () => ({ halo: token("--shelf"), night: token("--void") }),
    [],
  );

  useFrame(() => {
    if (!shape || !light.current) return;
    const point = subsolarPoint(date, time, shape, tilt);
    sunDirection(point, direction.current);
    light.current.position.copy(direction.current).multiplyScalar(6);
  });

  return (
    <group>
      {/* Helia. One directional light, warm and not bright. */}
      <directionalLight ref={light} intensity={1.4} color="#FFF3DC" />

      {/* Ambient stands in for scattered skylight, kept low so the night side
          is genuinely dark rather than merely dim. */}
      <ambientLight intensity={0.22} color={colours.night} />

      {/* Atmospheric shell. Additive and very faint — this is a limb, not a
          glow. */}
      <mesh scale={1.045}>
        <sphereGeometry args={[1, 64, 64]} />
        <meshBasicMaterial
          color={colours.halo}
          transparent
          opacity={0.07}
          side={BackSide}
          blending={AdditiveBlending}
          depthWrite={false}
        />
      </mesh>
    </group>
  );
}

/**
 * Advances the clock when it is running.
 *
 * One civil minute per real second by default, so a full Elysian day takes
 * about twenty-six real seconds to watch. Paused under reduced motion.
 */
export function Clock() {
  const carry = useRef(0);

  useFrame((_, delta) => {
    const state = useAtlas.getState();
    if (!state.running || prefersReducedMotion || state.load.status !== "ready") return;

    const shape = state.load.canon.calendar;
    carry.current += delta * 60; // civil minutes per real second

    if (carry.current < 1) return;
    const minutes = Math.floor(carry.current);
    carry.current -= minutes;

    const perDay = shape.clock.hoursPerDay * shape.clock.minutesPerHour;
    let total = state.time.hour * shape.clock.minutesPerHour + state.time.minute + minutes;

    if (total >= perDay) {
      const days = Math.floor(total / perDay);
      total %= perDay;
      void import("../lib/calendar.js").then(({ addDays }) => {
        useAtlas.getState().setDate(addDays(useAtlas.getState().date, days, shape));
      });
    }

    state.setTime({
      hour: Math.floor(total / shape.clock.minutesPerHour),
      minute: total % shape.clock.minutesPerHour,
      beat: 0,
    });
  });

  return null;
}
