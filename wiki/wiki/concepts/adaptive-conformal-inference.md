---
title: Adaptive Conformal Inference
page_id: concepts/adaptive-conformal-inference
page_type: concept
revision_id: 2
created: 2026-04-10 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- distribution-shift
- online-learning
sources:
- sources/gibbs-2021-aci
- sources/zaffran-2022-aci
- sources/zaffran-phd
- sources/koukorinis-2026-draci
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/coverage-guarantee
- concepts/exchangeability
- concepts/doubly-robust-estimation
- concepts/beta-mixing
- concepts/causal-inference
mind_map_priority: high
schema_version: 2
uuid: bdc3f5a3-72df-5e46-a4be-2e144815a092
content_hash: sha256:3e854e8f9c23bb3446f296721834889f2fc2f86ebf7a95b706026450bdc5e9b1
---

<!-- AUTHORED REGION START -->
# Adaptive Conformal Inference

## Primary Source

Primary source: [[sources/gibbs-2021-aci|Gibbs & Candès (2021), "Adaptive Conformal Inference Under Distribution Shift"]]. This NeurIPS paper introduces the online α-update rule formalised below and proves the deterministic long-run coverage guarantee; it is the foundational reference for ACI.

**Adaptive Conformal Inference (ACI)** is an extension of [[concepts/conformal-prediction|conformal prediction]] designed to handle time series data and distribution shifts, where the standard [[concepts/exchangeability|exchangeability]] assumption does not hold.

## Motivation

Standard conformal prediction requires exchangeable data, which excludes:
- Time series with temporal dependence
- Data with distribution shifts over time
- Non-stationary processes

ACI addresses this by adaptively updating the miscoverage level based on recent prediction performance.

## Algorithm

ACI modifies [[concepts/split-conformal-prediction|split conformal prediction]] with an adaptive quantile level:

1. Initialize α₁ = α (target miscoverage rate)

2. For each time step t:
   - Construct prediction interval using current αₜ
   - Observe true value yₜ
   - Update: αₜ₊₁ = αₜ + γ(α - errₜ)

   where errₜ = 1{yₜ ∉ Ĉₐₜ(xₜ)} and γ > 0 is a learning rate

## Key Properties

- **Self-correcting**: If intervals undercover, αₜ decreases → wider intervals
- **Asymptotic validity**: Achieves target coverage rate over time
- **Handles distribution shift**: Adapts to changing data distributions
- **Learning rate γ**: Controls adaptation speed (tradeoff between stability and responsiveness)

## AgACI: Aggregated ACI

[[entities/margaux-zaffran|Zaffran et al.]] proposed **AgACI**, a parameter-free method that:
- Runs multiple ACI instances with different γ values
- Uses online expert aggregation to combine them
- Avoids the need to tune γ manually

## Applications

- Electricity price forecasting (highly non-stationary)
- Financial time series
- Any sequential prediction with potential distribution drift

## Comparison with EnbPI

Another approach for time series conformal prediction is **Ensemble Prediction Interval (EnbPI)** by Xu and Xie (2021), which uses ensemble methods and bootstrap aggregation. ACI and EnbPI represent different philosophies:
- ACI: Adapt the quantile level
- EnbPI: Use ensemble diversity for coverage

## Extension to Causal Inference: DR-ACI

[[sources/koukorinis-2026-draci|Koukorinis (2026)]] extends ACI to [[concepts/causal-inference|causal inference]] settings with [[concepts/beta-mixing|beta-mixing]] dependence:

**Doubly Robust Adaptive Conformal Inference (DR-ACI)**:
- Targets [[concepts/doubly-robust-estimation|doubly robust]] pseudo-outcomes rather than raw residuals
- Uses [[concepts/temporal-cross-fitting|temporal block cross-fitting with guard bands]] to preserve DML product-bias rates
- Provides coverage guarantees with explicit decomposition into mixing gap, nuisance-bias tax, and adaptation rate

The variance-standardized version (VS-DR-ACI) achieves 63% narrower intervals than alternatives while being the only method maintaining valid coverage under combined temporal dependence and distribution drift.

## Theoretical Guarantees

The ACI update rule provides a **deterministic** long-run coverage guarantee (Gibbs and Candes, 2021):

$$\left|\frac{1}{T}\sum_{t=1}^T \text{err}_t - \alpha\right| \leq O(T^{-1/2})$$

This guarantee holds for any score sequence, making it applicable to dependent data without distributional assumptions.

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/split-conformal-prediction|Split Conformal Prediction]]
- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]]
- [[concepts/beta-mixing|Beta-Mixing]]
- [[concepts/causal-inference|Causal Inference]]
- [[entities/margaux-zaffran|Margaux Zaffran]]
- [[entities/andreas-koukorinis|Andreas Koukorinis]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper]]

<!-- AUTHORED REGION END -->
