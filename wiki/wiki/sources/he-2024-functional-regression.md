---
title: Multi-Factor Function-on-Function Regression of Bond Yields on WTI Commodity
  Futures Term Structure Dynamics
page_id: sources/he-2024-functional-regression
page_type: source
source_type: working-paper
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Peilun He
- Gareth W. Peters
- Nino Kordzakhia
- Pavel V. Shevchenko
year: 2024
venue: arXiv preprint (submitted to Journal of Commodity Markets)
tags:
- commodity-futures
- functional-regression
- state-space-models
- schwartz-smith
- yield-curves
- kalman-filter
related:
- sources/martin-2024-credit-curve
- concepts/functional-data-analysis
- concepts/schwartz-smith-model
- concepts/state-space-models
- concepts/kalman-filter
- entities/gareth-peters
- entities/pavel-shevchenko
mind_map_priority: high
schema_version: 2
uuid: 15c7a337-e534-5fdb-abf1-8bfebdb133f0
content_hash: sha256:a1d681f690a78c7f83ddc95c154b09b7abbf194e04d33da467f78d8b07382072
---

<!-- AUTHORED REGION START -->
# Multi-Factor Function-on-Function Regression of Bond Yields on WTI Commodity Futures

**Authors:** Peilun He, [[entities/gareth-peters|Gareth W. Peters]], Nino Kordzakhia, [[entities/pavel-shevchenko|Pavel V. Shevchenko]]

**Year:** 2024

**Venue:** arXiv preprint (submitted to Journal of Commodity Markets)

**Institutions:** Macquarie University, UC Santa Barbara

## Summary

Extends the [[concepts/schwartz-smith-model|Schwartz-Smith two-factor model]] for commodity futures by incorporating yield curve dynamics through [[concepts/functional-data-analysis|functional regression]], capturing interdependencies between futures and bond markets.

## Motivation

- Commodity futures influenced by economic conditions
- Yield curve is barometer of economic conditions
- Inverted yield curve predicts recession
- Traditional models treat commodity markets in isolation

## Key Contributions

### 1. Two-Factor Functional Regression Model
Extends Schwartz-Smith by adding functional regression component:
```
log F(t,T) = A(t) + exp(-κ_χ(T-t))χ_t + exp(-κ_ξ(T-t))ξ_t + Σ∫γ_i(τ)Z_t(τ)dτ
```
Where:
- χ_t = short-term fluctuation factor
- ξ_t = long-term equilibrium price level
- Z_t(·) = yield curve at time t
- γ_i(·) = functional coefficients

### 2. Kernel PCA for Dimension Reduction
- Transforms infinite-dimensional functional predictor
- Captures nonlinear relationships between variables
- Extracts principal factors from yield curve

### 3. State-Space Formulation
- Kalman filter for joint estimation
- Handles latent factors and unknown parameters
- Enables real-time updating

### 4. Stress Testing Framework
- Examines impact of yield curve shocks on futures
- Temporary vs. permanent shocks to Treasury yields
- Risk management applications

## Empirical Analysis

**Data:** WTI crude oil futures with US Treasury yields

**Results:**
- Functional regression outperforms standard Schwartz-Smith
- Particularly accurate for short-end of futures curve
- Captures yield curve interdependencies

## Model Components

1. **Schwartz-Smith Base:** Two OU processes for latent factors
2. **Functional Extension:** Yield curve as functional predictor
3. **kPCA:** Nonlinear dimension reduction
4. **Kalman Filter:** State estimation and parameter inference

## See Also

- [[concepts/schwartz-smith-model|Schwartz-Smith Model]]
- [[concepts/functional-data-analysis|Functional Data Analysis]]
- [[concepts/state-space-models|State-Space Models]]
- [[concepts/kalman-filter|Kalman Filter]]

<!-- AUTHORED REGION END -->
