# The Elysium Atlas — Deployment and Maintenance

**Document ID:** `eng.deployment`
**Status:** Proposed
**Version:** 1.0.0

---

## 1. Deploying to Vercel

The Atlas is a static site. There is no server, no database, and no environment
variable to set.

1. Push the repository to GitHub.
2. On Vercel: **Add New → Project → Import** the repository.
3. **Set Root Directory to `app`.** This is the only setting that matters;
   `app/vercel.json` supplies the rest.
4. Deploy.

Every subsequent `git push` redeploys.

**The build gate is deliberate.** `npm run build` runs, in order:

```
data:build   →  canon lint, schema validation, reference resolution, emit, types
typecheck    →  tsc --noEmit, strict
test:smoke   →  111 behavioural checks over the emitted data
check:contrast → every text and border pairing on its actual surface
vite build   →  the bundle
check:budget →  payload against the budgets in eng.design-system
```

Any failure exits non-zero and **the deploy fails rather than shipping a broken
atlas**. A canon error will name the exact file and problem.

## 2. Local development

```bash
cd app
npm install
npm run dev        # validates canon, then starts Vite
npm run verify     # everything except the bundle — the fast loop
npm run build      # the full gate, as Vercel runs it
npm run preview    # serve the production build locally
```

Node 20 or newer.

## 3. Changing canon

**Canon flows one way: `data/` → `app/public/data/`.** The app directory's copy
is a build artifact and is gitignored. Edit the source.

To change a fact about Elysium:

1. Edit the Bible chapter in `docs/bible/` that canonizes it.
2. Edit the matching value in `data/`.
3. Run `python3 tools/lint_canon.py` from the repository root.
4. Run `cd app && npm run verify`.

The linter will refuse most inconsistencies: a city outside its continent, an
indicator disagreeing with its source dataset, a reserve horizon that does not
follow from its own recovery rate, a Region count that does not match the
government tier table. That is the point — the checks exist so that a change in
one place cannot quietly contradict another.

For datasets generated from a table — `regions.json`, `industry.json`,
`energy.json`, `education.json`, `cities.json`, `routes.json` — edit the
generator in `tools/` and re-run it, or the next regeneration will overwrite
the edit.

## 4. Adding a map layer

One entry in `app/tools/layers.ts`:

```ts
{
  id: "layer.example",
  name: "Example",
  summary: "One line, shown in the switcher and read aloud by the tree.",
  datasets: ["example.json"],
  geometry: [{ kind: "region-point", source: "example.things", colour: "palette" }],
  selectable: ["example"],
  indicators: ["metric.something"],
  phase: "phase-26",
}
```

Nothing else changes. The switcher, the number-key shortcuts, the legend, the
accessible tree, and the generated manifests all read from the registry.

The pipeline will refuse the layer if it names a dataset that does not exist, an
indicator the Bible does not publish, or geometry its source data cannot supply.

## 5. The five geometry kinds

| Kind | Source entities must carry |
|---|---|
| `arc` | `path` — an ordered list of points |
| `latitude-band` | `latitudeBandDeg` |
| `point` | `coordinates` or `labelPoint` |
| `region-point` | `regions`, `bestRegions`, `deposits`, `biome`, or `polity` |
| `orbit` | `orbitalDistanceKm` |

## 6. Checks and where they live

| Check | Location | Count |
|---|---|---|
| Canon integrity | `tools/lint_canon.py` | 25 checks |
| Data behaviour | `app/tools/smoke.ts` | 111 checks |
| Contrast | `app/tools/check-contrast.ts` | 10 pairings |
| Payload budgets | `app/tools/check-budget.ts` | 3 budgets |
| Types | `tsc --noEmit`, strict | whole tree |

## 7. If something breaks

**A canon error fails the deploy.** Read the message: it names the dataset, the
field, and what disagreed with what. Fix the source, not the artifact.

**A budget breach fails the build.** Reduce the payload, or change the budget in
`check-budget.ts` deliberately and record why. It has caught three real
regressions; raising it silently would end that.

**A layer will not load.** The legend reports which dataset failed and offers a
retry. The globe and the accessible interface stay usable.

**WebGL is unavailable.** The error boundary reports it and the Atlas continues
through the accessible interface, which is complete on its own.
