/**
 * Search across every canonical entity.
 *
 * Runs on the eager index, so it works before any layer has loaded. Results are
 * a listbox with full keyboard support: arrows move, Enter selects, Escape
 * clears.
 */
import { useId, useRef, useState } from "react";
import { useAtlas } from "../state/store.js";

export function Search() {
  const query = useAtlas((s) => s.query);
  const setQuery = useAtlas((s) => s.setQuery);
  const select = useAtlas((s) => s.select);
  const results = useAtlas((s) => s.results());
  const total = useAtlas((s) => (s.load.status === "ready" ? s.load.canon.index.length : 0));

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
