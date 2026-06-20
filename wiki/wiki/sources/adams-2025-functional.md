---
title: Conformal Anomaly Detection for Functional Data with Elastic Distance Metrics
page_id: sources/adams-2025-functional
page_type: source
source_type: paper
revision_id: 1
created: 2026-04-10 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Jason Adams
- Brandon Berman
- Joshua Michalenko
- J. Derek Tucker
year: 2025
venue: Proceedings of Machine Learning Research 266:1-21 (COPA)
tags:
- conformal-prediction
- anomaly-detection
- functional-data-analysis
related:
- concepts/conformal-prediction
mind_map_priority: low
schema_version: 2
uuid: f2435ec5-b9a7-5295-9d03-3f36dd5eaafb
content_hash: sha256:fecdbc776cec15854605a5c4a2e144d1b0c384cd8c3d4a419c35685929eb1b3a
---

<!-- AUTHORED REGION START -->
# Conformal Anomaly Detection for Functional Data

**Authors:** Jason Adams, Brandon Berman, Joshua Michalenko, J. Derek Tucker (Sandia National Laboratories)

**Year:** 2025

**Venue:** Conformal and Probabilistic Prediction and Applications (COPA)

## Summary

This paper introduces a method for outlier detection in functional data using [[concepts/conformal-prediction|conformal prediction]] with elastic functional distance metrics, particularly effective for detecting shape outliers.

## Key Contributions

1. **Inductive conformal anomaly detection** for functional data
2. **Elastic distance metrics** that handle both magnitude and shape outliers
3. Comparison with existing functional outlier detection methods

## Background

Functional data vary continuously over an independent variable. Outliers in functional data can be:
- **Magnitude outliers**: Lie outside the range of most data
- **Shape outliers**: Within range but have different shape (harder to detect)

## Method

Combines:
- Conformal prediction framework (Vovk et al., 2005)
- Elastic functional data analysis (EFDA) framework
- Non-conformity scores based on elastic distances

## Applications

- Time series anomaly detection
- Quality control in manufacturing
- Signal processing

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]

<!-- AUTHORED REGION END -->
