---
title: "Gaussian Processes"
page_id: concepts/gaussian-processes
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [machine-learning, bayesian-methods, non-parametric, spatial-statistics]
sources: [sources/huynh-2021-mogp-longevity]
related: [concepts/kriging, concepts/multi-population-mortality, concepts/uncertainty-quantification, entities/mike-ludkovski]
mind_map_priority: high
---

# Gaussian Processes

A Gaussian process (GP) is a collection of random variables, any finite number of which have a joint Gaussian distribution. GPs provide a flexible, non-parametric approach to regression and classification with principled uncertainty quantification.

## Definition

A GP is fully specified by:
- **Mean function**: $m(x) = E[f(x)]$
- **Covariance function (kernel)**: $k(x, x') = E[(f(x)-m(x))(f(x')-m(x'))]$

We write: $f(x) \sim \mathcal{GP}(m(x), k(x, x'))$

## Common Kernels

| Kernel | Formula | Properties |
|--------|---------|------------|
| Squared Exponential (RBF) | $\exp(-\|x-x'\|^2/2\ell^2)$ | Infinitely smooth |
| Matérn 3/2 | $(1+\sqrt{3}r/\ell)\exp(-\sqrt{3}r/\ell)$ | Once differentiable |
| Matérn 5/2 | $(1+\sqrt{5}r/\ell + 5r^2/3\ell^2)\exp(-\sqrt{5}r/\ell)$ | Twice differentiable |
| Periodic | $\exp(-2\sin^2(\pi\|x-x'\|/p)/\ell^2)$ | Repeating patterns |

## GP Regression

Given training data $(X, \mathbf{y})$, predict at test points $X_*$:

$$\mathbf{f}_* | X_*, X, \mathbf{y} \sim \mathcal{N}(\bar{\mathbf{f}}_*, \text{cov}(\mathbf{f}_*))$$

Where:
- $\bar{\mathbf{f}}_* = K(X_*, X)[K(X, X) + \sigma^2 I]^{-1}\mathbf{y}$
- $\text{cov}(\mathbf{f}_*) = K(X_*, X_*) - K(X_*, X)[K(X, X) + \sigma^2 I]^{-1}K(X, X_*)$

## Multi-Output GPs

Extend to multiple correlated outputs via:
- **Intrinsic Coregionalization Model (ICM)**: $K(x,x') \otimes B$
- **Linear Model of Coregionalization (LMC)**: Sum of ICM components
- Enables joint modelling of related populations

## Applications in Finance/Actuarial

- Multi-population mortality modelling
- Yield curve interpolation
- Volatility surface fitting
- Uncertainty quantification in forecasts

## See Also

- [[concepts/kriging|Kriging]]
- [[concepts/multi-population-mortality|Multi-Population Mortality]]
- [[concepts/uncertainty-quantification|Uncertainty Quantification]]
- [[sources/huynh-2021-mogp-longevity|Multi-output Gaussian Processes for Multi-population Longevity Modelling (2021)]]
