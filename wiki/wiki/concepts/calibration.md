---
created: 2026-04-10 18:00:00+00:00
mind_map_priority: medium
page_id: concepts/calibration
page_type: concept
related:
- concepts/base-rates-reference-class-forecasting
- concepts/bayesian-inference
- concepts/conformal-prediction
- concepts/continuous-ranked-probability-score
- concepts/coverage-guarantee
- concepts/energy-score
- concepts/interval-score
- concepts/null-hypothesis-significance-testing
- concepts/split-conformal-prediction
- concepts/strictly-proper-scoring-rules
- concepts/superforecasting
- concepts/uncertainty-quantification
revision_id: 2
sources:
- sources/zaffran-phd
tags:
- probability
- uncertainty-quantification
- model-evaluation
title: Calibration
updated: '2026-06-09T12:00:00Z'
---

# Calibration

**Calibration** refers to the agreement between predicted probabilities or confidence levels and observed frequencies. A well-calibrated model's predictions match reality: when it says "90% confident," it should be correct 90% of the time.

## Formal Definition

A probabilistic predictor is **calibrated** if:

P{Y = 1 | P̂(Y=1|X) = p} = p for all p ∈ [0,1]

For prediction intervals: the interval with nominal coverage (1-α) should contain the true value approximately (1-α) × 100% of the time.

## Relationship to Conformal Prediction

[[concepts/conformal-prediction|Conformal prediction]] provides calibrated prediction intervals by construction:
- The [[concepts/coverage-guarantee|coverage guarantee]] ensures the interval contains the true value with probability ≥ 1-α
- This is a form of marginal calibration

However, conformal prediction provides **marginal** calibration, not conditional calibration (calibration for each specific X value).

## Miscalibration

### Overconfidence
- Predicted probabilities are too extreme
- Common in neural networks
- Intervals are too narrow

### Underconfidence
- Predicted probabilities are too conservative
- Intervals are too wide (inefficient)

## Measuring Calibration

### Reliability Diagrams
- Plot predicted probability vs. observed frequency
- Perfect calibration = diagonal line

### Expected Calibration Error (ECE)
- Average absolute difference between predicted and observed frequencies
- Binned calculation

### Coverage Analysis
- For intervals: empirical coverage vs. nominal coverage

## Calibration Methods

### Post-hoc Calibration
- Platt scaling
- Temperature scaling
- Isotonic regression

### Conformal Calibration
- Use [[concepts/split-conformal-prediction|split conformal prediction]] as calibration layer
- Achieves exact finite-sample calibration
- Works with any underlying model

## In the Context of [[entities/margaux-zaffran|Zaffran's]] Work

The calibration set in split conformal prediction is used to:
1. Compute conformity scores
2. Determine the quantile threshold
3. Ensure valid coverage without distributional assumptions

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/uncertainty-quantification|Uncertainty Quantification]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/base-rates-reference-class-forecasting|base-rates-reference-class-forecasting]]
- [[concepts/bayesian-inference|bayesian-inference]]
- [[concepts/continuous-ranked-probability-score|continuous-ranked-probability-score]]
- [[concepts/energy-score|energy-score]]
- [[concepts/interval-score|interval-score]]
- [[concepts/null-hypothesis-significance-testing|null-hypothesis-significance-testing]]
- [[concepts/strictly-proper-scoring-rules|strictly-proper-scoring-rules]]
- [[concepts/superforecasting|superforecasting]]