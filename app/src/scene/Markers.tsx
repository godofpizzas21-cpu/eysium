/**
 * City markers.
 *
 * Each marker carries an invisible hit sphere considerably larger than its
 * visible dot, so pointer targets meet the 44 px floor in
 * `eng.design-system` section 7 even when the globe is zoomed out.
 */
import { useMemo } from "react";
import { Color } from "three";

import type { City } from "../data/loader.js";
import { toVector3 } from "../lib/geo.js";
import { useAtlas } from "../state/store.js";

function token(name: string): string {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || "#ffffff";
}

/** Seats of the distributed capital are drawn a little larger. */
const isSeat = (city: City) => Boolean(city.seatOf) || city.id === "city.andrivar";

function Marker({ city }: { city: City }) {
  const select = useAtlas((s) => s.select);
  const hover = useAtlas((s) => s.hover);
  const selectedId = useAtlas((s) => s.selectedId);
  const hoveredId = useAtlas((s) => s.hoveredId);

  const position = useMemo(
    () => toVector3(city.coordinates, 0.012).toArray(),
    [city.coordinates],
  );

  const active = selectedId === city.id;
  const warm = hoveredId === city.id;
  const seat = isSeat(city);

  const colour = useMemo(() => {
    const base = new Color(token(seat ? "--ice" : "--sirocc"));
    return active ? base : base.multiplyScalar(warm ? 0.95 : 0.8);
  }, [seat, active, warm]);

  const radius = (seat ? 0.011 : 0.007) * (active ? 1.5 : warm ? 1.2 : 1);

  return (
    <group position={position}>
      <mesh>
        <sphereGeometry args={[radius, 12, 12]} />
        <meshBasicMaterial color={colour} />
      </mesh>
      {/* Hit target, invisible and deliberately generous. */}
      <mesh
        onPointerOver={(event) => {
          event.stopPropagation();
          hover(city.id);
          document.body.style.cursor = "pointer";
        }}
        onPointerOut={() => {
          hover(null);
          document.body.style.cursor = "";
        }}
        onClick={(event) => {
          event.stopPropagation();
          select(city.id);
        }}
      >
        <sphereGeometry args={[0.032, 8, 8]} />
        <meshBasicMaterial transparent opacity={0} depthWrite={false} />
      </mesh>
    </group>
  );
}

export function Markers() {
  const load = useAtlas((s) => s.load);
  if (load.status !== "ready") return null;

  return (
    <group>
      {load.canon.cities.cities.map((city) => (
        <Marker key={city.id} city={city} />
      ))}
    </group>
  );
}
