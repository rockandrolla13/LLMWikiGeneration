---
title: DtACI (Dynamically-tuned Adaptive Conformal Inference)
page_id: concepts/dtaci
page_type: concept
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
tags: [conformal-prediction, online-learning, expert-aggregation, dynamic-regret, adaptive-conformal-inference]
sources: [sources/gibbs-2024-online-aci, sources/stocker-2025-conformal-timeseries-intro]
related: [concepts/adaptive-conformal-inference, concepts/agaci, concepts/online-conformal-prediction, concepts/conformal-pid-control, concepts/conformal-prediction]
mind_map_priority: medium
---

# DtACI (Dynamically-tuned Adaptive Conformal Inference)

**DtACI** ([[sources/gibbs-2024-online-aci|Gibbs & Candès 2024]]) is the parameter-free generalisation of [[concepts/adaptive-conformal-inference|ACI]]. Instead of requiring the user to set the step-size `γ`, DtACI runs `k` parallel ACI experts with a geometric grid of step-sizes and aggregates them via exponential re-weighting plus uniform mixing.

## How It Works

For each step `t`:

1. Run `k` parallel ACI updates with step-sizes `γ_1 < γ_2 < ... < γ_k`.
2. Each expert `i` maintains its own `α_t^i`.
3. Combine via weights `w_t^i` that follow exponential re-weighting on the pinball loss plus a uniform-mixing `σ` update.
4. Output either a probability-weighted draw (Algorithm 1) or the weighted mean `ᾱ_t = Σ p_t^i α_t^i` (Algorithm 2).

## Theoretical Guarantees

- **Dynamic-regret bound (Theorem 3.1).** On any interval `I = [r, s]`, expected pinball-loss gap to the best `α_t*` sequence is bounded by `Σ_{t=r+1}^s |α_t* − α_{t-1}*| / |I|` (local rate of distribution shift), up to log-and-`σ` terms.
- **Local squared-deviation control (Proposition 3.1).** Pinball-loss control translates to `(α_t − α_t*)²` control under a density lower bound on `β_t`. Gives direct local-coverage guarantees without HMM structure.
- **Long-run coverage (Theorem 3.2).** If `η_t, σ_t → 0`, achieves exact long-run miscoverage `α`.

## Why It Matters

DtACI gives the **strongest theoretical local-coverage guarantee** in the ACI family. It outperforms AgACI on abrupt regime shifts (AgACI lags because its cumulative-loss weighting averages over all history) and Multivalid Prediction / MVP (which has essentially no local adaptivity).

## DtACI vs AgACI vs PID-Conformal

- **[[concepts/agaci|AgACI]]** (Zaffran 2022): expert aggregation by cumulative pinball loss. Smooth but slow to adapt after abrupt shifts.
- **DtACI** (Gibbs-Candès 2024): expert aggregation by exponential re-weighting + uniform mixing. Dynamic-regret bound; fast adaptation after shifts.
- **[[concepts/conformal-pid-control|Conformal PID Control]]** (Angelopoulos-Candès-Tibshirani 2023): explicit PID controller with proportional + integral + scorecaster. Deterministic adversarial guarantee.

## Practical Defaults

- `|I| = 500` for setting `η, σ` heuristically.
- `γ` grid: `{0.001, 0.002, ..., 0.128}` (geometric).
- Heuristic fixed `η = √(3 log(k) / (500 · ((1−α)²α + α²(1−α))/3))`.

## Sources

- [[sources/gibbs-2024-online-aci]] — primary source.
- [[sources/stocker-2025-conformal-timeseries-intro]] — places DtACI in the "adapt α online" family.

## Related Concepts

- [[concepts/adaptive-conformal-inference]]
- [[concepts/agaci]]
- [[concepts/online-conformal-prediction]]
- [[concepts/conformal-pid-control]]
