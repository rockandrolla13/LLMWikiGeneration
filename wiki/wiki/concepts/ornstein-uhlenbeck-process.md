---
title: Ornstein-Uhlenbeck Process
page_id: concepts/ornstein-uhlenbeck-process
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- stochastic-processes
- mean-reversion
- continuous-time
- diffusion-processes
related:
- concepts/mean-reversion
- concepts/kalman-filter
- concepts/pairs-trading
- concepts/state-space-models
sources:
- sources/moura-2016-pairs-trading-kalman
- sources/triantafyllopoulos-2011-mean-reverting-spreads
schema_version: 2
uuid: 74ecdfa4-1de1-5e5f-9278-aff44d0b328d
content_hash: sha256:2e8433b327d7980bc491bab3525337e5119fda3fedd073a666b9ca4061f436e6
---

<!-- AUTHORED REGION START -->
## Definition

The Ornstein-Uhlenbeck (O-U) process is a continuous-time stochastic process that models mean-reverting behavior. Originally developed to describe the velocity of a particle undergoing Brownian motion with friction, it has become fundamental in financial modeling.

## Mathematical Specification

### Stochastic Differential Equation

```
dX_t = kappa * (mu - X_t) * dt + sigma * dW_t
```

Where:
- X_t: Process value at time t
- kappa > 0: Speed of mean reversion (rate of pull toward mean)
- mu: Long-term mean (equilibrium level)
- sigma > 0: Volatility (diffusion coefficient)
- W_t: Standard Wiener process (Brownian motion)

### Solution

The explicit solution is:
```
X_t = mu + (X_0 - mu)*exp(-kappa*t) + sigma * integral_0^t exp(-kappa*(t-s)) dW_s
```

## Statistical Properties

### Stationary Distribution

For t -> infinity, X_t converges to stationary distribution:
```
X_infinity ~ N(mu, sigma^2 / (2*kappa))
```

### Moments

| Property | Formula |
|----------|---------|
| Mean | E[X_t] = mu + (X_0 - mu)*exp(-kappa*t) |
| Variance | Var(X_t) = sigma^2/(2*kappa) * (1 - exp(-2*kappa*t)) |
| Autocovariance | Cov(X_t, X_s) = sigma^2/(2*kappa) * exp(-kappa*\|t-s\|) |

### Autocorrelation

```
Corr(X_t, X_{t+h}) = exp(-kappa * h)
```

Exponential decay of correlations - characteristic of mean reversion.

## Half-Life

Time for expected deviation from mean to decay by half:
```
H = ln(2) / kappa
```

This is a key parameter for [[concepts/pairs-trading|pairs trading]] - indicates how long to wait for spread to revert.

## Discrete-Time Approximation

### Exact Discretization

Sampling at intervals Delta t:
```
X_{t+Delta} = mu + (X_t - mu)*exp(-kappa*Delta) + epsilon
epsilon ~ N(0, sigma^2/(2*kappa)*(1 - exp(-2*kappa*Delta)))
```

### AR(1) Approximation

For small Delta t, approximately:
```
X_{t+1} = c + phi*X_t + epsilon
```
Where:
- phi = exp(-kappa*Delta)
- c = mu*(1 - phi)
- sigma_epsilon = sigma*sqrt(Delta)

## Applications in Finance

### Interest Rate Models

Vasicek model (1977):
```
dr_t = kappa*(theta - r_t)*dt + sigma*dW_t
```
- O-U process for short rate
- Allows negative rates
- Analytically tractable bond prices

### Pairs Trading

[[sources/moura-2016-pairs-trading-kalman|de Moura et al. (2016)]]:
- Model spread between paired assets as O-U process
- Use Kalman filter for state estimation
- Trading signals based on deviations from mean

### Volatility Models

- Mean-reverting volatility (Heston model uses CIR, which is related)
- VIX modeling

## State-Space Representation

Elliott et al. (2005) discrete-time version:
```
x_t = a + (1-b)*x_{t-1} + C*eta_t     (state)
S_t = x_t + D*epsilon_t                (observation)
```

This is the discrete O-U with measurement noise, enabling [[concepts/kalman-filter|Kalman filter]] estimation.

## Extensions

### Time-Varying Parameters

[[sources/triantafyllopoulos-2011-mean-reverting-spreads|Triantafyllopoulos & Montana (2011)]]:
- kappa_t, mu_t allowed to evolve
- Bayesian on-line estimation
- Adapts to changing market conditions

### Non-Linear Mean Reversion

[[sources/zhang-2021-pairs-general-ssm|Zhang (2021)]]:
- Quadratic drift: f(x) = theta_1 + theta_2*x + theta_3*x^2
- Ait-Sahalia type: includes 1/x term
- Captures asymmetric reversion

### Multi-Factor Models

Multiple O-U processes for yield curve factors:
- Level, slope, curvature as O-U processes
- [[concepts/nelson-siegel-model|Nelson-Siegel]] dynamic model

## Estimation Methods

| Method | Description |
|--------|-------------|
| OLS | Estimate AR(1) regression |
| MLE | Maximum likelihood with exact transition density |
| Kalman Filter | State-space estimation with unobserved state |
| GMM | Moment matching (mean, variance, autocorrelation) |

## Limitations

- Normally distributed increments (no jumps)
- Constant volatility (no heteroscedasticity)
- Linear mean reversion (may be misspecified)
- Negative values possible (problematic for some applications)

## Related Concepts

- [[concepts/mean-reversion|Mean Reversion]] - general property
- [[concepts/kalman-filter|Kalman Filter]] - estimation method
- [[concepts/state-space-models|State Space Models]] - modeling framework
- [[concepts/vasicek-model|Vasicek Model]] - interest rate application

<!-- AUTHORED REGION END -->
