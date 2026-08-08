/**
 * Orbit controls.
 *
 * Three's own OrbitControls rather than a helper library: drei's barrel import
 * pulled roughly 750 kB of helpers we do not use into the renderer chunk. This
 * is forty lines and one import.
 */
import { useEffect, useRef } from "react";
import { extend, useFrame, useThree } from "@react-three/fiber";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

import { useAtlas } from "../state/store.js";

extend({ OrbitControls });

interface ControlsProps {
  onStart?: () => void;
}

/**
 * Camera envelopes. Space mode must hold Kalyra at 61.75 planet radii, so the
 * far limit opens up; surface mode keeps the globe filling the frame.
 */
const ENVELOPE = {
  surface: { min: 1.4, max: 6 },
  space: { min: 1.4, max: 90 },
} as const;

export function Controls({ onStart }: ControlsProps) {
  const camera = useThree((state) => state.camera);
  const gl = useThree((state) => state.gl);
  const controls = useRef<OrbitControls | null>(null);
  const view = useAtlas((s) => s.activeLayer()?.manifest.view ?? "surface");

  useEffect(() => {
    const instance = controls.current;
    if (!instance) return;
    const envelope = ENVELOPE[view];
    instance.minDistance = envelope.min;
    instance.maxDistance = envelope.max;
    // Pull back far enough to see the system when entering space mode.
    if (view === "space" && camera.position.length() < 20) {
      camera.position.setLength(24);
    } else if (view === "surface" && camera.position.length() > 6) {
      camera.position.setLength(2.9);
    }
  }, [view, camera]);

  useEffect(() => {
    const instance = new OrbitControls(camera, gl.domElement);
    instance.enablePan = false;
    instance.minDistance = ENVELOPE.surface.min;
    instance.maxDistance = ENVELOPE.space.max;
    instance.rotateSpeed = 0.5;
    instance.zoomSpeed = 0.7;
    instance.enableDamping = true;
    instance.dampingFactor = 0.08;
    // Keyboard control is a requirement, not an enhancement: arrow keys must
    // move the globe for anyone who cannot use a pointer.
    instance.listenToKeyEvents(window);
    controls.current = instance;

    const handleStart = () => onStart?.();
    instance.addEventListener("start", handleStart);

    return () => {
      instance.removeEventListener("start", handleStart);
      instance.dispose();
      controls.current = null;
    };
  }, [camera, gl, onStart]);

  useFrame(() => {
    controls.current?.update();
  });

  return null;
}
