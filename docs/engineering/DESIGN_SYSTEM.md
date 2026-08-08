# The Elysium Atlas — Design System

**Document ID:** `eng.design-system`
**Status:** Proposed
**Version:** 1.0.0
**Inherits:** `planet.biosphere` (the teal/gold palette), `env.conservation`
(dark-sky standards), `city.urbanism` (cities glow rather than glare),
`cult.arts` (green is the exotic pigment), `gov.administration` (right of access
to record), `metric.system` (paired counterweights)

---

## 1. The Brief, Stated

**Subject:** an atlas of one planet and 1,071 canonical entities.
**Audience:** a reader who wants to look something up, and a reader who wants to
wander. Usually the same person, ten minutes apart.
**The single job:** make canon navigable without flattening it.

Everything below is derived from the civilization rather than applied to it. The
Atlas should be recognisably *of* Elysium, and there is no need to invent a
visual language when canon already specifies one.

## 2. Palette — Taken From the Data

`data/biomes.json` already carries a canonical palette, because Phase 2B
canonized Elysian vegetation as **phyllocyanin teal and xantholin amber, not
chlorophyll green**. The Atlas does not choose colours; it reads them.

| Token | Hex | Source in canon |
|---|---|---|
| `--void` | `#070E10` | Space. Near-black with a teal undertone, never pure black |
| `--abyss` | `#0B2A45` | `biome.abyssal` — the deep ocean, and the app's ground colour |
| `--shelf` | `#2A7CA8` | `biome.shelf` — shallow water, the primary interactive accent |
| `--phyllocyanin` | `#0E5F5A` | `biome.equatorial-rainforest` — the living surface |
| `--xantholin` | `#C08A3E` | `biome.boreal-taiga` — dormancy, warmth, the secondary accent |
| `--sirocc` | `#D8B26A` | `biome.subtropical-desert` — the light neutral, used for body text |
| `--ice` | `#E4EDF0` | `biome.permanent-ice` — the highest-contrast surface, used sparingly |

Layer colours are read directly from each entity's `palette` field, so the
ecology layer is literally painted in the colours canon assigns to its biomes. A
palette change in the Bible repaints the Atlas.

**The green rule.** `cult.arts` §5 records that on Elysium **green is the exotic
pigment**, signalling strangeness, sickness, or the supernatural. The Atlas
honours this: no interface element is green in its normal state, and green
(`#7FA24A`, canon's savanna value, desaturated) is reserved **exclusively** for
anomaly — a threshold breach, a failed islanding drill, an indicator crossing its
counterweight. Green means *look at this, something is wrong.* It is the one
place canon's symbolism becomes a functional affordance.

**The glare rule.** Elysian cities "glow rather than glare" under dark-sky
standards covering 61% of land. The interface follows: no pure white, no bright
glows, no bloom, no neon. Light is low, warm, and downward. Maximum luminance in
the UI is `--ice` and it is used for perhaps 2% of pixels.

## 3. Typography

| Role | Face | Why this one |
|---|---|---|
| Display | **Spectral** | A screen-first serif with real character, restrained rather than high-contrast. Fits canon's naming aesthetic — "clear, dignified, slightly classical" (`charter.canon-rules` §3.1) — without the editorial-revival look that dominates fashionable typography |
| Body / UI | **Inter** | Neutral, exhaustively hinted, legible at 13 px in a dark interface |
| Data | **IBM Plex Mono** | Tabular figures, disambiguated zero, and it renders canonical IDs like `city.kessandra-reach` as the machine artefacts they are |

All three are open-licensed and self-hosted; no third-party font requests.

**Data typography is not decoration here, it is the personality.** This is an
atlas of a civilization that refuses composite indices, publishes distributions
rather than central values, and prints its own failures. Figures appear
constantly, and they are set in a monospace with tabular alignment so columns of
them read as columns. Where canon publishes a median with percentiles, the Atlas
shows all three.

Scale: 12 / 13 / 15 / 18 / 24 / 34 / 48 px, 1.5 line height for prose, 1.3 for
data.

## 4. The Signature: the Record Drawer

Every project should be remembered for one thing. The Atlas's is a panel.

**Any entity in the Atlas can show you its source.** A persistent control on
every entity panel opens the **Record Drawer**, which slides up from the bottom
edge and displays:

- the entity's canonical ID,
- the Bible chapter that canonizes it, quoted,
- the raw JSON as it appears in the dataset,
- and the dataset's own version.

This is not a developer feature. It is `gov.administration` §5 — the **right of
access to record** — expressed as an interface. The Concord publishes everything
and holds that a right of access is worth what someone's willingness to read the
record is worth. The Atlas makes reading the record one click from anywhere, and
the drawer is deliberately plain: no syntax highlighting theatre, monospace, the
document ID at the top, exactly as a Record Office terminal would show it.

The second, quieter signature is **paired counterweights** (`metric.system` §2):
where the Atlas shows a gameable indicator, it shows its counterweight beside it,
always, in the same card. Custody rate never appears without reoffending. This
is a civilization's statistical principle enforced as a layout rule.

## 5. Motion

Motion is used for orientation and nothing else.

- **Fly-to**: 900 ms, cubic ease-out, with the globe rotating under a fixed
  camera rather than the camera flying around the globe — cheaper, steadier, and
  it keeps the horizon level.
- **Terminator and cloud drift**: continuous, extremely slow, ambient. The
  day/night line moves in real time against the 25.9-hour Elysian day.
- **Panels**: 180 ms slide, no bounce.
- **Nothing else animates.** No hover glows, no pulsing markers, no parallax.

**`prefers-reduced-motion` is honoured completely**: fly-to becomes an instant
cut, ambient drift stops, and the terminator updates on a timer rather than per
frame. The application remains fully functional; it simply stops moving.

## 6. Performance Budget

Measured on a mid-range laptop (integrated graphics) and a three-year-old phone.

| Budget | Target | Hard fail |
|---|---|---|
| Initial JS, gzipped | ≤ 220 kB | 300 kB |
| Initial data, gzipped | ≤ 40 kB | 60 kB |
| Time to first interaction | ≤ 2.5 s | 4 s |
| Frame rate, desktop | 60 fps | below 45 sustained |
| Frame rate, mobile | 30 fps | below 24 sustained |
| Draw calls, typical layer | ≤ 120 | 200 |
| Total scene triangles | ≤ 400 k | 800 k |

Techniques fixed now so later phases do not have to argue about them:
instanced meshes for repeated markers, merged geometry per layer, texture atlas
for icons, frustum culling on entity markers, and layer geometry disposed on
deselect rather than hidden.

**Budgets are checked in CI** and a regression fails the build, on the same
principle as the canon linter: a rule nobody measures is a rule nobody keeps.

## 7. Accessibility Requirements

These are requirements, not aspirations, and Phase 25 verifies them.

- **The parallel interface** of `eng.architecture` §5 is complete and always
  present, not a fallback.
- **Keyboard**: every entity reachable by Tab, globe rotatable by arrow keys,
  zoom by `+`/`−`, layer switching by number keys, `Escape` closes panels. Focus
  is always visible and never trapped.
- **Screen readers**: canvas `aria-hidden`; selection changes announced via a
  polite live region; panels are proper landmarks with headings.
- **Colour is never the only channel.** Every layer distinguishes by shape,
  label, or pattern as well as hue. Verified against deuteranopia,
  protanopia, and tritanopia simulations.
- **Contrast**: 4.5:1 for body text, 3:1 for large text and interface borders,
  measured on the actual dark surfaces rather than assumed.
- **Targets**: 44 × 44 px minimum for pointer targets, including globe markers,
  which are given an invisible hit sphere larger than their visible dot.
- **Text scales to 200%** without loss of function; no fixed-height containers
  around text.
- **No content depends on hover.** Every hover reveal has a click or focus
  equivalent.

## 8. Voice

Interface copy follows the Concord's own habits, which happen to be good
practice: plain verbs, sentence case, active voice, no filler. A control says
what happens — *Show ecology layer*, not *Ecology*. Errors state what happened
and what to do, do not apologise, and are never vague. Empty states invite an
action rather than describing an absence.

Entity summaries in panels are the `summary` field from the dataset, unedited.
The Bible already wrote them, and rewriting them in the UI would create a second
description of a canonical fact.

## 9. Open Threads

- Token file and component implementations → Phase 19
- Layer legends and symbology → Phase 21
- Accessibility audit and conformance statement → Phase 25
