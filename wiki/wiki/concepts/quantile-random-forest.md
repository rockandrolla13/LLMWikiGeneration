---
title: Quantile Random Forests
page_id: concepts/quantile-random-forest
page_type: concept
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [machine-learning, quantile-regression, random-forest, uncertainty-quantification]
sources: [sources/xu-2022-spci]
related: [concepts/prediction-intervals, concepts/conformal-prediction, concepts/spci, concepts/uncertainty-quantification]
mind_map_priority: medium
---

# Quantile Random Forests

**Quantile Random Forests (QRF)** are an extension of random forests that estimate the full conditional distribution of the response variable, not just the mean. Introduced by Meinshausen (2006), QRF enables prediction of arbitrary quantiles, making them ideal for constructing [[concepts/prediction-intervals|prediction intervals]] and [[concepts/uncertainty-quantification|uncertainty quantification]].

## Key Idea

Standard random forests average the predictions of individual trees. QRF instead keeps track of **which training observations fall into each leaf** and uses their distribution to estimate conditional quantiles.

## Algorithm

Given a test point x:

1. **Find leaf memberships**: For each tree T(θₖ), determine which leaf l(x, θₖ) the point x falls into

2. **Compute weights**: For each training observation t:

   w_t(x) = (1/K) Σₖ [1(X_t ∈ leaf l(x, θₖ))] / |{Xᵢ ∈ leaf l(x, θₖ)}|

   This counts how often training point t shares a leaf with x across all trees.

3. **Estimate CDF**: The conditional distribution is estimated as:

   F̂(z|x) = Σₜ wₜ(x) · 1(Yₜ ≤ z)

4. **Compute quantile**: The p-th quantile is:

   Q̂(p) = inf{z : F̂(z|x) ≥ p}

## Advantages Over Direct Quantile Regression

| Aspect | QRF | Pinball Loss Methods |
|--------|-----|---------------------|
| Multiple quantiles | Single model, any quantile | Retrain for each quantile |
| Training | Standard RF training | Specialized loss function |
| Monotonicity | Guaranteed by construction | Not guaranteed (crossing) |
| Efficiency | One training, many quantiles | O(n) trainings for n quantiles |

## Application in SPCI

In [[concepts/spci|SPCI]] ([[sources/xu-2022-spci]]), QRF is used to predict the quantiles of **future residuals** based on past residuals:

- **Features**: X̃_t = (ε̂_{t-w}, ..., ε̂_{t-1}) (windowed past residuals)
- **Target**: Ỹ_t = ε̂_t (next residual)
- **Output**: Q̂_t(p) estimates the p-th quantile of ε̂_t given recent residual history

This enables SPCI to:
1. Exploit temporal correlation in residuals
2. Produce adaptive prediction intervals
3. Achieve asymptotic conditional coverage

## Theoretical Properties

From Meinshausen (2006) and extended in SPCI:

**For i.i.d. data**:
- QRF estimates converge to true conditional quantiles
- Consistency requires regularity conditions on the conditional distribution

**For dependent data** (SPCI Theorem 2):
- Under weak stationarity and decaying dependence assumptions
- Point-wise convergence of F̂(z|x) → F(z|x)
- Implies quantile convergence Q̂(p) → Q(p)

## Key Assumptions (SPCI)

1. **Weak stationarity of residual dependence**: Covariance depends only on lag
2. **Decaying dependence**: Correlation decays sufficiently fast with lag
3. **Weight decay**: QRF weights are O(1/T̃)
4. **Lipschitz continuity**: Conditional distribution is smooth

## Implementation

Python packages:
- `sklearn-quantile` (used in SPCI)
- `quantile-forest`
- `scikit-garden` (deprecated)

```python
from sklearn_quantile import RandomForestQuantileRegressor

qrf = RandomForestQuantileRegressor()
qrf.fit(X_train, y_train)
q_lower = qrf.predict(X_test, quantiles=0.05)
q_upper = qrf.predict(X_test, quantiles=0.95)
```

## Limitations

- **Computational cost**: Must store training data for inference
- **Extrapolation**: Like all tree methods, struggles outside training range
- **Small samples**: May not capture tail quantiles well

## See Also

- [[concepts/spci|SPCI]] - Uses QRF for sequential conformal prediction
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/uncertainty-quantification|Uncertainty Quantification]]
