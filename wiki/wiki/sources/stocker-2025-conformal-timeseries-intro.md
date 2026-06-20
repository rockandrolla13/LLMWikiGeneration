---
title: A Gentle Introduction to Conformal Time Series Forecasting
page_id: sources/stocker-2025-conformal-timeseries-intro
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- M. Stocker
- Wiktoria Małgorzewicz
- Matteo Fontana
- Souhaib Ben Taieb
year: 2025
venue: arXiv:2511.13608
tags:
- conformal-prediction
- time-series
- forecasting
- tutorial
- review
- non-exchangeability
- beta-mixing
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/adaptive-conformal-inference
- concepts/exchangeability
- concepts/prediction-intervals
- concepts/coverage-guarantee
- concepts/conditional-validity
- concepts/spci
- concepts/beta-mixing
- concepts/uncertainty-quantification
- concepts/conformalized-quantile-regression
- concepts/distributional-conformal-prediction
- concepts/distribution-drift
- concepts/weighted-conformal-prediction
- concepts/enbpi
- concepts/block-conformal-prediction
- concepts/agaci
- concepts/conformal-pid-control
- concepts/marginal-coverage
- concepts/conditional-coverage
- concepts/nonconformity-score
- entities/m-stocker
- entities/wiktoria-malgorzewicz
- entities/matteo-fontana
- entities/souhaib-ben-taieb
- sources/angelopoulos-2022-gentle-intro
- sources/zaffran-2022-aci
- sources/xu-2022-spci
- sources/xu-2023-enbpi
mind_map_priority: high
schema_version: 2
uuid: 8935d74c-01d3-570a-9fc8-b9afcc7a642a
content_hash: sha256:e1925d37f48953750f62651ea67a7b39cc3c4f70a9322d67d4da634a3311bd25
---

<!-- AUTHORED REGION START -->
# A Gentle Introduction to Conformal Time Series Forecasting

**Authors:** [[entities/m-stocker|M. Stocker]], [[entities/wiktoria-malgorzewicz|Wiktoria Małgorzewicz]], [[entities/matteo-fontana|Matteo Fontana]], [[entities/souhaib-ben-taieb|Souhaib Ben Taieb]]

**Year:** 2025

**Venue:** arXiv:2511.13608 (companion-style review to [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates 2022]] but specifically for time series)

## Summary

A pedagogical review that unifies recent advances in [[concepts/conformal-prediction|conformal prediction]] for time-series forecasting. The paper opens with a self-contained refresher on [[concepts/split-conformal-prediction|Split Conformal Prediction (SCP)]], then formalises how time-series data violate [[concepts/exchangeability|exchangeability]] through two mechanisms: **temporal dependence** (ARMA/GARCH-style filtration-driven structure) and **distribution shift** (abrupt breaks, gradual drift, seasonality). The authors derive finite-sample marginal and conditional coverage guarantees for SCP under [[concepts/beta-mixing|β-mixing]] weak-dependence conditions, presenting a cleaner exposition of the Oliveira et al. (2024) framework with full proofs in the appendices.

The core taxonomy classifies modern conformal-forecasting methods into **four mechanistically distinct families**:

1. **Reweighting the calibration data** — [[concepts/weighted-conformal-prediction|WCP / Nex-CP]] and learned-weight variants.
2. **Refreshing the residual pool via OOB bootstrapping** — [[concepts/enbpi|EnbPI]] and [[concepts/spci|SPCI / SPCI-T]].
3. **Adapting the target miscoverage level online** — [[concepts/adaptive-conformal-inference|ACI]], [[concepts/agaci|AgACI]], time-varying step sizes, [[concepts/conformal-pid-control|Conformal PID Control]].
4. **Randomising over blocks rather than points** — [[concepts/block-conformal-prediction|Block CP (transductive and split variants)]].

## Key Contributions

1. **Unified mechanistic taxonomy** of conformal-forecasting methods into four families (reweight / refresh / adapt-α / block-randomise).

2. **Self-contained theoretical re-derivation** of finite-sample marginal and conditional coverage guarantees for SCP under β-mixing weak dependence — explicit proofs (Assumptions A1–A5, Theorem A.3.1) that expand Oliveira et al. (2024).

3. **Formal distinction** between time-series non-exchangeability (ordinal index + temporal dependence + distribution shift) and other non-exchangeability settings (covariate shift, panel data).

4. **Controlled simulation study** comparing SCP, WCP (3 variants), ACI (3 step sizes), EnbPI (3 refresh rates), and Block-SCP on AR(1), ARMA(1,1), mean-shift, and GARCH(1,1) processes — mapping validity ↔ efficiency ↔ compute trade-offs.

5. **Empirical findings.**
   - Under stationary β-mixing, vanilla SCP suffices and is efficient; WCP, ACI, and EnbPI match coverage at varying widths/costs.
   - Under abrupt mean shift, **SCP, Block-SCP, and WCP-window all fail to cover**; ACI, EnbPI, WCP-exp, and WCP-linear self-correct via their explicit recency mechanisms.
   - Block-SCP under-covers even on stationary β-mixing data — a non-obvious failure mode.

6. **Practitioner recommendations and research agenda.** Defaults: SCP for stationary; WCP-exp/linear for cheap shift-robustness; ACI for active feedback; EnbPI/SPCI when heteroskedasticity matters and compute is available. Hybrid methods (ACI + SPCI conditional quantiles, learned WCP weights, distributional conformal forecasting) flagged as next frontier.

7. **Reproducible code** — accompanying GitHub repo by Małgorzewicz reproducing all experiments.

## Why This Source Matters

This is the **time-series-specific companion** to [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates]]. Where that tutorial assumes exchangeability throughout, this paper systematically organises the post-exchangeability landscape into navigable categories. Useful as a reading-list anchor and for choosing between methods in applied work.

## Relation to Other Wiki Sources

- [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates 2022]] — the i.i.d. companion tutorial.
- [[sources/zaffran-2022-aci|Zaffran 2022 — ACI]] — central reference in the "adapt-α" family.
- [[sources/xu-2022-spci|Xu & Xie 2022 — SPCI]] and [[sources/xu-2023-enbpi|Xu & Xie 2023 — EnbPI]] — central references in the "refresh residual pool" family.

## Questions Raised

- How does empirical performance change when the base forecaster is itself adaptive (re-trained ARIMA, neural sequence models) rather than a frozen AR-LS?
- Can sharper, locally-adaptive [[concepts/nonconformity-score|nonconformity scores]] recover asymptotic conditional validity for time series?
- How do the four families behave under strong seasonality, [[concepts/long-memory|long memory]], locally-stationary, and genuinely non-stationary processes — and under multi-step-ahead horizons?
- How should the taxonomy extend to multivariate and functional time series?
- Can hyperparameters (γ for ACI, ρ for WCP, refresh-rate `s` for EnbPI, block size `B` for BCP) be learned online rather than tuned ex ante?
- How should conformal forecasting be extended from intervals to full [[concepts/distributional-conformal-prediction|distributional forecasting]]?

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/adaptive-conformal-inference]]
- [[concepts/enbpi]]
- [[concepts/weighted-conformal-prediction]]
- [[concepts/block-conformal-prediction]]

<!-- AUTHORED REGION END -->
