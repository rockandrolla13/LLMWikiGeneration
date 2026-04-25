---
title: Calibration
page_id: concepts/calibration
page_type: concept
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [probability, uncertainty-quantification, model-evaluation]
sources: [sources/zaffran-phd]
related: [concepts/conformal-prediction, concepts/coverage-guarantee, concepts/uncertainty-quantification, concepts/split-conformal-prediction]
mind_map_priority: medium
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
