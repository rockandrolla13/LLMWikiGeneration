---
title: "Flexible Least Squares"
page_id: concepts/flexible-least-squares
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [time-varying-regression, kalman-filter, econometrics, adaptive-estimation]
related: [concepts/kalman-filter, concepts/time-varying-regression, concepts/statistical-arbitrage, concepts/state-space-models]
sources: [sources/montana-2009-flexible-least-squares, sources/triantafyllopoulos-2011-mean-reverting-spreads]
---

## Definition

Flexible Least Squares (FLS) is a penalized regression method that allows regression coefficients to vary smoothly over time. Introduced by Kalaba and Tesfatsion (1989), FLS balances fitting the data against maintaining smooth coefficient paths through a penalty term.

## Mathematical Formulation

### Cost Function

FLS minimizes the incompatibility cost:
```
J = sum_t (y_t - x_t' * beta_t)^2 + mu * sum_t ||beta_t - beta_{t-1}||^2
```

Where:
- First term: Measurement residuals (fit to observations)
- Second term: Dynamic residuals (smoothness of coefficient path)
- mu >= 0: Trade-off parameter

### Interpretation

- **mu = 0**: Standard OLS (coefficients free to jump)
- **mu -> infinity**: Constant coefficients (equivalent to pooled OLS)
- **Intermediate mu**: Smooth time-varying coefficients

## Equivalence to Kalman Filter

[[sources/montana-2009-flexible-least-squares|Montana et al. (2009)]] prove that FLS is algebraically equivalent to the [[concepts/kalman-filter|Kalman filter]] with:

### State Equation
```
beta_t = beta_{t-1} + eta_t,  eta_t ~ N(0, Q)
```
Random walk evolution of coefficients.

### Observation Equation
```
y_t = x_t' * beta_t + epsilon_t,  epsilon_t ~ N(0, R)
```

### Key Relationship
```
mu = R / Q
```

The FLS penalty parameter equals the ratio of observation noise variance to state noise variance.

## Implications of Equivalence

| FLS Perspective | Kalman Filter Perspective |
|-----------------|--------------------------|
| Penalized optimization | State-space estimation |
| Deterministic | Probabilistic |
| mu controls smoothness | Q/R ratio controls adaptation |
| No distributional assumptions | Gaussian assumption |

### Practical Benefits

1. **Numerical Stability**: Kalman filter recursions more stable than original FLS algorithm
2. **Interpretability**: Probabilistic interpretation of coefficients
3. **Confidence Intervals**: Kalman filter provides uncertainty estimates
4. **Initial Conditions**: Can incorporate prior information

## Original FLS Algorithm

From Kalaba and Tesfatsion (1989):

### Forward Recursion

```
S_t = S_{t-1} + x_t * x_t' + mu * I
s_t = s_{t-1} + x_t * y_t
beta_t = S_t^{-1} * (s_t + mu * beta_{t+1})  (requires future value)
```

### Backward Smoothing

Since FLS requires future observations (beta_{t+1}), full algorithm involves backward pass - making it offline.

## On-Line FLS via Kalman Filter

Montana et al.'s contribution enables on-line implementation:

1. Set Q = 1/mu * R (or equivalently Q = 1, R = mu)
2. Run standard Kalman filter forward recursions
3. Get filtered estimates beta_{t|t} in real-time

### Kalman Filter Recursions

```
Prediction:
  beta_{t|t-1} = beta_{t-1|t-1}
  P_{t|t-1} = P_{t-1|t-1} + Q

Update:
  K_t = P_{t|t-1} * x_t / (x_t' * P_{t|t-1} * x_t + R)
  beta_{t|t} = beta_{t|t-1} + K_t * (y_t - x_t' * beta_{t|t-1})
  P_{t|t} = (I - K_t * x_t') * P_{t|t-1}
```

## Application to Statistical Arbitrage

[[sources/montana-2009-flexible-least-squares|Montana et al. (2009)]] apply FLS to trading:

### Setting

- Target asset: S&P 500 Futures Index
- Predictors: Sector ETFs
- Goal: Construct synthetic asset tracking target

### Time-Varying Beta

```
y_t = x_t' * beta_t + epsilon_t
```
- y_t: Futures return
- x_t: ETF returns
- beta_t: Time-varying exposures

### Trading Signal

- Residual = y_t - x_t' * beta_t = "mispricing"
- Trade when mispricing is extreme
- Mean-reverting mispricing enables profit

## Advantages

1. **Minimal Assumptions**: No distributional requirements (via original FLS)
2. **Adaptability**: Tracks changing relationships
3. **Simplicity**: Single tuning parameter mu
4. **Efficiency**: O(p^3) per time step with Kalman recursions

## Choosing mu

### Cross-Validation

- Out-of-sample prediction error
- Computationally intensive

### Likelihood-Based

- Treat as state-space model
- Estimate mu (via Q) by MLE

### Domain Knowledge

- Beliefs about how fast coefficients should change
- Economic rationale for stability vs. adaptation

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] - equivalent probabilistic formulation
- [[concepts/time-varying-regression|Time-Varying Regression]] - general framework
- [[concepts/state-space-models|State Space Models]] - underlying structure
- [[concepts/statistical-arbitrage|Statistical Arbitrage]] - trading application
