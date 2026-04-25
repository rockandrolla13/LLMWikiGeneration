---
title: Adaptive Conformal Inference
page_id: concepts/adaptive-conformal-inference
page_type: concept
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [conformal-prediction, time-series, distribution-shift, online-learning]
sources: [sources/zaffran-2022-aci, sources/zaffran-phd]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/coverage-guarantee, concepts/exchangeability]
mind_map_priority: high
---

# Adaptive Conformal Inference

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

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/split-conformal-prediction|Split Conformal Prediction]]
- [[entities/margaux-zaffran|Margaux Zaffran]]
