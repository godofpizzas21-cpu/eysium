/**
 * Search across every canonical entity.
 *
 * Runs on the eager index, so it works before any layer has loaded. Results are
 * a listbox with full keyboard support: arrows move, Enter selects, Escape
 * clears.
 */
import { useId, useMemo, useRef, useState } from "react";
import { useAtlas } from "../state/store.js";

export function Search() {
  const query = useAtlas((s) => s.query);
  const setQuery = useAtlas((s) => s.setQuery);
  const select = useAtlas((s) => s.select);
  const load = useAtlas((s) => s.load);
  const total = load.status === "ready" ? load.canon.index.length : 0;

  /**
   * Results are computed here rather than in a store selector.
   *
   * A zustand selector that builds a new array returns a new reference every
   * time the store is read, which React sees as a change, which reads the store
   * again — an infinite render loop. Selectors must return values that already
   * exist; derived collections belong in useMemo.
   */
  const results = useMemo(() => {
    if (load.status !== "ready") return [];
    const needle = query.trim().toLowerCase();
    if (needle.length < 2) return [];

    const scored: { entry: (typeof load.canon.index)[number]; score: number }[] = [];
    for (const entry of load.canon.index) {
      const name = entry.name.toLowerCase();
      let score = -1;
      if (name === needle) score = 0;
      else if (name.startsWith(needle)) score = 1;
      else if (name.includes(needle)) score = 2;
      else if (entry.id.includes(needle)) score = 3;
      else if (entry.tags?.some((tag) => tag.toLowerCase().includes(needle))) score = 4;
      if (score >= 0) scored.push({ entry, score });
    }
    scored.sort((a, b) => a.score - b.score || a.entry.name.localeCompare(b.entry.name));
    return scored.slice(0, 12).map((hit) => hit.entry);
  }, [load, query]);

  const [active, setActive] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const listId = useId();

  const choose = (id: string) => {
    select(id);
    setQuery("");
    setActive(0);
  };

  return (
    <div className="search">
      <label className="search__label" htmlFor={`${listId}-input`}>
        Find a place
      </label>
      <input
        id={`${listId}-input`}
        ref={inputRef}
        className="search__input"
        type="search"
        role="combobox"
        aria-expanded={results.length > 0}
        aria-controls={listId}
        aria-autocomplete="list"
        aria-activedescendant={results.length ? `${listId}-${active}` : undefined}
        placeholder={total ? `Search ${total.toLocaleString("en")} entries` : "Loading"}
        value={query}
        onChange={(event) => {
          setQuery(event.target.value);
          setActive(0);
        }}
        onKeyDown={(event) => {
          if (event.key === "ArrowDown") {
            event.preventDefault();
            setActive((index) => Math.min(index + 1, results.length - 1));
          } else if (event.key === "ArrowUp") {
            event.preventDefault();
            setActive((index) => Math.max(index - 1, 0));
          } else if (event.key === "Enter") {
            const hit = results[active];
            if (hit) {
              event.preventDefault();
              choose(hit.id);
            }
          } else if (event.key === "Escape") {
            setQuery("");
          }
        }}
      />

      {results.length > 0 && (
        <ul className="search__results" id={listId} role="listbox" aria-label="Search results">
          {results.map((entry, index) => (
            <li
              key={entry.id}
              id={`${listId}-${index}`}
              role="option"
              aria-selected={index === active}
              className={index === active ? "is-active" : undefined}
            >
              <button type="button" onMouseEnter={() => setActive(index)} onClick={() => choose(entry.id)}>
                <span className="search__name">{entry.name}</span>
                <span className="search__id">{entry.id}</span>
              </button>
            </li>
          ))}
        </ul>
      )}

      {query.trim().length >= 2 && results.length === 0 && (
        <p className="search__empty">Nothing matches “{query.trim()}”. Try a shorter word.</p>
      )}
    </div>
  );
}
