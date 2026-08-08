/**
 * The layer switcher.
 *
 * Reads the generated manifests, so it enumerates nothing itself — adding a
 * layer to the registry adds it here (`eng.architecture` section 3).
 *
 * Number keys 1-9 switch layers; 0 clears. Keyboard access is a requirement,
 * not an enhancement.
 */
import { useEffect } from "react";

import { loadIndicators, loadLayer } from "../data/layers.js";
import { useAtlas } from "../state/store.js";

export function LayerSwitcher() {
  const manifests = useAtlas((s) => s.manifests);
  const activeLayerId = useAtlas((s) => s.activeLayerId);
  const status = useAtlas((s) => s.layerStatus);

  const show = useAtlas((s) => s.showLayer);

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      const target = event.target as HTMLElement | null;
      if (target && /^(INPUT|TEXTAREA)$/.test(target.tagName)) return;

      if (event.key === "0") {
        void show(null);
        return;
      }
      const index = Number(event.key) - 1;
      if (Number.isInteger(index) && index >= 0 && index < manifests.length) {
        void show(manifests[index]!.id);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [manifests, show]);

  if (!manifests.length) return null;

  return (
    <section className="layers" aria-label="Map layers">
      <h2 className="layers__heading">Layers</h2>
      <ul className="layers__list">
        {manifests.map((manifest, index) => {
          const active = manifest.id === activeLayerId;
          return (
            <li key={manifest.id}>
              <button
                type="button"
                className="layers__button"
                aria-pressed={active}
                onClick={() => void show(active ? null : manifest.id)}
              >
                <kbd className="layers__key">{index + 1}</kbd>
                <span className="layers__name">{manifest.name}</span>
                {active && status === "loading" && (
                  <span className="layers__state" role="status">
                    Loading
                  </span>
                )}
              </button>
            </li>
          );
        })}
      </ul>
      <p className="layers__hint">Press a number to switch, 0 to clear.</p>
    </section>
  );
}

/** Load a layer and its indicators, or clear the current one. */
export async function activateLayer(id: string | null) {
  const state = useAtlas.getState();

  if (!id) {
    state.setLayerState({ activeLayerId: null, layerStatus: "idle", layerError: null, indicators: [] });
    return;
  }

  const manifest = state.manifests.find((entry) => entry.id === id);
  if (!manifest) return;

  const cached = state.layers[id];
  if (cached) {
    state.setLayerState({ activeLayerId: id, layerStatus: "ready", layerError: null });
    state.setLayerState({ indicators: await loadIndicators(manifest.indicators ?? []) });
    return;
  }

  state.setLayerState({ activeLayerId: id, layerStatus: "loading", layerError: null, indicators: [] });
  try {
    const [bundle, indicators] = await Promise.all([
      loadLayer(manifest),
      loadIndicators(manifest.indicators ?? []),
    ]);
    useAtlas.getState().cacheLayer(id, bundle);
    useAtlas.getState().setLayerState({ layerStatus: "ready", indicators });
  } catch (error) {
    useAtlas.getState().setLayerState({
      layerStatus: "failed",
      layerError: (error as Error).message,
    });
  }
}
