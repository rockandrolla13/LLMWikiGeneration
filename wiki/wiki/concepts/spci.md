---
title: Sequential Predictive Conformal Inference (SPCI)
page_id: concepts/spci
page_type: concept
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [conformal-prediction, time-series, quantile-regression, adaptive]
sources: [sources/xu-2022-spci]
related: [concepts/conformal-prediction, concepts/adaptive-conformal-inference, concepts/quantile-random-forest, concepts/prediction-intervals, concepts/exchangeability]
mind_map_priority: high
---

# Sequential Predictive Conformal Inference (SPCI)

**Sequential Predictive Conformal Inference (SPCI)** is a distribution-free conformal prediction algorithm for time series that constructs prediction intervals by explicitly modeling the temporal dependence among prediction residuals. Introduced by [[entities/chen-xu|Chen Xu]] and [[entities/yao-xie|Yao Xie]] ([[sources/xu-2022-spci]]), SPCI addresses the fundamental challenge that time series violate the [[concepts/exchangeability|exchangeability]] assumption required by traditional [[concepts/conformal-prediction|conformal prediction]].

## Core Idea

Unlike methods that use empirical quantiles of residuals (e.g., EnbPI), SPCI casts interval construction as a **prediction problem**: given past residuals, predict the quantile of the future residual. This is achieved using [[concepts/quantile-random-forest|quantile random forests]] trained auto-regressively on windowed residuals.

## Why It Works

The key insight is that prediction residuals in time series are often **serially correlated**. For example, if recent predictions have been underestimating, the next prediction is also likely to underestimate. SPCI exploits this correlation to produce:
- **Narrower intervals** (more efficient)
- **Better conditional coverage** (adapts to local data characteristics)

## Algorithm

```
Input: Training data, prediction algorithm A, significance level α
Output: Prediction intervals C^α_{t-1}(X_t) for t > T

1. Train point predictor f̂ and compute residuals ε̂ on training data
2. For t > T:
   a. Train quantile random forest Q̂_t on windowed past residuals
   b. Compute Q̂_t(α/2) and Q̂_t(1-α/2) using features (ε̂_{t-w},...,ε̂_{t-1})
   c. Construct interval: [f̂(X_t) + Q̂_t(β̂), f̂(X_t) + Q̂_t(1-β̂)]
      where β̂ minimizes interval width
   d. Observe Y_t, compute new residual ε̂_t
   e. Update residual window (slide forward)
```

## Mathematical Formulation

Given residuals with conditional distribution F(z|E_t^w) where E_t^w = {ε̂_{t-1},...,ε̂_{t-w}}, the true conditional quantile is:

Q_t(p) = inf{z ∈ ℝ : F(z|E_t^w) ≥ p}

SPCI estimates Q̂_t(p) using quantile random forests and constructs:

C^α_{t-1}(X_t) = [f̂(X_t) + Q̂_t(β̂), f̂(X_t) + Q̂_t(1-β̂)]

## Theoretical Guarantees

### Under Exchangeability (Proposition 1)
When data are exchangeable, SPCI achieves exact finite-sample marginal coverage:

P{Y_t ∈ C^α_{t-1}(X_t)} ≥ 1 - α

### Beyond Exchangeability (Theorem 2)
Under weak stationarity and decaying dependence assumptions:

lim_{T→∞} P{Y_t ∈ C^α_{t-1}(X_t) | E_t^w} = 1 - α

This provides **asymptotic conditional coverage** for dependent data.

## Comparison with Related Methods

| Method | Quantile Estimation | Adaptivity | Coverage Type |
|--------|---------------------|------------|---------------|
| Split Conformal | Empirical (fixed) | None | Marginal |
| EnbPI | Empirical (updated) | Low | Marginal |
| AdaptCI | Empirical (α adjusted) | α-adaptive | Marginal |
| NEX-CP | Weighted empirical | Fixed weights | Marginal |
| **SPCI** | QRF (predictive) | Data-adaptive | Conditional |

## Advantages

1. **Leverages temporal structure**: Uses serial correlation rather than treating it as nuisance
2. **Data-adaptive weights**: Learns optimal weighting of past residuals (connection to NEX-CP)
3. **Narrower intervals**: Often 50%+ reduction in width compared to EnbPI
4. **Model-agnostic**: Works with any point prediction model

## Limitations

- **Scalar outputs only**: Not directly applicable to multivariate time series
- **Computational cost**: QRF retraining at each step
- **Multi-step extension**: Approximate divide-and-conquer approach doesn't capture joint distribution

## Applications

- Solar power forecasting
- Wind speed prediction
- Electricity demand forecasting
- Financial time series

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]] - Parent framework
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]] - Alternative for distribution shift
- [[concepts/quantile-random-forest|Quantile Random Forests]] - Core estimation method
- [[sources/sun-2022-copula-cpts|CopulaCPTS]] - Alternative for multi-step multivariate forecasting
