# Elysium — Physical Characteristics & Star System

**Document ID:** `planet.physical`
**Status:** Proposed
**Version:** 1.1.0
**Authoritative data:** `data/planet-physical.json`

---

## 1. The Star: Helia

Elysium orbits **Helia**, a stable G-class main-sequence star slightly more
massive and luminous than a typical G2V.

| Property | Value |
|---|---|
| Spectral class | G1V |
| Mass | 1.04 solar masses |
| Luminosity | 1.12 solar |
| Age | ≈ 5.1 billion years |
| Activity | Low variability (±0.04%), mild flare activity |

Helia's low variability is one of the physical foundations of the Concord's
long-horizon culture: the star will remain stable for billions of years, and
Elysian science has known this for centuries. Helia's mild flare cycle
(≈ 14.2 Elysian years) is fully monitored; its only civilizational relevance is
to orbital infrastructure shielding (see `space.infrastructure`).

## 1b. The Helian System

Helia holds seven planets and one substantial asteroid belt. Elysium is the
third.

| # | Body | Semi-major axis | Character |
|---|---|---|---|
| 1 | **Cindre** | 0.41 AU | Airless, tidally stressed rockball |
| 2 | **Halix** | 0.72 AU | Dense CO2 atmosphere, surface hot enough to melt lead |
| 3 | **Elysium** | 1.103 AU | — |
| 4 | **Marn** | 1.61 AU | Cold desert world, thin atmosphere, confirmed fossil microbial life |
| — | **The Tyrran Belt** | 2.3–3.5 AU | Asteroid population shepherded by Tyrran resonances |
| 5 | **Tyrran** | 5.2 AU | Gas giant, 291 Elysium masses; 61 known moons |
| 6 | **Nereus** | 9.4 AU | Ice giant |
| 7 | **Ossian** | 17.8 AU | Ice giant |

Two consequences run through the rest of canon. The **Tyrran Belt** is the source
of the impacting-body population that planetary defence exists to catalogue
(`mil.response` §3) and the target of the Concord's off-world materials
programme (`space.infrastructure` §4). **Marn** carries the only confirmed
extraterrestrial life yet found by Elysians — fossil microbial mats — and is
under permanent quarantine (`space.infrastructure` §6).

## 2. Orbit and Year

| Property | Value |
|---|---|
| Semi-major axis | 1.103 AU (165.0 million km) |
| Eccentricity | 0.011 (near-circular) |
| Solar year | **384.24 Elysian days** (≈ 414.7 Earth days) |
| Mean insolation | 0.92 of Earth's solar constant (1,255 W/m²) |

The near-circular orbit means seasonal forcing comes almost entirely from axial
tilt, not distance — seasons are symmetric between hemispheres and highly
predictable. The 0.24-day remainder is absorbed by a leap day roughly every
four years; the civil calendar built on this is owned by Phase 3
(`hist.calendar`), which inherits the clean factorization 384 = 12 × 32.

## 3. The Planet

| Property | Value |
|---|---|
| Mean radius | 6,510 km |
| Mass | 1.05 Earth masses |
| Surface gravity | 9.86 m/s² (1.01 g) |
| Solar day | **25.9 hours** (sidereal 25.83 h) |
| Axial tilt | **19.4°** |
| Magnetic field | 0.9 gauss equivalent; strong, stable magnetosphere |
| Land fraction | 34% land / 66% ocean |

The 19.4° tilt produces real but *gentle* seasons — polar day/night cycles
exist but are shorter and milder than a 23°-tilt world's. Combined with the
near-circular orbit and a large moon stabilizing the tilt (§5), Elysium's
climate machine is unusually steady on 10,000-year timescales. The Concord did
not design its planet, but its civilization is in part a product of this
stability — and its environmental policy (Phase 7) is explicitly framed as
*preserving a naturally stable system*, not taming a hostile one.

## 4. Atmosphere

| Property | Value |
|---|---|
| Surface pressure | 1.06 bar |
| Composition | N₂ 76.8%, O₂ 21.9%, Ar 0.9%, CO₂ 340 ppm (managed), trace |
| Mean surface temperature | 13.5 °C |
| Ozone layer | Intact, monitored |

Slightly lower insolation than Earth's is offset by marginally higher pressure
and water-vapor greenhouse; the equilibrium is Earth-like. The 340 ppm CO₂
figure is a *managed* value — the Concord's carbon regulation system (Phase 7)
holds atmospheric CO₂ within a constitutional target band of 320–360 ppm,
one of the clearest examples of the philosophy "resilient, continually
self-correcting" written into physical policy.

## 5. Moons

### Kalyra (major moon)
| Property | Value |
|---|---|
| Mean radius | 1,290 km |
| Orbital distance | 402,000 km |
| Orbital period | 26.4 Elysian days |
| Surface | Silicate, cratered highlands, basaltic maria-analogues |

Kalyra raises ocean tides ≈ 1.2× the strength of Earth's lunar tides,
stabilizes Elysium's axial tilt, and dominates the night sky at an angular size
≈ 10% larger than Earth's Moon. Kalyra hosts Concord installations (`space.infrastructure`).
Its 26.4-day period is close to, but deliberately **not equal to**, the civil
month Phase 3 will define (32 days) — Elysian calendars are solar, and the
drift of Kalyra through the civil month is culturally significant (Phase 14).

### Vesper (minor moon)
| Property | Value |
|---|---|
| Mean radius | 210 km |
| Orbital distance | 96,000 km |
| Orbital period | 3.09 Elysian days |

Vesper is a captured body: dark, fast-moving, visibly crossing the sky in a
single night — the origin of its name ("the evening runner" in Old Meridian,
Phase 3). Too small for tides of consequence; valuable as an early space-industry
site and counterweight anchor (`space.infrastructure`).

## 6. Tectonics and Interior

Elysium is tectonically active with **nine major plates** and a heat budget
similar to Earth's. Consequences the Concord engineers around:

- **Seismic zones** along the Cindral Arc (eastern Meridia) and the Thalassar
  Rim — building codes, early-warning networks, and disaster doctrine
  (Phase 12) are calibrated to a design-basis quake of magnitude 8.6.
- **Volcanism** concentrated in the Myriad Isles hotspot chain and the Cindral
  Arc; ~11 significant eruptions per century, all monitored.
- **Geothermal gradients** along plate margins are a canonical energy resource
  (Phase 7 quantifies capacity).

Failure mode acknowledged by canon: tectonic hazard cannot be eliminated, only
predicted and absorbed. The Concord's answer is redundancy and rapid response,
not prevention — a pattern that recurs across every Elysian system.

## 7. Why This Planet Shapes This Civilization

Three physical facts do disproportionate work in later chapters:

1. **Stability** (orbit, tilt, star) → long-horizon institutions and
   century-scale planning are *rational*, not utopian (Phases 4, 16).
2. **A 26-hour day** → the Elysian work-rest rhythm, shift structures, and
   productivity norms differ measurably from Earth baselines (Phases 6, 14).
3. **66% ocean with dispersed continents** → maritime trade, decentralized
   regional identity, and the political impossibility of any single land power
   dominating the planet — a geographic root of Concord federalism (Phase 4).
