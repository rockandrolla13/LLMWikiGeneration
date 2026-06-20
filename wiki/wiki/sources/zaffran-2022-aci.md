---
title: Adaptive Conformal Predictions for Time Series
page_id: sources/zaffran-2022-aci
page_type: source
source_type: paper
revision_id: 1
created: 2026-04-10 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Margaux Zaffran
- Aymeric Dieuleveut
- Olivier Féron
- Yannig Goude
- Julie Josse
year: 2022
venue: arXiv (2202.07282)
tags:
- conformal-prediction
- time-series
- adaptive-methods
- electricity-forecasting
related:
- sources/zaffran-phd
- concepts/adaptive-conformal-inference
- concepts/conformal-prediction
- entities/margaux-zaffran
mind_map_priority: high
schema_version: 2
uuid: d8adaa93-ca97-5eab-842c-4c8c8b83afc9
content_hash: sha256:3928cf5c09f9b5c00e665349d7f56cafe01477ab918be5dce8fe69f8ad22e061
---

<!-- AUTHORED REGION START -->
# Adaptive Conformal Predictions for Time Series

**Authors:** [[entities/margaux-zaffran|Margaux Zaffran]], Aymeric Dieuleveut, Olivier Féron, Yannig Goude, Julie Josse

**Year:** 2022

**Venue:** arXiv preprint (2202.07282)

## Summary

This paper analyzes and extends [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference (ACI)]] for time series with general dependency, motivated by electricity price forecasting applications.

## Key Contributions

1. **Theoretical analysis of ACI**: The authors prove that ACI with learning rate γ:
   - Deteriorates efficiency in the exchangeable case
   - Improves efficiency in autoregressive settings with well-chosen γ

2. **AgACI (Aggregated ACI)**: A parameter-free method that:
   - Runs multiple ACI instances with different γ values
   - Uses online expert aggregation to combine them
   - Eliminates the need to tune γ manually

3. **Extensive benchmarking**: Comparison against:
   - EnbPI (Xu and Xie, 2021)
   - Online [[concepts/split-conformal-prediction|split conformal prediction]]
   - Various γ settings for ACI

4. **Real-world application**: French electricity price forecasting demonstrating practical value

## Problem Setting

[[concepts/conformal-prediction|Conformal prediction]] requires [[concepts/exchangeability|exchangeability]], which fails for time series due to:
- Temporal dependence
- Distribution shifts over time
- Non-stationarity

ACI addresses this by adaptively updating the miscoverage level:
- αₜ₊₁ = αₜ + γ(α - errₜ)
- If undercovering: intervals widen
- If overcovering: intervals narrow

## Key Findings

- Higher γ → faster adaptation but more variability
- Lower γ → more stable but slower to adapt
- AgACI achieves good performance without requiring γ selection

## Applications

- Day-ahead electricity price forecasting
- Any sequential prediction with potential distribution drift

## Notable Quotes

> "We argue that ACI, developed for distribution-shift time series, is a good procedure for time series with general dependency."

## Questions Raised

- How to extend to multivariate time series?
- Optimal aggregation strategies for expert combination?

## See Also

- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[sources/zaffran-phd|Zaffran PhD Thesis]]
- [[entities/margaux-zaffran|Margaux Zaffran]]

<!-- AUTHORED REGION END -->
