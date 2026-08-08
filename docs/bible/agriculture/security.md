# Food Security and Reserves

**Document ID:** `agri.security`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/agriculture.json`
**Inherits:** `agri.production`, `planet.climate` (monsoon failure, Sirocc
drought, the Amarant Oscillation), `hist.timeline` (the Phosphorus Famine),
`gov.constitution` (rights 11 and 12; emergency powers), `ind.industry`
(just-in-time rejected, strategic reserves)

All figures as of **EY 412, Calenth 16**.

---

## 1. The Memory Behind the System

The **Phosphorus Famine** of 61–54 BE killed 210 million people
(`hist.timeline` §8). It was not a crop failure. It was a *supply* collapse — the
fertiliser trade seized, and the harvests that depended on it failed a season
later, on a planet whose institutions had no capacity to act together.

Everything in this chapter follows from that. Elysian food security is designed
around the assumption that **the failure will be a systems failure, not a weather
failure**, and that weather will merely be what exposes it.

## 2. Reserves

The Concord holds **14 months of planetary calorie consumption** in reserve,
across three tiers.

| Tier | Holding | Held as |
|---|---|---|
| **Concord strategic reserve** | 8 months | Grain, pulses, oils, and fermentation feedstock, in 340 dispersed depots |
| **Regional reserves** | 4 months | Regional staples, held to regional specification |
| **District reserves** | 2 months | Ready-to-distribute food and infant nutrition |

Reserves are **rotated continuously** — stock enters and leaves constantly, so
what is held is current rather than ancient — and are held physically, not as
contracts or futures. The Concord considered financial reserves in EY 254 and
rejected them on the reasoning that a claim on food is not food, and that the
circumstances that would require the reserve are exactly the circumstances in
which claims fail.

**The floor rule.** Reserves may not fall below 8 months except under a declared
emergency, and any draw below 12 months triggers an automatic report to the
Assembly and a published replenishment plan. The reserve has fallen below 12
months four times since EY 200 and below 8 months never.

**Sizing.** The reserve is sized against a specific scenario, published and
periodically re-derived: **three consecutive warm phases of the Amarant
Oscillation** (`planet.climate` §2), causing delayed or failed Elandric monsoons
in successive years, coinciding with a Sirocc drought. That scenario has never
occurred. The Concord holds against it anyway, and the holding cost — roughly
0.6% of GCP annually — is one of the least contested lines in Concord public
finance.

## 3. Is Food a Right?

**No — and this is a real and much-argued gap in the Charter.**

Food does not appear among the sixteen Charter rights
(`gov.constitution` §3). Housing, healthcare, education, and subsistence income
are provision rights; food is not. Its security is delivered indirectly: the
**Civic Income** (`econ.markets` §4) makes food affordable, the reserves make it
available, and price stabilisation keeps the two connected.

The founders' reasoning, recorded in the Convention minutes, was that a right to
food would be a right to a physical thing the state cannot guarantee in all
circumstances, and that a right which fails in a famine is worse than no right at
all — better to guarantee the income and the reserve, both of which are within
the state's power.

The counter-argument has never gone away. Three amendment attempts to add a food
right have been made, in EY 191, EY 302, and EY 377. All three failed, the last
narrowly. Canon records this as **an open constitutional question**, not a
settled design.

## 4. Affordability and Access

| Indicator | Value |
|---|---|
| Median household spend on food | 9.1% of income |
| Lowest income decile spend on food | 16.4% |
| Population experiencing food insecurity in the last year | 0.04% (2.9 million) |
| Population experiencing chronic undernourishment | Effectively zero |

Food is cheap, and the reasons are structural: land value tax does not fall on
production, controlled-environment and fermented food are energy-priced in an
energy-cheap civilization, producer cooperatives take no rentier margin, and the
reserve system removes the price spikes that scarcity would otherwise produce.

**The 2.9 million figure is not zero and canon does not round it away.** It is
concentrated in the same populations as long-term homelessness
(`city.housing` §4) — severe mental illness, dependence, and transitional
disruption — and is a symptom of those conditions rather than of food supply. No
Elysian goes hungry because food is unavailable; some do because they are unwell.

**Price stabilisation** operates through the reserve rather than through
subsidy: the Treasury and Materials portfolio buys into the reserve when staple
prices fall below a band and releases when they rise above it. The band is
published a year ahead, which removes most of the incentive to speculate against
it.

## 5. When It Goes Wrong

The hazard set is inherited from `planet.climate` §8:

| Event | Frequency | Response |
|---|---|---|
| Elandric monsoon failure | ~1 year in 7 | Regional reserve draw; interregional transfer; no planetary action required |
| Sirocc drought | ~1 year in 12 | Aquifer ceilings, desalination transfer, and Alcyon flow-share reallocation |
| Amarant warm phase | ~1 year in 4 | Fishery quota reduction set years ahead on the forecast |
| Compound scenario | Never observed | Concord strategic reserve; emergency powers available |

**The flow-share still governs the Alcyon.** In a drought year, water allocation
in the Alcyon basin reverts to a rotation whose direct ancestor was first attested
around 8,600 BE (`hist.timeline` §3). It has been modified beyond recognition in
its mechanics and is unchanged in its principle: allocation by turn, published in
advance, with the shortfall shared rather than concentrated. Elysian
constitutional lawyers cite it more often than any other precedent, and Elysian
farmers simply use it.

**Forecast lead is the real defence.** The Amarant Oscillation is forecast
reliably 14 months ahead (`planet.climate` §2), which means a warm phase is a
planning event rather than a shock. Quota reductions, planting changes, and
reserve positioning all happen before the phase arrives. Canon is explicit that
this capability — not the reserve itself — is what most distinguishes the modern
Concord from the civilization that lost 210 million people to a supply failure it
did not see coming.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Food is not a Charter right** | Three amendment attempts, the last narrow; an open constitutional question the Concord has not answered |
| **Food insecurity is not zero** | 2.9 million people, concentrated among the severely unwell; a health failure appearing as a food statistic |
| **Reserve cost is invisible until needed** | 0.6% of GCP annually against a scenario never observed; uncontested now, and canon notes such holdings historically erode when a generation passes without using them |
| **Bottom-decile food share** | 16.4% against a 9.1% median; food is cheap for most and not for everyone |
| **Compound scenario untested** | The reserve is sized against a combination that has never happened, so the sizing rests on modelling rather than experience |
| **Regional reserve specification drift** | Regions hold to their own specifications, and three hold stocks that would be poorly matched to a planetary distribution effort |

## 7. Open Threads

- Disaster logistics, distribution, and emergency operations → Phase 12
- Water allocation, desalination, and the Sirocc aquifer → `env.climate`, `energy.grid`
- Civic Income and affordability → `econ.markets`
- Nutrient loops and hypoxia → `agri.production`, `env.conservation`
- Food security and nutrition indicators → Phase 16
