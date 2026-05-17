---
title: "Distributional Conformal Prediction"
page_id: sources/chernozhukov-2021-distributional-cp
page_type: source
revision_id: 1
created: 2026-04-26T12:00:00Z
updated: 2026-04-26T12:00:00Z
authors: [Victor Chernozhukov, Kaspar Wüthrich, Yinchu Zhu]
publication: PNAS
year: 2021
arxiv: "1909.07889"
tags: [conformal-prediction, quantile-regression, distribution-regression, conditional-validity, heteroskedasticity]
related: [concepts/conformal-prediction, concepts/distributional-conformal-prediction, concepts/conditional-validity, concepts/probability-integral-transform, concepts/quantile-regression]
mind_map_priority: high
---

# Distributional Conformal Prediction

## Summary

This paper proposes **Distributional Conformal Prediction (DCP)**, a robust method for constructing prediction intervals that are approximately valid conditional on the full vector of predictors. Unlike standard conformal prediction methods based on modeling the conditional mean, DCP exploits the [[concepts/probability-integral-transform|probability integral transform]] and relies on permuting estimated ranks. This approach naturally handles [[concepts/heteroskedasticity|heteroskedasticity]] and achieves [[concepts/conditional-validity|conditional validity]].

## Key Contributions

1. **Novel conformity score**: Uses conditional ranks from estimated conditional distributions rather than regression residuals
2. **Conditional validity**: Achieves approximate validity conditional on predictors, not just marginal validity
3. **Heteroskedasticity adaptation**: Prediction intervals automatically adapt to heteroskedasticity without explicit modeling
4. **Optimal DCP extension**: Proposes a "shape adjustment" method that yields shortest possible prediction intervals
5. **Theoretical guarantees**: Establishes both finite-sample and asymptotic validity under various conditions

## Core Method

### Probability Integral Transform
The key insight is that for the conditional CDF F(y,x) = P(Y ≤ y | X = x), the conditional rank U_t := F(Y_t, X_t) is uniformly distributed on (0,1) and **independent of X_t**. This independence property allows construction of conditionally valid prediction intervals.

### Algorithm (Split DCP)
1. Split data into training and calibration sets
2. Estimate conditional CDF F̂ using quantile regression or distribution regression
3. Compute estimated ranks Û_t = F̂(Y_t, X_t) on calibration data
4. For test point X_{n+1}, construct prediction interval by inverting the quantile function using calibrated thresholds

### Conformity Score
The baseline conformity score is:
- ψ(y,x) = |F(y,x) - 1/2|

For optimal DCP with asymmetric distributions:
- ψ*(y,x) = |F(y,x) - b(x,α) - (1-α)/2|

where b(x,α) is a "shape adjustment" solving an optimization problem.

## Theoretical Results

### Theorem 1: Finite-Sample Unconditional Validity
Under exchangeability and permutation-invariant estimators:
> P(Y_{T+1} ∈ Ĉ(X_{T+1})) ≥ 1 - α

### Theorem 3: Asymptotic Conditional Validity
Under consistent estimation of F:
> P(Y_{T+1} ∈ Ĉ(X_{T+1}) | X_{T+1}) → 1 - α as T → ∞

### Theorem 4: Optimal DCP
Under suitable conditions, the optimal DCP achieves the shortest possible conditionally valid prediction interval asymptotically.

## Comparison with Related Methods

| Method | Conditional Validity | Handles Heteroskedasticity | Computational Cost |
|--------|---------------------|---------------------------|-------------------|
| Mean-based CP | No | No (fixed length) | Low |
| CQR (Romano et al.) | Approximate | Yes | Moderate |
| **DCP (this paper)** | Yes (asymptotic) | Yes (via ranks) | Moderate |

## Applications Demonstrated

1. **Stock return prediction**: DCP maintains 90% coverage across all volatility levels, while mean-based CP drops to ~50% during high-volatility periods
2. **Wage prediction**: DCP achieves near-90% coverage for individuals with different education/experience combinations

## Notable Quotes

> "Unlike regression residuals, ranks are independent of the predictors, allowing us to construct conditionally valid prediction intervals under heteroskedasticity."

> "Our approach exploits the probability integral transform and relies on permuting estimated ranks."

## Questions Raised

- How does DCP perform with high-dimensional predictors?
- Can the method be extended to multivariate responses?
- What is the finite-sample loss in conditional coverage?

## Related Concepts

- [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]
- [[concepts/probability-integral-transform|Probability Integral Transform]]
- [[concepts/conditional-validity|Conditional Validity]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/quantile-regression|Quantile Regression]]

## Related Entities

- [[entities/victor-chernozhukov|Victor Chernozhukov]] - MIT economist, lead author
- [[entities/kaspar-wuthrich|Kaspar Wüthrich]] - UC San Diego, econometrics
- [[entities/yinchu-zhu|Yinchu Zhu]] - Brandeis University, statistics
