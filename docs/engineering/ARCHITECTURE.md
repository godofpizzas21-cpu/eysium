# The Elysium Atlas — Architecture

**Document ID:** `eng.architecture`
**Status:** Proposed
**Version:** 1.1.0
**Applies to:** Phases 17–25
**Governs:** everything under `app/`

---

## 1. What Is Being Built

A **static, single-page, client-only** browser application that renders the
Civilization Bible as an explorable 3D globe. No server, no database, no
authentication, no API keys. The 29 canon datasets ship as static assets; the
app fetches and renders them.

This constraint is deliberate and permanent. A static build can be hosted
anywhere, archived intact, and will still run in ten years. It is the
redundancy principle applied to the deliverable.

## 2. Stack Decisions

Each decision below records the alternative rejected, because a specification
that only states conclusions cannot be argued with later.

| Concern | Decision | Rejected | Why |
|---|---|---|---|
| Build | **Vite 5** | Next.js, Webpack | No server rendering is wanted; Vite's static output is the whole requirement |
| Language | **TypeScript, `strict: true`** | JavaScript | 1,071 canonical entities with typed shapes — the type system is doing real work |
| UI | **React 18** | Svelte, Vue | Fixed by the brief |
| 3D | **Three.js via react-three-fiber + drei** | Raw Three.js; **ThreeGlobe** | See §2.1 |
| State | **Zustand** | Redux Toolkit, Context | See §2.2 |
| Routing | **A 30-line URL sync** (`src/lib/url.ts`) | React Router | See §2.4 |
| Styling | **CSS Modules + custom properties** | Tailwind, CSS-in-JS | See §2.3 |
| Data validation | **Zod**, at build time only | Runtime validation | Canon is fixed at build; runtime checks would cost bytes for no benefit |
| Testing | **Vitest** + **Playwright** | Jest | Vitest shares Vite's transform pipeline; Playwright covers the WebGL paths unit tests cannot |

### 2.1 Why not ThreeGlobe

The brief permits "ThreeGlobe or equivalent". ThreeGlobe is rejected for three
specific reasons:

- It carries **its own data model** (points, arcs, hex-bins) that our
  schema-first datasets would have to be reshaped into, inverting the project's
  core principle that the Bible is the source of truth.
- The Atlas needs **twenty-odd custom layers** — protected areas, grid, freight
  corridors, orbital shells — several of which are not points or arcs.
- It is **imperative**, and reconciling an imperative scene graph with React
  state by hand is the exact class of bug r3f exists to remove.

**react-three-fiber** keeps the scene graph declarative and reconciled by React,
which means a layer is a component and layer visibility is ordinary state. The
cost — a reconciliation layer between React and Three — is real and accepted.

### 2.4 Why not React Router

This specification originally named React Router 6. Phase 19B replaced it, and
the reasoning is recorded rather than quietly applied.

The Atlas has **no nested routes, no route-level data loading, and no
navigation guards**. It needs one thing: the focused entity id reflected in the
URL and restored from it. That is three functions over `history.pushState` and
`popstate`, which is what `src/lib/url.ts` contains. A routing library would
have added roughly 15 kB gzipped to the initial bundle to solve a problem the
application does not have.

If deep-linked layers, time positions, and space mode later need real route
composition, this decision should be revisited — the URL grammar in §4 is
unchanged and already anticipates them.

### 2.2 Why Zustand

The render loop must read state **outside React's render cycle** (camera
targets, hover state at 60 fps). Context would re-render the tree on every
change; Redux would add substantial ceremony for a single-user, single-session
app with no async mutations. Zustand's store is readable imperatively from
inside `useFrame` and subscribable selectively, which is precisely the shape of
this problem.

Store slices: `selection`, `layers`, `camera`, `time`, `search`, `preferences`.

### 2.3 Why CSS Modules and not Tailwind

The Atlas has a **canon-derived palette** (`eng.design-system` §2) with roughly
forty semantic tokens that must be readable from both CSS and TypeScript,
because the same colours paint DOM panels and Three.js materials. A single
source of custom properties, imported into both, is the honest solution. Tailwind
would require duplicating the palette into a config and would not help the WebGL
side at all.

## 3. Folder Structure

```
app/
├── index.html
├── vite.config.ts
├── tsconfig.json
├── package.json
├── public/
│   └── data/                  # canon datasets, copied by the pipeline
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── scene/                 # everything inside the WebGL canvas
│   │   ├── Globe.tsx
│   │   ├── Atmosphere.tsx
│   │   ├── Terminator.tsx
│   │   ├── Camera.tsx         # fly-to, damping, reduced-motion handling
│   │   └── primitives/        # shared geometry: arcs, markers, polygons
│   ├── layers/                # one folder per map layer
│   │   ├── registry.ts        # the only place layers are enumerated
│   │   ├── political/
│   │   ├── ecology/
│   │   ├── transport/
│   │   └── …
│   ├── panels/                # DOM UI outside the canvas
│   │   ├── EntityPanel.tsx
│   │   ├── RecordDrawer.tsx   # the signature element
│   │   ├── LayerSwitcher.tsx
│   │   └── Search.tsx
│   ├── a11y/                  # the parallel non-visual interface (§5)
│   ├── data/                  # loaders, generated types, indexes
│   ├── state/                 # zustand slices
│   ├── lib/                   # geo math, colour, formatting, Elysian dates
│   └── styles/                # tokens.css and module styles
└── tools/                     # build-time scripts (data pipeline entry)
```

**The layer registry is the single extension point.** Adding a map layer means
adding a folder and one registry entry. Nothing else in the app enumerates
layers — not the switcher, not the URL parser, not the accessible tree.

## 4. Routing and Deep Links

The URL is application state, so any view can be shared or bookmarked:

```
/                                     the globe, default layer
/layer/ecology                        a layer selected
/entity/city.kessandra-reach          an entity focused, panel open
/entity/polity.sirocc?layer=energy    both
/space                                orbital mode
/at/EY-0300-M01-D01                   the time scrubber positioned
```

Entity IDs in URLs are the canonical IDs from `charter.canon-rules` §3.2, which
are immutable — so a link shared today still resolves in ten years even if a
display name changes.

## 5. Two Interfaces, One Application

**This is an architectural requirement, not an accessibility afterthought.**

A WebGL globe is unusable to a screen-reader user and to anyone who cannot use a
pointer. The Atlas therefore ships **a parallel, complete, non-visual interface**
over the same state and the same data: a navigable tree of continents → Regions →
cities → entities, with every panel reachable, every layer switchable, and every
figure readable.

- The `<canvas>` is `aria-hidden`. It is decoration for assistive technology.
- `src/a11y/` renders the real accessible document from the same Zustand store.
- Selecting an entity in either interface selects it in both.
- Every action available by clicking the globe is available by keyboard.

The Concord requires accessibility as-built rather than on request
(`city.urbanism` §4). Canon's own rule is the specification's rule.

## 6. Build and Deployment

```
npm install
npm run data:build     # validate canon, emit public/data + generated types
npm run dev            # local development
npm run build          # static output to app/dist
npm run preview        # verify the production build locally
```

**Vercel:** root directory `app`, framework Vite, build `npm run build`, output
`dist`. `data:build` runs as part of `build`, so a canon error fails the deploy
rather than shipping a broken atlas. The repository's own `tools/lint_canon.py`
runs first in that chain.

## 7. Non-Goals

Stated so later phases do not drift into them: no user accounts, no persistence
of user data, no editing of canon through the UI, no multiplayer, no server-side
rendering, no analytics, and no advertising of any kind.

## 8. Open Threads

- Data pipeline, schemas, generated types, sharding → `eng.data-pipeline`
- Palette, typography, motion, the signature element → `eng.design-system`
- Layer implementations → Phase 21
- Space mode → Phase 23
