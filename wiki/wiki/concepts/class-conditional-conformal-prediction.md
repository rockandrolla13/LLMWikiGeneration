---
title: Class-Conditional Conformal Prediction
page_id: concepts/class-conditional-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
tags: [conformal-prediction, classification, conditional-validity, class-coverage]
sources: [sources/angelopoulos-2022-gentle-intro]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/conditional-coverage, concepts/group-balanced-conformal-prediction]
mind_map_priority: medium
---

# Class-Conditional Conformal Prediction

**Class-conditional CP** (Vovk, 2012; Sadinle, Lei, Wasserman, 2019) is the classification variant of [[concepts/group-balanced-conformal-prediction|group-balanced CP]] where the grouping is the **ground-truth class** `Y`. It calibrates within each class so that:

```
P(Y_test ∈ Ĉ(X_test) | Y_test = y) ≥ 1 − α    for every class y
```

## Why It Matters

In imbalanced classification (e.g., medical: 95% normal, 5% cancer), [[concepts/marginal-coverage|marginal coverage]] can be dominated by the majority class — the model may systematically under-cover the rare class while still attaining the marginal target.

Class-conditional CP forces per-class coverage at the cost of using only same-class calibration points to compute each class's quantile.

## Recipe

For each class `y`:
1. Take the calibration subset of examples whose true label is `y`.
2. Compute scores within the subset.
3. Empirical `⌈(n_y + 1)(1 − α)⌉/n_y` quantile → `q̂_y`.
4. At test time, include class `y` in the prediction set if `s(X_test, y) ≤ q̂_y`.

## Trade-off

Rare classes have small `n_y` → noisy `q̂_y` → wider prediction sets for those classes. Often the right move regardless, since class-balanced coverage is the actual deployment goal.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — chapter on class-conditional CP.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/group-balanced-conformal-prediction]]
- [[concepts/conditional-coverage]]
