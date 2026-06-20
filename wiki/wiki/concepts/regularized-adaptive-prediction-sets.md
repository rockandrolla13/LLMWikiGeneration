---
title: Regularized Adaptive Prediction Sets (RAPS)
page_id: concepts/regularized-adaptive-prediction-sets
page_type: concept
revision_id: 2
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- classification
- score-design
- regularisation
- large-class
sources:
- sources/angelopoulos-2021-raps
- sources/angelopoulos-2022-gentle-intro
related:
- concepts/conformal-prediction
- concepts/adaptive-prediction-sets
- concepts/split-conformal-prediction
- concepts/nonconformity-score
mind_map_priority: medium
schema_version: 2
uuid: 0fbf9383-0be1-5f7a-ba68-0e5470d7b790
content_hash: sha256:4d5ed5c0a64945917780a8d473761213bd54288055f2ad0a5e9476c4f4a84155
---

<!-- AUTHORED REGION START -->
# Regularized Adaptive Prediction Sets (RAPS)

## Primary Source

Primary source: [[sources/angelopoulos-2021-raps|Angelopoulos, Bates, Malik & Jordan (2021), "Uncertainty Sets for Image Classifiers using Conformal Prediction"]] (ICLR 2021). This paper introduces the RAPS score — APS plus a rank-penalty term — and demonstrates large reductions in median set size on ImageNet while retaining marginal coverage, which is the construction this concept page formalises.

**RAPS** (Angelopoulos, Bates, Malik, Jordan, 2021) is a regularised variant of [[concepts/adaptive-prediction-sets|APS]] that **penalises inclusion of low-ranked classes** to shrink prediction sets in large-class problems (e.g., ImageNet's 1000 classes) while retaining marginal coverage.

## The RAPS Score

Given sorted softmax probabilities and a target label `y` ranked at position `r_y(x)`, the RAPS [[concepts/nonconformity-score|score]] is:

```
s_RAPS(x, y) = s_APS(x, y) + λ · max(0, r_y(x) − k_reg)
```

where:
- `λ ≥ 0` is the regularisation strength,
- `k_reg ∈ {1, 2, ...}` is the rank below which no penalty is applied.

The penalty makes it costly to include classes ranked beyond `k_reg`, encouraging smaller sets in the high-ambiguity regime where APS otherwise accumulates a long tail.

## Trade-off

- `λ = 0` → recovers vanilla [[concepts/adaptive-prediction-sets|APS]].
- Large `λ` → recovers near-singleton "top-1" sets but loses adaptivity.
- Practical tuning: pick `λ, k_reg` on a validation split to minimise *size* while preserving validity (validity is automatic).

## Empirical Effect

On ImageNet, RAPS reduces median prediction-set size from ~10 (APS) to ~2 at the same coverage level, while improving size-stratified [[concepts/conditional-coverage|conditional coverage]] metrics.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — original RAPS construction with experiments.

## Related Concepts

- [[concepts/adaptive-prediction-sets]]
- [[concepts/nonconformity-score]]
- [[concepts/conditional-coverage]]

<!-- AUTHORED REGION END -->
