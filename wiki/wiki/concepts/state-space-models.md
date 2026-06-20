---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: high
page_id: concepts/state-space-models
page_type: concept
related:
- concepts/beta-mixing-processes
- concepts/functional-data-analysis
- concepts/hidden-markov-models
- concepts/kalman-filter
- concepts/linear-quadratic-control-kalman-filter
- concepts/nelson-siegel-model
- concepts/recursive-methods-dynamic-programming
- concepts/schwartz-smith-model
- entities/gareth-peters
revision_id: 3
sources:
- sources/he-2024-functional-regression
tags:
- time-series
- filtering
- econometrics
- latent-variables
title: State-Space Models
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 33dd2113-405d-57e1-b527-e6888e03584f
content_hash: sha256:47a8ddff96ccb7804a0598fd689ba08bbb4d62f321551a0c199fb31b1f86b53f
---

<!-- AUTHORED REGION START -->
# State-Space Models

State-space models represent dynamic systems through two equations: a state transition equation describing latent dynamics and an observation equation linking states to measurements.

## General Form

**State equation**:
$$\mathbf{x}_t = \mathbf{F}_t \mathbf{x}_{t-1} + \mathbf{G}_t \mathbf{u}_t + \mathbf{w}_t$$

**Observation equation**:
$$\mathbf{y}_t = \mathbf{H}_t \mathbf{x}_t + \mathbf{v}_t$$

Where:
- $\mathbf{x}_t$ = State vector (unobserved)
- $\mathbf{y}_t$ = Observation vector
- $\mathbf{F}_t$ = State transition matrix
- $\mathbf{H}_t$ = Observation matrix
- $\mathbf{w}_t, \mathbf{v}_t$ = Process and observation noise

## Key Properties

| Property | Implication |
|----------|-------------|
| Latent states | Model unobserved factors |
| Recursive updating | Online estimation possible |
| Missing data | Naturally handled |
| Time-varying | Parameters can change |

## Estimation

**Filtering**: Estimate $p(\mathbf{x}_t | \mathbf{y}_{1:t})$ (Kalman filter for linear Gaussian)

**Smoothing**: Estimate $p(\mathbf{x}_t | \mathbf{y}_{1:T})$ (use all data)

**Parameter estimation**: Maximum likelihood via prediction error decomposition

## Applications in Finance

### Dynamic Factor Models
Observe many series, few latent factors:
- Yield curve factors (level, slope, curvature)
- Credit cycle indicators
- Volatility factors

### Term Structure Models
- Dynamic Nelson-Siegel
- Affine term structure models
- Schwartz-Smith commodity model

### Functional Data
- Time-varying functional parameters
- Function-on-function regression

## Extensions

- **Nonlinear**: Extended/Unscented Kalman filters
- **Non-Gaussian**: Particle filters
- **Switching**: Regime-switching state-space models
- **Mixed frequency**: Handle data at different frequencies

## See Also

- [[concepts/kalman-filter|Kalman Filter]]
- [[concepts/schwartz-smith-model|Schwartz-Smith Model]]
- [[concepts/functional-data-analysis|Functional Data Analysis]]
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]]
- [[sources/he-2024-functional-regression|Multi-Factor Function-on-Function Regression (2024)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/hidden-markov-models|hidden-markov-models]]
- [[concepts/kalman-filter|kalman-filter]]
- [[concepts/linear-quadratic-control-kalman-filter|linear-quadratic-control-kalman-filter]]
- [[concepts/recursive-methods-dynamic-programming|recursive-methods-dynamic-programming]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/beta-mixing-processes|beta-mixing-processes]]
<!-- AUTHORED REGION END -->
