---
title: 'Extreme Conformal Prediction: Reliable Intervals for High-Impact Events'
page_id: sources/pasche-2025-extreme-conformal
page_type: source
revision_id: 1
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- extreme-value-theory
- prediction-intervals
- high-confidence
- flood-risk
- heavy-tails
authors:
- Olivier C. Pasche
- Henry Lam
- Sebastian Engelke
year: 2025
journal: Extremes
sources: []
related:
- concepts/conformal-prediction
- concepts/extreme-value-theory
- concepts/generalized-pareto-distribution
- concepts/coverage-guarantee
- concepts/prediction-intervals
- entities/olivier-pasche
- entities/sebastian-engelke
mind_map_priority: high
schema_version: 2
uuid: 2974e4b3-aaf5-504d-bd22-8f21cb8e1650
content_hash: sha256:22076c30bf9f87a1d7bb38a4bf030776b5c86bdafd25c49993deae4ec7a7898c
---

<!-- AUTHORED REGION START -->
# Extreme Conformal Prediction: Reliable Intervals for High-Impact Events

**Pasche, Lam, and Engelke (2025)** propose a novel method bridging [[concepts/extreme-value-theory|extreme value statistics]] and [[concepts/conformal-prediction|conformal prediction]] to construct reliable prediction intervals for high-impact events requiring very high confidence levels (e.g., 99.99%).

## Motivation

In applications with potentially high-impact events (flooding, financial crises), regulators often require prediction intervals with very high confidence. Classical conformal methods fail when:
- The desired confidence level $1 - \alpha$ exceeds $n_c/(n_c + 1)$ where $n_c$ is calibration set size
- The empirical quantile $\hat{q}_\alpha$ becomes infinite, yielding uninformative intervals

## Key Contribution

The paper overcomes this limitation by:
1. Using extreme quantile regression methods for initial predictions
2. Applying [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution (GPD)]] to extrapolate calibration score quantiles beyond the data range
3. Providing theoretical guarantees via confidence intervals for extreme quantiles

## Methodology

### Classical Conformal Limitation
For confidence level $1 - \alpha > n_c/(n_c + 1)$:
- Classical method returns $\hat{q}_\alpha = \infty$
- Results in degenerate trivial intervals $\hat{C}(\mathbf{x}) = (-\infty, \infty)$

### Extreme Conformal Prediction
The method uses peaks-over-threshold (POT) methodology:

1. **Fit extreme quantile regression** on training data
2. **Calibration**: Approximate tail distribution of scores $S_i = s(\mathbf{X}_i, Y_i)$ using GPD:
   $$\mathbb{P}\{S - u \leq y | S > u\} \approx G_{\xi, \sigma(u)}(y)$$
   where $G_{\xi, \sigma}$ is the GPD with shape $\xi$ and scale $\sigma$

3. **Extrapolate** quantile estimates beyond the data range using:
   $$\hat{Q}_{1-\alpha}^{\text{GPD}} = u + \frac{\sigma}{\xi}\left[\left(\frac{\alpha}{\tau_0}\right)^{-\xi} - 1\right]$$

### Conservative CI-Based Approach
To ensure valid coverage despite estimation/approximation biases:
- Use upper endpoint of $(1-\alpha_2)$-confidence interval for the $(1-\alpha_1)$-quantile
- Natural choice: $\alpha_1 = \alpha_2 = 1 - (1-\alpha)^{1/2}$ (Sidak correction)

**Proposition 3.1**: If the confidence interval has correct coverage and $\alpha_1 + \alpha_2 - \alpha_1\alpha_2 \leq \alpha$, then the resulting extreme conformal prediction interval satisfies the marginal [[concepts/coverage-guarantee|coverage guarantee]].

## GPD Confidence Interval Methods

The paper evaluates three methods:
1. **Profile likelihood**: Most conservative, occasional numerical difficulties
2. **Bootstrap**: Reliable but potentially less conservative
3. **Delta method**: Computationally efficient but symmetric (unrealistic for large quantiles)

**Recommended**: "GPD safeprofile" - use profile likelihood, fall back to bootstrap when numerically unstable.

## Weighted Extension for Nonstationary Data

For nonexchangeable data, the method extends to weighted conformal prediction:
- Assign weights $w_i \in [0,1]$ reflecting similarity to test observation
- Use weighted GPD likelihood for inference:
  $$\ell_w(\sigma, \xi) = \sum_{i: S_i > u} w_i \log g_{\xi, \sigma}(S_i - u)$$

## Experimental Results

### Simulation Study
- Heavy-tailed Student-t noise: GPD profile method achieves valid coverage for confidence levels up to $1 - 10^{-5}$
- Light-tailed Gaussian noise: All CI-based methods somewhat overconservative
- Poor base model (linear GPD): Still achieves valid marginal coverage

### Flood Risk Application
Applied to one-day-ahead forecasting of Aare river discharge in Bern, Switzerland:
- Sinusoidal weights for seasonal adjustment (24 blocks per year)
- **Results**: Extreme PIs significantly outperform classical method for all relevant confidence levels
- Classical method yields infinite PIs for $1-\alpha > 0.999$; extreme method provides informative finite intervals

## Extreme Quantile Regression Models

The paper uses several base prediction models:
- **EQRN**: Extreme quantile regression neural networks (best performance)
- **GBEX**: Gradient boosting for extremes
- **EGAM**: Extreme generalized additive models
- **EXQAR**: Extreme quantile autoregressive models

## Practical Recommendations

1. Use **GPD safeprofile** method for conservative coverage
2. For seasonal data, use **weighted extreme conformal** with appropriate periodic weights
3. The method works with **any black-box** extreme quantile regression model

## Implementation

Open-source R packages available:
- `ExtremeConformal`: Main method implementation
- `ExtremeCI`: Profile-likelihood confidence intervals for extreme quantiles
- Reproducibility code: `github.com/opasche/Reprod_ExtremeConformalPred`

## Limitations

- Potential overconservativeness for moderately extreme levels
- Lacks finite-sample guarantees (relies on asymptotic extreme value theory)
- Tradeoff: Cannot guarantee quantile extrapolation without distributional assumptions

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/extreme-value-theory|Extreme Value Theory]]
- [[concepts/generalized-pareto-distribution|Generalized Pareto Distribution]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/prediction-intervals|Prediction Intervals]]

<!-- AUTHORED REGION END -->
