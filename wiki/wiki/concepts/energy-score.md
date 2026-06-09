---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/energy-score
page_type: concept
related:
- concepts/calibration
- concepts/continuous-ranked-probability-score
- concepts/dawid-sebastiani-score
- concepts/diebold-mariano-test
- concepts/marginal-copula-score
- concepts/ranked-probability-score
- concepts/uncertainty-quantification
- concepts/variogram-score
revision_hash: sha256:5f5aefb9fbd92991ce6009d6a1224c807dd6646f0e13308fa58cbd78d3de5b42
revision_id: 1
sources:
- sources/gneiting-2007-strictly-proper-scoring-rules
- sources/ziel-2019-multivariate-forecasting-evaluation
tags: []
title: Energy Score
updated: '2026-06-09T12:00:00Z'
updated_by: creditmacro-batch
---

# Energy Score

## Definition

A strictly proper score for multivariate forecasts based on expected Euclidean distances raised to a power beta in (0,2); it generalizes the CRPS and admits a kernel representation via negative definite functions.

## Sources

- [[sources/gneiting-2007-strictly-proper-scoring-rules|Strictly Proper Scoring Rules, Prediction, and Estimation]]
- [[sources/ziel-2019-multivariate-forecasting-evaluation|Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper Scoring Rules]]

## Related Concepts

- [[concepts/calibration|calibration]]
- [[concepts/continuous-ranked-probability-score|continuous-ranked-probability-score]]
- [[concepts/dawid-sebastiani-score|dawid-sebastiani-score]]
- [[concepts/diebold-mariano-test|diebold-mariano-test]]
- [[concepts/marginal-copula-score|marginal-copula-score]]
- [[concepts/ranked-probability-score|ranked-probability-score]]
- [[concepts/uncertainty-quantification|uncertainty-quantification]]
- [[concepts/variogram-score|variogram-score]]