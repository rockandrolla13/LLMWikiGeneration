---
title: Olivier C. Pasche
page_id: entities/olivier-pasche
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- researcher
- conformal-prediction
- extreme-value-theory
- flood-risk
- machine-learning
sources:
- sources/pasche-2025-extreme-conformal
related:
- concepts/conformal-prediction
- concepts/extreme-value-theory
- concepts/generalized-pareto-distribution
- entities/sebastian-engelke
- entities/henry-lam
mind_map_priority: medium
schema_version: 2
uuid: 4edd0806-3471-52df-9067-9e6b986848fa
content_hash: sha256:789d61a6fa8156fe2a128984310a4625a99ed65039464cdb622295d36c47b5b8
---

<!-- AUTHORED REGION START -->
# Olivier C. Pasche

**Olivier C. Pasche** is a researcher specializing in [[concepts/conformal-prediction|conformal prediction]] and [[concepts/extreme-value-theory|extreme value theory]], with applications to flood risk forecasting and high-impact event prediction.

## Affiliations

- Research Institute for Statistics and Information Science, University of Geneva, Switzerland
- Department of Industrial Engineering and Operations Research, Columbia University, New York, USA (visiting scholar)

## Research Focus

Pasche's research bridges extreme value statistics and machine learning to develop reliable prediction methods for high-impact events. His work addresses the challenge of constructing prediction intervals with very high confidence levels beyond what classical methods can achieve.

## Key Contributions

### Extreme Conformal Prediction
[[sources/pasche-2025-extreme-conformal|Pasche, Lam, and Engelke (2025)]] developed extreme conformal prediction, which:
- Uses [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution]] to extrapolate calibration score quantiles
- Provides valid prediction intervals at extreme confidence levels (e.g., 99.99%)
- Includes weighted extensions for nonstationary data (e.g., seasonal patterns)

### Extreme Quantile Regression Neural Networks (EQRN)
Pasche developed EQRN (Pasche & Engelke, 2024), a neural network-based method for extreme quantile regression that combines deep learning with extreme value theory.

### Flood Risk Forecasting
Applied extreme conformal prediction to one-day-ahead forecasting of the Aare river discharge in Bern, Switzerland, demonstrating practical utility for environmental risk assessment.

## Software

- `ExtremeConformal`: R package implementing extreme conformal prediction
- `ExtremeCI`: R package for profile-likelihood confidence intervals for extreme quantiles
- Reproducibility repository: `github.com/opasche/Reprod_ExtremeConformalPred`

## Publications in This Wiki

- [[sources/pasche-2025-extreme-conformal|Extreme Conformal Prediction: Reliable Intervals for High-Impact Events (2025)]]

## Collaborators

- [[entities/sebastian-engelke|Sebastian Engelke]] (University of Geneva)
- [[entities/henry-lam|Henry Lam]] (Columbia University)

## Funding

Supported by Swiss National Science Foundation Eccellenza Grant 186858.

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/extreme-value-theory|Extreme Value Theory]]
- [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution]]

<!-- AUTHORED REGION END -->
