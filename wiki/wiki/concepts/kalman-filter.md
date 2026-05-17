---
title: "Kalman Filter"
page_id: concepts/kalman-filter
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [filtering, estimation, time-series, signal-processing]
sources: [sources/he-2024-functional-regression]
related: [concepts/state-space-models, concepts/schwartz-smith-model, concepts/functional-data-analysis]
mind_map_priority: medium
---

# Kalman Filter

The Kalman filter is the optimal linear recursive estimator for state-space models with Gaussian noise, providing minimum variance state estimates.

## Algorithm

For state-space model:
- State: $\mathbf{x}_t = \mathbf{F}\mathbf{x}_{t-1} + \mathbf{w}_t$, where $\mathbf{w}_t \sim N(0, \mathbf{Q})$
- Observation: $\mathbf{y}_t = \mathbf{H}\mathbf{x}_t + \mathbf{v}_t$, where $\mathbf{v}_t \sim N(0, \mathbf{R})$

### Prediction Step
$$\hat{\mathbf{x}}_{t|t-1} = \mathbf{F}\hat{\mathbf{x}}_{t-1|t-1}$$
$$\mathbf{P}_{t|t-1} = \mathbf{F}\mathbf{P}_{t-1|t-1}\mathbf{F}' + \mathbf{Q}$$

### Update Step
$$\mathbf{K}_t = \mathbf{P}_{t|t-1}\mathbf{H}'(\mathbf{H}\mathbf{P}_{t|t-1}\mathbf{H}' + \mathbf{R})^{-1}$$
$$\hat{\mathbf{x}}_{t|t} = \hat{\mathbf{x}}_{t|t-1} + \mathbf{K}_t(\mathbf{y}_t - \mathbf{H}\hat{\mathbf{x}}_{t|t-1})$$
$$\mathbf{P}_{t|t} = (\mathbf{I} - \mathbf{K}_t\mathbf{H})\mathbf{P}_{t|t-1}$$

## Key Quantities

| Symbol | Meaning |
|--------|---------|
| $\hat{\mathbf{x}}_{t\|t}$ | Filtered state estimate |
| $\mathbf{P}_{t\|t}$ | State covariance |
| $\mathbf{K}_t$ | Kalman gain |
| $\mathbf{y}_t - \mathbf{H}\hat{\mathbf{x}}_{t\|t-1}$ | Innovation (prediction error) |

## Optimality Properties

1. **BLUE**: Best Linear Unbiased Estimator
2. **Minimum variance**: Minimizes MSE among linear estimators
3. **Bayesian**: Gives exact posterior for linear Gaussian systems
4. **Recursive**: O(n) in time series length

## Extensions

| Extension | Use Case |
|-----------|----------|
| Extended Kalman Filter (EKF) | Nonlinear systems, linearization |
| Unscented Kalman Filter (UKF) | Nonlinear, better than EKF |
| Particle Filter | Non-Gaussian, severely nonlinear |
| Ensemble Kalman Filter | High-dimensional systems |

## Financial Applications

- **Yield curve factor extraction** (Nelson-Siegel factors)
- **Commodity price decomposition** (Schwartz-Smith)
- **Volatility filtering** (stochastic volatility models)
- **Missing data interpolation**

## See Also

- [[concepts/state-space-models|State-Space Models]]
- [[concepts/schwartz-smith-model|Schwartz-Smith Model]]
- [[concepts/functional-data-analysis|Functional Data Analysis]]
- [[sources/he-2024-functional-regression|Multi-Factor Function-on-Function Regression (2024)]]
