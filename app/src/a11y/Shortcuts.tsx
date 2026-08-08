/**
 * Keyboard shortcuts, discoverable rather than hidden.
 *
 * Opened with `?`, closed with Escape. Every action the globe offers has a
 * keyboard equivalent, and this is where a person finds out.
 */
import { useEffect, useRef, useState } from "react";

const SHORTCUTS: { keys: string; action: string }[] = [
  { keys: "1 – 9", action: "Show a map layer" },
  { keys: "0", action: "Clear the layer" },
  { keys: "Arrow keys", action: "Turn the globe" },
  { keys: "+ / −", action: "Zoom in and out" },
  { keys: "Tab", action: "Move through every place in the Atlas" },
  { keys: "Enter", action: "Select the focused place" },
  { keys: "Escape", action: "Close the panel" },
  { keys: "?", action: "Show this list" },
];

export function Shortcuts() {
  const [open, setOpen] = useState(false);
  const dialog = useRef<HTMLDivElement>(null);
  const opener = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      const target = event.target as HTMLElement | null;
      if (target && /^(INPUT|TEXTAREA)$/.test(target.tagName)) return;
      if (event.key === "?") {
        event.preventDefault();
        setOpen(true);
      } else if (event.key === "Escape" && open) {
        setOpen(false);
        opener.current?.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  useEffect(() => {
    if (open) dialog.current?.focus();
  }, [open]);

  return (
    <>
      <button
        ref={opener}
        type="button"
        className="shortcuts__open"
        onClick={() => setOpen(true)}
      >
        Keyboard shortcuts
      </button>

      {open && (
        <div
          ref={dialog}
          className="shortcuts"
          role="dialog"
          aria-modal="true"
          aria-label="Keyboard shortcuts"
          tabIndex={-1}
        >
          <h2 className="shortcuts__title">Keyboard shortcuts</h2>
          <dl className="shortcuts__list">
            {SHORTCUTS.map((shortcut) => (
              <div key={shortcut.keys}>
                <dt>
                  <kbd>{shortcut.keys}</kbd>
                </dt>
                <dd>{shortcut.action}</dd>
              </div>
            ))}
          </dl>
          <p className="shortcuts__note">
            The globe is decorative. Everything in it is reachable from the list of places
            beside it.
          </p>
          <button type="button" className="panel__close" onClick={() => setOpen(false)}>
            Close
          </button>
        </div>
      )}
    </>
  );
}
