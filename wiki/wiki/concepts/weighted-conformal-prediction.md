---
title: Weighted Conformal Prediction (WCP)
page_id: concepts/weighted-conformal-prediction
page_type: concept
revision_id: 2
created: 2026-05-21T14:00:00Z
updated: 2026-05-24T19:00:00Z
tags: [conformal-prediction, covariate-shift, distribution-shift, weights]
sources: [sources/tibshirani-2019-covariate-shift, sources/angelopoulos-2022-gentle-intro, sources/stocker-2025-conformal-timeseries-intro, sources/dieuleveut-zaffran-2025-cp-tutorial]
related: [concepts/conformal-prediction, concepts/exchangeability, concepts/distribution-drift, concepts/split-conformal-prediction]
mind_map_priority: high
---

# Weighted Conformal Prediction (WCP)

## Primary Source

Primary source: [[sources/tibshirani-2019-covariate-shift|Tibshirani, Barber, Candès & Ramdas (2019), "Conformal Prediction Under Covariate Shift"]]. This NeurIPS paper is the original construction of WCP: it shows that reweighting calibration scores by the test/training likelihood ratio recovers finite-sample marginal coverage under known covariate shift, which is the result this concept page formalises.

**Weighted Conformal Prediction** (Tibshirani, Barber, Candès, Ramdas, 2019) generalises [[concepts/conformal-prediction|CP]] to handle settings where [[concepts/exchangeability|exchangeability]] fails — most notably **covariate shift** — by reweighting calibration scores with a likelihood ratio between the test and training covariate distributions.

## Construction

If the test covariate distribution `P_test(X)` is related to training distribution `P_train(X)` by a known (or estimated) likelihood ratio `w(x) = dP_test/dP_train(x)`, define normalised weights:

```
w̃_i = w(X_i) / [w(X_1) + ... + w(X_n) + w(X_test)]
```

Then form a **weighted quantile** of calibration scores:

```
q̂_w = inf { q : Σ_i w̃_i · 1{s_i ≤ q} ≥ 1 − α }
```

The prediction set `Ĉ(X_test) = { y : s(X_test, y) ≤ q̂_w }` retains finite-sample marginal coverage **under covariate shift**.

## Time-Series Variants

In [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al.'s]] taxonomy, WCP is the "**reweight the calibration data**" family. Time-series variants include:

- **WCP-exponential.** `w(t) ∝ exp(−ρ(T − t))` — exponentially down-weight older calibration points.
- **WCP-linear.** Linear decay over a window.
- **WCP-window.** Hard truncation to the last `W` points.
- **Nex-CP** (Barber–Candès–Ramdas–Tibshirani 2022) — generalised non-exchangeable framework where weights need not be likelihood ratios; coverage gap bounded by total variation between weighted distributions.
- **Learned weights** — neural-net or kernel-learned `w(·)` to handle complex shifts.

## Empirical Behaviour Under Shift

[[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. (2025)]] find that under abrupt mean shift, **WCP-window fails** (hard truncation discards information) while **WCP-exp and WCP-linear self-correct** — recency reweighting is necessary but not sufficient, and the decay shape matters.

## Limitations

- Requires knowledge or estimation of the shift mechanism (`w` or distribution).
- Variance of the weighted quantile grows with `Var(w)` — small effective sample size when weights are concentrated.
- Doesn't help against shifts where the conditional `P(Y|X)` itself drifts (label shift remains an open frontier).

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — chapter on covariate shift.
- [[sources/stocker-2025-conformal-timeseries-intro]] — WCP family for time series.
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — derivation of validity under known shift.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/exchangeability]]
- [[concepts/distribution-drift]]
- [[concepts/adaptive-conformal-inference]] — alternative recipe targeting the same problem.
