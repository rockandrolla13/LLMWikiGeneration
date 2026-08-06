---
title: 'A New Approach to Statistical Arbitrage: Strategies Based on Dynamic Factor
  Models of Prices'
page_id: sources/focardi-2016-statistical-arbitrage-dfm
page_type: source
source_path: markdown_output/1-s2.0-S0378426615002824-main.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Sergio M. Focardi
- Frank J. Fabozzi
- Ivan K. Mitov
year: 2016
venue: Journal of Banking & Finance
tags:
- statistical-arbitrage
- dynamic-factor-models
- cointegration
- mean-reversion
- long-short
sources: []
related:
- concepts/statistical-arbitrage
- concepts/dynamic-factor-model
- concepts/cointegration
- concepts/pairs-trading
- concepts/principal-components-analysis
- concepts/mean-reversion
- concepts/diebold-mariano-test
- concepts/fama-french-factors
mind_map_priority: high
schema_version: 2
uuid: bdd455df-a8f7-5212-b3fd-eb8a9b8dcd23
content_hash: sha256:d0e4ac429072d3bb591c3d51238aa9847ace8e743b689849a2c530a001284f73
---

<!-- AUTHORED REGION START -->
# A New Approach to Statistical Arbitrage: Strategies Based on Dynamic Factor Models of Prices

**Authors:** Sergio M. Focardi, Frank J. Fabozzi, Ivan K. Mitov

**Year:** 2016 · **Venue:** Journal of Banking & Finance 65 (2016) 134–155

**Institutions:** Stony Brook University (SUNY) and De Vinci University, Paris;
EDHEC Business School; FinAnalytica Inc.

## Summary

Model log **prices**, not returns. That is the whole argument. A
[[concepts/dynamic-factor-model|dynamic factor model]] fitted to logprices
carries level information that first-differencing throws away, and a return-based
model would need many lagged factors — and so many more parameters — to recover
it. With roughly 200 weekly observations per series, that is a losing trade.

Data is the S&P 500 universe of daily prices from January 1989 to December 2011:
5,799 trading days and 1,127 series that appeared as index constituents at some
point. Backtests are strictly out of sample; the constituent set at each date is
the one known at that date.

## Findings

Price-based long-short portfolios beat return-based ones by a wide margin. The
naive price-based long-short strategy returns 25.22% annualized against 11.37%
for its return-based twin; the two optimized variants reach 27.29% and 29.04%.
Sharpe ratios follow: 1.50 versus 0.42 for the naive pair. The reversal-based
benchmark returns 20.46% at Sharpe 0.71.

The forecast-accuracy gap is significant on its own terms. The
[[concepts/diebold-mariano-test|Diebold-Mariano]] statistic comparing price-based
and return-based mean squared error is 32.24, and 2.23 against the reversals
model. All strategies pass the statistical arbitrage test of Hogan et al. (2004).

The mechanism is [[concepts/cointegration|cointegration]]. After PCA of
logprices, the authors cannot reject the null of a **single** integrated factor —
every other principal component is stationary. One common stochastic trend means
all logprice processes mean-revert around it, and that is what makes relative
returns forecastable.

Against Carhart's four factors, the price-based long-short alphas are positive
and significant in most sub-periods with very low R-squared, and carry
significant *negative* momentum exposure. Return-based strategies instead load on
HML and mostly lack significant alpha.

## Caveats

Turnover is the binding constraint, and the authors say so. The naive
price-based long-short strategy turns over 183% annually against break-even
transaction costs of 0.0014; the return-based one turns over 255% at 0.0004.
Optimization mostly buys turnover reduction rather than return. Long-only
variants lose the crisis protection: they fall in both bear markets, while the
price-based long-short avoided losses in 2007–2008.

## Open Questions

- The universe is deliberately liquid. Does the edge survive outside large-cap US
  equity, where the single-common-trend result may not hold?
- Sample ends 2011. The negative momentum loading suggests this competes with a
  crowded trade.

## See Also

[[concepts/statistical-arbitrage|Statistical Arbitrage]] ·
[[concepts/pairs-trading|Pairs Trading]] ·
[[concepts/mean-reversion|Mean Reversion]] ·
[[concepts/principal-components-analysis|Principal Components Analysis]] ·
[[concepts/factor-models|Factor Models]]

**Not yet written:** `hogan-statistical-arbitrage-test`,
`carhart-four-factor-model`, `expected-tail-loss-optimization`,
`common-stochastic-trend`, `avellaneda-lee-strategy`.
<!-- AUTHORED REGION END -->

