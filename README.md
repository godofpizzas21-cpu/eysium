# Project Elysium

A complete fictional civilization, and a browser atlas that renders it.

- **Planet:** Elysium — reference date **EY 412, Calenth 16**
- **Civilization:** the Elysian Concord — 7.25 billion people, 412 years old
- **The Bible:** 48 chapters, roughly 86,000 words, in `docs/`
- **The data:** 29 typed datasets, 1,071 canonical entities, in `data/`
- **The Atlas:** a static React and Three.js application, in `app/`

Everything in the Atlas comes from the Bible. Nothing in the Atlas is invented
by the Atlas.

---

## Run it

```bash
cd app
npm install
npm run dev
```

Then open the URL it prints. `npm run build` produces a static site; see
`docs/engineering/DEPLOYMENT.md` for hosting on Vercel.

## Check it

```bash
python3 tools/lint_canon.py       # 25 canon integrity checks
cd app && npm run verify          # data, types, 111 smoke tests, contrast
```

The application build runs the canon linter as its first stage, so **a canon
error fails the deploy rather than shipping a broken atlas**.

---

## The Bible

| Domain | Chapters |
|---|---|
| **Charter** | Project charter, canon rules, canonical units, versioning, data schema |
| **Planet** | Physical, geography, climate, biosphere, resources |
| **History** | Calendar, timeline, demographics |
| **Culture** | Languages, foundations, arts, daily life |
| **Government** | Constitution, institutions, regions, administration |
| **Justice** | Courts, substantive law, policing, corrections |
| **Economy** | Money, markets and labour, industry, concentration |
| **Energy** | Generation, grid |
| **Environment** | Climate management, conservation |
| **Education** | Schooling, lifelong learning |
| **Research** | System, sciences |
| **Health** | System, practice |
| **Settlement** | Urbanism, housing, transport, gateways |
| **Agriculture** | Production, food security |
| **Defence** | The Concord Service, response |
| **AI** | Governance, applications |
| **Space** | Infrastructure, external relations |
| **Metrics** | The indicator system, the 48 indicators |

Start with `docs/charter/PROJECT_CHARTER.md`. Every in-world term is registered
in `docs/glossary/GLOSSARY.md` (309 entries).

## Engineering

| Document | Covers |
|---|---|
| `docs/engineering/ARCHITECTURE.md` | Stack decisions and rejected alternatives, folder structure, the two-interface requirement |
| `docs/engineering/DATA_PIPELINE.md` | How canon becomes app data, schemas, generated types |
| `docs/engineering/DESIGN_SYSTEM.md` | The palette read from canon, typography, motion, budgets |
| `docs/engineering/ACCESSIBILITY.md` | Conformance statement, verified ratios, and known gaps |
| `docs/engineering/DEPLOYMENT.md` | Hosting, changing canon, adding a layer |

---

## How this was built

Twenty-five phases, each ending in a state that could be committed as a
milestone. `CHANGELOG.md` records every decision, every correction, and every
error the checks caught.

Four principles ran through all of it.

**Single source of truth.** Every fact lives in exactly one place, referenced by
an immutable id. When the reference-field list drifted into two files, it was
merged back into one.

**Publish the failures.** The Bible records what the Concord has not solved:
wealth inequality flat for ninety years, beryllium with no substitute after two
centuries, an attention problem the Concord has no fourth idea for. The
changelog does the same for the project.

**Check what you claim.** 25 canon checks, 111 smoke tests, a contrast audit,
and payload budgets, all inside the build. They caught a beryllium horizon that
contradicted its own definition, a civil service figure wrong by an order of
magnitude, cities that would have drifted into the ocean, and a colour that
failed the project's own accessibility rule.

**Let the world shape the software.** Elysian music is duodecimal because
Elysian hands have six digits. The Atlas uses no green in its interface because
canon records green as the exotic pigment. An indicator never appears without
its counterweight, because the Concord's own statistical principle forbids
publishing one without the other.

---

## Status

All twenty-five phases are complete. The Bible is finished. The Atlas renders
twelve layers, a computed day/night terminator on a 25.9-hour day, and both
moons at true relative distance.

| Milestone | State |
|---|---|
| Phase 1 — Project Charter & Canon Rules | ✅ complete |
| Phase 2A — Star System, Physical Planet & Geography | ✅ complete |
| Phase 2B — Climate, Biomes, Ecosystems & Resources | ✅ complete |
| Phase 3A — Calendar & History | ✅ complete |
| Phase 3B — Demographics, Languages & Culture Foundations | ✅ complete |
| Phase 4A — The Concord Charter & Planetary Institutions | ✅ complete |
| Phase 4B — Regional & Local Government, Civil Service, Anti-Corruption | ✅ complete |
| Phase 5A — Courts, Law & Legal Rights | ✅ complete |
| Phase 5B — Policing, Restorative Justice & Corrections | ✅ complete |
| Phase 6A — Money, Banking, Public Finance, Markets & Labour | ✅ complete |
| Phase 6B — Industry, Automation, Anti-Monopoly & Inequality | ✅ complete |
| Phase 7A — Energy: Generation, Grid & Storage | ✅ complete |
| Phase 7B — Environment, Carbon Management & Climate Resilience | ✅ complete |
| Phase 8A — Education: Schooling & Lifelong Learning | ✅ complete |
| Phase 8B — Research, Universities & the Sciences | ✅ complete |
| Phase 9 — Healthcare | ✅ complete |
| Phase 10A — Housing, Cities & Urban Design | ✅ complete |
| Phase 10B — Transportation Networks | ✅ complete |
| Phase 11 — Agriculture & Food Security | ✅ complete |
| Phase 12 — Defence, the Abolition & Disaster Response | ✅ complete |
| Phase 13 — Artificial Intelligence Governance | ✅ complete |
| Phase 14 — Culture, Arts & Daily Life | ✅ complete |
| Phase 15 — Space Infrastructure & Diplomacy | ✅ complete |
| Phase 16 — Metrics & Indicators | ✅ complete — **the Civilization Bible is complete** |
| Phase 17 — Software Architecture & Specification | ✅ complete |
| Phase 18 — Data Layer: pipeline, schemas, generated types | ✅ complete |
| Phase 19A — Globe Core: scaffold, globe, accessible interface | ✅ complete |
| Phase 19B — Picking, fly-to camera, search | ✅ complete |
| Phase 20 — UI shell: layer switcher, legend, responsive layout | ✅ complete |
| Phase 21A — Map layers: geometry for eight layers | ✅ complete |
| Phase 21B — Layer polish: swatches, hover labels, symbology | ✅ complete |
| Phase 22 — Atmosphere: clouds, terminator, the Elysian clock | ✅ complete |
| Phase 23 — Space mode: orbits, Kalyra, Vesper, the Belt | ✅ complete |
| Phase 24 — Advanced overlays & the Record Drawer | ✅ complete |
| Phase 25 — Documentation, testing & release polish | ✅ complete |
