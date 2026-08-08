/**
 * The parallel interface.
 *
 * The canvas is aria-hidden, so this is the real accessible document. It runs
 * over the same store and the same data, and selecting here selects on the
 * globe and flies the camera. Architecture, not afterthought —
 * `eng.architecture` section 5.
 */
import { useAtlas } from "../state/store.js";

export function AccessibleAtlas() {
  const load = useAtlas((s) => s.load);
  const select = useAtlas((s) => s.select);
  const selectedId = useAtlas((s) => s.selectedId);

  if (load.status !== "ready") return null;

  const { continents } = load.canon.continents;
  const { cities } = load.canon.cities;

  return (
    <main className="a11y" id="places" aria-label="Places in the Atlas">
      <h2>Continents</h2>
      <ul>
        {continents.map((continent) => {
          const here = cities.filter((city) =>
            continent.features.some((feature) => feature.id === city.polity),
          );
          return (
            <li key={continent.id}>
              <button
                type="button"
                aria-current={selectedId === continent.id ? "true" : undefined}
                onClick={() => select(continent.id)}
              >
                {continent.name}
              </button>
              <ul>
                {continent.features.map((feature) => (
                  <li key={feature.id}>
                    <button
                      type="button"
                      aria-current={selectedId === feature.id ? "true" : undefined}
                      onClick={() => select(feature.id)}
                    >
                      {feature.name}
                    </button>
                  </li>
                ))}
                {here.map((city) => (
                  <li key={city.id}>
                    <button
                      type="button"
                      aria-current={selectedId === city.id ? "true" : undefined}
                      onClick={() => select(city.id)}
                    >
                      {city.name}
                    </button>
                  </li>
                ))}
              </ul>
            </li>
          );
        })}
      </ul>

      <h2>Cities</h2>
      <ul>
        {cities.map((city) => (
          <li key={city.id}>
            <button
              type="button"
              aria-current={selectedId === city.id ? "true" : undefined}
              onClick={() => select(city.id)}
            >
              {city.name}
            </button>
          </li>
        ))}
      </ul>
    </main>
  );
}
