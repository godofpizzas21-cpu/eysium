# The Elysium Atlas — Data Pipeline

**Document ID:** `eng.data-pipeline`
**Status:** Proposed
**Version:** 1.0.0
**Inherits:** `charter.data-schema` (entity envelope, ID domains, geometry
conventions), `charter.canon-rules` (single source of truth), `eng.architecture`

---

## 1. The Rule

> **Canon flows one way: `data/` → `app/public/data/`. The application never
> writes back, and no fact exists in the app that is not in the Bible.**

`data/` at the repository root is authoritative. `app/public/data/` is a build
artifact and is `.gitignore`d. Anyone editing the copy is editing something that
will be overwritten.

## 2. The Pipeline

`npm run data:build` runs five stages, and any failure stops the build:

| Stage | Action | Fails on |
|---|---|---|
| 1. **Canon lint** | Runs `tools/lint_canon.py` | Any of the 24 canon checks |
| 2. **Schema validation** | Validates each dataset against its Zod schema | Shape or type mismatch |
| 3. **Reference resolution** | Resolves every cross-dataset ID reference | A dangling reference |
| 4. **Emit** | Writes indexes, shards, and layer manifests | — |
| 5. **Type generation** | Emits `src/data/generated/*.ts` from the Zod schemas | — |

Stage 1 is the same linter that has guarded canon since Phase 2B. The app build
inherits every consistency guarantee the Bible has — a city cannot drift off its
continent, an indicator cannot disagree with its source, and a reserve horizon
cannot contradict its own recovery rate.

## 3. Schemas and Generated Types

Schemas live in `app/tools/schemas/` as Zod, one per dataset, and are the
**only** place a dataset's shape is described.

```ts
// tools/schemas/cities.ts
export const City = Entity.extend({
  population: z.number().int().positive(),
  polity: id("polity"),
  coordinates: LatLon,
  seatOf: id("gov", "econ").optional(),
});
```

TypeScript types are **generated from the schemas**, never hand-written:

```ts
// src/data/generated/cities.ts  — DO NOT EDIT
export type City = z.infer<typeof CitySchema>;
```

Hand-written types would be a second description of the same shape, which is the
duplication `charter.canon-rules` §2 exists to prevent.

## 4. Loading Strategy

449 kB of canon across 29 files is small enough to be careless with and large
enough that carelessness would be felt on a slow connection. The split:

**Eager — loaded before first paint (~40 kB gzipped):**
`planet-physical.json`, `continents.json`, `oceans.json`, and a generated
`entity-index.json` holding id, name, summary, tags, and coordinates for every
entity in the project. The index is what search and the accessible tree run on,
so both work before any layer has loaded.

**Lazy — loaded when a layer is first shown:**
Every other dataset, fetched by the layer that needs it and cached in the store.
Selecting the ecology layer fetches `biomes.json`; nothing else does.

**Sharded — loaded per entity:**
Reserved for datasets that grow past ~150 kB. None does yet. When `cities.json`
eventually carries per-city detail it becomes `data/cities/<slug>.json` behind
the existing index, exactly as `charter.data-schema` §1 anticipated. The loader
already routes through an index, so the change will not touch calling code.

## 5. Layer Manifests

A **layer manifest** is generated for each map layer and is the contract between
data and rendering. A layer's manifest names the datasets it needs, the geometry
it draws, and the entity types it makes selectable:

```jsonc
{
  "id": "layer.ecology",
  "name": "Ecology",
  "datasets": ["biomes.json", "environment.json"],
  "geometry": [
    { "kind": "region-fill", "source": "biomes.terrestrialBiomes", "colour": "palette" },
    { "kind": "marker",      "source": "biomes.flagshipSpecies",   "icon": "species" }
  ],
  "selectable": ["biome", "species"],
  "legend": "palette",
  "indicators": ["metric.land-protected", "metric.ocean-protected", "metric.extinction-debt"]
}
```

Manifests are generated rather than written, from the layer registry plus the
datasets, so a layer cannot reference a dataset that does not exist or an
indicator that is not published.

## 6. Geometry Handling

Per `charter.canonical-units` §5 and `charter.data-schema` §5:

- **Data is render-agnostic.** Degrees in, degrees stored. No Three.js concept
  appears in `data/`.
- **Conversion happens once**, in `src/lib/geo.ts`: `lat/lon → Vector3` on a unit
  sphere, with planet radius from `planet-physical.json` used only where real
  distances matter.
- **Polygon rings** are `[lon, lat]`, wound counter-clockwise, and may exceed
  ±180° across the antimeridian — the loader normalises modulo 360 at
  tessellation time, as the schema promises.
- **Route paths** are already great-circle interpolated in `routes.json`
  (Phase 10B), so the renderer lifts them to altitude and draws; it does not
  re-interpolate.

## 7. The Elysian Calendar in Code

The time scrubber runs on Elysian dates, not Earth dates, so `src/lib/calendar.ts`
implements `hist.calendar` directly: 12 months of 32 days, 8-day weeks,
Thresholdday every fourth year except centennials, and the sortable
`EY-0412-M08-D16` form.

No JavaScript `Date` object appears anywhere in the application. Using one would
silently import Earth's calendar into a planet that does not have it.

## 8. Failure Behaviour

- **A dataset fails to load:** the layer reports that it could not load, names
  the dataset, and offers to retry. The globe stays usable. Errors state what
  happened and what to do, never apologise, and are never vague.
- **A reference does not resolve at runtime:** impossible by construction —
  stage 3 would have failed the build.
- **WebGL is unavailable:** the application falls back to the accessible
  interface of `eng.architecture` §5, which is complete on its own. This is not a
  degraded mode; it is the other half of the product.

## 9. Open Threads

- Concrete schemas and generated types → Phase 18
- Layer registry and the first manifests → Phases 19–21
- Sharding, if and when a dataset passes 150 kB → deferred until it does
