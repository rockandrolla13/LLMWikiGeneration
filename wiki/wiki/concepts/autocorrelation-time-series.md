---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/autocorrelation-time-series
page_type: concept
related:
- concepts/interrupted-time-series-design
- concepts/segmented-regression
revision_hash: sha256:b052be2f76bf56acb3836e1364bd4450d8a7a3d7d534b4091753ed7dedcc8b1c
revision_id: 1
sources:
- sources/hudson-2019-its-healthcare-reporting
tags: []
title: Autocorrelation in Time Series
updated: '2026-06-09T12:00:00Z'
updated_by: creditmacro-batch
---

# Autocorrelation in Time Series

## Definition

The correlation of observations collected close together in time, which violates independence assumptions and must be tested for (e.g. Durbin-Watson, ACF/PACF, Ljung-Box) and adjusted for (e.g. autoregressive error terms, Prais-Winsten) in time-series analysis.

## Sources

- [[sources/hudson-2019-its-healthcare-reporting|Methodology and reporting characteristics of studies using interrupted time series design in healthcare]]

## Related Concepts

- [[concepts/interrupted-time-series-design|interrupted-time-series-design]]
- [[concepts/segmented-regression|segmented-regression]]