/**
 * Projects the hovered entity's position to screen space each frame and moves
 * the DOM label. Nothing is stored, so this costs no re-renders.
 */
import { useFrame, useThree } from "@react-three/fiber";
import { useRef } from "react";
import { Vector3 } from "three";

import { positionLabel } from "../lib/hoverLabel.js";
import { toVector3 } from "../lib/geo.js";
import { useAtlas } from "../state/store.js";

export function HoverLabel() {
  const { camera, size, scene } = useThree();
  const projected = useRef(new Vector3());
  const shown = useRef<string | null>(null);

  useFrame(() => {
    const state = useAtlas.getState();
    const id = state.hoveredId;

    if (!id || state.load.status !== "ready") {
      if (shown.current !== null) {
        positionLabel(null);
        shown.current = null;
      }
      return;
    }

    const point = state.locate(id);
    if (!point) {
      positionLabel(null);
      shown.current = null;
      return;
    }

    // Follow the globe's own rotation so the label tracks the surface.
    toVector3(point, 0.05, projected.current).applyQuaternion(scene.quaternion);
    const world = projected.current.clone().applyMatrix4(scene.matrixWorld);

    // Hide labels on the far side of the planet.
    const toCamera = camera.position.clone().sub(world).normalize();
    if (world.clone().normalize().dot(toCamera) < 0) {
      positionLabel(null);
      shown.current = null;
      return;
    }

    world.project(camera);
    positionLabel(
      {
        x: (world.x * 0.5 + 0.5) * size.width,
        y: (-world.y * 0.5 + 0.5) * size.height,
      },
      shown.current === id ? undefined : (state.load.canon.byId.get(id)?.name ?? id),
    );
    shown.current = id;
  });

  return null;
}
