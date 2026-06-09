---
created: 2026-04-26 10:00:00+00:00
mind_map_priority: medium
page_id: concepts/copulas
page_type: concept
related:
- concepts/conformal-prediction
- concepts/copula-sklar-theorem
- concepts/multi-step-conformal-prediction
- concepts/uncertainty-quantification
revision_id: 2
sources:
- sources/sun-2022-copula-cpts
tags:
- probability
- dependency-modeling
- multivariate
- statistics
title: Copulas
updated: '2026-06-09T12:00:00Z'
---

# Copulas

A **copula** is a multivariate cumulative distribution function (CDF) that captures the dependency structure between random variables, independent of their marginal distributions. Copulas provide a powerful way to model and analyze the relationship between multiple variables in statistics, finance, and machine learning.

## Definition

Given a random vector (X₁, ..., Xₖ) with marginal CDFs F₁, ..., Fₖ, the copula C: [0,1]^k → [0,1] is defined as:

C(u₁, ..., uₖ) = P[F₁(X₁) ≤ u₁, ..., Fₖ(Xₖ) ≤ uₖ]

Equivalently, a copula is the joint CDF of the probability integral transforms (F₁(X₁), ..., Fₖ(Xₖ)), which are all uniformly distributed on [0,1].

## Sklar's Theorem

The fundamental result in copula theory states that for any multivariate distribution F with marginals F₁, ..., Fₖ, there exists a copula C such that:

F(x₁, ..., xₖ) = C(F₁(x₁), ..., Fₖ(xₖ))

Conversely, any copula combined with arbitrary marginals defines a valid joint distribution. This decomposition separates:
- **Marginals**: Individual variable distributions
- **Copula**: Dependency structure

## Types of Copulas

### Independence Copula
When variables are independent:
C(u₁, ..., uₖ) = u₁ × u₂ × ... × uₖ

### Empirical Copula
Non-parametric estimate from data ([[sources/sun-2022-copula-cpts]]):
C_empirical(u₁, ..., uₖ) = (1/n) Σᵢ 1(Uᵢ₁ ≤ u₁, ..., Uᵢₖ ≤ uₖ)

### Gaussian Copula
Derived from multivariate normal with correlation matrix Σ.

### Archimedean Copulas
Family including Clayton, Gumbel, and Frank copulas with explicit generator functions.

## Frechet-Hoeffding Bounds

All copulas are bounded:

**Lower bound** (W): max(Σuᵢ - k + 1, 0) ≤ C(u₁, ..., uₖ)
**Upper bound** (M): C(u₁, ..., uₖ) ≤ min(u₁, ..., uₖ)

The lower bound W corresponds to Bonferroni correction, while the upper bound M represents perfect positive dependence.

## Application in Conformal Prediction

In [[concepts/multi-step-conformal-prediction|multi-step conformal prediction]], copulas enable:

1. **Joint validity**: Coverage guarantee for the entire forecast horizon, not just individual steps
2. **Efficiency**: Tighter confidence regions than Bonferroni correction (which uses the lower Frechet-Hoeffding bound)
3. **Dependency capture**: Model how uncertainty at different time steps is correlated

### CopulaCPTS Approach
The [[sources/sun-2022-copula-cpts|CopulaCPTS]] algorithm:
1. Calibrates marginal CDFs of nonconformity scores for each time step
2. Uses empirical copula to model the joint distribution
3. Finds optimal u* such that C(u*) ≥ 1-α to construct valid confidence regions

## Applications

### Finance
- Portfolio risk modeling
- Credit default correlation
- Multi-asset option pricing

### Time Series
- Multi-step forecasting uncertainty
- Multivariate time series modeling
- Spatiotemporal dependencies

### Machine Learning
- Multi-output prediction
- Conformal prediction ([[concepts/conformal-prediction]])
- Probabilistic forecasting

## Key Properties

1. **Invariance**: Copulas are invariant under strictly increasing transformations of marginals
2. **Flexibility**: Can model various dependency structures (positive, negative, asymmetric)
3. **Dimension reduction**: Separates dependency from marginals, simplifying multivariate modeling

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/multi-step-conformal-prediction|Multi-step Conformal Prediction]]
- [[concepts/uncertainty-quantification|Uncertainty Quantification]]
- [[sources/sun-2022-copula-cpts|CopulaCPTS]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/copula-sklar-theorem|copula-sklar-theorem]]