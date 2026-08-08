/**
 * The live region.
 *
 * `eng.design-system` section 7 requires selection changes to be announced
 * politely. This is the one place the Atlas speaks to a screen reader without
 * being asked.
 */
import { useEffect, useState } from "react";
import { useAtlas } from "../state/store.js";

export function Announcer() {
  const entity = useAtlas((s) => s.selectedEntity());
  const layer = useAtlas((s) => s.activeLayer());
  const [message, setMessage] = useState("");

  useEffect(() => {
    if (!entity) return;
    setMessage(`Selected ${entity.name}.`);
  }, [entity]);

  useEffect(() => {
    if (!layer) return;
    setMessage(`${layer.manifest.name} layer shown. ${layer.manifest.summary}`);
  }, [layer]);

  return (
    <p className="visually-hidden" role="status" aria-live="polite" aria-atomic="true">
      {message}
    </p>
  );
}
