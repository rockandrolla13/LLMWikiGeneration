---
title: "Graph Learning for Financial Networks (Yu 2024)"
page_id: sources/yu-2024-graph-learning-financial
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [financial-networks, graph-neural-networks, link-prediction, otc-markets, corporate-bonds]
authors: [Shui Yu]
year: 2024
institution: Rutgers University
degree: PhD
supervisor: Xiaodong Lin
related: [concepts/graph-neural-networks, concepts/graph-laplacian, sources/misiakos-2025-dag-tfrc]
---

# Graph Learning for Financial Networks

**Author:** Shui Yu
**Supervisor:** Xiaodong Lin
**Institution:** Rutgers University, Graduate School-Newark
**Year:** 2024 (PhD Dissertation)

## Summary

This dissertation analyzes the over-the-counter (OTC) corporate bond dealer network using graph learning and neural network methods. It explores network topology, dealer trading behaviors, and develops dynamic link prediction methods for understanding risk propagation in financial networks.

## Key Contributions

### 1. Dealer Network Topology Analysis
- Constructs financial network from enhanced TRACE dataset (2010-2015)
- Reveals core-periphery structure in dealer networks
- Demonstrates scale-free properties (power-law degree distribution)
- Analyzes network resilience through node/edge removal simulations

### 2. Topological Importance and Trading Behavior
- Links dealer centrality metrics to trading outcomes
- Dealers with greater topological importance leverage position for market advantage
- Analyzes markup pricing, transaction chains, and inventory holding times
- Constructs round-trip transaction intermediation chains

### 3. Dynamic Graph Neural Network Link Prediction
- Develops continuous-time dynamic [[concepts/graph-neural-networks|graph neural network]] method
- Implements enhanced neighborhood message aggregation
- Predicts future trading relationships between dealers
- Addresses limitations of snapshot-based temporal network analysis

## Data and Methodology

### TRACE Dataset
- 67.7M total transaction records
- 22.5M dealer-to-dealer transactions (after deduplication)
- Covers 2010-2015 period
- Enhanced with buyer/seller identity information

### Network Construction
- Nodes: Corporate bond dealers (unique 4-letter identifiers)
- Edges: Transactions between dealers
- Edge weights: Transaction volume or count
- Both static and dynamic network representations

### Key Metrics Analyzed
- Degree centrality, betweenness centrality, closeness centrality
- PageRank, clustering coefficient
- Node strength (weighted degree)
- Network resilience measures

## Key Findings

### Network Structure
- Network exhibits community structure mirroring institutional organization
- High concentration: few dealers dominate trading volume
- Assortative mixing by degree (similar-degree dealers trade together)
- Network topology changes significantly during market stress periods

### Trading Behavior Patterns
1. **Markups:** Central dealers extract higher markups
2. **Transaction Chains:** More central dealers have shorter chains to counterparties
3. **Prearranged Trades:** Topological position affects trade pre-arrangement
4. **Inventory Holding:** Central dealers hold inventory for shorter periods
5. **Loss Probability:** Network position correlates with dealer loss rates

### Link Prediction Results
- Dynamic GNN with message aggregation outperforms static methods
- Continuous-time framework superior to fixed time-window snapshots
- Traditional similarity measures (Adamic-Adar, Jaccard) insufficient for bond networks

## Technical Approaches

### Static Link Prediction Methods Compared
- Common Neighbors, Adamic-Adar Index
- Jaccard Coefficient, Preferential Attachment
- Resource Allocation Index
- Graph embedding methods (Node2Vec, DeepWalk)

### Dynamic GNN Architecture
- Temporal attention mechanisms
- Memory modules for historical context
- Neighborhood aggregation with edge features
- Continuous-time representation learning

## Applications

- **Risk Management:** Predicting potential contagion paths
- **Regulatory Oversight:** Monitoring systemically important dealers
- **Trading Strategy:** Understanding market microstructure

## Related Work

- [[sources/misiakos-2025-dag-tfrc|DAG-TFRC]] - DAG learning from time series with applications to finance
- Financial network contagion literature (Allen & Gale, Boss et al.)
- OTC market structure analysis (Li & Schurhoff, Di Maggio et al.)

## See Also

- [[concepts/graph-neural-networks|Graph Neural Networks]]
- [[concepts/graph-laplacian|Graph Laplacian]]
- [[concepts/limit-order-book|Limit Order Book]]
