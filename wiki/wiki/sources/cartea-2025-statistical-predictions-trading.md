---
title: Statistical Predictions of Trading Strategies in Electronic Markets
page_id: sources/cartea-2025-statistical-predictions-trading
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Alvaro Cartea
- Samuel N. Cohen
- Robert Graumans
- Saad Labyad
- Leandro Sanchez-Betancourt
- Leon van Veldhuijzen
year: 2025
venue: Journal of Financial Econometrics
volume_issue_pages: 23(2), nbae025
doi: 10.1093/jjfinec/nbae025
tags:
- limit-order-book
- algorithmic-trading
- market-making
- agent-based-models
- trader-clustering
related:
- concepts/limit-order-book
- concepts/market-making
- concepts/agent-based-models
- concepts/algorithmic-trading
- concepts/order-flow-prediction
- concepts/trader-clustering
- concepts/high-frequency-trading
- entities/alvaro-cartea
- entities/samuel-n-cohen
- entities/leandro-sanchez-betancourt
- entities/robert-graumans
- entities/saad-labyad
- entities/leon-van-veldhuijzen
mind_map_priority: high
schema_version: 2
uuid: 5504be27-1952-525b-9846-52696df5328c
content_hash: sha256:2faac26c3129bd44128d1fc677d1e71a9dd2f3fd43b9b57107520bfbe0e67dcb
---

<!-- AUTHORED REGION START -->
# Statistical Predictions of Trading Strategies in Electronic Markets

**Authors:** [[entities/alvaro-cartea|Alvaro Cartea]], [[entities/samuel-n-cohen|Samuel N. Cohen]], [[entities/robert-graumans|Robert Graumans]], [[entities/saad-labyad|Saad Labyad]], [[entities/leandro-sanchez-betancourt|Leandro Sanchez-Betancourt]], [[entities/leon-van-veldhuijzen|Leon van Veldhuijzen]]

**Venue:** *Journal of Financial Econometrics*, 23(2), nbae025 (2025)

**DOI:** [10.1093/jjfinec/nbae025](https://doi.org/10.1093/jjfinec/nbae025)

## Summary

Uses a regulatory dataset from Euronext Amsterdam (with [[concepts/algorithmic-trading|algorithm]]- and member-level identifiers) to build statistical models predicting the direction, price, and volume of incoming [[concepts/limit-order-book|limit orders]]. Clusters trading behavior into directional, opportunistic, and [[concepts/market-making|market-making]] styles, finding that roughly one-third of Liquidity Providers behave as market makers and that algorithm-level identification materially improves [[concepts/order-flow-prediction|order-flow prediction]] accuracy.

## Key Claims

1. Logistic-regression models with algorithm and member identifiers achieve ~70% order-weighted accuracy for order-direction prediction vs ~54% without identifiers
2. Order-book imbalance, the algorithm's own resting orders, best-quote volumes, and intraday inventory are the most predictive features
3. Liquidity Providers split into three behavioral clusters with markedly different trading patterns despite a single dealing capacity

## Concepts

- [[concepts/limit-order-book|Limit Order Book]] — central
- [[concepts/market-making|Market Making]] — central
- [[concepts/agent-based-models|Agent-Based Models]] — central
- [[concepts/algorithmic-trading|Algorithmic Trading]] — central
- [[concepts/order-flow-prediction|Order Flow Prediction]] — central
- [[concepts/trader-clustering|Trader Clustering]] — central
- [[concepts/high-frequency-trading|High-Frequency Trading]] — supporting

## Related Sources

(Leave empty for now — links will be added by future ingestions)

<!-- AUTHORED REGION END -->
