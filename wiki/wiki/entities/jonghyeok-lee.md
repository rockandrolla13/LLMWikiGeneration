---
title: Jonghyeok Lee
page_id: entities/jonghyeok-lee
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- researcher
- conformal-prediction
- time-series
- kernel-methods
- machine-learning
sources:
- sources/lee-2024-kowcpi
related:
- concepts/conformal-prediction
- concepts/kowcpi
- concepts/nadaraya-watson-estimator
- entities/yao-xie
- entities/chen-xu
mind_map_priority: low
schema_version: 2
uuid: d0964a56-bccd-5ef4-8fb8-ee8a06836933
content_hash: sha256:b4e7bca5c6dc17117f00ba70fcbf65838c00c1647fc8335bfa2599b5eca1c137
---

<!-- AUTHORED REGION START -->
# Jonghyeok Lee

**Jonghyeok Lee** is a researcher at the H. Milton Stewart School of Industrial and Systems Engineering, Georgia Institute of Technology, working on [[concepts/conformal-prediction|conformal prediction]] methods for time-series data.

## Affiliation

- Georgia Institute of Technology, H. Milton Stewart School of Industrial and Systems Engineering

## Key Contributions

### KOWCPI Method
[[sources/lee-2024-kowcpi|Lee, Xu, and Xie (2024)]] introduced [[concepts/kowcpi|KOWCPI]] (Kernel-based Optimally Weighted Conformal Prediction Intervals), a novel method that:
- Adapts the [[concepts/nadaraya-watson-estimator|Reweighted Nadaraya-Watson]] estimator for quantile regression on non-conformity scores
- Learns optimal data-driven weights for handling non-exchangeable time-series data
- Achieves asymptotic conditional [[concepts/coverage-guarantee|coverage]] under strong mixing conditions
- Demonstrates superior performance with narrower prediction intervals than existing methods

## Publications in This Wiki

- [[sources/lee-2024-kowcpi|Kernel-based Optimally Weighted Conformal Prediction Intervals (2024)]]

## Collaborators

- [[entities/chen-xu|Chen Xu]] (Georgia Tech)
- [[entities/yao-xie|Yao Xie]] (Georgia Tech)

## See Also

- [[concepts/kowcpi|KOWCPI Method]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/nadaraya-watson-estimator|Nadaraya-Watson Estimator]]

<!-- AUTHORED REGION END -->
