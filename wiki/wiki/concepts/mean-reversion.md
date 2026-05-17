---
title: "Mean Reversion"
page_id: concepts/mean-reversion
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [time-series, statistical-properties, trading-strategies, stochastic-processes]
related: [concepts/statistical-arbitrage, concepts/pairs-trading, concepts/cointegration, concepts/ornstein-uhlenbeck-process, concepts/hurst-exponent]
sources: [sources/triantafyllopoulos-2011-mean-reverting-spreads, sources/moura-2016-pairs-trading-kalman, sources/zhang-2021-pairs-general-ssm]
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
