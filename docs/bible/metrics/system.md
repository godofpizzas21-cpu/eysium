# The Indicator System

**Document ID:** `metric.system`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/metrics.json`
**Inherits:** `gov.institutions` (the Ecological Commission, the Audit Service,
the Record Office), `gov.administration` (publication by default, the attention
problem), `edu.schooling` (no teacher-level outcome data), `res.system`
(the Negative Register), `cult.foundations` (candour)

All figures as of **EY 412, Calenth 16**.

---

## 1. Who Measures

No single body owns Elysian statistics, and that is deliberate.

| Producer | Domain |
|---|---|
| The **Ecological Commission** | Atmosphere, ocean, biodiversity, the carbon account |
| The **Audit Service** | Integrity, procurement, institutional performance |
| The **Record Office** | Access, transparency, archive completeness |
| Regional statistical services | Health, education, housing, employment, safety |
| The **Statistical Council** | Method, comparability, and the register of definitions |

The Statistical Council does not collect anything. It defines terms, arbitrates
comparability between Regions, and maintains the definition register — and it
cannot publish an indicator of its own. The separation exists so that the body
which decides *what counts* is not the body whose performance is being counted,
which is the audit principle (`gov.constitution` §2.2) applied to measurement.

## 2. Six Principles

**1. No composite headline index.**
The Concord refuses to produce a single number for how it is doing. A single
number invites optimisation and hides the tradeoffs that Elysian politics exists
to argue about. Proposals for a headline index have been made four times and
defeated four times, most recently in EY 371.

**2. Distributions, not central values.**
Every indicator publishes its spread. A median without a distribution is treated
as misleading rather than incomplete, and the standard published form is the
median with the 10th and 90th percentiles beside it.

**3. Paired counterweights.**
Indicators liable to gaming are published alongside an indicator that would move
the *wrong way* if the first were being gamed. Custody rate is published beside
reoffending; clearance rate beside wrongful conviction; screening coverage beside
over-diagnosis; energy reserve margin beside islanding-drill failure. The pairing
is part of the definition, and an indicator may not be published without its
counterweight.

**4. No indicator attaches to an individual.**
Generalised from the schooling rule that no teacher-level outcome data is
published (`edu.schooling` §5): a measure attached to a person becomes a target
for that person. This binds every producer and every tier.

**5. Revision transparency.**
Any restatement publishes the superseded series alongside the new one,
permanently. Elysians can see every number the Concord has ever changed its mind
about, and what it used to say.

**6. Indicators are not targets by default.**
Adopting an indicator as a target requires an Assembly resolution and carries an
automatic sunset. The Concord's own reviews cite the reoffending target — 12%,
unmet for forty years (`law.corrections` §4) — as the standing example of what a
target does to an indicator, and of why it kept the target anyway.

## 3. The Unmeasured Register

The Concord publishes a list of **things it believes matter and cannot measure**.

The Register is maintained on the same principle as the Negative Register in
science (`res.system` §2): what is not known must be visible, or it will be
mistaken for what is not there. It is short, argued over, and revised.

Current entries include: whether Elysians are lonely in ways surveys do not
reach; whether the Contention tradition improves public reasoning or only
performs it; whether restorative processes repair anything durable in the person
harmed; what the Stillness is actually for physiologically; whether the unfinished
tradition means anything to the generations that inherit it; and whether the
Concord's institutions would survive a genuine external shock, which it has not
had since the founding.

The last entry has been on the Register since EY 61 and is the one Elysian
commentators return to most often.

## 4. What the Indicators Are For

48 indicators are published across twelve domains. They are used to argue, not to
score. Canon should be exact about their limits, because the Concord is:

- They inform the **intergenerational account** attached to every budget
  (`econ.money` §5) and the Office of Future Generations' interventions.
- They drive the **Comparative Governance Register** (`gov.regions` §3), which
  tracks outcomes across the four regional governing forms and produced canon's
  most-cited unexplained finding: Assembly–Manager Regions deliver best and are
  trusted least.
- They populate the Atlas's overlay layers, each indicator carrying the dataset
  it derives from so a panel can link back to its source.

They do **not** allocate money, rank Regions officially, or trigger any automatic
consequence. Fiscal equalization runs on taxable capacity, not on outcomes
(`econ.money` §6), precisely so that measuring a Region cannot become a way of
funding or defunding it.

## 5. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Comparability across 34 Regions** | Regional services define carefully and collect differently; the Statistical Council arbitrates and the residual divergence is real |
| **Counterweights are gameable in pairs** | Pairing raises the cost of gaming without eliminating it, and the Audit Service has found two Districts optimising both halves of a pair |
| **The unmeasured stays unmeasured** | The Register makes ignorance visible and does not reduce it; four entries have been on it for over a century |
| **Survey-derived indicators are soft** | Life evaluation and financial distress rest on self-report, and their stability may reflect stable methodology as much as stable lives |
| **Refusing a headline index has a cost** | Without one, public attention has nothing simple to attach to, which feeds directly into the attention problem (`gov.administration` §7) |

## 6. Open Threads

- The indicators themselves → `metric.indicators` (this phase)
- Atlas overlay layers driven by this dataset → Phase 18 onward
- The Comparative Governance Register → `gov.regions`
- The attention problem → `cult.life`
