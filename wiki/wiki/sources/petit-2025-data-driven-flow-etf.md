---
title: "Data-Driven Trade Flow Decomposition for Exchange-Traded Funds and their Constituents"
page_id: sources/petit-2025-data-driven-flow-etf
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-06T23:30:00Z
updated: 2026-05-06T23:30:00Z
authors: [Nicolas Petit, Mihai Cucuringu, Alvaro Cartea]
year: 2025
venue: ICAIF 2025
tags: [etf-flows, machine-learning, clustering, order-imbalance, portfolio-construction, pca, k-means, market-microstructure]
related: [concepts/etf-flows, concepts/flow-decomposition, concepts/order-imbalance, concepts/clustering, entities/alvaro-cartea, entities/mihai-cucuringu, sources/optiver-2025-corporate-bond-etf-contraflow, sources/chao-2019-etf-flows-prices]
mind_map_priority: high
---

# Data-Driven Trade Flow Decomposition for ETFs and their Constituents

**Authors:** Nicolas Petit, Mihai Cucuringu, Alvaro Cartea

**Year:** 2025

**Venue:** 6th ACM International Conference on AI in Finance (ICAIF '25)

**Institutions:** University of Oxford, UCLA, Oxford-Man Institute

## Summary

This paper presents a novel data-driven methodology for decomposing trade flow based on co-occurrence patterns between ETFs and their constituent securities. Unlike prior rule-based approaches (Lu et al.), this work uses unsupervised learning with PCA dimensionality reduction followed by k-means++ clustering. The method captures joint informational content between ETFs and their underlying constituents.

## Key Contributions

### 1. Data-Driven Clustering Framework
- 16 features capturing market state at trade time (Table 1)
- Rolling percentile rank normalization by time-of-day
- PCA for dimensionality reduction
- k-means++ clustering with 14-day sliding windows
- Cluster alignment across consecutive windows

### 2. Feature Construction
- ETF and constituent trade counts
- Notional volumes
- Order imbalances
- Temporal co-occurrence metrics
- Joint ETF-constituent market microstructure features

### 3. Economic Validation
- Factor-mimicking portfolios from cluster-specific order imbalances
- Orthogonalization to standard risk factors
- Statistically significant Sharpe ratios for subset of clusters
- Data: SPY and constituents (Jan 2018 - Dec 2021)

### 4. Comparison to Rule-Based Methods
- Lu et al. (2018, 2019): K=4 fixed rule-based clusters
- Data-driven approach learns optimal decomposition
- Incorporates ETF-constituent interactions (not just constituents)

## Methodology

1. **Feature Construction**: 16 features capturing joint ETF-constituent microstructure
2. **Dimensionality Reduction**: PCA projection
3. **Clustering**: k-means++ on transformed feature space
4. **Portfolio Construction**: Conditional order imbalances by cluster

## Key Claims

1. Data-driven clustering outperforms rule-based decomposition
2. Cluster-specific order imbalances contain predictive information beyond raw OI
3. ETF-constituent co-occurrence patterns are economically meaningful
4. Factor-mimicking portfolios achieve significant risk-adjusted returns

## See Also

- [[concepts/etf-flows|ETF Flows]]
- [[concepts/order-imbalance|Order Imbalance]]
- [[concepts/clustering|Clustering]]
- [[entities/alvaro-cartea|Alvaro Cartea]]
- [[sources/optiver-2025-corporate-bond-etf-contraflow|Optiver (2025) Corporate Bond ETF Contraflow]]
- [[sources/chao-2019-etf-flows-prices|Chao et al. (2019) Why Do ETF Flows Move Prices]]
