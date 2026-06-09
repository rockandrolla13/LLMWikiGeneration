---
created: 2026-04-28 14:00:00+00:00
mind_map_priority: medium
page_id: concepts/causal-inference
page_type: concept
related:
- concepts/adaptive-conformal-inference
- concepts/at-at-theory-causal-influence
- concepts/average-treatment-effect
- concepts/back-door-front-door-adjustment
- concepts/backward-causation
- concepts/bayesian-additive-regression-trees
- concepts/beta-mixing
- concepts/causal-dags-confounding-selection-bias
- concepts/causal-diagram
- concepts/causal-identifiability-conditions
- concepts/causal-theory-of-time-direction
- concepts/conditional-independence-assumption
- concepts/conditional-independence-test
- concepts/conformal-prediction
- concepts/confounding
- concepts/correlation-vs-causation
- concepts/counterfactual-conditional
- concepts/counterfactuals
- concepts/difference-in-differences
- concepts/do-operator
- concepts/doubly-robust-estimation
- concepts/empirical-evaluation-causal-inference
- concepts/feedback-loops
- concepts/g-methods-time-varying-treatments
- concepts/heterogeneous-treatment-effects
- concepts/humes-problem-of-causation
- concepts/instrumental-variables
- concepts/interaction-analysis
- concepts/interrupted-time-series-design
- concepts/inverse-probability-weighting
- concepts/ip-weighting-marginal-structural-models
- concepts/ladder-of-causation
- concepts/mediation-analysis
- concepts/potential-outcomes
- concepts/probabilistic-causality
- concepts/propensity-score
- concepts/quantile-treatment-effects
- concepts/quasi-experimental-design
- concepts/randomised-controlled-trial
- concepts/regression-discontinuity
- concepts/regression-to-the-mean
- concepts/scientific-explanation
- concepts/singularist-causation
- concepts/spillover-interference-effects
- concepts/systems-thinking
- concepts/temporal-cross-fitting
- concepts/unconfoundedness-assumption
- concepts/unmeasured-confounding-sensitivity-analysis
revision_id: 3
sources:
- sources/koukorinis-2026-draci
tags:
- causal-inference
- statistics
- treatment-effects
- econometrics
title: Causal Inference
updated: '2026-06-09T12:00:00Z'
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

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/at-at-theory-causal-influence|at-at-theory-causal-influence]]
- [[concepts/back-door-front-door-adjustment|back-door-front-door-adjustment]]
- [[concepts/backward-causation|backward-causation]]
- [[concepts/causal-dags-confounding-selection-bias|causal-dags-confounding-selection-bias]]
- [[concepts/causal-diagram|causal-diagram]]
- [[concepts/causal-identifiability-conditions|causal-identifiability-conditions]]
- [[concepts/causal-theory-of-time-direction|causal-theory-of-time-direction]]
- [[concepts/conditional-independence-assumption|conditional-independence-assumption]]
- [[concepts/confounding|confounding]]
- [[concepts/correlation-vs-causation|correlation-vs-causation]]
- [[concepts/counterfactual-conditional|counterfactual-conditional]]
- [[concepts/counterfactuals|counterfactuals]]
- [[concepts/difference-in-differences|difference-in-differences]]
- [[concepts/do-operator|do-operator]]
- [[concepts/doubly-robust-estimation|doubly-robust-estimation]]
- [[concepts/feedback-loops|feedback-loops]]
- [[concepts/g-methods-time-varying-treatments|g-methods-time-varying-treatments]]
- [[concepts/humes-problem-of-causation|humes-problem-of-causation]]
- [[concepts/instrumental-variables|instrumental-variables]]
- [[concepts/interaction-analysis|interaction-analysis]]
- [[concepts/ip-weighting-marginal-structural-models|ip-weighting-marginal-structural-models]]
- [[concepts/ladder-of-causation|ladder-of-causation]]
- [[concepts/mediation-analysis|mediation-analysis]]
- [[concepts/potential-outcomes|potential-outcomes]]
- [[concepts/probabilistic-causality|probabilistic-causality]]
- [[concepts/quantile-treatment-effects|quantile-treatment-effects]]
- [[concepts/regression-discontinuity|regression-discontinuity]]
- [[concepts/regression-to-the-mean|regression-to-the-mean]]
- [[concepts/scientific-explanation|scientific-explanation]]
- [[concepts/singularist-causation|singularist-causation]]
- [[concepts/spillover-interference-effects|spillover-interference-effects]]
- [[concepts/systems-thinking|systems-thinking]]
- [[concepts/unmeasured-confounding-sensitivity-analysis|unmeasured-confounding-sensitivity-analysis]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/average-treatment-effect|average-treatment-effect]]
- [[concepts/bayesian-additive-regression-trees|bayesian-additive-regression-trees]]
- [[concepts/causal-identifiability-conditions|causal-identifiability-conditions]]
- [[concepts/conditional-independence-test|conditional-independence-test]]
- [[concepts/confounding|confounding]]
- [[concepts/empirical-evaluation-causal-inference|empirical-evaluation-causal-inference]]
- [[concepts/heterogeneous-treatment-effects|heterogeneous-treatment-effects]]
- [[concepts/interrupted-time-series-design|interrupted-time-series-design]]
- [[concepts/inverse-probability-weighting|inverse-probability-weighting]]
- [[concepts/potential-outcomes|potential-outcomes]]
- [[concepts/propensity-score|propensity-score]]
- [[concepts/quasi-experimental-design|quasi-experimental-design]]
- [[concepts/randomised-controlled-trial|randomised-controlled-trial]]
- [[concepts/unconfoundedness-assumption|unconfoundedness-assumption]]