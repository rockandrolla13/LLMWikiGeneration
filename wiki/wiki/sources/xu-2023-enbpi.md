---
title: "Conformal prediction for time series"
page_id: sources/xu-2023-enbpi
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
authors: ["Chen Xu", "Yao Xie"]
year: 2023
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence (arXiv:2010.09107)"
tags: [conformal-prediction, time-series, ensemble-methods, prediction-intervals, distribution-free, non-exchangeable, bootstrap]
related: [
  concepts/conformal-prediction,
  concepts/enbpi,
  concepts/prediction-intervals,
  concepts/exchangeability,
  concepts/coverage-guarantee,
  concepts/beta-mixing,
  concepts/quantile-regression,
  concepts/adaptive-conformal-inference,
  concepts/spci,
  concepts/jackknife-plus-after-bootstrap,
  concepts/marginal-coverage,
  concepts/conditional-coverage,
  entities/chen-xu,
  entities/yao-xie,
  sources/xu-2022-spci,
  sources/zaffran-2022-aci
]
mind_map_priority: high
---

# Conformal prediction for time series (EnbPI)

**Authors:** [[entities/chen-xu|Chen Xu]], [[entities/yao-xie|Yao Xie]]

**Year:** 2023 (arXiv v15 of 2010.09107, IEEE TPAMI version)

**Venue:** *IEEE Transactions on Pattern Analysis and Machine Intelligence* (arXiv:2010.09107)

## Summary

Xu and Xie develop a general framework for distribution-free [[concepts/prediction-intervals|prediction intervals]] for time series and introduce **[[concepts/enbpi|EnbPI]]** (Ensemble batch Prediction Intervals), a computationally efficient wrapper around ensemble predictors that is closely related to [[concepts/conformal-prediction|conformal prediction]] but does **not** require [[concepts/exchangeability|exchangeability]]. The method avoids both data-splitting and model retraining by combining a leave-one-out (LOO) residual construction with a bootstrap ensemble that supplies the LOO estimators essentially for free.

Theoretically, the paper establishes explicit, asymptotically vanishing upper bounds on both [[concepts/conditional-coverage|conditional]] and [[concepts/marginal-coverage|marginal coverage]] gaps under verifiable [[concepts/beta-mixing|β-mixing]] / strong-mixing dependence assumptions on the stochastic errors, plus bounds on the set difference between estimated and oracle intervals. These are some of the first conditional-coverage-style guarantees for CP under genuine time-series dependence.

## Key Contributions

1. **The EnbPI algorithm.** A bootstrap-ensemble conformal procedure that wraps an arbitrary point predictor, avoids data splitting, and avoids retraining during sequential inference — yielding LOO-style residuals at the cost of a single ensemble fit.

2. **Asymptotic conditional + marginal coverage guarantees beyond exchangeability.** Explicit upper bounds on both gaps that converge to zero under mild dependency assumptions (β-mixing) and estimator consistency. Conditional guarantees are notable because they are usually impossible at finite sample size in standard CP.

3. **Interval-width / oracle-gap analysis.** Bounds on the size of the set difference between estimated and oracle (narrowest conditionally valid) intervals — analysing *efficiency*, not just validity.

4. **General CP-under-dependence proof techniques.** Refined from Chernozhukov et al.; apply to split conformal and [[concepts/jackknife-plus-after-bootstrap|J+aB]]-style methods on time series, providing a template for future CP-under-dependence analyses.

5. **Empirical benchmark across high-stakes domains.** Solar/wind generation, anomaly detection, greenhouse-gas concentration, appliance energy, Beijing air quality. EnbPI maintains nominal coverage where ARIMA, ICP, WeightedICP, QOOB, AdaptCI (Gibbs–Candès), and J+aB fail; produces shorter intervals; robust to missing data; handles change points via sliding windows.

## Method Sketch

For training data `(X_i, Y_i)_{i=1..T}`:
1. Train `B` bootstrap point predictors. For each `i`, aggregate **only** the bootstrap models that did not see index `i` → LOO estimator `f̂^{−i}`.
2. Compute LOO residuals `ε̂_i = Y_i − f̂^{−i}(X_i)`.
3. At test time, form a sliding-window empirical quantile of the residuals. Intervals may be **asymmetric** via inner optimisation over a quantile offset `β`.
4. Update the residual window with new observations as they arrive — **no retraining of `f̂`**, very low marginal cost.

## Relation to Other Wiki Sources

- [[sources/xu-2022-spci|Xu & Xie 2022 — SPCI]]: the authors' later work that replaces residual quantiles with a learned quantile-regression score; addresses heteroskedasticity that EnbPI cannot.
- [[sources/zaffran-2022-aci|Zaffran 2022 — ACI]]: alternative approach via online α-update rather than ensemble-LOO; ACI is included in the EnbPI benchmark.
- [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]]: groups EnbPI as the "refresh residual pool" family in its taxonomy.
- [[sources/koukorinis-2026-draci|Koukorinis 2026 — DRACI]]: relevant for the doubly-robust extension of conformal time-series methods.

## Questions Raised

- How do EnbPI's coverage guarantees degrade as the β-mixing rate slows toward [[concepts/long-memory|long-memory]] behaviour?
- Can EnbPI be combined with online adaptive-α updates ([[concepts/adaptive-conformal-inference|ACI]]) for abrupt-shift robustness without sacrificing interval width?
- How should sliding-window length and bootstrap count `B` be chosen as functions of dependence strength and sample size?
- Does the conditional-coverage guarantee extend uniformly over covariate space, or only on-average within conditioning sets?
- Can the bootstrap-LOO trick generalise to non-residual scores (quantile-based, density-ratio-based) while preserving the guarantees?

## See Also

- [[concepts/enbpi]]
- [[concepts/conformal-prediction]]
- [[concepts/jackknife-plus-after-bootstrap]]
- [[entities/chen-xu]], [[entities/yao-xie]]
