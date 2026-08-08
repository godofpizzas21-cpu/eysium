/**
 * Legend swatches.
 *
 * Where a layer paints from `palette`, its entities carry their own canonical
 * colours — so the swatch list is the canon palette, shown directly. Each
 * swatch is a button: selecting it focuses the entity and flies the camera,
 * which makes the legend a navigation surface rather than a key.
 */
import { useMemo } from "react";

import { resolveSource } from "../data/layers.js";
import { useAtlas } from "../state/store.js";

interface Swatch {
  id: string;
  name: string;
  colour: string;
  detail?: string;
}

export function Swatches() {
  const bundle = useAtlas((s) => s.activeLayer());
  const select = useAtlas((s) => s.select);
  const selectedId = useAtlas((s) => s.selectedId);
  const hover = useAtlas((s) => s.hover);

  const swatches = useMemo<Swatch[]>(() => {
    if (!bundle) return [];
    const found: Swatch[] = [];

    for (const geometry of bundle.manifest.geometry) {
      if (geometry.colour !== "palette") continue;
      for (const entry of resolveSource(bundle, geometry.source) as Record<string, unknown>[]) {
        if (typeof entry.id !== "string" || typeof entry.palette !== "string") continue;
        const area = typeof entry.areaMkm2 === "number" ? entry.areaMkm2 : null;
        const band = Array.isArray(entry.latitudeBandDeg)
          ? (entry.latitudeBandDeg as number[])
          : null;
        found.push({
          id: entry.id,
          name: String(entry.name),
          colour: entry.palette,
          detail: area
            ? `${area.toLocaleString("en")} M km²`
            : band
              ? `${band[0]}–${band[1]}°`
              : undefined,
        });
      }
    }
    return found;
  }, [bundle]);

  if (!swatches.length) return null;

  return (
    <section className="swatches" aria-label="Legend">
      <h3 className="swatches__heading">Key</h3>
      <ul className="swatches__list">
        {swatches.map((swatch) => (
          <li key={swatch.id}>
            <button
              type="button"
              className="swatch"
              aria-current={selectedId === swatch.id ? "true" : undefined}
              onMouseEnter={() => hover(swatch.id)}
              onMouseLeave={() => hover(null)}
              onFocus={() => hover(swatch.id)}
              onBlur={() => hover(null)}
              onClick={() => select(swatch.id)}
            >
              <span
                className="swatch__chip"
                style={{ background: swatch.colour }}
                aria-hidden="true"
              />
              <span className="swatch__name">{swatch.name}</span>
              {swatch.detail && <span className="swatch__detail">{swatch.detail}</span>}
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}
