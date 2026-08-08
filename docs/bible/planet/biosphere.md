# Elysium — Biosphere

**Document ID:** `planet.biosphere`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/biomes.json`
**Inherits:** `planet.physical`, `planet.geography`, `planet.climate`

---

## 1. The Basis of Elysian Life

Elysian life arose independently and is **carbon-based and water-solvent**, but
it is not Earth life and is not interfertile with anything Earth-like.

| Property | Elysian biochemistry |
|---|---|
| Solvent | Water |
| Hereditary molecule | **Helicin** — a double-helical nucleic acid with **six** nucleobases |
| Genetic code | 4,096 possible codon meanings; 31 canonical proteinogenic amino acids |
| Chirality | Uniformly left-handed amino acid analogues, right-handed sugars |
| Primary photosynthetic pigment | **Phyllocyanin** |
| Accessory pigment | **Xantholin** (low-light and cold-adapted taxa) |
| Atmospheric O₂ | 21.9% at 1.06 bar — partial pressure ~1.10× Earth's |

Two consequences matter far beyond this chapter:

**The six-base genome.** Helicin's larger alphabet gives Elysian genomes greater
information density and, critically, a **natively higher error-correction
capacity** — repair enzymes exploit redundant codon families. Elysian biology is
therefore unusually stable across generations, cancers are comparatively rare,
and the genetics and longevity programmes of Phase 9 begin from a far better
starting position than Earth medicine did. This is a foundational reason the
Concord's healthcare ambitions are achievable rather than fantastical.

**Phyllocyanin is teal, not green.** It absorbs most strongly in the red and
yellow-orange and reflects in the blue-green, so Elysian vegetation ranges from
deep petrol-blue in the shaded equatorial canopy through jade and turquoise to
pale sea-green in arid scrub. Xantholin-dominant taxa — the boreal forests, the
polar margins, and deciduous species in their dormant season — are amber, ochre,
and rust. **The living surface of Elysium reads as teal and gold, not green and
brown.** This is a canonical visual fact and drives the Atlas's ecology palette
(`data/biomes.json`, field `palette`).

Higher oxygen partial pressure and 1.01 g support large active animals and
efficient flight; the largest flying Elysian animals exceed the mass of any
Earth bird by a wide margin, and gigantism among arthropod-analogues is common.

## 2. Kingdoms

Elysian multicellular life is grouped into five kingdom-level clades. Each is a
navigable category in the Atlas's ecology layer.

| Clade | Analogue | Defining trait |
|---|---|---|
| **Phytaea** | Plants | Phyllocyanin photosynthesis, cellulose-analogue walls |
| **Zoaea** | Animals | Motile heterotrophs; four-limbed and six-limbed body plans both common |
| **Mycora** | Fungi | Decomposers; also the base of Elysium's vast subsurface networks |
| **Thallidae** | Algae/protists | Marine primary production; the dominant oxygen source |
| **Archaeoforms** | Archaea/bacteria | Chemosynthesis, nitrogen fixation, extremophiles |

**Thallidae**, not Phytaea, generate the majority of Elysium's atmospheric
oxygen — 63% of net primary production is marine. The health of the ocean is
therefore not a moral preference in Concord policy but a respiratory necessity,
and this fact is quoted directly in the constitutional environment provisions
(Phase 4).

## 3. Terrestrial Biomes

Total land area **181.1 M km²** (`planet.geography`). Biomes describe *potential
natural vegetation*; human-modified land is an overlay, quantified in §6.

| Biome | Area (M km²) | Where | Character |
|---|---|---|---|
| Boreal taiga | 34.0 | Auroria | Xantholin-gold conifer-analogues; largest biome on Elysium |
| Equatorial rainforest | 22.0 | Verdanne, Myriad Isles, S. Elandris | Deep petrol-blue canopy, 110 m emergents |
| Tropical seasonal forest & savanna | 20.5 | Meridia margins, N. Elandris | Monsoon-deciduous, fire-adapted |
| Temperate broadleaf forest | 19.0 | S. Auroria, N. Meridia, Thalassar | Jade summer, rust autumn |
| Subtropical desert & semi-desert | 17.0 | Sirocc Basin | Hyper-arid core; salt pans, lithium brines |
| Temperate grassland | 16.5 | Meridian Plain | Historic agricultural core |
| Montane & alpine | 12.0 | Cindral Arc, Vail Spine, Thalassar Rim, Veydran Highlands | Lapse-zoned, endemic-rich |
| Tundra & polar barren | 10.5 | Boreal coasts, Veydra | Cushion flora, lichen-analogues |
| Oceanic temperate rainforest | 8.0 | N. Thalassar | Wettest land on Elysium (5,400 mm/yr) |
| Winter-wet scrub | 6.5 | S. Thalassar, Sirocc fringe | Aromatic, fire-cycled |
| Wetland & floodplain mosaic | 6.0 | Alcyon basin, Serapht margins | Disproportionate biodiversity and carbon |
| Coastal & littoral systems | 5.3 | All coasts | Tidal forest-analogues, dunes, salt marsh |
| Freshwater lakes & inland seas | 2.2 | Lake Serapht and others | Serapht alone is 96,000 km² |
| Permanent ice | 1.6 | Veydran Ice Cap, mountain glaciers | 1.42 cap + 0.21 glaciers |

## 4. Marine Realms

Total ocean area **351.5 M km²**.

| Realm | Area (M km²) | Notes |
|---|---|---|
| Abyssal plain & deep pelagic | 299.0 | Slow, cold, sparsely populated, largely unexplored |
| Continental shelf (< 200 m) | 26.5 | Mistral Shelf is the largest and most productive |
| Slope & rise | 21.0 | Nutrient-transporting margin |
| Trench | 2.0 | Deepest point 10,240 m (Serrance Trench, off Cape Serrance) |
| Reef systems | 1.8 | **Stonebloom** reefs, Myriad Isles and tropical shelves |
| Kelp-analogue forest | 1.2 | Cold shelves: Thalassar, Veydra, Boreal |

Hydrothermal vent fields along the Myriad Isles spreading ridge host
chemosynthetic Archaeoform ecosystems entirely independent of sunlight; they are
protected in perpetuity and are the principal natural laboratory for Elysian
origin-of-life research (Phase 8).

## 5. Flagship Organisms

Canonical species used as ecological indicators and as Atlas information-panel
anchors.

| Species | Clade | Range | Significance |
|---|---|---|---|
| **Skyroot** | Phytaea | Verdanne | 110 m emergent; single tree supports ~1,200 dependent species |
| **Vailpine** | Phytaea | Aurorian Taiga | Xantholin-gold conifer-analogue; the taiga's structural species |
| **Frostmane** | Zoaea | Auroria | 900 kg browsing herbivore; keystone of boreal nutrient cycling |
| **Silverdrift** | Zoaea | Mistral Shelf | Vast shoaling fish-analogue; foundation of the Thalassari fishery |
| **Stonebloom** | Thallidae + Zoaea symbiosis | Tropical reefs | Reef-builder; primary bleaching-risk indicator |
| **Austral glider** | Zoaea | Austral Ocean, Veydra | 6.4 m wingspan; the largest flying animal on Elysium |
| **Meshcap** | Mycora | Global forests | Subsurface network fungus linking forest root systems |
| **Alcyon lungfish** | Zoaea | Alcyon basin | Survives multi-year Sirocc droughts encysted in mud; cultural symbol of resilience |

## 6. The Human Footprint

| Land use | Share of land | Area (M km²) |
|---|---|---|
| Wild / minimally modified | 71.6% | 129.7 |
| Cultivated (field agriculture) | 8.9% | 16.1 |
| Managed forestry & rangeland | 14.6% | 26.4 |
| Built environment (all settlements, industry, transport) | 1.4% | 2.5 |
| Restoration in progress | 3.5% | 6.4 |

Two numbers deserve emphasis, because they are the ecological proof of the
founding philosophy rather than a claim about it.

**Built environment: 1.4%.** A population of this size and wealth occupies a
remarkably small footprint because Elysian settlement is dense, vertical, and
consolidated (Phase 10), and because transport corridors are shared and
multi-modal (Phase 10B).

**Cultivated land: 8.9%.** Elysium feeds itself on less than a tenth of its land
because a large share of calories comes from controlled-environment and marine
production (Phase 11). Field agriculture persists where it is genuinely superior,
not by default.

**Protected areas.** 44.0% of land (79.7 M km²) and 38.0% of ocean
(133.6 M km²) hold permanent protected status, including the whole of the
Veydran Ice Cap, the Verdanne core, all hydrothermal fields, and a connected
network of migration corridors. The legal instruments, enforcement, and the
process for altering a protected boundary are owned by Phases 4 and 7; the
extents themselves are canon here and drive the Atlas's protected-areas layer.

## 7. Biodiversity

- Described multicellular species: **2.41 million** (estimated true total 4.8 M).
- Species with complete reference genomes: 1.06 million.
- Documented extinctions attributable to industrial-era Elysian activity: 4,180
  species, the great majority before the ecological settlement (Phase 3).
- Species under active recovery programmes: 11,400.
- Functionally extinct in the wild but preserved in living collections: 260.

The **biodiversity index** used by the Concord to steer policy is defined in
Phase 16; this document supplies the underlying ecological facts it is computed
from. Canon requires the two never diverge.

## 8. Ecosystem Services and Failure Modes

| Service | Provider | Failure mode | Answered by |
|---|---|---|---|
| Oxygen production | Thallidae (63% of NPP) | Ocean acidification, stratification | Phase 7 |
| Carbon sequestration | Verdanne, taiga, wetlands, deep ocean | Fire, drought, permafrost-analogue thaw | Phase 7 |
| Fishery productivity | Mistral Shelf, Amarant Upwelling | Upwelling collapse in warm Amarant phases | Phase 11 |
| Pollination | Zoaea and Mycora complexes | Pathogen spread through managed populations | Phase 11 |
| Freshwater regulation | Cindral snowpack, Alcyon basin | Warming snowline; multi-year drought | Phases 7, 11 |
| Reef coastal protection | Stonebloom reefs | Thermal bleaching above +1.4 °C local anomaly | Phases 7, 10 |
| Soil formation | Mycora, Archaeoforms | Erosion under intensive cultivation | Phase 11 |

**Acknowledged residual risk:** a biosphere cannot be made safe, only monitored
and given room. The Concord's ecological doctrine is redundancy of habitat,
connectivity of range, and the constitutional principle that a system may not be
degraded faster than it is understood.
