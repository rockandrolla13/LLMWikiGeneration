---
title: "Conformal Inference for Online Prediction with Arbitrary Distribution Shifts"
page_id: sources/gibbs-2024-online-aci
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Isaac Gibbs", "Emmanuel J. Candès"]
year: 2024
venue: "Journal of Machine Learning Research 25 (arXiv:2208.08401)"
tags: [conformal-prediction, adaptive-conformal-inference, online-learning, distribution-shift, expert-aggregation, dynamic-regret, dtaci]
related: [
  concepts/adaptive-conformal-inference,
  concepts/dtaci,
  concepts/online-conformal-prediction,
  concepts/agaci,
  concepts/conformal-prediction,
  concepts/distribution-drift,
  entities/isaac-gibbs,
  entities/emmanuel-candes,
  sources/gibbs-2021-aci,
  sources/zaffran-2022-aci,
  sources/angelopoulos-2023-conformal-pid,
  sources/barber-2023-beyond-exchangeability,
  sources/stocker-2025-conformal-timeseries-intro
]
mind_map_priority: high
---

# Conformal Inference for Online Prediction with Arbitrary Distribution Shifts (DtACI)

**Authors:** [[entities/isaac-gibbs|Isaac Gibbs]], [[entities/emmanuel-candes|Emmanuel J. Candès]]

**Year:** 2024

**Venue:** *Journal of Machine Learning Research* 25 (arXiv:2208.08401, 2023). Code: `github.com/isgibbs/DtACI`.

## Summary

Extends the original [[sources/gibbs-2021-aci|ACI paper]] by introducing **DtACI** (Dynamically-tuned Adaptive Conformal Inference) — see the new wiki concept [[concepts/dtaci|DtACI]]. Removes the need for a user-specified step-size by running multiple ACI experts with different `γ` values in parallel and aggregating them via exponential re-weighting adapted from Gradu et al. (2020).

The method achieves provably small **dynamic regret** over all local time intervals of a given width and is adaptive to both the size and type of distribution shift.

## Key Theoretical Contributions

1. **ACI ≡ online gradient descent on pinball loss.** ACI's update `α_{t+1} = α_t + γ(α − err_t)` is equivalent to OGD on the pinball loss with subgradient `(α − err_t)`. The conceptual bridge enabling import of online-convex-optimisation machinery.
2. **DtACI algorithm.** Runs `k` parallel ACI experts with a geometric grid of step-sizes `γ_i`. Outputs `α_t` as either a probability-weighted draw (Algorithm 1) or weighted mean `ᾱ_t = Σ p_t^i α_t^i` (Algorithm 2). Weights follow exponential re-weighting plus uniform mixing (`σ` update).
3. **Dynamic-regret bound (Theorem 3.1).** On any interval `I = [r, s]`, expected pinball-loss gap to the best `α_t*` sequence is controlled by `Σ_{t=r+1}^s |α_t* − α_{t−1}*| / |I|` (local rate of distribution shift), up to `log(k)/η` and `σ` terms.
4. **Local squared-deviation control (Proposition 3.1).** Connects pinball-loss control to squared-deviation control `(α_t − α_t*)²` under a density lower bound on `β_t`. Gives direct local-coverage guarantees without requiring known shift magnitude, HMM structure, or fixed regression — the three assumptions needed by [[sources/gibbs-2021-aci|Gibbs-Candès 2021]].
5. **Long-run coverage (Theorem 3.2).** If `η_t, σ_t → 0`, DtACI achieves exact long-run miscoverage `α`.

## Empirical Validation

- **Simulated stationary / smooth / jump shifts.** DtACI outperforms AgACI and MVP on jump-shift environments. AgACI lags after regime change because its cumulative-loss weighting averages over all history. MVP shows essentially no local adaptivity.
- **Stock-market volatility (Nvidia, AMD, BlackBerry, Fannie Mae) with GARCH(1, 1).** DtACI tracks the 1 − α = 0.9 level locally without prior knowledge of shift size. QQ-plot vs i.i.d. Bernoulli(α) shows local-coverage gaps are essentially unimprovable.
- **COVID-19 case-count forecasting.** Conditional-coverage diagnostics show DtACI is not merely reactive (alternating over/under-coverage) but actually tracks `α_t*`.

## Practical Defaults

- `|I| = 500` for setting `η, σ` (heuristic).
- `γ` grid: `{0.001, 0.002, ..., 0.128}` (geometric).
- Heuristic fixed `η = √(3 log(k) / (500 · ((1−α)²α + α²(1−α))/3))`.

## Relation to Other Wiki Sources

- [[sources/gibbs-2021-aci]] — the original single-parameter ACI this extends.
- [[sources/zaffran-2022-aci]] — AgACI as the immediate predecessor in expert-aggregation ACI.
- [[sources/angelopoulos-2023-conformal-pid]] — concurrent generalisation via PID control.
- [[sources/barber-2023-beyond-exchangeability]] — companion theoretical framework for non-exchangeable CP via fixed weights.
- [[sources/stocker-2025-conformal-timeseries-intro]] — taxonomy placement.

## Questions Raised

- DtACI may produce small bias in long-run coverage with constant `η, σ`. A rigorous bound is not given.
- Sensitivity to the heuristic `|I| = 500` choice across application domains is not characterised.

## See Also

- [[concepts/dtaci]]
- [[concepts/adaptive-conformal-inference]]
- [[concepts/online-conformal-prediction]]
- [[entities/isaac-gibbs]]
