---
title: KOWCPI
page_id: concepts/kowcpi
page_type: concept
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [conformal-prediction, time-series, kernel-methods, uncertainty-quantification, nonparametric-statistics]
sources: [sources/lee-2024-kowcpi]
related: [concepts/conformal-prediction, concepts/nadaraya-watson-estimator, concepts/adaptive-conformal-inference, concepts/coverage-guarantee, concepts/prediction-intervals]
mind_map_priority: medium
---

# KOWCPI

**KOWCPI (Kernel-based Optimally Weighted Conformal Prediction Intervals)** is a [[concepts/conformal-prediction|conformal prediction]] method for time-series data that learns optimal data-adaptive weights using the [[concepts/nadaraya-watson-estimator|Reweighted Nadaraya-Watson (RNW)]] estimator for quantile regression on non-conformity scores.

## Key Innovation

Unlike classical conformal prediction which assumes [[concepts/exchangeability|exchangeability]], KOWCPI handles non-exchangeable time-series data by:
1. Learning data-dependent optimal weights in a data-driven manner
2. Using nonparametric kernel quantile regression on non-conformity scores
3. Providing asymptotic conditional [[concepts/coverage-guarantee|coverage]] guarantees under strong mixing conditions

## Methodology

### Setup
Given sequential observations $(X_t, Y_t)$ and a pre-trained predictor $\hat{f}$:
- Compute non-conformity scores: $\hat{\varepsilon}_t = Y_t - \hat{f}(X_t)$
- Use sliding window of length $w$ to create overlapping segments
- Perform quantile regression using RNW estimator

### Algorithm Steps

1. **Break residuals into segments**: Given past $T$ residuals $\mathcal{E}_{T+1}$, create $n = (T-w)$ overlapping segments of length $w$
2. **Compute adjustment weights**: Solve optimization for $\lambda$ to get $p_i(\tilde{X}_{n+1})$
3. **Calculate final weights**: $\hat{W}_i(\tilde{X}) = \frac{p_i(\tilde{X}) K_h(\tilde{X} - \tilde{X}_i)}{\sum_{j=1}^n p_j(\tilde{X}) K_h(\tilde{X} - \tilde{X}_j)}$
4. **Estimate conditional quantiles**: Using RNW estimator
5. **Construct asymmetric intervals**: Optimize $\beta^*$ for tightest coverage

### Prediction Interval
$$\hat{C}_{t-1}^{(\alpha)}(X_t) = \left[\hat{f}(X_t) + \hat{Q}_{\beta^*}(\tilde{X}_{n+1}), \hat{f}(X_t) + \hat{Q}_{1-\alpha+\beta^*}(\tilde{X}_{n+1})\right]$$

## Theoretical Guarantees

### Marginal Coverage
The marginal coverage gap depends on the $\ell_1$-distance between learned weights and oracle-optimal weights.

### Conditional Coverage
Under strong mixing assumptions ($\alpha(\tau) = O(\tau^{-(2+\delta)})$), KOWCPI achieves asymptotic conditional coverage:
$$\mathbb{P}\{Y_t \in \hat{C}_{t-1}^{(\alpha)}(X_t) | X_t\} \geq 1 - \alpha \text{ as } n \to \infty$$

## Practical Considerations

### Bandwidth Selection
Uses nonparametric AIC (Cai & Tiwari, 2000):
$$\text{AIC}(h) = \log(\text{RSS}/n) + 2 \cdot \text{tr}(SS^{\top})/n$$

### Window Length Selection
- Can use cross-validation
- Performance generally less sensitive to $w$ than bandwidth $h$
- Adaptive selection approach available

## Advantages

1. **Data-driven weights**: No prior knowledge required about data distribution
2. **Narrower intervals**: Achieves tighter intervals than competitors without losing coverage
3. **Conditional coverage**: Stronger guarantee than marginal coverage
4. **Addresses weight selection**: Solves open problem from Barber et al. (2023)

## Comparison with Related Methods

| Method | Exchangeability Required | Conditional Coverage | Data-Driven Weights |
|--------|--------------------------|---------------------|---------------------|
| Classical CP | Yes | No | No |
| [[concepts/adaptive-conformal-inference|ACI]] | No | No | No |
| Weighted CP (Barber et al.) | No | No | Pre-specified |
| **KOWCPI** | No | Yes (asymptotic) | Yes |

## Applications

- Financial market forecasting
- Anomaly detection in time series
- Energy systems prediction (wind, solar)
- Any domain with non-exchangeable sequential data

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/nadaraya-watson-estimator|Nadaraya-Watson Estimator]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/prediction-intervals|Prediction Intervals]]
