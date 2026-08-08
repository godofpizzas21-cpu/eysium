# Elysium — Geography

**Document ID:** `planet.geography`
**Status:** Proposed
**Version:** 1.1.0
**Authoritative data:** `data/continents.json`, `data/oceans.json`
**Amended by:** Phase 2B (`planet.climate`, `planet.biosphere`, `planet.resources`)

Coordinates use the conventions of `charter.canonical-units` §1. The prime
meridian (longitude 0°) is defined through the **Meridian Stone** on the west
coast of central Meridia — the site where the Concord's founding charter was
signed (Phase 3 canonizes the event; this document canonizes the location:
0.0° E, 12.5° N).

---

## 1. Overview

Land covers 34% of Elysium's surface, divided among **five continents** and the
**Myriad Isles** archipelago, separated by **five named oceans**. No continent
holds a majority of land, population, or resources — a fact with deep political
consequences (see `planet.physical` §7).

| Continent | Approx. area (M km²) | Share of land | Character |
|---|---|---|---|
| Meridia | 58.2 | 32% | Equatorial–temperate heartland; cradle of the Concord |
| Auroria | 41.5 | 23% | Boreal north; forests, minerals, long winters |
| Elandris | 31.0 | 17% | Subtropical east; monsoonal, densely habitable coasts |
| Thalassar | 27.4 | 15% | Maritime west; fjords, rain, ocean economy |
| Veydra | 19.4 | 11% | Subpolar south; highlands, ice margin, research heart |
| Myriad Isles | 3.6 | 2% | Volcanic equatorial archipelago |

*(Areas are canon; the polygon geometry in `data/continents.json` is a
deliberately coarse cartographic outline for the Atlas and will gain detail in
later data revisions without changing these canonical areas.)*

## 2. The Continents

### 2.1 Meridia — the Heartland
Spanning the equator from roughly 25° S to 30° N and longitudes 30° W–45° E.
The largest and most populous continent and the birthplace of the Concord.

- **Cindral Arc** — the great eastern mountain system (highest peak **Mount
  Cindral**, 7,940 m), seismically active, geothermally rich.
- **River Alcyon** — Elysium's longest river (5,850 km), flowing west from the
  Cindral Arc across the Meridian Plain to the Solward Ocean; its basin feeds
  a third of Meridia's agriculture.
- **The Meridian Plain** — vast temperate lowland, historic agricultural core.
- **The Verdanne** — equatorial rainforest belt of southern Meridia, the
  planet's largest carbon sink and biodiversity reservoir (`planet.biosphere`).
- **The Sirocc Basin** — the planet's largest desert (17.0 M km², 20–30° N),
  lying in the Cindral Arc's rain shadow beneath the Hadley descent. Hyper-arid
  at its core, crossed by the exotic River Alcyon, and underlain by the lithium
  brines that fuel the Concord's fusion programme (`planet.climate`,
  `planet.resources`).
- The **Meridian Stone** (0.0° E, 12.5° N) anchors the prime meridian on the
  Alcyon estuary's northern shore.

### 2.2 Auroria — the Boreal North
Between 35° N and 75° N, longitudes 60° E–150° E.

- **The Aurorian Taiga** — the largest contiguous forest on Elysium.
- **The Vail Spine** — an old, eroded mountain range (max 4,200 m) rich in
  metal ores; historically the source of Auroria's industrial strength.
- **Lake Serapht** — largest freshwater body on the planet (area 96,000 km²).
- Long winters and the 26-hour day at high latitude shaped Auroria's compact,
  energy-conscious settlement culture (Phases 10, 14).

### 2.3 Elandris — the Monsoon East
Between 35° S and 10° N, longitudes 100° E–160° E.

- **The Elandric Terraces** — monsoon-fed uplands, the planet's most productive
  rice-analogue agriculture (Phase 11).
- **Cape Serrance** — the storm-wracked southeastern promontory; the proving
  ground of Elysian maritime engineering.
- Dense, ancient coastal urbanism; Elandris holds the highest population
  density of any continent (Phase 3 quantifies).

### 2.4 Thalassar — the Maritime West
Between 10° S and 45° N, longitudes 140° W–90° W.

- **The Thalassar Rim** — young coastal mountains along the western seaboard;
  seismically active; spectacular fjord systems in the north.
- **The Mistral Shelf** — broad, shallow continental shelf; the richest
  fishery on Elysium (Phase 11) and site of pioneering underwater settlements
  (Phase 10).
- Thalassari identity is oceanic: shipbuilding, navigation, and the oldest
  continuous meteorological records in canon.

### 2.5 Veydra — the Austral South
Between 70° S and 35° S, longitudes 80° W–10° W.

- **The Veydran Highlands** — cold plateau averaging 2,100 m elevation.
- **The Veydran Ice Cap** — Elysium's only permanent continental ice,
  1.42 M km² on the highlands; permanently protected (`planet.climate` §6).
- **The Ice Margin** — seasonal ice shelf on the southern coast; Elysium has
  no permanent continental ice sheet of Antarctic scale, a consequence of the
  19.4° tilt and ocean circulation (`planet.climate`).
- Sparse population, immense scientific presence: Veydra hosts the Concord's
  flagship observatories and deep-time research stations (Phase 8).

### 2.6 The Myriad Isles
A volcanic hotspot chain straddling the antimeridian (165° E–165° W) near the
equator; three major islands (**Kaelis**, **Orphir**, **Sable**) and ~400
minor ones. Culturally distinct, constitutionally a full region of the Concord
(Phase 4); the planet's spiritual capital of ocean stewardship (Phase 14).

## 3. The Oceans

| Ocean | Share of ocean area | Notes |
|---|---|---|
| **Solward Ocean** | 38% | The great western ocean between Thalassar, Meridia, and Veydra; named for the **Solward Current**, the warm equatorial stream that moderates Thalassar's climate. |
| **Amarant Ocean** | 30% | Eastern ocean between Meridia, Auroria, and Elandris; monsoon engine of Elandris. |
| **Meridian Sea** | 12% | The busy waters between southern Meridia and Veydra; densest shipping lanes on the planet. |
| **Boreal Ocean** | 11% | North polar ocean; seasonally ice-covered above 78° N. |
| **Austral Ocean** | 9% | South polar ocean ringing Veydra's Ice Margin; the stormiest waters of Elysium. |

Major circulation (mechanism detailed in `planet.climate` §3):
- **Solward Current** — warm, west-flowing equatorial current, the single most
  important climate feature of the western hemisphere.
- **Mistral Countercurrent** — cold equatorward return flow along Thalassar's
  shelf margin; its mixing with the Solward Current's warm water is what makes
  the Mistral Shelf the richest fishery on Elysium.
- **Veydran Gyre** — cold circumpolar-style gyre driving Austral storm tracks.
- **Amarant Upwelling** — nutrient-rich upwelling off western Elandris;
  fisheries cornerstone.

Ocean floor features of note: the **Serrance Trench** (10,240 m, the deepest
point on Elysium) and the **Myriad Hydrothermal Fields**, both canonized in
`planet.biosphere`.

## 4. Hazard Geography (summary)

- Seismic: Cindral Arc, Thalassar Rim (design-basis M 8.6, `planet.physical` §6).
- Volcanic: Myriad Isles, Cindral Arc.
- Storm: Cape Serrance (monsoon cyclones), Austral Ocean (winter storms).
- Flood: Alcyon basin (managed, Phase 7/11).

Every hazard listed here must be answered by a named system in Phases 7, 10,
and 12; this list is the checklist those phases design against.
