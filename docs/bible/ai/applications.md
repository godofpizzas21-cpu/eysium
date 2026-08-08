# Artificial Systems in Practice

**Document ID:** `ai.applications`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/ai.json`
**Inherits:** `ai.governance` (the Cassian Rules, tiers), `energy.grid`
(islanding, manual fallback), `edu.lifelong` (AI tutor constraints),
`health.practice` (the named clinician), `res.system` (research integrity),
`cult.languages` (equal authenticity of 41 texts), `law.courts`

All figures as of **EY 412, Calenth 16**.

---

## 1. Infrastructure

Artificial systems run the Elysian grid, water networks, transit, and freight
scheduling. All are Tier A, all carry the four Cassian Rules, and all carry two
additional constraints that follow from Phase 7A and Phase 12.

**Manual fallback is exercised, not documented.** Every grid District must be
operable by hand, and the capability is tested in the annual islanding drill
(`energy.grid` §1). A control system whose fallback exists only on paper fails
its licence.

**The protective asymmetry applies.** Grid systems may shed non-critical load,
open refuges, and dispatch reserves automatically — that is protection, and the
Serrance inversion requires it to be automatic (`mil.response` §1). They may
never automatically disconnect a hospital, a water plant, or a Commune's critical
circuit; that is harm, and it needs a named human.

Grid automation has been the proximate factor in one significant failure: the
**Kessandra Blackout** of EY 271, where a protection-relay misconfiguration
propagated faster than any operator could intervene (`energy.grid` §4). The
current minimum decision windows under Rule 4 date directly from that inquiry.

## 2. Public Assistants

Every resident of the Concord has access to a **public assistant**: a Tier B
system, free, publicly built and operated, with published source
(`gov.administration` §6).

| Property | Value |
|---|---|
| Users | 6.1 billion |
| Cost | Free |
| Source | Published |
| Logs | Owned by the user, held by the Record Office |
| Advertising | Prohibited |
| Engagement optimisation | **Prohibited** |

The engagement prohibition is the distinctive rule. A public assistant may not be
optimised for time spent, return frequency, or any proxy for attention. It is
required to be *useful and then finished*, and the Systems Board tests for this
by measuring whether task completion correlates negatively with session length —
if it does not, the system fails.

The reasoning is stated in the founding statute and is characteristically
Elysian: a system rewarded for holding attention will eventually learn to hold
it, and attention is not a resource the Concord permits anyone to farm.

Two further constraints:

- **Assistants must be able to say "ask a person."** A public assistant that
  cannot route a user to a human clinician, advocate, librarian, or official on
  request fails its registration.
- **Commercial assistants may not act on public records on a person's behalf**
  without that person's specific instruction and, for anything touching a Charter
  right, without a warrant. Private assistants exist, are lawful, and are barred
  from the public record layer.

## 3. Medicine

Artificial systems in Elysian medicine are pervasive and constrained by one
sentence: **they may recommend and may not decide.**

The named clinician (`health.system` §2) remains accountable for every decision,
signs every consequential output, and must be given the system's reasoning rather
than its conclusion. Three specific rules:

- **No treatment may be refused on the recommendation of a system.** A refusal
  requires a clinician's independent judgement, recorded.
- **Diagnostic systems must present differentials, not answers**, with
  calibrated uncertainty — Rule 2 applied clinically.
- **A patient may require that a system not be used** in their care, without
  giving reasons and without prejudice to their treatment.

Measured effect is substantial and honest: diagnostic concordance improved 14
percentage points in the two decades after clinical deployment, and the
improvement plateaued. The Concord's medical AI review notes that the systems are
now better than clinicians at pattern recognition and worse at knowing when the
pattern does not apply, which is precisely the failure Rule 2 exists to surface.

## 4. Science

Artificial systems are used freely in research — hypothesis generation, protein
and materials search, simulation, and literature synthesis — under the integrity
regime of `res.system` §2 rather than under a separate AI regime.

Three rules connect them:

- **AI-generated findings attract red grants like any other.** A team is funded
  to find them wrong.
- **The Negative Register applies.** Failed AI-directed searches deposit like
  any other null result, and roughly 31% of Register entries are now
  AI-generated.
- **Provenance must be declared.** A publication states which findings were
  machine-generated and which were machine-verified; the two are recorded
  separately because they fail differently.

Materials substitution — the Concord's most important unmet objective
(`res.sciences` §3) — has been the largest single application, and canon records
the outcome plainly: **two centuries of machine-assisted search have not produced
a beryllium replacement.** Elysian scientists cite this regularly when discussing
what these systems are and are not.

## 5. Translation and Law

Translation is the load-bearing application. **Equal authenticity of legislation
in all 41 registered languages** (`cult.languages` §4) is affordable only because
machine translation makes simultaneous drafting practical, and canon has recorded
since Phase 3B that this makes the constitution structurally dependent on a
technology.

The safeguards:

- **Legally operative translation is reviewable by a human translator on
  request**, and the request may be made by any party at any stage.
- **Divergence between language texts is resolved by the Constitutional Court**
  (`gov.institutions` §4), never by a system, and never by treating one text as
  the original.
- **Court proceedings may not be automated at any point.** Adjudication,
  assessment of evidence, and sentencing are human acts. This mirrors the
  educational rule that assessment is human (`edu.lifelong` §5).

Legal research and case retrieval systems are widely used and Tier A licensed.
An advocate remains accountable for what they file, and the Court of Review
sanctioned eleven advocates in the last decade for filing machine-generated
citations they had not verified.

## 6. Culture and Creation

The Concord regulates artificial systems in creative work lightly and labels
them heavily.

- **Disclosure of provenance is required** for published creative work — not to
  restrict it, but because Elysians consider misattributed authorship a form of
  the vice of *presentation* (`cult.foundations` §1).
- **No system may be represented as a person.** A system in conversation with a
  member of the public must be identifiable as a system on request, without
  evasion.
- **Likeness and voice of a real person** may not be synthesised without that
  person's consent, and the prohibition survives death by 50 Elysian years.

Beyond that, machine-assisted art is ordinary, unremarkable, and argued about in
exactly the terms Elysians argue about everything else. Phase 14 takes up how it
sits within Elysian cultural life.

## 7. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Constitutional dependence on translation** | Equal authenticity rests on a technology; the human-review safeguard is requested in only 4% of eligible proceedings, so the dependency is real and the check is mostly theoretical |
| **Clinical over-reliance** | Concordance improvement plateaued, and the review finds clinicians increasingly reluctant to override a system even where Rule 2 flags uncertainty |
| **Engagement rules are hard to test** | The negative-correlation test is a proxy, is gameable, and the Systems Board says so in its own reports |
| **Private assistants are a growing gap** | Barred from the public record layer and otherwise lightly regulated, and their share of use has risen for forty years |
| **Provenance declarations decay** | Machine-generated and machine-verified are recorded separately in principle and conflated in practice by roughly a fifth of publications |
| **Substitution has not worked** | The largest scientific application of these systems has failed at its principal target for two hundred years |

## 8. Open Threads

- Machine-assisted art within Elysian cultural life → Phase 14
- Off-world autonomous operations and the light-lag rule → `space.infrastructure`
- Capability research and thresholds → `ai.governance`, `res.system`
- AI in public administration → `gov.administration`
- Governance, trust, and knowledge indicators → Phase 16
