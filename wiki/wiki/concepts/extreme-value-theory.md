---
title: Extreme Value Theory
page_id: concepts/extreme-value-theory
page_type: concept
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [statistics, risk-management, heavy-tails, floods, finance, extreme-events]
sources: [sources/pasche-2025-extreme-conformal]
related: [concepts/generalized-pareto-distribution, concepts/conformal-prediction, concepts/prediction-intervals, concepts/coverage-guarantee]
mind_map_priority: high
---

# Extreme Value Theory

**Extreme Value Theory (EVT)** provides statistical tools for accurate estimation and inference in the tails of distributions, enabling extrapolation beyond the observed data range. EVT forms the theoretical foundation for analyzing rare, high-impact events such as floods, financial crashes, and extreme weather.

## Core Concepts

### The Fundamental Problem
For applications involving high-impact events, we need to estimate:
- Very high quantiles (e.g., 99.99th percentile)
- Return levels (e.g., 100-year flood)
- Probabilities of extreme events

Classical statistical methods fail when these targets are beyond the data range.

### Fisher-Tippett-Gnedenko Theorem
For i.i.d. random variables $X_1, \ldots, X_n$ with maximum $M_n = \max\{X_1, \ldots, X_n\}$, if there exist sequences $a_n > 0$ and $b_n$ such that:
$$\mathbb{P}\left(\frac{M_n - b_n}{a_n} \leq x\right) \to G(x)$$

then $G$ must be one of three types: **Gumbel**, **Fréchet**, or **Weibull** (unified as the Generalized Extreme Value distribution).

## Peaks-Over-Threshold (POT) Approach

The POT methodology is fundamental to extreme conformal prediction and other applications.

### Theoretical Foundation
For a high threshold $u$, the conditional distribution of exceedances approximates the [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution]]:
$$\mathbb{P}\{X - u \leq y | X > u\} \approx G_{\xi, \sigma(u)}(y)$$

This approximation is theoretically justified as $u$ approaches the upper endpoint (Balkema & de Haan, 1974; Pickands, 1975).

### Quantile Extrapolation
Extreme quantiles can be estimated using:
$$\hat{Q}_{1-\alpha}^{\text{GPD}} = u + \frac{\sigma}{\xi}\left[\left(\frac{\alpha}{\tau_0}\right)^{-\xi} - 1\right]$$

where $\tau_0 = 1 - k/n$ and $k$ is the number of exceedances.

## Applications

### Flood Risk Assessment
- River flow prediction for protective infrastructure
- Return level estimation (e.g., 100-year flood)
- Spatial extreme modeling for river networks

### Financial Risk
- Value-at-Risk (VaR) for extreme losses
- Expected Shortfall estimation
- Stress testing for banks and insurance

### Conformal Prediction
[[sources/pasche-2025-extreme-conformal|Pasche et al. (2025)]] bridge EVT and [[concepts/conformal-prediction|conformal prediction]] for high-confidence prediction intervals:
- Extrapolate calibration score quantiles beyond data range
- Enable confidence levels beyond $n_c/(n_c + 1)$ limit

### Climate Extremes
- Heat wave probability estimation
- Extreme precipitation analysis
- Sea level rise projections

## Key Distributions

| Distribution | Support | Application |
|-------------|---------|-------------|
| Generalized Extreme Value (GEV) | Depends on $\xi$ | Block maxima |
| [[concepts/generalized-pareto-distribution|Generalized Pareto (GPD)]] | $[0, -\sigma/\xi]$ or $[0, \infty)$ | Threshold exceedances |
| Gumbel | $(-\infty, \infty)$ | Light-tailed extremes |
| Fréchet | $(0, \infty)$ | Heavy-tailed extremes |

## Estimation Methods

### Maximum Likelihood
Standard approach for GPD parameters $(\sigma, \xi)$ given exceedances over threshold $u$.

### Profile Likelihood
For confidence intervals on extreme quantiles:
- Most conservative method
- Captures asymmetric uncertainty
- May have numerical difficulties for very extreme levels

### Bootstrap Methods
- Nonparametric bootstrap
- Parametric bootstrap
- Various aggregation methods (percentile, basic, normal)

## Threshold Selection

A critical practical challenge is choosing the threshold $u$:
- Too low: Bias from non-extreme observations
- Too high: Variance from few observations
- Common choice: Empirical 95th percentile ($\tau_0 = 0.95$)

Methods include:
- Mean residual life plots
- Parameter stability plots
- Automated selection (Danielsson et al., 2001)

## Limitations

1. **Finite-sample bounds**: Impossible without distributional assumptions
2. **Threshold sensitivity**: Results depend on threshold choice
3. **Asymptotic theory**: Relies on limiting distributions
4. **Small samples**: Limited exceedances for extreme inference

## Foundational References

- de Haan & Ferreira (2006): *Extreme Value Theory*
- Coles (2001): *An Introduction to Statistical Modeling of Extreme Values*
- Balkema & de Haan (1974): Residual life time at great age
- Pickands (1975): Statistical inference using order statistics

## See Also

- [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
