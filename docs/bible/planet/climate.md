# Elysium — Climate

**Document ID:** `planet.climate`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/climate-zones.json`
**Inherits:** `planet.physical` (tilt 19.4°, day 25.9 h, year 384.24 dE,
insolation 1,255 W/m², mean surface temperature 13.5 °C, 34% land),
`planet.geography` (continents, oceans, currents)

---

## 1. The Climate Machine

Three inherited facts govern everything in this chapter.

**1. A 19.4° axial tilt.** The tropics reach only ±19.4°; the polar circles sit
at 70.6°. Compared to Earth, Elysium has a *narrower* tropical belt but far
*larger* mid-latitude zone, and much smaller regions of midnight sun. Seasonal
insolation contrast at 45° latitude is roughly 78% of Earth's. Seasons are real
and agriculturally decisive, but they are gentle: continental interiors that
would be brutal on Earth are merely severe on Elysium.

**2. A 25.9-hour day.** Elysium's angular velocity is 0.926 of Earth's, so the
Coriolis parameter is proportionally weaker. The consequences are systematic:

- **Wider Hadley cells.** The descending dry branch sits near 34–38° latitude
  rather than ~30°, pushing the subtropical arid belts poleward and widening the
  humid tropics beyond what the tilt alone would give.
- **Larger, slower weather systems.** The Rossby deformation radius is ~8%
  greater; mid-latitude cyclones are broader, longer-lived, and slower-moving
  than Earth's. Elysian storms are less violent per unit area but persist longer
  — a hazard profile of duration rather than intensity, which the Concord's
  disaster doctrine (Phase 12) is explicitly built around.
- **A stronger diurnal cycle.** Longer daylight and longer night mean greater
  day–night temperature swings inland (typically 1.3× Earth-equivalent), driving
  powerful late-afternoon convection and a pronounced evening thunderstorm
  regime in the tropics.

**3. Dispersed continents in a 66%-ocean world.** No landmass blocks a global
circumpolar flow in the south, and no supercontinent creates a true extreme
continental interior. Ocean thermal inertia dominates the planetary heat budget,
damping variability everywhere.

The net result is the single most important climatic fact in canon: **Elysium's
climate is unusually stable and unusually predictable.** The Concord did not
earn this; it inherited it. Environmental policy (Phase 7) is therefore framed
as the stewardship of a stable system, never the taming of a hostile one.

## 2. Atmospheric Circulation

Per hemisphere, three cells, as on Earth, but displaced poleward:

| Cell | Latitudes | Surface winds | Character |
|---|---|---|---|
| Hadley | 0–36° | Easterly trades | Rising at the ITCZ, descending 34–38° |
| Ferrel | 36–63° | Westerlies | Storm-track belt, broad slow cyclones |
| Polar | 63–90° | Polar easterlies | Weak; shallow polar cell, no strong vortex |

**The Intertropical Convergence Zone (ITCZ)** migrates between roughly 9° S and
9° N over the year — a narrower migration than Earth's, because of the smaller
tilt. This narrow, reliable migration is the hydrological foundation of Elysian
agriculture: the monsoon arrives, and it arrives on schedule. Interannual
variability of ITCZ position is ±1.6°, against Earth's ±4–5°.

**The polar vortex is weak.** With a shallow equator-to-pole temperature
gradient and weaker Coriolis force, Elysium lacks a tight, persistent
stratospheric vortex. Sudden warming events are frequent and mild rather than
rare and catastrophic; cold-air outbreaks into mid-latitudes are correspondingly
gentler.

**Standing oscillation.** One coupled ocean–atmosphere oscillation is canon:
the **Amarant Oscillation**, a 4.1-year (mean) fluctuation in the strength of the
Amarant Upwelling and the trade winds over the eastern Amarant Ocean. In its warm
phase the upwelling weakens, Elandric monsoon onset is delayed by 8–20 days, and
Thalassari rainfall increases. It is the closest Elysian analogue to an El Niño,
but its amplitude is roughly half, and it has been forecast reliably 14 months in
advance since the maturation of Concord climate modelling. Food reserve policy
(Phase 11) is sized against a three-consecutive-warm-phase scenario.

## 3. Ocean Circulation and Heat Transport

Canonical currents (`data/oceans.json`):

- **Solward Current** — warm, west-flowing equatorial current across the Solward
  Ocean, terminating against Thalassar's coast where it splits north and south.
  It is the dominant heat pump of the western hemisphere and the reason
  Thalassar is temperate and wet to 45° N.
- **Mistral Countercurrent** — *(added in this phase)* cold, equatorward flow
  along Thalassar's outer shelf margin, formed by the southward-turning branch
  of the Solward Current cooling at depth and returning. Where it meets warm
  surface water over the **Mistral Shelf**, it produces the vigorous nutrient
  mixing that makes that shelf the richest fishery on Elysium
  (`planet.geography` §2.4).
- **Veydran Gyre** — cold circum-Veydran flow driven by the austral westerlies;
  thermally isolates Veydra and drives the Austral storm track.
- **Amarant Upwelling** — cold, nutrient-rich upwelling off western Elandris;
  the eastern hemisphere's fishery cornerstone and a key modulator of monsoon
  strength.

**Overturning circulation.** Deep water forms in two places: the Boreal Ocean
beneath the seasonal ice, and along Veydra's Ice Margin. The resulting
overturning cell has an estimated turnover time of 980 years. Concord Earth-system
science treats the overturning as the planet's most consequential *slow* variable
and monitors its strength continuously; a sustained 20% weakening is a
constitutionally defined environmental emergency trigger (mechanism in Phase 7).

## 4. Climate Zones

Elysium's climates are classified by the **Standard Climate Register**, a
ten-class scheme maintained by the Concord's environmental science service
(institution named in Phase 8). Classes are defined by growing-season length,
annual precipitation, and seasonality index.

| Code | Zone | Approx. latitudes | Mean annual T | Precipitation | Exemplar |
|---|---|---|---|---|---|
| `E1` | Equatorial humid | 0–10° | 25–28 °C | 2,200–3,600 mm | The Verdanne; Myriad Isles |
| `E2` | Tropical monsoon | 5–22° | 23–27 °C | 1,400–3,000 mm (strongly seasonal) | Elandric coasts |
| `E3` | Tropical seasonal / savanna | 12–26° | 22–26 °C | 600–1,300 mm | Southern Meridia margins |
| `A1` | Subtropical arid | 20–36° | 18–26 °C | < 250 mm | Sirocc Basin |
| `A2` | Subtropical semi-arid steppe | 24–38° | 15–22 °C | 250–500 mm | Sirocc fringes |
| `T1` | Winter-wet temperate | 34–44° | 13–18 °C | 500–900 mm (winter-max) | Southern Thalassar |
| `T2` | Oceanic temperate | 38–52° | 8–14 °C | 1,200–2,600 mm | Northern Thalassar fjord coast |
| `T3` | Continental temperate | 34–54° | 4–12 °C | 400–800 mm | Meridian Plain; southern Auroria |
| `B1` | Boreal / subarctic | 50–70° | −6 to +4 °C | 300–600 mm | Aurorian Taiga |
| `P1` | Polar margin & tundra | > 68° | −18 to −2 °C | < 300 mm | Boreal coasts; Veydran Highlands |
| `H1` | Highland (elevation-modified) | any | lapse-adjusted | orographic | Cindral Arc; Veydran Highlands |

`H1` is an overlay class: it modifies whichever zone it sits within, applying a
lapse rate of 6.1 °C/km and orographic precipitation enhancement on windward
slopes.

## 5. Regional Climates

**Meridia.** Spans the full tropical-to-subtropical range. The Cindral Arc
intercepts the easterly trades off the Amarant Ocean, soaking its eastern flank
(> 3,000 mm/yr) and casting a continental rain shadow to the west. That shadow,
combined with Hadley descent at 34–38°, produces the **Sirocc Basin** — the
planet's largest desert, 20–30° N, hyper-arid at its core. Across it runs the
**River Alcyon**, an exotic river fed entirely by Cindral snowmelt and monsoon
runoff, which turns a dead basin into the historic cradle of Elysian agriculture
(Phase 3). South of the equator, the Verdanne sits in the ITCZ's southern
excursion and receives year-round convective rainfall.

**Auroria.** Continental and boreal. Winters are long (5.5 months below 0 °C at
60° N) but, thanks to the gentle tilt and oceanic heat, 6–9 °C milder than
equivalent Earth latitudes. The Vail Spine blocks Boreal Ocean moisture, leaving
the interior dry and snow-dominated; Lake Serapht generates substantial lake-effect
snowfall on its eastern shore. Aurorian settlement design (Phase 10) is a direct
response to the cold-and-dark season.

**Elandris.** The monsoon continent. The Amarant Upwelling cools the western
coast while the ITCZ and the summer land–sea thermal contrast drive a powerful
monsoon over the **Elandric Terraces**. Onset is reliable to within ±9 days in a
neutral Amarant Oscillation phase. **Cape Serrance** in the southeast lies at the
convergence of the monsoon trough and the mid-latitude storm track, producing
1–3 landfalling tropical cyclones per year — the planet's most storm-exposed
inhabited coast.

**Thalassar.** Maritime and mild along its whole length, warmed by the Solward
Current. The Thalassar Rim forces enormous orographic rainfall on its western
slopes (up to 5,400 mm/yr in the northern fjords — the wettest place on Elysium)
and creates a dry interior plateau. Frost is rare below 35° N.

**Veydra.** Cold, windy, and dry. The Veydran Gyre isolates it thermally; the
austral westerlies scour it. The **Veydran Highlands** at 2,100 m mean elevation
carry the planet's only permanent continental ice — the **Veydran Ice Cap**,
1.42 M km², far smaller than an Antarctic analogue because Veydra never reaches
the pole and the tilt keeps polar summer insolation relatively high. The seasonal
**Ice Margin** doubles the ice-covered area each winter.

**Myriad Isles.** Equatorial oceanic: warm, humid, minimal seasonality, and
almost no diurnal or annual temperature variation (annual range 2.1 °C). The
most climatically constant inhabited place on Elysium.

## 6. The Cryosphere and Sea Level

| Component | Extent | Notes |
|---|---|---|
| Veydran Ice Cap | 1.42 M km² permanent | Sea-level equivalent 3.9 m |
| Boreal sea ice | Seasonal above 78° N | No permanent multi-year pack |
| Austral sea ice (Ice Margin) | Seasonal, up to 8.1 M km² | Collapses to 1.6 M km² in summer |
| Mountain glaciers | 0.21 M km² | Cindral Arc, Vail Spine, Thalassar Rim |

Total cryospheric sea-level equivalent is 4.6 m — a small, well-characterised
budget. This is a structural resilience advantage: Elysium is not one ice sheet
away from a coastal catastrophe, and Concord coastal planning (Phase 10) is
built to a defensible worst case rather than an open-ended one.

## 7. Paleoclimate

Weak Milankovitch forcing — obliquity varies only ±0.6°, eccentricity stays
below 0.028 — gives Elysium **shallow glacial cycles**: a ~118,000-year rhythm
with a glacial–interglacial global temperature swing of about 3.4 °C, against
Earth's 5–6 °C. Ice ages on Elysium extended the boreal biomes and lowered sea
level by ~60 m; they never produced continental ice sheets over mid-latitudes.
This is the deep-time reason the Concord's homeland has never been erased and
its long-horizon institutions are rational rather than naive.

The industrial-era excursion — its magnitude, its correction, and the political
settlement that produced the CO₂ corridor of 320–360 ppm — is historical canon
owned by Phase 3, and its policy machinery by Phase 7.

## 8. Hazards and Failure Modes

Per `charter.canon-rules` §5, the climate system is documented with its failure
modes:

| Hazard | Where | Frequency / severity | Answered by |
|---|---|---|---|
| Tropical cyclone | Cape Serrance; Elandric coast | 1–3 landfalls/yr, design basis 285 km/h | Phases 10, 12 |
| Austral winter storm | Austral Ocean, Veydran coast | 20–30/season, long duration | Phase 12 |
| Monsoon failure | Elandris | Warm Amarant phase, ~1 yr in 7 | Phase 11 (reserves) |
| Sirocc drought | Sirocc Basin, Alcyon flow | Multi-year, 1 in 12 yr | Phases 7, 11 |
| Alcyon flood | Alcyon lower basin | Design basis 1-in-500-yr event | Phases 7, 10 |
| Boreal cold outbreak | Auroria | Annual, mild by Earth standards | Phase 10 |
| Overturning weakening | Global, slow | Constitutional emergency trigger at −20% | Phase 7 |
| Heat extremes | Sirocc, tropical cities | Rising with any CO₂ excursion | Phases 7, 9, 10 |

**Acknowledged residual risk:** the Concord cannot prevent any of these. Its
doctrine is early detection, absorbed impact, and rapid restoration — the same
pattern as its tectonic answer in `planet.physical` §6, and the recurring
signature of every Elysian system.
