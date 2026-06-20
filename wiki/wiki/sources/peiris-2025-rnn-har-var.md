---
title: Loss-Based Bayesian Sequential Prediction of Value-at-Risk with a Long-Memory
  and Non-Linear Realized Volatility Model
page_id: sources/peiris-2025-rnn-har-var
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Rangika Peiris
- Minh-Ngoc Tran
- Chao Wang
- Richard Gerlach
year: 2025
venue: Journal of Financial Econometrics
volume_issue_pages: 23(4), nbaf017
doi: 10.1093/jjfinec/nbaf017
tags:
- value-at-risk
- har-model
- recurrent-neural-networks
- sequential-monte-carlo
- generalized-bayes
related:
- concepts/value-at-risk
- concepts/har-model
- concepts/recurrent-neural-networks
- concepts/rnn-har
- concepts/generalized-bayesian-inference
- concepts/sequential-monte-carlo
- concepts/asymmetric-laplace-density
- concepts/realized-variance
- concepts/quantile-regression
- entities/rangika-peiris
- entities/minh-ngoc-tran
- entities/chao-wang
- entities/richard-gerlach
- entities/fulvio-corsi
mind_map_priority: high
schema_version: 2
uuid: caa7832d-6557-5bf2-8b9f-863924befcbd
content_hash: sha256:293545bab0612e3b91c20345d3db1437c7821d47c6bc562961d054b3d734dc28
---

<!-- AUTHORED REGION START -->
# Loss-Based Bayesian Sequential Prediction of Value-at-Risk with a Long-Memory and Non-Linear Realized Volatility Model

**Authors:** [[entities/rangika-peiris|Rangika Peiris]], [[entities/minh-ngoc-tran|Minh-Ngoc Tran]], [[entities/chao-wang|Chao Wang]], [[entities/richard-gerlach|Richard Gerlach]]

**Venue:** *Journal of Financial Econometrics*, 23(4), nbaf017 (2025)

**DOI:** [10.1093/jjfinec/nbaf017](https://doi.org/10.1093/jjfinec/nbaf017)

## Summary

Proposes [[concepts/rnn-har|RNN-HAR]], a hybrid model that embeds three [[concepts/recurrent-neural-networks|recurrent neural networks]] (daily/weekly/monthly) inside the [[concepts/har-model|HAR]] additive cascade for direct [[concepts/value-at-risk|Value-at-Risk]] forecasting. Estimation uses [[concepts/asymmetric-laplace-density|asymmetric Laplace]] [[concepts/quantile-regression|quantile-loss]] [[concepts/generalized-bayesian-inference|generalized Bayes]] with [[concepts/sequential-monte-carlo|Sequential Monte Carlo]]; across 31 market indices the model consistently outperforms HAR and its extensions on quantile scores.

## Key Claims

1. Integrating RNN non-linearity inside HAR materially improves VaR forecasts versus linear HAR variants
2. Loss-based generalized Bayesian inference with the asymmetric Laplace quantile loss avoids return-distribution assumptions
3. Sequential Monte Carlo enables expanding-window posterior updating efficient for deep models

## Concepts

- [[concepts/value-at-risk|Value-at-Risk]] — central
- [[concepts/har-model|Heterogeneous Autoregressive Model]] — central
- [[concepts/recurrent-neural-networks|Recurrent Neural Networks]] — central
- [[concepts/rnn-har|RNN-HAR]] — central
- [[concepts/generalized-bayesian-inference|Generalized Bayesian Inference]] — central
- [[concepts/sequential-monte-carlo|Sequential Monte Carlo]] — central
- [[concepts/asymmetric-laplace-density|Asymmetric Laplace Density]] — supporting
- [[concepts/realized-variance|Realized Variance]] — supporting
- [[concepts/quantile-regression|Quantile Regression]] — supporting

## Related Sources

(Leave empty for now — links will be added by future ingestions)

<!-- AUTHORED REGION END -->
