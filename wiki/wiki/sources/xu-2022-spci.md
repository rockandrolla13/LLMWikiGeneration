---
title: Sequential Predictive Conformal Inference for Time Series
page_id: sources/xu-2022-spci
page_type: source
revision_id: 1
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- quantile-regression
- sequential-prediction
authors:
- entities/chen-xu
- entities/yao-xie
publication: ICML 2023 (Proceedings of the 40th International Conference on Machine
  Learning)
year: 2023
related:
- sources/sun-2022-copula-cpts
- sources/zaffran-2022-aci
- concepts/conformal-prediction
- concepts/adaptive-conformal-inference
mind_map_priority: high
schema_version: 2
uuid: 0a05f2e1-9fa5-5975-8d89-071ade50644e
content_hash: sha256:183ad64b9cebb6de7d6d9d26cde366e10ba070ed113fe8715e376a96e974133d
---

<!-- AUTHORED REGION START -->
# Sequential Predictive Conformal Inference for Time Series

## Summary

This paper introduces **Sequential Predictive Conformal Inference (SPCI)**, a distribution-free conformal prediction algorithm specifically designed for time series data. Unlike traditional conformal prediction methods that assume [[concepts/exchangeability|exchangeability]], SPCI explicitly accounts for the non-exchangeable nature of time series by adaptively re-estimating the conditional quantile of non-conformity scores using the temporal dependence among prediction residuals.

## Key Contributions

1. **Adaptive quantile re-estimation**: SPCI uses [[concepts/quantile-random-forest|quantile random forests]] to predict the quantile of future residuals, leveraging serial correlation rather than ignoring it
2. **Asymptotic conditional coverage**: Theoretical guarantees extended to dependent data by adapting QRF consistency analyses
3. **Significantly narrower intervals**: Experiments show major reductions in interval width compared to EnbPI, AdaptCI, and NEX-CP
4. **Multi-step extension**: Algorithm 3 provides a divide-and-conquer approach for multi-step ahead prediction intervals

## Methodology

### Core Insight
The key observation is that prediction residuals in time series are often serially correlated (see Figure 1 in paper - PACF of solar prediction residuals shows significant autocorrelation). SPCI exploits this by treating interval construction as a prediction problem for the quantile of future residuals.

### Algorithm
1. Train a point predictor f̂ and compute prediction residuals on training data
2. For each prediction step t:
   - Fit a [[concepts/quantile-random-forest|quantile random forest]] on windowed past residuals
   - Predict quantiles Q̂_t(α/2) and Q̂_t(1-α/2) for the new residual
   - Construct interval: [f̂(X_t) + Q̂_t(α/2), f̂(X_t) + Q̂_t(1-α/2)]
   - Observe true Y_t and update residual window

### Theoretical Results
- **Proposition 1**: Under [[concepts/exchangeability|exchangeability]], SPCI maintains exact 1-α marginal coverage (same as split conformal)
- **Theorem 2**: Under weak stationarity and decaying dependence (Assumptions 1-4), SPCI achieves asymptotic conditional coverage

## Connection to Other Methods

- **EnbPI** (Xu & Xie, 2021b): SPCI reduces to EnbPI when using empirical quantiles instead of QRF
- **NEX-CP** (Barber et al., 2022): Both use weighted residuals, but SPCI learns data-adaptive weights rather than pre-specified ones
- **AdaptCI** (Gibbs & Candès, 2021): AdaptCI adjusts α dynamically; SPCI adjusts quantile estimates directly

## Experimental Results

| Dataset | Method | Coverage | Width |
|---------|--------|----------|-------|
| Wind | SPCI | 0.95 | **2.65** |
| Wind | EnbPI | 0.93 | 6.38 |
| Solar | SPCI | 0.91 | **47.61** |
| Solar | EnbPI | 0.88 | 48.95 |
| Electric | SPCI | 0.93 | **0.22** |
| Electric | EnbPI | 0.91 | 0.32 |

SPCI consistently achieves the target 90% coverage with substantially narrower intervals.

## Key Claims

- "The main idea is to adaptively re-estimate the conditional quantile of non-conformity scores, upon exploiting the temporal dependence among them"
- "SPCI can obtain significantly narrower intervals on real data without coverage loss"
- "We establish asymptotic valid conditional coverage upon extending consistency analyses in quantile regression"

## Limitations & Future Work

- Currently limited to scalar outputs; multivariate extension is future work
- Multi-step SPCI uses a divide-and-conquer approximation that doesn't capture the full joint distribution
- QRF retraining at each step can be computationally expensive

## Related Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/quantile-random-forest|Quantile Random Forests]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/spci|SPCI]]

## See Also

- [[sources/sun-2022-copula-cpts|CopulaCPTS]] - Alternative approach using copulas for multi-step forecasting
- [[sources/zaffran-2022-aci|Adaptive Conformal Predictions for Time Series]]

<!-- AUTHORED REGION END -->
