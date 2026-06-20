---
title: Multifactor Timing with Deep Learning
page_id: sources/cotturo-2026-multifactor-timing-deep-learning
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Paul Cotturo
- Fred Liu
- Robert Proner
year: 2026
venue: Journal of Financial Econometrics
volume_issue_pages: 24(3), nbag006
doi: 10.1093/jjfinec/nbag006
tags:
- factor-timing
- deep-learning
- multitask-learning
- lstm
- factor-investing
related:
- concepts/factor-timing
- concepts/multitask-learning
- concepts/lstm-networks
- concepts/deep-learning-for-finance
- concepts/shapley-values
- concepts/factor-investing
- concepts/no-arbitrage-restrictions
- concepts/factor-models
- entities/paul-cotturo
- entities/fred-liu
- entities/robert-proner
- entities/bryan-kelly
- entities/dacheng-xiu
- entities/shihao-gu
mind_map_priority: high
schema_version: 2
uuid: 4890d3ba-fc99-5ee9-a35e-15656161b4af
content_hash: sha256:b82905e21e62da228fa35ccd9d04255bc5eedc5b7c827d24fe58bcc95e12df5a
---

<!-- AUTHORED REGION START -->
# Multifactor Timing with Deep Learning

**Authors:** [[entities/paul-cotturo|Paul Cotturo]], [[entities/fred-liu|Fred Liu]], [[entities/robert-proner|Robert Proner]]

**Venue:** *Journal of Financial Econometrics*, 24(3), nbag006 (2026)

**DOI:** [10.1093/jjfinec/nbag006](https://doi.org/10.1093/jjfinec/nbag006)

## Summary

Develops a dynamic multitask (DMT) neural network for [[concepts/factor-timing|multifactor timing]] that combines hard-sharing [[concepts/multitask-learning|multitask]] layers with separate macroeconomic and financial [[concepts/lstm-networks|LSTMs]]. Across 1965-2021 the DMT model outperforms linear, tree, and off-the-shelf neural baselines on accuracy and Sharpe ratio, with unemployment, leverage, profitability, and money as the most influential predictors (assessed via [[concepts/shapley-values|Shapley values]]).

## Key Claims

1. Multitask learning provides effective regularization for low signal-to-noise factor returns by sharing structure across factor portfolios
2. DMT achieves 56.4% directional accuracy and a Sharpe ratio of 0.82 after costs, outperforming buy-and-hold, RF, GBT, NN, and LSTM benchmarks
3. Unemployment is the single most influential macro predictor; leverage, profitability, and money drive common factor structure

## Concepts

- [[concepts/factor-timing|Factor Timing]] — central
- [[concepts/multitask-learning|Multitask Learning]] — central
- [[concepts/lstm-networks|LSTM Networks]] — central
- [[concepts/deep-learning-for-finance|Deep Learning for Finance]] — central
- [[concepts/shapley-values|Shapley Values]] — supporting
- [[concepts/factor-investing|Factor Investing]] — supporting
- [[concepts/no-arbitrage-restrictions|No-Arbitrage Restrictions]] — supporting
- [[concepts/factor-models|Factor Models]] — supporting

## Related Sources

(Leave empty for now — links will be added by future ingestions)

<!-- AUTHORED REGION END -->
