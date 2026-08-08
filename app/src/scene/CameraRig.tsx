/**
 * The fly-to camera.
 *
 * The globe rotates under a camera that stays level, rather than the camera
 * flying around the globe: cheaper, steadier, and it keeps the horizon fixed
 * (`eng.design-system` section 5).
 *
 * Reduced motion is honoured by cutting instantly instead of easing.
 */
import { useEffect, useRef } from "react";
import { useFrame, useThree } from "@react-three/fiber";
import { Vector3 } from "three";

import { toVector3 } from "../lib/geo.js";
import { prefersReducedMotion, useAtlas } from "../state/store.js";

/** Cubic ease-out: fast departure, gentle arrival. */
const ease = (t: number) => 1 - Math.pow(1 - t, 3);

const DURATION_MS = 900;

export function CameraRig() {
  const camera = useThree((state) => state.camera);
  const target = useAtlas((s) => s.cameraTarget);

  const from = useRef(new Vector3());
  const to = useRef(new Vector3());
  const startedAt = useRef<number | null>(null);

  useEffect(() => {
    if (!target) return;

    // The point on the surface, pushed out to the requested distance.
    toVector3({ lat: target.lat, lon: target.lon }, 0, to.current)
      .normalize()
      .multiplyScalar(target.distance);

    if (prefersReducedMotion) {
      camera.position.copy(to.current);
      camera.lookAt(0, 0, 0);
      startedAt.current = null;
      return;
    }

    from.current.copy(camera.position);
    startedAt.current = performance.now();
  }, [target, camera]);

  useFrame(() => {
    if (startedAt.current === null) return;

    const elapsed = performance.now() - startedAt.current;
    const t = Math.min(1, elapsed / DURATION_MS);

    // Slerp the direction so the camera arcs over the surface rather than
    // cutting through the planet, and lerp the distance separately.
    const direction = from.current.clone().normalize();
    const destination = to.current.clone().normalize();
    const angle = direction.angleTo(destination);
    const eased = ease(t);

    if (angle > 1e-4) {
      const axis = new Vector3().crossVectors(direction, destination).normalize();
      direction.applyAxisAngle(axis, angle * eased);
    }

    const distance =
      from.current.length() + (to.current.length() - from.current.length()) * eased;

    camera.position.copy(direction.multiplyScalar(distance));
    camera.lookAt(0, 0, 0);

    if (t >= 1) startedAt.current = null;
  });

  return null;
}
