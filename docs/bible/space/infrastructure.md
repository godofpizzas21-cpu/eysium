# Space Infrastructure

**Document ID:** `space.infrastructure`
**Status:** Proposed
**Version:** 1.1.0
**Authoritative data:** `data/space.json`
**Inherits:** `planet.physical` (the Helian system, Kalyra, Vesper, the Tyrran
Belt), `route.gateways` (four launch ranges), `mil.service` (Orbital Guard,
orbital accounting), `planet.resources` (beryllium, Constrained List),
`gov.constitution` (orbital space as a planetary commons), `ai.governance`
(the Cassian Rules)

All figures as of **EY 412, Calenth 16**.

---

## 1. Where the 28 Million Live

| Location | Population | Character |
|---|---|---|
| **The Low Ring** | 14.2 million | Rotating habitats and industry in low and mid orbit |
| **Kalyra** | 7.4 million | Surface settlements, the far-side observatory, logistics |
| **Vesper** | 3.1 million | The industrial moon; where off-world manufacture began |
| **Tyrran Belt** | 2.1 million | Mining and processing stations, on long rotations |
| In transit | 1.2 million | Crews, passengers, and long-haul construction |

28 million Elysians live off Elysium — 0.4% of the population, the whole of the
**Orbital Territory** (`dipl.external` §1), and the product of 260 years of
continuous building since the Outward Turn began around EY 150.

**Stationary orbit sits at 38,556 km** above the surface, a consequence of the
25.83-hour sidereal day and Elysium's mass. Communications, weather, and
navigation infrastructure occupy it; habitation does not, because the radiation
environment is worse and the delta-v to reach it is higher than the Low Ring.

## 2. The Low Ring

The Low Ring is not a single structure. It is roughly 3,400 orbital objects
above 100 tonnes, of which 210 are inhabited rotating habitats, arranged across
several inclination bands and coordinated as one traffic system by the Orbital
Guard (`mil.service` §1).

Habitats spin for gravity — most at 0.7–1.0 g at the rim — and are built
overwhelmingly from **Vesper and Belt material**, because lifting structural mass
out of a 1.01 g well with an 11.42 km/s escape velocity is something the Concord
does as little as possible. Roughly 94% of orbital structural mass by weight has
never been on Elysium.

Industry in the Low Ring concentrates on what microgravity and vacuum actually
help with: large single-crystal growth, certain alloys and glasses, precision
optics, and — the largest single activity — **assembly of things too big to
launch**, including the Belt vessels themselves.

## 3. Kalyra and Vesper

**Vesper** was first, and the reason is orbital mechanics. At 96,000 km it is
four times closer than Kalyra, its escape velocity is negligible, and it is a
captured carbonaceous body full of the volatiles and carbon that early orbital
industry needed. Off-world manufacture began there in the EY 160s and Vesper
remains the Concord's industrial moon, with a mass driver that has been the
cheapest source of bulk material in Elysian space for two centuries.

**Kalyra** came later and is where people settled. It has enough mass for
buried habitation and enough regolith for shielding, and its far side is the
quietest radio environment in the Helian system — permanently shielded from
Elysium's emissions by 1,290 km of rock.

The **Kalyra Far-Side Array** is the Concord's principal radio observatory and
one of the few installations anywhere on Elysium or off it that has a legal
protection zone written around it: no transmitter may operate within a defined
volume, and the restriction binds the Orbital Guard, commercial operators, and
the Service alike. It is the instrument that has resolved most of the 41
candidate technosignatures (`res.sciences` §2).

## 4. The Belt, and What It Is For

Belt operations exist for one reason and canon has said so since Phase 2B:
**beryllium**, and behind it the rest of the Constrained List
(`planet.resources` §9).

| Indicator | Value |
|---|---|
| Belt stations | 340 |
| Population on rotation | 2.1 million |
| One-way light lag to Elysium | 10–38 civil minutes |
| Typical transit, Elysium to Belt | 8–14 Elysian months |
| Share of Concord beryllium supply | **11%** |
| Share of platinum-group supply | 34% |

The honest assessment recorded in `energy.generation` §3 stands: off-world
sourcing is **"a hope with a budget rather than a plan."** Concretely: Belt
supply covers 11% of the Concord's 7,500 t/yr net virgin beryllium draw, which
extends the terrestrial horizon from 120 years to roughly 135. That is real,
it is worth having, and it is not a solution. After 180 years of
Belt operations, the Belt supplies about a ninth of Concord beryllium
consumption, and the economics have improved slowly. It does better on
platinum-group metals, where the ore grades are extraordinary and the tonnages
required are small.

Belt mining is subject to the same instruments as terrestrial mining
(`ind.industry` §4): restoration bonds posted before operations begin — here
meaning stabilisation and debris control rather than replanting — and material
passports following every tonne.

## 5. Autonomy and the Light Lag

The Belt's 10–38 minute one-way light lag creates a genuine conflict with
**Cassian Rule 4**, which requires that the accountable human have the practical
capacity to refuse (`ai.governance` §2). A human on Elysium supervising a Belt
system does not have that capacity; by the time they could object, the moment has
passed.

The Concord's resolution is simple and strict: **the named human must be inside
the light-lag budget.**

- Any Tier A system operating off-world must have its accountable human within a
  round-trip latency of **4 civil seconds**.
- In practice this means crewed presence: Belt stations carry accountable
  officers because the rules will not let them be supervised from home.
- Where no human can be within budget — deep-system probes, outer-planet
  missions — the system is **restricted to non-consequential action**. It may
  observe, record, manoeuvre for its own safety, and refuse. It may not decide
  anything that would require a Rule 3 signature on Elysium.

This is the reason the Belt is inhabited at all. A purely robotic Belt would be
cheaper and is not lawful, and Concord debate about relaxing the rule surfaces
roughly every thirty years. It has not been relaxed.

## 6. Marn and Planetary Protection

**Marn carries the only extraterrestrial life Elysians have ever found**:
fossil microbial mats in ancient lake sediments, confirmed in EY 214, and
persistent unresolved evidence of possible extant subsurface communities.

Marn is under **permanent quarantine**. Crewed landing is prohibited outright.
Robotic missions are sterilised to a standard that makes them expensive and slow,
and every sample returned is handled at the highest containment tier
(`health.practice` §6). The Concord has flown 61 Marn missions and landed
Elysians on it zero times.

The prohibition is Tier 1 entrenched and follows directly from the inviolable
places doctrine of Article 12 (`gov.constitution` §2.3): a biosphere that cannot
argue for itself, whose destruction would be irreversible and whose scientific
value is not yet understood, is exactly what that Article exists to protect.
Elysians regard the question as settled, and the small minority who want to land
have never come close to a majority anywhere.

## 7. Exploration

Robotic missions have visited every planet in the Helian system and 41 Tyrran
moons. Crewed presence extends to the Low Ring, Kalyra, Vesper, and the Belt —
and no further. No Elysian has been to Tyrran, and the Concord has no crewed
programme beyond the Belt.

**The Long Signal.** In EY 340 the Concord launched a fusion-accelerated probe
toward the nearest Helia-like star, on a trajectory that will arrive in
approximately 9,100 Elysian years. It transmits continuously. Nobody involved in
building it will learn what it finds, and nobody involved in receiving it will
have met anyone who built it.

The vote to fund it passed the Assembly by a wide margin and is cited in Elysian
civic education as the clearest single expression of the civilization's
relationship with time — the same instinct that produced century programmes
(`res.system` §4), the zero discount rate (`econ.money` §5), and buildings left
deliberately unfinished for successors (`cult.arts` §6).

## 8. Space Law

- **Orbital space is a planetary commons.** No Region may own or appropriate it;
  it is an enumerated Concord power (`gov.constitution` §2.1).
- **Every object above 10 cm is catalogued and attributed** to an operator by the
  Verification Inspectorate (`mil.service` §5). Unattributed objects are removed
  at the last known operator's cost.
- **Deorbit bonds.** Every object placed in orbit carries a bond covering its
  removal, posted before launch, on the same principle as mine restoration bonds.
- **No weapons in orbit.** Part of the Abolition and verified through the same
  accounting.
- **Use charges** fund the Orbital Guard and the commons, at 4% of Concord
  revenue (`econ.money` §4).

## 9. Known Weaknesses

| Weakness | Nature |
|---|---|
| **The Belt has not solved beryllium** | 11% of supply after 180 years; the economics improve slowly and the fusion fleet's growth ceiling remains |
| **The light-lag rule is expensive** | A robotic Belt would be cheaper and is not lawful; the rule is challenged roughly every thirty years and defended each time on Cassian grounds |
| **Habitat radiation ageing** | Low Ring habitats accumulate structural damage faster than models predicted; 14 of 210 are past their design life and operating under waiver |
| **Debris in mid orbit** | Attribution works and removal is slow; the mid-inclination bands hold a debris population the Guard describes as "manageable and not improving" |
| **Kalyra quiet zone erosion** | Commercial pressure to relax the transmitter exclusion is constant, and three exemptions have been granted since EY 380 |
| **Off-world dependence on Elysium** | Every habitat imports food, medicine, and complex components; none is self-sufficient, and the Concord has never tested what a 12-month resupply interruption would do |

## 10. Open Threads

- The Orbital Territory's constitutional position, external relations, first contact → `dipl.external` (this phase)
- Beryllium substitution → `res.sciences`
- Orbital Guard operations and debris → `mil.service`
- Space indicators → Phase 16
