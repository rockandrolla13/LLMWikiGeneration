---
title: "Sheaf Laplacian"
page_id: concepts/sheaf-laplacian
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [algebraic-topology, graph-theory, spectral-methods, sheaf-theory]
related: [concepts/graph-laplacian, concepts/graph-signal-processing, concepts/graph-neural-networks, sources/zhi-2024-gaussian-processes-graphs]
---

# Sheaf Laplacian

The sheaf Laplacian generalizes the [[concepts/graph-laplacian|graph Laplacian]] by attaching vector spaces to nodes and linear maps to edges, enabling richer representations of data on graphs.

## Motivation

The standard graph Laplacian assumes scalar signals on nodes. Many applications require:
- **Vector-valued data:** Features at each node
- **Edge relationships:** How features should relate across edges
- **Heterogeneous structure:** Different types of connections

Cellular sheaves provide this generalization.

## Cellular Sheaves

### Definition
A cellular sheaf $\mathcal{F}$ on a graph $G = (V, E)$ assigns:
- **Stalk $\mathcal{F}(v)$:** Vector space $\mathbb{R}^{d_v}$ to each node $v$
- **Restriction map $\mathcal{F}_{v \triangleleft e}$:** Linear map from edge $e$ to incident node $v$

### Global Sections
A global section $\mathbf{x}$ assigns a vector to each node:
$$\mathbf{x} = (\mathbf{x}_v)_{v \in V}, \quad \mathbf{x}_v \in \mathcal{F}(v)$$

The section is **consistent** if restriction maps agree on edges.

## Sheaf Laplacian

### Construction
For edge $e = (u, v)$, define the **coboundary**:
$$(\delta \mathbf{x})_e = \mathcal{F}_{v \triangleleft e}\mathbf{x}_v - \mathcal{F}_{u \triangleleft e}\mathbf{x}_u$$

The sheaf Laplacian:
$$\mathbf{L}_\mathcal{F} = \delta^T \delta$$

### Block Structure
$$(\mathbf{L}_\mathcal{F})_{uv} = \begin{cases}
\sum_{e \ni u} \mathcal{F}_{u \triangleleft e}^T \mathcal{F}_{u \triangleleft e} & u = v \\
-\mathcal{F}_{u \triangleleft e}^T \mathcal{F}_{v \triangleleft e} & (u,v) = e \in E \\
0 & \text{otherwise}
\end{cases}$$

### Special Case: Standard Laplacian
When all stalks are $\mathbb{R}$ and restriction maps are identity:
$$\mathbf{L}_\mathcal{F} = \mathbf{L}$$

The standard [[concepts/graph-laplacian|graph Laplacian]] is recovered.

## Properties

### Positive Semi-definiteness
$$\mathbf{x}^T \mathbf{L}_\mathcal{F} \mathbf{x} = \|\delta \mathbf{x}\|^2 = \sum_e \|(\delta \mathbf{x})_e\|^2 \geq 0$$

### Kernel
$$\ker(\mathbf{L}_\mathcal{F}) = \ker(\delta) = \{\text{global sections}\}$$

Signals in the kernel are consistent across all edges.

### Spectral Decomposition
Eigendecomposition provides generalized graph frequencies:
$$\mathbf{L}_\mathcal{F} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^T$$

Low eigenvalues indicate smooth (consistent) sections.

## Applications

### Heterogeneous Graphs
Different node/edge types with specific relationships:
- Knowledge graphs
- Multi-relational networks
- Typed social networks

### Opinion Dynamics
Model disagreement with discourse sheaves:
- Stalks: opinion spaces
- Maps: how agents perceive others' opinions
- Laplacian dynamics: consensus or polarization

### [[concepts/graph-neural-networks|Sheaf Neural Networks]]
Generalize GNNs with sheaf structure:
$$\mathbf{H}^{(l+1)} = \sigma\left((\mathbf{I} - \mathbf{L}_\mathcal{F})\mathbf{H}^{(l)}\mathbf{W}^{(l)}\right)$$

Learn restriction maps alongside weights.

### [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes]]
Kernels via sheaf Laplacian spectral functions:
$$k_\mathcal{F}(\mathbf{x}, \mathbf{x}') = g(\mathbf{L}_\mathcal{F})$$

Richer covariance structure than scalar Laplacian.

### Signal Processing on Sheaves
Extend [[concepts/graph-signal-processing|GSP]] concepts:
- Sheaf [[concepts/graph-fourier-transform|Fourier transform]]
- Sheaf [[concepts/spectral-graph-filters|filtering]]
- Sheaf wavelets

## Comparison

| Aspect | Graph Laplacian | Sheaf Laplacian |
|--------|----------------|-----------------|
| Node data | Scalar $\mathbb{R}$ | Vector $\mathbb{R}^{d_v}$ |
| Edge encoding | Weight only | Linear map |
| Matrix size | $N \times N$ | $\sum d_v \times \sum d_v$ |
| Kernel | Constants | Global sections |
| Complexity | $O(N^2)$ | $O((\sum d_v)^2)$ |

## Examples

### Orientable Sheaf
Restriction maps are $\pm 1$ based on edge orientation:
$$\mathbf{L}_\mathcal{F} = \mathbf{B}\mathbf{B}^T$$

where $\mathbf{B}$ is the incidence matrix.

### Feature Transformation Sheaf
Maps transform features between node types:
- Nodes have embeddings in different spaces
- Edge maps align representations

### Consensus Sheaf
Identity maps everywhere (standard Laplacian behavior):
- Stalks are all $\mathbb{R}^d$
- Maps are identity $\mathbf{I}_d$

## Computational Considerations

### Sparsity
Like graph Laplacian, sheaf Laplacian is sparse:
- Non-zero blocks only for adjacent nodes
- Block size varies with stalk dimensions

### Learning Restriction Maps
In neural network setting:
- Parameterize $\mathcal{F}_{v \triangleleft e}$ as learnable matrices
- Optimize via backpropagation
- Share parameters across similar edges

## See Also

- [[concepts/graph-laplacian|Graph Laplacian]]
- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-neural-networks|Graph Neural Networks]]
- [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]
