# Versioning & Change Control

**Document ID:** `charter.versioning`
**Status:** Canon
**Version:** 1.0.0

---

## 1. What Is Versioned

Three things carry versions, independently:

1. **Each document** (its `Version:` header) — semantic versioning.
2. **Each dataset** in `data/` (a `"schemaVersion"` and `"dataVersion"` field).
3. **The project as a whole** — milestone tags matching completed phases.

## 2. Semantic Versioning for Documents and Data

`MAJOR.MINOR.PATCH`

- **PATCH** — wording, typos, formatting; no change of meaning. No founder
  approval needed; still logged in `CHANGELOG.md`.
- **MINOR** — additive: new sections, new facts that contradict nothing.
  Approved implicitly by phase approval.
- **MAJOR** — changes or removes existing canon. Requires an explicit founder
  request or decision. The superseded text is preserved under a
  `## Deprecated` appendix in the same document with the date and reason.

## 3. Project Milestone Tags

When a phase is approved, the repository state is considered tagged
`phase-<n><letter?>` (e.g. `phase-03a`). The `CHANGELOG.md` entry for the tag
lists files created, files modified, and decisions promoted to Canon — mirroring
the "✅ Phase Complete" report.

## 4. Change Requests (post-approval changes)

When the founder wants to alter approved canon:

1. The assistant identifies every document, dataset, and code file the change
   touches (impact analysis) and presents it before editing.
2. On confirmation, all touched artifacts are updated in one response, versions
   bumped, changelog written. Partial application of a change is not permitted.

## 5. Changelog Format

`CHANGELOG.md` is newest-first. Entry template:

```
## [phase-04] — Government & Constitution (approved EY-date / real-date optional)
### Added
- docs/bible/government/constitution.md (gov.constitution 1.0.0)
### Changed
- docs/bible/planet/geography.md 1.0.0 → 1.1.0 — added capital region reference
### Decisions
- Bicameral planetary parliament (Proposed → Canon)
```

## 6. Synchronization Rule

A version bump anywhere triggers the `CANON_RULES.md` §6 obligations: glossary,
data, and cross-referencing documents are updated in the same response. The
project must never contain two artifacts that disagree about a canonical fact.
