---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/continuous-ranked-probability-score
page_type: concept
related:
- concepts/calibration
- concepts/energy-score
- concepts/ranked-probability-score
- concepts/uncertainty-quantification
revision_hash: sha256:6667e58a91eeb4abaecf7fbb9ae64b400372819e3edd4a859522e1e509aa6ec1
revision_id: 1
sources:
- sources/gneiting-2007-strictly-proper-scoring-rules
tags: []
title: Continuous Ranked Probability Score (CRPS)
updated: '2026-06-09T12:00:00Z'
updated_by: creditmacro-batch
---

# Continuous Ranked Probability Score (CRPS)

## Definition

A strictly proper score for predictive CDFs equal to the integral of Brier scores over all thresholds; it generalizes absolute error and reduces to it for deterministic forecasts.

## Sources

- [[sources/gneiting-2007-strictly-proper-scoring-rules|Strictly Proper Scoring Rules, Prediction, and Estimation]]

## Related Concepts

- [[concepts/calibration|calibration]]
- [[concepts/energy-score|energy-score]]
- [[concepts/ranked-probability-score|ranked-probability-score]]
- [[concepts/uncertainty-quantification|uncertainty-quantification]]