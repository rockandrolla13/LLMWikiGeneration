---
title: Distributional Conformal Prediction
page_id: concepts/distributional-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- quantile-regression
- conditional-validity
- heteroskedasticity
sources:
- sources/chernozhukov-2021-distributional-cp
related:
- concepts/conformal-prediction
- concepts/probability-integral-transform
- concepts/conditional-validity
- concepts/quantile-regression
- concepts/prediction-intervals
mind_map_priority: high
schema_version: 2
uuid: 6026bfad-02fd-5bdd-836d-ad746afec5f2
content_hash: sha256:f40d814ca9d84014acbd1b5207f55bbc08a59c80e2e277ab998722bb6700161c
---

<!-- AUTHORED REGION START -->
# Distributional Conformal Prediction

**Distributional Conformal Prediction (DCP)** is a method for constructing prediction intervals that achieve approximate [[concepts/conditional-validity|conditional validity]]—that is, valid coverage conditional on the full vector of predictors—by exploiting the [[concepts/probability-integral-transform|probability integral transform]] and permuting estimated ranks.

## Core Insight

Standard conformal prediction based on regression residuals produces prediction intervals with **fixed length** that do not adapt to heteroskedasticity. DCP addresses this by using the conditional rank as the conformity score:

> U_t = F(Y_t, X_t)

where F(y,x) = P(Y ≤ y | X = x) is the conditional CDF. By the probability integral transform, U_t is **uniformly distributed** and **independent of X_t**, enabling conditionally valid prediction intervals.

## Key Advantages over Mean-Based Conformal Prediction

| Property | Mean-based CP | DCP |
|----------|--------------|-----|
| Interval length | Fixed | Adapts to local variance |
| Conditional validity | No | Yes (asymptotic) |
| Handles heteroskedasticity | No | Yes |
| Conformity score | |Y - μ̂(X)| | |F̂(Y,X) - 0.5| |

## Algorithm

### Split DCP Procedure
1. **Split** data into training T₁ and calibration T₂
2. **Estimate** conditional CDF F̂ from T₁ using [[concepts/quantile-regression|quantile regression]] or distribution regression
3. **Compute ranks** Û_t = F̂(Y_t, X_t) for t ∈ T₂
4. **Compute conformity** V̂_t = |Û_t - 0.5|
5. **Find threshold** q̂ = (1-α)-quantile of {V̂_t}_{t∈T₂}
6. **Construct interval** Ĉ(X_{n+1}) = {y : |F̂(y, X_{n+1}) - 0.5| ≤ q̂}

## Optimal DCP

For asymmetric distributions, the baseline ψ(y,x) = |F(y,x) - 0.5| may not yield the shortest intervals. **Optimal DCP** uses a "shape adjustment":

> ψ*(y,x) = |F(y,x) - b(x,α) - (1-α)/2|

where b(x,α) is chosen to minimize interval length while maintaining coverage. For symmetric unimodal distributions, b(x,α) = α/2 recovers the baseline.

## Theoretical Guarantees

1. **Finite-sample unconditional validity**: With exchangeable data, P(Y_{n+1} ∈ Ĉ) ≥ 1-α
2. **Asymptotic conditional validity**: Under consistent F̂ estimation, P(Y_{n+1} ∈ Ĉ | X_{n+1}) → 1-α
3. **Optimality**: Optimal DCP achieves the shortest possible conditionally valid interval

## Implementation Requirements

DCP requires estimating the full conditional distribution F(y|x), not just the conditional mean. Common approaches:
- Linear quantile regression
- Distribution regression
- Quantile neural networks
- Quantile random forests

## Example: Stock Return Prediction

When predicting stock returns given realized volatility:
- **Mean-based CP**: Fixed-width interval drops to ~50% coverage during high-volatility periods
- **DCP**: Maintains ~90% coverage across all volatility levels by widening intervals when variance is high

## Relation to Other Methods

- **CQR (Conformalized Quantile Regression)**: Uses |Y - Q̂(τ,X)| as score; DCP uses ranks
- **Standard CP**: Uses residuals; DCP uses probability transform
- **Model-free prediction (Politis)**: Uses bootstrap; DCP uses permutation

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/probability-integral-transform|Probability Integral Transform]]
- [[concepts/conditional-validity|Conditional Validity]]
- [[sources/chernozhukov-2021-distributional-cp|Chernozhukov et al. (2021)]]

<!-- AUTHORED REGION END -->
