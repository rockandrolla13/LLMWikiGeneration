---
created: 2026-04-26 12:00:00+00:00
mind_map_priority: medium
page_id: concepts/quantile-regression
page_type: concept
related:
- concepts/distributional-conformal-prediction
- concepts/nonparametric-conditional-moment-test
- concepts/optimum-score-estimation
- concepts/prediction-intervals
- concepts/probability-integral-transform
- concepts/quantile-treatment-effects
- concepts/tick-loss
revision_id: 4
sources:
- sources/chernozhukov-2021-distributional-cp
- sources/peiris-2025-rnn-har-var
- sources/barendse-2026-efficient-tail-interquantile
tags:
- regression
- statistics
- prediction-intervals
- econometrics
title: Quantile Regression
updated: '2026-06-09T12:00:00Z'
---

# Quantile Regression

**Quantile regression** is a statistical technique for estimating conditional quantile functions, providing a more complete view of the conditional distribution than mean regression alone.

## Core Idea

While ordinary least squares (OLS) estimates E[Y|X], quantile regression estimates the τ-th conditional quantile:

> Q(τ, x) = inf{y : P(Y ≤ y | X = x) ≥ τ}

for any τ ∈ (0,1). This allows modeling the full conditional distribution.

## Mathematical Formulation

### Linear Quantile Regression
Assumes Q(τ, x) = x⊤β(τ) and estimates:

> β̂(τ) = argmin_β Σᵢ ρ_τ(Yᵢ - Xᵢ⊤β)

where ρ_τ(u) = u(τ - 1{u < 0}) is the **check function** or **pinball loss**.

### Properties
- For τ = 0.5, minimizes median absolute deviation
- No distributional assumptions required
- Robust to outliers (compared to least squares)
- Coefficient β(τ) varies with τ, revealing heterogeneous effects

## Key Advantages

1. **Robustness**: Less sensitive to outliers than mean regression
2. **Heterogeneity**: Captures how covariate effects vary across the distribution
3. **Full distribution**: By fitting multiple quantiles, recovers the entire conditional distribution
4. **Heteroskedasticity**: Naturally handles non-constant variance

## Connection to Conformal Prediction

Quantile regression is central to several [[concepts/conformal-prediction|conformal prediction]] methods:

### Conformalized Quantile Regression (CQR)
Uses quantile estimates to form prediction intervals:
> Ĉ(x) = [Q̂(α/2, x) - c, Q̂(1-α/2, x) + c]

where c is a calibration correction.

### Distributional Conformal Prediction
[[concepts/distributional-conformal-prediction|DCP]] uses quantile regression to estimate the full conditional CDF:
> F̂(y,x) = ∫₀¹ 1{Q̂(τ,x) ≤ y} dτ

This enables using the [[concepts/probability-integral-transform|probability integral transform]] for [[concepts/conditional-validity|conditional validity]].

## Distribution Regression

Extends quantile regression by directly modeling the conditional CDF:

> F(y,x) = P(Y ≤ y | X = x)

Can be estimated by fitting quantile regression at many τ values and integrating, or by direct parametric/nonparametric methods.

## Applications

- **Economics**: Wage distributions, returns heterogeneity
- **Finance**: Value-at-Risk (VaR), expected shortfall
- **Health**: Patient outcome variability
- **Environmental science**: Extreme event modeling
- **Machine learning**: Prediction intervals via neural network quantile regression

## Extensions

- **Quantile random forests**: Nonparametric quantile estimation
- **Quantile neural networks**: Deep learning for quantile functions
- **Bayesian quantile regression**: Uncertainty in quantile estimates
- **Censored quantile regression**: For survival data

## Historical Note

Quantile regression was introduced by Roger Koenker and Gilbert Bassett in 1978, building on earlier work on median regression and L₁ estimation.

## See Also

- [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/probability-integral-transform|Probability Integral Transform]]
- [[sources/chernozhukov-2021-distributional-cp|Chernozhukov et al. (2021)]]
- [[sources/peiris-2025-rnn-har-var|Peiris, Tran, Wang, Gerlach (2025)]] — quantile loss (asymmetric Laplace) used as the working pseudo-likelihood for RNN-HAR Value-at-Risk forecasting under generalized Bayesian inference
- [[sources/barendse-2026-efficient-tail-interquantile|Barendse (2026)]] — first-stage quantile-regression nuisance estimation feeds into the efficient joint estimation of tail and interquantile expectations under Fissler-Ziegel loss

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/optimum-score-estimation|optimum-score-estimation]]
- [[concepts/quantile-treatment-effects|quantile-treatment-effects]]
- [[concepts/tick-loss|tick-loss]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/nonparametric-conditional-moment-test|nonparametric-conditional-moment-test]]