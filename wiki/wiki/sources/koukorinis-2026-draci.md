---
title: Doubly Robust Adaptive Conformal Inference for Causal Effects Under Temporal
  Dependence
page_id: sources/koukorinis-2026-draci
page_type: source
source_type: paper
revision_id: 1
created: 2026-04-28 12:45:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Andreas Koukorinis
year: 2026
venue: JMLR (submitted)
tags:
- conformal-prediction
- causal-inference
- time-series
- doubly-robust
- market-microstructure
related:
- concepts/conformal-prediction
- concepts/adaptive-conformal-inference
- concepts/doubly-robust-estimation
- concepts/beta-mixing
- entities/andreas-koukorinis
mind_map_priority: high
schema_version: 2
uuid: 29d31285-2986-5caa-82ac-1424b1dfb77a
content_hash: sha256:ba4cd453652a1aa321bda328908f57b0efbb77375c7f4d465ef985d823e6574b
---

<!-- AUTHORED REGION START -->
# Doubly Robust Adaptive Conformal Inference for Causal Effects Under Temporal Dependence

**Authors:** [[entities/andreas-koukorinis|Andreas Koukorinis]]

**Year:** 2026

**Venue:** JMLR (submitted)

**Code:** https://github.com/ak/draci

## Summary

This paper introduces **DR-ACI (Doubly Robust Adaptive Conformal Inference)**, a method for constructing prediction intervals for treatment effects under temporal dependence. The key innovation is combining [[concepts/doubly-robust-estimation|doubly robust pseudo-outcomes]] with [[concepts/adaptive-conformal-inference|adaptive conformal inference]] while explicitly handling [[concepts/beta-mixing|β-mixing]] dependence.

## Key Contributions

1. **Temporal block cross-fitting with guard bands**: Partitioning time series into contiguous blocks with guard bands that ensure training-calibration separation. This preserves DML product-bias rates under β-mixing with explicit coupling remainder O(β(g)^{δ/(2+δ)}).

2. **Switch-coefficient control for DR scores**: Shows that conformity scores constructed from doubly robust pseudo-outcomes inherit the switch-coefficient bound of the underlying process.

3. **Coverage decomposition**: The coverage gap has three interpretable terms:
   - Mixing gap: min_τ{τ/T + 2β(τ)}
   - Nuisance-bias tax: ||ê-e||₂ · ||μ̂-μ||₂
   - Adaptation term: O(T^{-1/2})

4. **VS-DR-ACI**: Variance-standardized version that produces 63% narrower intervals than alternatives while maintaining valid coverage—the only method that works under combined dependence (ρ=0.95) and covariate drift.

## Problem Setting

Standard [[concepts/conformal-prediction|conformal prediction]] targets observable outcomes Y; this paper targets the latent CATE τ(X) = E[Y(1) - Y(0) | X]. Access is through doubly robust pseudo-outcomes:

ψ_t^DR = μ̂₁(X_t) - μ̂₀(X_t) + W_t(Y_t - μ̂₁(X_t))/ê(X_t) - (1-W_t)(Y_t - μ̂₀(X_t))/(1 - ê(X_t))

Under temporal dependence, naïve conformal prediction fails because [[concepts/exchangeability|exchangeability]] no longer holds.

## Technical Approach

### Guard Bands
When calibrating on block k, exclude g adjacent observations from training. Under β-mixing, residual dependence is O(β(g)^{δ/(2+δ)}). Setting g = b (guard band equals block size) balances the bias-variance trade-off.

### Main Theorem
Coverage guarantee decomposes into:
- Mixing gap from temporal dependence
- Product-bias term from nuisance estimation
- Adaptation term from online calibration

Under geometric β-mixing and standard nuisance convergence, asymptotic rate matches the exchangeable case.

## Key Findings

| Regime | VS-DR-ACI Coverage | VS-DR-ACI Width | Alternatives |
|--------|-------------------|-----------------|--------------|
| Stationary | 90.0% | Narrowest | All valid |
| Dependence only (ρ=0.95) | 89.9% | 4.9 | All valid but wider |
| Dependence + Drift | 89.9% | 4.9 | Split: -29pp, Bootstrap: 46× wider |

**Critical finding**: VS-DR-ACI is the only method maintaining valid coverage AND stable width under combined temporal dependence and distribution drift.

## Application

Applied to **Nasdaq's Dynamic M-ELO rollout** to produce stock-level prediction intervals for hidden-order execution quality. Temporal dependence is unavoidable in market microstructure data (volatility clustering, autocorrelated order flow).

## Simulation Calibration

Parameters calibrated from German Bund futures (RX1) limit order book data:
- GARCH persistence ≈ 0.98
- Student-t degrees of freedom ≈ 4
- Heavy tails (kurtosis 105)

## Related Work

- [[sources/zaffran-2022-aci|Zaffran et al. (2022)]] - ACI for time series
- Lei & Candès (2021) - Conformal causal inference (assumes exchangeability)
- [[concepts/double-machine-learning|Chernozhukov et al. (2018)]] - DML product-bias

## Notable Quotes

> "The goal is finite-sample coverage control for individual treatment effect estimates without assuming independent observations."

> "The theoretical mixing bound is conservative in practice; tightening it remains an open problem."

## Scope of Guarantees

- **What is covered**: DR pseudo-outcomes ψ_t^DR under temporal dependence
- **What is guaranteed**: Finite-horizon coverage error decomposition
- **What links to CATEs**: Asymptotic CATE containment when point estimator is consistent
- **What is NOT proved**: Finite-sample (1-α)-coverage for latent CATE τ(X_t)

## Questions Raised

- Can the switch coefficient bound be tightened? (Empirical coverage exceeds theory at ρ=0.99)
- Formal efficiency bounds for VS-DR-ACI?
- Extension to continuous treatments?

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]]
- [[concepts/beta-mixing|β-Mixing]]
- [[concepts/double-machine-learning|Double Machine Learning]]

<!-- AUTHORED REGION END -->
