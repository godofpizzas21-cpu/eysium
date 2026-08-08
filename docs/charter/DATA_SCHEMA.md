# Data Schema Philosophy

**Document ID:** `charter.data-schema`
**Status:** Canon
**Version:** 1.13.0

This document defines *how* structured data is designed throughout the project,
so that when Phase 18 builds the data layer, every earlier phase's data slots in
without rework. Concrete schemas are owned by the phases that create each dataset.

---

## 1. Principles

1. **Bible-first.** Every value in `data/` is derivable from, and cited by, the
   Bible. Data files never contain facts absent from canon prose.
2. **Static, typed, versioned.** Datasets are plain JSON files loaded by the
   Atlas at runtime (with code-split lazy loading for heavy layers). Each file
   declares `schemaVersion` and `dataVersion`. TypeScript interfaces in the app
   are generated to mirror schemas 1:1.
3. **Entities own IDs; layers reference them.** A city exists once, in
   `cities.json`, with ID `city.aurelia`. The transport layer, economy overlay,
   and search index all reference `city.aurelia` — they never redefine it.
4. **Render-agnostic data.** Data describes the world (coordinates in degrees,
   sizes in metres). All conversion to render space happens in the app, per
   `charter.canonical-units` §5. No Three.js concepts leak into `data/`.
5. **Scalable by sharding, not by schema breaks.** When a dataset grows large
   (e.g. per-city detail), it shards into `data/cities/<slug>.json` keyed by ID,
   with a lightweight index file — the schema of each shard stays stable.

## 2. Standard Entity Envelope

Every entity in every dataset shares this envelope, extended per type:

**Enforcement.** From Phase 18 the envelope is machine-checked: the Atlas data
pipeline validates every entity in every dataset against it and fails the build
on a violation. The check found 31 pre-existing entities missing `summary` or
`sources`, all since corrected.

```jsonc
{
  "id": "city.aurelia",          // immutable namespaced ID (CANON_RULES §3.2)
  "name": "Aurelia",             // display name (may change)
  "summary": "…",                // one-sentence description for panels/search
  "sources": ["planet.geography"], // Bible document IDs that canonize it
  "tags": ["capital", "coastal"] // free taxonomy for filtering
}
```

## 3. Registered ID Domains (initial set)

| Prefix | Meaning | Owning phase |
|---|---|---|
| `charter.` | Charter documents | 1 |
| `planet.` | Planetary/physical documents & constants | 2 |
| `region.` `ocean.` | Geographic entities | 2A |
| `climate.` | Climate zones, cells, oscillations, hazards | 2B |
| `biome.` | Terrestrial biomes and marine realms | 2B |
| `clade.` `species.` | Biological clades, flagship organisms, the Elysian species | 2B, 3B |
| `resource.` | Materials, renewable potential, reserves | 2B |
| `hist.` | Historical eras, events, demographics | 3 |
| `cal.` | Calendar months, weekdays, reference date | 3A |
| `demo.` | Demographic aggregates | 3B |
| `lang.` | Language families, scripts, language guarantees | 3B |
| `gov.` | Constitution, institutions, rights, offices | 4 |
| `polity.` | The 34 constituent Regions | 4B |
| `law.` | Courts, criminal and civil law | 5 |
| `econ.` | Currency, finance, taxation, markets, labour | 6A |
| `ind.` | Industry, automation, logistics | 6B |
| `energy.` | Generation, grid, storage, energy pricing | 7A |
| `env.` | Environment, carbon management, climate resilience | 7B |
| `edu.` | Schooling, entitlement, institutions, libraries | 8A |
| `res.` | Research, sciences, funding | 8B |
| `health.` | Healthcare, clinical practice, epidemic capability | 9 |
| `city.` | Cities, urbanism, housing | 10A |
| `route.` | Transport routes and networks | 10B |
| `agri.` | Agriculture, fisheries, food reserves | 11 |
| `mil.` | The Concord Service, Abolition regime, disaster response | 12 |
| `ai.` | Artificial systems, the Cassian Rules, licensing | 13 |
| `cult.` | Culture, civic virtues, belief, observances | 3B, 14 |
| `space.` | Orbital, lunar, and Belt infrastructure | 15 |
| `dipl.` | Orbital Territory, external relations, first contact | 15 |
| `metric.` | Indicator system, the 48 indicators, the Unmeasured Register | 16 |
| `eng.` | Software architecture, data pipeline, design system | 17 |

New prefixes are added here (MINOR bump) by the phase that needs them.

## 4. Layer Model (forward design for the Atlas)

The Atlas's switchable map layers (political, infrastructure, military, ecology,
research, transportation, population, economy, weather, space) will each be
driven by one **layer manifest**: a JSON file listing the entities, geometries,
and metrics the layer displays, referencing entity IDs. Phases 2–16 therefore
produce entity data; Phase 18 produces manifests; Phase 21+ renders them. This
separation lets worldbuilding proceed without UI decisions and vice versa.

## 5. Geometry Conventions

- Points: `{ "lat": …, "lon": … }` decimal degrees.
- Paths (routes, currents, grid lines): arrays of points, great-circle
  interpolation applied at render time.
**Known geometry gap.** Only continents and islands carry polygon rings. Biomes,
climate zones, and protected areas are canonized as areas, latitude bands, and
region references rather than as outlines, so the Atlas draws them as bands and
region-anchored symbols rather than as fills (Phase 21A). Adding biome polygons
would be a data extension, not a rendering change, and is recorded here so the
absence is visible rather than mistaken for an oversight.

- Areas (continents, zones, protected areas): GeoJSON-style polygon rings in
  degrees, wound counter-clockwise for outer rings. Ring vertices are compact
  `[lon, lat]` arrays (GeoJSON order) — the one deliberate exception to the
  `{ "lat", "lon" }` object form used for points and paths. Rings crossing the
  antimeridian may exceed ±180° for continuity; normalize modulo 360 at render
  time.
- Orbits (Phase 15/23): Keplerian elements relative to Elysium, in a dedicated
  `space-orbits.json` schema.
