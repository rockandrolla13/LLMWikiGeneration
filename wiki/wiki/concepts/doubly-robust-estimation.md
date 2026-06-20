---
created: 2026-04-28 12:45:00+00:00
page_id: concepts/doubly-robust-estimation
page_type: concept
related:
- concepts/adaptive-conformal-inference
- concepts/average-treatment-effect
- concepts/causal-inference
- concepts/conformal-prediction
- concepts/confounding
- concepts/double-machine-learning
- concepts/ip-weighting-marginal-structural-models
revision_id: 3
sources:
- sources/gentzel-2021-osrct-evaluation
- sources/hernan-2020-causal-inference-what-if
- sources/hill-2011-bart-causal-inference
- sources/koukorinis-2026-draci
tags:
- causal-inference
- statistics
- methodology
title: Doubly Robust Estimation
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: e52f4695-f6a1-50a3-96ba-76a82fe6acf3
content_hash: sha256:9fa5ab0da3ca89ca52f7e2742b818083d12c6c2ad682bbe9fc8b3c89a75261da
---

<!-- AUTHORED REGION START -->
# Doubly Robust Estimation

## Definition

Doubly robust (DR) estimation is a technique in causal inference that combines two models—a propensity score model and an outcome regression model—to estimate treatment effects. The key property is that the estimator is consistent if **either** model is correctly specified, not necessarily both.

## The Doubly Robust Pseudo-Outcome

For binary treatment W ∈ {0,1} with covariates X and outcome Y:

$$\psi^{DR} = \hat\mu_1(X) - \hat\mu_0(X) + \frac{W(Y - \hat\mu_1(X))}{\hat{e}(X)} - \frac{(1-W)(Y - \hat\mu_0(X))}{1 - \hat{e}(X)}$$

Where:
- ê(X) = estimated propensity score P(W=1|X)
- μ̂_w(X) = estimated conditional outcome E[Y|X, W=w]

## Product-Bias Property

The bias of the DR pseudo-outcome is bounded by the **product** of nuisance errors:

$$\text{Bias} = O(\|\hat{e} - e\|_2 \cdot \|\hat\mu - \mu\|_2)$$

Not the sum. This means:
- If propensity score is perfect → bias = 0 regardless of outcome model
- If outcome model is perfect → bias = 0 regardless of propensity score
- If both have moderate error → bias is small (product of two small terms)

## Connection to Double Machine Learning

[[concepts/double-machine-learning|Double Machine Learning (DML)]] formalizes this in a Neyman-orthogonal framework where:
- Cross-fitting prevents overfitting bias
- Product-bias rate enables √n-consistent inference even with slow ML nuisance estimators

## Applications in Conformal Prediction

In [[sources/koukorinis-2026-draci|DR-ACI]], doubly robust pseudo-outcomes serve as the calibration target for [[concepts/conformal-prediction|conformal prediction]]:
- Intervals calibrated for ψ^DR provide finite-sample coverage guarantees
- CATE τ(X) coverage follows as a derived implication when point estimator is consistent

## Under Temporal Dependence

The product-bias property extends to β-mixing time series via **temporal block cross-fitting with guard bands**:
- Guard bands ensure training-calibration separation
- Coupling remainder is O(β(g)^{δ/(2+δ)}) where g is guard band size
- This is a key technical contribution of [[sources/koukorinis-2026-draci|DR-ACI]]

## Advantages

- Robustness to model misspecification
- Efficiency (achieves semiparametric efficiency bound)
- Compatibility with machine learning estimators

## Limitations

- Requires overlap assumption (propensity scores bounded away from 0 and 1)
- Variance can inflate when propensity scores are extreme
- Does not provide direct CATE coverage—only pseudo-outcome coverage

## See Also

- [[concepts/double-machine-learning|Double Machine Learning]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper]]
- [[concepts/conformal-prediction|Conformal Prediction]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/hernan-2020-causal-inference-what-if]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/gentzel-2021-osrct-evaluation]], [[sources/hill-2011-bart-causal-inference]]
<!-- AUTHORED REGION END -->
