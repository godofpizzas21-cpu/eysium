# Project Elysium — Project Charter

**Document ID:** `charter.project-charter`
**Status:** Canon (pending founder approval)
**Version:** 1.9.0
**Applies to:** Entire project, all phases

---

## 1. Mission Statement

Project Elysium designs the most detailed, internally consistent, and technologically
advanced fictional civilization ever created, and builds a production-quality,
browser-based interactive 3D visualization of that civilization.

The project has two coupled deliverables:

1. **The Civilization Bible** — a complete, versioned reference work describing every
   major system of the civilization of Elysium.
2. **The Elysium Atlas** — a React + TypeScript + Three.js application that renders
   the planet, its infrastructure, and its data as an explorable 3D globe.

The Bible is the **single source of truth**. The Atlas visualizes it and never
invents facts of its own.

## 2. Canonical Names

| Entity | Canonical Name | Notes |
|---|---|---|
| The planet | **Elysium** | Approved by the founder. |
| The civilization | **The Elysian Concord** | Proposed in Phase 1. May be renamed by the founder before Phase 2 begins; after that it is locked canon. |
| The reference work | **The Civilization Bible** (informally "the Bible") | |
| The software application | **The Elysium Atlas** (informally "the Atlas") | |
| The project as a whole | **Project Elysium** | |

## 3. Founding Philosophy (Immutable)

Every system designed in this project must be measured against the founding
philosophy. The Elysian Concord is:

- wealthy without cruelty
- technologically advanced without instability
- powerful without aggression
- environmentally sustainable
- scientifically driven
- democratic, decentralized, and transparent
- resilient, beautiful, free, and efficient
- designed to survive for centuries

**Design axiom:** the goal is not perfection. The goal is an extremely resilient
civilization that continually improves itself. Every system must therefore include
its own failure modes, correction mechanisms, and improvement loops. A system
described without a failure mode is considered incomplete.

## 4. Scope

### In scope
- Full worldbuilding of one planet, its civilization, and its near-space infrastructure.
- Structured datasets derived from the Bible (geography, cities, routes, metrics, orbits).
- A browser application (React, TypeScript, Vite, Three.js) visualizing those datasets.
- Complete documentation: worldbuilding, engineering specs, user docs, changelogs.

### Out of scope (unless the founder expands scope later)
- Interstellar civilizations beyond what Diplomacy/First Contact (Phase 15) requires.
- Backend servers, accounts, or multiplayer features — the Atlas is a static client app.
- Non-English editions of the Bible.

## 5. Working Method

- The project advances **one phase (or sub-phase) per response**, per the approved
  26-item roadmap (Phases 1–25 plus this charter's rules).
- Every phase ends in a state that could be committed to a Git repository as a
  completed milestone.
- No phase begins without explicit founder approval.
- Approved content is never contradicted or rewritten without an explicit founder
  request. Corrections go through the change-control process in `VERSIONING.md`.

## 6. Quality Bar

All work is held to professional standards:

- **Worldbuilding:** internally consistent, quantified where possible, with causes
  and consequences — not lists of adjectives.
- **Engineering:** modular, typed, documented, performant, accessible; no placeholder
  implementations where a real one is practical.
- **Documentation:** every canonical fact lives in exactly one authoritative file;
  everything else references it by document ID.

## 7. Roles

The founder (the human) is the **product owner and final authority on canon**.
The assistant acts as Lead Systems Architect, Worldbuilding Director, Senior
Software Engineer, Principal UI/UX Designer, Technical Writer, and Project Manager.

## 8. Repository Layout (authoritative)

```
elysium/
├── README.md                  # Project overview and navigation
├── CHANGELOG.md               # Project-wide change log
├── docs/
│   ├── charter/               # This charter, canon rules, versioning, units
│   ├── bible/                 # The Civilization Bible, one folder per domain
│   ├── glossary/              # Master glossary
│   └── engineering/           # Software specs (from Phase 17)
│       ├── ARCHITECTURE.md    # Stack, folder structure, routing, the two interfaces
│       ├── DATA_PIPELINE.md   # Canon to app data, schemas, generated types
│       └── DESIGN_SYSTEM.md   # Palette from canon, type, motion, budgets, a11y
├── data/                      # Typed JSON datasets (seeded from Phase 2)
├── tools/                     # Canon integrity tooling (from Phase 2B)
│   ├── lint_canon.py          # ID, reference, header and totals checker
│   ├── build_regions.py       # Generates data/regions.json from the canonical table
│   ├── build_industry.py      # Generates data/industry.json from the canonical table
│   ├── build_energy.py        # Generates data/energy.json from the canonical mix table
│   ├── build_education.py     # Generates data/education.json from the canonical stage table
│   ├── build_cities.py        # Generates data/cities.json from the canonical city table
│   └── build_routes.py        # Generates data/routes.json with great-circle path geometry
└── app/                       # The Elysium Atlas application
    ├── tools/                 # Data pipeline, layer registry, schemas (Phase 18)
    ├── src/                   # Application source (from Phase 19)
    └── public/data/           # Build artifact — canon flows one way, gitignored
```

New folders are added only by a phase that owns them, and this section is updated
in the same phase.
