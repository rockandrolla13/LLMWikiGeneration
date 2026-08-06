---
title: Yield Curve Forecasting
page_id: concepts/yield-curve-forecasting
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- yield-curve
- forecasting
- term-structure
- machine-learning
- state-space-models
sources:
- sources/omrane-2017-yield-curve-forecasting
- sources/nunes-2022-ml-fixed-income
- sources/krishnan-2007-credit-spread-forecast
related:
- concepts/yield-curve
- concepts/nelson-siegel-model
- concepts/credit-spread-forecasting
mind_map_priority: medium
schema_version: 2
uuid: 91425cfd-c844-5630-a272-40f5e024e74e
content_hash: sha256:e5996dcb33816eedbd2d39cc00e06e00c7dc42c09f1d7badd4d14b4608475c77
---

<!-- AUTHORED REGION START -->
# Yield Curve Forecasting

Predicting future yields, almost always by forecasting the three factors of the curve rather than each maturity separately. The benchmark to beat is the random walk, and at short horizons it is hard to beat.

## The State-Space Route

[[sources/omrane-2017-yield-curve-forecasting|Ben Omrane et al. (2017)]] put the Nelson-Siegel factors in a state-space model — factors follow a VAR-type state equation, the measurement equation carries the Nelson-Siegel loadings — and estimate everything, including the decay parameter λ, by maximum likelihood with a Kalman filter. Freeing λ instead of fixing it is the paper's innovation.

The horizon result is the useful part:

| Horizon | Dynamic factor model | Diebold-Li | Random walk |
|---|---|---|---|
| 1 month | Moderate | Good | **Best** |
| 6 months | Good | Moderate | Poor |
| 12 months | **Best** | Poor | Poor |

The model wins at six and twelve months and loses at one, which the authors attribute to the Kalman filter trading robustness for efficiency. Economic shocks cause breaks the filter adapts to slowly, so short-maturity, short-horizon forecasts are the least reliable.

## The Machine Learning Route

[[sources/nunes-2022-ml-fixed-income|Nunes (2022)]] compares multivariate linear regression against MLPs across five horizons and finds MLPs with well-chosen features do best; feature selection matters, and different features matter for different targets. A dynamic LSTM for the 10-year yield gives lower error with higher confidence than static MLPs, and the thesis adds **LSTM-LagLasso** to interpret which exogenous variables drive the internal gating signals — hidden units switch across temporal regimes.

## What Does Not Help

[[sources/krishnan-2007-credit-spread-forecast|Krishnan et al. (2007)]], forecasting credit spreads rather than yields, report a sufficiency result worth carrying over: the current credit-spread and riskless-yield curves impound essentially all relevant information, and adding macro, market or firm variables gives no improvement. Their credit-spread factor model beat the spot benchmark for over 80% of firms, with average absolute error of 31bp on six-month-ahead five-year spreads.

## See Also

[[concepts/yield-curve|Yield Curve]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]] · [[concepts/credit-spread-forecasting|Credit Spread Forecasting]] · [[concepts/kalman-filter|Kalman Filter]] · [[concepts/state-space-models|State-Space Models]] · [[concepts/term-structure-risk-premium|Term Structure Risk Premium]]

**Not yet written:** `concepts/diebold-li-model`, `concepts/dynamic-factor-model`, `concepts/lstm`, `concepts/random-walk-benchmark`

<!-- AUTHORED REGION END -->
