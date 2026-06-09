---
title: Online Conformal Prediction
page_id: concepts/online-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
tags: [conformal-prediction, online-learning, time-series, sequential-prediction, adversarial]
sources: [sources/gibbs-2021-aci, sources/gibbs-2024-online-aci, sources/angelopoulos-2023-conformal-pid, sources/zaffran-2022-aci, sources/xu-2023-enbpi, sources/stocker-2025-conformal-timeseries-intro]
related: [concepts/conformal-prediction, concepts/adaptive-conformal-inference, concepts/agaci, concepts/conformal-pid-control, concepts/dtaci, concepts/enbpi, concepts/non-exchangeable-conformal-prediction, concepts/exchangeability]
mind_map_priority: high
---

# Online Conformal Prediction

**Online conformal prediction** is the umbrella family of [[concepts/conformal-prediction|CP]] methods designed for the streaming setting: data arrive sequentially, predictions are made one at a time, and labels are revealed before the next prediction. The goal is **long-run coverage** `(1/T) Σ err_t → α` (or deterministic adversarial coverage) without requiring [[concepts/exchangeability|exchangeability]].

## Why It's Different

Standard split / full CP assumes exchangeability of `(X_1, Y_1), ..., (X_n, Y_n), (X_test, Y_test)`. In the streaming setting:

- The `t`-th test point may have been generated under a different distribution from the calibration history.
- Labels arrive sequentially, enabling feedback-style adaptation that batch CP cannot use.
- Distribution shift, regime change, and non-stationarity are the rule rather than the exception.

Online CP methods exploit the feedback signal to maintain coverage despite these violations.

## The Major Families

| Method | Mechanism | Primary source |
|---|---|---|
| [[concepts/adaptive-conformal-inference\|ACI]] | Proportional update on miscoverage target `α_t` | [[sources/gibbs-2021-aci\|Gibbs & Candès 2021]] |
| [[concepts/agaci\|AgACI]] | Expert aggregation over multiple `γ`-tuned ACI instances | [[sources/zaffran-2022-aci\|Zaffran et al. 2022]] |
| [[concepts/dtaci\|DtACI]] | Dynamic-regret-bounded expert aggregation | [[sources/gibbs-2024-online-aci\|Gibbs & Candès 2024]] |
| [[concepts/conformal-pid-control\|Conformal PID Control]] | PID controller (proportional + integral + scorecaster) | [[sources/angelopoulos-2023-conformal-pid\|Angelopoulos-Candès-Tibshirani 2023]] |
| [[concepts/enbpi\|EnbPI]] | Bootstrap-LOO refresh of residual pool with sliding window | [[sources/xu-2023-enbpi\|Xu & Xie 2023]] |
| [[concepts/non-exchangeable-conformal-prediction\|NexCP]] | Fixed weights on calibration history with TV-bounded coverage gap | [[sources/barber-2023-beyond-exchangeability\|Barber et al. 2023]] |

[[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]] reorganises these into a four-family taxonomy: reweight calibration / refresh residuals / adapt α online / block randomisation.

## Coverage Guarantees in the Streaming Setting

- **Long-run coverage:** `lim (1/T) Σ err_t = α`. Achieved by ACI (Proposition 4.1), DtACI (Theorem 3.2 with decaying step sizes), and Conformal PID (Theorem 1, deterministically).
- **Local coverage:** Coverage at each step or within sliding windows. Harder; addressed by DtACI's dynamic-regret bound and Conformal PID's deterministic local bound.
- **Adversarial coverage:** Distribution-free, worst-case-sequence guarantees. Conformal PID gives the strongest result: deterministic long-run coverage for any sequence of scores in a bounded range.

## When To Use Which

| Setting | Recommended method |
|---|---|
| Slow stationary drift | NexCP-exp or vanilla SCP with sliding window |
| Abrupt regime change | ACI / AgACI / DtACI / Conformal PID |
| Heteroskedastic time series | EnbPI or SPCI |
| Hybrid (drift + heteroskedasticity + abrupt change) | EnbPI + ACI (the auto-memory recommendation), or Conformal PID with scorecaster |

## Sources

See the table above for primary sources of each family.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/adaptive-conformal-inference]]
- [[concepts/conformal-pid-control]]
- [[concepts/non-exchangeable-conformal-prediction]]
- [[concepts/enbpi]]
- [[concepts/exchangeability]]
