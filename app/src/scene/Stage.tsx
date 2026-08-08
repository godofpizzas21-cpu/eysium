/**
 * The WebGL stage, loaded on demand.
 *
 * Three.js would breach the initial-JS budget in `eng.design-system` section 6,
 * so it is lazy: the accessible interface — which is the real document — paints
 * first, and the globe streams in behind it. If WebGL never arrives, the Atlas
 * still works.
 */
import { Suspense, lazy, useCallback, useEffect, useRef } from "react";
import { registerLabelElement } from "../lib/hoverLabel.js";
import { useAtlas } from "../state/store.js";

const Scene = lazy(async () => {
  const [
    { Canvas },
    { Globe },
    { Controls },
    { Markers },
    { CameraRig },
    { LayerGeometryRenderer },
    { HoverLabel },
    { Atmosphere, Clock },
    { Clouds },
    { OrbitalSystem },
    { Starfield },
  ] = await Promise.all([
    import("@react-three/fiber"),
    import("./Globe.js"),
    import("./Controls.js"),
    import("./Markers.js"),
    import("./CameraRig.js"),
    import("../layers/LayerGeometry.js"),
    import("./HoverLabel.js"),
    import("./Atmosphere.js"),
    import("./Clouds.js"),
    import("./OrbitalSystem.js"),
    import("./Starfield.js"),
  ]);

  return {
    default: function Scene({ onInteract }: { onInteract: () => void }) {
      return (
        <Canvas camera={{ position: [0, 0.6, 2.9], fov: 42 }} dpr={[1, 2]}>
          <Starfield />
          <Atmosphere />
          <Clock />
          <Globe />
          <Clouds />
          <OrbitalSystem />
          <Markers />
          <LayerGeometryRenderer />
          <HoverLabel />
          <CameraRig />
          <Controls onStart={onInteract} />
        </Canvas>
      );
    },
  };
});

export function Stage() {
  const setAutoRotate = useAtlas((s) => s.setAutoRotate);
  const onInteract = useCallback(() => setAutoRotate(false), [setAutoRotate]);

  const label = useRef<HTMLDivElement>(null);
  useEffect(() => {
    registerLabelElement(label.current);
    return () => registerLabelElement(null);
  }, []);

  return (
    <div className="stage" aria-hidden="true">
      <Suspense fallback={<div className="stage__pending" />}>
        <Scene onInteract={onInteract} />
      </Suspense>
      {/* Real DOM text rather than a texture, so it scales with the user's
          font size. Hidden from assistive technology like the canvas. */}
      <div ref={label} className="hoverLabel" data-visible="false" />
    </div>
  );
}
