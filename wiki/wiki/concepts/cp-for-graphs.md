---
title: Conformal Prediction for Graph Data
page_id: concepts/cp-for-graphs
page_type: concept
revision_id: 1
created: 2026-05-24 16:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- graph-neural-networks
- node-classification
- link-prediction
- fdr-control
sources:
- sources/zhou-2025-cp-data-perspective
related:
- concepts/conformal-prediction
- concepts/graph-neural-networks
- concepts/exchangeability
- concepts/transductive-learning
- concepts/nonconformity-score
mind_map_priority: medium
schema_version: 2
uuid: b53d7ea7-a9df-55b1-b77c-196b7675b81c
content_hash: sha256:966a31236e670d9a81f2ba383fa1bff8d5016249b1ec0cef290645651dd9f180
---

<!-- AUTHORED REGION START -->
# Conformal Prediction for Graph Data

**CP for graphs** applies [[concepts/conformal-prediction|conformal prediction]] to data with explicit relational structure: node classification, link prediction, graph-level property prediction, and message-passing [[concepts/graph-neural-networks|GNN]] outputs.

## The Exchangeability Problem on Graphs

Nodes in a graph are emphatically *not* exchangeable — their features, labels, and embeddings depend on their neighborhoods. Standard CP applied to GNN outputs typically over- or under-covers depending on graph topology and the train/test split. Two regimes:

- **Inductive setting.** Train graph and test graph are disjoint; exchangeability assumed at the graph level. Easier case for CP.
- **Transductive setting.** Train and test nodes share the same graph; exchangeability holds only over labelled-node subsets under specific sampling assumptions. Most graph ML problems are transductive.

## Methods

- **Neighborhood Adaptive Prediction Sets (NAPS).** Construct prediction sets from K-nearest neighbours in learned representation space, restoring approximate exchangeability conditional on representations.
- **Diffused nonconformity scores.** Aggregate per-node scores over neighborhoods (e.g., 1-hop or 2-hop) to incorporate structural signal.
- **Conformalized link prediction with FDR control.** Treat each candidate edge as a test; apply Benjamini-Hochberg to conformal p-values to bound the false discovery rate of predicted edges.
- **Graph-population CP via quotient spaces.** When the population is *graphs* rather than nodes, exchangeability returns naturally.

## Sources

- [[sources/zhou-2025-cp-data-perspective]] — survey chapter on CP for graphs.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/graph-neural-networks]]
- [[concepts/exchangeability]]
- [[concepts/transductive-learning]]
- [[concepts/nonconformity-score]]

<!-- AUTHORED REGION END -->
