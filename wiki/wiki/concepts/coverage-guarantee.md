---
title: Coverage Guarantee
page_id: concepts/coverage-guarantee
page_type: concept
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [conformal-prediction, statistical-guarantee, validity]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci, sources/johnstone-2025-multioutput]
related: [concepts/conformal-prediction, concepts/prediction-intervals, concepts/calibration, concepts/exchangeability]
mind_map_priority: medium
---

# Coverage Guarantee

A **coverage guarantee** (also called **validity**) is the statistical property that a prediction interval or set contains the true value with at least a specified probability.

## Formal Definition

For a prediction set C(X) and miscoverage rate α ∈ (0,1):

**Marginal Coverage**: P{Y ∈ C(X)} ≥ 1 - α

This means that over repeated draws from the data distribution, the prediction set contains the true response at least (1-α) × 100% of the time.

## Types of Coverage

### Marginal Coverage
- Guarantee holds on average over the distribution of X
- This is what [[concepts/conformal-prediction|conformal prediction]] provides
- Easier to achieve than conditional coverage

### Conditional Coverage
- P{Y ∈ C(X) | X = x} ≥ 1 - α for all x
- Much stronger but generally impossible without distributional assumptions
- Some methods approximate this (e.g., localized conformal prediction)

### Approximate Coverage
- Coverage holds asymptotically or approximately
- Traditional confidence intervals often provide only this

## Why Coverage Matters

1. **Trust**: Users can rely on prediction intervals
2. **Decision-making**: Risk-based strategies require calibrated uncertainty
3. **Safety**: Critical applications need guaranteed error rates
4. **Fairness**: Coverage should hold across subgroups

## Measuring Coverage

- **Empirical coverage**: Fraction of test points where Y ∈ C(X)
- **Coverage gap**: |empirical coverage - (1-α)|
- **Conditional coverage analysis**: Check coverage within subgroups

## Trade-offs

Coverage is often traded against **efficiency** (interval width):
- Trivially, C(X) = ℝ always covers but is uninformative
- The goal is the smallest set achieving valid coverage

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/calibration|Calibration]]
