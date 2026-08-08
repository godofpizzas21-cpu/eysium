# Regional and Local Government

**Document ID:** `gov.regions`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/regions.json`
**Inherits:** `gov.constitution` (decentralization by default, floors not
ceilings), `gov.institutions` (the Council of Regions), `hist.demographics`
(regional populations), `planet.geography`

All figures as of **EY 412, Calenth 16**.

---

## 1. Four Tiers

| Tier | Count | Typical population | Core competences |
|---|---|---|---|
| **Concord** (planetary) | 1 | 7.25 bn | The ten enumerated powers (`gov.constitution` §2.1) |
| **Region** | 34 | 213 million | Health, education, housing, policing, land use, most taxation |
| **District** | 1,104 | 6.6 million | Delivery: hospitals, schools, transit, utilities, planning |
| **Commune** | 47,900 | 151,000 | Neighbourhood: public space, local services, participatory budget |

The Concord tier is small in every sense. It employs 1.9% of all public
servants and spends 22% of all public money; the remaining 78% is raised and
spent below it. An Elysian's ordinary dealings with government are almost
entirely with their District and Commune, and most Elysians could not name more
than two of the nine Executive Board portfolios.

### The subsidiarity test

Article 3 is operationalised by a four-question test that any tier must satisfy
before taking a competence from the tier below. The Constitutional Court applies
it, and it is taught verbatim in civics:

1. **Can the lower tier do this at all?** If yes, the enquiry usually ends.
2. **Does the problem cross the lower tier's boundary?** Atmosphere does;
   refuse collection does not.
3. **Would fragmentation impose costs the gain does not justify?** This is the
   only economic question, and it is deliberately the third one.
4. **Is the transfer reversible?** An irreversible centralization requires a
   Tier 2 amendment, not an ordinary decision.

The fourth question is unusual and follows from the humility clause. Roughly a
third of competence disputes are decided on it alone.

## 2. The Thirty-Four Regions

Regions are the constituent units of the Concord. Their boundaries follow
watersheds, coastlines, and mountain divides far more often than historical
borders — a deliberate choice of the Meridian Convention, which held that a unit
that shares a river has a reason to cooperate that a unit that shares a grievance
does not.

Boundaries are not permanent. A Region may split, merge, or transfer territory
by referendum in every affected District plus Council of Regions consent. Eleven
boundary changes have occurred since EY 1.

**Meridia (9 Regions, 2.18 bn)** — Ilvaret, Alcyone, Sirocc, Cindral, Kethran,
Meridian, Verdanne, Amarath Coast, Sudmark.

**Elandris (9 Regions, 2.31 bn)** — Kessandra, Serrance, Andriel, Halvane,
Terrace North, Terrace South, Mirran, Oshaal, Delvane.

**Thalassar (5 Regions, 1.16 bn)** — Mistral, Fjordmark, Rimward, Sablewater,
Coronal.

**Auroria (5 Regions, 1.09 bn)** — Vailmark, Serapht, Korren, Northreach,
Hollen.

**Myriad Isles (3 Regions, 342 m)** — Kaelis Group, Orphir Group, Sable Group.

**Veydra (2 Regions, 140 m)** — Highmarch, Austral Shore.

**Off-world (1 Region, 28 m)** — the Orbital Territory, comprising Kalyra
settlements, orbital habitats, and Tyrran Belt stations. Its constitutional
position is genuinely unsettled and is taken up in `dipl.external` §1: it holds four
Council seats like any Region, but its residents are dispersed across
locations that do not share a horizon, let alone a watershed, and its District
structure is organised by installation rather than by territory.

Full populations, capitals, governing forms, and delegate-selection methods are
in `data/regions.json`, which drives the Atlas's political map layer.

## 3. Regional Government

The Charter says almost nothing about how a Region governs itself. This is not
an omission — Article 3 forbids the Concord from prescribing it. Regions must
satisfy four constitutional floors and are otherwise free:

1. Government by an elected body, on a franchise no narrower than the Concord's.
2. Charter rights fully enforceable within the Region.
3. An audit body the regional government cannot appoint, fund, or discipline.
4. Publication of records to the Concord standard.

The result is genuine institutional diversity, which the Concord treats as a
research asset rather than an untidiness. Four broad patterns exist:

| Form | Regions | Character |
|---|---|---|
| **Assembly–Executive** | 16 | An elected assembly choosing a small collegial executive; the commonest form and closest to the planetary model |
| **Assembly–Manager** | 9 | An elected assembly setting policy, a professionally appointed manager executing it on a fixed contract |
| **Direct-democratic** | 5 | Frequent binding referendums with a small standing council; all three Isle Regions and two Veydran |
| **Delegate council** | 4 | The Region is governed by delegates sent from its Districts, with no separately elected regional body |

The **Comparative Governance Register** — maintained by the Record Office —
tracks outcomes across the four forms on standard indicators (Phase 16). It has
found no form clearly superior overall, which Elysians cite as vindication of
letting Regions differ. It has found, repeatedly, that Assembly–Manager Regions
score highest on service delivery and lowest on public trust, and canon records
that nobody has satisfactorily explained why.

### Selecting Council of Regions delegates

Each Region chooses its four Council delegates by its own method
(`gov.institutions` §2.2). The current distribution:

| Method | Regions |
|---|---|
| Elected by the regional assembly | 19 |
| Directly elected by the regional electorate | 9 |
| Selected by a sortition panel from a qualified pool | 4 |
| Rotated among District heads on a fixed schedule | 2 |

Delegates are recallable by their Region at any time, which makes the Council a
genuinely regional chamber rather than a second national one — a delegate who
votes against their Region's settled position can be replaced within weeks, and
this happens roughly twice a decade.

## 4. Districts

Districts are where public services actually happen: hospitals, schools,
transit, water, waste, planning permission, and local policing all sit here.
A District averages 6.6 million people — large enough to run a teaching hospital
and a transit network, small enough that its council meetings are attended.

Districts are established by their Region, not by the Concord, and vary in
powers accordingly. Two features are universal because the Charter's provision
rights require them: every District must guarantee the housing, healthcare,
education, and subsistence floors within its territory, and every District
publishes a standard-format annual account comparable across the planet.

**Comparability is the quiet mechanism here.** The Concord cannot direct a
District, but it can require that every District's performance be published in
the same format. The resulting league tables are unofficial, universally read,
and considerably more feared by District councils than any Concord instruction
would be. Canon notes the obvious risk — measuring what is easy to measure — and
Phase 16 addresses it directly.

## 5. Communes

The Commune is the smallest unit of government, averaging 151,000 residents —
a large neighbourhood, a small town, or a valley. Communes handle public space,
street-level services, local planning consultation, and community facilities.

Their distinctive power is the **participatory allocation**: between 8% and 15%
of the Commune's budget (the share is set regionally) is allocated directly by
residents in open assembly and online deliberation, on a one-resident-one-vote
basis from age 16 EY. Participation averages 31% of eligible residents, higher
than any other form of Elysian political activity except planetary referendums.

Communes also hold the **local objection**: a Commune may formally object to any
District or Regional decision affecting it, which compels a published response
and a public hearing but does not block. It is the same suspensive design as the
Office of Future Generations — delay and force an answer, never veto.

## 6. Interregional Cooperation

Regions cooperate directly, without the Concord, through **compacts**: binding
agreements between two or more Regions on shared problems. There are 340 active
compacts, covering river basins, migratory corridors, shared universities,
disaster mutual aid, and cross-border transit.

Compacts must be registered and published, and may not create obligations
binding on non-parties or infringe Charter rights, but otherwise require no
planetary approval. The Concord regards them as the healthiest thing in Elysian
federalism: the great majority of interregional problems are solved by the
Regions concerned, and never reach the planetary tier at all.

## 7. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Interregional inequality** | Floors without ceilings (`gov.constitution` §8) means wealthy Regions race ahead. Fiscal equalization (Phase 6) narrows but does not close the gap, and is renegotiated in bad temper roughly every decade |
| **Capacity asymmetry** | Veydran and Isle Regions have small administrations and struggle to exercise competences they legally hold; the Concord funds shared services, which critics call centralization by the back door |
| **Comparability distortion** | Published league tables reward measurable outcomes and can quietly starve the unmeasurable |
| **Orbital Territory anomaly** | A Region defined by installations rather than territory strains every assumption in Article 3 (`dipl.external` §1) |
| **Boundary conservatism** | Watershed boundaries drawn at the founding no longer match settlement patterns in three Regions; the amendment threshold makes correction slow |
| **Compact opacity** | 340 compacts are published but rarely read; a compact can shape a Region's obligations more than any statute without ever being debated planetarily |

## 8. Open Threads

- Civil service, public administration, anti-corruption → `gov.administration` (this phase)
- Regional courts and local justice → Phase 5
- Fiscal equalization and regional taxation → Phase 6
- District-level service delivery in health, education, housing → Phases 8–10
- The Orbital Territory's constitutional position → `dipl.external`
- Indicator design and the measurement problem → Phase 16
