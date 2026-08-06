---
title: "Combining mean reversion and momentum trading strategies in foreign exchange markets"
page_id: sources/serban-2010-mean-reversion-momentum-fx
page_type: source
source_type: journal-article
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
authors: [Alina F. Serban]
year: 2010
venue: Journal of Banking & Finance
doi: 10.1016/j.jbankfin.2010.05.011
tags: [foreign-exchange, momentum, mean-reversion, uncovered-interest-parity, carry-trade, currency-strategy, cross-sectional-momentum, trading-strategies, sharpe-ratio]
related: [concepts/uncovered-interest-parity, concepts/forward-premium-puzzle, concepts/mean-reversion, concepts/cross-sectional-momentum, concepts/mean-reversion-momentum-combination-strategy, concepts/carry-trade, concepts/moving-average-trading-rules, concepts/half-life-of-adjustment, entities/alina-serban, entities/ronald-balvers, entities/yangru-wu, entities/narasimhan-jegadeesh, entities/sheridan-titman, entities/eugene-fama]
mind_map_priority: high
---

# Combining mean reversion and momentum trading strategies in foreign exchange markets

**Authors:** [[entities/alina-serban|Alina F. Serban]]

**Venue:** Journal of Banking & Finance, 2010

## Summary

This paper ports [[entities/ronald-balvers|Balvers]] and [[entities/yangru-wu|Wu]]'s (2006) parametric [[concepts/mean-reversion-momentum-combination-strategy|combination strategy]] — which jointly models [[concepts/mean-reversion|mean reversion]] and momentum — from equity markets to foreign exchange, applying it to deviations from [[concepts/uncovered-interest-parity|uncovered interest parity]] (UIP) for five developed-country currencies (Canada, UK, Japan, Germany, with the US Dollar as home currency). The starting point is the [[concepts/forward-premium-puzzle|forward premium puzzle]] of [[entities/eugene-fama|Fama]] (1984), which treats UIP deviations as a tradable, stock-return-like series. The combined signal generates abnormal returns of roughly 10–12% annually and Sharpe ratios about 2.5 times higher than the same strategy in equities, and it outperforms traditional FX benchmarks such as the [[concepts/carry-trade|carry trade]] and [[concepts/moving-average-trading-rules|moving-average technical rules]]. The FX contribution is a returns-based (rather than fundamentals-based) alpha whose momentum and mean-reversion parameters are quantitatively close to those estimated in equity markets, with a [[concepts/half-life-of-adjustment|half-life of adjustment]] near 45 months and a stronger momentum coefficient than in stocks.

## Key Claims

1. Applying the [[concepts/cross-sectional-momentum|Jegadeesh–Titman winner-minus-loser strategy]] to cumulative UIP deviations reveals the same qualitative pattern found in equities: winners keep outperforming losers for roughly 9–12 months (momentum), then the two portfolios switch positions over the subsequent 4–5 years (mean reversion).
2. Pooled parameter estimates put the mean-reversion coefficient d at 0.9859 (half-life of 45 months) and the momentum coefficient q at 0.0428 — both statistically significant and close to Balvers–Wu (2006) equity estimates, with the momentum effect stronger in FX (0.043 vs. 0.023 in stocks).
3. Omitting either effect biases the estimates: pure mean reversion inflates the half-life to 124 months, and the momentum and mean-reversion components are negatively correlated (−0.35 in both FX and equity markets).
4. The [[concepts/mean-reversion-momentum-combination-strategy|combination strategy]] (long the highest expected-return currency, short the lowest) yields zero-investment returns of about 10–12% per year for J = 12, and produces higher mean returns than the pure momentum strategy in all 25 (J, K) pairs.
5. Because FX returns have far lower volatility than equities, the FX combination strategy delivers Sharpe ratios roughly 2.5 times higher than the equity version, and outperforms the [[concepts/carry-trade|carry trade]] (Burnside et al. Sharpe ≈ 1.06) and dynamic technical [[concepts/moving-average-trading-rules|trading rules]] (LeBaron Sharpe ≈ 0.67–0.96).
6. Transaction costs (up to 0.2% per developed-country trade) do not materially alter the returns or Sharpe ratios.
7. The parallel between equity and FX return dynamics points to a common source — either shared market inefficiency or an unobserved risk factor — with behavioral overreaction (De Bondt–Thaler) and exchange-rate overshooting (Dornbusch) offered as a possible unifying mechanism.

## Concepts

- [[concepts/uncovered-interest-parity|Uncovered interest parity]] — its deviations are the FX analog of a stock return and the core input signal for the strategy.
- [[concepts/forward-premium-puzzle|Forward premium puzzle]] — Fama's (1984) forward-puzzle motivation for why tradable UIP deviations exist.
- [[concepts/mean-reversion|Mean reversion]] — the long-run stationary component of log FX values, modeled with speed 1−d.
- [[concepts/cross-sectional-momentum|Cross-sectional momentum]] — the non-parametric Jegadeesh–Titman ranking used to confirm momentum-then-reversion in UIP deviations.
- [[concepts/mean-reversion-momentum-combination-strategy|Mean-reversion/momentum combination strategy]] — the parametric Balvers–Wu model ported from equities and the paper's central method.
- [[concepts/carry-trade|FX carry trade]] — a traditional FX benchmark the combination strategy beats on Sharpe ratio.
- [[concepts/moving-average-trading-rules|Moving-average and technical trading rules]] — the incumbent FX momentum-style benchmark the strategy outperforms.
- [[concepts/half-life-of-adjustment|Half-life of adjustment]] — estimated near 45 months under the combined model versus ~124 months for pure mean reversion.

## Related Sources

(Leave empty for now — links added by future ingestions)
