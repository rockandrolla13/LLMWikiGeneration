---
title: Graph Convolutional Networks
page_id: concepts/graph-convolutional-networks
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- deep-learning
- graphs
- neural-networks
- spectral-methods
- semi-supervised-learning
related:
- concepts/graph-neural-networks
- concepts/graph-signal-processing
- concepts/spectral-graph-filters
- concepts/graph-laplacian
- concepts/transductive-learning
schema_version: 2
uuid: c7ecd993-526b-5732-bcd5-870321aa831f
content_hash: sha256:c51ddea7d13be2e4f0127d1e720c3d72823a36bb4d17e57d647b021636f4178b
---

<!-- AUTHORED REGION START -->
# Graph Convolutional Networks

Graph Convolutional Networks (GCNs) are a foundational [[concepts/graph-neural-networks|graph neural network]] architecture that performs efficient spectral graph convolutions through a first-order approximation.

## Definition

The GCN layer (Kipf & Welling, 2017):

$$\mathbf{H}^{(l+1)} = \sigma\left(\tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}\mathbf{H}^{(l)}\mathbf{W}^{(l)}\right)$$

where:
- $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}$ (adjacency with self-loops)
- $\tilde{\mathbf{D}}_{ii} = \sum_j \tilde{\mathbf{A}}_{ij}$ (degree matrix)
- $\mathbf{H}^{(l)}$ is the $l$-th layer representation
- $\mathbf{W}^{(l)}$ is learnable weight matrix
- $\sigma$ is activation function (typically ReLU)

## Spectral Interpretation

GCN derives from [[concepts/spectral-graph-filters|spectral graph filtering]]:

### From ChebNet to GCN
Starting with Chebyshev polynomial filter:
$$g_\theta(\mathbf{L}) = \sum_{k=0}^K \theta_k T_k(\tilde{\mathbf{L}})$$

**Simplifications:**
1. **First-order ($K=1$):** $g_\theta = \theta_0 + \theta_1(\mathbf{L} - \mathbf{I})$
2. **Single parameter ($\theta_0 = -\theta_1 = \theta$):** $g_\theta = \theta(\mathbf{I} + \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2})$
3. **Renormalization trick:** $\mathbf{I} + \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2} \to \tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}$

### Filter Response
GCN implements a **low-pass filter** on graph signals:
- Eigenvalue $\lambda = 0$: preserved (constant signal)
- Eigenvalue $\lambda = 2$: suppressed (high-frequency)

This explains why GCN smooths representations across neighborhoods.

## Architecture

### Two-Layer GCN (Typical)
```
Input: X ∈ R^{N×F} (node features)
       A ∈ R^{N×N} (adjacency)

Layer 1: H = ReLU(Ã X W_0)     # Hidden representation
Layer 2: Z = softmax(Ã H W_1)  # Output (class probabilities)

where Ã = D̃^{-1/2} Ã D̃^{-1/2}
```

### Propagation Matrix
The normalized adjacency:
$$\hat{\mathbf{A}} = \tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}$$

Properties:
- Symmetric (preserves signal energy)
- Eigenvalues in $[-1, 1]$ (stable iteration)
- Self-loops prevent vanishing features

## Training

### Semi-supervised Node Classification
GCN excels at [[concepts/transductive-learning|transductive learning]]:

1. **Input:** Graph with partial labels
2. **Loss:** Cross-entropy on labeled nodes
3. **Propagation:** Information flows through edges
4. **Output:** Labels for all nodes

$$\mathcal{L} = -\sum_{v \in \mathcal{V}_L} \sum_{c=1}^C y_{vc} \log z_{vc}$$

### Over-smoothing Problem
Deep GCNs suffer from feature convergence:
- Each layer averages with neighbors
- After many layers, all features become similar
- Practical limit: 2-4 layers

**Solutions:**
- Skip connections (residual)
- Jumping knowledge networks
- Layer normalization
- DropEdge regularization

## Variants

### Simplified GCN (SGC)
Remove non-linearities:
$$\mathbf{Z} = \text{softmax}(\hat{\mathbf{A}}^K \mathbf{X} \mathbf{W})$$

Linear in features, surprisingly competitive.

### GCN with Attention (GAT)
Replace fixed normalization with learned attention:
$$\alpha_{ij} = \frac{\exp(\text{LeakyReLU}(\mathbf{a}^T[\mathbf{W}\mathbf{h}_i \| \mathbf{W}\mathbf{h}_j]))}{\sum_{k \in \mathcal{N}(i)} \exp(\text{LeakyReLU}(\mathbf{a}^T[\mathbf{W}\mathbf{h}_i \| \mathbf{W}\mathbf{h}_k]))}$$

### APPNP
Personalized PageRank propagation:
$$\mathbf{Z} = \text{softmax}(\alpha(\mathbf{I} - (1-\alpha)\hat{\mathbf{A}})^{-1}\mathbf{X}\mathbf{W})$$

Decouples prediction and propagation.

## Comparison with GSP Filters

| Aspect | GCN | General Spectral Filter |
|--------|-----|------------------------|
| Order | 1 | Arbitrary |
| Parameters | $O(F_{in} \times F_{out})$ | $O(K \times F_{in} \times F_{out})$ |
| Locality | 1-hop | $K$-hop |
| Frequency response | Fixed low-pass | Learnable |
| Computation | $O(\|E\|F)$ | $O(K\|E\|F)$ |

## Code Example

```python
import torch
import torch.nn.functional as F

class GCN(torch.nn.Module):
    def __init__(self, n_features, n_hidden, n_classes):
        super().__init__()
        self.W1 = torch.nn.Linear(n_features, n_hidden)
        self.W2 = torch.nn.Linear(n_hidden, n_classes)

    def forward(self, X, A_hat):
        # A_hat = D̃^{-1/2} Ã D̃^{-1/2} precomputed
        H = F.relu(A_hat @ self.W1(X))
        Z = A_hat @ self.W2(H)
        return F.log_softmax(Z, dim=1)
```

## Applications

### Node Classification
- Citation networks (Cora, Citeseer, Pubmed)
- Social networks
- Biological networks

### Graph Classification
With global pooling for entire graph representation.

### Link Prediction
Encode nodes, predict edge existence.

### Recommendation
User-item graphs, collaborative filtering.

## See Also

- [[concepts/graph-neural-networks|Graph Neural Networks]]
- [[concepts/spectral-graph-filters|Spectral Graph Filters]]
- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/transductive-learning|Transductive Learning]]
- [[concepts/graph-laplacian|Graph Laplacian]]

<!-- AUTHORED REGION END -->
