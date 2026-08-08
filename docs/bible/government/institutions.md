# Planetary Institutions of the Concord

**Document ID:** `gov.institutions`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/government.json`
**Inherits:** `gov.constitution`, `cult.foundations` (discomfort with heroism,
comfort with disagreement), `hist.demographics` (112-year lifespans)

All figures as of **EY 412, Calenth 16**.

---

## 1. The Shape of the Planetary Tier

The Concord has **34 Regions** — 33 continental and one off-world territory
(`dipl.external`) — which are its constituent units. Their internal government is
owned by Phase 4B. This chapter covers only the planetary tier, which consists
of four parts:

1. **Parliament** — the Assembly and the Council of Regions
2. **The Executive Board** — a collegial executive of nine
3. **The Constitutional Court**
4. **The Independent Offices** — five bodies outside all three of the above

The fourth part is the one that would surprise an Earth constitutionalist, and
it exists because of the audit principle (`gov.constitution` §2.2): a body that
audits government cannot be part of government.

## 2. Parliament

### 2.1 The Assembly

The directly elected chamber and the primary legislature.

| Property | Value |
|---|---|
| Members | 720 |
| Term | 4 Elysian years |
| Electoral system | Open-list proportional representation in 34 regional constituencies, with a compensatory planetary tier correcting overall proportionality |
| Threshold | 1.5% planetary, or one full regional quota |
| Franchise | All residents aged 16 EY and above |
| Term limits | 3 consecutive terms; 5 terms lifetime in the Assembly |
| Typical turnout | 78.4% |

The lifetime cap matters more here than it would elsewhere. With a median
lifespan of 112 EY (`hist.demographics` §1), an uncapped Elysian politician
could plausibly serve seventy years, and several did in the Consolidation before
the Ninth Amendment closed it.

The Assembly legislates, holds the purse for planetary functions, elects and
dismisses the Executive Board, and can extend an emergency.

### 2.2 The Council of Regions

The chamber of the constituent units, and the guardian of decentralization.

| Property | Value |
|---|---|
| Members | 136 — four per Region, regardless of population |
| Selection | By each Region's own legislature, by its own method (Phase 4B) |
| Term | 6 Elysian years, staggered so one delegate per Region is replaced every 18 months |
| Powers | Absolute veto on any measure touching regional competence or the distribution of powers; suspensive veto (one year) on all other legislation; concurrence required for Tier 2 and Tier 3 amendments |

Equal representation regardless of population is a real and deliberate
distortion: Veydra's 140 million residents have the same Council weight as
Elandris's 2.31 billion. The founders accepted the distortion because the
Council's function is not to represent people — the Assembly does that — but to
prevent the large from legislating the small out of their competences. The
asymmetry is a live grievance in Elandris and appears in Concord politics
roughly once a decade.

### 2.3 How law is made

A bill passes the Assembly, then goes to the Council. If the Council finds it
touches regional competence, it may veto outright; the Assembly's only recourse
is the Constitutional Court, which rules on whether the competence claim is
sound. Otherwise the Council may delay one year, after which the Assembly may
pass it again by absolute majority.

Every bill carries a mandatory **impact statement** covering ecological effect,
effect on the Constrained List, distributional effect, and — distinctively — a
**reversibility statement**: what it would take to undo this law if it proves
wrong. A bill without a reversibility statement is out of order.

## 3. The Executive Board

The Concord has no president, no prime minister, and no single head of state or
government. It has a **Board of nine**.

| Property | Value |
|---|---|
| Members | 9, each elected individually by the Assembly and confirmed by the Council |
| Term | 4 Elysian years, 2 consecutive terms maximum |
| Chair | The **Convenor**, rotating among the nine every 18 months, never consecutively |
| Decision rule | Collective; decisions are of the Board, not of a member |
| Dismissal | Individually by Assembly majority; collectively by two-thirds |

Each member holds a portfolio and chairs the corresponding department, but no
member may direct another's portfolio, and the Convenor has no power over
colleagues beyond setting the agenda and speaking for agreed positions.

**Why nine and not one.** This is the constitutional expression of a cultural
fact: Elysians are uncomfortable with heroism (`cult.foundations` §5) and read a
single powerful executive as a single point of failure — a phrase that carries
moral weight on Elysium. The Cassian Incident (`hist.timeline` §8) taught the
same lesson from the other direction: a system that concentrates a decision in
one place will eventually put a catastrophe there.

The design has real costs, and canon records them. Collegial executives are slow.
The Board is regularly criticized as diffuse, hard to hold responsible, and prone
to lowest-common-denominator positions. The Serrance Storm Failure (EY 341) was
partly a coordination failure between two portfolios that each assumed the other
had acted. The Concord's answer has been better process rather than
consolidation, and whether that is wisdom or stubbornness is genuinely argued.

**The Convenor is not a leader.** Foreign observers, and later first-contact
protocols (`dipl.external` §3), consistently misread the office. The Convenor's own
standard formula on taking the chair — *"I speak for a decision, not for a
people"* — is taught in Concord civics precisely to forestall the mistake.

## 4. The Constitutional Court

| Property | Value |
|---|---|
| Justices | 15 |
| Term | **18 Elysian years, single, non-renewable** |
| Appointment | Nominating Assembly (§6) selects from a shortlist prepared by the judiciary and the Regions; Council of Regions confirms |
| Removal | Only for incapacity or serious misconduct, by two-thirds of both chambers on a finding of the Audit Service |
| Retirement | Mandatory at end of term; former justices are barred from all public office and from paid advocacy for life |

Single non-renewable terms exist because reappointment is leverage. The lifetime
bar on subsequent office exists because a justice with a future career has a
future patron. Both rules cost the Concord a great deal of accumulated expertise,
and both are considered worth it.

The Court's jurisdiction: constitutional review of legislation and executive
acts, competence disputes between the Concord and Regions, automatic review of
emergency declarations, arbitration of withdrawal terms, and reconciliation of
divergent language texts (`cult.languages` §4).

Judgments publish every dissent in full. A unanimous constitutional judgment is
rare and is noted as such in the headnote.

## 5. Elections

Elections are administered by the Electoral Commission (§6), never by government.

- **Assembly elections** every 4 years, on a fixed date. There is no power of
  early dissolution anywhere in the Charter — a deliberate removal of a tool the
  founders regarded as an invitation to opportunism.
- **Voting** is by open list, allowing preference for individuals within a party
  list. Voting is a right, not a duty; there is no compulsion.
- **Campaign finance** is entirely public. Private and corporate donations to
  candidates and parties are prohibited outright; each qualifying candidate
  receives an equal public allocation. Independent political expenditure must be
  registered, capped, and published in real time.
- **The record requirement.** Every candidate publishes a standard-format record
  of prior public positions, votes, and reversals. Changing one's mind is not
  penalized; concealing that one changed is.
- **Party system.** Six planetary parties currently hold Assembly seats, plus
  eleven regional formations. No party has ever held an Assembly majority alone;
  every Executive Board in Concord history has been a coalition of at least
  three.

## 6. The Independent Offices

Five bodies sit outside Parliament, Executive, and Court. They exist to satisfy
the audit principle, and their independence is structural rather than
conventional.

**Common protections (Article 9):**
- **Funding is constitutional**, set as a fixed proportion of planetary revenue
  and not voted annually. Parliament cannot starve an office that is
  investigating it.
- **Heads are appointed by the Nominating Assembly**, not by any organ they
  oversee, for single non-renewable 9-year terms.
- **Publication cannot be prevented.** No organ may delay, edit, or classify an
  independent office's report. Reports go to the public and to Parliament
  simultaneously.
- **Cooling-off.** Office heads and senior staff may not take any public office,
  or paid work in a sector they regulated, for 10 years afterwards.

| Office | Function |
|---|---|
| **The Audit Service** | Audits every organ of government — financial, performance, and legal compliance. Rebuilt after the Corran Scandal (EY 187); may compel documents and testimony, and its findings trigger removal procedures. |
| **The Record Office** | Administers the right of access to record and the Public Record Act; maintains the permanent archive; adjudicates access refusals. Its refusal-overturn rate is published quarterly. |
| **The Electoral Commission** | Administers elections, registers parties, enforces campaign finance, and certifies results. |
| **The Ecological Commission** | Monitors the Article 12 constitutional limits and publishes the planetary environmental account. It cannot make policy — it can only measure, publish, and, on a threshold breach, compel a response. |
| **The Office of Future Generations** | Represents the interests of Elysians not yet born. Holds a **suspensive veto**: it may delay any measure for one year and compel a published Parliamentary response addressing its objection. It cannot block anything permanently. |

**The Nominating Assembly.** Four hundred citizens chosen by lot from the full
adult population, serving one year, with paid leave from their employment as of
right. They appoint the heads of the five offices, confirm the shortlist for
Constitutional Court appointments, and do nothing else. Members may not be
appointed to any office they appointed for, or regulated by, for 10 years.

Sortition here solves a specific problem: any body appointed by an institution
is eventually captured by it. A body that exists for one year, is chosen at
random, and can never benefit from its own appointments has nothing to trade.
Canon is candid that the mechanism is imperfect — Nominating Assemblies are
lobbied intensively and vary noticeably in quality — but it has never been
successfully captured, and the Corran network's failure to capture the EY 187
Assembly is what ultimately exposed it.

**The Office of Future Generations is the most criticized institution in the
Concord.** Its critics argue it is unaccountable by construction, since it
represents a constituency that cannot vote it out; its defenders argue that is
precisely the point, and that a suspensive veto with a mandatory public reply is
the weakest form of power that could still work. It has used its veto 41 times in
206 years and been overridden, after the year's delay, 23 times.

## 7. Accountability in Practice

The Concord's accountability machinery is dense and worth stating plainly, since
later phases will invoke it constantly:

| Body | Audited by | Removable by |
|---|---|---|
| Assembly members | Audit Service | Electorate; recall by regional petition and referendum |
| Executive Board | Audit Service, Parliament | Assembly (individually or collectively) |
| Constitutional Court | Audit Service (conduct only, never judgments) | Both chambers, on an Audit finding |
| Independent Offices | **Each other, in rotation**, plus an external panel of Regional auditors | Both chambers, two-thirds, on a finding by the rotating auditor |
| Regions | Regional audit bodies + Concord Audit Service on Concord-funded functions | Their own electorates (Phase 4B) |

The rotating audit of the auditors is the Concord's answer to *quis custodiet* —
not a final custodian, but a cycle with no fixed apex. Elysians find the absence
of an apex reassuring for the same reason they distrust unanimity.

## 8. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Executive slowness** | Nine-member collegial decision-making is genuinely slow; contributed to the Serrance failure |
| **Council malapportionment** | Veydra's 140 M equal Elandris's 2.31 bn; a standing grievance |
| **Diffuse responsibility** | Collective decisions make individual blame hard to assign, which is sometimes a feature and sometimes an escape |
| **Sortition variance** | Nominating Assemblies vary in quality year to year and are heavily lobbied |
| **Expertise loss** | Single non-renewable terms and 10-year cooling-off discard enormous accumulated skill by design |
| **Coalition opacity** | Every Board is a coalition; the bargains that form it are published, but their real weight is not always visible |

## 9. Open Threads

- Regional and local government, and how Regions choose Council delegates → Phase 4B
- The civil service, public administration, and anti-corruption systems → Phase 4B
- Courts below the Constitutional Court, and all of criminal and civil law → Phase 5
- Public finance, taxation, and the constitutional funding formula → Phase 6
- Party politics, media, and civic participation → Phase 14
