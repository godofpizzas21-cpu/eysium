# Energy Generation

**Document ID:** `energy.generation`
**Status:** Proposed
**Version:** 1.1.0
**Authoritative data:** `data/energy.json`
**Inherits:** `planet.resources` (renewable potentials, fusion fuels, Constrained
List), `planet.physical` (25.9-hour day, Kalyra tides), `hist.timeline` (fusion
transition EY 103–158), `gov.constitution` (Article 12, grid as an enumerated
power), `ind.industry` (public natural monopolies)

All figures as of **EY 412, Calenth 16**.

---

## 1. The Scale of It

| Indicator | Value |
|---|---|
| Mean planetary demand | **44 TW** |
| Per capita | 6.07 kW continuous |
| Peak-to-mean ratio | 1.31 |
| Share of energy delivered as electricity | 91% |
| Energy sector share of GCP | 6% (with utilities and materials recovery) |

Six kilowatts per person, continuously, is roughly two and a half times what the
Integration achieved at its industrial peak and is delivered without combustion
of any kind. It is the material precondition for most of what the modern Concord
does: desalination, recovery at rates above 90% (`ind.industry` §1),
controlled-environment agriculture (Phase 11), and orbital access (`space.infrastructure`) are
all energy-intensive substitutes for things that were once cheaper to do badly.

## 2. The Generation Mix

| Source | Share | Output | Share of technical potential used |
|---|---|---|---|
| **Fusion** | 58% | 25.5 TW | — (fuel-limited, not flux-limited) |
| Solar | 20% | 8.8 TW | 0.5% |
| Wind | 9% | 4.0 TW | 1.3% |
| Geothermal | 7% | 3.1 TW | 5.0% |
| **Tidal** | 3% | 1.3 TW | **47%** |
| Hydro | 2% | 0.9 TW | 21% |
| Marine thermal and current | 1% | 0.4 TW | 31% |

Two figures in the right-hand column matter.

**Solar, wind, and geothermal are nowhere near their limits.** The Concord uses
half a percent of its solar potential. Nothing physical constrains expansion;
what constrains it is materials, land, and the fact that fusion is already
sufficient.

**Tidal is close to its ceiling**, at 47% of technical potential, and this is
deliberate. Kalyra's tides are 1.2× Earth's and — the decisive property —
**perfectly predictable centuries in advance** (`planet.resources` §4). Elysian
grid planners value a source they can schedule in EY 700 far above one that is
merely cheap, and have built tidal out toward its physical limit precisely
because its output is knowable. The remaining potential is in sites the
protected-areas regime forecloses.

## 3. Fusion

**6,200 plants, averaging 4.1 GW each.** Deuterium–tritium, magnetically
confined, with tritium bred in lithium blankets.

| Property | Value |
|---|---|
| First net-positive commercial plant | EY 103 |
| Grid transition complete | EY 158 |
| Typical plant capacity | 4.1 GW |
| Fleet capacity factor | 0.86 |
| Typical plant design life | 60 EY |
| Fuel: deuterium | Seawater; effectively unlimited |
| Fuel: lithium (tritium breeding) | 900-year horizon |
| Neutron multiplier: beryllium | **120-year horizon (30 without recovery) — Constrained** |
| Plasma-facing: tungsten | 340-year horizon |

Fusion plants are **public enterprises** at the Regional or Concord tier
(`ind.industry` §7), because the Concord treats a technology whose failure mode
is a regional blackout and whose fuel cycle touches the Constrained List as a
natural monopoly rather than a market.

### The beryllium problem

Canon has stated this since Phase 2B and states it again here because it is the
single hardest constraint in the Elysian energy system: **the fusion fleet cannot
grow indefinitely, because beryllium runs out in roughly 120 years.**

The chain is worth setting out, because canon defines a reserve horizon as years
of supply at *net* consumption after recovery (`planet.resources` §1):

| Quantity | Value |
|---|---|
| Reserve | 900,000 t |
| Gross consumption | 30,000 t/yr |
| Recovery from decommissioned blankets | 75% |
| **Net virgin draw** | **7,500 t/yr** |
| Horizon without recovery | 30 years |
| **Horizon with recovery** | **120 years** |

The Concord's responses are three, none of them solved:

- **Substitution research** is a standing national priority. Lead-based
  multipliers work and are worse; nothing yet matches beryllium.
- **Recovery** from decommissioned blankets runs at 75%, which is what turns a
  30-year horizon into a 120-year one, and cannot easily go higher because
  neutron-activated beryllium is difficult to reprocess. Every other Constrained
  material recovers above 86%; beryllium is the exception, and the exception is
  the whole problem.
- **Off-world sourcing** (`space.infrastructure`) is the principal economic argument for the
  space programme. It is unproven at scale and expensive, and Concord energy
  planners describe it as a hope with a budget rather than a plan.

The honest position, published annually by the Networks portfolio, is that the
Concord has about a century to solve this and no current solution.

### Safety and siting

Fusion carries no runaway failure mode and no long-lived high-level waste, but
it is not consequence-free. Activated structural material requires management for
roughly 120 years, tritium handling is regulated stringently, and plants are
sited away from seismic risk where the geography permits — which in Cindral and
the Thalassar Rim it frequently does not. Two plants have suffered significant
release incidents, in EY 219 and EY 302; both were contained, both killed no one,
and both are taught in engineering formation as case studies.

## 4. Renewables

Renewables are not a supplement to fusion in Elysian planning. They serve three
functions fusion cannot:

**Distributed generation.** Solar and small wind are built at Commune and
District scale, on rooftops, over car parks and rail corridors, and on
agricultural land in dual use. This is what makes microgrid islanding possible
(`energy.grid` §3), and it is why 34% of Elysian generation capacity sits below
the regional grid rather than on it.

**Siting where fusion cannot go.** The Myriad Isles, Northreach, Austral Shore,
and thousands of remote settlements are served by local renewables and storage
rather than by transmission from a distant plant.

**Load-following.** Fusion plants run best at steady output. Solar, wind, and
hydro absorb variation, with tidal providing the scheduled component.

**Solar** is concentrated in the Sirocc Basin, which has the highest surface
irradiance on the planet (`planet.resources` §4), and its arrays double as the
power source for the lithium brine operations beneath them. **Wind** is
overwhelmingly austral and offshore, in the Ferrel westerly belt and the Austral
storm track. **Geothermal** follows the plate margins — Cindral Arc, Thalassar
Rim, Myriad Isles hotspot — and provides both electricity and direct heat.

## 5. The Long Day

Elysium's 25.9-hour day (`planet.physical`) has a consequence that shapes the
entire renewable system: **nights are longer, so solar storage requirements are
about 8% higher per installed watt** than an Earth-equivalent system, and the
daily demand cycle is correspondingly deeper.

Biphasic sleep (`hist.demographics` §1) partly compensates. Elysian demand has
**two peaks and two troughs** rather than one of each: a morning rise, a
pronounced dip through the Stillness, a long second-waking peak, and a deep
overnight trough. The Stillness dip is the single most useful feature of Elysian
load: it arrives in the middle of the solar day, every day, at a predictable
time, and grid operators schedule storage charging and industrial heat around it.

## 6. Fuels for What Cannot Be Electrified

91% of energy is delivered as electricity. The remainder is:

- **Synthetic hydrocarbons** for aviation, long-distance shipping, and a few
  industrial processes, manufactured from **atmospheric carbon** using fusion
  electricity. The carbon is drawn down and returned; the cycle is closed and
  the fuel is not fossil. This is the only reason air freight exists at all
  (`ind.industry` §6), and it is priced to stay at 1% of tonne-kilometres.
- **Hydrogen** for high-temperature industrial processes and as a storage medium.
- **Direct fusion heat** piped to co-located industry and to district heating in
  Auroria, where 71% of Aurorian buildings are heated from a plant rather than
  individually.

**Retained carbon remains untouched** (`planet.resources` §7). Synthetic fuel
manufacture is not extraction, and the constitutional prohibition on combusting
fossil carbon is unaffected by it — a distinction the Charter draws explicitly,
because the founders anticipated exactly this argument.

## 7. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Beryllium** | A century of headroom and no solution. Substitution has not worked, recovery is near its ceiling, off-world supply is unproven |
| **Tidal near ceiling** | At 47% of technical potential, tidal cannot grow much further; the remaining sites are inside protected areas and canon does not expect that to change |
| **Fusion siting in seismic zones** | Cindral and Thalassar Rim plants sit where the geothermal and industrial demand is, which is also where the earthquakes are |
| **Activated material inventory** | 120-year management obligation on a growing inventory, with no permanent disposal route agreed — deferred rather than solved |
| **Capacity factor plateau** | Fleet capacity factor has been 0.85–0.87 for sixty years; further gains would require plant designs the beryllium constraint makes unaffordable to prototype |
| **Renewable materials footprint** | Distributed solar and wind consume indium, gallium, and rare earths — all Constrained or near it — so the renewable share cannot expand without worsening a different scarcity |

That last is the structural bind of Elysian energy, and canon states it plainly:
**the Concord cannot escape its fuel constraint by building more renewables,
because renewables have a materials constraint of their own.** Every path
forward is a trade between two scarcities.

## 8. Open Threads

- Grid architecture, storage, microgrids, pricing → `energy.grid` (this phase)
- Carbon drawdown, the CO₂ corridor, climate resilience → Phase 7B
- Off-world beryllium and the economic case for space → `space.infrastructure`
- Materials substitution research → Phase 8
- Energy indicators → Phase 16
