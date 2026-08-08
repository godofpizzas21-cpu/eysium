/**
 * The globe.
 *
 * Renders Elysium as a unit sphere with continent geometry lifted from canon.
 * Colours come from the token file, which is itself generated from
 * `data/biomes.json` — the palette is read from canon, not chosen.
 */
import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import earcut from "earcut";
import {
  BackSide,
  BufferAttribute,
  BufferGeometry,
  Color,
  type Group,
  Vector3,
} from "three";

import type { Continent, ContinentsData } from "../data/loader.js";
import { densifyRing, toVector3, unwrapRing } from "../lib/geo.js";
import { prefersReducedMotion, useAtlas } from "../state/store.js";

/** Read a token from the stylesheet so the scene and the DOM share one palette. */
function token(name: string): string {
  if (typeof window === "undefined") return "#ffffff";
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || "#ffffff";
}

/**
 * Build a filled mesh for one polygon ring, projected onto the sphere.
 *
 * The ring is unwrapped across the antimeridian, densified so its edges follow
 * the surface rather than cutting through it, then tessellated in lon/lat space
 * before projection.
 */
function ringGeometry(ring: readonly [number, number][], altitude: number): BufferGeometry {
  const unwrapped = unwrapRing(ring);
  const dense = densifyRing(unwrapped);

  const flat: number[] = [];
  for (const [lon, lat] of dense) flat.push(lon, lat);
  const indices = earcut(flat);

  const positions = new Float32Array(dense.length * 3);
  const scratch = new Vector3();
  dense.forEach(([lon, lat], i) => {
    toVector3({ lat, lon }, altitude, scratch);
    positions.set([scratch.x, scratch.y, scratch.z], i * 3);
  });

  const geometry = new BufferGeometry();
  geometry.setAttribute("position", new BufferAttribute(positions, 3));
  geometry.setIndex(indices);
  geometry.computeVertexNormals();
  return geometry;
}

interface LandmassProps {
  continent: Continent;
  colour: string;
}

function Landmass({ continent, colour }: LandmassProps) {
  const select = useAtlas((s) => s.select);
  const hover = useAtlas((s) => s.hover);
  const selectedId = useAtlas((s) => s.selectedId);
  const hoveredId = useAtlas((s) => s.hoveredId);

  const rings = useMemo(() => {
    const all: { key: string; geometry: BufferGeometry }[] = [];
    if (continent.outline) {
      all.push({ key: continent.id, geometry: ringGeometry(continent.outline, 0.004) });
    }
    for (const island of continent.islandOutlines ?? []) {
      all.push({ key: island.featureId, geometry: ringGeometry(island.outline, 0.004) });
    }
    return all;
  }, [continent]);

  const active = selectedId === continent.id;
  const warm = hoveredId === continent.id;
  const base = useMemo(() => new Color(colour), [colour]);
  const shade = useMemo(() => {
    const c = base.clone();
    if (active) c.lerp(new Color(token("--ice")), 0.28);
    else if (warm) c.lerp(new Color(token("--ice")), 0.12);
    return c;
  }, [base, active, warm]);

  return (
    <group
      onPointerOver={(event) => {
        event.stopPropagation();
        hover(continent.id);
        document.body.style.cursor = "pointer";
      }}
      onPointerOut={() => {
        hover(null);
        document.body.style.cursor = "";
      }}
      onClick={(event) => {
        event.stopPropagation();
        select(continent.id);
      }}
    >
      {rings.map(({ key, geometry }) => (
        <mesh key={key} geometry={geometry}>
          {/* Matte. The glare rule forbids bloom and specular highlights. */}
          <meshStandardMaterial color={shade} roughness={0.95} metalness={0} />
        </mesh>
      ))}
    </group>
  );
}

export function Globe() {
  const group = useRef<Group>(null);
  const load = useAtlas((s) => s.load);
  const autoRotate = useAtlas((s) => s.autoRotate);

  const palette = useMemo(
    () => ({
      ocean: token("--abyss"),
      land: token("--phyllocyanin"),
      halo: token("--shelf"),
    }),
    [],
  );

  useFrame((_, delta) => {
    if (!group.current || !autoRotate || prefersReducedMotion) return;
    // Ambient orientation only, and slower than before: since Phase 22 the
    // terminator carries the sense of time, so the globe need not spin to
    // suggest it.
    group.current.rotation.y += delta * 0.02;
  });

  const continents: ContinentsData["continents"] =
    load.status === "ready" ? load.canon.continents.continents : [];

  return (
    <group ref={group}>
      {/* Ocean sphere. */}
      <mesh>
        <sphereGeometry args={[1, 96, 96]} />
        <meshStandardMaterial color={palette.ocean} roughness={0.9} metalness={0} />
      </mesh>

      {/* Atmospheric halo: a back-faced shell, deliberately faint. */}
      <mesh scale={1.035}>
        <sphereGeometry args={[1, 48, 48]} />
        <meshBasicMaterial color={palette.halo} transparent opacity={0.08} side={BackSide} />
      </mesh>

      {continents.map((continent) => (
        <Landmass key={continent.id} continent={continent} colour={palette.land} />
      ))}
    </group>
  );
}
