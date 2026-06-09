---
title: Jackknife+ Prediction
page_id: concepts/jackknife-plus
page_type: concept
revision_id: 2
created: 2026-05-24T16:00:00Z
updated: 2026-05-24T19:00:00Z
tags: [conformal-prediction, jackknife, leave-one-out, prediction-intervals]
sources: [sources/barber-2021-jackknife-plus, sources/angelopoulos-2022-gentle-intro, sources/fontana-2023-cp-unified-review]
related: [concepts/conformal-prediction, concepts/cross-conformal-prediction, concepts/jackknife-plus-after-bootstrap, concepts/enbpi, concepts/full-conformal-prediction, concepts/split-conformal-prediction]
mind_map_priority: medium
---

# Jackknife+ Prediction

## Primary Source

Primary source: [[sources/barber-2021-jackknife-plus|Barber, Candès, Ramdas & Tibshirani (2021), "Predictive inference with the jackknife+"]]. This Annals of Statistics paper introduces the jackknife+ construction and proves the finite-sample 1 − 2α marginal coverage bound formalised below; it is the original reference for the LOO-prediction trick that distinguishes jackknife+ from the plain jackknife.

**Jackknife+** (Barber, Candès, Ramdas, Tibshirani, 2021) is the canonical leave-one-out variant of [[concepts/conformal-prediction|conformal prediction]]. It provides finite-sample marginal coverage at level 1 − 2α using leave-one-out residuals from `n` refits of the base model.

## The Construction

For training data `(X_i, Y_i)_{i=1..n}`:

1. For each `i`, refit the base model `μ̂^{−i}` on the data with `(X_i, Y_i)` removed.
2. Compute LOO residuals `R_i = |Y_i − μ̂^{−i}(X_i)|`.
3. At test point `x`, the Jackknife+ interval is:

```
Ĉ(x) = [ Q^{−}_α({μ̂^{−i}(x) − R_i}_{i=1..n}),   Q^{+}_{1−α}({μ̂^{−i}(x) + R_i}_{i=1..n}) ]
```

where `Q^{−}` and `Q^{+}` are the lower and upper quantiles of the n-point distributions.

The key innovation over the **plain jackknife** is the use of LOO *predictions* in the interval construction, not just LOO residuals. This is what buys back the rigorous coverage guarantee.

## Coverage Guarantee

`P(Y_test ∈ Ĉ(X_test)) ≥ 1 − 2α` in finite samples, under [[concepts/exchangeability|exchangeability]].

The `1 − 2α` (rather than `1 − α`) is the theoretical cost of avoiding the data split. In practice the actual coverage is typically close to `1 − α` — the `2α` bound is loose.

## Variants in the Wiki

- **[[concepts/cross-conformal-prediction|CV+]].** K-fold version; refit only K times instead of n.
- **[[concepts/jackknife-plus-after-bootstrap|Jackknife+ after Bootstrap (J+aB)]].** Aggregates bootstrap models to get LOO estimates without explicit retraining.
- **[[concepts/enbpi|EnbPI]].** J+aB-style construction extended to time-series via sliding residual windows.

## When To Use

- **Small `n`** where [[concepts/split-conformal-prediction|split CP]] wastes too much data.
- **Moderately expensive base models** where `n` refits are tolerable but `|𝒴| × n` ([[concepts/full-conformal-prediction|full CP]]) is not.
- **High-stakes settings** where you want LOO efficiency without losing the coverage guarantee.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — Jackknife+ chapter; the 1 − 2α theorem.
- [[sources/fontana-2023-cp-unified-review]] — theoretical positioning within the cross-conformal family.

## Related Concepts

- [[concepts/cross-conformal-prediction]]
- [[concepts/jackknife-plus-after-bootstrap]]
- [[concepts/enbpi]]
- [[concepts/conformal-prediction]]
