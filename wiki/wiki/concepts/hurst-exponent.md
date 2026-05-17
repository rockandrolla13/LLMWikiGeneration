---
title: "Hurst Exponent"
page_id: concepts/hurst-exponent
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [time-series, fractal-analysis, long-memory, mean-reversion, persistence]
related: [concepts/mean-reversion, concepts/statistical-arbitrage, concepts/pairs-trading, concepts/long-memory]
sources: [sources/he-2023-hf-pairs-chinese-futures]
---

## Definition

The Hurst exponent (H) is a measure of long-term memory and self-similarity in time series. Named after hydrologist Harold Edwin Hurst, it quantifies the tendency of a series to either regress to the mean (anti-persistence), trend in one direction (persistence), or behave as a random walk.

## Interpretation

| H Value | Behavior | Implication |
|---------|----------|-------------|
| 0 < H < 0.5 | Anti-persistent (mean-reverting) | Series tends to reverse direction |
| H = 0.5 | Random walk | No memory; independent increments |
| 0.5 < H < 1 | Persistent (trending) | Series tends to continue direction |

## Mathematical Formulation

### Rescaled Range (R/S) Analysis

For a time series X of length n:

1. Calculate mean: X_bar = (1/n) * sum(X_i)
2. Create mean-adjusted series: Y_t = X_t - X_bar
3. Cumulative deviation: Z_t = sum(Y_1 to Y_t)
4. Range: R = max(Z) - min(Z)
5. Standard deviation: S = sqrt((1/n) * sum((X_i - X_bar)^2))
6. Rescaled range: R/S

The Hurst exponent satisfies:
```
E[R/S] ~ c * n^H
```

Estimate H via log-log regression:
```
log(R/S) = H * log(n) + log(c)
```

### Detrended Fluctuation Analysis (DFA)

1. Integrate series: Y_t = sum(X_i - X_bar)
2. Divide into boxes of length n
3. Fit trend in each box and detrend
4. Calculate RMS fluctuation F(n)
5. Plot log(F(n)) vs log(n)
6. H is the slope

## Application to Pairs Trading

[[sources/he-2023-hf-pairs-chinese-futures|He et al. (2023)]] use Hurst exponent as a filter:

### Adaptive Fractal Analysis (AFA)

Steps:
1. Calculate Hurst exponent on spread time series
2. If H < 0.5: Spread is mean-reverting (good for pairs trading)
3. If H >= 0.5: Spread is trending or random (avoid)

### Integration with Framework

He et al.'s pairs trading framework:
1. Cointegration test (identify potential pairs)
2. ADF test (confirm stationarity)
3. Kalman filter (estimate hedge ratio)
4. **Hurst exponent** (confirm mean-reverting nature)
5. Trading execution

## Relationship to Mean Reversion

For fractional Brownian motion:
- H < 0.5 implies negative autocorrelation of increments
- Deviations from trend tend to be reversed
- Consistent with [[concepts/mean-reversion|mean reversion]]

### Half-Life Connection

For mean-reverting O-U process:
```
H = 0.5 - kappa / (2 * pi * f_c)
```

Where:
- kappa: Mean reversion speed
- f_c: Characteristic frequency

Lower H -> faster mean reversion -> shorter half-life.

## Estimation Methods

### Classical R/S

- Original method by Hurst
- Sensitive to short-term correlations
- May be biased for small samples

### Modified R/S (Lo, 1991)

- Corrects for short-term dependence
- Uses Andrews' adjustment
- More robust for financial data

### DFA (Peng et al., 1994)

- Handles non-stationarity
- Widely used in physics and finance
- Multiple variants (MF-DFA for multifractal)

### Wavelet-Based

- Uses wavelet decomposition
- Robust to trends and non-stationarity
- Provides time-frequency analysis

## Practical Considerations

### Sample Size

- Large samples needed for reliable estimation
- Minimum ~1000 observations typically recommended
- Finite sample bias exists

### Non-Stationarity

- Classical R/S assumes stationarity
- Use DFA or wavelet methods for non-stationary data
- Beware structural breaks

### Regime Changes

- Hurst exponent may vary over time
- Rolling window estimation
- Regime-switching models

## Financial Applications

### Market Efficiency

- H = 0.5 consistent with efficient markets
- H != 0.5 suggests predictability (inefficiency)

### Asset Selection

- H < 0.5: Good for mean-reversion strategies
- H > 0.5: Good for momentum/trend-following

### Risk Management

- Persistent series (H > 0.5) have fatter tails
- Impact on VaR calculations

## Related Concepts

- [[concepts/mean-reversion|Mean Reversion]] - H < 0.5 case
- [[concepts/long-memory|Long Memory]] - persistent autocorrelation
- [[concepts/pairs-trading|Pairs Trading]] - application
- [[concepts/mfdfa|MF-DFA]] - multifractal extension
