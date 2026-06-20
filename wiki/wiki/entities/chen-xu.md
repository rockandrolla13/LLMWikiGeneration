---
title: Chen Xu
page_id: entities/chen-xu
page_type: entity
entity_type: person
revision_id: 2
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- researcher
- conformal-prediction
- time-series
- georgia-tech
affiliation: Georgia Institute of Technology
sources:
- sources/kim-2020-jackknife-plus-after-bootstrap
related:
- entities/yao-xie
- concepts/conformal-prediction
- concepts/spci
mind_map_priority: medium
schema_version: 2
uuid: 0a356db6-be6c-5d4c-a2cc-b83b4468aace
content_hash: sha256:b24500324b5a1fdfa0a6eeffa7f7aa52438a83f07525127dca16c48fa18f09b6
---

<!-- AUTHORED REGION START -->
# Chen Xu

**Chen Xu** is a researcher at the H. Milton Stewart School of Industrial and Systems Engineering at Georgia Institute of Technology. He works on conformal prediction methods for time series and sequential data, with a focus on uncertainty quantification for machine learning models.

## Research Contributions

### Key Works

1. **Sequential Predictive Conformal Inference (SPCI)** - Introduced [[concepts/spci|SPCI]], a method that uses [[concepts/quantile-random-forest|quantile random forests]] to adaptively predict the quantiles of future residuals, exploiting temporal dependencies in time series data [[sources/xu-2022-spci]]

2. **Ensemble Batch Prediction Intervals (EnbPI)** (Xu & Xie, 2021b) - Earlier work on conformal prediction for time series using ensemble methods and leave-one-out predictors

3. **Conformal Anomaly Detection** (Xu & Xie, 2021a) - Applied conformal prediction to spatiotemporal anomaly detection with missing data

## Research Focus

Chen Xu's work centers on:
- Distribution-free uncertainty quantification
- Sequential conformal prediction methods
- Extending conformal prediction beyond [[concepts/exchangeability|exchangeability]] assumptions
- Leveraging temporal structure in prediction residuals

## Collaborations

Frequently collaborates with:
- [[entities/yao-xie|Yao Xie]] - Faculty advisor/collaborator at Georgia Tech

## Key Ideas

From the SPCI paper:
- Prediction residuals in time series are often serially correlated, and this correlation contains information about the uncertainty of future predictions
- Traditional conformal prediction methods that use empirical quantiles ignore this temporal structure
- Quantile regression on residuals provides a principled way to incorporate temporal dependencies

## Related Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/spci|SPCI]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/prediction-intervals|Prediction Intervals]]

<!-- AUTHORED REGION END -->
