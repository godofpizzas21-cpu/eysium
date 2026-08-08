/**
 * The entity panel, and the Record Drawer beneath it.
 *
 * The drawer is the signature element: any entity can show you its canonical
 * id, the Bible chapters that canonize it, the dataset it lives in with its
 * version, and the entry exactly as it exists in canon.
 *
 * This is `gov.administration` section 5 — the right of access to record —
 * expressed as an interface. It is deliberately plain: monospace, no syntax
 * highlighting theatre, as a Record Office terminal would show it.
 */
import { useEffect, useState } from "react";

import { loadRecord, type EntityRecord } from "../data/record.js";
import { useAtlas } from "../state/store.js";

export function EntityPanel() {
  const entity = useAtlas((s) => s.selectedEntity());
  const summary = useAtlas((s) => s.selectedSummary());
  const city = useAtlas((s) => s.selectedCity());
  const select = useAtlas((s) => s.select);

  const [recordOpen, setRecordOpen] = useState(false);
  const [record, setRecord] = useState<EntityRecord | null>(null);
  const [recordError, setRecordError] = useState<string | null>(null);

  // Close the drawer when the selection changes, so it never shows the
  // previous entity's record.
  useEffect(() => {
    setRecordOpen(false);
    setRecord(null);
    setRecordError(null);
  }, [entity?.id]);

  useEffect(() => {
    if (!recordOpen || !entity || record) return;
    let cancelled = false;
    loadRecord(entity.id, entity.dataset)
      .then((found) => {
        if (cancelled) return;
        if (found) setRecord(found);
        else setRecordError(`No entry for ${entity.id} in ${entity.dataset}.`);
      })
      .catch((error: Error) => !cancelled && setRecordError(error.message));
    return () => {
      cancelled = true;
    };
  }, [recordOpen, entity, record]);

  if (!entity) return null;

  return (
    <aside className="panel" aria-label={`About ${entity.name}`}>
      <header className="panel__head">
        <h2 className="panel__title">{entity.name}</h2>
        <button type="button" className="panel__close" onClick={() => select(null)}>
          Close
        </button>
      </header>

      {summary && <p className="panel__summary">{summary}</p>}

      {(entity.population !== undefined || city) && (
        <dl className="figures">
          {entity.population !== undefined && (
            <div>
              <dt>Population</dt>
              <dd>{entity.population.toLocaleString("en")}</dd>
            </div>
          )}
          {city && (
            <div>
              <dt>Coordinates</dt>
              <dd>
                {city.coordinates.lat.toFixed(1)}°, {city.coordinates.lon.toFixed(1)}°
              </dd>
            </div>
          )}
        </dl>
      )}

      <button
        type="button"
        className="panel__record"
        aria-expanded={recordOpen}
        onClick={() => setRecordOpen((open) => !open)}
      >
        {recordOpen ? "Hide record" : "Show record"}
      </button>

      {recordOpen && (
        <div className="record">
          <dl>
            <div>
              <dt>Canonical id</dt>
              <dd>{entity.id}</dd>
            </div>
            <div>
              <dt>Dataset</dt>
              <dd>
                {entity.dataset}
                {record ? ` · ${record.dataVersion}` : ""}
              </dd>
            </div>
            {record && record.sources.length > 0 && (
              <div>
                <dt>Canonized in</dt>
                <dd>{record.sources.join(", ")}</dd>
              </div>
            )}
          </dl>

          {recordError && <p className="record__error">{recordError}</p>}

          {record && (
            <pre className="record__raw" tabIndex={0} aria-label="The entry as it exists in canon">
              {JSON.stringify(record.raw, null, 2)}
            </pre>
          )}

          {!record && !recordError && <p className="record__note">Fetching the record.</p>}

          <p className="record__note">
            Every figure in the Atlas comes from the Civilization Bible. This is where this
            one lives.
          </p>
        </div>
      )}
    </aside>
  );
}
