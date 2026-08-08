/**
 * Off-world settlement, shown when the space layer is active.
 *
 * The Belt appears here rather than in the scene: at 2.3 AU it lies roughly
 * 52,800 planet radii out, four orders of magnitude beyond Kalyra, and drawing
 * it in view would misrepresent the distance. Canon is candid about scale, so
 * the Atlas is too.
 */
import { useAtlas } from "../state/store.js";

interface Settlement {
  id: string;
  name: string;
  summary: string;
  population: number;
}

export function OffWorld() {
  const bundle = useAtlas((s) => s.activeLayer());
  const select = useAtlas((s) => s.select);
  const selectedId = useAtlas((s) => s.selectedId);

  if (bundle?.manifest.view !== "space") return null;

  const space = bundle.data["space.json"] as
    | {
        offWorldPopulation?: { total: number; distribution: Settlement[] };
        belt?: { lightLagCivilMinutes: number[]; transitElysianMonths: number[] };
      }
    | undefined;

  const settlements = space?.offWorldPopulation?.distribution ?? [];
  const total = space?.offWorldPopulation?.total ?? 0;
  const belt = space?.belt;

  return (
    <section className="offworld" aria-label="Off-world settlement">
      <h3 className="swatches__heading">Off-world · {total.toLocaleString("en")} people</h3>
      <ul className="offworld__list">
        {settlements.map((settlement) => (
          <li key={settlement.id}>
            <button
              type="button"
              className="swatch"
              aria-current={selectedId === settlement.id ? "true" : undefined}
              onClick={() => select(settlement.id)}
            >
              <span className="swatch__name">{settlement.name}</span>
              <span className="swatch__detail">
                {(settlement.population / 1_000_000).toFixed(1)} M
              </span>
            </button>
          </li>
        ))}
      </ul>

      {belt && (
        <p className="offworld__note">
          The Tyrran Belt is not drawn: at 2.3 AU it lies some 52,800 planet radii out, four
          orders of magnitude beyond Kalyra. Signals take {belt.lightLagCivilMinutes[0]}–
          {belt.lightLagCivilMinutes[1]} civil minutes each way, and a crossing takes{" "}
          {belt.transitElysianMonths[0]}–{belt.transitElysianMonths[1]} Elysian months.
        </p>
      )}
    </section>
  );
}
