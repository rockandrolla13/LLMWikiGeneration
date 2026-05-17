---
title: "Causal Inference"
page_id: concepts/causal-inference
page_type: concept
revision_id: 1
created: 2026-04-28T14:00:00Z
updated: 2026-04-28T14:00:00Z
tags: [causal-inference, statistics, treatment-effects, econometrics]
sources: [sources/koukorinis-2026-draci]
related: [concepts/doubly-robust-estimation, concepts/conformal-prediction, concepts/adaptive-conformal-inference, concepts/beta-mixing, concepts/temporal-cross-fitting]
mind_map_priority: medium
---

# Causal Inference

**Causal inference** is the process of drawing conclusions about causal relationships from data, going beyond correlation to understand how interventions affect outcomes. It is fundamental to policy evaluation, medical trials, and economic analysis.

## Core Framework: Potential Outcomes

The **Rubin Causal Model** (potential outcomes framework) defines:
- $Y(1)$: outcome if treated
- $Y(0)$: outcome if not treated
- $W$: treatment indicator (0 or 1)
- $X$: observed covariates

**Fundamental Problem of Causal Inference:** For any unit, we observe either $Y(1)$ or $Y(0)$, never both.

## Key Estimands

### Average Treatment Effect (ATE)
$$\text{ATE} = \mathbb{E}[Y(1) - Y(0)]$$

### Conditional Average Treatment Effect (CATE)
$$\tau(x) = \mathbb{E}[Y(1) - Y(0) \mid X = x]$$

The CATE is the target of **heterogeneous treatment effect** estimation---understanding how effects vary across subpopulations.

## Identification Assumptions

For causal effects to be identified from observational data:

1. **Unconfoundedness** (Conditional Independence):
   $$(Y(0), Y(1)) \perp W \mid X$$
   Treatment is independent of potential outcomes given covariates.

2. **Overlap** (Positivity):
   $$0 < \eta \leq e(x) \leq 1 - \eta < 1$$
   where $e(x) = P(W=1 \mid X=x)$ is the propensity score. All units have positive probability of each treatment.

3. **SUTVA** (Stable Unit Treatment Value):
   No interference between units; treatment is well-defined.

## Estimation Methods

### Inverse Propensity Weighting (IPW)
Weight observations by inverse probability of their observed treatment:
$$\hat{\tau}_{\text{IPW}} = \frac{1}{n}\sum_i \frac{W_i Y_i}{\hat{e}(X_i)} - \frac{1}{n}\sum_i \frac{(1-W_i) Y_i}{1 - \hat{e}(X_i)}$$

### Outcome Regression
Estimate conditional outcomes directly:
$$\hat{\tau}_{\text{OR}}(x) = \hat\mu_1(x) - \hat\mu_0(x)$$

### Doubly Robust Estimation
[[concepts/doubly-robust-estimation|Doubly robust methods]] combine both approaches:
$$\psi^{\mathrm{DR}} = \hat\mu_1(X) - \hat\mu_0(X) + \frac{W(Y - \hat\mu_1(X))}{\hat{e}(X)} - \frac{(1-W)(Y - \hat\mu_0(X))}{1 - \hat{e}(X)}$$

Consistent if **either** propensity or outcome model is correct.

## Uncertainty Quantification

Standard methods for CATE uncertainty:
1. **Asymptotic variance**: Based on influence function
2. **Bootstrap**: Resample-based intervals
3. **Bayesian**: Posterior credible intervals

All require distributional assumptions or asymptotics.

### Conformal Inference for Causal Effects

[[sources/koukorinis-2026-draci|DR-ACI]] provides **distribution-free** prediction intervals by combining:
- [[concepts/doubly-robust-estimation|Doubly robust estimation]] for nuisance removal
- [[concepts/conformal-prediction|Conformal prediction]] for finite-sample coverage
- [[concepts/adaptive-conformal-inference|ACI]] for temporal dependence

The key insight: calibrate on the DR pseudo-outcome (observable) rather than the latent CATE.

## Temporal Dependence

Standard causal inference assumes independent observations. Extensions to time series face challenges:
- **Exchangeability fails**: Temporal ordering breaks symmetry
- **Mixing dependence**: Observations are correlated
- **Distribution shift**: Treatment effects may change over time

[[concepts/beta-mixing|Beta-mixing]] provides a framework for weakly dependent time series, with [[concepts/temporal-cross-fitting|temporal cross-fitting with guard bands]] enabling DML-style estimation.

## Applications

- **Policy evaluation**: Effects of economic interventions
- **Medical trials**: Drug efficacy and safety
- **A/B testing**: Product feature effects
- **Market design**: [[sources/koukorinis-2026-draci|Effect of market mechanism changes]] (e.g., Nasdaq M-ELO)

## See Also

- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/beta-mixing|Beta-Mixing]]
- [[concepts/temporal-cross-fitting|Temporal Cross-Fitting]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper]]
