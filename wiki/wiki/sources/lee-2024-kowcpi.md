---
title: Kernel-based Optimally Weighted Conformal Prediction Intervals
page_id: sources/lee-2024-kowcpi
page_type: source
revision_id: 1
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- kernel-methods
- uncertainty-quantification
- nonparametric-statistics
authors:
- Jonghyeok Lee
- Chen Xu
- Yao Xie
year: 2024
sources: []
related:
- concepts/conformal-prediction
- concepts/adaptive-conformal-inference
- concepts/coverage-guarantee
- concepts/kowcpi
- concepts/nadaraya-watson-estimator
- entities/yao-xie
mind_map_priority: high
schema_version: 2
uuid: 500e1da0-350e-53fb-9cbf-0b429ee0f020
content_hash: sha256:7f3c5f7375181775e5d31d52dfbed13a04fd19d1e9e350fcb869457c127bf945
---

<!-- AUTHORED REGION START -->
# Kernel-based Optimally Weighted Conformal Prediction Intervals

**Lee, Xu, and Xie (2024)** propose KOWCPI, a novel conformal prediction method for time-series data that learns optimal data-adaptive weights using the Reweighted Nadaraya-Watson (RNW) estimator for quantile regression on non-conformity scores.

## Key Contribution

The paper addresses the challenge of constructing valid prediction intervals for non-exchangeable time-series data by:
1. Adapting the classic [[concepts/nadaraya-watson-estimator|Reweighted Nadaraya-Watson]] estimator for quantile regression on dependent data
2. Learning optimal data-dependent weights in a data-driven manner
3. Establishing conditional coverage guarantees under strong mixing conditions

## Methodology

### Problem Setup
- Sequential observations $(X_t, Y_t)$ where data is non-exchangeable with temporal dependencies
- Given a pre-trained point predictor $\hat{f}$, construct prediction intervals with significance level $\alpha$
- Target both marginal and conditional [[concepts/coverage-guarantee|coverage]]

### KOWCPI Algorithm
The method uses a sliding window approach on non-conformity scores $\hat{\varepsilon}_t = Y_t - \hat{f}(X_t)$:
1. Break past $T$ residuals into $n = (T - w)$ overlapping segments of length $w$
2. Fit RNW estimator to these segments for quantile regression
3. Compute optimal adjustment weights by maximizing empirical log-likelihood
4. Construct asymmetric prediction intervals using the fitted conditional quantiles

### RNW Estimator
The Reweighted Nadaraya-Watson estimator introduces adjustment weights $p_i(\tilde{X})$ that:
- Maximize the empirical log-likelihood subject to normalization and moment constraints
- Combine favorable bias properties of local linear estimators
- Produce consistent estimates under strongly mixing conditions

## Theoretical Results

### Marginal Coverage Bound
The marginal coverage gap depends on the $\ell_1$-distance between learned optimal weights and oracle-optimal weights (Proposition 4.1).

### Conditional Coverage
Under strong mixing assumptions (Assumption 4.2), the method achieves **asymptotic conditional coverage**:
$$\mathbb{P}\{Y_t \in \hat{C}_{t-1}^{(\alpha)}(X_t) | X_t\} \geq 1 - \alpha \text{ as } n \to \infty$$

### Key Assumptions
1. **Strong mixing**: The residual process is strongly mixing with coefficient $\alpha(\tau) = O(\tau^{-(2+\delta)})$
2. **Smoothness**: Conditional CDF is twice continuously differentiable
3. **Kernel regularity**: Nonnegative, bounded, compactly supported kernel function

## Practical Considerations

### Bandwidth Selection
- Uses nonparametric AIC (Cai & Tiwari, 2000) rather than cross-validation
- Optimal bandwidth $h^* \sim n^{-1/(w+4)}$ minimizes asymptotic mean squared error

### Window Length Selection
- Can use cross-validation to select $w$
- Performance generally less sensitive to $w$ than to bandwidth $h$
- Adaptive window selection approach available (Appendix E)

## Experimental Results

The paper demonstrates superior performance on real and synthetic time-series data:
- **Narrower prediction intervals** compared to state-of-the-art methods
- **Maintained coverage** at target levels
- Tested against ACI ([[entities/margaux-zaffran|Zaffran]] et al.), EnbPI, and other baselines

## Relation to Existing Work

### Weighted Conformal Prediction
- Addresses the weight selection issue in [[sources/barber-2023-conformal-nonexchangeable|Barber et al. (2023)]]
- Provides data-driven weights without prior knowledge

### Time-Series Conformal Prediction
- Extends sequential predictive approaches (Xu & Xie, 2023a,b)
- Relates to [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]] methods

## Applications

The method is applicable to:
- Financial market forecasting
- Anomaly detection in time series
- Any domain with non-exchangeable sequential data

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/kowcpi|KOWCPI Method]]
- [[concepts/nadaraya-watson-estimator|Nadaraya-Watson Estimator]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]

<!-- AUTHORED REGION END -->
