---
title: Uncertainty Quantification
page_id: concepts/uncertainty-quantification
page_type: concept
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [machine-learning, statistics, decision-making]
sources: [sources/zaffran-phd, sources/johnstone-2025-multioutput]
related: [concepts/conformal-prediction, concepts/prediction-intervals, concepts/calibration, concepts/coverage-guarantee]
mind_map_priority: medium
---

# Uncertainty Quantification

**Uncertainty quantification (UQ)** is the science of quantifying and communicating the confidence in predictions or estimates. In machine learning, it addresses the critical question: "How much should we trust this prediction?"

## Why UQ Matters

1. **Decision-making**: Informed decisions require knowing prediction reliability
2. **Safety-critical systems**: Autonomous vehicles, medical AI need calibrated confidence
3. **Trust**: Users can't trust black-box predictions without uncertainty estimates
4. **Risk management**: Financial and energy applications require probabilistic forecasts

## Types of Uncertainty

### Aleatoric Uncertainty
- Inherent randomness in the data
- Cannot be reduced with more data
- Example: Measurement noise

### Epistemic Uncertainty
- Uncertainty due to limited knowledge/data
- Can be reduced with more data
- Example: Model uncertainty in sparse regions

## Methods

### Probabilistic Predictions
- Output full predictive distributions
- Bayesian methods, ensemble methods

### [[concepts/prediction-intervals|Prediction Intervals]]
- Output ranges containing true value with high probability
- [[concepts/conformal-prediction|Conformal prediction]] provides guaranteed intervals

### Calibration
- Ensure predicted probabilities match empirical frequencies
- [[concepts/calibration|Calibration]] is necessary but not sufficient for good UQ

### Ensemble Methods
- Train multiple models, aggregate predictions
- Disagreement indicates uncertainty

## Challenges

- **Neural networks**: Often overconfident, poorly calibrated
- **High dimensions**: UQ becomes harder
- **Distribution shift**: Uncertainty estimates may not transfer

## Applications in Conformal Prediction Context

[[concepts/conformal-prediction|Conformal prediction]] provides UQ with:
- **Guaranteed coverage**: Finite-sample validity
- **Model-agnostic**: Works with any predictor
- **Distribution-free**: No assumptions beyond exchangeability

Key applications:
- Electricity price forecasting
- Medical diagnosis
- Financial risk assessment

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/calibration|Calibration]]
