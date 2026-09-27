---
content_hash: sha256:bf4c95c6c6973e48264b8e995af18679777bedaeda1f0d66dc3af1345b56fc42
created: 2026-08-06 00:00:00+00:00
mind_map_priority: high
page_id: concepts/stylized-facts
page_type: concept
related:
- concepts/long-memory
- concepts/mfdfa
- concepts/hurst-exponent
- concepts/copulas
- concepts/limit-order-book
revision_id: 1
schema_version: 2
sources:
- sources/guillaume-1997-stylized-facts-fx
- sources/koukorinis-stylized-facts
- sources/aslam-2020-covid-mfdfa
- sources/stavroyiannis-2017-bitcoin-multifractal
- sources/golub-2014-multiscale-liquidity
- sources/murphy-2006-order-flow-critique
- sources/aldrich-2014-random-walk-high-frequency-trading
- sources/aloud-2016-time-series-analysis-indicators-under-directional
- sources/bakhach-2018-developing-trading-strategies-under-directional-changes
- sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts
- sources/bechler-2017-order-flows-limit-order-book-resiliency
- sources/briola-2024-hlobinformation-persistence-structure-limit-order-books
- sources/chang-2021-epps-effect-under-alternative-sampling-schemes
- sources/chen-2019-studying-regime-change-directional-change
- sources/constantinou-2010-periodicities-fx-markets-intrinsic-time
- sources/corradi-2015-liquidity-crises-different-time-scales
- sources/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear
- sources/eisler-2007-limit-order-book-different-time-scales
- sources/fayyaz-2026-frequency-controlled-comparison-tick-minute-based
- sources/gencay-2004-information-flow-between-volatilities-across-time-scales
- sources/gillemot-2006-there-s-more-volatility-than-volume
- sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery
- sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time
- sources/glattfelder-2024-theory-intrinsic-time-primer
- sources/gontis-2023-discrete-q-exponential-limit-order-cancellation
- sources/gu-2007-empirical-distributions-chinese-stock-returns-different
- sources/mynbaev-2020-full-limit-order-book-price-jump
- sources/onofri-2025-emergence-randomness-temporally-aggregated-financial-tick
- sources/palsma-2019-optimising-directional-changes-trading-strategies-different
- sources/rayment-2023-high-frequency-trading-deep-reinforcement-learning
- sources/rola-2025-boltzmann-price-toward-understanding-fair-price
- sources/shi-2021-limit-order-book-recreation-model-lobrm
- sources/shternshis-2023-price-predictability-ultra-high-frequency-entropy
- sources/silva-2005-applications-physics-finance-economics-returns-trading
- sources/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate
- sources/sjogren-2021-general-compound-hawkes-processes-mid-price
- sources/tao-2018-directional-change-information-extraction-financial-market
- sources/tsang-2024-nowcasting-directional-change-high-frequency-fx
- sources/turkoglu-2015-natural-time-crash-risk
- sources/ye-2017-developing-sustainable-trading-strategies-directional-changes
tags:
- stylized-facts
- high-frequency-data
- market-microstructure
- long-memory
- multifractality
- econophysics
title: Stylized Facts
updated: '2026-09-27T01:47:00Z'
uuid: cbbc8da1-ba00-51a0-8533-90ccf344c00d
---

<!-- AUTHORED REGION START -->
# Stylized Facts

Empirical regularities that recur across instruments, markets and sample periods, and which any candidate price model is expected to reproduce. Descriptive, not theoretical: they say what the data does, not why.

Used here in the high-frequency sense of [[sources/guillaume-1997-stylized-facts-fx|Guillaume et al. (1997)]] and [[sources/koukorinis-stylized-facts|Koukorinis, Peters & Germano (2022)]].

## The Regularities

Grouped as in Guillaume et al. (1997):

**Distribution of price changes** — heavy tails; non-normality persists at high frequency; aggregation does not quickly restore normality; regular scaling of moments.

**Price formation** — negative first-order autocorrelation from bid-ask bounce; distinct behaviour below ~10–15 minutes.

**Heterogeneous structure** — 24-hour FX market across Tokyo, London, New York; participants differ in horizon, risk profile and location; intra-daily seasonality tracks geography.

**Persistence** — [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]] add long memory in order flow and dependence between arrival rates and price variations, examined with [[concepts/copulas|copulas]]. See [[concepts/long-memory|Long Memory]].

## The Clock Problem

The facts are not invariant to the choice of time scale, so the clock is a modelling decision, not a detail.

| Source | Clock | Claim |
|---|---|---|
| [[sources/guillaume-1997-stylized-facts-fx\|Guillaume et al. (1997)]] | physical / theta / intrinsic | Time-scale choice changes observed properties |
| [[sources/golub-2014-multiscale-liquidity\|Golub et al. (2014)]] | intrinsic time, directional changes | For Brownian motion, expected overshoot equals threshold δ, independent of volatility |
| [[sources/koukorinis-stylized-facts\|Koukorinis et al. (2022)]] | information clock, subordinated processes | Activity-based sampling may yield more stable quantities |

[[sources/murphy-2006-order-flow-critique|Murphy & Izzeldin (2006)]] is the counterweight: returns conditioned on the recentred number of trades are **not** approximately Gaussian, and higher moments of latent information flow cannot be reliably recovered.

## Multifractality as a Measure

Spectrum width from [[concepts/mfdfa|MFDFA]] gives a time-varying proxy for inefficiency; wider means stronger multifractality. See [[concepts/hurst-exponent|Hurst Exponent]].

- **European equity indices, COVID-19** ([[sources/aslam-2020-covid-mfdfa|Aslam et al. 2020]], 5-min, Jan–Mar 2020): Δh from 0.56 (Spain) to 0.68 (Austria).
- **Bitcoin** ([[sources/stavroyiannis-2017-bitcoin-multifractal|Stavroyiannis et al. 2017]], minute-level): Δα > 0.5, h(2) ≈ 0.55; stronger multifractality and higher kurtosis than equities.

## Open Questions

- Which regularities are universal, and which are artefacts of one market's microstructure?
- Does algorithmic trading weaken or strengthen the classical facts?
- Do information clocks stabilise the facts, or merely relabel them?

## See Also

[[concepts/long-memory|Long Memory]] · [[concepts/mfdfa|MFDFA]] · [[concepts/hurst-exponent|Hurst Exponent]] · [[concepts/copulas|Copulas]] · [[concepts/limit-order-book|Limit Order Book]] · [[entities/andreas-koukorinis|Andreas Koukorinis]] · [[entities/gareth-peters|Gareth Peters]]

**Not yet written:** `concepts/volatility-clustering`, `concepts/fat-tails`, `concepts/market-microstructure`, `concepts/heterogeneous-agents`, `concepts/information-clock`, `concepts/intrinsic-time`, `concepts/order-flow`, `concepts/market-efficiency`

<!-- AUTHORED REGION END -->