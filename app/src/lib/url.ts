/**
 * URL synchronisation.
 *
 * The URL is application state, so any view can be shared or bookmarked
 * (`eng.architecture` section 4). Entity ids in URLs are the immutable
 * canonical ids, so a link shared today still resolves in ten years even if a
 * display name changes.
 *
 * This is thirty lines rather than a routing library because the Atlas has no
 * nested routes and needs only id-in-URL sync. See the Phase 19B changelog note.
 */

/** Read the focused entity id from the current URL, if any. */
export function entityFromUrl(): string | null {
  const match = window.location.pathname.match(/^\/entity\/([a-z0-9.-]+)\/?$/i);
  return match?.[1] ?? null;
}

/** Reflect the focused entity in the URL without reloading. */
export function writeEntityToUrl(id: string | null, replace = false) {
  const next = id ? `/entity/${id}` : "/";
  if (window.location.pathname === next) return;
  const method = replace ? "replaceState" : "pushState";
  window.history[method]({ id }, "", next + window.location.search);
}

/** Subscribe to back/forward navigation. Returns an unsubscribe function. */
export function onUrlChange(handler: (id: string | null) => void): () => void {
  const listener = () => handler(entityFromUrl());
  window.addEventListener("popstate", listener);
  return () => window.removeEventListener("popstate", listener);
}
