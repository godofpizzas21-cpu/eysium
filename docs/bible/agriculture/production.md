# Food Production

**Document ID:** `agri.production`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/agriculture.json`
**Inherits:** `planet.resources` (cultivated land, phosphorus, marine harvest,
soil), `planet.biosphere` (land use, Silverdrift, Mistral Shelf),
`energy.generation` (44 TW, cheap energy), `hist.timeline` (the Alcyon flow-share,
the Thalassar Accord, the Phosphorus Famine), `env.conservation` (nutrient runoff)

All figures as of **EY 412, Calenth 16**.

---

## 1. Where the Calories Come From

| Source | Share of calories | Land used |
|---|---|---|
| **Field agriculture** | 41% | 16.1 M km² (8.9% of land) |
| **Controlled-environment agriculture** | 24% | 0.04 M km² |
| Marine — wild capture and aquaculture | 14% | — |
| **Fermentation and cultured protein** | 13% | 0.02 M km² |
| Livestock on pasture and rangeland | 8% | Shared with the 26.4 M km² of managed rangeland |

The headline fact established back in Phase 2B is that **Elysium feeds 7.25
billion people on 8.9% of its land**, and this table is why. Field agriculture
persists where it is genuinely superior — grains, pulses, oil crops, and tree
crops — and everything else has moved to systems that use almost no land at all.

The enabling condition is energy. Controlled-environment agriculture and
precision fermentation are electricity-intensive processes that were uneconomic
before fusion (`energy.generation` §1) and are now cheaper than field production
for a large class of foods. Cheap energy is the reason Elysium's wild fraction is
71.6% rather than something far lower.

## 2. Field Agriculture

The prime arable of Elysium is the **Meridian Plain**, the **Elandric
Terraces**, the **Alcyon floodplain**, and **southern Auroria**
(`planet.resources` §6). Field agriculture is worked by 144.8 million people —
4% of the labour force — and is overwhelmingly organised as producer
cooperatives (`econ.markets` §1).

Practice is governed by the stewardship obligation on land
(`law.substantive` §5), which means an operator may not degrade the ecological
function of soil they hold. In practice this produces:

- **Continuous cover and rotation.** Bare soil over winter requires justification.
- **Net soil accumulation.** Formation runs at 0.6 t/ha/yr against lower losses,
  so Elysian soil is deepening — one of the few unambiguously positive
  environmental trends in canon.
- **Field-margin obligations.** A proportion of every holding is managed for
  passage and pollination, which is how farmland qualifies as connectivity
  corridor (`env.conservation` §1).

**Crop genetic diversity is a security concern, not an aesthetic one.** The
Concord maintains 41 distinct staple crop species in commercial production and
requires that no single cultivar exceed 15% of the planted area of its species.
Seed stock is held by **stewardship foundations** (`econ.markets` §1), whose
purpose-bound structure means nobody can sell the seed bank, and duplicated
across four geographically separated collections.

## 3. Controlled-Environment Agriculture

**1.1 million facilities**, mostly attached to or inside cities, producing 24% of
Elysian calories on 0.04 M km² — roughly 1/400th of the land field agriculture
uses for less than twice the output.

They produce nearly all leafy vegetables, berries, fruiting vegetables, and
out-of-season produce, plus a growing share of staples in Regions where field
conditions are poor. Northreach and Austral Shore are fed substantially from
controlled environments; growing food outdoors at 68° N in Auroria is possible
and pointless.

Water use is closed-loop and roughly 4% of equivalent field production. Pesticide
use is essentially zero. The trade is energy: 0.31 TW planet-wide, 0.7% of
generation, which the Concord regards as one of its better bargains.

## 4. Fisheries

**210 Mt harvested annually** — 84 Mt wild capture and 126 Mt aquaculture
(`planet.resources` §8).

The governing framework is still the **Thalassar Accord** of 14 BE
(`hist.timeline` §8): the first binding planetary treaty, agreed on fisheries
only, in the middle of the Long Emergency, by people who could not agree on
anything else. It worked, it held, and the founders' argument at the Meridian
Convention was substantially *"look — it works, on fish."* Modern Concord
fisheries law is a direct descendant.

**Quota mechanics.** Catch limits are set per stock by the Ecological
Commission's assessment (`gov.institutions` §6) — which measures and publishes
but cannot make policy — and allocated as regional catch shares. Every limit is
set **below** assessed maximum sustainable yield, with the margin published. Vessel
monitoring is universal and the data is public.

The **Mistral Shelf** is the richest fishery on Elysium, built on Silverdrift
shoals, and the **Amarant Upwelling** off western Elandris is the second. Both
are vulnerable to the Amarant Oscillation (`planet.climate` §2): in a warm phase
the upwelling weakens and the Amarant fishery's productivity falls sharply, which
is why quota is set on multi-year averages rather than annual assessments.

**Aquaculture** is predominantly closed-containment on land or in enclosed
coastal systems, fed on fermentation-derived feed rather than on wild-caught
fish — a change completed in EY 288 that ended the practice of catching fish to
feed fish.

**Two stocks are currently over-exploited**, both in Elandric coastal waters,
both under mandatory recovery plans, and both the subject of an unresolved
dispute between the Region and the Commission about whether the assessment or the
enforcement is at fault. Canon records that the system is good and not perfect.

## 5. Livestock

Livestock supplies 8% of Elysian calories, down from 34% before the founding.
**The decline was not prohibition.** No law forbids eating animals anywhere in
the Concord. Two ordinary forces did the work: cultured and fermented protein
became cheaper, and welfare law made animal husbandry more expensive.

The principal domesticates are the **durn** (a large grazing Zoaea kept for meat
and milk), the **pell** (a smaller flock animal kept for fibre and meat), and the
**corvet** (a bird-analogue kept for eggs).

**Welfare law is graded by sentience.** Species are assessed on a published
scale by an independent panel, and legal protections scale with the assessment
rather than with the species' economic role. The regime prohibits close
confinement, prohibits painful procedures without anaesthesia, requires outdoor
access appropriate to the species, mandates stunning before slaughter, and caps
transport duration at 6 civil hours.

Elysians talk about this in the language of the founding philosophy: a
civilization that intends to be **wealthy without cruelty** cannot exempt the
part of its economy where cruelty is cheapest. Canon notes the position is
contested at the margins — several traditional pastoral practices in Auroria and
Veydra sit uneasily with it, and the Concord has granted narrow cultural
derogations that its critics regard as inconsistent.

## 6. Fermentation and Cultured Protein

13% of calories, and the fastest-growing category for two centuries. Precision
fermentation produces proteins, fats, and specialised nutrients; cultured tissue
produces muscle and fat directly.

Both are electricity-intensive and therefore cheap. Cultured protein reached
price parity with pastured meat in EY 231 and is now roughly 40% cheaper, which
is the single largest reason livestock's share fell.

Canon records the Elysian attitude accurately: this food is ordinary. It is not
marketed as a substitute for anything, most Elysians alive have never eaten
anything else in that category, and the historical debate about whether it counts
as real food is studied in schools as a curiosity.

## 7. Nutrients

**Phosphorus is the binding nutrient** and the Concord's clearest example of
circularity converting an existential constraint into a manageable one
(`planet.resources` §6). Recovery from wastewater and agricultural residue runs
at **92%**, giving a 380-year reserve horizon; without recovery it would be 41
years.

The loop is a legal obligation, not a market outcome: nutrient recovery is a
mandatory function of every District's water and waste system, and a District
falling below the recovery standard is subject to the same enforcement as any
other Concord floor.

Nitrogen is unconstrained — fusion-powered fixation makes it effectively
unlimited. Potassium comes from Sirocc evaporites with a horizon over 1,000
years.

**The 8% that escapes the loop is the largest single pollution flow in the
Concord** and produces seasonal coastal hypoxia in four Regions
(`env.conservation` §4). It is the only pollution problem on Elysium that is a
live policy fight rather than a legacy cleanup, and it has not been solved.

## 8. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Nutrient leakage** | 8% loop escape, four Regions with seasonal hypoxia, no agreed solution and an active political fight |
| **Two over-exploited stocks** | Under recovery plans, with Region and Commission disputing whether assessment or enforcement failed |
| **Cultivar concentration despite the rule** | The 15% cap applies per species; in practice three staples are dominated by closely related cultivars that satisfy the letter of the rule and not its purpose |
| **CEA energy dependence** | 24% of calories depend on 0.31 TW; an extended grid failure is a food failure, and the 14-day islanding rule (`energy.grid` §1) is what stands between them |
| **Pastoral derogations** | Cultural exemptions from welfare law that the Concord's own welfare panel describes as inconsistent with the regime's stated basis |
| **Amarant vulnerability** | The second-largest fishery loses productivity in every warm phase, roughly one year in seven, and no management change alters that |

## 9. Open Threads

- Reserves, food security, and famine response → `agri.security` (this phase)
- Nutrient loops and water systems → `env.conservation`, `gov.regions`
- Fishery ecology and the Amarant Oscillation → `planet.climate`, `planet.biosphere`
- Food processing cooperatives and labour → `econ.markets`
- Food and nutrition indicators → Phase 16
