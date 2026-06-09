---
created: 2026-04-26 03:00:00+00:00
page_id: concepts/mean-reversion
page_type: concept
related:
- concepts/alpha-correlation-turnover
- concepts/arima-garch-models
- concepts/behavioral-finance
- concepts/cointegration
- concepts/contrarian-market-timing
- concepts/credit-relative-value
- concepts/credit-spread-curve
- concepts/cross-asset-rotation
- concepts/earnings-growth-persistence
- concepts/ewmac-carry-trading-rules
- concepts/expectations-hypothesis-term-structure
- concepts/fast-mean-reversion
- concepts/great-moderation
- concepts/hidden-markov-models
- concepts/hurst-exponent
- concepts/law-of-active-management
- concepts/market-integration-concordance-measure
- concepts/market-timing
- concepts/mean-reversion-in-profitability
- concepts/ornstein-uhlenbeck-process
- concepts/pairs-trading
- concepts/regime-switching-models
- concepts/regression-to-the-mean
- concepts/relative-value-spread-trading
- concepts/statistical-arbitrage
- concepts/strategy-robustness
- concepts/style-premia
- concepts/term-structure-risk-premium
- concepts/trend-following
- concepts/value-premium
revision_id: 3
sources:
- sources/moura-2016-pairs-trading-kalman
- sources/ms-2011-03-28-high-grade-mid-cycle
- sources/ms-2018-06-05-emfx-risk-premia-two-factor
- sources/ms-2019-02-03-self-catalysing-dollar-weakness
- sources/ms-2019-02-17-goldilocks-whiplash
- sources/ms-2019-02-28-selling-the-rally
- sources/ms-2019-03-03-an-easing-trio
- sources/ms-2020-03-19-volatility-peaks-before-markets-trough
- sources/ms-2020-04-01-what-do-recoveries-look-like
- sources/ms-2022-11-04-end-of-trends
- sources/triantafyllopoulos-2011-mean-reverting-spreads
- sources/zhang-2021-pairs-general-ssm
tags:
- time-series
- statistical-properties
- trading-strategies
- stochastic-processes
title: Mean Reversion
updated: '2026-06-09T12:00:00Z'
---

## Definition

Mean reversion is the statistical tendency of a time series to return to its long-run average level after deviations. A mean-reverting process exhibits negative autocorrelation of changes: large positive movements tend to be followed by negative movements, and vice versa.

## Mathematical Characterization

### Ornstein-Uhlenbeck Process

The canonical continuous-time mean-reverting process:
```
dX_t = kappa * (mu - X_t) * dt + sigma * dW_t
```

Where:
- kappa > 0: Speed of mean reversion
- mu: Long-term mean
- sigma: Volatility
- W_t: Wiener process (Brownian motion)

### Discrete-Time AR(1)

Discrete version with mean reversion:
```
X_t = c + phi * X_{t-1} + epsilon_t
```

Mean reversion requires |phi| < 1, with:
- Long-run mean: mu = c / (1 - phi)
- Speed of reversion: kappa = -ln(phi)

## Half-Life

The expected time to revert halfway to the mean:
```
H = ln(2) / kappa = -ln(2) / ln(phi)
```

### Example Half-Lives

| phi | kappa | Half-Life |
|-----|-------|-----------|
| 0.95 | 0.051 | 13.5 days |
| 0.90 | 0.105 | 6.6 days |
| 0.80 | 0.223 | 3.1 days |
| 0.50 | 0.693 | 1.0 day |

## Testing for Mean Reversion

### ADF Test (Augmented Dickey-Fuller)
Tests null hypothesis of unit root (no mean reversion):
- Reject null: Evidence of mean reversion
- Fail to reject: May be random walk

### [[concepts/hurst-exponent|Hurst Exponent]]
Measures long-memory characteristics:
- H < 0.5: Mean-reverting (anti-persistent)
- H = 0.5: Random walk
- H > 0.5: Trending (persistent)

### Variance Ratio Test
Compares variance at different horizons:
- Ratio < 1: Mean reversion
- Ratio = 1: Random walk
- Ratio > 1: Trending

## Mean Reversion in Finance

### Asset Classes

| Asset | Typical Behavior | Mean Reversion? |
|-------|-----------------|-----------------|
| Stock prices | Random walk | Generally no |
| Spreads (pairs) | Mean-reverting | Yes |
| Interest rates | Mean-reverting | Yes (to central rate) |
| Volatility | Mean-reverting | Yes (VIX tends to fall after spikes) |
| Valuations (P/E) | Mean-reverting | Yes (long-run) |

### Trading Implications

Mean reversion enables [[concepts/statistical-arbitrage|statistical arbitrage]]:
1. Identify mean-reverting series (spread, ratio)
2. Enter position when deviation is extreme
3. Profit when series reverts to mean

## State-Space Modeling

[[concepts/kalman-filter|Kalman filter]] approaches to mean reversion:

### Elliott et al. (2005) Model
Hidden mean-reverting state observed with noise:
```
x_t = a + (1-b)*x_{t-1} + C*eta_t  (state equation)
S_t = x_t + D*epsilon_t            (observation equation)
```

Mean reversion requires 0 < b < 2 (or |1-b| < 1).

### Time-Varying Mean Reversion
[[sources/triantafyllopoulos-2011-mean-reverting-spreads|Triantafyllopoulos & Montana (2011)]]:
- Allow parameters a, b to vary over time
- Bayesian estimation provides uncertainty quantification
- Detect when mean reversion may be breaking down

### Conditional Probability Approach
[[sources/moura-2016-pairs-trading-kalman|de Moura et al. (2016)]]:
- Calculate P(spread crosses mean within k periods)
- Enter position when probability exceeds threshold
- More sophisticated than simple threshold rules

## Non-Linear Mean Reversion

[[sources/zhang-2021-pairs-general-ssm|Zhang (2021)]] considers:

### Quadratic Model
```
X_t = theta_1 + theta_2*X_{t-1} + theta_3*X_{t-1}^2 + eta_t
```

### Ait-Sahalia Model
```
X_t = theta_1 + theta_2/X_{t-1} + theta_3*X_{t-1} + theta_4*X_{t-1}^2 + eta_t
```

Non-linear models can capture:
- Asymmetric reversion speeds
- Regime-dependent dynamics
- Boundary behavior

## Practical Considerations

### False Mean Reversion
- Small samples may show apparent mean reversion
- Structural breaks can create false signals
- Survivorship bias in pair selection

### Parameter Stability
- Mean reversion parameters may change over time
- Adaptive estimation (Kalman filter) helps
- Monitor for regime changes

## Related Concepts

- [[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck Process]] - continuous-time model
- [[concepts/cointegration|Cointegration]] - long-run equilibrium
- [[concepts/hurst-exponent|Hurst Exponent]] - alternative test
- [[concepts/stationarity|Stationarity]] - statistical property

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/alpha-correlation-turnover|alpha-correlation-turnover]]
- [[concepts/arima-garch-models|arima-garch-models]]
- [[concepts/contrarian-market-timing|contrarian-market-timing]]
- [[concepts/credit-relative-value|credit-relative-value]]
- [[concepts/earnings-growth-persistence|earnings-growth-persistence]]
- [[concepts/ewmac-carry-trading-rules|ewmac-carry-trading-rules]]
- [[concepts/expectations-hypothesis-term-structure|expectations-hypothesis-term-structure]]
- [[concepts/fast-mean-reversion|fast-mean-reversion]]
- [[concepts/hidden-markov-models|hidden-markov-models]]
- [[concepts/law-of-active-management|law-of-active-management]]
- [[concepts/market-integration-concordance-measure|market-integration-concordance-measure]]
- [[concepts/mean-reversion-in-profitability|mean-reversion-in-profitability]]
- [[concepts/pairs-trading|pairs-trading]]
- [[concepts/regression-to-the-mean|regression-to-the-mean]]
- [[concepts/relative-value-spread-trading|relative-value-spread-trading]]
- [[concepts/strategy-robustness|strategy-robustness]]
- [[concepts/style-premia|style-premia]]
- [[concepts/term-structure-risk-premium|term-structure-risk-premium]]
- [[concepts/value-premium|value-premium]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2011-03-28-high-grade-mid-cycle]], [[sources/ms-2018-06-05-emfx-risk-premia-two-factor]], [[sources/ms-2019-02-03-self-catalysing-dollar-weakness]], [[sources/ms-2019-02-17-goldilocks-whiplash]], [[sources/ms-2019-02-28-selling-the-rally]], [[sources/ms-2019-03-03-an-easing-trio]], [[sources/ms-2020-03-19-volatility-peaks-before-markets-trough]], [[sources/ms-2020-04-01-what-do-recoveries-look-like]], [[sources/ms-2022-11-04-end-of-trends]]