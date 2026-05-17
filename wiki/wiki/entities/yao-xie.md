---
title: Yao Xie
page_id: entities/yao-xie
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [researcher, conformal-prediction, time-series, georgia-tech, professor, kernel-methods]
affiliation: Georgia Institute of Technology
email: yao.xie@isye.gatech.edu
sources: [sources/lee-2024-kowcpi]
related: [entities/chen-xu, entities/jonghyeok-lee, concepts/conformal-prediction, concepts/spci, concepts/kowcpi, concepts/nadaraya-watson-estimator]
mind_map_priority: medium
---

# Yao Xie

**Yao Xie** is a faculty member at the H. Milton Stewart School of Industrial and Systems Engineering at Georgia Institute of Technology. Her research focuses on sequential analysis, change-point detection, and uncertainty quantification for machine learning, with significant contributions to [[concepts/conformal-prediction|conformal prediction]] for time series.

## Research Contributions

### Conformal Prediction for Time Series
- **KOWCPI** ([[sources/lee-2024-kowcpi|Lee, Xu & Xie, 2024]]) - Kernel-based Optimally Weighted Conformal Prediction Intervals using [[concepts/nadaraya-watson-estimator|Reweighted Nadaraya-Watson]] estimator
- **EnbPI** (Xu & Xie, 2021b) - Conformal prediction intervals for dynamic time series using ensemble methods
- **SPCI** ([[sources/xu-2022-spci]]) - Sequential Predictive Conformal Inference that exploits temporal dependencies in residuals
- **Conformal Anomaly Detection** (Xu & Xie, 2021a) - Spatiotemporal applications with missing data

### Key Research Themes
1. Distribution-free uncertainty quantification
2. Sequential change-point detection
3. Time series analysis and prediction
4. Energy systems forecasting (wind, solar)

## Academic Impact

From the SPCI paper, her work addresses fundamental challenges:
- "Conformal prediction for time series has been a challenging case because such data do not satisfy the exchangeability assumption"
- "We specifically exploited the feedback structure in designing sequential conformal prediction algorithms"

## Collaborators

- [[entities/chen-xu|Chen Xu]] - Primary collaborator on SPCI and EnbPI
- [[entities/jonghyeok-lee|Jonghyeok Lee]] - KOWCPI development
- Shu Zhu - Multi-resolution spatiotemporal prediction (wind power)

## Related Research Groups

Xie's work connects to several active research communities:
- [[entities/emmanuel-candes|Emmanuel Candès]] - ACI methodology
- [[entities/vladimir-vovk|Vladimir Vovk]] - Foundational conformal prediction theory
- Rina Barber - NEX-CP for non-exchangeable data

## Research Applications

Her methods have been applied to:
- Solar power radiation prediction
- Wind speed forecasting
- Electricity load forecasting
- Stock market return prediction

## Related Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/spci|SPCI]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
