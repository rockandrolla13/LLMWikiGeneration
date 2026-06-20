---
title: Nonconformity Score
page_id: concepts/nonconformity-score
page_type: concept
revision_id: 1
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- score-design
- validity
sources:
- sources/angelopoulos-2022-gentle-intro
- sources/dieuleveut-zaffran-2025-cp-tutorial
- sources/stocker-2025-conformal-timeseries-intro
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/conformalized-quantile-regression
- concepts/adaptive-prediction-sets
- concepts/regularized-adaptive-prediction-sets
mind_map_priority: high
schema_version: 2
uuid: 2cfbdfe9-8d13-5a6e-becb-74dc344e78fa
content_hash: sha256:2e1a405817364adb299a98b122a09dccd8bca00b4ecdb7e54a13f43dfbd2d3f8
---

<!-- AUTHORED REGION START -->
# Nonconformity Score

A **nonconformity score** `s(x, y)` (or `s(x)` in unsupervised settings) is a function that measures how poorly a labelled point conforms to a calibration sample. [[concepts/conformal-prediction|Conformal prediction]]'s validity holds for **any** score, but score *design* determines set size, adaptivity, and shape.

## The Score-Quantile Recipe

Given a calibration set of scores `{s(X_i, Y_i)}_{i=1..n}`, the conformal prediction set at level `1 − α` is:

```
Ĉ(x) = { y : s(x, y) ≤ q̂ }    where q̂ = ⌈(n+1)(1−α)⌉/n empirical quantile
```

[[concepts/marginal-coverage|Marginal coverage]] follows from [[concepts/exchangeability|exchangeability]] alone — the choice of `s` is free.

## Canonical Score Designs

| Task | Score | Notes |
|---|---|---|
| Regression (basic) | `\|y − μ̂(x)\|` | Equal-width intervals around point predictor |
| Regression (heteroskedastic) | `\|y − μ̂(x)\| / σ̂(x)` | σ̂-scaled residuals |
| Regression (quantile) | [[concepts/conformalized-quantile-regression\|CQR]]: `max(q̂_lo − y, y − q̂_hi)` | Width adapts to local quantile spread |
| Classification (basic) | `1 − f̂_y(x)` (1-minus-softmax) | Simple but non-adaptive in set size |
| Classification (adaptive) | [[concepts/adaptive-prediction-sets\|APS]] cumulative softmax | Set size grows for ambiguous inputs |
| Classification (regularised) | [[concepts/regularized-adaptive-prediction-sets\|RAPS]] | Penalises low-rank classes; smaller sets |
| Bayes | `−log p(y \| x)` | Posterior predictive density |
| Time series (heteroskedastic) | [[concepts/spci\|SPCI]] learned quantile score | Replaces residual quantile with learned QR |

## Historical Note

The term descends from Kolmogorov-complexity randomness deficiency — measures of how "atypical" a point is under a hypothesised generating distribution. Vovk, Gammerman, and Shafer (2005) formalised this for prediction.

## Design Principles

- **Validity is free** for any deterministic score. The non-trivial work is in choosing a score whose ranking aligns with predictive uncertainty.
- **Adaptivity is a property of `s`, not the CP protocol.** A static, heuristic score (1−softmax) gives valid but un-adaptive sets; APS/RAPS/CQR adapt set width to instance difficulty.
- **Score learning** is an open frontier — can `s` itself be learned from a held-out fold to optimise efficiency under validity constraints?

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — canonical catalogue of scores.
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — derivation of validity via the quantile lemma.
- [[sources/stocker-2025-conformal-timeseries-intro]] — score design for time-series CP.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/conformalized-quantile-regression]]
- [[concepts/adaptive-prediction-sets]]

<!-- AUTHORED REGION END -->
