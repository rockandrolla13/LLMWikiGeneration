---
created: 2026-04-26 03:00:00+00:00
page_id: concepts/cointegration
page_type: concept
related:
- concepts/mean-reversion
- concepts/pairs-trading
- concepts/stationarity
- concepts/statistical-arbitrage
- concepts/vector-error-correction-model
revision_id: 2
sources:
- sources/duasa-2010-predicting-crisis-recovery
- sources/he-2023-hf-pairs-chinese-futures
- sources/moura-2016-pairs-trading-kalman
tags:
- econometrics
- time-series
- stationarity
- error-correction
- unit-root
title: Cointegration
updated: '2026-06-09T12:00:00Z'
---

## Definition

Cointegration describes a long-run equilibrium relationship between non-stationary time series. Two or more series are cointegrated if:
1. Each individual series is integrated of order 1, I(1) - i.e., non-stationary
2. A linear combination of the series is stationary, I(0)

## Mathematical Formulation

### Two Series Case

If Y_t ~ I(1) and X_t ~ I(1), they are cointegrated if:
```
Y_t - beta * X_t = e_t ~ I(0)
```
where beta is the cointegration coefficient and e_t is the stationary equilibrium error.

### Vector Form

For n variables X_t = (X_1t, ..., X_nt)', cointegration exists if there exists vector alpha such that:
```
alpha' * X_t ~ I(0)
```

## Economic Interpretation

Cointegration captures:
- **Long-run equilibrium**: Variables move together over time
- **Short-run deviations**: Temporary divergences from equilibrium
- **Error correction**: Forces that restore equilibrium

Example: Stock prices of Coca-Cola and PepsiCo may individually be random walks, but their ratio (or difference) may be mean-reverting due to competitive dynamics.

## Testing Methods

### Engle-Granger Two-Step

1. Estimate cointegrating regression via OLS:
   Y_t = alpha + beta * X_t + e_t

2. Test residuals e_t for stationarity using ADF test

**Critical values** differ from standard ADF (Engle-Granger tables)

### Johansen Test

Multivariate approach based on VAR representation:
- Tests number of cointegrating vectors (rank)
- Maximum eigenvalue and trace statistics
- More powerful than Engle-Granger

### Phillips-Ouliaris Test

- Non-parametric corrections
- Robust to serial correlation
- Alternative to ADF-based tests

## Error Correction Model (ECM)

Cointegration implies ECM representation (Granger Representation Theorem):

```
Delta(Y_t) = alpha_y * (Y_{t-1} - beta*X_{t-1}) + lagged differences + e_yt
Delta(X_t) = alpha_x * (Y_{t-1} - beta*X_{t-1}) + lagged differences + e_xt
```

Where:
- alpha_y, alpha_x: Adjustment coefficients (speed of error correction)
- Y_{t-1} - beta*X_{t-1}: Equilibrium error from previous period

## Application to Pairs Trading

### Pair Selection

Cointegrated pairs are ideal for [[concepts/pairs-trading|pairs trading]]:
- Long-run relationship ensures mean reversion
- Spread = Y_t - beta*X_t is stationary
- Statistical basis for trading signals

### Trading Framework ([[sources/he-2023-hf-pairs-chinese-futures|He et al. 2023]])

1. **Screen pairs** using Johansen cointegration test
2. **Confirm stationarity** of spread via ADF test
3. **Estimate hedge ratio** from cointegrating vector
4. **Trade spread** based on Z-score or other signals

### Dynamic Cointegration

[[concepts/kalman-filter|Kalman filter]] allows for time-varying cointegration:
- Hedge ratio beta evolves over time
- Captures structural breaks in relationship
- More robust to changing market conditions

## Properties

### Spurious Regression Problem

Non-cointegrated I(1) series produce:
- High R-squared
- Apparently significant t-statistics
- Invalid inference

Cointegration testing avoids this trap.

### Super-Consistency

OLS estimator of cointegrating vector:
- Converges at rate T (not sqrt(T))
- Asymptotically normal
- Consistent even with endogeneity

## Limitations

| Issue | Description |
|-------|-------------|
| Structural breaks | Cointegration may be time-varying |
| Sample dependence | Results sensitive to sample period |
| Specification | Linear model may be misspecified |
| Multiple vectors | Choice of normalization matters |

## Related Concepts

- [[concepts/stationarity|Stationarity]] - property of I(0) series
- [[concepts/pairs-trading|Pairs Trading]] - primary application
- [[concepts/mean-reversion|Mean Reversion]] - implied by cointegration
- [[concepts/error-correction-model|Error Correction Model]] - ECM representation

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/duasa-2010-predicting-crisis-recovery]]