/**
 * The legend, and the indicators a layer surfaces.
 *
 * A gameable indicator never appears without its counterweight, because
 * `metric.system` section 2 forbids publishing one without the other. The
 * pairing is applied in `data/layers.ts`; this component only renders it.
 */
import { useAtlas } from "../state/store.js";
import { Swatches } from "./Swatches.js";
import { OffWorld } from "./OffWorld.js";

function format(value: number, unit: string): string {
  const shown =
    Math.abs(value) >= 1_000_000
      ? value.toLocaleString("en", { maximumFractionDigits: 0 })
      : value.toLocaleString("en", { maximumFractionDigits: 2 });
  return unit ? `${shown} ${unit}` : shown;
}

export function Legend() {
  const layer = useAtlas((s) => s.activeLayer());
  const indicators = useAtlas((s) => s.indicators);
  const status = useAtlas((s) => s.layerStatus);
  const error = useAtlas((s) => s.layerError);

  if (status === "idle") return null;

  if (status === "failed") {
    return (
      <section className="legend" aria-label="Layer">
        <p className="legend__error" role="alert">
          {error ?? "That layer could not load."} Select it again to retry.
        </p>
      </section>
    );
  }

  if (!layer) {
    return (
      <section className="legend" aria-label="Layer">
        <p className="legend__pending">Loading layer</p>
      </section>
    );
  }

  return (
    <section className="legend" aria-label={`${layer.manifest.name} layer`}>
      <h2 className="legend__title">{layer.manifest.name}</h2>
      <p className="legend__summary">{layer.manifest.summary}</p>

      {indicators.length > 0 && (
        <ul className="legend__indicators">
          {indicators.map((indicator) => (
            <li key={indicator.id} className="indicator">
              <div className="indicator__row">
                <span className="indicator__name">{indicator.name}</span>
                <span className="indicator__value">
                  {format(indicator.value, indicator.unit)}
                </span>
              </div>
              <span className="indicator__trend">{indicator.trend}</span>

              {indicator.counterweight && (
                <div className="indicator__pair">
                  <span className="indicator__pairLabel">Counterweight</span>
                  <div className="indicator__row">
                    <span className="indicator__name">{indicator.counterweight.name}</span>
                    <span className="indicator__value">
                      {format(indicator.counterweight.value, indicator.counterweight.unit)}
                    </span>
                  </div>
                </div>
              )}
            </li>
          ))}
        </ul>
      )}

      <Swatches />
      <OffWorld />

      {!layer.manifest.geometry.length && (
        <p className="legend__note">Geometry for this layer arrives in {layer.manifest.phase}.</p>
      )}
    </section>
  );
}
