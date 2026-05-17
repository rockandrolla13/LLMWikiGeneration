---
title: "Copula Conformal Prediction for Multi-step Time Series Forecasting"
page_id: sources/sun-2022-copula-cpts
page_type: source
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [conformal-prediction, time-series, copulas, multi-step-forecasting, multivariate]
authors: [entities/sophia-sun, entities/rose-yu]
publication: "ICLR 2024 (International Conference on Learning Representations)"
year: 2024
related: [sources/xu-2022-spci, sources/zaffran-2022-aci, concepts/conformal-prediction, concepts/copulas]
mind_map_priority: high
---

# Copula Conformal Prediction for Multi-step Time Series Forecasting

## Summary

This paper introduces **CopulaCPTS** (Copula Conformal Prediction for Time Series), a method for constructing valid confidence regions that cover the **entire forecast horizon** in multivariate, multi-step time series forecasting. The key innovation is using [[concepts/copulas|copulas]] to model the joint dependency structure across prediction time steps, which produces significantly more efficient (smaller) confidence regions compared to methods that apply Bonferroni corrections or ignore temporal dependencies.

## Key Contributions

1. **Full-horizon validity guarantee**: CopulaCPTS proves finite-sample validity for the entire k-step prediction horizon, not just individual time steps
2. **Copula-based joint modeling**: Uses empirical copulas to capture the dependency structure of nonconformity scores across time steps
3. **Two-step calibration**: Splits calibration set into D_cal-1 (for marginal CDFs) and D_cal-2 (for copula), enabling the validity proof
4. **Large efficiency gains**: 30-50% reduction in confidence region area compared to Bonferroni-based methods, especially for long horizons

## Problem Setting

Unlike single time series methods (EnbPI, ACI), CopulaCPTS addresses the setting with **multiple independent time series** (e.g., different vehicle trajectories, patient EEG recordings). Within each series, time steps are temporally dependent. The goal is:

P[∀j ∈ {1,...,k}, y_j ∈ Γ_j^{1-α}] ≥ 1 - α

This is the full-horizon validity condition, stronger than step-wise validity.

## Methodology

### Algorithm Overview (Algorithm 1)
1. **Training**: Split D into D_train, D_cal-1, D_cal-2. Train forecaster f̂ on D_train
2. **CDF calibration on D_cal-1**: Build conformal predictive distributions F̂_j for each time step j using the nonconformity scores s_j = ||y_j - f̂(x)_j||
3. **Copula calibration on D_cal-2**: Transform scores to u^i = (F̂_1(s^i_1),...,F̂_k(s^i_k)) and construct empirical copula
4. **Optimization**: Find u* minimizing region size subject to C_empirical(u*) ≥ 1-α
5. **Prediction**: For test input, construct Γ_j = {y : ||y - ŷ_j|| < F̂_j^{-1}(u*_j)}

### Copula Background
A [[concepts/copulas|copula]] C: [0,1]^k → [0,1] captures the dependency structure of a multivariate distribution through Sklar's theorem:

F(X_1,...,X_k) = C(F_1(X_1),...,F_k(X_k))

The empirical copula provides a nonparametric estimate that preserves validity guarantees.

### Theoretical Foundation
**Theorem 4.1 (Validity)**: CopulaCPTS produces valid confidence regions for the entire forecast horizon.

The proof extends the ICP proof by:
1. Showing conformal predictive distributions are valid (Lemma A.2, from Vovk et al. 2017)
2. Using exchangeability of the transformed scores u^i under the empirical copula
3. Applying the quantile-based ranking argument

## Experimental Results

| Dataset | Method | Coverage | Area |
|---------|--------|----------|------|
| Particle (σ=0.05) | CopulaCPTS | **90.6** | 5.27 |
| Particle (σ=0.05) | CF-RNN | 94.5 | 5.80 |
| COVID-19 | CopulaCPTS | **90.5** | **408.6** |
| COVID-19 | CF-RNN | 95.4 | 610.2 |
| Argoverse | CopulaCPTS | **90.2** | 126.8 |
| Argoverse | CF-RNN | 98.8 | 396.9 |

CopulaCPTS achieves near-perfect calibration (coverage ≈ 90%) with much smaller confidence regions.

### Horizon Length Scaling
The advantage increases with forecast horizon:
- At 20 time steps: ~30% area reduction vs CF-RNN
- At 25 time steps: >50% area reduction

## Key Claims

- "By using copulas to model the uncertainty jointly over future time steps, we can shrink the confidence regions significantly while maintaining validity"
- "CopulaCPTS produces significantly sharper and more calibrated uncertainty estimates than state-of-the-art baselines"
- "The Bonferroni correction [used by CF-RNN] is a lower bound for copula functions" (Frechet-Hoeffding bounds)

## Limitations

- Requires two calibration sets, so needs abundant calibration data
- Validity proof relies on empirical copula; doesn't extend to parametric copula families
- Autoregressive extension requires re-estimating copula for non-stationary series

## Related Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/copulas|Copulas]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/multi-step-conformal-prediction|Multi-step Conformal Prediction]]
- [[concepts/exchangeability|Exchangeability]]
- [[concepts/uncertainty-quantification|Uncertainty Quantification]]

## See Also

- [[sources/xu-2022-spci|SPCI]] - Alternative approach using quantile regression on residuals
- [[sources/zaffran-2022-aci|Adaptive Conformal Predictions for Time Series]]
- [[entities/rose-yu|Rose Yu]] - Senior author, UC San Diego STL Lab
