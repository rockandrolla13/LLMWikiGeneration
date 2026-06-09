---
title: Group-Balanced Conformal Prediction
page_id: concepts/group-balanced-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
tags: [conformal-prediction, fairness, conditional-validity, group-coverage]
sources: [sources/angelopoulos-2022-gentle-intro]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/conditional-coverage, concepts/class-conditional-conformal-prediction]
mind_map_priority: medium
---

# Group-Balanced Conformal Prediction

**Group-balanced CP** (Vovk, 2012; Sadinle, Lei, Wasserman, 2019) stratifies the calibration set by a discrete observed group feature `G ∈ {1, ..., K}` and applies the split-conformal recipe **within each group**, achieving (1 − α) coverage *conditional on group membership*:

```
P(Y_test ∈ Ĉ(X_test) | G_test = g) ≥ 1 − α    for all g
```

## Recipe

For each group `g`:
1. Take the calibration subset `{(X_i, Y_i) : G_i = g}` — size `n_g`.
2. Compute scores `{s(X_i, Y_i)}` within the subset.
3. Take the `⌈(n_g + 1)(1 − α)⌉/n_g` empirical quantile → `q̂_g`.
4. At test time, look up `G_test = g` and use `q̂_g`.

## Why It Matters

Pure [[concepts/marginal-coverage|marginal coverage]] can hide systematic under-coverage on minority groups. Group-balanced CP gives a **finite-sample, distribution-free** guarantee for every group, useful for:

- **Fairness audits** — ensure coverage holds across demographic groups.
- **Medical applications** — ensure coverage holds across patient subpopulations.
- **Domain robustness** — ensure coverage holds across known shift sources.

## Trade-off

Cost is **statistical efficiency**: each group's `q̂_g` is computed from `n_g` points only. If `n_g` is small for some group, the empirical quantile is noisy and the resulting intervals are wider than necessary.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — chapter on group-balanced CP.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/conditional-coverage]]
- [[concepts/class-conditional-conformal-prediction]]
