---
authors:
- Fan Yu
content_hash: sha256:28bcb4edd31f2ea2b0877e6c4a02024615a45da332521d81df4f399750828d00
created: '2026-10-05T15:52:32Z'
page_id: sources/yu-2006-how-profitable-capital-structure-arbitrage
page_type: source
publication_date: '2006'
publication_venue: Financial Analysts Journal 62(5)
related:
- concepts/capital-structure-arbitrage
- concepts/structural-models
- concepts/merton-model
- concepts/credit-default-swaps
- concepts/credit-default-swap-spread
- concepts/statistical-arbitrage
- concepts/limits-to-arbitrage
- concepts/credit-hedge-ratios-equity-options
- concepts/survival-probability
- concepts/relative-value-spread-trading
- concepts/creditgrades-model
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/avino-2024-hedging-credit-equity-options
- sources/dafonseca-2020-cds-equity-volatility-comovement
- sources/finger-2002-creditgrades-technical-document
- analyses/capital-structure-arbitrage-literature-review
- entities/fan-yu
- entities/markit-group
revision_id: 1
schema_version: 2
source_hash: sha256:74cf176f528004baf22f497c2b1f10e798cdf248ce29eaaebceee2530104fc88
source_path: markdown_output/yu-2006-how-profitable-capital-structure-arbitrage.md
source_type: paper
sources: []
tags:
- capital-structure-arbitrage
- credit-default-swaps
- creditgrades
- structural-models
- convergence-trading
- equity-hedge
- hedge-fund-returns
- markit
title: How Profitable Is Capital Structure Arbitrage?
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 7bc02198-acfb-5bcd-b2a2-a0ff79b1180a
version_read: Working paper dated 3 June 2005 (first draft 30 September 2004), not
  the published FAJ version
year: 2006
---

<!-- AUTHORED REGION START -->
# How Profitable Is Capital Structure Arbitrage?

**Authors:** Fan Yu · **Year:** 2006 · **Venue:** Financial Analysts Journal 62(5)
**Version read:** Working paper dated 3 June 2005 (first draft 30 September 2004), not the published FAJ version

## Summary

This paper asks whether capital structure arbitrage makes money when it is run in a disciplined way across many names. The trade compares a firm's market CDS spread with a spread implied by its equity price through a structural model. When the two diverge by enough, the trader takes a CDS position and hedges it with stock, betting that the gap will close.

Yu uses the CreditGrades model as the spread engine. He fixes the bond recovery and backs out the global recovery from the first ten days of each name's data, then holds the model fixed. Trades open when the market spread is a set fraction above or below the model spread. They close when the gap closes, when a maximum holding period ends, or when the trade's capital is wiped out.

Single trades are risky. The worst case is selling protection just before spreads blow out. The stock hedge then does almost nothing, because CDS spreads and share prices barely move together day to day. Names fall into three groups: spikes that converge (good), spreads that keep rising toward distress (bad), and slow drifts that look like model error (also bad).

At the portfolio level the picture is better. An equal-weighted index of all open trades earns Sharpe ratios similar to fixed-income arbitrage hedge fund benchmarks. Its monthly returns do not load on equity or bond market factors. The result holds when the CDS bid/ask cost is doubled, when CDS positions are valued without the model, and when the hedge is rebalanced daily.

## Data

- CDS: Markit daily composite 5-year spreads, senior unsecured, North American obligors, modified restructuring clause, USD, 2001-2004.
- Filters: longest run of more than 252 daily quotes no more than 14 calendar days apart, with matching equity and balance-sheet data; financials and utilities excluded.
- Final sample: 135,759 daily spreads on 261 obligors (210 investment grade, 51 speculative grade including two unrated).
- Equity: CRSP daily prices; balance sheet: Compustat quarterly, lagged one month after quarter end.
- Rates: 5-year constant-maturity Treasury and 3-month T-bill from Datastream.
- Factors: S&P Industrial index, Lehman Baa and Ba intermediate indices, CSFB/Tremont Fixed Income Arbitrage index (Datastream), monthly.

## Method

Model spread $c_t^*$ comes from CreditGrades. Firm value per share follows driftless GBM $dV_t/V_t = \sigma\,dW_t$. Default is first passage to the barrier $LD = \bar L D e^{\lambda Z - \lambda^2/2}$, with $Z$ standard normal and $\lambda^2 = \mathrm{var}(\ln L)$. Inputs: debt per share $D$ = total liabilities / shares outstanding, $\sigma_S$ = 1,000-day historical equity volatility, $r$ = 5-year CMT yield, $\lambda = 0.3$, bond recovery $R = 0.5$. Asset volatility uses $\sigma = \sigma_S\,S/(S + \bar L D)$. $\bar L$ is fitted per name by least squares on the first 10 daily spreads.

Trading rule: enter when $c_t > (1+\alpha)c_t^*$ (sell CDS, short $\delta_t$ shares) or $c_t^* > (1+\alpha)c_t$ (buy CDS, buy shares), with trigger $\alpha \in \{0.5, 1, 2\}$. The hedge ratio is the model equity delta $\delta = \partial\pi/\partial S$ of the CDS contract value, fixed at entry (static hedge). Exit on convergence ($c_t = c_t^*$), at a maximum holding period (30 or 180 days), or when trade value turns negative (limited liability). Initial capital of 0.1 or 0.5 per 1 of CDS notional. Existing CDS positions are valued as a survival-contingent annuity using CreditGrades survival probabilities, approximating $c(t,T)$ by $c(t,t+T)$. A 5% proportional CDS bid/ask cost applies; stock trading costs are ignored.

Portfolio: equal-weighted daily excess returns of all open trades, compounded to monthly. Tests: Hogan-Jarrow-Teo-Warachka constrained-mean statistical arbitrage test, and regressions of monthly returns on equity, IG bond, HY bond and fixed-income-arbitrage index returns. Robustness: Duffie-Singleton risk-adjusted discounting for CDS value, daily rebalanced hedge, 10% bid/ask.

## Key Findings

1. After filtering, the study covers 135,759 daily five-year CDS quotes on 261 North American industrial obligors from 2001 to 2004.
2. Daily changes in CDS spreads and share prices are only weakly correlated. The correlation is mostly negative and grows in size as rating falls, from about 0.01 for AAA names to -0.23 for CCC names. This is why the equity hedge does little.
3. In the Altria case, the Moody's downgrade pushed the market spread from 210bp to 299bp in one day, while the model spread rose only 11bp. A short-CDS trade opened at 299bp against a 168bp model spread was wiped out four days later when the market spread reached 529bp.
4. Across all obligors, single trades carry large tail losses (minimum holding-period return of -88.71% for investment grade). Speculative-grade trades with a 30-day horizon lose money on average (-0.52% at the lowest trigger). Longer holding periods produce more converging trades and higher mean returns.
5. The equal-weighted monthly index earns annualised Sharpe ratios of about 0.39 to 0.80 for investment-grade names and about 0.74 to 0.76 for speculative-grade names. This is in line with fixed-income arbitrage hedge fund benchmarks.
6. Monthly index returns show no significant exposure to equity, investment-grade bond, high-yield bond or fixed-income-arbitrage index returns. Regression intercepts stay close to the raw mean returns. None of the strategies passes the statistical-arbitrage test at conventional levels with 48 months of data.
7. Doubling the CDS bid/ask cost to 10% cuts mean monthly excess returns by about 10 to 20bp but does not remove them. Rebalancing the equity hedge daily does not improve the risk-return trade-off.

## Limitations

- Only one model (CreditGrades), calibrated once on the first 10 observations, with historical rather than option-implied volatility and quarterly balance-sheet debt; the author lists implied volatility, closer capital-structure monitoring and alternative models as untested improvements.
- CDS mark-to-market uses model survival probabilities and approximates aged contracts by new 5-year quotes; there is no secondary-market price data.
- Bid/ask is assumed (5% proportional), not observed; stock trading and borrow costs are ignored.
- Short sample (48 months, 2001-2004), dominated by investment-grade names, so the statistical-arbitrage test has little power.
- The equal-weighted 'portfolio of hedge funds' aggregation ignores capital constraints and correlated margin calls across trades.

## Questions Raised

- Would calibrating the structural model to option-implied volatility cut the false signals that come from stale historical volatility?
- Can the 'diverging' names (spreads rising toward distress) be screened out before entry, for example with a distress or liquidity filter?
- How do returns change if the trade uses cash bonds instead of CDS, given bond illiquidity and the CDS-bond basis?
- Do the attractive portfolio Sharpe ratios survive in later samples that include 2008, when divergences became systemic?

## Relevance to Bond Signals

The gap between a market credit spread and an equity-implied structural spread is a candidate cross-sectional relative-value signal for corporate bonds. The paper shows the signal is noisy for single names and dangerous when spreads widen toward distress. It works only diversified and with a large entry threshold, so it is best used with a distress filter.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/statistical-arbitrage|Statistical Arbitrage]]
- [[concepts/limits-to-arbitrage|Limits to Arbitrage]]
- [[concepts/credit-hedge-ratios-equity-options|Credit Hedge Ratios with Equity Options]]
- [[concepts/survival-probability|Survival Probability]]
- [[concepts/relative-value-spread-trading|Relative Value / Spread Trading]]
- [[concepts/creditgrades-model|CreditGrades Model]]

## Entities

- [[entities/fan-yu|Fan Yu]]
- [[entities/markit-group|Markit Group]]

## Related Sources

- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/avino-2024-hedging-credit-equity-options|Contingent Claims and Hedging of Credit Risk with Equity Options]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
- [[sources/finger-2002-creditgrades-technical-document|CreditGrades Technical Document]]
<!-- AUTHORED REGION END -->