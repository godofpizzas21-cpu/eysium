# Canon Rules

**Document ID:** `charter.canon-rules`
**Status:** Canon
**Version:** 1.0.0

These rules govern how facts about Elysium are created, named, referenced, and
changed. They exist to keep a multi-year project internally consistent.

---

## 1. Levels of Canon

Every statement in the project has exactly one of these statuses:

| Status | Meaning | Who can change it |
|---|---|---|
| **Canon** | Approved fact. Binding on all future work. | Founder only, via change control. |
| **Proposed** | Written by the assistant, awaiting founder approval at phase completion. | Becomes Canon when the founder approves the phase. |
| **Draft** | Work-in-progress inside an active phase. | Freely editable within the phase. |
| **Deprecated** | Former canon superseded by a change request. Kept for history, never referenced by new work. | — |

Approving a phase ("continue", "proceed", etc.) promotes all Proposed content in
that phase to Canon unless the founder states otherwise.

## 2. Single Source of Truth

- Every canonical fact is defined in **exactly one** authoritative document,
  identified by a **document ID** (see §4).
- All other documents, data files, and code **reference** the fact; they never
  restate numbers that could drift. If restating is unavoidable for readability,
  the restatement must cite the source ID, e.g. *(source: `planet.physical`)*.
- Structured values (populations, distances, dates, coordinates) that the Atlas
  will consume live in `data/` as JSON. The Bible prose cites the dataset; the
  dataset is authoritative for the number.

## 3. Naming Conventions

### 3.1 In-world names
- **Language of record:** English. In-world proper nouns are invented words that
  must be pronounceable in English and unique within the project.
- Proper nouns are registered in the Master Glossary before first use in canon.
- No Earth place-names, brand names, or names of real people.
- Naming aesthetic: clear, dignified, slightly classical; avoid apostrophes,
  gratuitous diacritics, and "randomly generated" letter salads.

### 3.2 Identifiers (machine-readable)
- **Slugs:** lowercase kebab-case: `solward-current`, `high-meridian`.
- **Namespaced IDs:** `<domain>.<slug>`, e.g. `city.aurelia`, `region.thalassar`,
  `route.maglev-aurelia-kessandra`, `metric.biodiversity-index`.
- Domain prefixes are registered in `DATA_SCHEMA.md` §3. An ID, once canon,
  is **immutable** — display names may change; IDs may not.

### 3.3 Files
- Documents: `SCREAMING_SNAKE.md` for charter/engineering docs,
  `kebab-case.md` for Bible chapters (e.g. `docs/bible/planet/geography.md`).
- Data: `kebab-case.json` in `data/`, one dataset per file.
- Code (from Phase 19): follows the conventions in the Phase 17 software spec.

## 4. Document IDs and Cross-References

- Every Markdown document carries a header block with `Document ID`, `Status`,
  and `Version`.
- Document IDs use the same namespaced form as data IDs: `charter.canon-rules`,
  `planet.geography`, `gov.constitution`.
- Cross-references in prose use the ID in backticks. Broken references are
  treated as build errors from Phase 18 onward (the data pipeline will lint them).

## 5. Quantification Rules

- Prefer numbers to adjectives. "Large city" is Draft-quality; "population
  2.4 million (`data/cities.json`)" is Canon-quality.
- All units follow `CANONICAL_UNITS.md`. Mixed or ambiguous units are not
  permitted in canon documents.
- Every quantified system should state at least one **tolerance or failure
  threshold** (e.g. grid reserve margin, food reserve duration), because the
  founding philosophy demands resilience, and resilience is measurable.

## 6. Consistency Obligations

When any phase introduces content that touches an existing canon system:

1. The authoritative document of the affected system is updated **in the same
   phase**, with a version bump per `VERSIONING.md`.
2. The change is recorded in `CHANGELOG.md`.
3. Affected data files and glossary entries are updated in the same phase.

No phase may end with known inconsistencies. If a conflict with canon is
discovered mid-phase, work stops and the conflict is presented to the founder
as a decision, with options.

## 7. The Assistant's Constraints

- Never silently retcon. Every change to canon is explicit and logged.
- Never invent canon in code or data that does not exist in the Bible.
- When ambiguity requires a decision the founder has not made, either
  (a) present it as a Proposed decision clearly flagged in the phase summary, or
  (b) if it is structurally important, stop and ask before proceeding.
