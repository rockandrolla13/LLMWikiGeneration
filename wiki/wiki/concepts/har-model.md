---
title: "Heterogeneous Autoregressive Model"
page_id: concepts/har-model
page_type: concept
revision_id: 1
created: 2026-05-21T12:00:00Z
updated: 2026-05-21T12:00:00Z
tags: [realized-volatility, long-memory, time-series, corsi]
sources: [sources/bodilsen-2025-hf-dynamic-factor-portfolio, sources/peiris-2025-rnn-har-var]
related: []
mind_map_priority: medium
---

# Heterogeneous Autoregressive Model

**Heterogeneous Autoregressive Model (HAR)** is the Corsi (2009) regression of realized volatility on daily, weekly, and monthly lagged averages; an additive cascade approximating long-memory behavior of volatility with parsimonious linear structure.

## Sources

- [[sources/bodilsen-2025-hf-dynamic-factor-portfolio|Large-Dimensional Portfolio Selection with HF Dynamic Factor Model (2025)]] — central; used in HAR-DRD benchmarks for realized covariance forecasting
- [[sources/peiris-2025-rnn-har-var|Loss-Based Bayesian Sequential VaR with RNN-HAR (2025)]] — central; the additive cascade into which the RNNs are embedded

## Related Concepts

(Leave empty for now)
