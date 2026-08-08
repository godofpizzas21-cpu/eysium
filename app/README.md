# The Elysium Atlas

Interactive 3D atlas of the Elysian Concord, rendered from the Civilization
Bible in `../docs/bible` and the canon datasets in `../data`.

Specifications: `eng.architecture`, `eng.data-pipeline`, `eng.design-system`
in `../docs/engineering`.

## Status

**Phase 24 — advanced overlays.** Twelve layers draw, and the Record Drawer is
complete: any entity in the Atlas will show you its canonical id, the Bible
chapters that canonize it, its dataset and version, and the entry exactly as it
exists in canon.

## Running it

```bash
npm install
npm run dev            # validate canon, then start the dev server
npm run build          # data + typecheck + bundle + budget check
npm run preview        # serve the production build locally
```

`data:build` is the gate. It runs five stages and exits non-zero on any failure,
so a canon error fails the build rather than shipping a broken atlas:

| Stage | What it does |
|---|---|
| 1. Canon lint | Runs `../tools/lint_canon.py` — all 25 canon checks |
| 2. Schema validation | Every dataset against `DatasetHeader`; nine against strict schemas; **every entity anywhere against the charter's entity envelope** |
| 3. Reference resolution | Every cross-dataset ID reference must resolve |
| 4. Emit | Datasets, `entity-index.json`, `layer-manifests.json` → `public/data/` |
| 5. Types | `src/data/generated/` from the schemas |

Current output: **29 datasets, 1,071 entities (106 with coordinates), 9 layer
manifests.**

## Performance

`npm run build` ends with a budget check that fails the build if the payload
grows past the limits in `eng.design-system` section 6.

| Measure | Current | Target | Hard fail |
|---|---|---|---|
| Initial JS, gzipped | 65.8 kB | 220 kB | 300 kB |
| Initial CSS, gzipped | 2.8 kB | 20 kB | 40 kB |
| Eager data, gzipped | 33.2 kB | 40 kB | 60 kB |
| Renderer (lazy) | 243.8 kB | — | — |

Three.js is lazy-loaded. The accessible interface is the real document and
paints without it, so the renderer is not on the critical path.

## Deploying

Vercel: import the repository, set **root directory** to `app`. `vercel.json`
supplies the rest. The build runs the canon linter first, so a canon error fails
the deploy rather than shipping a broken atlas.

## Layout

```
app/
├── tools/
│   ├── build-data.ts        the pipeline
│   ├── layers.ts            the layer registry — the only place layers are listed
│   └── schemas/
│       ├── common.ts        entity envelope, IDs, geometry primitives
│       └── datasets.ts      strict schemas for the datasets the Atlas renders
├── src/
│   ├── scene/               Globe, Markers, CameraRig, Controls, Stage
│   ├── layers/              LayerGeometry — manifest-driven renderers
│   ├── a11y/                the parallel accessible interface
│   ├── panels/              EntityPanel, Record Drawer, Search, LayerSwitcher, Legend
│   ├── state/               zustand store
│   ├── lib/                 geo, calendar, sun — no JavaScript Date anywhere
│   ├── data/                loader and generated types
│   └── styles/              tokens.css, generated from the canon palette
└── public/data/             build artifact (gitignored)
```

## Two rules worth knowing

**Canon flows one way.** `../data` is authoritative. `public/data/` and
`src/data/generated/` are build artifacts and are gitignored. Editing either is
editing something that will be overwritten.

**The registry is the extension point.** Adding a map layer means one entry in
`tools/layers.ts` and a folder in `src/layers/`. The switcher, the URL parser,
the accessible tree, and the manifests all read from the registry. The pipeline
fails the build if a layer names a dataset or an indicator that does not exist,
so a layer cannot promise data the Bible does not hold.
