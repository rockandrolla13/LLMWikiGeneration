---
title: "Exact and Approximate Conformal Inference for Multi-Output Regression"
page_id: sources/johnstone-2025-multioutput
page_type: source
source_type: paper
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
authors: [Chancellor Johnstone, Eugene Ndiaye]
year: 2025
venue: "Proceedings of Machine Learning Research 266:1-20 (COPA)"
tags: [conformal-prediction, multi-output-regression, multivariate, computational-efficiency]
related: [concepts/conformal-prediction, concepts/prediction-intervals]
mind_map_priority: medium
---

# Exact and Approximate Conformal Inference for Multi-Output Regression

**Authors:** Chancellor Johnstone (GE Aerospace / Air Force Institute of Technology), Eugene Ndiaye (Apple / Georgia Tech)

**Year:** 2025

**Venue:** Conformal and Probabilistic Prediction and Applications (COPA)

## Summary

This paper extends [[concepts/conformal-prediction|conformal prediction]] to multi-output regression settings, providing exact derivations and efficient approximations for prediction regions in high-dimensional response spaces.

## Problem

Standard conformal inference assumes univariate response Y ∈ ℝ. For multi-output regression with Y ∈ ℝᵍ:
- Prediction regions become complex shapes in q dimensions
- Computational cost increases dramatically
- Traditional methods don't scale

## Key Contributions

### 1. Exact p-value Change-Point Sets
For linear predictors ŷ = Hy:
- Conformity scores are affine functions of candidate value z
- Enables exact computation of conformal p-values
- Only requires training the model once

### 2. rootCP Extension (Multivariate)
Extended Ndiaye and Takeuchi (2021)'s root-finding approach:
- Finds boundary points of prediction regions efficiently
- Uses bisection search in each direction
- Complexity: O(dq log₂(1/ε)) for nonlinear models

### 3. unionCP (Approximate)
Union-based conservative approximation:
- Faster than exact methods
- Still provides valid coverage guarantees
- Works with both linear and nonlinear predictors

## Computational Complexity

| Method | Nonlinear Complexity |
|--------|---------------------|
| splitCP | O(q) |
| gridCP | O(rᵍ) |
| rootCP | O(dq log₂(1/ε)) |

## Applications

- Multi-task learning
- Multivariate time series forecasting
- Joint prediction of related outcomes

## Key Insight

> "We only require the predictions be linear functions of the input" - this covers ridge regression, kernel ridge regression, and many practical predictors.

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
