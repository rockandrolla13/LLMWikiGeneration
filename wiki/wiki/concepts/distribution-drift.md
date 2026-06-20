---
title: Distribution Drift
page_id: concepts/distribution-drift
page_type: concept
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- machine-learning
- time-series
- non-stationarity
- model-monitoring
sources:
- sources/farinhas-2024-non-exchangeable-crc
- sources/huyen-2022-designing-ml-systems
- sources/zaffran-2022-aci
related:
- concepts/exchangeability
- concepts/conformal-prediction
- concepts/adaptive-conformal-inference
- concepts/conformal-risk-control
mind_map_priority: medium
updated_by: wiki-batch-ai-engineering-2026-05-17
schema_version: 2
uuid: 8d3dac69-b457-55db-9969-492f4740f3a5
content_hash: sha256:bd43cc36d350494ca9f21458a2bc146689c479bf0241e8201a388a397d327a84
---

<!-- AUTHORED REGION START -->
# Distribution Drift

**Distribution drift** (also called concept drift or data drift) occurs when the statistical properties of data change over time, violating the common assumption that training and test data come from the same distribution.

## Types of Distribution Drift

### Covariate Shift

P(X) changes while P(Y|X) remains constant.

Example: A model trained on daytime images deployed at night.

### Label Shift

P(Y) changes while P(X|Y) remains constant.

Example: Disease prevalence changes seasonally.

### Concept Drift

P(Y|X) changes - the relationship between features and target evolves.

Example: Customer preferences change over time.

### Full Distribution Shift

Both P(X) and P(Y|X) change arbitrarily.

## Impact on Conformal Prediction

Standard [[concepts/conformal-prediction|conformal prediction]] assumes **exchangeability**:

P((X_π(1), Y_π(1)), ..., (X_π(n), Y_π(n))) = P((X_1, Y_1), ..., (X_n, Y_n))

Distribution drift violates exchangeability, causing:
- **Invalid coverage guarantees**
- **Miscalibrated prediction intervals**
- **Systematic under- or over-coverage**

## Measuring Drift

### Total Variation Distance

d_TV(P, Q) = (1/2) ∫ |p(x) - q(x)| dx

Used in [[sources/farinhas-2024-non-exchangeable-crc|non-exchangeable CRC]] to bound coverage degradation.

### KL Divergence

D_KL(P || Q) = ∫ p(x) log(p(x)/q(x)) dx

Related to TV distance via Pinsker's inequality.

### Kolmogorov-Smirnov Test

Tests whether two samples come from same distribution.

## Handling Drift in Conformal Prediction

### Adaptive Conformal Inference (ACI)

[[concepts/adaptive-conformal-inference|ACI]] and [[sources/zaffran-2022-aci|AgACI]] adaptively adjust the miscoverage level:

α_{t+1} = α_t + γ(α - 1{Y_t ∉ C_t})

Learning rate γ controls adaptation speed.

### Non-Exchangeable Conformal Prediction

Barber et al. (2023) provided coverage bounds accounting for drift:

P(Y_{n+1} ∈ C(X_{n+1})) ≥ 1 - α - ∑_i w̃_i d_TV(Z, Z^i)

### Non-Exchangeable Conformal Risk Control

[[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] extended this to arbitrary loss functions:

E[L(λ̂; (X_{n+1}, Y_{n+1}))] ≤ α + (B-A) ∑_i w̃_i d_TV(Z, Z^i)

### Weight Selection Strategies

For time series with bounded drift d_TV(Z_i, Z_{n+1}) ≤ ε(n+1-i):

**Exponential decay weights**: w_i = ρ^{n+1-i} where ρ = exp(-βε)

This places higher weight on recent, more relevant observations.

## Practical Examples

### Time Series Forecasting

- Electricity prices exhibit daily, weekly, seasonal patterns
- Economic shocks create sudden distribution changes
- [[sources/zaffran-2022-aci|AgACI]] addresses this with adaptive calibration

### Question Answering

- Topics of questions evolve over time
- [[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] use embedding similarity for weighting

### Medical Data

- Disease prevalence changes seasonally
- New treatments alter patient outcomes
- Drift-aware methods essential for reliable predictions

## Detection Methods

1. **Statistical tests**: Compare distributions of features/predictions
2. **Model performance monitoring**: Track calibration metrics
3. **Residual analysis**: Monitor prediction errors over time

## Key Assumptions for Theory

### Lipschitz-Type Condition

d_TV(Z_i, Z_{n+1}) ≤ ε(n+1-i)

Drift is bounded and grows linearly with time distance.

### Independent but Not Identical

Variables are independent but from different distributions:

d_TV(Z, Z^i) ≤ 2 d_TV(Z_i, Z_{n+1})

## Key References

- Barber et al. (2023) - Non-exchangeable conformal prediction
- [[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] - Non-exchangeable CRC
- [[sources/zaffran-2022-aci|Zaffran et al. (2022)]] - Adaptive conformal inference
- Gibbs & Candès (2021, 2022) - Online conformal prediction

## See Also

- [[concepts/exchangeability|Exchangeability]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/conformal-risk-control|Conformal Risk Control]]

## See Also (AI Engineering batch)
<!-- wiki-batch-ai-engineering-2026-05-17 -->
- [[sources/huyen-2022-designing-ml-systems|huyen-2022-designing-ml-systems]]

<!-- AUTHORED REGION END -->
