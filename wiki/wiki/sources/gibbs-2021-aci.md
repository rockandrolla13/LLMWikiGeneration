---
title: "Adaptive Conformal Inference Under Distribution Shift"
page_id: sources/gibbs-2021-aci
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Isaac Gibbs", "Emmanuel J. Candès"]
year: 2021
venue: "NeurIPS 2021 (arXiv:2106.00170)"
tags: [conformal-prediction, adaptive-conformal-inference, distribution-shift, online-learning, time-series, volatility-forecasting]
related: [
  concepts/adaptive-conformal-inference,
  concepts/online-conformal-prediction,
  concepts/conformal-prediction,
  concepts/distribution-drift,
  concepts/marginal-coverage,
  concepts/exchangeability,
  entities/isaac-gibbs,
  entities/emmanuel-candes,
  sources/zaffran-2022-aci,
  sources/gibbs-2024-online-aci,
  sources/angelopoulos-2023-conformal-pid,
  sources/xu-2023-enbpi,
  sources/stocker-2025-conformal-timeseries-intro
]
mind_map_priority: high
---

# Adaptive Conformal Inference Under Distribution Shift (ACI)

**Authors:** [[entities/isaac-gibbs|Isaac Gibbs]], [[entities/emmanuel-candes|Emmanuel J. Candès]]

**Year:** 2021

**Venue:** NeurIPS 2021 (arXiv:2106.00170)

## Summary

**Primary source** for the wiki concept [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference (ACI)]]. The wiki previously anchored ACI via [[sources/zaffran-2022-aci|Zaffran et al. 2022]] (which built on this paper) — now properly grounded in the Gibbs-Candès original.

Introduces a wrapper around any black-box predictor that produces prediction sets with valid long-run coverage even when the data-generating distribution shifts arbitrarily over time. The method models the distribution shift as a **single-parameter online learning problem**: at each step `t`, the miscoverage target `α_t` is updated via

```
α_{t+1} = α_t + γ · (α − err_t)
```

where `err_t` indicates whether the previous prediction set failed to cover `Y_t` and `γ > 0` controls the adaptation / stability trade-off.

## Key Claims

1. **Bounded `α_t` (Lemma 4.1).** `α_t` stays in `[−γ, 1 + γ]`.
2. **Distribution-free anytime bound (Proposition 4.1).** `|empirical miscoverage − α| ≤ max(α_1, 1 − α_1) / (γ T) + γ`, so coverage error decays as `O(1 / T)` for any `T` — no distributional assumption.
3. **Default `γ = 0.005`.** Practical recommendation that protects against shifts without inducing large oscillations.
4. **HMM tighter bound (Theorem 4.2).** Under a hidden Markov model with small shifts, optimal step size scales as `√|α*_{t+1} − α*_t|`, and ACI obtains approximate marginal coverage at most time steps.
5. **Method-agnostic.** Wraps any conformity score (residual, CQR, etc.); works with both split and full conformal inference.

## Empirical Validation

- **Stock-market volatility (Nvidia, AMD, BlackBerry, Fannie Mae 2000-2020) with GARCH(1, 1) base.** ACI maintains local 90% coverage during shocks (e.g., 2008 Fannie Mae crisis) where fixed-α conformal undercovers dramatically.
- **COVID-19 case-count forecasting.** Local coverage tracking within Bernoulli-sequence noise of the 90% target.

## Why It Matters

This paper launched the modern online / sequential branch of CP. The single-parameter `α_t` update opened up the entire subsequent literature: [[sources/gibbs-2024-online-aci|DtACI]], [[sources/zaffran-2022-aci|AgACI]], [[sources/angelopoulos-2023-conformal-pid|Conformal PID Control]], and the multi-valid / SAOCP families surveyed by [[sources/zhou-2025-cp-data-perspective|Zhou et al. 2025]] and [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]].

## Relation to Other Wiki Sources

- [[sources/zaffran-2022-aci]] — direct successor introducing AgACI (parameter-free aggregation).
- [[sources/gibbs-2024-online-aci]] — same authors' DtACI extension with dynamic-regret bounds.
- [[sources/angelopoulos-2023-conformal-pid]] — generalises the proportional update to full PID control.
- [[sources/xu-2023-enbpi]] — alternative approach via bootstrap-LOO residual refresh.
- [[sources/stocker-2025-conformal-timeseries-intro]] — places ACI in the "adapt α online" family.

## Questions Raised

- How should `γ` be chosen adaptively from data rather than fixed a priori? (Addressed by [[sources/zaffran-2022-aci|AgACI]] and [[sources/gibbs-2024-online-aci|DtACI]].)
- Can the `α_t` recursion be replaced by a multi-parameter or quantile-tracking scheme that achieves conditional rather than marginal coverage?
- How does ACI behave when the conformity score itself (not just the marginal distribution) drifts?
- Does combining ACI with feedback-control or PID-style updates yield better finite-sample local coverage? (Answered in the affirmative by [[sources/angelopoulos-2023-conformal-pid|Angelopoulos-Candès-Tibshirani 2023]].)

## See Also

- [[concepts/adaptive-conformal-inference]]
- [[concepts/online-conformal-prediction]]
- [[entities/isaac-gibbs]]
