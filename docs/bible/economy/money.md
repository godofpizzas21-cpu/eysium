# Money, Banking, and Public Finance

**Document ID:** `econ.money`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/economy.json`
**Inherits:** `gov.constitution` (currency as an enumerated power; right 11
subsistence; ecological limits), `gov.regions` (most taxation is regional),
`gov.institutions` (Nominating Assembly, Office of Future Generations),
`planet.resources` (Constrained List, retained carbon), `cult.foundations`
(redundancy, stewardship, restraint)

All figures as of **EY 412, Calenth 16**.

---

## 1. The Dram

The currency of the Concord is the **dram** (symbol **đ**), divided into 100
**minims**. The name descends from a Thalassic trade weight used across the Long
Reach; like Concordial itself (`cult.languages` §3), it was adopted because it
belonged to no region's imperial past.

| Indicator | Value |
|---|---|
| Gross Concord Product | đ1.03 quadrillion |
| GCP per capita | đ142,000 |
| Inflation target | 1.5% ± 1.0 |
| Current inflation | 1.4% |

**The dram is issued in two forms, deliberately.** Digital dram are accounts at
the Monetary Authority; physical dram are notes and coin. Physical currency is
constitutionally protected and cannot be withdrawn: it works when the network
does not, it leaves no record, and it is usable by anyone. Notes are printed
and distributed even though only 3.1% of transactions use them, and the cost is
treated as an insurance premium rather than a subsidy.

This is the civic virtue of redundancy (`cult.foundations` §1) applied to money.
An economy with one payment system has a single point of failure, which on
Elysium is a moral objection as much as an engineering one.

## 2. The Monetary Authority

The **Concord Monetary Authority** issues currency and sets monetary policy. It
is not one of the five Independent Offices, but it is built on the same pattern:
its nine-member Board is appointed by the Nominating Assembly
(`gov.institutions` §6) for single non-renewable 9-year terms, its funding comes
from its own operations, and it is audited by the Audit Service like everything
else.

**Its mandate has three limbs, in no fixed priority:**

1. Price stability, 1.5% ± 1.0
2. Full employment
3. Financial system resilience

The absence of a lexical ordering is deliberate and contested. The Board must
publish, with every decision, which limb it prioritised and why — the reasons
requirement (`gov.constitution` §2.4) applied to monetary policy. Minority
positions are published in full, and Board members are frequently outvoted in
public.

Critics argue an unordered mandate is no mandate, and that it grants the Board
discretion a democracy should not delegate. The Concord's answer is that a
single-target central bank simply hides the tradeoff rather than resolving it,
and that a published tradeoff is more accountable than a concealed one. The
argument recurs every decade and has never been settled.

## 3. Narrow Banking

The most distinctive feature of Elysian finance is that **deposits are not
claims on banks.**

Every resident and firm holds a **settlement account at the Monetary Authority**
directly. Money in a settlement account is central bank money: it cannot fail,
cannot be lent out, and is not a bank's liability. Payment runs on public
infrastructure (`gov.administration` §6), free at the point of use, with source
published.

Banks exist and lend, but they are **pure intermediaries**. A bank funds its
lending by issuing term liabilities — bonds, certificates, and equity — bought
by people who understand they are investors and can lose money. No bank creates
deposits, and no bank failure destroys anyone's means of payment.

The consequences are the point:

- **Bank runs are structurally impossible** on the payment system, because the
  payment system is not what banks hold.
- **No deposit insurance is needed**, and therefore no implicit public guarantee
  of private lending, and therefore far less of the moral hazard that
  characterised pre-founding finance.
- **A bank can be allowed to fail.** Resolution is an ordinary insolvency, and
  fourteen banks have failed since EY 1 without a public rescue.

The system dates from the Consolidation and was a direct response to the
financial collapses of the Integration, in which the failure of lending
institutions destroyed the payment system that ordinary people depended on and
forced rescues that were, in the founders' phrase, *"the socialisation of a
gamble already lost."*

**The cost, stated plainly:** credit is somewhat scarcer and somewhat dearer
than it would be under fractional banking. Elysian firms complain about this
constantly. Concord monetary economists broadly agree the complaint is correct
and consider the price worth paying; a substantial minority does not.

## 4. Taxation

Taxation is **overwhelmingly regional** — the Concord did not take it, because
Article 3 gives it only what is enumerated. Regions and Districts raise 78% of
all revenue.

| Tax | Tier | Share of revenue |
|---|---|---|
| **Land value tax** | Regional | 24% |
| Income tax (progressive) | Regional | 26% |
| **Wealth transfer tax** | Regional, Concord floor | 14% |
| Consumption and materials taxes | Regional | 13% |
| **Constrained List extraction levy** | Concord | 9% |
| Corporate surplus tax | Regional | 8% |
| Commons and orbital use charges | Concord | 4% |
| Other | Mixed | 2% |

Total tax take: **41% of Gross Concord Product**.

Three of these deserve explanation because they follow from earlier canon rather
than from Earth practice.

**Land value tax is the largest single regional tax**, and it exists because of
the stewardship obligation (`law.substantive` §5). Land on Elysium is held
subject to duties and cannot be degraded; taxing its unimproved value follows
naturally from a legal tradition in which the Alcyon flow-share allocated water
and never sold it. It is also, conveniently, the tax that is hardest to avoid
and least distorting of effort — a point Elysian textbooks make second, not
first.

**The wealth transfer tax is unusually heavy**, and demography is the reason.
With median lifespans of 112 Elysian years and four living generations ordinary
(`hist.demographics` §4), an untaxed inheritance regime would compound dynastic
fortunes across overlapping lifetimes at a rate no Earth society ever faced. The
tax applies to *receipts* rather than estates, is levied on the recipient's
lifetime cumulative total, and is steeply progressive above a generous
threshold. Ordinary family transfers are untouched; the top band is 71%.

**The Constrained List extraction levy** prices scarcity directly. Materials with
a reserve horizon under 150 years (`planet.resources` §9) — beryllium,
platinum-group metals, indium/gallium/germanium — carry an extraction levy that
rises automatically as the horizon shortens. The levy is not a revenue measure
in intent; it is the price signal that funds substitution research and makes
recycling profitable. Recovery rates above 90% across the Concord are largely
its doing.

## 5. Public Finance

Public spending is **43% of GCP**, of which the Concord tier accounts for 22%
and Regions, Districts, and Communes the remaining 78% (`gov.regions` §1).

### Debt and the intergenerational account

The Concord may borrow, but under two constraints:

- **Purpose limitation.** Concord borrowing is permitted only for assets whose
  benefits extend beyond the current generation — infrastructure, research,
  restoration, orbital capacity — and never for current consumption.
- **The intergenerational account.** Every budget publishes a statement of what
  it transfers to, and takes from, Elysians not yet born: debt incurred, assets
  built, resources consumed, ecological capacity used or restored. The Office of
  Future Generations may exercise its suspensive veto against a budget on this
  statement alone, and has done so four times.

Concord debt currently stands at 34% of GCP; regional debt varies from 4% to
61%.

### The discount rate

Elysian public appraisal uses a **pure time preference of zero**.

This follows directly from `cult.foundations` §5: Elysians find the practice of
discounting future welfare simply because it is future to be a moral error, not
merely an economic assumption. Public project appraisal therefore discounts only
for the expected growth in wealth (future Elysians will be richer, so a dram
means less to them) and for genuine risk that the benefit will not materialise.

The practical effect is enormous and is the single most important economic fact
about the Concord. A sea wall protecting a city in 300 years is appraised at
close to its full value. Restoration projects with century-scale payback are
routinely funded. The fusion transition, the CO₂ corridor's 122-year managed
decline, and the Veydran research commons were all appraised under this rule
and none would have passed a conventional discounted test.

The cost is real and canon states it: with near-zero discounting, a great many
projects clear the bar, and the binding constraint becomes real resources and
administrative capacity rather than financial appraisal. Prioritisation is
consequently harder, more political, and more prone to capture by whoever argues
best.

## 6. Fiscal Equalization

Because the Concord may set floors but not ceilings (`gov.constitution` §2.1),
wealthy Regions race ahead. Equalization is the counterweight and the most
politically bitter recurring negotiation in Concord public finance.

The formula transfers from Regions with above-average **fiscal capacity** —
measured by taxable base, not by actual revenue, so a Region cannot gain by
taxing itself lightly — to those below. It equalises capacity to 86% of the
planetary mean, not to 100%, a number renegotiated every eight years and fought
over every time.

| Indicator | Value |
|---|---|
| Transfers as share of GCP | 3.1% |
| Net contributor Regions | 12 |
| Net recipient Regions | 22 |
| Capacity equalisation target | 86% of mean |
| Highest-to-lowest regional income ratio, pre-transfer | 4.1 |
| Post-transfer | 1.9 |

Elandris and Vailmark are the largest net contributors and the loudest
complainants; Highmarch, Austral Shore, and Northreach are structurally
dependent. Canon records the honest position: equalization narrows the gap
substantially and does not close it, and the Concord has never agreed whether
closing it would be desirable.

## 7. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Credit scarcity** | Narrow banking makes credit dearer; firms complain constantly and a substantial minority of economists agree with them |
| **Unordered monetary mandate** | Three limbs with no priority grants the Board discretion critics say a democracy should not delegate |
| **Appraisal permissiveness** | A zero pure time preference lets almost everything clear the bar, shifting prioritisation from analysis to politics |
| **Equalization is a standing grievance** | Renegotiated every eight years; neither contributors nor recipients regard the current settlement as legitimate |
| **Wealth transfer avoidance** | Long lifespans give enormous time to structure transfers; the tax's yield has drifted down for sixty years despite unchanged rates |
| **Regional debt divergence** | Regional debt ranges from 4% to 61% of regional output with no planetary limit, and no agreed answer to what happens if a Region cannot pay |

## 8. Open Threads

- Enterprise, ownership, markets, labour, the Civic Income → `econ.markets` (this phase)
- Industry, automation, anti-monopoly, inequality → Phase 6B
- Energy pricing and the fusion economy → Phase 7
- Off-world economy and orbital resource pricing → `space.infrastructure`
- Economic and inequality indicators → Phase 16
