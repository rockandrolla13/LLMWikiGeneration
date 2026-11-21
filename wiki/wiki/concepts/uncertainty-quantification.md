---
created: 2026-04-10 18:00:00+00:00
mind_map_priority: medium
page_id: concepts/uncertainty-quantification
page_type: concept
related:
- concepts/bayesian-updating
- concepts/calibration
- concepts/conformal-prediction
- concepts/continuous-ranked-probability-score
- concepts/coverage-guarantee
- concepts/energy-score
- concepts/logarithmic-score
- concepts/prediction-intervals
- concepts/strictly-proper-scoring-rules
revision_id: 3
sources:
- sources/zaffran-phd
- sources/johnstone-2025-multioutput
- sources/marks-2020-nobody-knows-ii
tags:
- machine-learning
- statistics
- decision-making
title: Uncertainty Quantification
updated: '2026-11-21T02:50:17Z'
schema_version: 2
uuid: e87bcfdd-8434-5b88-b0ad-99e2351b40bb
content_hash: sha256:edc711dbc4ada6b5420d29ede8049a65b5135aecaebeb406ff89c5ef0defc98c
updated_by: op_ac3a896f7d8e
---

<!-- AUTHORED REGION START -->
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

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/bayesian-updating|bayesian-updating]]
- [[concepts/continuous-ranked-probability-score|continuous-ranked-probability-score]]
- [[concepts/energy-score|energy-score]]
- [[concepts/logarithmic-score|logarithmic-score]]
- [[concepts/strictly-proper-scoring-rules|strictly-proper-scoring-rules]]

## In Howard Marks's Memos

- [[sources/marks-2020-nobody-knows-ii|Nobody Knows II]] (2020)
<!-- AUTHORED REGION END -->
