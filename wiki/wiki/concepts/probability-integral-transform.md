---
created: 2026-04-26 12:00:00+00:00
mind_map_priority: medium
page_id: concepts/probability-integral-transform
page_type: concept
related:
- concepts/conditional-validity
- concepts/copula-sklar-theorem
- concepts/distributional-conformal-prediction
- concepts/marginal-copula-score
- concepts/quantile-regression
revision_id: 2
sources:
- sources/chernozhukov-2021-distributional-cp
tags:
- probability
- statistics
- uniformity
- transformations
title: Probability Integral Transform
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 246434d2-b580-5391-ae29-1c0a1a7b90ff
content_hash: sha256:32d0037e46ab38129d33541822d455766e8e2628201ce93eb3a0c70550c2155b
---

<!-- AUTHORED REGION START -->
# Probability Integral Transform

The **probability integral transform (PIT)** is a fundamental result in probability theory stating that applying a continuous cumulative distribution function (CDF) to a random variable produces a uniformly distributed random variable.

## Formal Statement

If X is a continuous random variable with CDF F(x), then:

> U = F(X) ~ Uniform(0, 1)

Conversely, if U ~ Uniform(0, 1) and F is a continuous CDF with inverse F⁻¹, then:

> X = F⁻¹(U) ~ F

## Key Properties

1. **Universality**: Works for any continuous distribution
2. **Invertibility**: The transformation can be reversed using quantile functions
3. **Independence from parameters**: The resulting uniform distribution has no free parameters

## Conditional Version

For conditional distributions F(y|x) = P(Y ≤ y | X = x):

> U = F(Y, X) | X ~ Uniform(0, 1)

Crucially, this conditional rank U is **independent of X**, which is the key insight exploited by [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]].

## Applications

### Distributional Conformal Prediction
The PIT enables [[concepts/conditional-validity|conditional validity]] by transforming the problem into one with a known, fixed distribution. Since ranks U_t = F(Y_t, X_t) are:
1. Uniform on (0,1)
2. Independent of X_t

Permutation-based inference can be applied to construct conditionally valid prediction intervals.

### Calibration Assessment
PIT is used to assess probabilistic forecast calibration:
- If forecasts are well-calibrated, PIT values should be uniform
- Systematic deviations indicate miscalibration

### Copula Theory
PITs of marginal distributions are central to copula construction:
> C(F₁(X₁), F₂(X₂), ..., F_n(X_n)) captures the dependence structure

### Simulation
The inverse PIT (quantile function) enables sampling:
1. Generate U ~ Uniform(0,1)
2. Apply X = F⁻¹(U) to get sample from F

## Mathematical Proof Sketch

For continuous F and X ~ F:

P(F(X) ≤ u) = P(X ≤ F⁻¹(u)) = F(F⁻¹(u)) = u

for u ∈ (0,1), which is the CDF of Uniform(0,1).

## Discreteness and Ties

For discrete or mixed distributions, the standard PIT does not yield exact uniformity. Remedies include:
- **Randomized PIT**: U = F(X⁻) + V·(F(X) - F(X⁻)) where V ~ Uniform(0,1)
- **Jittering**: Add small continuous noise

## Connection to Conformity Scores

In conformal prediction, the conformity score ψ(y,x) = |F(y,x) - 0.5| measures how "central" a point is in its conditional distribution. The PIT guarantees that under the true distribution:
- P(|F(Y,X) - 0.5| ≤ c) = 2c for c ∈ [0, 0.5]

This enables construction of valid prediction intervals by calibrating the threshold c.

## See Also

- [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]
- [[concepts/quantile-regression|Quantile Regression]]
- [[concepts/calibration|Calibration]]
- [[sources/chernozhukov-2021-distributional-cp|Chernozhukov et al. (2021)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/copula-sklar-theorem|copula-sklar-theorem]]
- [[concepts/marginal-copula-score|marginal-copula-score]]
<!-- AUTHORED REGION END -->
