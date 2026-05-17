---
title: "Graph Neural Networks"
page_id: concepts/graph-neural-networks
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [deep-learning, graphs, neural-networks, machine-learning, spectral-methods]
related: [concepts/graph-signal-processing, concepts/graph-convolutional-networks, concepts/spectral-graph-filters, concepts/graph-laplacian, sources/dong-2020-gsp-for-ml]
---

# Graph Neural Networks

Graph Neural Networks (GNNs) are deep learning architectures designed to operate on graph-structured data, enabling end-to-end learning for tasks like node classification, link prediction, and graph classification.

## Overview

GNNs extend neural networks to irregular domains by learning representations that capture both node features and graph topology. They connect deeply to [[concepts/graph-signal-processing|graph signal processing]] theory.

## Core Framework

### Message Passing
Most GNNs follow a message passing paradigm:

$$\mathbf{h}_v^{(l+1)} = \text{UPDATE}\left(\mathbf{h}_v^{(l)}, \text{AGG}\left(\{\mathbf{h}_u^{(l)} : u \in \mathcal{N}(v)\}\right)\right)$$

- **AGG:** Aggregates neighbor representations (sum, mean, max, attention)
- **UPDATE:** Combines with node's own representation
- **$\mathcal{N}(v)$:** Neighborhood of node $v$

### Layer-wise Propagation
$$\mathbf{H}^{(l+1)} = \sigma\left(\tilde{\mathbf{A}}\mathbf{H}^{(l)}\mathbf{W}^{(l)}\right)$$

where $\tilde{\mathbf{A}}$ is a normalized adjacency and $\mathbf{W}^{(l)}$ are learnable weights.

## Spectral vs Spatial

### Spectral Methods
Based on [[concepts/graph-fourier-transform|graph Fourier transform]] and [[concepts/spectral-graph-filters|spectral filtering]]:

- **Spectral CNN:** Learnable filters in frequency domain
- **ChebNet:** Polynomial approximation with Chebyshev basis
- **[[concepts/graph-convolutional-networks|GCN]]:** Simplified first-order filter

**Advantage:** Theoretical grounding in GSP.
**Limitation:** Requires fixed graph; expensive eigendecomposition.

### Spatial Methods
Define convolution directly on node neighborhoods:

- **GraphSAGE:** Sampling and aggregating neighbors
- **GAT:** Attention-weighted aggregation
- **MPNN:** General message passing framework

**Advantage:** Scalable, inductive (generalizes to new graphs).
**Limitation:** Less theoretical clarity on frequency response.

## Key Architectures

### Graph Convolutional Network (GCN)
[[concepts/graph-convolutional-networks|GCN layer]]:
$$\mathbf{H}^{(l+1)} = \sigma\left(\tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}\mathbf{H}^{(l)}\mathbf{W}^{(l)}\right)$$

Simple, effective, widely used baseline.

### Graph Attention Network (GAT)
Attention-weighted aggregation:
$$\mathbf{h}_v^{(l+1)} = \sigma\left(\sum_{u \in \mathcal{N}(v)} \alpha_{vu}\mathbf{W}\mathbf{h}_u^{(l)}\right)$$

where $\alpha_{vu}$ are learned attention coefficients.

### ChebNet
Chebyshev polynomial filters (see [[concepts/spectral-graph-filters|Spectral Graph Filters]]):
$$g_\theta(\mathbf{L}) = \sum_{k=0}^K \theta_k T_k(\tilde{\mathbf{L}})$$

Captures multi-hop interactions with localized filters.

### GraphSAGE
Sample-and-aggregate for inductive learning:
1. Sample fixed-size neighborhood
2. Aggregate features (mean, LSTM, pool)
3. Concatenate with node's own features

Enables learning on unseen nodes.

## Connection to GSP

[[sources/dong-2020-gsp-for-ml|Dong et al. (2020)]] establish deep connections:

| GNN Component | GSP Interpretation |
|---------------|-------------------|
| GCN layer | Low-pass [[concepts/spectral-graph-filters|spectral filter]] |
| Multi-hop aggregation | Polynomial filter |
| Attention weights | Adaptive graph construction |
| Skip connections | High-frequency preservation |

### Over-smoothing
Deep GNNs cause signal over-smoothing:
- Repeated low-pass filtering
- All node representations converge
- Limits depth to ~2-4 layers typically

**Mitigations:** Skip connections, normalization, high-pass components.

## Training Paradigms

### [[concepts/transductive-learning|Transductive Learning]]
Train and test on same graph (fixed split).
- All nodes visible during training
- Labels available for subset

### Inductive Learning
Train on one graph, test on different graph.
- Requires spatial (not spectral) methods
- GraphSAGE, GAT support this

### Self-supervised Learning
Pre-training without labels:
- Contrastive learning on graphs
- Graph-level objectives
- Node-level pretext tasks

## Applications

### Node Classification
Predict labels for unlabeled nodes:
- Semi-supervised with few labels
- Citation networks, social networks

### Link Prediction
Predict missing or future edges:
- Knowledge graph completion
- Recommendation systems

### Graph Classification
Classify entire graphs:
- Molecular property prediction
- Protein function prediction

### Temporal Graphs
[[sources/misiakos-2025-dag-tfrc|Time-series on graphs]]:
- Traffic prediction
- Dynamic social networks
- Financial networks

## Scalability

### Sampling Methods
- Node sampling (GraphSAGE)
- Layer sampling (FastGCN)
- Subgraph sampling (Cluster-GCN)

### Mini-batching
- Historical embeddings
- Neighbor caching
- Precomputation

## Code Example (Conceptual)

```python
import torch
import torch.nn.functional as F

class GCNLayer(torch.nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.W = torch.nn.Linear(in_features, out_features)

    def forward(self, X, A_norm):
        # A_norm = D^{-1/2} A D^{-1/2}
        return F.relu(A_norm @ self.W(X))
```

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-convolutional-networks|Graph Convolutional Networks]]
- [[concepts/spectral-graph-filters|Spectral Graph Filters]]
- [[concepts/transductive-learning|Transductive Learning]]
- [[sources/dong-2020-gsp-for-ml|GSP for Machine Learning Review]]
