---
title: Kriging
page_id: concepts/kriging
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- spatial-statistics
- geostatistics
- interpolation
- gaussian-processes
sources:
- sources/huynh-2021-mogp-longevity
related:
- concepts/gaussian-processes
- concepts/multi-population-mortality
mind_map_priority: medium
schema_version: 2
uuid: 32d28f57-9a9c-5afd-8463-40ae3ca278aa
content_hash: sha256:8b0821510ae65ea4cbe21ba425e030188969a49d689850ecd9a92e005490c238
---

<!-- AUTHORED REGION START -->
# Kriging

Kriging is a geostatistical interpolation method that provides optimal linear predictions at unobserved locations, along with prediction uncertainty estimates.

## Historical Context

Named after South African mining engineer Danie Krige (1951), kriging was formalized by Georges Matheron in the 1960s. It is mathematically equivalent to Gaussian process regression.

## Types of Kriging

### Simple Kriging
Assumes known constant mean $\mu$:
$$\hat{Z}(s_0) = \mu + \sum_{i=1}^{n} \lambda_i (Z(s_i) - \mu)$$

### Ordinary Kriging
Estimates unknown constant mean:
$$\hat{Z}(s_0) = \sum_{i=1}^{n} \lambda_i Z(s_i), \quad \sum_i \lambda_i = 1$$

### Universal Kriging
Allows spatially varying trend:
$$Z(s) = \mu(s) + \epsilon(s)$$

## The Kriging System

Weights $\lambda_i$ are found by minimizing prediction variance subject to unbiasedness, leading to the kriging equations:

$$\begin{pmatrix} C_{11} & \cdots & C_{1n} & 1 \\ \vdots & \ddots & \vdots & \vdots \\ C_{n1} & \cdots & C_{nn} & 1 \\ 1 & \cdots & 1 & 0 \end{pmatrix} \begin{pmatrix} \lambda_1 \\ \vdots \\ \lambda_n \\ \mu \end{pmatrix} = \begin{pmatrix} C_{10} \\ \vdots \\ C_{n0} \\ 1 \end{pmatrix}$$

## Variogram

The variogram $\gamma(h)$ measures spatial dependence:
$$\gamma(h) = \frac{1}{2}\text{Var}(Z(s+h) - Z(s))$$

Related to covariance: $\gamma(h) = C(0) - C(h)$

## Applications Beyond Geography

- **Mortality surfaces**: Interpolate across age-period grids
- **Yield curves**: Fill gaps in maturity spectrum
- **Computer experiments**: Emulate expensive simulations
- **Financial surfaces**: Volatility, correlation matrices

## See Also

- [[concepts/gaussian-processes|Gaussian Processes]]
- [[concepts/multi-population-mortality|Multi-Population Mortality]]
- [[sources/huynh-2021-mogp-longevity|Multi-output Gaussian Processes for Multi-population Longevity Modelling (2021)]]

<!-- AUTHORED REGION END -->
