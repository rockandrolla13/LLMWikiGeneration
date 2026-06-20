---
title: Conformal Predictive Distribution
page_id: concepts/conformal-predictive-distribution
page_type: concept
revision_id: 1
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- predictive-distribution
- distributional-forecasting
sources:
- sources/angelopoulos-2022-gentle-intro
related:
- concepts/conformal-prediction
- concepts/distributional-conformal-prediction
- concepts/uncertainty-quantification
- concepts/probability-integral-transform
mind_map_priority: medium
schema_version: 2
uuid: a12c7f3b-bdf2-5552-b30e-1a8f321fd50f
content_hash: sha256:d6991d4ef519da5cffab823a584820eb60816a172c9d7a8225b3229da12e8074
---

<!-- AUTHORED REGION START -->
# Conformal Predictive Distribution

A **conformal predictive distribution** (Vovk, Shen, Manokhin, Xie, 2017) is a distribution-free predictive **CDF** over `Y` constructed from conformal p-values — it outputs a full distribution over the response rather than a single prediction set, while inheriting CP's finite-sample validity.

## Construction (Sketch)

Given a calibration set and a candidate `y`, compute the conformal p-value:

```
p(y; x) = (# calibration scores ≤ s(x, y)) / (n + 1)
```

The function `y ↦ p(y; x)` is a (distribution-free) **CDF** for `Y | X = x` in the sense that:

```
P(p(Y_test; X_test) ≤ τ) = τ   for any τ ∈ (0, 1)
```

— a uniformity property analogous to the [[concepts/probability-integral-transform|probability integral transform]].

## Why It Matters

Returning a full predictive CDF rather than a single set lets the user query **any** coverage level on demand: 80%, 90%, 95% intervals all come from the same predictive distribution, with calibrated probabilistic interpretation.

## Relation to Distributional CP

[[concepts/distributional-conformal-prediction]] (Chernozhukov, Wüthrich, Zhu, 2021) generalises this idea using quantile regression as the base — see [[sources/chernozhukov-2021-distributional-cp]].

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — section on conformal predictive distributions.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/distributional-conformal-prediction]]
- [[concepts/uncertainty-quantification]]
- [[concepts/probability-integral-transform]]

<!-- AUTHORED REGION END -->
