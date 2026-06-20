---
title: Conformal Prediction (CMU Lecture Notes, Spring 2023)
page_id: sources/tibshirani-2023-cp-lecture-notes
page_type: source
source_type: lecture-notes
revision_id: 1
created: 2026-05-24 20:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Ryan J. Tibshirani
year: 2023
venue: Advanced Topics in Statistical Learning, Carnegie Mellon University (Spring
  2023 lecture notes). 15 pages.
tags:
- conformal-prediction
- lecture-notes
- cmu
- pedagogical
- split-conformal
- full-conformal
- exchangeability
- statistical-learning
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/full-conformal-prediction
- concepts/exchangeability
- concepts/nonconformity-score
- concepts/conformalized-quantile-regression
- concepts/jackknife-plus
- concepts/weighted-conformal-prediction
- concepts/conditional-coverage
- concepts/marginal-coverage
- concepts/adaptive-prediction-sets
- entities/ryan-tibshirani
- sources/tibshirani-2019-covariate-shift
- sources/barber-2021-jackknife-plus
- sources/barber-2023-beyond-exchangeability
- sources/lei-2018-distribution-free-regression
- sources/angelopoulos-2022-gentle-intro
- sources/vovk-2005-algorithmic-learning
- sources/angelopoulos-2023-conformal-pid
mind_map_priority: high
schema_version: 2
uuid: 52105506-05ae-518c-aa12-8871c2c0f223
content_hash: sha256:10e0f062b8b6b5134ed7352c7c5a5f79b0e71b73419d56d6eb433ad4951ccbf5
---

<!-- AUTHORED REGION START -->
# Conformal Prediction (CMU Lecture Notes, Spring 2023)

**Author:** [[entities/ryan-tibshirani|Ryan J. Tibshirani]]

**Year:** 2023

**Venue:** *Advanced Topics in Statistical Learning*, Carnegie Mellon University. Spring 2023 lecture notes. 15 pages.

## Summary

Graduate-level, theoretically grounded introduction to [[concepts/conformal-prediction|conformal prediction]] for statistics PhD students. The notes build the framework from first principles, starting with finite-sample valid prediction intervals from rank-based statistics of i.i.d. response values, and identifying [[concepts/exchangeability|exchangeability]] (rather than i.i.d.) as the minimal sufficient condition.

Tibshirani isolates two **"key ideas"** that organise the entire presentation:

1. **Rank-based adjusted-level quantiles** for exact finite-sample coverage.
2. **Symmetric score construction** that treats the test point symmetrically with the calibration data so that exchangeability is preserved.

From this foundation he develops [[concepts/split-conformal-prediction|split conformal]], then [[concepts/full-conformal-prediction|full conformal]], and finally extensions to classification.

## Distinctive Emphasis

Substantial space is dedicated to **conditional coverage and its impossibility**:
- The calibration-set-conditional Beta distribution for split CP coverage is derived explicitly (showing why small calibration sets give wide variability around the nominal level).
- The Lei-Wasserman (2014) impossibility result for nontrivial X-conditional coverage in the distribution-free setting is formally stated.
- The practical goal is reframed as **local adaptivity**, with studentized residuals and [[concepts/conformalized-quantile-regression|CQR]] presented as the canonical regression remedies, and likelihood / cumulative-likelihood ([[concepts/adaptive-prediction-sets|APS]] / RAPS) scores for classification.

Throughout the treatment is mathematically careful: quantile / CDF equivalent formulations are given, auxiliary randomization for exact coverage is derived, the p-value interpretation of full conformal is spelled out.

## Key Topics Covered

- Rank-based ("first key idea") derivation of finite-sample coverage via adjusted-level quantiles.
- Exchangeability as the minimal assumption — weaker than i.i.d.
- Symmetric score construction ("second key idea") and why naive train-residual prediction undercovers.
- Split conformal with calibration-set residuals; coverage upper bound under no-ties.
- Equivalent quantile, CDF, and rank formulations of the conformal set.
- Auxiliary randomization for exact `1 − α` coverage.
- Full conformal via augmented training sets, with the p-value / hypothesis-testing interpretation.
- Calibration-set-conditional coverage as a Beta distribution and its variability.
- Lei-Wasserman impossibility theorem for distribution-free X-conditional coverage.
- Local adaptivity via studentized residuals and CQR.
- Conformal prediction for classification: likelihood scores and APS / RAPS.

## Why This Source Matters

Unlike the [[sources/angelopoulos-2022-gentle-intro|Angelopoulos-Bates tutorial]] which optimises for ML-practitioner accessibility, Tibshirani teaches CP **as a statistician**:

- Isolates and names the two key ideas (rank-based adjusted quantiles, then symmetric score construction).
- Proves equivalences between quantile / CDF / rank formulations.
- Derives the Beta-distributed calibration-conditional coverage explicitly.
- Dedicates substantial space to the Lei-Wasserman X-conditional impossibility result.

The historical framing reflects an **insider's lineage** (Vovk → Wasserman → Lei → Tibshirani at CMU) rather than the ML community's perspective. Useful complement to Angelopoulos-Bates for anyone wanting the formal-statistical view.

## Relation to Other Wiki Sources

- [[sources/tibshirani-2019-covariate-shift]] — Tibshirani's own primary research; the notes likely cover the WCP construction.
- [[sources/barber-2021-jackknife-plus]] — co-authored research presented in the notes.
- [[sources/barber-2023-beyond-exchangeability]] — companion theoretical work.
- [[sources/lei-2018-distribution-free-regression]] — direct predecessor in the CMU CP-regression lineage.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner-facing counterpart with overlapping topic coverage.
- [[sources/vovk-2005-algorithmic-learning]] — foundational textbook the notes situate themselves against.
- [[sources/angelopoulos-2023-conformal-pid]] — Tibshirani's later co-authored extension to online time series.

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/exchangeability]]
- [[concepts/conditional-coverage]]
- [[entities/ryan-tibshirani]]

<!-- AUTHORED REGION END -->
