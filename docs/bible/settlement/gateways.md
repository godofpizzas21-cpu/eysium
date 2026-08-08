# Gateways: Ports, Air, and Orbit

**Document ID:** `route.gateways`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/routes.json`
**Inherits:** `route.transport`, `ind.industry` (freight modal shares, strategic
reserves), `energy.generation` (synthetic hydrocarbons), `city.urbanism`
(the distributed capital), `planet.physical` (equatorial launch advantage)

All figures as of **EY 412, Calenth 16**.

---

## 1. Freight

| Mode | Share of tonne-kilometres |
|---|---|
| **Rail and maglev** | 61% |
| **Sea** | 27% |
| Road | 11% |
| Air | 1% |

Elysian freight intensity is roughly **a third** of what the Integration achieved
at comparable industrial output (`ind.industry` §6), for one structural reason:
distributed manufacturing means most things are made near where they are used, so
there is simply less to move.

Freight is slow and cheap in energy terms by design. Sea freight runs at 26–34
km/h on fusion-electric hulls; rail freight is scheduled around passenger paths
rather than competing with them; and road freight is last-mile only, capped by
regulation at journeys under 300 km except where no rail alternative exists.

**Inventory is held high.** Just-in-time is explicitly rejected
(`ind.industry` §6), strategic reserves of Constrained List materials, critical
components, and medical supplies run to two years, and Districts hold local
reserves besides. A logistics system that cannot absorb a two-year interruption
is regarded on Elysium as an unfinished logistics system.

## 2. Ports

Sea is the only practical mover of bulk between continents. The Concord operates
**340 major ports**, all publicly owned as natural monopolies
(`ind.industry` §7), with operations franchised.

The largest are Kessandra Reach and Halvane Bay in Elandris, Mistral Harbour and
Kalthane in Thalassar, Amarath Port and Alcyon Mouth in Meridia, and Vail Forge's
outport in Auroria.

Ports carry two obligations beyond commerce. Every major port maintains
**disaster reception capacity** — the ability to receive and distribute relief at
scale on 48 hours' notice (Phase 12) — and every port is a **biosecurity control
point**, with hull, ballast, and cargo inspection under the Biosecurity portfolio
(`health.practice` §6).

## 3. Aviation, and Why There Is So Little of It

Air is **0.6% of passenger trips and 1% of freight tonne-kilometres**, and it is
priced deliberately to stay there.

Aircraft burn synthetic hydrocarbons manufactured from atmospheric carbon using
fusion electricity (`energy.generation` §6) — so aviation is not a fossil
activity and does not touch retained carbon. The cycle is closed. What keeps
aviation small is not emissions but **cost and the materials the fuel synthesis
consumes**, and the Concord has never reduced that cost.

There are 210 airports of any size on Elysium. Subsonic, roughly 850 km/h, no
supersonic service — the Concord evaluated it twice and concluded the energy and
noise costs bought a saving that Elysians did not want enough to pay for.

## 4. Crossing an Ocean

**Elysians rarely cross oceans, and this is one of the quiet oddities of their
civilization.**

A journey from Tessarene in Thalassar to Andrivar in Elandris is 13,485 km. By
sea it is 123 civil hours — **4.7 Elysian days**. By air it is 15.9 hours and
expensive. There are no intercontinental fixed links: the distances defeat
tunnelling, and the Concord has never seriously proposed one.

The result is a planet that is politically unified and physically spread out.
Most Elysians never leave their continent. Interregional migration is high
(`hist.demographics` §5) and overwhelmingly *within* a landmass.

**This creates a real problem for the distributed capital.** The Concord
deliberately placed its institutions on five continents (`city.urbanism` §2), and
those institutions must function across distances that take days to cross.

The answer is that **Concord governance is conducted remotely by default**.
Assembly sittings, Council deliberation, and committee work are hybrid as a
matter of standing order, with translation into all 41 registered languages
(`cult.languages` §4) making remote participation genuinely equivalent rather
than second-class. Physical travel is reserved for constitutional occasions,
Court hearings, and the periods each chamber sits in full.

Canon records the trade honestly: a legislature that mostly meets remotely is
less collegial, forms fewer cross-regional relationships, and is — by the
Assembly's own repeated finding — worse at the informal negotiation that
resolves disputes before they become positions. Every review since EY 250 has
identified this. None has proposed a capital city.

## 5. Orbital Launch

Launch is an **enumerated Concord power** (`gov.constitution` §2.1) and the
gateway to everything in `space.infrastructure`.

Elysium's 25.9-hour rotation gives an equatorial launch site a somewhat smaller
rotational assist than Earth's would, and its slightly higher escape velocity of
11.42 km/s makes launch marginally more expensive in energy terms
(`planet.physical` §3). Neither is decisive, and the Concord launches a great
deal.

| Site | Location | Role |
|---|---|---|
| **Kaelis Range** | Myriad Isles, ~1° S | Principal equatorial site; heavy lift |
| **Verdanne Range** | Southern Meridia, ~11° S | Secondary equatorial; crewed launch |
| **Sirocc Range** | Sirocc Basin, ~26° N | High-inclination and polar orbits; dry, empty, and instrumented |
| **Austral Range** | Austral Shore, ~62° S | Polar and retrograde; supports the observation constellations |

Two-source sufficiency (`ind.industry` §2) applies: no single range may hold more
than 60% of planetary launch capacity, and Kaelis currently holds 47%.

Launch is powered by fusion-electric infrastructure and uses synthetic propellant
manufactured on site. Environmental conditions are strict — Kaelis sits beside
inviolable reef systems, and its licence was contested for eleven years before it
was granted.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Remote governance costs collegiality** | Identified by every Assembly review since EY 250, never solved, and the alternative — a capital — is refused on principle |
| **Ocean crossing is slow and dear** | Most Elysians never leave their continent, and canon does not claim this is entirely healthy for a planetary polity |
| **Aviation cost has never fallen** | Synthetic fuel keeps aviation clean and expensive; the Isles and Veydra bear the isolation |
| **Port concentration** | Seven ports handle 41% of intercontinental tonnage, which sits uneasily with the Concord's own redundancy doctrine |
| **Launch concentration** | Kaelis at 47% is within the 60% cap and above where planners would like it, and the alternative sites are all worse-placed |
| **Freight rail capacity at ports** | The landward side of major ports is the tightest capacity constraint in Elysian logistics and has been for forty years |

## 7. Open Threads

- Orbital operations, stations, and off-world logistics → `space.infrastructure`
- Disaster reception, evacuation, and relief logistics → Phase 12
- Biosecurity at ports and borders → `health.practice`
- Freight, inventory, and strategic reserves → `ind.industry`
- Transport and access indicators → Phase 16
