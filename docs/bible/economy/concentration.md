# Concentration and Inequality

**Document ID:** `ind.concentration`
**Status:** Proposed
**Version:** 1.0.0
**Authoritative data:** `data/industry.json`
**Inherits:** `econ.money` (taxation, equalization, Gini), `econ.markets`
(ownership forms, Civic Income), `ind.industry`, `gov.institutions`
(Court of Review), `hist.timeline` (the Integration)

All figures as of **EY 412, Calenth 16**.

---

## 1. Why Structure Rather Than Conduct

Elysian competition law asks a different question from the Earth tradition. It
does not primarily ask whether a large firm has *behaved* badly. It asks whether
any private entity has accumulated enough power that its behaviour matters.

The reasoning is historical. During the Integration (`hist.timeline` §7),
planetary systems became fully coupled while the institutions governing them
stayed weak, and a small number of firms in shipping, fertiliser, and energy
acquired the capacity to make decisions with planetary consequences without
anyone having chosen them to. Several of those decisions contributed directly to
the Phosphorus Famine. None of them were illegal.

The founders' conclusion was that conduct rules arrive too late: by the time a
firm's behaviour is worth prosecuting, its power is already a constitutional
fact. Elysian law therefore limits **structure**, and treats conduct as
secondary.

## 2. The Concentration Regime

Enforcement sits with the **Concentration Board**, a statutory body within the
Treasury and Materials portfolio, with adjudication by a specialist division of
the Court of Review (`law.courts` §1). It is not one of the five Independent
Offices — the Charter fixes those at five — but its decisions are appealable only
to the court, not to the Executive Board.

**Thresholds.**

| Share of a relevant market | Consequence |
|---|---|
| Above 20% | Mandatory registration and annual reporting |
| Above 30% | **Reversed burden**: the firm must justify its continued scale every 5 years |
| Above 45% | Structural remedy presumed; the firm must divest unless it rebuts the presumption |

The reversed burden at 30% is the distinctive move. A firm above the threshold
does not defend itself against an accusation; it makes an affirmative case, in
public, that its scale produces benefits that separation would destroy. Firms do
sometimes win — 34 have successfully rebutted since EY 300, mostly in
capital-intensive network industries — but they win by argument rather than by
the regulator's failure to prove anything.

**Absolute prohibitions**, which no justification can overcome:

- Acquiring an actual or potential competitor above the 20% threshold.
- Interlocking directorates between firms in the same or adjacent markets.
- Exclusive control of an essential dataset. Data that a market needs to
  function must be licensed on published, non-discriminatory terms.
- Vertical integration between a natural monopoly and a competitive market that
  depends on it. Grid, rails, ports, payment, and identity are public precisely
  so this question does not arise (`ind.industry` §7).
- Most-favoured-nation and parity clauses in platform contracts.

**Results.** Concentration is genuinely low. The largest private firm in the
Concord accounts for 0.9% of GCP; the top 100 firms together account for 14%.
Median market concentration across registered markets, measured on a
Herfindahl-equivalent, is roughly a third of what the Integration recorded at
comparable industrial output.

## 3. The Cost, Stated Honestly

Canon does not present this as free.

Structural limits mean the Concord forgoes some genuine economies of scale, and
its firms are smaller than optimal in several industries — most clearly in
semiconductor fabrication, large-scale pharmaceutical development, and orbital
launch, where the minimum efficient scale genuinely is enormous. The Concord's
answers have been public enterprise, stewardship foundations, and research
consortia rather than permitting private consolidation, and those answers work
unevenly.

A recurring criticism, made most forcefully by Elandric industrial economists, is
that the Concord has traded away roughly 3–5% of potential output for a
distribution of power it prefers, and that it should say so plainly rather than
claiming the arrangement is costless. Canon records this criticism as **probably
correct on the numbers and unresolved on the tradeoff.**

## 4. Inequality

| Measure | Value |
|---|---|
| Income Gini, pre-tax and transfer | 0.38 |
| Income Gini, post-tax and transfer | **0.21** |
| **Wealth Gini** | **0.44** |
| Top 1% share of wealth | 11% |
| Top 10% share of wealth | 34% |
| Bottom 40% share of wealth | 14% |
| Interregional income ratio, post-transfer | 1.9 |
| Ratio of 90th to 10th percentile income | 3.1 |

**Income inequality is low and the mechanisms are unglamorous.** The Civic Income
sets a floor that is never withdrawn; sectoral bargaining compresses the middle;
progressive income tax and the wealth transfer tax compress the top; fiscal
equalization compresses across Regions; and universal provision of healthcare,
education, and housing means low income does not compound into low everything
else.

Pay ratios are constrained by disclosure rather than by law in the private
sector: every firm above 250 workers publishes the ratio of its highest to its
median compensation, and the figures are widely read. Public enterprises and
cooperatives face hard statutory caps of 8:1 and, in most cooperative statutes,
6:1.

### The wealth problem

**Wealth inequality is markedly higher than income inequality, and it has not
fallen in ninety years.** This is the clearest unsolved distributional problem in
the Concord, and canon states it without softening.

The causes are understood and the remedies are not:

- **Long lives compound.** A person accumulating modestly over a 96-year adult
  life ends with far more than the same person over an Earth-length one, even
  with identical saving rates. Time does most of the work, and the Concord cannot
  legislate against time.
- **Transfer avoidance.** The wealth transfer tax is heavy, but 112-year
  lifespans give enormous scope to structure transfers as lifetime gifts,
  trusts, foundations, and cooperative shares. Yield has drifted down for sixty
  years despite unchanged rates (`econ.money` §7).
- **Housing.** Land value tax captures much of the unearned gain, but not all,
  and long-tenured households in high-demand Districts hold substantial
  appreciated wealth (Phase 10).

Three remedies are actively debated and none commands a majority: a periodic net
wealth tax, a lifetime receipts cap, and a sovereign endowment paying a universal
capital dividend. The Office of Future Generations has intervened in favour of
the third; the Council of Regions has blocked all three at different times.

## 5. What Inequality Does Not Buy

One structural point distinguishes Elysian inequality from the Earth pattern, and
it is why 0.44 wealth Gini produces less social damage than the number suggests.

**Wealth does not purchase advantage in the systems that matter most.** Political
donations are prohibited outright (`gov.institutions` §5). Healthcare and
education are universal and there is no significant private tier. Courts provide
representation free at the point of use. Housing is a right. There is no private
security industry of consequence and no gated development.

A wealthy Elysian has a larger home, better food, more travel, and more
discretion over their time. They do not have a better court, a better school, a
better hospital, or a better legislator. Concord social scientists argue this
decoupling matters more than the Gini coefficient, and that a society should be
measured by what money *cannot* buy as much as by how unequally it is held.

Canon offers this as the Concord's own account of itself rather than as a settled
finding — and notes the obvious rejoinder, made regularly in Concord politics,
that this is exactly what a comfortable society tells itself about its remaining
inequalities.

## 6. Known Weaknesses

| Weakness | Nature |
|---|---|
| **Wealth inequality is not falling** | Flat for ninety years; causes understood, remedies blocked, no majority for any of the three proposals |
| **Scale forgone** | An estimated 3–5% of potential output, most clearly in semiconductors, pharmaceutical development, and launch |
| **Relevant-market definition** | Every structural threshold depends on defining a market, and that definition is contestable, litigated, and quietly political |
| **Data licensing is weak in practice** | Non-discriminatory licensing of essential datasets is required and unevenly enforced; the Concentration Board has lost four of its last seven data cases |
| **Small-firm exemptions accumulate** | Thresholds at 250 workers create a visible clustering of firms at 240–249, a distortion recognised for a century and never fixed |
| **Public enterprise accountability** | Public enterprises escape the concentration regime by construction, and their own accountability is to Districts and Regions of varying capacity |

## 7. Open Threads

- Housing wealth and land policy → Phase 10
- Universal provision as an inequality mechanism → Phases 8, 9
- Sovereign endowment proposals and public wealth → Phase 16
- Data governance and essential datasets → Phase 13
- Inequality, wealth, and mobility indicators → Phase 16
