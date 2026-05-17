---
title: Generalized Pareto Distribution
page_id: concepts/generalized-pareto-distribution
page_type: concept
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [statistics, extreme-value-theory, probability-distribution, heavy-tails, risk-management]
sources: [sources/pasche-2025-extreme-conformal]
related: [concepts/extreme-value-theory, concepts/conformal-prediction, concepts/coverage-guarantee, concepts/prediction-intervals]
mind_map_priority: medium
---

# Generalized Pareto Distribution

The **Generalized Pareto Distribution (GPD)** is a fundamental distribution in [[concepts/extreme-value-theory|extreme value theory]] for modeling threshold exceedances. It provides the theoretical basis for extrapolating quantiles beyond the observed data range in applications such as extreme [[concepts/conformal-prediction|conformal prediction]].

## Definition

The GPD has cumulative distribution function:
$$G_{\xi,\sigma}(y) = \begin{cases} 1 - \left(1 + \xi \frac{y}{\sigma}\right)^{-1/\xi} & \xi \neq 0 \\ 1 - \exp\left(-\frac{y}{\sigma}\right) & \xi = 0 \end{cases}$$

where:
- $\sigma > 0$ is the **scale parameter**
- $\xi \in \mathbb{R}$ is the **shape parameter** (tail index)

## Support

The support depends on the shape parameter:
- $\xi \geq 0$: $y \in [0, \infty)$
- $\xi < 0$: $y \in [0, -\sigma/\xi]$

## Tail Behavior

The shape parameter $\xi$ determines the tail heaviness:

| $\xi$ | Tail Type | Example Distributions |
|-------|-----------|----------------------|
| $\xi > 0$ | Heavy-tailed (Fréchet domain) | Student-t, Pareto |
| $\xi = 0$ | Light-tailed (Gumbel domain) | Normal, Exponential |
| $\xi < 0$ | Bounded support (Weibull domain) | Uniform, Beta |

## Theoretical Foundation

### Pickands-Balkema-de Haan Theorem
For a random variable $X$ with distribution $F$ satisfying mild conditions, the conditional distribution of threshold exceedances converges to GPD:
$$\mathbb{P}\{X - u \leq y | X > u\} \to G_{\xi,\sigma(u)}(y) \text{ as } u \to x_F$$

where $x_F$ is the upper endpoint of $F$.

This fundamental result (Balkema & de Haan, 1974; Pickands, 1975) justifies using GPD for extreme quantile estimation.

## Quantile Function

The quantile function (inverse CDF) for probability level $p$:
$$Q_p = \begin{cases} \frac{\sigma}{\xi}\left[(1-p)^{-\xi} - 1\right] & \xi \neq 0 \\ -\sigma \log(1-p) & \xi = 0 \end{cases}$$

## Application to Conformal Prediction

In [[sources/pasche-2025-extreme-conformal|extreme conformal prediction]], the GPD is used to extrapolate calibration score quantiles:

### Standard Extrapolation
Given threshold $u$ (e.g., empirical 95th percentile) and exceedance proportion $\tau_0 = k/n$:
$$\hat{Q}_{1-\alpha}^{\text{GPD}} = u + \frac{\hat{\sigma}}{\hat{\xi}}\left[\left(\frac{\alpha}{\tau_0}\right)^{-\hat{\xi}} - 1\right]$$

### Conservative CI Approach
For valid coverage at extreme levels, use confidence interval upper endpoint:
1. Fit GPD to calibration score exceedances
2. Compute $(1-\alpha_2)$-confidence interval for $(1-\alpha_1)$-quantile
3. Use upper endpoint as the extreme conformal correction

## Estimation Methods

### Maximum Likelihood
Given exceedances $y_1, \ldots, y_k$ over threshold $u$:
$$\ell(\sigma, \xi) = -k\log\sigma - \left(1 + \frac{1}{\xi}\right)\sum_{i=1}^k \log\left(1 + \xi\frac{y_i}{\sigma}\right)$$

### Weighted Likelihood
For nonstationary data with weights $w_i$:
$$\ell_w(\sigma, \xi) = \sum_{i: S_i > u} w_i \log g_{\xi, \sigma}(S_i - u)$$

## Confidence Intervals for Quantiles

### Profile Likelihood
- Most conservative method
- Captures asymmetric uncertainty
- May have numerical issues for very extreme quantiles

### Bootstrap
- Nonparametric bootstrap with percentile aggregation
- Reliable but potentially less conservative
- Never fails to provide finite estimates

### Delta Method
- Normal approximation using Fisher information
- Computationally efficient
- Symmetric intervals (unrealistic for large quantiles)

## Practical Considerations

### Threshold Selection
Critical choice affecting bias-variance tradeoff:
- **Too low**: Bias from non-extreme observations
- **Too high**: High variance from few exceedances
- **Common choice**: Empirical 95th percentile

Methods:
- Mean residual life plots
- Parameter stability plots
- Automated procedures

### Sample Size Requirements
For reliable GPD inference:
- At least 50-100 exceedances typically needed
- More exceedances required for smaller $\alpha$
- Trade-off with threshold choice

## Related Distributions

- **Exponential**: GPD with $\xi = 0$
- **Pareto Type II**: GPD with $\xi > 0$
- **Beta-type**: GPD with $\xi < 0$
- **GEV**: Related family for block maxima

## Software

R packages for GPD analysis:
- `evd`: Basic extreme value distributions
- `ismev`: Interactive threshold selection
- `extRemes`: Comprehensive EVT toolkit
- `ExtremeCI`: Profile-likelihood CIs for extreme quantiles

## See Also

- [[concepts/extreme-value-theory|Extreme Value Theory]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/prediction-intervals|Prediction Intervals]]
