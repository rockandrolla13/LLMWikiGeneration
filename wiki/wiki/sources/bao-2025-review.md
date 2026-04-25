---
title: "A Review and Comparative Analysis of Univariate Conformal Regression Methods"
page_id: sources/bao-2025-review
page_type: source
source_type: paper
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
authors: [Jie Bao, Nicolo Colombo, Valery Manokhin, Suqun Cao, Rui Luo]
year: 2025
venue: "Proceedings of Machine Learning Research 266:1-23 (COPA)"
tags: [conformal-prediction, regression, survey, benchmark]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/prediction-intervals]
mind_map_priority: medium
---

# Review of Univariate Conformal Regression Methods

**Authors:** Jie Bao, Nicolo Colombo, Valery Manokhin, Suqun Cao, Rui Luo

**Year:** 2025

**Venue:** Conformal and Probabilistic Prediction and Applications (COPA)

## Summary

A comprehensive survey and comparative analysis of state-of-the-art [[concepts/conformal-prediction|conformal regression]] methods, providing both theoretical overview and empirical benchmarking.

## Key Contributions

1. **Categorization** of existing conformal regression techniques
2. **Detailed examination** of 8 leading methods
3. **Simulation experiments** visualizing prediction interval differences
4. **Benchmarking** on 12 real-world datasets

## Methods Reviewed

The paper examines and compares:
- [[concepts/split-conformal-prediction|Split Conformal Prediction]]
- Conformal Quantile Regression (CQR)
- Conformal Histogram Regression
- Conformal Thresholded Intervals
- And 4 additional methods

## Key Findings

- Different methods excel in different scenarios
- CQR is effective for heteroskedastic data
- Trade-offs between computational cost and interval quality

## Value

This paper serves as an excellent entry point for practitioners choosing among conformal regression methods, providing:
- Unified notation and framework
- Head-to-head comparisons
- Practical guidance

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/split-conformal-prediction|Split Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
