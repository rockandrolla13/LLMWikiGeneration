---
created: 2026-04-10 18:00:00+00:00
mind_map_priority: medium
page_id: concepts/prediction-intervals
page_type: concept
related:
- concepts/calibration
- concepts/conformal-prediction
- concepts/coverage-guarantee
- concepts/interval-score
- concepts/uncertainty-quantification
revision_id: 2
sources:
- sources/zaffran-phd
- sources/zaffran-2022-aci
- sources/johnstone-2025-multioutput
tags:
- uncertainty-quantification
- regression
- forecasting
title: Prediction Intervals
updated: '2026-06-09T12:00:00Z'
---

# Prediction Intervals

A **prediction interval** is a range of values that is expected to contain a future observation with a specified probability. Unlike confidence intervals (which quantify uncertainty about parameters), prediction intervals quantify uncertainty about individual predictions.

## Definition

For a new observation (Xₙ₊₁, Yₙ₊₁) and coverage level (1-α):

A prediction interval Ĉ(Xₙ₊₁) = [L(Xₙ₊₁), U(Xₙ₊₁)] satisfies:

P{Yₙ₊₁ ∈ Ĉ(Xₙ₊₁)} ≥ 1 - α

## Key Properties

### Validity
The interval achieves the target [[concepts/coverage-guarantee|coverage]].

### Efficiency
The interval should be as narrow as possible while maintaining validity. Efficiency is measured by:
- Average width
- Median width (robust to outliers)

### Adaptivity
For heteroskedastic data, intervals should be wider where uncertainty is higher.

## Construction Methods

### Parametric Methods
- Assume error distribution (e.g., Gaussian)
- Use model-based standard errors
- Valid only asymptotically and under correct model specification

### [[concepts/conformal-prediction|Conformal Prediction]]
- Distribution-free
- Finite-sample valid
- Model-agnostic

### Quantile Regression
- Directly estimate conditional quantiles
- Can be combined with conformal prediction (CQR)

### Bootstrap
- Resample-based uncertainty
- Asymptotic validity

## Applications

- **Electricity price forecasting**: Risk management in energy markets ([[entities/margaux-zaffran|Zaffran's]] PhD work)
- **Medical diagnosis**: Quantifying diagnostic uncertainty
- **Financial forecasting**: Value-at-risk, expected shortfall
- **Demand forecasting**: Inventory management

## Challenges

- **High dimensions**: Prediction sets become complex (see [[sources/johnstone-2025-multioutput|multi-output regression]])
- **Time series**: Exchangeability violations require [[concepts/adaptive-conformal-inference|adaptive methods]]
- **Conditional coverage**: Hard to achieve uniformly across all X

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/uncertainty-quantification|Uncertainty Quantification]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/interval-score|interval-score]]