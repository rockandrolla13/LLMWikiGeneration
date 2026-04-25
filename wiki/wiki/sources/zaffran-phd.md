---
title: "Post-hoc predictive uncertainty quantification: methods with applications to electricity price forecasting"
page_id: sources/zaffran-phd
page_type: source
source_type: thesis
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
authors: [Margaux Zaffran]
year: 2024
venue: PhD Thesis, Institut Polytechnique de Paris
tags: [conformal-prediction, uncertainty-quantification, electricity-forecasting, missing-data, time-series]
related: [sources/zaffran-2022-aci, concepts/conformal-prediction, concepts/adaptive-conformal-inference, concepts/split-conformal-prediction, entities/margaux-zaffran]
mind_map_priority: high
---

# Post-hoc predictive uncertainty quantification

**Author:** [[entities/margaux-zaffran|Margaux Zaffran]]

**Year:** 2024

**Type:** PhD Thesis, Institut Polytechnique de Paris / École Polytechnique

**Supervisors:** Julie Josse (INRIA), Aymeric Dieuleveut (École Polytechnique)

## Summary

This thesis develops methods for constructing [[concepts/prediction-intervals|prediction intervals]] for any prediction model (including neural networks) without distributional assumptions, with applications to electricity price forecasting.

## Motivation

- Renewable energy → volatile electricity markets
- Accurate forecasting needed for production planning
- ML models provide no uncertainty quantification
- Decision-makers need calibrated confidence

## Key Contributions

### 1. ACI Analysis and AgACI
- Analyzed influence of learning rate γ on [[concepts/adaptive-conformal-inference|ACI]] efficiency
- Proposed AgACI: parameter-free method using online expert aggregation
- Demonstrated improvements on French electricity prices

### 2. Impact of Non-stationarity
- Studied electricity price explosion of 2021
- Compared adaptive post-hoc layers (SCP, online aggregation)
- Found adaptive methods handle distribution shift better

### 3. Conformal Prediction with Missing Data
**Major theoretical contribution:**
- Proved [[concepts/split-conformal-prediction|SCP]] on imputed data maintains validity guarantees
- Works with ANY imputation method, even naive ones
- Valid even for informative missingness (MNAR)

### 4. Heteroskedasticity from Missing Values
- Identified that NAs generate heteroskedasticity
- Proposed first algorithms to address conditional coverage with missingness
- Assumptions are nearly minimal per hardness results

## Structure

1. Introduction to electricity markets and forecasting
2. [[concepts/conformal-prediction|Conformal prediction]] background
3. [[concepts/adaptive-conformal-inference|ACI]] for time series
4. Missing data and conformal prediction
5. Conditional coverage with missing values
6. Applications to electricity forecasting

## Impact

The thesis establishes that:
- Conformal methods can be safely applied to imputed data
- Adaptive methods extend CP to non-exchangeable settings
- Practical uncertainty quantification for energy sector is achievable

## See Also

- [[sources/zaffran-2022-aci|Zaffran et al. 2022 (ACI paper)]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
