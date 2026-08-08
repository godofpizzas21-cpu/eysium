# Industry, Materials, and Automation

**Document ID:** `ind.industry`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/industry.json`
**Inherits:** `planet.resources` (recovery rates, Constrained List, retained
carbon, timber yield), `econ.money` (extraction levy, zero discount rate),
`econ.markets` (ownership forms, labour), `gov.constitution` (Article 12,
deep-sea prohibition), `cult.foundations` (repair, restraint)

All figures as of **EY 412, Calenth 16**.

---

## 1. The Governing Idea: Materials Are Borrowed

Elysian industry rests on a legal fiction that has become an economic fact:

> **You may sell the product. You may not sell the material.**

A producer retains permanent responsibility for the physical substance it puts
into circulation. When a product reaches end of life, the material returns to the
producer or to a licensed recoverer at the producer's cost. Ownership of the
*thing* transfers to the buyer; ownership of the *stuff* never leaves.

This single rule is why the Concord's recovery rates run above 90% for almost
every material (`planet.resources` §2), and it is why almost every reserve
horizon in Elysian canon depends more on institutions than on geology. The
Constrained List extraction levy (`econ.money` §4) supplies the price signal;
producer responsibility supplies the obligation; and the two together make
recovery cheaper than extraction for most metals.

**Secondary supply now exceeds primary.** 71% of metal entering Elysian
manufacturing is recovered material rather than newly mined ore. For copper,
aluminium, and iron the figure exceeds 80%. Mining continues, but it is
increasingly a *topping-up* industry rather than a foundational one.

### The three enabling instruments

**Material passports.** Every manufactured product above a trivial threshold
carries a machine-readable record of its composition, its disassembly sequence,
the provenance of its Constrained List content, and its recovery route. The
passport is a legal document; falsifying one is a band 3 offence
(`law.substantive` §2.2). Recovery facilities read passports rather than guessing
at composition, which is the difference between recycling and downcycling.

**Design for disassembly.** Products must be separable into material streams
using published tools within a stated time. Permanent bonding of dissimilar
materials — glues, composites, potting compounds — requires justification and a
recovery route, and is refused where an alternative exists.

**The right to repair.** Spare parts, service manuals, diagnostic tools, and
firmware must be available to any owner or independent repairer, at
non-discriminatory prices, for **20 Elysian years** after last sale. Software
locks that prevent repair are void and their use is an offence. The repair sector
employs 34 million Elysians and is culturally prestigious — an expression of the
civic virtue of repair (`cult.foundations` §1) that Elysians make explicitly.

**Residual waste is 3.4% of material throughput.** Landfilling anything with a
material passport is prohibited; the residual is genuinely unrecoverable
material, and its volume is published per District.

## 2. Manufacturing

| Indicator | Value |
|---|---|
| Share of Gross Concord Product | 16% |
| Share of employment | 12% |
| Employment | 421 million |
| Output produced in facilities under 500 workers | 41% |
| Robots per 10,000 workers | 2,400 |

**Manufacturing is distributed, not concentrated.** There are no planetary
mega-factories. Production is organised regionally, with the same product made
in several Regions at moderate scale rather than in one Region at maximum scale.

This costs efficiency and is chosen anyway, for two reasons that recur throughout
Elysian engineering. The first is redundancy: a planetary supply chain with a
single source has a single point of failure, and the Long Emergency demonstrated
what that means when the failure arrives. The second is transport: moving
finished goods across a planet consumes energy and infrastructure that
distributed production does not need.

The Concord's standard requirement, written into procurement rather than into
general law, is **two-source sufficiency**: for any product the Concord considers
essential, at least two Regions must be capable of producing it, and neither may
hold more than 60% of capacity. Roughly 1,900 product categories are listed.

**Fabrication technology** is dominated by high-precision additive manufacture
and automated assembly, with molecular-scale processes confined to
semiconductors, catalysts, and biomedical work. Elysian industry is very good at
making moderate quantities of complex things close to where they are used, and
comparatively unimpressed by economies of scale.

## 3. Robotics and Automation

At 2,400 robots per 10,000 workers, the Concord is heavily automated by any
historical standard. Most physically dangerous, repetitive, and precise work is
performed by machines, and has been since roughly EY 200.

Automation is not treated as a threat, and canon is specific about why: the
Concord has never had an unemployment problem caused by it. Displacement is
real, continuous, and individually painful; aggregate employment is not the
issue. What the Concord built instead is a set of rules about *who bears the
transition cost.*

**The automation disclosure.** Any firm above 250 workers must publish planned
automation that will displace roles **two Elysian years before implementation**,
with the affected roles identified. The disclosure is public, not merely internal
to the workforce. It exists because the Concord judged that surprise, not
automation, is what makes displacement destructive.

**The transition right.** A worker displaced by automation is entitled to:
full income continuation for 2 Elysian years, funded retraining of their choice
for up to 3 years (Phase 8), placement support, and priority consideration for
vacancies with their former employer for 5 years. The right attaches to the
worker, not to the job, and cannot be waived by contract.

**There is no robot tax.** The Concord debated one seriously and rejected it in
EY 289, on the reasoning that a tax on the specific form of capital that
substitutes for labour would distort investment toward less productive
alternatives without helping the displaced worker, whom the transition right
helps directly. The minority report from that decision is still cited by its
supporters, and the argument resurfaces roughly every thirty years.

Automation of *decision-making* rather than of physical work is governed
separately and much more tightly, under the AI regime of Phase 13.

## 4. Mining

| Indicator | Value |
|---|---|
| Share of GCP | 4% (with materials recovery) |
| Employment | 21 million |
| Primary share of metal input | 29% |
| Active major operations | 1,240 |

Extraction is concentrated in the **Vail Spine** (iron, nickel, cobalt,
platinum-group, beryllium, rare earths), the **Cindral Arc** (zinc, lead,
tungsten), the **Thalassar Rim** (copper, silver), and the **Sirocc Basin**
lithium brines (`planet.resources` §2–3).

Three constraints define the industry:

- **Deep-sea mining is constitutionally prohibited.** The abyssal plain is the
  largest intact ecosystem on Elysium and is inviolable under Article 12
  (`gov.constitution` §2.3). The prohibition has been challenged twice, most
  recently during a beryllium shortage in EY 356, and has held both times.
- **Restoration bonds.** A full restoration bond, independently costed and
  posted in public funds, must be lodged *before* a site opens. The operator
  recovers it only on certified restoration. Abandoned sites are therefore
  impossible in principle, and the seven that exist all predate the rule.
- **Closed-loop water.** The Sirocc brine operations return all extracted water
  to the aquifer. The Sirocc fields are the most instrumented industrial site on
  the planet, and their monitoring data is published continuously.

**Beryllium remains the binding constraint** on the fusion programme
(`planet.resources` §3), and the case for orbital and Belt sourcing (`space.infrastructure`) is
made primarily in these terms rather than in terms of exploration.

## 5. Construction

| Indicator | Value |
|---|---|
| Share of GCP | 8% |
| Share of employment | 7% |
| Employment | 246 million |
| Structures manufactured off-site | 68% |
| Design life standard | 150 Elysian years |

**Engineered timber is the default structural material below 12 storeys**
(`planet.resources` §8), drawn from continuous-cover forestry with no clear-fell
above 4 hectares. Above 12 storeys, low-carbon cement and recovered steel
dominate.

Buildings are designed to two requirements that follow from the material
doctrine: a **150-year design life**, and **disassembly at end of life** with a
material passport covering the whole structure. Demolition to rubble is treated
as a recovery failure and requires justification.

68% of structure by value is manufactured off-site in controlled conditions and
assembled on site — the same distributed, moderate-scale pattern as the rest of
Elysian manufacturing, and the reason construction productivity has risen
steadily rather than stagnating.

## 6. Logistics

| Indicator | Value |
|---|---|
| Share of GCP | 5% |
| Share of employment | 6% |
| Freight moved | 41.2 Gt-km per capita annually |
| Freight by rail and maglev | 61% |
| Freight by sea | 27% |
| Freight by road | 11% |
| Freight by air | 1% |

Elysian logistics is deliberately slow and deliberately cheap in energy terms.
Air freight is 1% of tonne-kilometres and is priced to stay there; overnight
planetary delivery exists but is expensive and culturally regarded as slightly
absurd. The transport networks themselves are canon for Phase 10; what belongs
here is the industrial consequence: **distributed manufacturing means less
freight**, and Elysian freight intensity per unit of output is roughly a third
of what the Integration achieved at comparable industrial output.

Warehousing and inventory are held higher than efficiency would dictate.
Strategic reserves of Constrained List materials, critical components, and
medical supplies are maintained by the Treasury and Materials portfolio at
levels sized against a two-year supply interruption — an explicit rejection of
just-in-time logistics, which the Concord regards as an optimisation that
converts a robust system into a fragile one.

## 7. Public and Cooperative Industry

Industry is not uniformly private (`econ.markets` §1). Public enterprises
dominate where a market would be either impossible or dangerous:

- **Natural monopolies** — grid, water, rail track, ports, payment, identity.
- **Strategic materials** — Constrained List extraction and the strategic
  reserves.
- **Long-horizon research infrastructure** — fusion plant, orbital launch,
  planetary sensing.

Public enterprises are commercially operated, publish full accounts, may fail
and be restructured, and have a **statutory pay ratio limit of 8:1** between
highest and lowest full-time compensation. Worker cooperatives are strongest in
construction, food processing, repair, and precision manufacture, where they
account for over 40% of employment.

## 8. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Distributed production costs efficiency** | Two-source sufficiency and moderate scale carry a real unit-cost penalty, estimated at 9–14% for affected categories. It is paid deliberately and criticised constantly |
| **Beryllium** | The fusion programme's growth ceiling is a materials constraint with no terrestrial solution and an unproven off-world one |
| **Recovery plateau** | Recovery rates have not improved in forty years; the remaining 3.4% residual is genuinely hard, and further gains would cost more energy than the materials are worth |
| **Passport falsification** | Material passports are only as good as their accuracy; enforcement finds falsified passports in 0.9% of audited imports from small producers |
| **Transition right take-up** | 71% of eligible displaced workers claim the transition right; the non-claimants are disproportionately older and in small firms |
| **Repair prestige without repair capacity** | Repair is culturally admired and chronically short-staffed; vacancies in the sector run at 8.1% against 2.9% economy-wide |
| **Inventory cost** | Rejecting just-in-time ties up capital and warehouse space; the policy has never been costed against a counterfactual because no counterfactual exists |

## 9. Open Threads

- Concentration, competition, and inequality → `ind.concentration` (this phase)
- Energy supply and the fusion fleet → Phase 7
- Transport networks and freight corridors → Phase 10
- Agriculture and food processing → Phase 11
- Orbital industry and Belt sourcing → `space.infrastructure`
- Automated decision-making → Phase 13
