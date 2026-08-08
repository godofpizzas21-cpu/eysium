# Elysium — Natural Resources

**Document ID:** `planet.resources`
**Status:** Proposed
**Version:** 1.1.0
**Authoritative data:** `data/resources.json`
**Inherits:** `planet.physical`, `planet.geography`, `planet.climate`, `planet.biosphere`

This document canonizes the **physical resource endowment** of Elysium: what
exists, where, how much, and for how long. Extraction policy, industry, and
energy systems built on this endowment are owned by Phases 6, 7, and 11.
Off-world resources are canonized in `space.infrastructure`.

---

## 1. Resource Doctrine (physical framing)

Concord resource accounting rests on three measured quantities, reported for
every material in `data/resources.json`:

- **Reserve** — economically and technically extractable stock, in tonnes.
- **Recovery rate** — the share of end-of-life material returned to use.
- **Reserve horizon** — years of supply at current net consumption, *after*
  recovery. A horizon under 150 years places a material on the **Constrained
  List**, which triggers substitution research and consumption ceilings
  (mechanisms in Phases 6 and 7).

A civilization designed to last centuries measures its materials in centuries.
Every figure below is a reserve horizon, not a reserve.

## 2. Metals and Industrial Minerals

| Material | Principal deposits | Recovery rate | Reserve horizon |
|---|---|---|---|
| Iron | Vail Spine (Auroria); Cindral foothills | 96% | > 2,000 yr |
| Aluminium | Lateritic Verdanne margins; Elandric uplands | 97% | > 2,000 yr |
| Copper | Thalassar Rim porphyries; Vail Spine | 94% | 610 yr |
| Nickel & cobalt | Vail Spine ultramafics | 93% | 480 yr |
| Zinc, lead | Cindral Arc massive sulphides | 91% | 390 yr |
| Titanium | Thalassar coastal sands | 95% | > 1,000 yr |
| Rare earth elements | Vail Spine carbonatites; Sirocc placer | 88% | **210 yr** |
| Silver | Thalassar Rim | 92% | **165 yr** |
| Platinum group | Vail Spine | 90% | **135 yr — Constrained** |
| Indium, gallium, germanium | By-product streams | 86% | **95 yr — Constrained** |

The **Vail Spine** is the single most important mineral province on Elysium, and
Auroria's early industrial dominance follows directly from it (Phase 3). The
**Thalassar Rim**, younger and seismically active, supplies the copper and
precious metals. Deep-sea nodule mining is technically feasible and
**constitutionally prohibited** — the abyssal plain is the largest intact
ecosystem on the planet, and canon treats it as untouchable (Phase 7).

## 3. Fusion and Energy Materials

Elysium's primary energy is fusion (system design in Phase 7); the fuel base is
canonized here.

| Material | Source | Stock | Horizon |
|---|---|---|---|
| Deuterium | Seawater, 33 ppm of hydrogen | 1.16 × 10¹⁶ t of ocean-borne D | Effectively unlimited |
| Lithium (tritium breeding) | Sirocc Basin brines; Veydran pegmatites | 41 Mt reserve | 900 yr |
| Beryllium (neutron multiplier) | Vail Spine, Cindral pegmatites | 0.9 Mt | **120 yr — Constrained** (30 yr without its 75% recovery) |
| Tungsten (plasma-facing) | Cindral Arc | 7.2 Mt | 340 yr |

The **Sirocc Basin lithium brines** are the strategic irony of Elysian
geography: the planet's deadest landscape underwrites its energy system. The
brine fields lie beneath salt pans in the hyper-arid core, are extracted with
closed-loop evaporation that returns all water to the aquifer, and are the most
heavily monitored industrial site on the planet.

**Beryllium is the tightest constraint in the Elysian energy system.** Canon
records this openly: the Concord's fusion programme has a materials bottleneck,
substitution research is a standing national priority, and off-world sourcing is
one of the principal economic arguments for the space programme (`space.infrastructure`).

## 4. Renewable Energy Resource Base

Physical potential, independent of what is actually built (Phase 7):

| Resource | Basis | Technical potential |
|---|---|---|
| Solar | 1,255 W/m² insolation; Sirocc Basin has the highest surface irradiance | 1,900 TW |
| Wind | Ferrel-belt westerlies; austral storm belt | 310 TW |
| Geothermal | Cindral Arc, Thalassar Rim, Myriad Isles hotspot | 62 TW |
| Hydro | Alcyon system; Thalassar Rim orographic runoff | 4.1 TW |
| Tidal | 1.2× Earth lunar tides; spring range 2.9 m open coast, 9.4 m in Thalassar's funnel bays | 2.8 TW |
| Marine thermal / current | Solward Current | 1.4 TW |

Tidal energy on Elysium is unusually attractive because Kalyra's larger tides
are perfectly predictable centuries ahead — a resilience property the Concord
values above raw capacity.

## 5. Water

| Stock | Volume | Notes |
|---|---|---|
| Ocean | 1.31 × 10⁹ km³ | 66% of surface |
| Cryosphere | 1.9 × 10⁶ km³ | Veydran cap and glaciers |
| Groundwater | 2.1 × 10⁷ km³ | Sirocc fossil aquifer is 8% of this |
| Surface fresh water | 1.4 × 10⁵ km³ | Lake Serapht is the largest single body |
| Atmospheric | 1.5 × 10⁴ km³ | — |

Fresh water is **abundant globally and scarce regionally**, which is the harder
problem. Two basins are structurally stressed: the **Sirocc Basin**, where the
fossil aquifer is non-renewing on civilizational timescales, and the **lower
Alcyon**, where demand concentrates. Desalination is cheap given fusion energy;
the binding constraint is not water but the ecological cost of moving it
(Phase 7).

## 6. Soil and Agricultural Base

- Prime arable soil: 21.4 M km² (11.8% of land) — Meridian Plain, Elandric
  Terraces, Alcyon floodplain, southern Auroria.
- Soil formation rate: ~0.6 t/ha/yr; net erosion under Concord practice is
  negative (soil is accumulating).
- **Phosphorus** is the binding nutrient. Sedimentary reserve 3.4 Gt; recovery
  from wastewater and agricultural residue runs at 92%, giving a horizon of
  **380 years**. Without recovery it would be 41 years. Canon states this
  explicitly because it is the clearest single example of circularity converting
  an existential constraint into a manageable one.
- Nitrogen is unconstrained (atmospheric fixation, fusion-powered).
- Potassium: Sirocc evaporites, horizon > 1,000 years.

## 7. Fossil Hydrocarbons

Elysium has substantial coal, oil, and gas — an estimated 2.9 Tt of carbon in
recoverable deposits, principally beneath the Meridian Plain, the Amarant
continental shelf, and northern Auroria.

**None of it is burned.** Extraction for combustion ended with the ecological
settlement (date and politics owned by Phase 3). A small extraction programme
continues for **chemical feedstock** where no synthetic route is yet superior —
roughly 0.02% of the pre-settlement rate — and the remainder is legally
classified as **retained carbon**: a geological store deliberately left in place
and counted as a national asset precisely because it is unused.

This is one of the defining canonical facts about the Elysian Concord. The
civilization is not wealthy because it has no fossil fuels; it is wealthy while
sitting on top of them, having decided not to.

## 8. Timber, Fibre, and Biological Materials

- Sustainable timber yield: 1.9 Gt/yr from 26.4 M km² of managed forestry, all
  under continuous-cover rotation; no clear-felling above 4 ha.
- Engineered structural timber is the default material for buildings under
  12 storeys (Phase 10).
- Marine biomass harvest: 210 Mt/yr, capped below assessed maximum sustainable
  yield in every fishery (Phase 11).
- Biopolymer feedstock: 340 Mt/yr from agricultural residue, displacing the
  majority of what petrochemistry would otherwise supply.

## 9. Constrained List and Failure Modes

Materials currently on the Constrained List (horizon < 150 yr): **platinum group
metals, indium/gallium/germanium, beryllium**.

| Failure mode | Consequence | Answered by |
|---|---|---|
| Beryllium exhaustion | Fusion programme growth ceiling | Phases 7, 15 (off-world), substitution research |
| PGM exhaustion | Catalysis and electronics constraints | Phase 6 substitution mandates |
| Sirocc aquifer depletion | Regional habitability loss | Phase 7 water policy |
| Phosphorus recovery-rate collapse | 380 yr horizon falls to 41 yr | Phase 11 nutrient loop integrity |
| Recovery-rate decay generally | Every horizon in this document shortens | Phase 6 circularity enforcement |

**The structural insight of this chapter:** almost every reserve horizon in
Elysian canon depends more on the recovery rate than on the size of the deposit.
The Concord's material security is an *institutional* achievement resting on a
*geological* base — and if the institutions fail, the geology alone gives it
decades, not centuries. Canon states this plainly so that no later phase may
treat abundance as automatic.
