# Changelog — Project Elysium

Newest first. Format defined in `docs/charter/VERSIONING.md`.

## [phase-25] — Documentation, Testing & Release Polish — **project complete**
### Added
- docs/engineering/ACCESSIBILITY.md (eng.accessibility 1.0.0) — conformance statement with verified ratios and a stated list of known gaps
- docs/engineering/DEPLOYMENT.md (eng.deployment 1.0.0) — hosting, changing canon, adding a layer, and what to do when a check fails
- app/tools/check-contrast.ts — measures every text and border pairing on its actual painted surface, wired into the build
- app/src/a11y/Announcer.tsx — polite live region announcing selection and layer changes
- app/src/a11y/Shortcuts.tsx — discoverable keyboard reference, opened with `?`
- app/src/a11y/ErrorBoundary.tsx — if the renderer fails, the accessible interface survives
- Skip link past the globe, and the accessible tree promoted to a `<main>` landmark
### Fixed (found by the contrast audit)
- **`--shelf` measured 2.86:1 as an interface border on a raised surface, below the 3:1 that eng.design-system section 7 requires.** Rather than lower the threshold or alter a canon colour, a derived `--shelf-edge` token was introduced at 3.06:1 and used wherever the accent carries an edge. The canon colour is unchanged and remains correct as a fill
### Changed
- README.md rewritten as the project front door
- app/package.json — `check:contrast` added to `build` and `verify`
### Verified by building and running it
- Full chain green: canon lint, schema validation, typecheck, 111 smoke tests, contrast audit, bundle, budget
- All ten contrast pairings pass: body text 6.6-9.7:1, strong text 11.1-13.7:1, focus ring 13.7:1, borders 3.1-4.5:1
- Initial JS 66.5 kB gzipped against a 220 kB target; eager data 33.2 kB against 40 kB
### Decisions (Proposed → Canon on phase approval)
- **The accessibility statement lists its gaps.** No testing with real assistive technology, no browser-level audit in CI, and colour-blindness differentiation reasoned rather than simulated. A conformance claim without a gap list is not credible, and canon's own habit is to publish failures
- The contrast audit runs in the build, so a palette change that breaks a ratio fails rather than ships
- The Atlas's own accessibility argument is borrowed from the Concord: a right of access is worth what someone's willingness to use it is worth, and an interface nobody can operate has the same problem

## [phase-24] — Advanced Overlays & the Record Drawer
### Added
- Three layers, each costing **one registry entry and nothing else** — proving the extension point works as `eng.architecture` section 3 claimed:
  - **Protected areas** — the four protection tiers over 44% of land and 38% of ocean, shown through the biomes they cover and the hazards they answer
  - **Governance** — the distributed capital's five seats on five continents, and the 34 Regions that send delegates to it
  - **Materials** — where the Concord's minerals come from, including the three on the Constrained List
- app/src/data/record.ts — record retrieval: fetches an entity's own dataset and finds the entry
### Changed
- **app/src/panels/EntityPanel.tsx — the Record Drawer is now complete.** Phase 17 promised the canonical id, the Bible chapters that canonize it, the raw entry, and the dataset version; Phase 19A delivered the first two. All four are now shown, with the raw entry rendered as plain monospace exactly as a Record Office terminal would
- app/tools/smoke.ts — 111 checks, adding record retrieval across a sample of the index and a version check on every dataset
### Verified by building and running it
- Full chain green; 111 smoke tests pass; 12 layer manifests emitted
- Initial JS 65.8 kB gzipped, eager data 33.2 kB, renderer 243.8 kB lazy — within budget
- The pipeline refused the protection layer's first geometry source, because restoration programmes carry area but name no places. Corrected rather than worked around
### Decisions (Proposed → Canon on phase approval)
- **The Record Drawer closes when the selection changes**, so it can never show the previous entity's record
- Records are fetched on demand rather than held in the index, keeping the eager payload at 33 kB while still letting any of 1,071 entities produce its own entry
- The raw entry is shown as unhighlighted monospace with a focusable scroll region — the drawer is a record, not a code sample
- Adding three layers required no change to the renderer, the switcher, the keyboard shortcuts, or the accessible tree, which was the point of building the registry that way

## [phase-23] — Space Mode — **all nine layers draw**
### Added
- app/src/scene/OrbitalSystem.tsx — Kalyra and Vesper at true relative distance and size, orbiting on their canonical periods against the Elysian clock, with the stationary ring and the Low Ring shell
- app/src/panels/OffWorld.tsx — off-world settlement by location, and the Belt reported with its light lag and transit time
### Changed
- app/tools/layers.ts — a fifth geometry kind, `orbit`, requiring `orbitalDistanceKm`; the space layer declares `view: "space"`
- app/tools/build-data.ts — validates the new kind
- app/src/scene/Controls.tsx — the camera envelope follows the active layer's view, opening to 90 planet radii in space mode so Kalyra fits at 61.75
- app/src/panels/Legend.tsx — the "geometry arrives later" note now keys off whether a layer actually declares geometry, rather than a hardcoded phase
- app/tools/smoke.ts — 88 checks, adding the orbit kind and six on the orbital system
### Verified by building and running it
- Full chain green; 88 smoke tests pass
- Initial JS 65.4 kB gzipped, eager data 33.2 kB, renderer 243.8 kB lazy — within budget
- The orbital tests confirm both moons carry orbit geometry, that they orbit outside the planet, that the stationary ring sits inside Vesper's orbit, and that Kalyra orbits beyond Vesper and more slowly
### Decisions (Proposed → Canon on phase approval)
- **The moons are drawn at true relative scale.** One render unit is 6,510 km, so Kalyra really does sit 61.75 planet radii out and Vesper really is small and fast. Only Vesper's drawn radius carries a floor, so it stays clickable rather than becoming a pixel
- **The Tyrran Belt is not drawn, and the Atlas says why.** At 2.3 AU it lies some 52,800 render units out — four orders of magnitude beyond Kalyra — and any diagram placing it in view would misrepresent the distance. It is reported in the panel with its 10-38 minute light lag and 8-14 month transit instead. Canon is candid about scale, so the Atlas is
- The Low Ring is drawn as a shell rather than 3,400 individual objects, which would be noise at this scale
- Space mode is declared by the layer rather than held as separate application state, so the camera envelope follows the manifest like everything else

## [phase-22] — Atmosphere & Dynamics
### Added
- app/src/lib/calendar.ts — **the Elysian calendar in code**: 12 months of 32 days, 8-day weeks, Thresholdday outside both, and 26 civil hours of 60 minutes of 60 beats. No JavaScript `Date` object appears anywhere in the application
- app/src/lib/sun.ts — subsolar point from the 19.4-degree tilt and the 384.24-day year, plus daylight length by latitude
- app/src/scene/Atmosphere.tsx — terminator lighting driven by Helia's actual position, and the running clock
- app/src/scene/Clouds.tsx — procedural cloud shell following the canonical three-cell circulation: a migrating ITCZ band, dry subtropical belts at the Hadley descent, and mid-latitude storm cloud
- app/src/panels/ClockPanel.tsx — civil date and time, a time-of-day scrubber, day stepping, and a run control
### Changed
- app/src/data/loader.ts — calendar.json joins the eager set at 1.6 kB gzipped
- app/src/state/store.ts — the clock, opening at the Bible's reference date of EY 412, Calenth 16
- app/src/scene/Globe.tsx — ambient rotation slowed, since the terminator now carries the sense of time
- app/tools/check-budget.ts — the eager list had gone stale again and was omitting calendar.json
- app/tools/smoke.ts — 82 checks, adding twelve on the calendar
### Verified by building and running it
- Full chain green; 82 smoke tests pass
- Initial JS 65.1 kB gzipped, eager data 33.2 kB, renderer 242.5 kB lazy — within budget
- The calendar tests confirm 12 x 32 = 384, that 384 divides evenly into 8-day weeks so the calendar is perpetual, that the leap rule yields the 384.24-day solar year to within 0.005 days, and that **a civil hour is 3,586.15 seconds and demonstrably not an SI hour**
### Decisions (Proposed → Canon on phase approval)
- **The terminator is computed, not decorated.** Declination follows from the tilt and the position in the year, and canon fixes the year's start at the northward equinox, so declination is zero on Verane 1. The day/night line therefore tilts with the season and sweeps at Elysium's own rate
- **Clouds follow canon rather than a texture.** The band structure is the three-cell circulation of `planet.climate` section 2, with the ITCZ migrating between 9 degrees south and north over the year — the narrow swing the gentle tilt produces
- The clock opens at **EY 412, Calenth 16**, the reference date every figure in the Bible is stated against
- The globe's ambient rotation was slowed rather than removed: the terminator now conveys time, so spinning to suggest it would be redundant
- The glare rule holds in three dimensions: one warm directional light, low ambient so the night side is genuinely dark, and an atmospheric limb at 7% opacity rather than a glow

## [phase-21b] — Layer Polish
### Added
- app/src/panels/Swatches.tsx — legend swatches showing the canon palette directly, each one a button that focuses the entity and flies the camera
- app/src/scene/HoverLabel.tsx and app/src/lib/hoverLabel.ts — hover labels projected each frame and rendered as real DOM text
### Changed
- app/src/layers/LayerGeometry.tsx — four symbol shapes (sphere, octahedron, box, cone) assigned per geometry source
- app/src/panels/Legend.tsx — swatches folded into the legend
- app/tools/smoke.ts — 71 checks, adding verification that every palette-painted layer has swatches carrying real hex values
### Verified by building and running it
- Full chain green; 71 smoke tests pass
- Initial JS 63.6 kB gzipped, eager data 31.7 kB, renderer 241.0 kB lazy — within budget
### Decisions (Proposed → Canon on phase approval)
- **Shape carries meaning alongside colour.** `eng.design-system` section 7 requires colour never to be the only channel, so each geometry source gets a distinct silhouette that survives any colour vision deficiency and greyscale print
- **The legend is a navigation surface, not a key.** Every swatch is a button: hovering highlights the entity on the globe, selecting focuses it and flies the camera. The swatch list is literally the canon palette, read from each entity's own `palette` field
- **Hover labels are DOM text, not textures**, so they honour the user's font size and never blur. The scene projects the point and moves the element; nothing enters the store, so the label costs no re-renders at 60 fps
- React context does not cross the react-three-fiber reconciler boundary, so the two halves of the label meet through a small module rather than a provider — the alternative, pushing screen coordinates into the store each frame, would re-render the tree every frame

## [phase-21a] — Map Layers: Geometry
### Added
- app/src/layers/LayerGeometry.tsx — manifest-driven renderers for all four geometry kinds; it knows nothing about which layer it draws, so adding a layer needs no change here
### Fixed (found by writing the renderer)
- **The layer registry promised geometry the data cannot provide.** Four layers declared `region-fill` from sources that carry no polygons — biomes and climate zones are canonized as areas, latitude bands, and region references, not outlines. The registry now declares only what the datasets support
- The pipeline gained geometry validation: each kind states what its source entities must carry, and a layer whose source cannot supply it fails the build. This caught two further layers whose sources name places through `bestRegions` and `biome` rather than `regions`
### Changed
- app/tools/layers.ts — geometry kinds reduced to the four the data supports: `arc`, `latitude-band`, `point`, `region-point`
- app/tools/build-data.ts — geometry validation, with coverage notes where a source only partly supports a kind
- app/src/data/layers.ts — runtime geometry type aligned with the registry
- app/tools/smoke.ts — 13 further checks, one per declared geometry, verifying every layer is drawable
- docs/charter/DATA_SCHEMA.md 1.12.0 → 1.13.0 — the biome-polygon gap recorded, so the absence is visible rather than mistaken for an oversight
### Verified by building and running it
- Full chain green; 69 smoke tests pass
- Initial JS 63.1 kB gzipped, eager data 31.7 kB, renderer 240.4 kB lazy — all within budget
- Coverage notes are honest data facts: 33/34 Regions have label points because the Orbital Territory has no location; 10/11 climate zones have bands because H1 is an overlay class; 1/5 century programmes name regions
### Decisions (Proposed → Canon on phase approval)
- **Four geometry kinds, each stating what its data must carry.** `arc` needs a path, `latitude-band` needs a band, `point` needs coordinates, `region-point` needs a reference to somewhere located. The pipeline enforces the contract, so a layer cannot promise geometry the Bible does not hold
- Climate bands are mirrored into both hemispheres, because canon states them as absolute latitudes
- Point symbols scale on a cube root, so area rather than radius reads proportionally
- Where a dataset names places through a field other than `regions` — `bestRegions`, `deposits`, `biome`, `polity` — the renderer follows it, because canon uses several such fields and inventing a uniform one would mean editing the Bible to suit the renderer

## [phase-20] — UI Shell
### Added
- app/src/data/layers.ts — manifest and layer loading, dot-path source resolution, and **counterweight pairing enforced at the data level**
- app/src/panels/LayerSwitcher.tsx — switcher over the nine registered layers, driven entirely by the generated manifests, with number keys 1-9 and 0 to clear
- app/src/panels/Legend.tsx — layer summary and indicators, each rendered as one card with its counterweight
### Changed
- app/src/state/store.ts — layer state, bundle caching so switching back is instant, and an injected loader so the store never imports it
- app/src/App.tsx — the side column now holds the switcher, legend, and accessible tree as one scrolling region
- app/src/styles/app.css — layer and indicator styling; narrow layout stacks the side column under the globe
- app/tools/smoke.ts — extended from 12 to 56 checks: every layer's datasets must be emitted, every indicator a layer surfaces must exist, and both halves of every counterweight pair must exist
### Verified by building and running it
- Full chain green: canon lint, schema validation, typecheck, 56 smoke tests, bundle, budget
- Initial JS 62.9 kB gzipped (target 220), eager data 31.7 kB (target 40), renderer 239.0 kB lazy
- Confirmed a layer promising a nonexistent indicator fails the build
### Decisions (Proposed → Canon on phase approval)
- **The counterweight rule is enforced in the data layer, not in a component.** `metric.system` section 2 says an indicator may not be published without its counterweight; pairing them in `loadIndicators` means no view can show one half by accident, and the smoke tests verify both halves exist
- The switcher enumerates nothing itself — it reads the manifests generated from the registry, so adding a layer to `tools/layers.ts` adds it to the UI, the keyboard shortcuts, and the accessible tree at once
- Layer bundles are cached on first load, so switching back is instant and costs no network
- A layer that has not yet been given geometry says so plainly, naming the phase it arrives in, rather than rendering an empty globe

## [phase-19b] — Picking, Fly-to Camera & Search
### Added
- app/src/scene/Markers.tsx — 37 clickable city markers, seats of the distributed capital drawn larger, each with an invisible hit sphere well above the 44 px pointer-target floor
- app/src/scene/CameraRig.tsx — animated fly-to that slerps the camera over the surface rather than through the planet, with an instant cut under reduced motion
- app/src/panels/Search.tsx — combobox search across all 1,071 entities with full keyboard support and an ARIA listbox
- app/src/lib/url.ts — URL synchronisation in both directions, using immutable canonical ids
- app/tools/smoke.ts — twelve behavioural tests over the emitted data, wired into the build
### Changed
- app/src/state/store.ts — camera targeting, search scoring, and location resolution, including continent centroids derived from labelled features
- app/src/a11y/AccessibleAtlas.tsx — cities added, so both interfaces reach the same entities and selecting in either flies the camera
- app/src/data/loader.ts — cities.json joins the eager set at 6.6 kB gzipped
- app/tools/check-budget.ts — corrected: it was omitting cities.json from the eager set and misclassifying three lazy chunks as initial
- **docs/engineering/ARCHITECTURE.md 1.0.0 → 1.1.0 — React Router was specified in Phase 17 and is not used.** The Atlas has no nested routes, no route-level loading, and no guards; it needs the focused entity id in the URL, which is three functions over history.pushState. A routing library would have added ~15 kB gzipped to solve a problem the application does not have. The decision and the conditions for revisiting it are recorded in the spec rather than applied silently
### Verified by building and running it
- Full chain green: canon lint, schema validation, typecheck, smoke tests, bundle, budget
- Initial JS 61.6 kB gzipped (target 220), eager data 31.7 kB (target 40), renderer 239.0 kB lazy
### Decisions (Proposed → Canon on phase approval)
- **Selection is one action wherever it happens.** Clicking a marker, choosing a search result, or activating an item in the accessible tree all run the same `select`, which focuses the entity, updates the URL, and flies the camera
- The camera **slerps over the surface** rather than lerping through the planet, and honours reduced motion by cutting instantly
- Search runs on the eager index, so it works before any layer loads, and scores exact match above prefix above substring above id above tag
- Escape closes the panel from anywhere; back and forward navigate selection history

## [phase-19a] — Globe Core — **the Atlas runs**
### Added
- app/vite.config.ts, index.html, vercel.json — static build configured for Vercel
- app/src/styles/tokens.css — **generated from data/biomes.json**, so the palette is read from canon rather than chosen
- app/src/styles/app.css — application styles built entirely on those tokens
- app/src/lib/geo.ts — the only place degrees become vectors: projection, antimeridian unwrapping, ring densification, great-circle distance
- app/src/data/loader.ts — eager canon loading with caching
- app/src/state/store.ts — zustand store shared by both interfaces
- app/src/scene/Globe.tsx — ocean sphere, atmospheric halo, and continent geometry tessellated with earcut and projected onto the sphere
- app/src/scene/Controls.tsx — Three's own OrbitControls with keyboard events bound
- app/src/scene/Stage.tsx — the lazy renderer boundary
- app/src/a11y/AccessibleAtlas.tsx — the parallel interface, navigable and visible
- app/src/panels/EntityPanel.tsx — entity panel with the **Record Drawer**
- app/tools/check-budget.ts — build-time performance budget enforcement
### Fixed (single source of truth, raised during review)
- **The reference-field list existed in two places and had drifted: the Python linter checked 111 fields, the TypeScript pipeline checked 12 — meaning the pipeline silently ignored 100 of them.** Extracted to tools/reference-fields.json, now read by both. Verified by injecting a bad reference into a previously-ignored field, which the pipeline now catches
- The linter learned that `sourceDataset` holds a filename rather than an entity ID, and validates it as such
### Verified by building and running it
- `npm run build` completes: canon lint, schema validation, reference resolution, emit, types, typecheck, bundle, budget check
- **Initial JS 60.2 kB gzipped against a 220 kB target**; eager data 25.5 kB against 40 kB; renderer 237.6 kB lazy and off the critical path
- The budget check was confirmed to fail by tightening a limit, and it caught two genuine breaches during the phase
### Decisions (Proposed → Canon on phase approval)
- **The renderer is lazy.** Three.js would breach the initial-JS budget, so the accessible interface — the real document — paints first and the globe streams in behind it. If WebGL never arrives, the Atlas still works
- **drei was removed.** Its barrel import pulled roughly 750 kB of unused helpers into the renderer chunk; Three's own OrbitControls is forty lines and one import
- **The eager index carries no summaries.** They are 44 kB across 1,071 entities, are only needed once an entity is selected, and would have breached the eager-data budget — which the budget check caught. Search runs on name and tags; summaries come from the loaded dataset
- Tokens are generated from the canon palette, so changing a biome colour in the Bible repaints the Atlas
- The green rule is implemented: `--anomaly` is the only green token and is used solely for the error notice
- Keyboard control of the globe is bound at the controls level rather than added later, because arrow-key rotation is a requirement rather than an enhancement

## [phase-18] — Data Layer
### Added
- app/ — the application scaffold: package.json, tsconfig.json (strict, `noUncheckedIndexedAccess`), .gitignore, README.md
- app/tools/schemas/common.ts — the charter's entity envelope, ID domains, and geometry primitives as Zod
- app/tools/schemas/datasets.ts — strict schemas for the nine datasets the Atlas renders directly
- app/tools/layers.ts — **the layer registry**, the single place map layers are enumerated
- app/tools/build-data.ts — the five-stage pipeline
### Fixed (found by the new pipeline)
- **31 entities across three datasets were missing the `summary` or `sources` fields that charter.data-schema section 2 requires of every entity.** The Python linter had never checked the envelope; the Zod schema does. All 31 were given real summaries and sources rather than placeholders, since they surface in Atlas panels — continents.json 1.1.1 → 1.1.2, climate-zones.json 1.0.0 → 1.0.1, planet-physical.json 1.1.0 → 1.1.1
### Changed
- docs/charter/DATA_SCHEMA.md 1.11.0 → 1.12.0 — records that the envelope is now machine-checked
- docs/charter/PROJECT_CHARTER.md 1.8.0 → 1.9.0 — app/ layout expanded
- README.md — application section, status table
### Verified by running it
- The pipeline runs end to end: **29 datasets, 1,071 entities (106 with coordinates), 9 layer manifests, types generated**
- `tsc --noEmit` passes under strict mode with `@types/node`; two genuine strict-mode errors were fixed rather than suppressed
- Failure paths tested by injecting a dangling reference, a negative population, and a missing summary into cities.json: all three were caught and the pipeline exited 1
### Decisions (Proposed → Canon on phase approval)
- **Zod schemas are the single description of every dataset's shape**, and TypeScript types are generated from them. A hand-written type would be a second description of the same thing
- **Every entity anywhere in any dataset is validated against the charter envelope**, not only those in datasets with strict schemas — which is how the 31 violations surfaced
- The pipeline runs `tools/lint_canon.py` as stage 1, so the application build inherits all 25 canon checks and a canon error fails the deploy
- `entity-index.json` carries id, name, summary, tags, dataset origin, and coordinates for all 1,071 entities in roughly 40 kB, so search and the accessible tree work before any layer loads
- Each index entry records **which dataset it came from**, which is what makes the Record Drawer possible
- The layer registry drives the generated manifests, and the pipeline fails if a layer names a dataset or indicator that does not exist — a layer cannot promise data the Bible does not hold
- Nine layers registered: political, ecology, climate, transport, population, energy, economy, research, and space

## [phase-17] — Software Architecture & Specification
### Added
- docs/engineering/ARCHITECTURE.md (eng.architecture 1.0.0) — stack decisions with rejected alternatives, folder structure, routing, the two-interface requirement, build and deployment
- docs/engineering/DATA_PIPELINE.md (eng.data-pipeline 1.0.0) — the one-way canon flow, five pipeline stages, Zod schemas as the single shape description, loading strategy, layer manifests, geometry handling, the Elysian calendar in code
- docs/engineering/DESIGN_SYSTEM.md (eng.design-system 1.0.0) — palette read from canon, typography, the signature element, motion, performance budgets, accessibility requirements, interface voice
### Changed
- docs/charter/DATA_SCHEMA.md 1.10.1 → 1.11.0 — registered the eng. prefix
- docs/charter/PROJECT_CHARTER.md 1.7.0 → 1.8.0 — engineering documents added to the repository layout
- README.md — engineering specification index, status table
- tools/lint_canon.py — added check_engineering_specs: **any biome cited as a palette source must exist and its canonical hex must appear in the spec**, the green-as-exotic rule must be carried, and every engineering document must declare an eng. document ID (verified by changing a canon palette value, which it caught)
### Decisions (Proposed → Canon on phase approval)
- The Atlas is **static, client-only, and permanently so** — no server, no database, no accounts. A static build can be hosted anywhere and archived intact, which is the redundancy principle applied to the deliverable
- **react-three-fiber over ThreeGlobe**, with reasons recorded: ThreeGlobe carries its own data model that our schema-first datasets would have to be reshaped into, it does not extend to twenty-odd custom layer types, and reconciling an imperative scene graph with React state by hand is the bug class r3f exists to remove
- **Zustand over Redux or Context**, because the render loop must read state outside React's render cycle at 60 fps
- **CSS custom properties over Tailwind**, because the same palette paints DOM panels and Three.js materials and must be readable from both
- **Two interfaces, one application.** The canvas is `aria-hidden` and a complete parallel non-visual interface runs over the same state — architecture, not afterthought. Canon's own accessibility-as-built rule becomes the specification's rule
- URLs carry immutable canonical entity IDs, so a link shared today resolves in ten years even if a display name changes
- **Canon flows one way.** `data/` is authoritative, `app/public/data/` is a gitignored build artifact, and `tools/lint_canon.py` runs as stage 1 of the app build — so a canon error fails the deploy rather than shipping a broken atlas
- **No JavaScript `Date` object anywhere in the application**, because using one would silently import Earth's calendar into a planet that does not have it
- **The palette is read from canon, not chosen.** Tokens derive from `biomes.json`, so a palette change in the Bible repaints the Atlas
- **The green rule**: canon records green as the exotic pigment signalling strangeness or sickness, so no interface element is green in its normal state and green is reserved exclusively for anomaly. Canon's symbolism becomes a functional affordance
- **The glare rule**: Elysian cities glow rather than glare, so no pure white, no bloom, no neon
- **The signature element is the Record Drawer** — any entity can show you its canonical ID, the Bible chapter that canonizes it, and its raw dataset entry. The right of access to record, expressed as an interface
- Paired counterweights are enforced as a layout rule: a gameable indicator never appears without its counterweight in the same card
- Performance budgets and accessibility requirements are checked in CI, because a rule nobody measures is a rule nobody keeps

## [phase-16] — Metrics & Indicators — **the Civilization Bible is complete**
### Added
- docs/bible/metrics/system.md (metric.system 1.0.0)
- docs/bible/metrics/indicators.md (metric.indicators 1.0.0) — generated from the dataset so prose and data cannot drift
- data/metrics.json (1.0.0) — 5 producers, 6 principles, the Unmeasured Register, **48 indicators across 12 domains**, 5 known weaknesses
### Method
- The Phase 16 drafts quarantined during the phase-15 completion pass were audited before adoption: **all 46 checkable indicator values were verified against their domain datasets and every one matched exactly.** The drafts were adopted, domains added, and the `derivedFrom` field replaced with a validated `sourceDataset` filename plus an explicit `derivation` for the two non-administrative entries
### Changed
- docs/charter/DATA_SCHEMA.md 1.10.0 → 1.10.1
- docs/glossary/GLOSSARY.md 1.22.0 → 1.23.0 — 3 new terms (309 total)
- tools/lint_canon.py — added check_metrics, which binds **42 indicators to the exact canonical location each derives from** and fails if either the indicator or its source moves; also requires each indicator to declare provenance exactly one way, forbids more than one declared composite, and forbids an empty Unmeasured Register (verified by drifting a value in each direction)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- **No single body owns Elysian statistics.** The Statistical Council defines terms and arbitrates comparability and may publish nothing of its own — the audit principle applied to measurement
- **No composite headline index.** Proposed four times, defeated four times. A single number invites optimisation and hides the tradeoffs Elysian politics exists to argue about
- **Distributions, not central values**: a median without a spread is treated as misleading rather than incomplete
- **Paired counterweights**: custody rate beside reoffending, clearance beside wrongful conviction, screening coverage beside over-diagnosis, reserve margin beside islanding failure. The pairing is part of the definition and an indicator may not publish without its pair
- **No indicator attaches to an individual**, generalised from the schooling rule: a measure attached to a person becomes a target for that person
- **Revision transparency**: every restatement publishes the superseded series permanently, so Elysians can see every number the Concord has changed its mind about
- **Indicators are not targets by default**; adopting one as a target needs an Assembly resolution and an automatic sunset
- **The Unmeasured Register** publishes what the Concord believes matters and cannot measure — including whether its institutions would survive a genuine external shock, an entry standing since EY 61
- Indicators inform argument and allocate nothing: fiscal equalization runs on taxable capacity, not outcomes, so that measuring a Region cannot become a way of funding or defunding it
- The six indicators Elysians watch most are all stubborn — wealth Gini, overturning strength, the beryllium horizon, late-life cognitive decline, reoffending, and trust in the Concord tier — and canon records that a list of six unresolved problems published annually is roughly what a healthy civilization's indicator set should look like

## [phase-15] — Space Infrastructure & Diplomacy
### Added
- docs/bible/space/infrastructure.md (space.infrastructure 1.0.0)
- docs/bible/space/external.md (dipl.external 1.0.0)
- data/space.json (1.0.0) — off-world population and 5 settlements, orbital mechanics, the Kalyra Far-Side Array, the Belt, the light-lag rule, Marn protection, exploration and the Long Signal, 5 space-law instruments, the Orbital Territory problem and 3 reforms, external relations, the 5-step Reception Protocol, 12 known weaknesses
### Fixed (found in audit)
- dipl.external compared the Orbital Territory's representation against **Elandris, a continent of nine Regions**, rather than against a single Region. Corrected to Kessandra, the most populous Region: 88.75 million per seat against 7 million, a ratio of thirteen to one rather than eighty-two
- a prose string sat in the `sharedAdvisoryPanelWith` reference field; moved to a note
### Changed
- docs/bible/government/regions.md and docs/bible/energy/generation.md — Phase 15 open threads closed
- docs/charter/DATA_SCHEMA.md 1.9.3 → 1.10.0 — split space. from dipl.
- docs/glossary/GLOSSARY.md 1.21.0 → 1.22.0 — 7 new terms (306 total)
- tools/lint_canon.py — added check_space: off-world settlement populations must sum and agree with demographics.json, Orbital Territory seats and population per seat must follow from regions.json, **stationary orbit altitude must be derivable from the planet's own mass and sidereal day**, candidate signals must all remain resolved, first contact may not be asserted, Marn must remain unlanded, and the light-lag rule must remain unrelaxed (verified against injected errors, including the exact continent-for-Region mistake found in audit)
- README.md — Bible index, status table
### Fixed (beryllium audit, requested review of the Tyrran Belt)
- **The beryllium reserve horizon did not follow from its own definition.** planet.resources defines a reserve horizon as years of supply at *net* consumption after recovery; applying that to the stated 0.9 Mt reserve, 7,500 t/yr consumption, and 91% recovery gives 1,333 years, not the 120 that Phases 7A, 8B, 12 and 15 all depend on. energy.generation also contradicted itself, claiming 91% recovery turned a 30-year horizon into a 120-year one, which is arithmetically impossible
- Corrected to the single self-consistent chain the prose itself pointed at: **gross consumption 30,000 t/yr, recovery 75%, net virgin draw 7,500 t/yr, 30 years without recovery, 120 years with.** 75% also fits the stated reason recovery cannot go higher — neutron-activated beryllium is difficult to reprocess
- Updated data/resources.json 1.0.0 → 1.1.0, data/energy.json 1.0.0 → 1.1.0, tools/build_energy.py, docs/bible/planet/resources.md 1.0.0 → 1.1.0, docs/bible/energy/generation.md 1.0.0 → 1.1.0, docs/bible/space/infrastructure.md 1.0.0 → 1.1.0
- space.infrastructure now states the Belt's actual effect: 11% of net virgin draw extends the horizon from 120 years to roughly 135 — real, worth having, and not a solution
- tools/lint_canon.py — added check_reserve_horizons, which requires any material declaring a reserve, gross consumption, and recovery rate to satisfy canon's own definition arithmetically, and cross-checks beryllium between resources.json, energy.json, and space.json (verified by reinstating the original 91% figure, which it caught)
### Fixed (phase-15 completion pass)
- **34 stale forward-references to "Phase 15" across 19 Bible chapters and 2 datasets** were resolved to the documents that now exist (`space.infrastructure`, `dipl.external`), discharging the CANON_RULES section 6 consistency obligation. tools/build_regions.py updated so regeneration cannot reintroduce one
- Premature Phase 16 draft artifacts (data/metrics.json and an empty docs/bible/metrics/) appeared in the working tree and were failing lint with 48 dangling references; quarantined outside the repository pending founder approval of Phase 16
### Decisions (Proposed → Canon on phase approval)
- **The honest answer to why the Concord is in space is beryllium.** Space activity was an industrial programme with an astronomical side-effect, and Elysians are unromantic about this in a way visitors find deflating
- 28 million off-world across the Low Ring (14.2 M), Kalyra (7.4 M), Vesper (3.1 M), the Belt (2.1 M), and transit (1.2 M). **94% of orbital structural mass has never been on Elysium**
- Vesper came first because orbital mechanics said so; Kalyra is where people settled; the **Kalyra Far-Side Array** sits behind 1,290 km of rock in a legally protected radio quiet zone
- **The light-lag rule** is the phase's central idea: Cassian Rule 4 requires the accountable human to have the capacity to refuse, which nobody on Elysium has across a 10–38 minute lag. The named human must be within a **4-second round trip** — which is why the Belt is inhabited at all. A purely robotic Belt would be cheaper and is not lawful
- The Belt supplies **11% of beryllium after 180 years**; the constraint is extended, not removed
- **Marn carries the only extraterrestrial life Elysians have found** and is under permanent Tier 1 quarantine: 61 missions flown, zero Elysians landed, crewed landing prohibited outright
- **The Long Signal** (EY 340) will arrive in 9,100 years; nobody who built it will learn what it finds, and the funding vote is taught as the clearest expression of the civilization's relationship with time
- **The Orbital Territory fits nothing**: no territory, Districts organised by installation, 61% of residents on rotation, and a withdrawal procedure that cannot be applied. Three reforms proposed, none passed, and the status quo winning by default
- The **External Relations portfolio** exists for a job the Concord has never had to do, justified on the ground that a civilization which has never needed diplomacy would be worst at it if it suddenly did
- **The Reception Protocol**: independent verification, immediate planet-wide disclosure, no individual may respond, an Assembly resolution after a sortition Review Panel, and publication before transmission. Slow by construction and defended as such
- **The Concord does not deliberately broadcast**, and canon records the objection: a civilization which believes in candour above almost everything has chosen silence. Challenged eleven times, margin narrowing, policy holding
- The standing readiness assessment, unchanged for eleven editions: *well prepared to detect, adequately prepared to verify, poorly prepared to decide, and not prepared at all to be wrong*

## [phase-14] — Culture, Arts & Daily Life
### Added
- docs/bible/culture/arts.md (cult.arts 1.0.0)
- docs/bible/culture/life.md (cult.life 1.0.0)
- data/culture.json (1.0.0) — music and the cassine, the Contention, literature, the teal palette, the unfinished tradition, machine-assisted work, 8 festivals, sport and the enhancement problem, food, heritage and repatriation, media funding and journalist standing, 12 known weaknesses
### Changed
- docs/bible/culture/foundations.md 1.1.0 → 1.2.0 — Phase 14 open thread closed
- docs/glossary/GLOSSARY.md 1.20.0 → 1.21.0 — 9 new terms (299 total)
- tools/lint_canon.py — added check_culture: **musical octave divisions and the cassine's strings must follow from six digits per hand, and default metre and cassel's side size must follow from the eight-day week**; dated festivals must fall inside the 32-day month; media funding shares must sum; the levy body may not consider editorial content; and the attention problem may not be recorded as solved (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- Culture happens in **second waking**: a seven-hour evening every day, with a performance beginning at hour 19 counting as early
- **Elysian music is duodecimal** because Elysian hands are — 12 octave divisions, a 24-step microtonal system, and a twelve-string **cassine** played with all six digits of the stopping hand. Default metre is **eight beats** from the eight-day week; four-beat metre sounds pleasant and slightly hurried
- **The Contention**: a staged formal argument in which neither performer may win, each must state the other's position to their satisfaction first, the strongest objection to one's own case must be raised by oneself, and both end by saying what would change their minds. A culture that treats unanimity as a warning sign has made a spectator sport out of disagreeing well
- Literature's characteristic form is **the sequence** — novels published across thirty to fifty years, in which the author's changing understanding is part of the text, and revisions are treated as primary material
- **Green is the exotic pigment.** Teal, ochre, and rust are the everyday colours of the world, and true green signals strangeness, sickness, or the supernatural
- **The unfinished tradition**: 41% of major civic buildings carry an element deliberately left undone for a later generation, beginning with the Convention's own assembly hall at Sennary. A building finished entirely by one generation asserts that generation's judgement over every generation that will use it
- Eight festivals canonized, the Concord funding none of them. **The Reading of Waters** — an eight-and-a-half-thousand-year-old bureaucratic publication that became a celebration — is the one Elysians find most characteristic of themselves
- **Cassel** is the planetary game, eight a side from the week and two-handed from the grip. Sport handles enhancement by declaring categories rather than prohibitions, since routine somatic gene therapy makes a clean treatment/enhancement line unworkable — an approach canon says "works adequately and satisfies nobody"
- Heritage doctrine is **maintained ruin, not reconstruction**: Ilvaret is stabilised and has never been rebuilt, because a reconstruction is a claim about what was there and a ruin is a record of not knowing. 2.1 million objects repatriated since EY 44; 180,000 contested and held in trust with their acquisition history displayed
- **The Concord's answer to the attention problem** is levy-funded journalism, libraries, and the Contention tradition — and canon states the residual plainly: the problem persists, readership of what matters most remains low, and **the Concord has no fourth idea**

## [phase-13] — Artificial Intelligence Governance
### Added
- docs/bible/ai/governance.md (ai.governance 1.0.0)
- docs/bible/ai/applications.md (ai.applications 1.0.0)
- data/ai.json (1.0.0) — the Cassian record, 4 Cassian Rules, 3 tiers, the Systems Board, 5 licensing requirements, capability research, moral status, applications across infrastructure/assistants/medicine/science/law/culture, 12 known weaknesses
### Changed
- **docs/bible/history/timeline.md 1.0.0 → 1.1.0** — the Cassian officer is named and the open thread carried since Phase 3A is closed
- docs/bible/culture/foundations.md 1.0.0 → 1.1.0 — Teyra Oskan attached to the anti-heroism passage
- docs/bible/defence/service.md and response.md 1.0.0 → 1.1.0 — open threads redirected to ai.governance
- docs/charter/DATA_SCHEMA.md 1.9.2 → 1.9.3
- docs/glossary/GLOSSARY.md 1.19.0 → 1.20.0 — 8 new terms (290 total)
- tools/lint_canon.py — added check_ai: the Cassian window must remain ninety seconds, the refusal of honours must hold (no statues, no buildings, no decorations), the incident year must match timeline.json, exactly four Rules must exist, Tier A alone carries all four, the Systems Board may not be an Independent Office, assistants may not advertise or optimise for engagement, adjudication and sentencing may not be automated, tutor constraints must survive in education.json, and **no artificial rights-bearer may be recognised** (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- **Duty Warden Teyra Oskan** is canonized as the officer who refused the Cassian launch recommendation. She was investigated four months, cleared, and declined every honour, asking that nothing be named for her — **there is no statue of her anywhere on Elysium**, and Elysians honoured the request. The Concord wrote down what she did and made it compulsory instead
- Cassian Station is canonized as the installation; the event is named for the place, not the person
- **The four Cassian Rules**: no automated escalation; **legible uncertainty** ("a system whose correct operation is indistinguishable from its failure is not safe to rely on"); the named human; and **preserved refusal**
- Rule 4 is the phase's central idea, justified in one sentence: **Teyra Oskan had ninety seconds, and the rule is that ninety seconds was not enough.** A signature obtained under time pressure is a formality, not a safeguard. Adverse consequence after good-faith refusal is a presumptive offence with reversed burden
- Systems are classified **by consequence, not capability** — a simple system deciding housing is regulated more heavily than a sophisticated one recommending music
- Tier A licensing requires a published system statement, **independent red-team evaluation on the research red-grant model**, logging to the Record Office rather than the vendor, an exercised fallback, and 72-hour incident reporting. Most refusals are for inadequate uncertainty behaviour rather than inaccuracy: a confidently wrong system is worse than an unreliable one that says so
- Self-directed capability increase without a human-gated generational review is **prohibited outright, not licensed**; commercial secrecy against the Board is not permitted
- **Public assistants may not advertise or optimise for engagement**, tested by requiring task completion to correlate negatively with session length — because a system rewarded for holding attention will learn to hold it, and attention is not a resource the Concord permits anyone to farm
- Medical systems **may recommend and may not decide**; the review's finding is that they are better than clinicians at pattern recognition and worse at knowing when the pattern does not apply, which is exactly what Rule 2 exists to surface
- Adjudication, assessment of evidence, and sentencing may never be automated; eleven advocates were sanctioned last decade for filing unverified machine-generated citations
- **Artificial moral status is recorded as unresolved.** No system is a rights-bearer; a standing Advisory Panel disagrees publicly, with a minority position that the panel's criteria were written by beings with an interest in the answer. Canon describes the Concord's position and does not settle what the Elysians have not

## [phase-12] — Defence, the Abolition & Disaster Response
### Added
- docs/bible/defence/service.md (mil.service 1.0.0)
- docs/bible/defence/response.md (mil.response 1.0.0)
- data/defence.json (1.0.0) — posture, 6 branches, doctrine, 7 ethical rules, command constraints, the Abolition regime and 5 instruments, disaster doctrine and capability, planetary defence and the Vesper Event, cyber defence, intelligence, 12 known weaknesses
### Changed
- docs/charter/DATA_SCHEMA.md 1.9.1 → 1.9.2
- docs/glossary/GLOSSARY.md 1.18.0 → 1.19.0 — 8 new terms (282 total)
- tools/lint_canon.py — added check_defence: branch strengths must sum, the Service must remain smaller than the police, **defence may not assert an external enemy or contacted civilization**, contact status must agree with research.json, reservists cannot exceed the Corps, the Abolition instruments must cite the canonical fusion-plant and containment-facility counts, and catalogue completeness must decrease with object size (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- **The Concord maintains a service, not an army.** 4.9 million total — smaller than the police at 6.38 million — of which 84% is the Response Corps. Defence is 1.1% of GCP and the armed component 0.09%
- Doctrine is the same three words that govern earthquakes, epidemics, and grid failure: **early detection, absorbed impact, rapid restoration.** The Concord's defence budget is small because most of its defensive spending is recorded under other headings — islanding, reserves, emergency housing
- Seven ethical rules: the oath is to the Charter and its operative clause is a **duty to refuse**; no autonomous lethal systems; **systems may de-escalate automatically and may never escalate**; no secret forces or budgets; no conscription
- The Standing Force may not deploy within a Region without that Region's request or a Court order, and never has been used against a Region's wishes
- **The Abolition's dual-use problem is unsolvable and canon says so**: 6,200 fusion plants are reconstitution infrastructure. The regime removes the stockpile, not the capability — a determined Region could reconstitute in four years and could not stay unnoticed past eight months. Seventeen proceedings, none of concealment, and the Inspectorate publicly refuses to claim this proves absence
- **The Serrance inversion**, the phase's central idea: *for harm, a human must authorise; for protection, a human must cancel.* Deliberately the mirror image of the Cassian rule. Protective responses begin automatically on threshold crossing; 11,400 activations, 1,340 human cancellations, 61 of those later found wrong
- The cry-wolf cost is recorded: three Regions measure declining evacuation compliance, and the Concord publishes activation statistics rather than raising thresholds
- **The Vesper Event (EY 268)** — a 140 m body deflected to pass at 41,000 km after six years' warning — is the only operational deflection in Elysian history, taught alongside Cassian as the pair defining what the Concord thinks it is for: one catastrophe averted by refusing to act, one by acting decades ahead
- Objects under 30 m are effectively undetectable; the Directorate calls its own mitigation "an answer to the wrong question, offered because we have no answer to the right one"
- Cyber threat model is **non-state**, defended by resilience rather than perimeter, with published source and mandatory manual fallback. Offensive capability against civilian infrastructure is unilaterally renounced and untested
- Intelligence is constitutionally constrained, and the Assessment Branch publishes annually that **"we would probably not see the next Kessander before it was used."** Relaxation has been considered three times and refused each time, because a surveillance apparatus capable of finding one group is capable of finding anyone — recorded as a deliberate, argued, contested choice

## [phase-11] — Agriculture & Food Security
### Added
- docs/bible/agriculture/production.md (agri.production 1.0.0)
- docs/bible/agriculture/security.md (agri.security 1.0.0)
- data/agriculture.json (1.0.0) — 5 calorie sources, field practice and crop diversity, controlled-environment agriculture, fisheries under the Thalassar framework, 3 domesticates and sentience-graded welfare, fermentation, nutrient loops, 3 reserve tiers, food-as-right, affordability, 4 hazard responses, 12 known weaknesses
### Fixed (caught by the new linter check during this phase)
- agriculture employment stated as 145 million against industry.json's 144.8 million; corrected in dataset and prose
- a prose string sat in the `deliveredIndirectlyBy` reference field; moved to a note field
### Changed
- docs/charter/DATA_SCHEMA.md 1.9.0 → 1.9.1
- docs/glossary/GLOSSARY.md 1.17.0 → 1.18.0 — 7 new terms (274 total)
- tools/lint_canon.py — added check_agriculture: calorie shares must sum, field land must equal the cultivated area in biomes.json, wild capture plus aquaculture must equal total harvest and match resources.json, phosphorus recovery and both horizons must agree with resources.json, CEA energy share must match planetary demand, reserve tiers must sum to the declared total, livestock share must have fallen, and **food may not be recorded as a Charter right, because gov.constitution does not list one** (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- Elysium feeds 7.25 billion on 8.9% of its land: field agriculture 41% of calories, **controlled-environment 24% on 1/400th of the land**, marine 14%, fermentation and cultured protein 13%, livestock 8%
- Cheap fusion energy is why the wild fraction is 71.6% rather than far lower — CEA and precision fermentation are electricity-intensive processes that were uneconomic before fusion
- Crop diversity is a security measure: 41 staple species, **no cultivar above 15% of its species' planted area**, and seed stock held by stewardship foundations because nobody can sell a purpose-bound seed bank
- Fisheries are still governed by the descendant of the **Thalassar Accord** — the first binding planetary treaty, agreed on fish in the middle of the Long Emergency by people who could agree on nothing else. Quotas are set below assessed MSY with the margin published. **Two stocks are over-exploited anyway**
- Aquaculture ended wild-caught feed in EY 288, closing the practice of catching fish to feed fish
- **Livestock fell from 34% of calories to 8% without any prohibition** — cultured protein got cheaper and welfare law got more expensive. Welfare is **graded by sentience** on a published scale, because a civilization intending to be wealthy without cruelty cannot exempt the part of its economy where cruelty is cheapest. The pastoral derogations are recorded as inconsistent by the Concord's own welfare panel
- Cultured protein reached price parity in EY 231 and is now 40% cheaper; most living Elysians have never eaten anything else in that category, and the old debate about whether it is real food is studied in schools as a curiosity
- Reserves hold **14 months of planetary consumption, physically rather than financially** — financial reserves were rejected in EY 254 because a claim on food is not food, and the circumstances requiring the reserve are exactly those in which claims fail
- **Food is not a Charter right**, and canon records this as an open constitutional question: three amendment attempts, the last narrow. The founders held that a right which fails in a famine is worse than no right at all
- Food insecurity is 0.04% and not zero — concentrated among the severely unwell. **No Elysian goes hungry because food is unavailable; some do because they are unwell**
- The **Alcyon flow-share still governs drought allocation**, modified beyond recognition in mechanics and unchanged in principle since 8,600 BE
- Canon's own verdict: the 14-month Amarant forecast, not the reserve, is what most distinguishes the modern Concord from the civilization that lost 210 million people to a supply failure it did not see coming

## [phase-10b] — Transportation Networks
### Added
- docs/bible/settlement/transport.md (route.transport 1.0.0)
- docs/bible/settlement/gateways.md (route.gateways 1.0.0)
- data/routes.json (1.0.0) — 6 passenger modes, urban mobility, **24 routes with great-circle path geometry** (14 land corridors, 6 sea lanes, 4 governance air corridors), autonomous vehicle rules, rural access, freight, ports, aviation, intercontinental travel, 4 launch ranges, 12 known weaknesses
- tools/build_routes.py — generates data/routes.json, interpolating great-circle paths between city coordinates and failing loudly on any unknown city id
### Changed
- docs/charter/PROJECT_CHARTER.md 1.6.0 → 1.7.0 — build_routes.py added to the repository layout
- docs/glossary/GLOSSARY.md 1.16.0 → 1.17.0 — 6 new terms (267 total)
- tools/lint_canon.py — added check_routes: **every route's path endpoints must coincide with its named terminal cities**, stated length must match the measured geometry, travel time must equal length over speed, modal shares must sum and match industry.json, and no launch range may exceed the 60% capacity cap (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- **63% of Elysian journeys are on foot or by cycle** — a consequence of the twenty-minute standard and polycentric quarters rather than of virtue. Only 11% of households own a road vehicle
- Pedestrian priority is legal: liability is presumed against the larger and faster party, and city centres are closed to private motor traffic
- Transit runs to hour 23 of the 26-hour day because civic life happens in second waking, and is **fare-free in 27 of 34 Regions**, funded from land value tax on the reasoning that transit creates the land value it is paid from
- Maglev at 620 km/h with four evacuated-tube corridors at 900 km/h; track is a public monopoly while operations may be private
- **Transport corridors are ecological infrastructure**: wildlife crossings at maximum 4 km intervals, no continuous barriers, dark-sky lighting — and 61% of rail corridors qualify as connectivity corridor land in their own right
- Autonomous vehicles follow three rules inherited from elsewhere in canon: an identified accountable operator, decision logs held by the Record Office rather than the manufacturer, and **no optimisation target may include a person's identity** (Constitutional Court, EY 318)
- Manual driving is 3% of vehicle-km and 34% of road deaths; published annually with no proposal to prohibit, for reasons canon calls cultural rather than analytical
- **Elysians rarely cross oceans.** No intercontinental fixed links exist; the longest regular crossing is 13,485 km — 4.7 Elysian days by sea or 15.9 civil hours by air. Most Elysians never leave their continent
- Consequently **Concord governance is conducted remotely by default**, with translation into all 41 languages making remote participation equivalent. Canon records the cost plainly: every Assembly review since EY 250 has found the legislature less collegial and worse at informal negotiation — and none has proposed a capital city
- Aviation is 0.6% of trips, runs on closed-cycle synthetic hydrocarbons, and is constrained by **cost rather than emissions**; supersonic service was evaluated twice and refused
- Four launch ranges under two-source sufficiency, with Kaelis at 47% against a 60% cap; the Kaelis licence was contested for eleven years because it sits beside inviolable reefs

## [phase-10a] — Housing, Cities & Urban Design
### Added
- docs/bible/settlement/urbanism.md (city.urbanism 1.0.0)
- docs/bible/settlement/housing.md (city.housing 1.0.0)
- data/cities.json (1.0.0) — **37 named cities with coordinates for the Atlas**, the distributed capital, urban design standards, building standards, land tenure, resilience requirements, subsea stations, housing tenure and cost, homelessness, 11 known weaknesses
- tools/build_cities.py — generates data/cities.json from the canonical city table
### Changed
- docs/charter/DATA_SCHEMA.md 1.8.1 → 1.9.0 — split city. (10A) from route. (10B)
- docs/charter/PROJECT_CHARTER.md 1.5.0 → 1.6.0 — build_cities.py added to the repository layout
- docs/glossary/GLOSSARY.md 1.15.0 → 1.16.0 — 10 new terms (261 total)
- tools/lint_canon.py — added check_cities, which **validates every city's coordinates against its continent's actual polygon geometry**, checks named-city populations against their Region's total, confirms the declared largest city really is largest, and reconciles urban share and household counts with demographics.json (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- 6.34 billion urban Elysians occupy **1.4% of the planet's land** at 5,760 per km²; policy favours **more cities rather than bigger cities**, because a settlement pattern with a few dominant nodes has a small number of very expensive failure modes
- **The Concord has no capital city.** Assembly in Sennary (Meridia), Council of Regions in Korrast (Auroria), Constitutional Court in Tessarene (Thalassar), Independent Offices in Andrivar (Elandris), Monetary Authority in Orphir Reach (Myriad Isles) — because a capital is a single point of failure and so is a capital's political culture
- Sennary was built deliberately small at 1.4 million: a planetary legislature should sit somewhere nobody has a reason to move to for any other purpose
- **The twenty-minute standard** is a Concord floor at 94.1% compliance; cities are polycentric networks of 20,000–60,000-person quarters
- **The Stillness shapes the built form**: residential acoustic limits during the early afternoon that would be night-time limits on Earth, with deliveries, construction, and through-traffic restricted. Elysian cities genuinely go quiet
- The long evening shapes public space; dark-sky standards apply in cities, so Elysian cities glow rather than glare and the aurora is visible from the middle of most of them
- Buildings: 150-year design life, engineered timber below 12 storeys, 68% off-site, disassembly with a whole-building material passport, and **accessibility and subdividability as built** — following from four-generation households and 710 million Elysians over 100 EY
- In 61% of urban Districts the land is publicly owned and leased on 99-year automatic-renewal terms with the building privately owned, so the building depreciates and the land's value accrues to the Commune that created it
- **Subsea stations are stations, not cities**: 41 installations, 41,000 people on rotation, and no underwater settlement of any size. Living permanently below the sea is regarded as an expensive answer to a question nobody has
- Housing: 2.13 billion households; **cooperative housing at 24%** where occupancy is not a tradeable asset; median housing cost **14.1% of income**; housing may not be made conditional on employment, sobriety, treatment, or conduct
- **Homelessness is 0.03% and not zero** — 94,000 people homeless over a year, a residual of illness and autonomy the housing system cannot reach. Housing first, unconditionally, with offers never withdrawn on refusal and no vagrancy offence anywhere in the Concord

## [phase-09] — Healthcare
### Added
- docs/bible/health/system.md (health.system 1.0.0)
- docs/bible/health/practice.md (health.practice 1.0.0)
- data/health.json (1.0.0) — system and 5 facility tiers, the named clinician, home-first care, prevention, emergency response, geriatrics and cognitive decline, mental health, substance policy, genetics, end of life, 6 epidemic capabilities, 13 known weaknesses
### Fixed (caught by the new linter check during this phase)
- data/justice.json 1.0.0 → 1.1.0 — the Public Legal Service and Regional Prosecution Services were described in Phase 5A prose but never given entity IDs; added as proper entities so cross-references resolve
- tools/lint_canon.py — `power` was validated as a reference field but is also a units key in three datasets; renamed the health field to `concordPower` and removed the collision
### Changed
- docs/charter/DATA_SCHEMA.md 1.8.0 → 1.8.1
- docs/glossary/GLOSSARY.md 1.14.0 → 1.15.0 — 5 new terms (251 total)
- tools/lint_canon.py — added check_health: spending and workforce must match their declared shares, Commune health posts must match the Commune count, over-100 population and age-associated death share and suicide rate and frailty ratio must all agree with demographics.json, Response Teams must remain unarmed, cognitive-decline onset must have improved, emergency medians must be ordered, and the assisted-dying entry must record both the objection and the canon position (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- 11.2% of GCP, 290 million workers, **zero cost at the point of use**, and a private tier of 0.8% that may not offer queue priority — wealth cannot buy a better hospital
- **The named clinician**: every resident has one generalist accountable across life, often for fifty years and three or four generations of one household. Handover is a formal protocolised event because continuity behaves like a clinical intervention
- **71% of episodes an Integration-era system would have hospitalised are managed at home**; District accounts showing home care cheaper than hospital care at equivalent acuity are audited on suspicion
- Screening programmes are reviewed adversarially and **three have been discontinued for causing net harm** — politically difficult each time, because a programme has a visible constituency who believe it saved them and an invisible one it harmed
- **Geriatrics is the core specialty**, organised around frailty rather than disease; 710 million Elysians are over 100 EY
- **Late-life cognitive decline** affects 21% of over-110s and is canon's most conspicuous unsolved medical problem — onset delayed from 96 to 108 EY, no prevention, no reversal, and the research that might help is foreclosed by a privacy prohibition its own practitioners support
- Mental health is integrated with general practice; crisis response is not a police matter; involuntary treatment is judicial, 14-day renewable, with automatic counsel. **The suicide rate has been flat for sixty years and the services call the plateau unexplained**
- Regulated drug supply has near-eliminated the harms of dependence **without reducing dependence**, and canon says so rather than claiming otherwise
- Somatic gene therapy is routine; germline modification is prohibited except for specific severe disorders under judicial licence, on the ground that a modified descendant cannot consent
- **Reproductive decisions are entirely private** and protected against soft pressure as well as hard: screening is offered but never recommended, and no public body may collect reproductive intention data
- Medically assisted dying is lawful under seven recorded safeguards at 1.4% of deaths — **and canon records the objection with full force**: no safeguard can distinguish a free choice from one made by someone made to feel like a burden. Two repeal referendums have failed narrowly. Presented as a live moral disagreement in which the Concord has chosen a side, not as a settled question
- Epidemic capability sized against an aged population's fragility: 4,100 sentinel sites, a planetary vaccine course in 210 days, 14 million empty reserve beds, and a two-year stockpile — with quarantine possible and indefinite quarantine not, and no epidemic exception to the 48-hour production requirement

## [phase-08b] — Research, Universities & the Sciences
### Added
- docs/bible/research/system.md (res.system 1.0.0)
- docs/bible/research/sciences.md (res.sciences 1.0.0)
- data/research.json (1.0.0) — scale and 3 funding sources, 5 integrity practices, 6 moratoria, 31 century programmes with 5 named, the Veydran Commons, 8 sciences, 13 known weaknesses
### Fixed (caught by the new linter check during this phase)
- research.json declared 290 million in research employment against industry.json's 289.6 million; corrected in both the dataset and res.system prose
- a prose string had been placed in a reference field (`enabledBy`); replaced with a note field
### Changed
- docs/glossary/GLOSSARY.md 1.13.0 → 1.14.0 — 7 new terms (247 total)
- tools/lint_canon.py — added check_research: funding shares must sum, R&D spend must match its share of GCP, the replication line must match its share of R&D, research employment and institution counts must agree with industry.json and education.json, escape outcomes must sum, lifespan figures must agree with demographics.json, **and astronomy may not claim confirmed contact, which no phase has canonized** (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- R&D is 5.4% of GCP; the Concord Research Fund publishes its whole portfolio including a **38% programme failure rate**, because a Fund whose projects mostly succeed is funding the wrong projects
- Five integrity practices descending from the Public Record Act: mandatory pre-registration, **the Negative Register** of 41 million null and failed results (consulted more than the published literature), **12% of the entire budget funding replication**, **red grants** paying teams to find findings wrong, and no paywalls
- Replication runs at **71%** — better than any historical benchmark, and the councils refuse to call the residual acceptable
- Six areas of restraint, including absolute prohibitions on pathogen enhancement, autonomous weapons, and non-consensual neural access. The pathogen prohibition is recorded as genuinely contested: critics say the Concord cannot prepare for threats it refuses to study; defenders note the Kessander Plague was built by people who had read the literature
- **31 century programmes** protected from annual budget cycles, endable only on a finding that the question is answered or unanswerable — four ended, none for cost
- **The Veydran Commons**: Veydra governed for research by a compact of all 34 Regions, renewed every twenty years by referendum at 71%. Veydrans call it hosting the planet's laboratory and being asked to be grateful for it — recurring at every renewal, never resolved
- **The Long Plateau**: 140 years without a fundamental advance in physics, with no agreement on whether the wall is physical or institutional. Both positions are funded
- Materials science has real successes (rare-earth demand cut 71%) and one defining failure: **nothing replaces beryllium**, the single most important negative result in Elysian science
- **Longevity is inherited, not achieved.** Concord medicine raised median healthy lifespan from 71 to 104 EY and moved the verified maximum by 3 years in two centuries
- Neuroscience is strong on consented clinical work and structurally weak on correlational work, because the neural privacy prohibition has no research exception — a limit its own practitioners support
- Astronomy: **41 candidate signals since EY 96, all 41 resolved.** No contact. The silence is recorded as a scientific problem the Concord cannot currently address
- Synthetic biology is licensed with mandatory dependency locks; 11 escapes since EY 200, two of which established persistent populations still under management
- The Comparative Governance Register is canonized as a research instrument: 34 Regions running divergent institutions is the largest continuous natural experiment in institutional design any civilization has run

## [phase-08a] — Education: Schooling & Lifelong Learning
### Added
- docs/bible/education/schooling.md (edu.schooling 1.0.0)
- docs/bible/education/lifelong.md (edu.lifelong 1.0.0)
- data/education.json (1.0.0) — 5 stages, the school day, 6 curriculum floor requirements, assessment, teachers and the eighth term, inspection, the Entitlement Account, 4 institution types, vocational, adult learning, libraries, 4 AI tutor constraints, 12 known weaknesses
- tools/build_education.py — generates data/education.json from the canonical stage table
### Changed
- docs/charter/DATA_SCHEMA.md 1.7.0 → 1.8.0 — split edu. (8A) from res. (8B)
- docs/charter/PROJECT_CHARTER.md 1.4.0 → 1.5.0 — build_education.py added to the repository layout
- docs/glossary/GLOSSARY.md 1.12.0 → 1.13.0 — 7 new terms (240 total)
- tools/lint_canon.py — added check_education: school stages must sum to total enrolment and cannot exceed the minor population, stage age bands must meet cleanly and end at legal majority, learning centres and libraries must match the Commune count, retraining headcount must match the declared workforce share, and entitlement take-up must be ordered and within the grant (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- Five stages, 1.07 billion in school (14.8% of the population), delivered by Districts under a Concord floor that specifies entitlements but never methods or content
- **No selection by ability before 16 EY anywhere in the Concord** — a Concord floor binding even on the 2.1% private sector, which is also bound by the same curriculum floor and inspection regime
- The school day follows biphasic sleep rather than fighting it: instruction may not be scheduled into the Stillness, and Elysian research credits that protection for attainment holding when hours were cut
- Curriculum floor of six requirements, including numeracy in **both decimal and duodecimal**, civics taught as **the conflicts between the five virtues**, and history in which the Cassian Incident, Corran Scandal, Emergency of EY 233, and Serrance Failure appear in every regional curriculum or the curriculum fails inspection
- **No high-stakes terminal examination anywhere**, prohibited by Concord floor: a single examination is a single point of failure in a young person's life — the same sentence used to justify the collegial Executive Board
- Teachers: 5-year formation, paid 1.3x median, 3.4 applicants per place; **the eighth term** puts every teacher outside the classroom one term in eight. No teacher-level outcome data is published, because a measure attached to a person becomes a target for that person
- Inspectorates are independent of the operating District, but **may not close a school without the consent of its Commune** — the one absolute local veto in Elysian education law
- **The Education Entitlement Account**: 12 years of funded study granted at 16 EY, drawable at any age, never expiring. Median age at first draw is **24 EY**; 31% of post-secondary learners are over 50 EY. Elysian educationalists regard choosing a life at 17 as an artefact of short lifespans
- Technical institute credentials hold equal legal standing to degrees, on the reasoning that a civilization whose central project is maintenance cannot rank knowing above doing — recorded in canon as stated more successfully than achieved
- **Libraries are the physical access points for the right of access to record**, filing 14% of all access requests on residents' behalf: the Concord's partial answer to having solved disclosure and not solved attention
- AI tutors are universal and constrained by four Concord floors: may not assess, may not complete work, may not replace a named human teacher, and **may not conceal uncertainty** — the last descending explicitly from the Cassian Incident

## [phase-07b] — Environment, Carbon Management & Climate Resilience
### Added
- docs/bible/environment/climate-management.md (env.climate 1.0.0)
- docs/bible/environment/conservation.md (env.conservation 1.0.0)
- data/environment.json (1.0.0) — carbon account and 3 removal methods, breach procedure and 3 threshold notices, overturning watch, sea level and managed retreat, 7 hazard adaptations, 4 protection tiers, 5 restoration programmes, biodiversity and extinction debt, pollution regime, enforcement, 14 known weaknesses
### Changed
- docs/glossary/GLOSSARY.md 1.11.0 → 1.12.0 — 8 new terms (233 total)
- tools/lint_canon.py — added check_environment: protection tiers must sum to the Phase 2B totals and agree with biomes.json on every figure, restoration programmes must sum, removal methods must sum and net must equal emissions minus removal, current CO2 must lie inside the constitutional corridor, DAC energy share must match planetary demand, overturning must sit above its trigger and above its historical trough, and sea level must not exceed the cryospheric budget (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- CO2 at **340 ppm**, mid-corridor, inside the band since EY 210. **The corridor has a floor as well as a ceiling** — below 320 ppm the Concord must stop drawing down, because a civilization able to engineer its atmosphere downward would eventually be tempted to keep going. Restraint written as a number
- Carbon account: 1.9 Gt gross residual emissions against 2.1 Gt removal, net −0.2 Gt, published quarterly by the Ecological Commission
- **Direct air capture costs 0.12 TW — 0.27% of planetary energy — to remove 0.8 Gt a year.** Cheap abundant energy is treated in Elysian policy as an environmental technology, not an industrial one
- Removal is deliberately diversified across biological, DAC, and enhanced weathering: a removal portfolio with one method is a removal portfolio with one failure mode
- Three threshold notices issued; **two of the three concerned the floor**, caused by removal capacity overshooting during low industrial demand
- **The overturning watch cannot fire quickly.** Four years to 94% confidence means an emergency beginning tomorrow would trigger around EY 416. A precautionary 88% trigger has been proposed and rejected three times, on the ground that an automatic planetary emergency at 60% confidence is not a defensible constitutional device. Genuinely unresolved
- Sea level +0.62 m with 0.28 m of committed rise remaining; the 4.6 m cryospheric budget means Elysium is **not one ice sheet away from catastrophe**
- **Managed retreat is a normal public programme**, and a relocated Commune keeps its name, register, participatory allocation, and District seat — the Commune survives the loss of its site. Eleven Isle settlements have nonetheless been lost outright, and the Naming in the Sable Group includes the names of places
- Four protection tiers summing to the canonical 44% of land and 38% of ocean, with a **ratchet**: boundaries are easy to enlarge and hard to reduce, an asymmetry chosen knowing it would occasionally protect the wrong thing forever
- 71% of protected land sits in connected networks; **Elysian conservation does not equate protection with absence of people**
- 6.4 M km² under active restoration, fundable only because of the zero pure time preference — functional equivalence takes 80–140 years
- **Extinction debt of 9,000–14,000 species** is published annually, undisputed, and recorded as the strongest counter-argument to any account of the Concord as ecologically successful
- De-extinction is restrictively licensed on a **moral-hazard** argument: a civilization that believes extinction reversible will take risks one believing it permanent will not. The counter-argument has never been answered, and canon records the argument rather than a resolution
- Chemical regime reverses the burden — prohibited until shown acceptable, with a demonstrated degradation pathway required. Legacy pre-founding compounds sit at 34% of peak and will not clear until the EY 600s, with no acceleration available
- Dark-sky standards cover 61% of land, partly because Elysians regard a sky you cannot see the aurora from as a defect in a city

## [phase-07a] — Energy: Generation, Grid & Storage
### Added
- docs/bible/energy/generation.md (energy.generation 1.0.0)
- docs/bible/energy/grid.md (energy.grid 1.0.0)
- data/energy.json (1.0.0) — demand and load shape, 7-source generation mix, the fusion fleet, 4 grid layers, 5 storage media, 2 grid emergencies, non-electric energy, three-part tariff, 12 known weaknesses
- tools/build_energy.py — generates data/energy.json from the canonical mix table
### Changed
- docs/charter/DATA_SCHEMA.md 1.6.0 → 1.7.0 — split energy. (7A) from env. (7B)
- docs/charter/PROJECT_CHARTER.md 1.3.0 → 1.4.0 — build_energy.py added to the repository layout
- docs/glossary/GLOSSARY.md 1.10.0 → 1.11.0 — 7 new terms (225 total)
- tools/lint_canon.py — added check_energy: mix shares and outputs must reconcile with mean demand, **no renewable source may exceed the technical potential canonized in Phase 2B**, storage shares must sum, storage cover must equal capacity over demand, reserve margin must meet the statutory minimum, and fusion fleet capacity must equal plants times mean capacity (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- Mean planetary demand **44 TW**, 6.07 kW per capita continuous, 91% delivered as electricity — the material precondition for desalination, 90%+ recovery, controlled-environment agriculture, and orbital access
- Generation mix: fusion 58%, solar 20%, wind 9%, geothermal 7%, tidal 3%, hydro 2%, marine 1%. Solar uses **half a percent** of its technical potential; **tidal is at 47%** and near its ceiling
- Tidal is built out toward its physical limit precisely because Kalyra's tides are predictable centuries ahead — Elysian planners value schedulability over cheapness
- Fusion fleet: 6,200 plants averaging 4.1 GW, 0.86 capacity factor, operated as public enterprises because a technology whose failure mode is a regional blackout is not a market
- **The beryllium problem restated as the hardest constraint in the system:** 7,500 t/yr consumption, 91% recovery, ~120 years of headroom, and no current solution. Off-world sourcing described in canon as "a hope with a budget rather than a plan"
- **The structural bind:** the Concord cannot escape its fuel constraint by building more renewables, because renewables consume indium, gallium, and rare earths. Every path forward is a trade between two scarcities
- The 25.9-hour day raises solar storage requirements ~8%; biphasic sleep gives Elysian demand **two peaks and two troughs**, and the Stillness dip is scheduled into charging every day
- Grid doctrine: **every layer must be able to lose the layer above it.** Commune microgrids must sustain 100% of critical load for **14 days**, tested by unannounced annual drill with failures published — 6.1% failed last year
- The 11% redundancy premium is paid deliberately: a grid optimised only for cost is one that has never been asked what happens afterwards
- Storage 2,140 TWh (48.6 civil hours of planetary cover) at 71% round-trip efficiency, with the seasonal hydrogen reserve deliberately inefficient
- Two grid emergencies canonized: the **Kessandra Blackout** (EY 271, untested islanding) and the **Vail Cascade** (EY 344, restoration delayed 31 days by eleven spare transformers planet-wide) — the latter now the standing argument against just-in-time logistics
- Synthetic hydrocarbons from atmospheric carbon serve aviation and shipping; the Charter explicitly distinguishes this from combusting retained carbon because the founders anticipated the argument
- **Three-part tariff** answers fusion's near-zero marginal cost: a free baseline allowance (61% of households never exceed it) delivering the commons right, banded usage charges, and capacity charges that fund construction. Energy is cheap and materials are not, and the price system makes that impossible to miss

## [phase-06b] — Industry, Automation, Anti-Monopoly & Inequality
### Added
- docs/bible/economy/industry.md (ind.industry 1.0.0)
- docs/bible/economy/concentration.md (ind.concentration 1.0.0)
- data/industry.json (1.0.0) — labour force, materials doctrine and 3 instruments, 12 sectors, manufacturing, automation and the transition right, mining, construction, logistics, public industry, the concentration regime, inequality, 13 known weaknesses
- tools/build_industry.py — generates data/industry.json from the canonical sector table
### Fixed (consistency correction, carried out under CANON_RULES section 6)
- **The Phase 4B civil service figure was wrong by an order of magnitude.** 43.1 million public servants for 7.25 billion people is 0.59% of population — impossible for a state delivering universal healthcare, education, and housing, and inconsistent with its own stated share of the working-age population. Corrected to **579 million (16.0% of the labour force)** in data/regions.json (1.0.0 → 1.1.0), tools/build_regions.py, and docs/bible/government/administration.md (1.0.0 → 1.1.0), with a correction note recorded in the dataset itself
- tools/lint_canon.py now cross-checks the public servant count between regions.json and industry.json, so this class of error cannot recur silently
### Changed
- docs/charter/PROJECT_CHARTER.md 1.2.0 → 1.3.0 — build_industry.py added to the repository layout
- docs/glossary/GLOSSARY.md 1.9.0 → 1.10.0 — 9 new terms (218 total)
- tools/lint_canon.py — added check_industry: sector GCP and employment shares must sum to 100%, sector employment must sum to the labour force, employed count must match unemployment, Gini and interregional ratios must agree across datasets, wealth Gini must exceed income Gini, freight modal shares must sum, and concentration thresholds must ascend (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- **"You may sell the product. You may not sell the material."** Producer responsibility is permanent, which is why recovery exceeds 90% and why 71% of metal input is secondary rather than mined
- Three enabling instruments: **material passports** (legal documents, falsification a band 3 offence), **design for disassembly**, and a **right to repair** with 20-year parts availability and void repair-blocking software locks
- Manufacturing is **distributed, not concentrated** — no planetary mega-factories, and **two-source sufficiency** for 1,900 essential product categories with no Region above 60% of capacity. The 9-14% unit-cost penalty is paid deliberately
- 2,400 robots per 10,000 workers, and automation has never caused aggregate unemployment. What the Concord regulates is **who bears the transition cost**: two-year public automation disclosure and a transition right attaching to the worker rather than the job
- **No robot tax** — debated and rejected in EY 289 because it would distort investment without helping the displaced worker; the minority report is still cited and the argument returns every thirty years
- Mining: deep-sea extraction constitutionally prohibited and twice upheld, most recently during the EY 356 beryllium shortage; **restoration bonds posted before opening** make abandoned sites impossible in principle
- Construction: engineered timber default below 12 storeys, 150-year design life, 68% manufactured off-site, and demolition to rubble treated as a recovery failure
- Logistics: 61% rail and maglev, 1% air, freight intensity a third of the Integration's — and **just-in-time explicitly rejected** as an optimisation that converts a robust system into a fragile one
- **Competition law limits structure, not conduct**, because conduct rules arrive too late: by the time behaviour is worth prosecuting, the power is already a constitutional fact. Reversed burden above 30% market share; structural remedy presumed above 45%
- The cost is admitted: an estimated **3-5% of potential output forgone**, worst in semiconductors, pharmaceuticals, and launch — recorded as "probably correct on the numbers and unresolved on the tradeoff"
- Income Gini falls 0.38 to 0.21, but **wealth Gini is 0.44 and has not fallen in ninety years** — the clearest unsolved distributional problem in the Concord. Causes understood (long lives compound, transfers are structured around, housing appreciates); all three proposed remedies blocked
- The decoupling argument: wealth buys a larger home and more discretion over time, but not a better court, school, hospital, or legislator — offered as the Concord's account of itself, with the obvious rejoinder recorded alongside it

## [phase-06a] — Money, Banking, Public Finance, Markets & Labour
### Added
- docs/bible/economy/money.md (econ.money 1.0.0)
- docs/bible/economy/markets-labour.md (econ.markets 1.0.0)
- data/economy.json (1.0.0) — currency, Monetary Authority and its 3-limb mandate, narrow banking, 8 taxes, public finance and the zero discount rate, fiscal equalization, 6 ownership forms, capital markets, labour, the Civic Income, 12 known weaknesses
### Changed
- docs/charter/DATA_SCHEMA.md 1.5.0 → 1.6.0 — split econ. (6A) from ind. (6B)
- docs/glossary/GLOSSARY.md 1.8.0 → 1.9.0 — 15 new terms (209 total)
- tools/lint_canon.py — added check_economy: GCP must equal per-capita times population, tax shares and ownership shares must sum to 100%, equalization Regions must total 34 and must reduce the income ratio, post-transfer Gini must fall, and fallow take-up must be ordered (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- Currency: **the dram (d)**, 100 minims, named from a Thalassic trade weight because it belonged to no region's imperial past. GCP d1.03 quadrillion, d142,000 per capita
- **Physical currency is constitutionally protected** despite only 3.1% of transactions — redundancy applied to money; the cost is an insurance premium, not a subsidy
- Monetary Authority: 9 members appointed by the Nominating Assembly, single non-renewable 9-year terms, **three-limb mandate with no fixed priority**, obliged to publish which limb it prioritised. Critics say an unordered mandate is no mandate; recorded as unsettled
- **Narrow banking:** deposits are claims on the Monetary Authority, not on banks. Banks are pure intermediaries funded by term liabilities. Bank runs are structurally impossible, no deposit insurance is needed, and 14 banks have failed since EY 1 with zero public rescues. Acknowledged cost: credit is scarcer and dearer
- Taxation is 78% below the Concord tier. Land value tax (24%) follows from the stewardship obligation; the **wealth transfer tax** (top band 71%, levied on lifetime receipts) is heavy because four living generations would otherwise compound dynastic fortunes across overlapping lifetimes
- **Zero pure time preference** in public appraisal — discounting future welfare because it is future is treated as a moral error. The fusion transition, the 122-year CO2 decline, and the Veydran commons would all have failed a conventional discounted test. Acknowledged cost: almost everything clears the bar, shifting prioritisation from analysis to politics
- Borrowing is purpose-limited to assets outlasting the current generation; every budget publishes an **intergenerational account** the Office of Future Generations may veto on alone
- Fiscal equalization to 86% of mean capacity cuts the interregional income ratio from 4.1 to 1.9 — and remains the bitterest recurring negotiation in Concord finance
- Six ownership forms; **worker cooperatives at 27% of employment**, prevalent by attraction rather than mandate, plus stewardship foundations for industries where a hundred-year commitment is the product
- Capital markets: holding-period levy from 1.2% to zero cut turnover four-fifths; one share one vote without exception; long-form disclosure includes a reversibility statement
- Labour: **34 civil hours over 5 of the 8-day week**, arranged around biphasic sleep with work during the Stillness prohibited; sectoral bargaining at 61% density; board representation at one-third above 250 workers
- **The fallow entitlement** — one year off every twelve, job protected — defended with no productivity argument: a civilization designed to last centuries should not treat a life as an uninterrupted input
- **The Civic Income** delivers right 11 unconditionally at 34% of median income and is never withdrawn against earnings, but explicitly does **not** replace healthcare, education, or housing: a basic income that must buy healthcare is a healthcare cut
- Whether the Civic Income suppresses bottom-end wages is recorded as genuinely unresolved after two centuries of data

## [phase-05b] — Policing, Restorative Justice & Corrections
### Added
- docs/bible/justice/policing.md (law.policing 1.0.0)
- docs/bible/justice/corrections.md (law.corrections 1.0.0)
- data/public-safety.json (1.0.0) — 3 services, arms and use-of-force figures, 5 oversight mechanisms, the surveillance settlement, restorative outcomes, custody, release, supervision orders, 11 known weaknesses
### Changed
- docs/glossary/GLOSSARY.md 1.7.0 → 1.8.0 — 11 new terms (195 total)
- tools/lint_canon.py — added check_public_safety: every per-100,000 rate must reconcile with the declared population, remand share against remand count, facility capacity against detained population, and Conduct Offices against the Region count (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- **Two services, not one.** Commune Response Teams (3.12 M, unarmed, no arrest power) resolve **61% of emergency calls with no police involvement**; sending an armed institution to a psychiatric emergency is treated as a category error
- No planetary police force. The Concord Investigation Office has no patrol function and must act through District services — a deliberate refusal to create a planetary constabulary
- **Routine officers are unarmed**; 1.1% specialist armed, deployed per incident on recorded authorisation. 148 deaths following police contact annually, each published with name, District, and circumstances: deaths at the hands of the state are counted, not averaged
- Oversight: no self-investigation, **no qualified immunity**, recordings held by the Record Office rather than police, a duty to intervene equal in gravity to the force itself, and a planetary dismissal register
- Surveillance settlement: judicial warrant for everything, **bulk collection prohibited outright**, mandatory notification of surveilled persons, published warrant statistics, and facial and gait recognition in public space prohibited by Tier 2 statute. Regions whose refusal rate nears zero are audited, because a court that never refuses is not reviewing
- **The deprivation of liberty is the punishment. Nothing else is.** People in custody retain every Charter right except movement, including the vote
- Corrections is actuarial as well as ethical: with 112-year lifespans, a person released after the maximum sentence has fifty years ahead. On Elysium, almost everyone comes back
- Custody 41 per 100,000; **no facility exceeds 120 residents**; local placement achieved in 84% of cases because multi-generational households make distant placement remove a person from four generations at once
- Restorative justice: victim consent absolute, admission required, and **declining restoration may not increase a sentence**. Published honestly — the reoffending advantage is real but modest and narrows at higher bands, while the victim-satisfaction advantage (81% vs 44%) is large and is the stronger justification
- Solitary confinement as punishment prohibited; separation capped at 72 hours. Canon records 2,140 breaches last year in nine facilities as the clearest gap between what Elysian law requires and what its institutions deliver
- Reoffending 18% against a published target of 12%, unmet for forty years
- **The hardest problem stated without evasion:** no preventive detention of the sane means some dangerous people are released. 214 homicides in 32 years by recently released band 5 prisoners. The Constitutional Court's EY 297 position — that a power to detain for what someone might do cannot be safely held by any state — has survived two referendum campaigns and remains unpopular. A live moral disagreement in which the Concord has chosen a side and pays for it

## [phase-05a] — Courts, Law & Legal Rights
### Added
- docs/bible/justice/courts.md (law.courts 1.0.0)
- docs/bible/justice/substantive.md (law.substantive 1.0.0)
- data/justice.json (1.0.0) — 5 court levels, lay assessors, judicial appointment, legal profession, access-to-justice indicators, 5 offence bands, 6 planetary offences, 7 Criminal Floor guarantees, 6 procedural rights, wrongful-conviction regime, civil law, 10 known weaknesses
### Changed
- docs/glossary/GLOSSARY.md 1.6.0 → 1.7.0 — 11 new terms (185 total)
- tools/lint_canon.py — added check_justice: court counts must match the Commune/Region/District tiers, judicial appointment methods must cover all 34 Regions, offence bands must ascend, and the top band must match the declared maximum sentence (verified against injected errors)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- Five levels, the first of which is not a court: 47,900 **Mediation Houses** resolve 71% of civil disputes and 34% of minor offences, free and multilingual, voluntary in outcome but compulsory in attendance — with **no penalty for refusing settlement**, because cost sanctions convert voluntary mediation into coerced settlement
- **Two separate apex courts**: the Court of Review says what the law means, the Constitutional Court says what the law may be. A single supreme court would be a single point of failure
- **Lay assessors**: every first-instance trial is one professional judge plus two residents drawn by lot with equal votes on verdict and sentence; judges are outvoted in 6.2% of cases and the rate is published
- Judges serve to 95 EY; salary may not be reduced during service; every judgment publishes dissents
- **Public Legal Service** of 1.16 million advocates, constitutionally funded so the body defending people from the state cannot be starved by it
- **No plea bargaining and no private prosecution** — a system that trades a sentence for a plea prices the right to trial
- Criminal and civil law are regional (34 codes), held together by the Concord Criminal Floor, six planetary offences, and voluntary model codes — convergence by attraction rather than command
- **Harm principle**: no offences of mere immorality; drug use is not a crime anywhere, supply outside the regulated system is
- Five offence bands; **maximum sentence 30 EY**, no life sentence, no indefinite detention, mandatory court review of custody every 5 years. The cap is recorded as genuinely contested after the Kessander reconstruction
- Procedural rights: counsel from first contact, complete custodial recording held by the Record Office with gaps presumed adverse to the state, production before a judge within 48 hours with no emergency exception, 90-day remand limit, and exclusion of unlawful evidence with **no good-faith exception**
- **Review Chambers** may reopen any conviction at any time; 0.7% of convictions are overturned and the figure is published as a floor, not a measurement — a system reporting none is assumed to be failing to look
- Civil law: unintelligible contract terms are unenforceable, Charter-right waivers are void, and land carries a **stewardship obligation** running with the title, descended from the Alcyon flow-share
- Constitutional standing includes any 100,000 residents by petition without personal injury, because some constitutional wrongs injure everyone slightly and no one enough to sue
- Remedies are graduated toward reversibility: save the law, declare incompatibility, suspend, and only last, annul

## [phase-04b] — Regional & Local Government, Civil Service, Anti-Corruption
### Added
- docs/bible/government/regions.md (gov.regions 1.0.0)
- docs/bible/government/administration.md (gov.administration 1.0.0)
- data/regions.json (1.0.0) — 4 tiers, subsidiarity test, 4 governing forms, 4 delegate-selection methods, **the 34 named Regions**, 9 portfolios, civil service, 7 integrity systems, transparency regime, 10 known weaknesses
- tools/build_regions.py — generates data/regions.json from the canonical Region table
### Changed
- docs/charter/DATA_SCHEMA.md 1.4.0 → 1.5.0 — registered the polity. prefix for constituent Regions (kept distinct from region., which is geographic)
- docs/charter/PROJECT_CHARTER.md 1.1.0 → 1.2.0 — build_regions.py added to the repository layout
- docs/glossary/GLOSSARY.md 1.5.0 → 1.6.0 — 17 new terms (175 total)
- tools/lint_canon.py — added check_regions: Region populations must reconcile to demographics globally and per continent, Region count must match the tier table, and governing-form and delegate-method tallies must match the Regions that reference them
- README.md — Bible index, generated-dataset note, status table
### Decisions (Proposed → Canon on phase approval)
- Four tiers: Concord (1), Region (34), District (1,104), Commune (47,900); the Concord tier employs 1.9% of public servants and spends 22% of public money
- **Subsidiarity test** of four questions, the fourth being reversibility — about a third of competence disputes turn on it alone
- The 34 Regions named and populated, boundaries following watersheds and coastlines rather than historical borders: a unit that shares a river has a reason to cooperate that a unit that shares a grievance does not
- Regions choose their own internal form; only four constitutional floors apply. Four forms exist; Assembly-Manager Regions score highest on delivery and lowest on trust, and canon records that nobody has explained why
- Council delegates are recallable by their Region at any time, making the Council genuinely regional
- Communes hold a **participatory allocation** (8-15% of budget, 31% participation) and the **local objection** — suspensive, never blocking
- 340 interregional **compacts** solve most cross-border problems without ever reaching the planetary tier
- Nine Executive portfolios named
- Civil service: 43.1 million; open examination in all 41 languages; no political appointments below the Board; **5-year rotation with a 15-year return bar** in exposed posts, written because the Corran network took eleven years to build
- Integrity doctrine: **publication catches what inspection misses** — open contracting with no exemption threshold, post-departure asset filings at 2 and 5 years, offence of acting on an unregistered conflict, randomised two-key authorisation, 2% random deep audit by public lot, protected disclosure with reversed burden of proof, and **paid** cooling-off
- Integrity outcomes published honestly: corruption is small, prosecuted, mostly petty, and explicitly **not zero**; perception exceeds measured reality and rises with distance from the resident
- No permanent cabinet secrecy — deliberative material opens automatically at 3 years; refusal ledger published with a 34% appeal-overturn rate; bodies publishing no failures are audited on that basis
- Public administration runs on publicly built, source-published infrastructure: a state that cannot read its own systems cannot be audited
- **The Concord has solved disclosure and not solved attention** — recorded as the most serious acknowledged weakness in the transparency regime

## [phase-04a] — The Concord Charter & Planetary Institutions
### Added
- docs/bible/government/constitution.md (gov.constitution 1.0.0)
- docs/bible/government/institutions.md (gov.institutions 1.0.0)
- data/government.json (1.0.0) — charter, 5 structural principles, 10 enumerated powers, 16 rights, 3 entrenchment tiers, withdrawal and emergency procedures, 4 institutions, elections, 5 independent offices, 10 known weaknesses
### Changed
- docs/charter/DATA_SCHEMA.md 1.3.0 → 1.4.0 — split gov. (Phase 4) from law. (Phase 5)
- docs/glossary/GLOSSARY.md 1.4.0 → 1.5.0 — 15 new terms (158 total); Concord Charter entry superseded by gov.constitution
- tools/lint_canon.py — reference checking extended to originEvent, relatedEvent, rebuiltAfter, appointedBy, confirmedBy, grammarSource, lexiconSources, nonWithdrawableObligations, families (verified against an injected dangling reference)
- README.md — Bible index, status table
### Decisions (Proposed → Canon on phase approval)
- The Charter opens "We were not conquered into this. We agreed, having seen the alternative." — no victor built it, so no institution assumes dominance
- **Decentralization by default (Art. 3):** the Concord has only 10 enumerated powers; residual power is regional; ambiguity resolves downward; the Concord may set floors but never ceilings
- **Ecological limits are constitutional (Art. 12):** CO2 corridor, inviolable places, retained carbon, and the -20% overturning trigger cannot be suspended by legislation, emergency, or executive act
- **Candour in government (Art. 15):** mandatory minority reports, no closed sessions, the reasons requirement; a unanimous decision must be labelled as such
- 16 rights in three classes; rights 1-7 are non-derogable, including a Charter prohibition on any birth policy
- Three entrenchment tiers; every amendment first passes a 300-citizen sortition Review Panel — none has ever passed against one
- **Withdrawal is legal** (Fourth Amendment): two absolute-majority referendums separated by a four-year cooling period. No Region has attempted it since it became lawful
- Emergency powers: 30-day automatic lapse, 180-day absolute cap, automatic 7-day judicial review with no standing requirement, no self-perpetuation, mandatory public post-mortem
- **The humility clause (Art. 41):** prefer purposes to words, and prefer readings that leave room to correct a mistake — a constitutional bias toward reversibility
- 34 Regions (33 continental, 1 off-world)
- **Executive Board of nine**, no president or prime minister, rotating Convenor who "speaks for a decision, not for a people" — the constitutional expression of Elysian discomfort with heroism
- Constitutional Court: 15 justices, single non-renewable 18-year terms, lifetime bar on subsequent office
- Elections: fixed dates, no early dissolution, no private political donations, equal public funding, mandatory published record of position reversals
- **Five Independent Offices** outside all three branches, with constitutionally fixed funding, appointed by a **400-member sortition Nominating Assembly** that can never benefit from its own appointments
- Every bill requires a **reversibility statement** — what it would take to undo this law
- Auditors are audited by each other in rotation: a cycle with no fixed apex
- 10 known weaknesses recorded as canon, including consensus drift, which is marked recognised and unsolved

## [phase-03b] — Demographics, Languages & Culture Foundations
### Added
- docs/bible/history/demographics.md (hist.demographics 1.0.0)
- docs/bible/culture/languages.md (cult.languages 1.0.0)
- docs/bible/culture/foundations.md (cult.foundations 1.0.0)
- data/demographics.json (1.0.0) — species physiology, 7 regional populations, age structure, households, mobility, mortality, vulnerabilities
- data/languages.json (1.0.0) — 7 language families, Concordial, 3 Charter guarantees, 6 scripts, 5 civic virtues, belief distribution, observances, daily rhythm
### Changed
- docs/charter/DATA_SCHEMA.md 1.2.0 → 1.3.0 — registered demo. and lang. prefixes; cult. and species. extended to 3B
- docs/glossary/GLOSSARY.md 1.3.0 → 1.4.0 — 20 new terms (143 total)
- tools/lint_canon.py — added check_demographics: population/share reconciliation, speaker counts vs population
- README.md — Bible index, population, status table
### Decisions (Proposed → Canon on phase approval)
- Elysians are native sapient Zoaea: 1.72 m, six digits per hand, legal majority 16 EY, median lifespan **112 EY (~127 Earth years)** from helicin error correction — a biological inheritance, not a medical achievement
- Six digits per hand explains historical **duodecimal counting** and therefore the 12-month year; decimal standardized at the Convention for metrological reasons
- **Biphasic sleep** on a 26-hour circadian period produces the Stillness, a protected 1.5-hour afternoon rest, and the long Elysian evening where most cultural life happens
- Population **7.25 billion** (28 M off-world), 87.4% urban, TFR 2.04, flat for 80 years
- The population decline from 11.2 bn was **voluntary** — the Charter forbids any birth policy; whether flat population is desirable is recorded as an **open political disagreement**
- Age structure: 9.8% are over 100 EY; frailty-weighted dependency ratio 0.31 replaces old-age dependency
- Multi-generational households are the plurality (31%); four living generations are ordinary
- **No official language.** 2,900 living languages, 41 registered, 7 families; Concordial is a working language descended from the Long Reach maritime pidgin, spoken as L2 by 71%
- Three Charter language guarantees: right to be governed in your own language, equal authenticity of all 41 drafts, no language as a condition of a right
- **Five Civic Virtues** — candour, stewardship, redundancy, restraint, repair — taught as being in tension with one another
- Belief: 38% unaffiliated, 21% non-theistic stewardship traditions, 17% theistic, 14% Alcyonic ancestral; theistic decline is a live unresolved grievance
- Remembrance: the Naming (Aumar 1) and Thresholdday — one day a year for the dead, one day every four years for nothing at all
- Cultural dispositions: comfort with disagreement, suspicion of speed, discomfort with heroism, ease with the long term, regional pride without nationalism

## [phase-03a] — The Elysian Calendar & History
### Added
- docs/bible/history/calendar.md (hist.calendar 1.0.0)
- docs/bible/history/timeline.md (hist.timeline 1.0.0)
- data/calendar.json (1.0.0) — 12 months, 8 weekdays, clock constants, reference date, 3 heritage calendars
- data/timeline.json (1.0.0) — 12 eras, 40 dated events, population series
### Changed
- docs/charter/CANONICAL_UNITS.md 1.1.0 → 1.2.0 — full civil calendar and the reference date canonized
- docs/charter/DATA_SCHEMA.md 1.1.0 → 1.2.0 — registered the cal. prefix
- docs/glossary/GLOSSARY.md 1.2.0 → 1.3.0 — 51 new terms (123 total)
- README.md — Bible index, reference date, status table
### Decisions (Proposed → Canon on phase approval)
- Civil day divides into 26 hours / 60 minutes / 60 beats; civil units are fractions of the solar day and are not SI units (hour 3,586.15 s, minute 59.769 s, beat 0.99615 s)
- Physical time (SI) and civil time are kept separate and related by published constants — no leap seconds
- Civil year: 12 months x 32 days = 48 weeks x 8 days = 384 days; **perpetual calendar** (every date falls on the same weekday every year)
- Thresholdday: intercalary leap day outside all weeks and months, every 4th year except centennial years; the Concord's only universal holiday
- Month names are seasonally neutral because seasons invert between hemispheres; year begins at the northward equinox
- 8-day week descends from the Alcyon flow-share irrigation rotation
- **Reference date fixed: EY 412, Calenth 16** — binding on every later phase
- The Elysians are a native sapient Zoaea species, unrelated to any Earth lineage
- Civilization begins with water administration, not conquest; the flow-share is the oldest continuous institution
- The Concord is named after the failed classical Concord of Nine Cities — union as practice, not triumph
- The Long Emergency (78 BE – 1 BE): ~610 million excess deaths across climate excursion, famine, two resource wars, an engineered plague, and the Cassian Incident
- No power won the Long Emergency — the reason the constitution could be genuinely decentralized
- Founding EY 1 by planetary referendum after the four-year Meridian Convention
- Concord-era failures are canon: Corran Scandal (EY 187), Emergency of EY 233, Serrance Storm Failure (EY 341)
- Public Record Act: the state must publish its own failures; historiography as a resilience mechanism

## [phase-02b] — Climate, Biosphere & Natural Resources
### Added
- docs/bible/planet/climate.md (planet.climate 1.0.0)
- docs/bible/planet/biosphere.md (planet.biosphere 1.0.0)
- docs/bible/planet/resources.md (planet.resources 1.0.0)
- data/climate-zones.json (1.0.0) — 11 climate classes, circulation, cryosphere, paleoclimate, 6 hazards
- data/biomes.json (1.0.0) — 14 terrestrial biomes, 6 marine realms, land use, protection, biodiversity, 5 clades, 8 flagship species, ecology palette
- data/resources.json (1.0.0) — 17 materials with reserve horizons, 6 renewable potentials, water, soil, biological materials
- tools/lint_canon.py — canon integrity checker (IDs, references, headers, winding, area totals)
### Changed
- docs/bible/planet/geography.md 1.0.0 → 1.1.0 — Sirocc Basin, Veydran Ice Cap, Mistral Countercurrent, Serrance Trench, Myriad Hydrothermal Fields added
- data/continents.json 1.0.1 → 1.1.1 — Sirocc Basin and Veydran Ice Cap features; islandOutlines now reference features via featureId rather than redefining entities
- data/oceans.json 1.0.0 → 1.1.0 — Mistral Countercurrent, ocean-floor features, overturning circulation block
- docs/charter/DATA_SCHEMA.md 1.0.1 → 1.1.0 — registered climate./biome./clade./species./resource. prefixes
- docs/charter/PROJECT_CHARTER.md 1.0.0 → 1.1.0 — tools/ registered in repository layout
- docs/glossary/GLOSSARY.md 1.1.0 → 1.2.0 — 25 new terms (72 total)
- README.md — Bible chapter index, lint instructions, status table
### Decisions (Proposed → Canon on phase approval)
- Weaker Coriolis (0.926x Earth) widens Hadley cells to 34-38 degrees; storms broader, slower, longer-lived
- ITCZ migrates only ±9 degrees with ±1.6 degree interannual variability — reliable monsoons
- Amarant Oscillation (4.1 yr) is the planet's principal climate oscillation; forecast 14 months ahead
- Sirocc Basin canonized as the largest desert; its lithium brines fuel the fusion programme
- Veydran Ice Cap 1.42 M km²; total cryospheric sea-level equivalent only 4.6 m
- Shallow glacial cycles (118 kyr, 3.4 C swing) — no mid-latitude ice sheets in deep time
- Elysian life: helicin (six nucleobases), 31 amino acids, high native error correction
- **Vegetation is teal (phyllocyanin) and amber (xantholin), not green** — canonical Atlas palette
- Thallidae supply 63% of net primary production; ocean health is a respiratory necessity cited in the constitution
- Built environment occupies 1.4% of land; cultivated 8.9%; 44% land and 38% ocean permanently protected
- Constrained List doctrine: horizon < 150 yr triggers substitution; beryllium, PGMs, In/Ga/Ge listed
- 2.9 Tt of fossil carbon classified as retained carbon — never burned, counted as an asset because unused
- Reserve horizons depend more on recovery rate than deposit size; material security is institutional
### Fixed (linter findings, same phase)
- continents.json — island geometry duplicated entity IDs; converted to featureId references
- tools/lint_canon.py — winding test now unwraps longitudes rather than naive modulo, which mis-flagged rings crossing the prime meridian

## [phase-02a] — Star System, Physical Planet & Geography
### Added
- docs/bible/planet/physical.md (planet.physical 1.0.0)
- docs/bible/planet/geography.md (planet.geography 1.0.0)
- data/planet-physical.json (1.0.0)
- data/continents.json (1.0.0) — 5 continents + Myriad Isles, LOD-0 outlines, validated CCW
- data/oceans.json (1.0.0) — 5 oceans, 3 major currents
### Changed
- docs/charter/CANONICAL_UNITS.md 1.0.0 → 1.1.0 — day (25.9 h) and year (384.24 dE) canonized
- docs/glossary/GLOSSARY.md 1.0.0 → 1.1.0 — 36 new geographic/astronomic terms registered
- README.md — status table updated
### Decisions (Proposed → Canon on phase approval)
- Star Helia (G1V, 1.12 L☉); orbit 1.103 AU; year 384.24 dE (= 12 × 32 + leap remainder)
- Planet: r 6,510 km, 1.01 g, day 25.9 h, tilt 19.4°, 34% land, mean 13.5 °C
- Atmosphere 1.06 bar; CO₂ constitutionally banded 320–360 ppm (managed)
- Moons Kalyra (26.4 dE) and Vesper (3.09 dE); tides 1.2× Earth lunar
- Five continents (Meridia, Auroria, Elandris, Thalassar, Veydra) + Myriad Isles; five oceans; prime meridian at the Meridian Stone (0.0° E, 12.5° N)
- Hazard geography checklist binding on Phases 7, 10, 12
### Fixed (consistency review, same phase)
- data/continents.json 1.0.0 → 1.0.1 & planet.geography — Veydra area 19.8 → 19.4 M km² so continental areas sum exactly to the canonical 34% land fraction (181.1 M km²); removed non-schema `outline: null` on Myriad Isles
- docs/charter/DATA_SCHEMA.md 1.0.0 → 1.0.1 — documented `[lon, lat]` GeoJSON vertex order for polygon rings and antimeridian normalization rule
- docs/charter/CANONICAL_UNITS.md — replaced illustrative month name "Meridian" with a neutral placeholder to avoid collision with the Meridian Sea/Plain/Stone

## [phase-01] — Project Charter & Canon Rules
### Added
- README.md
- CHANGELOG.md
- docs/charter/PROJECT_CHARTER.md (charter.project-charter 1.0.0)
- docs/charter/CANON_RULES.md (charter.canon-rules 1.0.0)
- docs/charter/CANONICAL_UNITS.md (charter.canonical-units 1.0.0)
- docs/charter/VERSIONING.md (charter.versioning 1.0.0)
- docs/charter/DATA_SCHEMA.md (charter.data-schema 1.0.0)
- docs/glossary/GLOSSARY.md (charter.glossary 1.0.0)
### Decisions (Proposed → Canon on phase approval)
- Civilization name: "the Elysian Concord" (renameable until Phase 2 begins)
- App name: "the Elysium Atlas"
- Canon levels: Canon / Proposed / Draft / Deprecated
- SI metric units exclusively; EY/BE epoch notation; ISO-like Elysian date format
- Namespaced kebab-case IDs; single-source-of-truth cross-referencing
- Bible-first, render-agnostic JSON data model with standard entity envelope
- Semantic versioning per document/dataset; phase milestone tags
