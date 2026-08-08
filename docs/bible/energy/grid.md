# The Grid, Storage, and Energy Resilience

**Document ID:** `energy.grid`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/energy.json`
**Inherits:** `energy.generation`, `gov.constitution` (grid as an enumerated
Concord power), `gov.regions` (District and Commune tiers), `ind.industry`
(public natural monopolies, rejection of just-in-time), `cult.foundations`
(redundancy), `hist.timeline` (grid emergencies)

All figures as of **EY 412, Calenth 16**.

---

## 1. Three Layers That Can Survive Each Other

The Elysian grid is built on one governing requirement, which is the civic virtue
of redundancy (`cult.foundations` §1) written as engineering regulation:

> **Every layer must be able to lose the layer above it.**

| Layer | Operator | Function | Must survive |
|---|---|---|---|
| **Planetary backbone** | Concord (Networks portfolio) | HVDC links between continents and Regions; balances across time zones and weather systems | — |
| **Regional grids** | Regional public utilities | Bulk transmission and regional balancing | Loss of the backbone, indefinitely, at 80% of normal load |
| **District networks** | District utilities | Distribution | Loss of the regional grid, 30 days, at 60% of load |
| **Commune microgrids** | Communes and cooperatives | Local generation, storage, and critical loads | Loss of everything above, **14 days**, at 100% of critical load |

The 14-day Commune islanding requirement is the load-bearing rule. It means every
Commune on Elysium holds enough local generation and storage to keep its
hospital, water, cold chain, communications, and heating running for two weeks
with no external supply, and it is why 34% of generating capacity sits below the
regional grid.

It is also expensive — an estimated 11% premium on total system cost — and the
Concord pays it deliberately. The argument, made in every review since EY 271,
is that a grid optimised only for cost is a grid that has never been asked what
happens afterwards.

**Islanding is tested, not assumed.** Every Commune conducts a full disconnection
drill annually, unannounced within a stated month, audited by the Region.
Failures are published. In the last reporting year 6.1% of Communes failed to
sustain 14 days, concentrated in Northreach, Austral Shore, and older Elandric
urban Communes — a recurring finding discussed in §6.

## 2. The Backbone

The planetary backbone is undersea and overland HVDC, linking all five inhabited
continents and the Myriad Isles. Its purpose is not primarily to move energy from
surplus to deficit — fusion means few Regions are structurally in deficit — but
to **share variance**: a storm over the Austral wind fleet is not a storm over
Sirocc solar, and a fusion plant in refit is covered from four Regions away.

| Indicator | Value |
|---|---|
| Backbone capacity | 9.4 TW |
| Longest single link | Thalassar–Elandris, 11,400 km |
| Transmission losses, backbone | 4.1% |
| Statutory planetary reserve margin | **22%** |
| Current reserve margin | 24.6% |

The backbone is publicly owned and publicly operated, and generation is
forbidden from owning transmission (`ind.concentration` §2) — the vertical
prohibition exists so that nobody who sells power decides who may reach the
market.

## 3. Storage

Storage on Elysium is sized against darkness and disaster rather than against
price arbitrage.

| Medium | Share of capacity | Role |
|---|---|---|
| Thermal (molten salt, rock, and district heat stores) | 34% | Hours to days; industrial and district heat |
| Pumped hydro and gravity | 27% | Hours to days; the Thalassar Rim and Cindral provide the head |
| Flow batteries | 21% | Minutes to hours; grid stabilisation |
| Hydrogen and synthetic fuel | 14% | Weeks to seasons; the long-duration reserve |
| Electrochemical (fixed) | 4% | Sub-second to minutes; frequency response |

| Indicator | Value |
|---|---|
| Total installed storage | 2,140 TWh |
| Planetary cover at mean demand | 48.6 civil hours |
| Critical-load cover | 21 civil days |
| Round-trip efficiency, fleet mean | 71% |

The **long day makes storage more expensive** (`energy.generation` §5): a longer
night requires roughly 8% more storage per installed solar watt than an
Earth-equivalent system. The Stillness partly repays this, arriving as a
predictable midday demand trough that grid operators schedule charging into.

Hydrogen and synthetic fuel are held as the **seasonal reserve** and are
deliberately inefficient. At 71% fleet round-trip efficiency the Concord throws
away a great deal of energy, and considers this the correct trade: the energy is
abundant, and the reserve is what stands between a bad Austral winter and a
crisis.

## 4. Resilience and Its Failures

Two grid emergencies have been declared under the Charter's emergency powers
(`gov.constitution` §6), and both reshaped the system.

**The Kessandra Blackout (EY 271).** A protection-relay misconfiguration
propagated across northern Elandris, taking 380 million people off supply for up
to 60 civil hours. Islanding was supposed to prevent exactly this and largely
failed, because most Communes had never tested it. The Blackout produced the
mandatory annual islanding drill, the published failure register, and the
statutory 22% reserve margin.

**The Vail Cascade (EY 344).** A winter storm brought down three Aurorian
backbone links within nine hours. Islanding worked; 94% of affected Communes
sustained critical load for the full duration. The failure was elsewhere — the
restoration took 31 days because the Concord had allowed spare high-voltage
transformer stock to fall to eleven units planet-wide. The Cascade is the reason
strategic reserves of grid components are now held at two-year replacement levels
(`ind.industry` §6) and is cited constantly in the argument against just-in-time
logistics.

Both are taught. Neither is described in Concord materials as having been
anyone's isolated mistake, which is a deliberate historiographical choice
(`hist.timeline` §13).

## 5. Pricing and Access

Fusion has near-zero marginal cost, which breaks conventional energy pricing:
a market that prices at marginal cost cannot fund the plant. The Concord's answer
is a **three-part tariff**:

- **A baseline allowance**, free, sized to ordinary household needs — lighting,
  cooking, refrigeration, communications, heating to a defined comfort standard,
  and hot water. Roughly 61% of households never exceed it.
- **A usage charge** above the allowance, rising in bands, so that heavy
  discretionary use pays.
- **A capacity charge** on large and industrial connections, which is what
  actually funds plant construction.

The baseline allowance is not framed as a subsidy. It is the delivery mechanism
for the "clean air and water" limb of Charter right 12 — access to the commons —
extended by statute to energy on the reasoning that a household without power in
Northreach in Tavric is not participating in civic life.

**Industrial pricing** carries a materials surcharge tied to the Constrained List
levy (`econ.money` §4), so that energy-intensive processes using scarce materials
face both prices at once. Energy in the Concord is cheap; materials are not, and
the price system is designed to make that distinction impossible to miss.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Islanding failures** | 6.1% of Communes failed the 14-day drill last year, concentrated in exactly the Regions least able to fix it — the capacity asymmetry of `gov.regions` §7 appearing as an engineering problem |
| **Reserve margin gaming** | Regions count assets toward the 22% margin that are unavailable in the conditions that would need them; the Audit Service has flagged this three times without a satisfactory definition emerging |
| **Storage round-trip losses** | 71% fleet efficiency wastes energy on a scale that would be indefensible if energy were scarce, and the seasonal reserve is the worst of it |
| **Backbone concentration** | 9.4 TW across a small number of very long links; the Vail Cascade showed three failures can matter, and no Region wants a fourth link routed through it |
| **Transformer and component lead times** | Now reserved at two-year levels, but the manufacturing base for the largest HVDC components sits in four Regions, which sits uneasily with two-source sufficiency |
| **Cost of redundancy is never independently tested** | The 11% islanding premium is an estimate produced by the institution that requires the islanding, and no counterfactual grid exists to check it against |

## 7. Open Threads

- Carbon drawdown powered by this system, and the CO₂ corridor → Phase 7B
- Transport electrification and freight corridors → Phase 10
- Grid components, HVDC manufacture, and two-source sufficiency → `ind.industry`
- Disaster response and grid restoration doctrine → Phase 12
- Automated grid control and its governance → Phase 13
- Energy access and reliability indicators → Phase 16
