---
title: Conformal Prediction
page_id: concepts/conformal-prediction
page_type: concept
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [uncertainty-quantification, prediction-intervals, machine-learning]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci, sources/johnstone-2025-multioutput, sources/vovk-2005-alrw]
related: [concepts/split-conformal-prediction, concepts/adaptive-conformal-inference, concepts/coverage-guarantee, concepts/exchangeability, concepts/prediction-intervals]
mind_map_priority: high
---

# Conformal Prediction

**Conformal prediction (CP)** is a framework for constructing prediction sets or intervals that come with finite-sample, distribution-free validity guarantees. Unlike traditional confidence intervals that rely on asymptotic approximations or distributional assumptions, conformal prediction provides exact coverage guarantees under only the assumption of [[concepts/exchangeability|exchangeability]].

## Core Idea

Given training data and a new test point, conformal prediction asks: "How well does a candidate prediction conform to the patterns seen in the training data?" By measuring this conformity through a **conformity score** (or nonconformity score), CP constructs prediction sets containing all candidate values that are not "too nonconforming."

## Key Properties

1. **Finite-sample validity**: Coverage guarantees hold for any sample size, not just asymptotically
2. **Distribution-free**: No assumptions on the data distribution beyond exchangeability
3. **Model-agnostic**: Works with any underlying prediction model (neural networks, random forests, etc.)
4. **Guaranteed coverage**: For a user-specified miscoverage rate α, the prediction set contains the true value with probability ≥ 1-α

## Mathematical Foundation

For data (X₁,Y₁),...,(Xₙ,Yₙ) and a new point Xₙ₊₁, conformal prediction constructs a set Cₐ(Xₙ₊₁) such that:

P{Yₙ₊₁ ∈ Cₐ(Xₙ₊₁)} ≥ 1 - α

This is achieved by computing conformity scores and including all candidate values whose scores are not among the most extreme.

## Variants

- [[concepts/split-conformal-prediction|Split Conformal Prediction]]: Computationally efficient variant using data splitting
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]: Extension for time series and distribution shift
- Full conformal prediction: Uses all data but computationally expensive
- Cross-conformal prediction: Uses cross-validation for better efficiency

## Applications

- [[concepts/uncertainty-quantification|Uncertainty quantification]] for black-box models
- Medical diagnosis with guaranteed error rates
- Electricity price forecasting ([[entities/margaux-zaffran|Zaffran]]'s work)
- Financial risk assessment
- Autonomous systems requiring safety guarantees

## Historical Context

Conformal prediction was developed by [[entities/vladimir-vovk|Vladimir Vovk]], Alex Gammerman, and Glenn Shafer in the late 1990s and early 2000s, with the foundational text "Algorithmic Learning in a Random World" (2005) establishing the theoretical framework.

## See Also

- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/calibration|Calibration]]
