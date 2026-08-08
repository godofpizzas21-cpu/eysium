# The Elysium Atlas — Accessibility

**Document ID:** `eng.accessibility`
**Status:** Proposed
**Version:** 1.0.0
**Inherits:** `eng.architecture` (the two-interface requirement),
`eng.design-system` (section 7, accessibility requirements)

---

## 1. The Claim

The Elysium Atlas is **usable without WebGL, without a pointer, and without
sight**. This is not a fallback: the accessible interface is half the product,
and Phase 17 made it an architectural requirement rather than a late addition.

Target: **WCAG 2.2 Level AA**. This document records what has been verified,
what is checked automatically on every build, and what remains untested.

## 2. Architecture

**The canvas is `aria-hidden`.** It is decoration for assistive technology.

The real document is `src/a11y/AccessibleAtlas.tsx`, a `<main>` landmark
containing every continent, geographic feature, and city in the Atlas as a
navigable tree of buttons. It runs over the same store and the same data as the
globe, so:

- Selecting in either interface selects in both.
- The camera flies whether the selection came from a click or a keystroke.
- Nothing is reachable by pointer that is not reachable by keyboard.

If WebGL fails entirely, an error boundary reports it and the Atlas continues.

## 3. What Is Verified Automatically

These run on every build and fail it:

| Check | Tool |
|---|---|
| Contrast of every text and border pairing on its actual painted surface | `tools/check-contrast.ts` |
| Every entity is reachable and can produce its own record | `tools/smoke.ts` |
| Every layer's data is loadable and drawable | `tools/smoke.ts` |
| Payload budgets, so the interface stays usable on slow connections | `tools/check-budget.ts` |

**The contrast audit found and fixed a real failure.** `--shelf`, the canonical
`biome.shelf` colour, measures 2.86:1 as an interface border on a raised
surface — below the 3:1 requirement. Rather than lower the threshold or alter a
canon colour, a derived token `--shelf-edge` was introduced at 3.06:1 and used
wherever the accent carries an edge. The canon colour is unchanged and still
correct as a fill.

Current measured ratios, all passing: body text 6.6–9.7:1, strong text
11.1–13.7:1, dim text 4.0:1 (large only), focus ring 13.7:1, borders 3.1–4.5:1.

## 4. Keyboard

Every action has a keyboard equivalent, and `?` lists them.

| Key | Action |
|---|---|
| Skip link (first Tab) | Jump past the globe to the list of places |
| `1`–`9` | Show a map layer |
| `0` | Clear the layer |
| Arrow keys | Turn the globe |
| `+` / `−` | Zoom |
| `Tab` | Move through every place |
| `Enter` | Select the focused place |
| `Escape` | Close the panel or the shortcut list |
| `?` | Show the shortcut list |

Search is a proper combobox: arrows move through results, `Enter` selects,
`Escape` clears. Focus is always visible, never trapped, and returns to the
opener when the shortcut dialog closes.

## 5. Screen Readers

- The canvas is `aria-hidden`; the accessible tree is a `<main>` landmark.
- Selection and layer changes are announced through a polite live region.
- Panels carry accessible names and headings; the shortcut list is a modal
  dialog with `aria-modal`.
- Every button has a text label. No control communicates through an icon alone.

## 6. Motion, Colour, and Targets

**Motion.** `prefers-reduced-motion` is honoured completely: fly-to becomes an
instant cut, the globe stops turning, clouds stop drifting, and the clock does
not advance on its own. The Atlas remains fully functional; it simply stops
moving.

**Colour is never the only channel.** Layer symbols carry four distinct
silhouettes — sphere, octahedron, box, cone — so they remain distinguishable in
greyscale and under any colour vision deficiency. Every swatch carries its name
as text.

**Targets.** Interactive controls are at least 44 px tall. Globe markers carry
an invisible hit sphere far larger than their visible dot, so they stay
selectable when zoomed out.

**Text scaling.** Hover labels are DOM text rather than textures, so they scale
with the user's font size. No container around text is fixed in height.

## 7. Known Gaps

Stated plainly, because a conformance claim without a gap list is not credible.

| Gap | Status |
|---|---|
| **No testing with real assistive technology** | The markup follows the specifications and has not been driven by a screen reader user. This is the largest untested assumption in the document |
| **No automated axe or Lighthouse run** | The build has no browser, so DOM-level auditing is not yet part of CI |
| **Colour-blindness simulation is reasoned, not measured** | Shape differentiation was designed for it; no simulator has been run over screenshots |
| **The accessible tree lists places, not layer data** | Layer indicators appear in the legend, which is reachable, but the tree itself does not enumerate them |
| **Long lists are not virtualised** | 1,071 entities are searchable but the tree renders continents, features, and cities only — full enumeration would need virtualisation to stay responsive |

## 8. Reporting

Accessibility failures should be treated as defects rather than enhancements.
The project's own canon takes the view that a right of access is worth what
someone's willingness to use it is worth (`gov.administration` section 7); an
interface nobody can operate has the same problem.
