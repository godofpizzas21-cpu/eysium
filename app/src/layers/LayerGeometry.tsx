/**
 * Layer geometry.
 *
 * Everything here is driven by the manifest: a layer declares geometry kinds
 * and sources, and this module draws them. It knows nothing about which layer
 * it is rendering, so adding a layer needs no change here.
 *
 * The four kinds are exactly what the datasets can support, and the pipeline
 * refuses to emit a manifest promising anything else.
 */
import { useMemo } from "react";
import { BufferGeometry } from "three";

import type { IndexEntry } from "../data/generated/index.js";
import type { LayerBundle, LayerGeometry } from "../data/layers.js";
import { resolveSource } from "../data/layers.js";
import { toVector3 } from "../lib/geo.js";
import { useAtlas } from "../state/store.js";

function token(name: string): string {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim() || "#ffffff";
}

/** A colour spec is either the token name or `palette`, meaning the entity's own. */
function colourFor(spec: string, entry: Record<string, unknown>): string {
  if (spec === "palette") {
    const own = entry.palette;
    return typeof own === "string" ? own : token("--sirocc");
  }
  return token(spec);
}

/* ---------------------------------------------------------------- arc */

/** A route or current, lifted above the surface and drawn as a line. */
function Arc({ path, colour }: { path: { lat: number; lon: number }[]; colour: string }) {
  const geometry = useMemo(() => {
    const points = path.map((point) => toVector3(point, 0.018));
    return new BufferGeometry().setFromPoints(points);
  }, [path]);

  return (
    <line>
      <primitive object={geometry} attach="geometry" />
      <lineBasicMaterial color={colour} transparent opacity={0.85} />
    </line>
  );
}

/* ------------------------------------------------------- latitude band */

/**
 * A climate zone, drawn as the band of sphere between two latitudes.
 *
 * Bands are mirrored into both hemispheres, because canon states them as
 * absolute latitudes rather than signed ones.
 */
function LatitudeBand({
  from,
  to,
  colour,
}: {
  from: number;
  to: number;
  colour: string;
}) {
  const shells = useMemo(() => {
    const toPhi = (lat: number) => ((90 - lat) * Math.PI) / 180;
    return [
      { start: toPhi(to), length: toPhi(from) - toPhi(to) },
      { start: toPhi(-from), length: toPhi(-to) - toPhi(-from) },
    ].filter((shell) => shell.length > 0.001);
  }, [from, to]);

  return (
    <group>
      {shells.map((shell, index) => (
        <mesh key={index}>
          <sphereGeometry args={[1.006, 64, 24, 0, Math.PI * 2, shell.start, shell.length]} />
          <meshBasicMaterial color={colour} transparent opacity={0.42} depthWrite={false} />
        </mesh>
      ))}
    </group>
  );
}

/* -------------------------------------------------------------- point */

/**
 * Shapes carry meaning alongside colour.
 *
 * `eng.design-system` section 7 requires that colour is never the only channel,
 * so each geometry role gets a distinct silhouette that survives any colour
 * vision deficiency and any greyscale print.
 */
export type SymbolShape = "sphere" | "octahedron" | "box" | "cone";

function ShapeGeometry({ shape, radius }: { shape: SymbolShape; radius: number }) {
  if (shape === "octahedron") return <octahedronGeometry args={[radius * 1.25, 0]} />;
  if (shape === "box") return <boxGeometry args={[radius * 1.7, radius * 1.7, radius * 1.7]} />;
  if (shape === "cone") return <coneGeometry args={[radius * 1.3, radius * 2.4, 6]} />;
  return <sphereGeometry args={[radius, 12, 12]} />;
}

function PointSymbol({
  point,
  colour,
  radius,
  id,
  selectable,
  shape,
}: {
  point: { lat: number; lon: number };
  colour: string;
  radius: number;
  id: string;
  selectable: boolean;
  shape: SymbolShape;
}) {
  const select = useAtlas((s) => s.select);
  const hover = useAtlas((s) => s.hover);
  const selectedId = useAtlas((s) => s.selectedId);

  const position = useMemo(() => toVector3(point, 0.014).toArray(), [point]);
  const active = selectedId === id;

  return (
    <group position={position}>
      <mesh>
        <ShapeGeometry shape={shape} radius={radius * (active ? 1.5 : 1)} />
        <meshBasicMaterial color={colour} transparent opacity={active ? 1 : 0.85} />
      </mesh>
      {selectable && (
        <mesh
          onPointerOver={(event) => {
            event.stopPropagation();
            hover(id);
            document.body.style.cursor = "pointer";
          }}
          onPointerOut={() => {
            hover(null);
            document.body.style.cursor = "";
          }}
          onClick={(event) => {
            event.stopPropagation();
            select(id);
          }}
        >
          <sphereGeometry args={[0.03, 8, 8]} />
          <meshBasicMaterial transparent opacity={0} depthWrite={false} />
        </mesh>
      )}
    </group>
  );
}

/* ------------------------------------------------------------ dispatch */

const REGION_FIELDS = ["regions", "bestRegions", "deposits", "biome", "polity"] as const;

/** Scale a symbol by a value, on a cube root so area reads proportionally. */
function scaleRadius(value: number, max: number): number {
  if (!max) return 0.007;
  return 0.005 + 0.014 * Math.cbrt(value / max);
}

function GeometryGroup({
  geometry,
  bundle,
  byId,
}: {
  geometry: LayerGeometry;
  bundle: LayerBundle;
  byId: Map<string, IndexEntry>;
}) {
  const entries = useMemo(
    () => resolveSource(bundle, geometry.source) as Record<string, unknown>[],
    [bundle, geometry.source],
  );

  const maxScale = useMemo(() => {
    if (!geometry.scaleBy) return 0;
    return entries.reduce((max, entry) => {
      const value = entry[geometry.scaleBy!];
      return typeof value === "number" && value > max ? value : max;
    }, 0);
  }, [entries, geometry.scaleBy]);

  const selectable = bundle.manifest.selectable;
  const isSelectable = (id: string) =>
    selectable.some((domain) => id.startsWith(`${domain}.`));

  // A stable shape per source, so a layer's symbols are distinguishable from
  // each other without reading their colour.
  const shape: SymbolShape = geometry.scaleBy
    ? "sphere"
    : geometry.source.includes("species")
      ? "cone"
      : geometry.source.includes("regions") || geometry.source.includes("Potential")
        ? "octahedron"
        : "box";

  return (
    <group>
      {entries.map((entry, index) => {
        const id = typeof entry.id === "string" ? entry.id : `${geometry.source}-${index}`;
        const colour = colourFor(geometry.colour, entry);

        if (geometry.kind === "arc") {
          const path = entry.path as { lat: number; lon: number }[] | undefined;
          if (!path?.length) return null;
          return <Arc key={id} path={path} colour={colour} />;
        }

        if (geometry.kind === "latitude-band") {
          const band = entry.latitudeBandDeg as [number, number] | undefined;
          if (!band) return null;
          return <LatitudeBand key={id} from={band[0]} to={band[1]} colour={colour} />;
        }

        if (geometry.kind === "point") {
          const point = (entry.coordinates ?? entry.labelPoint) as
            | { lat: number; lon: number }
            | undefined;
          if (!point) return null;
          const value = geometry.scaleBy ? Number(entry[geometry.scaleBy] ?? 0) : 0;
          return (
            <PointSymbol
              key={id}
              id={id}
              point={point}
              colour={colour}
              radius={geometry.scaleBy ? scaleRadius(value, maxScale) : 0.007}
              selectable={isSelectable(id)}
              shape={shape}
            />
          );
        }

        // region-point: place the entity at each place it names.
        const targets: string[] = [];
        for (const field of REGION_FIELDS) {
          const value = entry[field];
          if (typeof value === "string") targets.push(value);
          else if (Array.isArray(value)) targets.push(...(value as string[]));
        }

        return (
          <group key={id}>
            {targets.map((target) => {
              const located = byId.get(target);
              if (located?.lat === undefined || located.lon === undefined) return null;
              return (
                <PointSymbol
                  key={`${id}-${target}`}
                  id={id}
                  point={{ lat: located.lat, lon: located.lon }}
                  colour={colour}
                  radius={0.008}
                  selectable={isSelectable(id)}
                  shape={shape}
                />
              );
            })}
          </group>
        );
      })}
    </group>
  );
}

export function LayerGeometryRenderer() {
  const bundle = useAtlas((s) => s.activeLayer());
  const load = useAtlas((s) => s.load);

  if (!bundle || load.status !== "ready") return null;

  return (
    <group>
      {bundle.manifest.geometry.map((geometry, index) => (
        <GeometryGroup
          key={`${geometry.kind}-${geometry.source}-${index}`}
          geometry={geometry}
          bundle={bundle}
          byId={load.canon.byId}
        />
      ))}
    </group>
  );
}
