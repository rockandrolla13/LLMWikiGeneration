---
title: Conformal PID Control for Time Series Prediction
page_id: sources/angelopoulos-2023-conformal-pid
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Anastasios N. Angelopoulos
- Emmanuel J. Candès
- Ryan J. Tibshirani
year: 2023
venue: NeurIPS 2023 (arXiv:2307.16895)
tags:
- conformal-prediction
- time-series
- online-learning
- control-theory
- pid-control
- distribution-shift
- quantile-tracking
related:
- concepts/conformal-pid-control
- concepts/adaptive-conformal-inference
- concepts/agaci
- concepts/online-conformal-prediction
- concepts/conformal-prediction
- concepts/distribution-drift
- entities/anastasios-angelopoulos
- entities/emmanuel-candes
- entities/ryan-tibshirani
- sources/gibbs-2021-aci
- sources/gibbs-2024-online-aci
- sources/zaffran-2022-aci
- sources/xu-2023-enbpi
- sources/stocker-2025-conformal-timeseries-intro
mind_map_priority: high
schema_version: 2
uuid: 9f654911-307a-56b3-a95f-d1710717c3a7
content_hash: sha256:ea08bbb9b1db87e38f4475e1551a4f5031441fbc62996d425b730c17388d3da7
---

<!-- AUTHORED REGION START -->
# Conformal PID Control for Time Series Prediction

**Authors:** [[entities/anastasios-angelopoulos|Anastasios N. Angelopoulos]], [[entities/emmanuel-candes|Emmanuel J. Candès]], [[entities/ryan-tibshirani|Ryan J. Tibshirani]]

**Year:** 2023

**Venue:** NeurIPS 2023 (arXiv:2307.16895). Code: `github.com/aangelopoulos/conformal-time-series`.

## Summary

**Primary source** for the wiki concept [[concepts/conformal-pid-control|Conformal PID Control]]. Reframes online [[concepts/conformal-prediction|conformal prediction]] for time series as a **PID controller**: prediction sets track a coverage set point via proportional (quantile tracking), integral (error integration with saturation), and derivative (forward-looking scorecaster) components.

The framework subsumes vanilla [[concepts/adaptive-conformal-inference|ACI]] as a special case (Proposition 2: ACI is the quantile tracker on a transformed bounded score) and explains why ACI sometimes produces infinite or null prediction sets while direct quantile tracking does not.

## Theorem 1 (Deterministic Long-Run Coverage)

The PID iteration achieves `|(1/T) Σ err_t − α| → 0` **deterministically** for any admissible saturation integrator and any scorecaster, with **no probabilistic assumptions** on the data sequence. The bound is `(c·h(T) + 1)/T` for any sequence of scores in `[−b/2, b/2]`.

## Key Contributions

1. **Conformal PID control framework.** Casts online CP as a PID controller with prediction sets tracking a coverage set point.
2. **Deterministic adversarial coverage guarantee.** Theorem 1 holds without distributional assumptions on the data sequence.
3. **Pinball-loss / gradient-descent equivalence (Proposition 2).** Quantile tracking via online gradient descent on the pinball loss is equivalent to a pure linear error integrator. Unifies and simplifies prior online-conformal analyses.
4. **ACI as a special case.** Vanilla ACI is recovered as quantile tracking on a transformed bounded score. Exposes why ACI can return infinite / null sets while direct quantile tracking does not.
5. **Tan integrator.** `r_t(x) = K_I · tan(x · log(t) / (t · C_sat))` — saturation function whose effective learning rate adapts to the coverage gap via a sec² response.
6. **Scorecasting.** Modular forward-looking layer (analogous to D control) that predicts the next-step score quantile to residualise systematic trends, seasonality, and exogenous covariate effects.

## Empirical Validation

- **COVID-19 4-week-ahead death forecasting (California, winter 2020/2021):** restored coverage from 20% to 70% over a 10-week miscoverage stretch versus the CDC ensemble baseline.
- **New South Wales electricity demand:** Transformer base forecaster + Theta scorecaster. PID hugs the ground truth tightly without the infinite-set pathology of ACI.
- **Stock returns (AMZN, GOOGL, MSFT) and Delhi temperature** with AR / Theta / Prophet / Transformer base forecasters from the `darts` library.

## Relation to Other Wiki Sources

- [[sources/gibbs-2021-aci]] — the original ACI paper this generalises.
- [[sources/gibbs-2024-online-aci]] — concurrent extension to dynamic-regret-bounded online CP.
- [[sources/zaffran-2022-aci]] — AgACI as a contemporary expert-aggregation alternative.
- [[sources/xu-2023-enbpi]] — EnbPI as the bootstrap-LOO alternative for time-series CP.
- [[sources/stocker-2025-conformal-timeseries-intro]] — places PID-Conformal in the "adapt α online" family.

## Questions Raised

- How should integrator constants (`C_sat`, `K_I`) and learning rates be set principled rather than heuristically?
- Can a local / windowed integrator avoid late-sequence oscillation when global integrator marginal coverage stays near 1−α despite local drift?
- How to design scorecasters that avoid injecting variance on near-i.i.d. score sequences (automatic gating between reactive and forward-looking modes)?
- Does the deterministic long-run guarantee extend to conditional-coverage notions without losing the assumption-free property?

## See Also

- [[concepts/conformal-pid-control]]
- [[concepts/adaptive-conformal-inference]]
- [[entities/ryan-tibshirani]]

<!-- AUTHORED REGION END -->
