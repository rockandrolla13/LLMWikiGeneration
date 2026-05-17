---
title: Conformal Prediction
page_id: concepts/conformal-prediction
page_type: concept
revision_id: 3
created: 2026-04-10T18:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [uncertainty-quantification, prediction-intervals, machine-learning]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci, sources/johnstone-2025-multioutput, sources/vovk-2005-alrw, sources/xu-2022-spci, sources/sun-2022-copula-cpts, sources/lee-2024-kowcpi, sources/pasche-2025-extreme-conformal, sources/chernozhukov-2021-distributional-cp, sources/yang-2026-multi-distribution-robust-cp, sources/koukorinis-2026-draci]
related: [concepts/split-conformal-prediction, concepts/adaptive-conformal-inference, concepts/coverage-guarantee, concepts/exchangeability, concepts/prediction-intervals, concepts/spci, concepts/copulas, concepts/multi-step-conformal-prediction, concepts/kowcpi, concepts/extreme-value-theory, concepts/generalized-pareto-distribution, concepts/nadaraya-watson-estimator, concepts/distributional-conformal-prediction, concepts/conditional-validity, concepts/multi-distribution-robust-cp, concepts/doubly-robust-estimation, concepts/beta-mixing, concepts/causal-inference, concepts/temporal-cross-fitting]
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
- [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]: Achieves [[concepts/conditional-validity|conditional validity]] via [[concepts/probability-integral-transform|probability integral transform]] ([[sources/chernozhukov-2021-distributional-cp|Chernozhukov et al., 2021]])
- [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]]: Uniform validity across multiple heterogeneous distributions ([[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin, 2026]])
- [[concepts/spci|SPCI]]: Sequential Predictive Conformal Inference using quantile regression on residuals
- [[concepts/kowcpi|KOWCPI]]: Kernel-based Optimally Weighted CP using [[concepts/nadaraya-watson-estimator|Nadaraya-Watson]] estimator ([[sources/lee-2024-kowcpi|Lee et al., 2024]])
- [[concepts/multi-step-conformal-prediction|Multi-step Conformal Prediction]]: Methods for full-horizon validity including [[concepts/copulas|copula]]-based approaches
- **Extreme Conformal Prediction**: Bridges [[concepts/extreme-value-theory|extreme value theory]] with CP for high-confidence intervals ([[sources/pasche-2025-extreme-conformal|Pasche et al., 2025]])
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

## Time Series Extensions

Extending CP to time series is challenging because sequential data violates [[concepts/exchangeability|exchangeability]]:

- **EnbPI** (Xu & Xie, 2021b): Ensemble methods with rolling residual updates
- **[[concepts/spci|SPCI]]** ([[sources/xu-2022-spci]]): Uses [[concepts/quantile-random-forest|quantile random forests]] on residuals to exploit temporal correlation
- **[[concepts/kowcpi|KOWCPI]]** ([[sources/lee-2024-kowcpi]]): Kernel-based method using [[concepts/nadaraya-watson-estimator|Reweighted Nadaraya-Watson]] for optimal weights with asymptotic conditional coverage
- **[[sources/sun-2022-copula-cpts|CopulaCPTS]]**: [[concepts/copulas|Copula]]-based method for multi-step forecasting with full-horizon validity
- **[[sources/koukorinis-2026-draci|DR-ACI]]**: [[concepts/doubly-robust-estimation|Doubly robust]] adaptive conformal inference for [[concepts/causal-inference|causal effects]] under [[concepts/beta-mixing|beta-mixing]]

## Extreme Confidence Levels

For high-impact events requiring very high confidence (e.g., 99.99%), classical CP fails when $\alpha < 1/(n_c + 1)$:

- **Extreme Conformal Prediction** ([[sources/pasche-2025-extreme-conformal|Pasche et al., 2025]]): Uses [[concepts/generalized-pareto-distribution|GPD]] from [[concepts/extreme-value-theory|extreme value theory]] to extrapolate calibration score quantiles beyond the data range
- Enables informative prediction intervals at confidence levels orders of magnitude beyond classical methods
- Weighted version handles nonstationary data (e.g., seasonal patterns)

## Conditional and Distributional Validity

Standard CP only guarantees **marginal** coverage. For [[concepts/conditional-validity|conditional validity]] (coverage for specific feature values):

- **[[concepts/distributional-conformal-prediction|Distributional CP]]** ([[sources/chernozhukov-2021-distributional-cp|Chernozhukov et al., 2021]]): Uses estimated conditional ranks instead of residuals, achieving approximate conditional validity under consistent distribution estimation
- Exploits [[concepts/probability-integral-transform|probability integral transform]]: If F(y|x) is the true conditional CDF, then F(Y,X) is uniform and independent of X

## Multi-Distribution Robustness

When data comes from multiple heterogeneous sources:

- **[[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]]** ([[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin, 2026]]): Achieves valid coverage across all sources simultaneously
- Uses [[concepts/max-p-aggregation|max-p aggregation]] for finite-sample [[concepts/worst-case-coverage|worst-case coverage]]
- Applications: fairness without protected attributes, subpopulation shift, federated learning

## See Also

- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/calibration|Calibration]]
- [[concepts/conditional-validity|Conditional Validity]]
- [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]
- [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]]
- [[concepts/spci|SPCI]]
- [[concepts/kowcpi|KOWCPI]]
- [[concepts/extreme-value-theory|Extreme Value Theory]]
- [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution]]
- [[concepts/multi-step-conformal-prediction|Multi-step Conformal Prediction]]
