import { useEffect } from "react";

import { Stage } from "./scene/Stage.js";
import { AccessibleAtlas } from "./a11y/AccessibleAtlas.js";
import { Announcer } from "./a11y/Announcer.js";
import { Shortcuts } from "./a11y/Shortcuts.js";
import { ErrorBoundary } from "./a11y/ErrorBoundary.js";
import { EntityPanel } from "./panels/EntityPanel.js";
import { Search } from "./panels/Search.js";
import { LayerSwitcher, activateLayer } from "./panels/LayerSwitcher.js";
import { Legend } from "./panels/Legend.js";
import { ClockPanel } from "./panels/ClockPanel.js";
import { loadCanon } from "./data/loader.js";
import { loadManifests } from "./data/layers.js";
import { entityFromUrl, onUrlChange, writeEntityToUrl } from "./lib/url.js";
import { prefersReducedMotion, useAtlas } from "./state/store.js";

export default function App() {
  const load = useAtlas((s) => s.load);
  const setLoad = useAtlas((s) => s.setLoad);
  const setAutoRotate = useAtlas((s) => s.setAutoRotate);
  const selectedId = useAtlas((s) => s.selectedId);
  const select = useAtlas((s) => s.select);
  const setManifests = useAtlas((s) => s.setManifests);
  const setShowLayer = useAtlas((s) => s.setShowLayer);

  useEffect(() => {
    let cancelled = false;
    loadCanon()
      .then((canon) => {
        if (cancelled) return;
        setLoad({ status: "ready", canon });
        // Restore the entity named in the URL, if it exists.
        const fromUrl = entityFromUrl();
        if (fromUrl && canon.byId.has(fromUrl)) select(fromUrl);
      })
      .catch((error: Error) => !cancelled && setLoad({ status: "failed", message: error.message }));
    return () => {
      cancelled = true;
    };
  }, [setLoad, select]);

  useEffect(() => {
    if (prefersReducedMotion) setAutoRotate(false);
  }, [setAutoRotate]);

  // The switcher's loader is injected so the store never imports it.
  useEffect(() => {
    setShowLayer(activateLayer);
    loadManifests()
      .then(setManifests)
      .catch(() => setManifests([]));
  }, [setManifests, setShowLayer]);

  // The URL is application state, in both directions.
  useEffect(() => writeEntityToUrl(selectedId), [selectedId]);
  useEffect(() => onUrlChange((id) => select(id)), [select]);

  // Escape closes the panel from anywhere.
  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") select(null);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [select]);

  return (
    <div className="atlas">
      {/* Skip straight to the real document, past the decorative globe. */}
      <a className="skip" href="#places">
        Skip to the list of places
      </a>

      <header className="masthead">
        <div>
          <h1 className="masthead__title">The Elysium Atlas</h1>
          <p className="masthead__sub">
            {load.status === "ready"
              ? `${load.canon.index.length.toLocaleString("en")} entities · EY 412, Calenth 16`
              : "Loading canon"}
          </p>
        </div>
        <Search />
        <Shortcuts />
      </header>

      {load.status === "failed" && (
        <div className="notice" role="alert">
          <p>{load.message}</p>
        </div>
      )}

      {/* The canvas is decoration for assistive technology; AccessibleAtlas is
          the real document, and it paints before the renderer arrives. */}
      <ErrorBoundary>
        <Stage />
      </ErrorBoundary>

      <Announcer />

      <div className="side">
        <ClockPanel />
        <LayerSwitcher />
        <Legend />
        <AccessibleAtlas />
      </div>
      <EntityPanel />
    </div>
  );
}
