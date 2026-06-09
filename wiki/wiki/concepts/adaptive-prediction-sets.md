---
title: Adaptive Prediction Sets (APS)
page_id: concepts/adaptive-prediction-sets
page_type: concept
revision_id: 2
created: 2026-05-21T14:00:00Z
updated: 2026-05-24T19:00:00Z
tags: [conformal-prediction, classification, score-design, adaptivity]
sources: [sources/romano-2020-aps, sources/angelopoulos-2022-gentle-intro, sources/dieuleveut-zaffran-2025-cp-tutorial]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/regularized-adaptive-prediction-sets, concepts/nonconformity-score, concepts/conditional-coverage]
mind_map_priority: medium
---

# Adaptive Prediction Sets (APS)

## Primary Source

Primary source: [[sources/romano-2020-aps|Romano, Sesia & Candès (2020), "Classification with Valid and Adaptive Coverage"]]. This NeurIPS paper introduces the greedy-cumulative-softmax APS score formalised below and shows that the resulting CP sets adapt their size to input difficulty while retaining marginal validity.

**Adaptive Prediction Sets (APS)** is a [[concepts/conformal-prediction|conformal]] classification procedure introduced by Romano, Sesia, and Candès (2020). It produces prediction sets whose **size adapts to input difficulty** — ambiguous instances get larger sets, confident instances get small (often singleton) sets.

## The APS Score

Given softmax probabilities `π̂(x) = (π̂_1, ..., π̂_K)` sorted in decreasing order, the APS [[concepts/nonconformity-score|nonconformity score]] for label `y` is the **greedy cumulative sum** of sorted probabilities up to and including class `y`:

```
s_APS(x, y) = Σ_{k : π̂_(k) ≥ π̂_y(x)}  π̂_(k)(x)
```

The CP prediction set is `{y : s_APS(x, y) ≤ q̂}`.

## Why It Adapts

For a confident input (one class with high probability), `s_APS` jumps quickly past `q̂` after just the top class — small set.

For an ambiguous input (probability mass spread across many classes), the cumulative sum grows slowly — large set.

Critically, **marginal validity is automatic** (it's CP); APS only affects which `y`'s land in the set.

## Limitations

APS sets can be **larger than necessary** for very large-class problems (e.g., ImageNet), because it must keep accumulating low-probability classes. The fix is [[concepts/regularized-adaptive-prediction-sets|RAPS]] (Angelopoulos-Bates-Malik-Jordan 2021), which adds a penalty for low-ranked classes.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — section on APS construction and behaviour.
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — APS in the wider score-design landscape.

## Related Concepts

- [[concepts/regularized-adaptive-prediction-sets]]
- [[concepts/nonconformity-score]]
- [[concepts/split-conformal-prediction]]
