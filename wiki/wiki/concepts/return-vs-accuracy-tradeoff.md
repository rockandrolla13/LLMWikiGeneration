---
title: Return-vs-Accuracy Divergence
page_id: concepts/return-vs-accuracy-tradeoff
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [quant-finance, futures, backtesting, deep-learning, directional-forecasting, evaluation]
sources: [sources/chen-2024-volume-price-product-factor]
related: [concepts/directional-forecasting, concepts/overfitting-in-alpha-research, concepts/backtesting, concepts/information-ratio]
mind_map_priority: medium
---

# Return-vs-Accuracy Divergence

**Return-vs-Accuracy Divergence** is the observation that predictive accuracy metrics (MSE, classification accuracy) do not translate into trading profitability for futures, so models should be evaluated on annualized return and a trade-based profitability ratio rather than point-forecast error alone.

## Overview

The paper contrasts an LSTM benchmark that achieves low MSE but only ~0.2 R-squared with a one-step predictive lag against the VPPMA, which reaches R-squared above 0.7 on most top-ranked varieties. The authors argue that a low point-forecast error can coexist with poor tradability, because a lagged next-day price prediction fails to time entries and exits. The practical prescription is to judge a forecasting model by realized annualized return and a trade-level profitability ratio rather than by MSE or classification accuracy.

## Sources

- [[sources/chen-2024-volume-price-product-factor]] — uses the LSTM-vs-VPPMA comparison to argue accuracy metrics mislead when profitability is the goal.

## Related Concepts

- [[concepts/directional-forecasting]]
- [[concepts/overfitting-in-alpha-research]]
- [[concepts/backtesting]]
- [[concepts/information-ratio]]
