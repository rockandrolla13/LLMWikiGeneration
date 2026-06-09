---
title: Conformal Outlier Detection
page_id: concepts/conformal-outlier-detection
page_type: concept
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
tags: [conformal-prediction, outlier-detection, anomaly-detection, unsupervised]
sources: [sources/angelopoulos-2022-gentle-intro]
related: [concepts/conformal-prediction, concepts/exchangeability, concepts/split-conformal-prediction, concepts/nonconformity-score]
mind_map_priority: medium
---

# Conformal Outlier Detection

The unsupervised variant of [[concepts/conformal-prediction|CP]]: calibrate a [[concepts/nonconformity-score|score]] `s(x)` on clean i.i.d. data `X_1, ..., X_n` and **flag a test point as an outlier** when its score exceeds the empirical `⌈(n+1)(1−α)⌉/n` quantile.

## Type-1 Error Control

```
P(X_test flagged as outlier | X_test ∼ P_train) ≤ α
```

This is a **finite-sample, distribution-free** false-positive rate guarantee — the unsupervised counterpart of conformal coverage.

## Construction

1. Train a one-class scorer `s(x)` (e.g., LOF, isolation forest, density estimate).
2. On a clean calibration set, compute `{s(X_i)}`.
3. Compute `q̂ = ⌈(n+1)(1−α)⌉/n` empirical quantile.
4. **Flag** any test point with `s(X_test) > q̂`.

## Caveats

- The clean calibration set must genuinely be free of outliers — calibration leakage breaks the guarantee.
- The type-1 rate is marginal over the test distribution; **per-input** conditional false-positive control is impossible without distributional assumptions (analogous to [[concepts/conditional-coverage|conditional coverage]] impossibility).
- Type-2 error (power, recall of true outliers) depends entirely on score quality — CP gives nothing here.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — chapter on conformal outlier detection.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/nonconformity-score]]
