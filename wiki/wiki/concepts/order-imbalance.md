---
title: Order Imbalance
page_id: concepts/order-imbalance
page_type: concept
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T17:35:34Z'
tags:
- order-imbalance
- etf-flows
- order-flow
- market-microstructure
- limit-order-book
sources:
- sources/petit-2025-data-driven-flow-etf
- sources/xu-2020-mlofi
- sources/koukorinis-stylized-facts
related:
- concepts/order-flow
- concepts/etf-flows
- concepts/flow-decomposition
- concepts/limit-order-book
- concepts/market-microstructure
mind_map_priority: medium
schema_version: 2
uuid: 1540ec85-cc5d-51ef-90b6-490aeee07443
content_hash: sha256:de026a07e58e033d56f58b9bc48ab5379c63926c6b706c29f4604f8643c7c6e5
---

<!-- AUTHORED REGION START -->
# Order Imbalance

The net difference between buy-initiated and sell-initiated activity over an interval. It is the quantity that carries directional information: gross volume says how much traded, imbalance says which way the pressure went.

## At the Book Level

[[sources/xu-2020-mlofi|Xu, Gould & Howison (2020)]] generalise scalar Order-Flow Imbalance into **Multi-Level OFI**, a vector measuring net flow across several price levels of the [[concepts/limit-order-book|limit order book]], counting limit order arrivals, cancellations and market orders together. Imbalance deep in the book turns out to matter for price formation, not just imbalance at the touch. See [[concepts/order-flow|Order Flow]].

## At the ETF Level

[[sources/petit-2025-data-driven-flow-etf|Petit, Cucuringu & Cartea (2025)]] use imbalance among 16 features describing market state at trade time, in a clustering approach that decomposes ETF and constituent trade flow by co-occurrence pattern. Rather than classifying flow by rule, they normalise features by rolling time-of-day percentile rank, reduce dimension with PCA, and cluster with k-means++ over 14-day sliding windows, aligning clusters across windows. See [[concepts/etf-flows|ETF Flows]] and [[concepts/flow-decomposition|Flow Decomposition]].

## Why It Is Studied

[[sources/koukorinis-stylized-facts|Koukorinis, Peters & Germano (2022)]] list order imbalance among the variables examined when characterising persistence and dependence in high-frequency data — imbalance is one of the series in which long memory is looked for, alongside inter-arrival rates and volumes.

## Open Questions

- How stable is the cluster structure in [[sources/petit-2025-data-driven-flow-etf|Petit et al. (2025)]] across market regimes rather than within 14-day windows?
- Is deep-book imbalance informative in less liquid markets, or only where the book is well populated?

## See Also

[[concepts/order-flow|Order Flow]] · [[concepts/etf-flows|ETF Flows]] · [[concepts/flow-decomposition|Flow Decomposition]] · [[concepts/limit-order-book|Limit Order Book]] · [[concepts/market-microstructure|Market Microstructure]] · [[entities/alvaro-cartea|Alvaro Cartea]]

<!-- AUTHORED REGION END -->
