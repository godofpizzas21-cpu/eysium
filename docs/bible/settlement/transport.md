# Transport

**Document ID:** `route.transport`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/routes.json`
**Inherits:** `city.urbanism` (twenty-minute standard, polycentric cities, the
Stillness), `ind.industry` (freight modal shares, just-in-time rejected),
`gov.constitution` (interregional transport as an enumerated power),
`energy.generation` (synthetic fuels), `env.conservation` (connectivity corridors)

All figures as of **EY 412, Calenth 16**.

---

## 1. How Elysians Actually Move

| Mode | Share of all trips |
|---|---|
| **Walking** | 41.0% |
| Urban transit — metro, tram, bus | 24.0% |
| **Cycling** | 22.0% |
| Interurban rail and maglev | 8.0% |
| Road vehicle | 4.4% |
| Air | 0.6% |

Nearly two-thirds of Elysian journeys are made on foot or by cycle, and this is
a consequence of urban design rather than of virtue. The twenty-minute standard
(`city.urbanism` §3) places everything essential within walking distance by
regulation; polycentric quarters mean there is no single centre everyone must
reach; and the Stillness restricts through-traffic in residential quarters
every afternoon.

**Private vehicle ownership is uncommon.** 11% of households own a road vehicle,
mostly in rural Auroria, Veydra, and the outer Isles where distances make it
necessary. In cities, road vehicles are overwhelmingly shared, summoned, and
autonomous.

## 2. Urban Movement

**Pedestrian priority is legal, not aspirational.** In collision, liability is
presumed against the larger and faster party, and city centres in every Region
above a population threshold are closed to private motor traffic entirely.

**Cycling** runs on protected networks physically separated from motor traffic —
1.9 million km of protected cycleway planet-wide — with secure parking mandatory
at every transit stop, workplace, school, and dwelling. Cycle share reaches 38%
in the flat Elandric delta cities and falls to 9% in mountainous Cindral.

**Transit runs late by default.** Because most social and civic life happens in
the long second waking (`cult.foundations` §4), Elysian transit timetables are
built around an evening peak that runs to roughly hour 23 of the 26-hour day,
with reduced overnight service rather than none. Fares are zero at the point of
use in 27 of 34 Regions and capped in the rest; the funding sits in the land
value tax on the reasoning that transit creates the land value it is paid from.

## 3. The Continental Networks

Interregional transport is an **enumerated Concord power**
(`gov.constitution` §2.1) and track is a **public natural monopoly**
(`ind.industry` §7). Operations may be public, cooperative, or private; the
infrastructure never is.

Standard maglev runs at **620 km/h**; four evacuated-tube corridors on the
busiest continental routes run at **900 km/h**. Conventional electrified rail
carries the bulk of freight and the slower passenger services.

| Continental network | Trunk corridors |
|---|---|
| **Meridia** | The Alcyon Trunk (Alcyon Mouth–Kelvaran–Sennary–Tessarel); the Cindral Line (Tessarel–Cindral Gate–Amarath Port); the Sirocc Spur |
| **Elandris** | The Terrace Trunk (Kessandra Reach–Ostervale–Andrivar–Lundareth–Oshaal); the Serrance Line |
| **Thalassar** | The Rim Line (Kalthane–Tessarene–Mistral Harbour–Sablewater); the Rimward Branch |
| **Auroria** | The Vail Trunk (Hollen–Korrast–Vail Forge–Seraphine–Korren); the Northreach Line |
| **Veydra** | The Austral Link (Highmarch–Austral Landing) |
| **Myriad Isles** | Inter-island ferry network; no fixed link |

A journey from Tessarel to Cindral Gate — 5,551 km across Meridia — takes 9
civil hours at standard maglev speed. Elysians consider this fast and do not
consider it urgent.

**Corridors are ecological infrastructure too.** Any transport corridor crossing
a connectivity corridor (`env.conservation` §1) must meet passage standards:
wildlife crossings at maximum 4 km intervals, no continuous barrier longer than
that, and lighting that meets dark-sky requirements. 61% of the Concord's rail
corridors qualify as connectivity corridor land in their own right, which is why
the protected-area figures include working landscapes.

## 4. Autonomous Vehicles

Road vehicles in Elysian cities are autonomous, electric, and shared. The
regulatory settlement rests on three rules that follow directly from earlier
canon rather than from vehicle engineering:

- **An identified operator is accountable.** No vehicle may operate without a
  named legal person answerable for its decisions — the same rule that governs
  automated administrative decisions (`gov.administration` §6).
- **The decision log is not held by the manufacturer.** Vehicle decision records
  go to the Record Office, which manufacturers may request but not edit — the
  identical arrangement to custodial recordings (`law.substantive` §3), and for
  the identical reason.
- **No optimisation target may include a person's identity.** A vehicle may not
  weigh who is in its path. This was settled by the Constitutional Court in
  EY 318 and is treated as an application of Charter right 6, equality before
  the law.

Autonomous road fatalities run at 0.11 per billion vehicle-km. Manual driving
remains lawful everywhere, requires a licence and periodic re-testing, and
accounts for 3% of vehicle-km and 34% of road deaths — a disproportion that
Elysian road safety authorities publish annually and that has not yet produced a
proposal to prohibit manual driving.

## 5. Rural and Remote Transport

The twenty-minute standard is an urban guarantee. Beyond the cities, the Concord
promises access rather than proximity:

- Every settlement above 400 residents has a scheduled service, minimum daily.
- Below that, **demand-responsive services** operate on request with a maximum
  booking lead of one day.
- Northreach, Austral Shore, and the outer Isles rely on air and sea links that
  weather interrupts; canon records in §6 that these are the least reliable
  services in the Concord.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Manual driving disproportion** | 3% of vehicle-km and 34% of road deaths. Published annually; no proposal to prohibit has been made, and the reasons are cultural rather than analytical |
| **Cycle share varies with terrain** | 38% in the delta cities, 9% in Cindral. Topography defeats policy and no Region has closed the gap |
| **Rural reliability** | Weather-interrupted air and sea links in three Regions; the Charter guarantees access and cannot guarantee it on any given day |
| **Corridor land take** | Passage standards make corridors wider and more expensive, and Communes resist new corridors even when the Region needs them |
| **Evacuated-tube corridors are fragile** | Four corridors, high capital cost, and a failure mode that closes the whole line for weeks. Their expansion has stalled twice |
| **Fare-free is not planet-wide** | 27 of 34 Regions; the remaining seven are disproportionately those with the weakest fiscal capacity, so the poorest Regions charge the most |

## 7. Open Threads

- Ports, air, orbital launch, intercontinental travel, freight → `route.gateways` (this phase)
- Orbital launch operations and off-world logistics → `space.infrastructure`
- Grid and communications backbone → `energy.grid`, Phase 13
- Disaster evacuation and transport in emergency → Phase 12
- Mobility and access indicators → Phase 16
