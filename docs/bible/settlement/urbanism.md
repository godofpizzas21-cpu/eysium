# Cities and Settlement

**Document ID:** `city.urbanism`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/cities.json`
**Inherits:** `planet.biosphere` (built environment 1.4% of land),
`hist.demographics` (87.4% urban, multi-generational households, biphasic sleep),
`gov.regions` (34 Regions, 1,104 Districts, 47,900 Communes),
`energy.grid` (14-day islanding), `env.climate` (hazards, managed retreat),
`cult.foundations` (the Stillness, the long evening)

All figures as of **EY 412, Calenth 16**.

---

## 1. Dense, Small, and Everywhere

| Indicator | Value |
|---|---|
| Urban population | 6.34 billion (87.4%) |
| Built environment | 2.54 M km² — **1.4% of land** |
| Mean urban density | 5,760 per km² |
| Cities over 1 million | 412 |
| Largest city (Kessandra Reach) | 21.4 million |

The defining spatial fact about the Concord is the one canon established back in
Phase 2B: **a highly urban civilization of 7.25 billion occupies 1.4% of its
planet's land.** It achieves this by being dense, vertical, and consolidated, and
by refusing to spread.

Elysian cities are not enormous. The largest holds 21.4 million; only nine exceed
15 million; the median resident of a city lives in one of about 2 million people.
Concord urban policy has consistently favoured *more cities* over *bigger
cities*, on the same reasoning that produced distributed manufacturing
(`ind.industry` §2): a settlement pattern with a few dominant nodes has a small
number of very expensive failure modes.

## 2. The Distributed Capital

**The Concord has no capital city.** Its planetary institutions sit on five
different continents, and this is deliberate.

| Institution | Seat | Region |
|---|---|---|
| The Assembly | **Sennary** | Meridian (Meridia) |
| The Council of Regions | **Korrast** | Vailmark (Auroria) |
| The Constitutional Court | **Tessarene** | Mistral (Thalassar) |
| The Independent Offices | **Andrivar** | Andriel (Elandris) |
| The Monetary Authority | **Orphir Reach** | Orphir Group (Myriad Isles) |

**Sennary** is the smallest of them at 1.4 million, purpose-built on the Alcyon
estuary within sight of the Meridian Stone (`planet.geography`), where the
Convention sat. It was kept deliberately small: the founders had watched capital
cities accumulate wealth, attention, and interpretation, and concluded that a
planetary legislature should sit somewhere nobody had a reason to move to for any
other purpose.

Placing the Monetary Authority in the Isles follows the same logic that produced
Concordial (`cult.languages` §3) — it belongs to no region's imperial past. The
arrangement is expensive and inconvenient, requires constant travel, and is
defended in exactly the terms the rest of Concord design uses: **a capital is a
single point of failure, and so is a capital's political culture.**

## 3. How an Elysian City Is Arranged

**The twenty-minute standard.** Every dwelling must lie within 20 civil minutes,
on foot or by cycle, of: a Commune health post, a school, a library, a food
market, a public green space, and a transit stop. This is a Concord floor, audited
per Commune, and currently met for 94.1% of urban dwellings.

Cities are therefore **polycentric** — networks of walkable quarters rather than
a centre with a periphery. A quarter of 20,000–60,000 people is the basic unit,
several quarters make a Commune, and the Commune is the unit of everything else
in Elysian life (`gov.regions` §5).

**The Stillness shapes the built form.** Acoustic standards are strict and
unusual: residential quarters must meet a daytime noise limit during the
Stillness that would be a night-time limit on Earth. Deliveries, construction,
and through-traffic are restricted in that window. An Elysian city genuinely goes
quiet in the early afternoon, and visitors find it the most disorienting thing
about the planet.

**The long evening shapes public space.** Because most social and civic life
happens in second waking (`cult.foundations` §4), Elysian cities invest heavily
in evening infrastructure: lit and sheltered public squares, extended market and
library hours, and transit that runs late by default. Dark-sky standards
(`env.conservation` §4) apply even in cities, which means lighting is downward,
warm, and low — Elysian cities glow rather than glare, and the aurora is visible
from the middle of most of them.

**Green is not optional.** Every dwelling within 300 m of usable green space
(96.8% compliance), continuous green corridors through every city connecting to
the regional connectivity network (`env.conservation` §1), and no city may reduce
its green area without replacing it elsewhere within its own boundary.

## 4. Building to Last

| Standard | Requirement |
|---|---|
| Design life | 150 Elysian years |
| Structural material below 12 storeys | Engineered timber by default |
| Off-site manufacture | 68% of structure by value |
| End of life | Disassembly, with a whole-building material passport |
| Accessibility | Step-free and adaptable as built, not on request |
| Adaptability | Dwellings must be subdividable and recombinable |

Two of these deserve explanation because they follow from earlier canon rather
than from Earth practice.

**Adaptability follows from household structure.** With multi-generational
households the plurality (`hist.demographics` §4) and four living generations
ordinary, an Elysian dwelling is expected to hold different numbers of people at
different points in a 150-year life. Apartments are built with movable
partitions, dual entrances, and services sized for subdivision, so a home can
become two homes and then one again without structural work. Elysians move house
far less often than Earth populations and reconfigure far more.

**Accessibility follows from ageing.** 710 million Elysians are over 100 EY, and
home-first healthcare (`health.system` §3) depends on dwellings that a frail
person can live and be cared for in. Step-free access, door and corridor widths,
bathroom provision, and structural capacity for later adaptation are all
mandatory in new build — not adaptations available on request, but the default
condition of every home.

## 5. Land

**In 61% of urban Districts the land beneath housing is publicly owned and leased
on 99-year renewable terms**, with the building privately owned. The remaining
Districts have freehold land subject to the stewardship obligation
(`law.substantive` §5) and land value tax (`econ.money` §4).

Separating land from building is the Concord's principal instrument against
housing speculation: the building depreciates and is maintained; the land's value
accrues to the Commune that created it through its own investment. Lease renewal
is automatic and cannot be refused for the purpose of raising ground rent.

Canon records honestly in §7 that this has not solved housing wealth
accumulation, only slowed it.

## 6. Resilience in the Built Form

Every Elysian city carries requirements that come from the hazard canon of
`planet.climate` §8 and `env.climate` §5:

- **14-day islanding** — local generation, storage, water, and critical services
  (`energy.grid` §1).
- **Cool refuge** in every Commune, publicly accessible, running on islanded
  power, sized for 30% of residents.
- **Cyclone design basis of 285 km/h** in Serrance, the Elandric coast, and the
  Isles.
- **Flood design basis of 1-in-500 years** in the Alcyon basin, achieved by
  floodplain reconnection rather than by walls.
- **Setback and retreat lines** published for every coastal Commune, with the
  retreat line legally binding on new construction.

**Subsea stations.** The Concord operates 41 permanent subsea habitats — research
stations on the continental shelves, hydrothermal observatories at the Myriad
fields, and maintenance bases for the undersea grid backbone. They house 41,000
people on rotation. Canon is precise that these are **stations, not cities**: no
Elysian settlement of any size exists underwater, no one is born in one, and the
Concord has never proposed subsea urbanisation. Living permanently below the sea
is regarded on Elysium as an expensive answer to a question nobody has.

## 7. Known Weaknesses

| Weakness | Nature |
|---|---|
| **The twenty-minute standard is 94.1%, not 100%** | The 5.9% shortfall is concentrated in older Elandric quarters and in Aurorian settlements too small to support the services |
| **Housing wealth still accumulates** | Leasehold land and land value tax slow appreciation without stopping it; housing remains a principal driver of the flat wealth Gini (`ind.concentration` §4) |
| **Heritage against density** | Communes hold real power over their own built form, and some use it to prevent the density the Region needs. There is no mechanism to override them and canon does not propose one |
| **Retreat lines are contested** | A published retreat line lowers property value the day it is drawn; three Regions have litigated their own lines |
| **Small-settlement viability** | Below about 8,000 residents a settlement cannot support the full Commune service set, and 6,100 settlements are subsidised to remain viable |
| **Sennary is unloved** | A capital nobody has a reason to move to is also a capital nobody knows, and Concord-tier remoteness (`gov.administration` §4) is partly architectural |

## 8. Open Threads

- Housing tenure, allocation, and the right to housing → `city.housing` (this phase)
- Transport networks, transit, freight, and orbital launch sites → Phase 10B
- District and Commune service delivery → `gov.regions`
- Disaster response and evacuation operations → Phase 12
- Urban and housing indicators → Phase 16
