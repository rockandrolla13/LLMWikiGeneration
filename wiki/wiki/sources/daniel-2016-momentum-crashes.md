---
title: Momentum crashes
page_id: sources/daniel-2016-momentum-crashes
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Kent Daniel
- Tobias J. Moskowitz
year: 2016
venue: Journal of Financial Economics 122, 221-247
tags:
- momentum
- crash-risk
- conditional-beta
- volatility-scaling
- dynamic-strategy
sources: []
related:
- concepts/cross-sectional-momentum
- concepts/momentum-trend-following
- concepts/volatility-targeting
- concepts/fama-french-factors
mind_map_priority: high
schema_version: 2
uuid: 54b24e4c-1dbf-5ef5-80e2-6d78ef58e095
content_hash: sha256:d5fe06e94e99139ffe8c11c1022b707223051b39021198e643c53f9b8167bc4a
---

<!-- AUTHORED REGION START -->
# Momentum Crashes

**Authors:** Kent Daniel, Tobias J. Moskowitz

**Year:** 2016 · **Venue:** Journal of Financial Economics 122, 221–247

**Institutions:** Columbia Business School; Yale SOM; NBER

## Summary

Momentum earns high average returns but is punctuated by rare, persistent crashes — and those crashes are **partly forecastable**. They occur in panic states: after market declines, when ex ante volatility is high, and contemporaneously with market rebounds. Scaling momentum by forecasts of its own conditional mean and variance roughly doubles its Sharpe ratio.

## Sample

US common stocks from CRSP (NYSE, Amex, Nasdaq), 1927:01–2013:03, value-weighted deciles on the t−12 to t−2 return, rebalanced monthly. Robustness runs cover four equity markets (US, Europe, Japan, UK) and five asset classes (equity indices, commodities, fixed income, currencies, equities).

## Findings

Over the full sample the winner decile earns 15.3% excess per year and the loser decile −2.5%; WML has a Sharpe ratio of 0.71 against 0.40 for the market, an unconditional beta of −0.58 and a CAPM alpha of 22.3% per year (t = 8.5).

The two worst momentum months are July and August 1932, when the loser decile returned 232% against 32% for winners. From March to May 2009 losers rose 163% and winners 8%.

The mechanism is conditional beta. After major market declines, loser-decile betas rise above 3 while winner betas fall below 0.5. In bear markets the momentum portfolio's up-market beta exceeds its down-market beta, so momentum in bear markets behaves like a **written call option on the market**. Most of the asymmetry comes from the losers.

Hedging the strategy's time-varying exposure to market variance (via VIX-imputed variance swap returns) does not restore bear-market profitability, so volatility risk exposure is not the explanation.

The implementable dynamic strategy lifts the annualized Sharpe ratio from 0.682 (static WML) to 1.041 (constant-volatility scaling) to 1.194 (out-of-sample dynamic) over 1934:01–2013:03. Combined across all markets and asset classes it reaches 1.19.

## Why It Matters / Caveats

The paper reframes momentum's tail as a conditional-beta phenomenon rather than a pure mispricing artefact, and it kills the Grundy–Martin hedging result by showing their betas are forward-looking. The authors themselves flag the data-mining hazard: crashes are few, so the dynamic strategy is fitted on a small number of extreme episodes.

## Open Questions

- The option-like loser payoff is explicable via [[concepts/risk-vs-mispricing|leverage in equity capital structure]], but the same convexity appears in commodity, currency and fixed income momentum where that story does not apply. What generates it there?
- Does the dynamic weighting survive realistic turnover and financing costs in the leveraged states?

## See Also

[[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/momentum-trend-following|Momentum and Trend Following]] · [[concepts/volatility-targeting|Volatility Targeting]] · [[concepts/fama-french-factors|Fama-French Factors]]

[[sources/blitz-2011-residual-momentum|Blitz, Huij & Martens (2011)]] attack the same time-varying exposures by ranking on residual returns instead of scaling. [[sources/li-2025-systematic-momentum|Li, Yuan & Zhou (2025)]] cite this paper for momentum's crash risk and claim their systematic momentum avoids it.

**Not yet written:** `concepts/momentum-crash-risk`, `entities/kent-daniel`, `entities/tobias-moskowitz`

<!-- AUTHORED REGION END -->
