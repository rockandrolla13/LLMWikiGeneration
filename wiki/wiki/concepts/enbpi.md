---
title: EnbPI (Ensemble batch Prediction Intervals)
page_id: concepts/enbpi
page_type: concept
revision_id: 1
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- ensemble-methods
- bootstrap
- prediction-intervals
sources:
- sources/xu-2023-enbpi
- sources/stocker-2025-conformal-timeseries-intro
- sources/zaffran-2022-aci
related:
- concepts/conformal-prediction
- concepts/prediction-intervals
- concepts/exchangeability
- concepts/spci
- concepts/jackknife-plus-after-bootstrap
- concepts/adaptive-conformal-inference
- concepts/beta-mixing
mind_map_priority: high
schema_version: 2
uuid: 2b7b980d-5b8c-5cd0-8956-b276dab49c02
content_hash: sha256:92788780cf48751ea635a28e48f740e8686dea1b3547dd9dccefee8c0bd8db57
---

<!-- AUTHORED REGION START -->
# EnbPI (Ensemble batch Prediction Intervals)

**EnbPI** is a conformal-style algorithm by [[entities/chen-xu|Xu]] and [[entities/yao-xie|Xie]] ([[sources/xu-2023-enbpi|2023]]) that wraps an ensemble of bootstrap-trained point predictors to produce sequential, distribution-free [[concepts/prediction-intervals|prediction intervals]] for time series — **without** requiring [[concepts/exchangeability|exchangeability]].

## Mechanism

For training data `(X_i, Y_i)_{i=1..T}`:

1. **Bootstrap ensemble.** Train `B` point predictors on independent bootstrap samples.
2. **Leave-one-out for free.** For each index `i`, aggregate **only** the bootstrap models whose sample did not include `i` → LOO estimator `f̂^{−i}`.
3. **LOO residuals.** Compute `ε̂_i = Y_i − f̂^{−i}(X_i)`.
4. **Calibrated intervals.** Form a (possibly asymmetric) sliding-window empirical quantile of the residuals; centre new intervals on the full-ensemble prediction.
5. **Sequential update.** As new observations arrive, slide the residual window. **No retraining of `f̂` at test time.**

## Why It Matters

- **No data split** (unlike [[concepts/split-conformal-prediction|SCP]]) — uses all data for both fitting and calibration.
- **No retraining at test time** — marginal cost per new prediction is `O(1)`.
- **Asymptotic [[concepts/conditional-coverage|conditional coverage]] guarantee** under [[concepts/beta-mixing|β-mixing]] dependence — rare for CP-on-time-series methods.

## Place in the CP-for-time-series Taxonomy

In Stocker et al. ([[sources/stocker-2025-conformal-timeseries-intro|2025]])'s four-family taxonomy, EnbPI is the canonical "**refresh the residual pool via OOB bootstrapping**" method. The other families:

- **Reweight calibration** — [[concepts/weighted-conformal-prediction|WCP]] / Nex-CP.
- **Adapt α online** — [[concepts/adaptive-conformal-inference|ACI]], [[concepts/agaci|AgACI]], [[concepts/conformal-pid-control|Conformal PID]].
- **Block randomisation** — [[concepts/block-conformal-prediction|BCP]].

## Empirical Behaviour

- Maintains nominal coverage where ARIMA, ICP, WeightedICP, QOOB, and J+aB fail.
- Yields shorter intervals than competitors on solar/wind power, anomaly detection, energy, and air-quality benchmarks.
- Robust to missing data.
- Handles change points via sliding-window resets.

## Limitations

- Cannot adapt **interval width** to local heteroskedasticity (residuals are aggregated globally). Addressed by the authors' follow-up [[concepts/spci|SPCI]], which replaces residual quantiles with a learned [[concepts/quantile-regression|quantile regression]] score.
- Coverage degrades as the dependence rate slows toward [[concepts/long-memory|long memory]].

## Sources

- [[sources/xu-2023-enbpi]] — original paper (arXiv 2010.09107; IEEE TPAMI 2023).
- [[sources/stocker-2025-conformal-timeseries-intro]] — review placing EnbPI in the four-family taxonomy.
- [[sources/zaffran-2022-aci]] — benchmark comparison against ACI/AgACI.

## Related Concepts

- [[concepts/spci]] — the authors' heteroskedasticity-aware successor.
- [[concepts/jackknife-plus-after-bootstrap]] — closely related construction; EnbPI extends J+aB to non-exchangeable data.
- [[concepts/adaptive-conformal-inference]] — alternative way of handling distribution shift.

<!-- AUTHORED REGION END -->
