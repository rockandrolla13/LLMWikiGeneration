---
title: Random Forest
page_id: concepts/random-forest
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T17:35:34Z'
tags:
- random-forest
- machine-learning
- corporate-bonds
- trade-classification
- return-prediction
sources:
- sources/fedenia-2021-ml-trade-classifier
- sources/feng-2025-predicting-bond-returns
related:
- concepts/trade-classification
- concepts/market-microstructure
mind_map_priority: medium
schema_version: 2
uuid: 3d999c08-f817-53a7-b542-c8a063ea7e12
content_hash: sha256:259996e51f56cd4123f6165ac4f0eea566937e95700338ea95003ea6d90e6026
---

<!-- AUTHORED REGION START -->
# Random Forest

An ensemble of decision trees, each fitted on a bootstrap sample with a random subset of features considered at each split, with predictions averaged or voted. In this wiki it appears as the workhorse non-linear model in two corporate bond applications, both of which report it beating linear or rule-based baselines.

## Trade Classification

[[sources/fedenia-2021-ml-trade-classifier|Fedenia, Ronen & Nam (2021)]] build a Random Forest classifier to infer trade direction in corporate bonds, trained on TRACE Enhanced data with true buy/sell indicators over 17.5 years.

| Comparison | Accuracy gain |
|---|---|
| RF vs Tick Rule (bonds) | +8.3% |
| RF vs Lee-Ready (equities) | +3.6% |
| RF vs Tick Rule (equities) | +3.3% |

Two findings beyond the headline: accuracy is higher in more liquid bonds, and a model trained on bonds transfers usefully to equities. See [[concepts/trade-classification|Trade Classification]].

## Return Prediction

[[sources/feng-2025-predicting-bond-returns|Feng, He, Wang & Wu (2025)]] apply Random Forest to individual corporate bond returns across 1976–2020, including private as well as public bonds, testing out of sample on 1996–2020.

- Out-of-sample R² of 4.48%, annualised Sharpe of 3.27, monthly alpha 2.09%.
- Outperforms Lasso and combination forecasts.
- Predictability is time-varying: stronger under high risk aversion, slow growth and high VIX.
- Leading predictors include downside risk, short-term reversal, return skewness and credit spreads.

## Why It Suits These Problems

Both tasks involve many weakly informative, interacting features and non-linear relationships — conditions where a linear model underfits. The trade-off is interpretability: feature importance rankings are available, but the fitted function is not readable the way a coefficient vector is.

## Open Questions

- How much of the return-prediction performance survives realistic transaction costs in a market as illiquid as corporate bonds?
- Does the bonds-to-equities transfer in [[sources/fedenia-2021-ml-trade-classifier|Fedenia et al. (2021)]] hold outside the sample period tested?

## See Also

[[concepts/trade-classification|Trade Classification]] · [[concepts/market-microstructure|Market Microstructure]]

**Not yet written:** `concepts/machine-learning-bonds`, `concepts/bond-return-predictability`, `concepts/trace-data`

<!-- AUTHORED REGION END -->
