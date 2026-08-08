/**
 * Cloud shell.
 *
 * A procedural band structure rather than a texture: Elysium's circulation is
 * canon (`planet.climate` section 2), so the clouds follow it — a bright ITCZ
 * band migrating with the season, dry subtropical belts at the Hadley descent
 * near 34-38 degrees, and broad mid-latitude storm cloud in the Ferrel belt.
 *
 * The shell drifts westward slowly. Under reduced motion it does not move.
 */
import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import { CanvasTexture, type Mesh } from "three";

import { prefersReducedMotion, useAtlas } from "../state/store.js";

/** Build a banded alpha map from the canonical circulation latitudes. */
function buildCloudTexture(itczLatitude: number): CanvasTexture {
  const width = 512;
  const height = 256;
  const canvas = document.createElement("canvas");
  canvas.width = width;
  canvas.height = height;
  const context = canvas.getContext("2d");
  if (!context) throw new Error("Could not create the cloud texture.");

  const image = context.createImageData(width, height);

  /** Cloud density by latitude, following the three-cell circulation. */
  const density = (lat: number): number => {
    const itcz = Math.exp(-(((lat - itczLatitude) / 7) ** 2)) * 0.95;
    const hadleyDry = Math.exp(-(((Math.abs(lat) - 36) / 9) ** 2)) * 0.55;
    const ferrel = Math.exp(-(((Math.abs(lat) - 52) / 14) ** 2)) * 0.7;
    const polar = Math.exp(-(((Math.abs(lat) - 78) / 10) ** 2)) * 0.3;
    return Math.max(0, itcz + ferrel + polar - hadleyDry);
  };

  // Cheap value noise, deterministic so the planet looks the same each visit.
  const hash = (x: number, y: number) => {
    const n = Math.sin(x * 127.1 + y * 311.7) * 43758.5453;
    return n - Math.floor(n);
  };
  const noise = (x: number, y: number) => {
    const xi = Math.floor(x);
    const yi = Math.floor(y);
    const xf = x - xi;
    const yf = y - yi;
    const smooth = (t: number) => t * t * (3 - 2 * t);
    const a = hash(xi, yi);
    const b = hash(xi + 1, yi);
    const c = hash(xi, yi + 1);
    const d = hash(xi + 1, yi + 1);
    const u = smooth(xf);
    const v = smooth(yf);
    return a * (1 - u) * (1 - v) + b * u * (1 - v) + c * (1 - u) * v + d * u * v;
  };

  for (let y = 0; y < height; y += 1) {
    const lat = 90 - (y / height) * 180;
    const band = density(lat);
    for (let x = 0; x < width; x += 1) {
      const u = (x / width) * 12;
      const v = (y / height) * 6;
      const detail = noise(u, v) * 0.6 + noise(u * 2.7, v * 2.7) * 0.3 + noise(u * 6, v * 6) * 0.1;
      const alpha = Math.max(0, Math.min(1, band * (detail * 1.5 - 0.35))) * 255;
      const index = (y * width + x) * 4;
      image.data[index] = 255;
      image.data[index + 1] = 255;
      image.data[index + 2] = 255;
      image.data[index + 3] = alpha;
    }
  }

  context.putImageData(image, 0, 0);
  const texture = new CanvasTexture(canvas);
  texture.anisotropy = 4;
  return texture;
}

export function Clouds() {
  const shell = useRef<Mesh>(null);
  const load = useAtlas((s) => s.load);
  const date = useAtlas((s) => s.date);

  /**
   * The ITCZ migrates between about 9 degrees south and 9 degrees north over
   * the year — a narrower swing than Earth's, because of the gentle tilt.
   */
  const itcz = useMemo(() => {
    if (load.status !== "ready") return 0;
    const shape = load.canon.calendar;
    const fraction =
      ((date.month - 1) * shape.year.daysPerMonth + date.day - 1) / shape.year.solarYearDays;
    return 9 * Math.sin(2 * Math.PI * fraction);
  }, [load, date]);

  const texture = useMemo(() => buildCloudTexture(itcz), [itcz]);

  useFrame((_, delta) => {
    if (!shell.current || prefersReducedMotion) return;
    // Slow westward drift, ambient rather than simulated.
    shell.current.rotation.y -= delta * 0.006;
  });

  return (
    <mesh ref={shell} scale={1.012}>
      <sphereGeometry args={[1, 64, 64]} />
      <meshStandardMaterial
        map={texture}
        transparent
        opacity={0.5}
        roughness={1}
        metalness={0}
        depthWrite={false}
      />
    </mesh>
  );
}
