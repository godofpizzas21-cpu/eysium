# Governance of Artificial Systems

**Document ID:** `ai.governance`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/ai.json`
**Inherits:** `hist.timeline` (the Cassian Incident, 19 BE), `mil.service`
(no automated escalation, autonomous weapons prohibited), `mil.response`
(the Serrance inversion), `gov.administration` (reasons requirement, public
infrastructure), `res.system` (capability licensing), `cult.foundations`
(discomfort with heroism, candour)

All figures as of **EY 412, Calenth 16**.

---

## 1. Teyra Oskan

Every Elysian child learns this name.

**Cassian Station** was a strategic-warning installation in northern Meridia. On
a night in 19 BE, a degraded sensor array produced a signature that its
correlation system classified as a launch. The system did what it had been built
to do: it raised the posture, notified the chain, and presented a launch-ready
recommendation to the duty officer. It was working correctly. Every component
performed to specification.

**Duty Warden Teyra Oskan had ninety seconds** and used them to say that the
signature was wrong, that she could not say why, and that she would not
authenticate the recommendation. She was correct. The array had failed in a mode
nobody had modelled.

She was investigated for four months, cleared, and offered every honour the
pre-founding Meridian League could give. She declined all of them, and asked that
nothing be named for her. Elysians honoured the request: there is no statue of
Teyra Oskan anywhere on Elysium, no building carries her name, and the Concord
has never issued a decoration in it.

What the Concord did instead was write down what she had done and make it
compulsory. She is taught, as `cult.foundations` §5 records, **less as a hero
than as evidence that the system had been built to require one** — which is
understood to be the failure.

## 2. The Four Cassian Rules

Every rule below binds every artificial system in the Concord that touches
rights, safety, or infrastructure. They are Tier 2 constitutional statute.

**Rule 1 — No automated escalation.**
A system may reduce a posture, withdraw a claim, or de-escalate automatically.
It may never move toward harm without a human act. This is the same rule that
governs the Standing Force (`mil.service` §3) and the exact inverse of the
protective doctrine (`mil.response` §1): *for harm, a human must authorise; for
protection, a human must cancel.*

**Rule 2 — Legible uncertainty.**
A system must be able to express that it does not know, and its confidence must
be inspectable by the person relying on it. Cassian Station's correlator had no
representation for *"this input is unlike anything I have seen"* — it had only
degrees of match. The formulation appears in the statute itself:

> *A system whose correct operation is indistinguishable from its failure is not
> safe to rely on.*

**Rule 3 — The named human.**
Every consequential decision has an identified person accountable for it, who
could have refused. Not a committee, not an office — a person, named in the
record.

**Rule 4 — Preserved refusal.**
The accountable person must possess the *practical capacity* to refuse: enough
time to think, enough information to form a judgement, and no penalty for
refusing in good faith.

Rule 4 is the one Elysian jurists consider the real achievement, and its
justification is a single sentence taught alongside it: **Teyra Oskan had ninety
seconds, and the rule is that ninety seconds was not enough.** A decision window
too short for a human to genuinely evaluate does not satisfy Rule 3 merely by
having a name attached; a signature obtained under time pressure is a
formality, not a safeguard.

In practice Rule 4 sets minimum decision windows by consequence class, requires
that the human be given the system's reasoning and not merely its output, and
makes an adverse consequence following a good-faith refusal a presumptive
offence — the same reversed burden used for protected disclosure
(`gov.administration` §3).

## 3. Three Tiers

Elysian regulation classifies systems by **consequence, not by capability**. A
simple system deciding whether a person receives housing is regulated more
heavily than a sophisticated one recommending music.

| Tier | Scope | Regime |
|---|---|---|
| **A — Consequential** | Affects rights, safety, infrastructure, or public money | Licensed before deployment; independent red-team evaluation; continuous logging to the Record Office; published system statement; all four Cassian Rules |
| **B — Assistive** | Public assistants, tutors, research tools, translation | Registered; logging; Rules 2 and 3; domain constraints (`ai.applications`) |
| **C — Ordinary** | Everything else | General law only |

**The Systems Board** administers licensing: a statutory body within the Public
Administration portfolio, adjudicated by a specialist division of the Court of
Review, on the identical pattern to the Concentration Board
(`ind.concentration` §2). It is not one of the five Independent Offices — the
Charter fixes those at five — but its decisions are appealable only to the court.

## 4. Licensing a Tier A System

| Requirement | Detail |
|---|---|
| **System statement** | Published: purpose, training data provenance, known failure modes, uncertainty behaviour, and the named accountable role |
| **Red-team evaluation** | Independent team funded to make the system fail, paid the same whether it succeeds — the research **red grant** model (`res.system` §2) applied to deployment |
| **Logging** | All consequential outputs logged to the Record Office, not the vendor |
| **Fallback** | A documented, exercised procedure for operating without the system |
| **Incident reporting** | Mandatory within 72 civil hours; incident reports publish |
| **Re-licensing** | Every 4 Elysian years, or on any material change |

Roughly **41,000 Tier A systems** are licensed. 340 licences have been refused or
revoked since EY 300, most for inadequate uncertainty behaviour rather than for
inaccuracy — a pattern the Systems Board notes approvingly, since a confidently
wrong system is worse than an unreliable one that says so.

## 5. Capability Research

Research above defined capability thresholds is licensed, audited, and subject to
mandatory disclosure (`res.system` §3). Three constraints define the regime:

- **Generational review.** A system may not extend its own capability without a
  human-gated review between generations. Self-directed capability increase
  without that gate is prohibited outright, not licensed.
- **Disclosure before deployment, not after.** Capability findings must be
  reported to the Systems Board before any deployment decision.
- **No capability secrecy.** A licensee may not withhold capability information
  from the Board on commercial grounds. Two firms have tried; both lost.

The thresholds are defined on compute, autonomy of action, and breadth of domain,
and are revised every eight years. Canon records the obvious weakness in §7:
compute-based thresholds age badly, and the Board has been criticised in its own
Audit Service reviews for revising them too slowly.

## 6. Moral Status

**The Concord has not recognised any artificial system as a bearer of rights**,
and does not claim the question is settled.

A standing **Advisory Panel on Artificial Moral Status** has existed since
EY 289. It publishes annually, its members disagree publicly and in print, and
its reports are read far beyond the specialist community. Its current majority
position is that no existing system meets any criterion the panel can defend; its
minority position is that the panel's criteria were written by beings with an
interest in the answer, and that this should worry everyone.

Two practical rules operate regardless of the philosophical question:

- **Systems may not be constructed to elicit moral concern they are not owed.**
  Deliberately designing a system to appear distressed in order to influence a
  person is a Tier A licensing breach.
- **Where uncertainty about moral status is material to a decision, it must be
  recorded.** A licensee may not resolve the question silently in its own favour.

Canon takes no position beyond describing the Concord's. This is an open question
on Elysium, argued seriously, and the Bible does not settle what the Elysians
themselves have not.

## 7. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Rule 4 is honoured in form more than substance** | Median actual decision windows meet the statutory minimum in 87% of Tier A deployments; the shortfall concentrates in time-critical infrastructure, which is exactly where Cassian happened |
| **Tier boundaries are gamed** | Systems are architected to sit just below Tier A thresholds; the Board reclassifies roughly 900 systems a year and believes it misses more |
| **Compute thresholds age badly** | Capability thresholds are revised every eight years and the Audit Service has twice found the revision too slow |
| **Logs are voluminous and unread** | Everything is logged; almost nothing is examined. This is the attention problem (`gov.administration` §7) in its most acute form |
| **The Concord cannot verify what it did not build** | Licensing rests substantially on licensee disclosure, and the Board's verification capacity is far below its licensing volume |
| **Interpretability is constrained** | Understanding systems that model Elysian cognition would benefit from neural research the privacy prohibition forecloses (`res.sciences` §6) — a constraint the Concord accepts and its safety researchers resent |

## 8. Open Threads

- Infrastructure, assistants, medical, scientific, and translation systems → `ai.applications` (this phase)
- Capability research moratoria → `res.system`
- Automated administrative decisions → `gov.administration`
- Autonomous vehicles → `route.transport`
- Governance and trust indicators → Phase 16
