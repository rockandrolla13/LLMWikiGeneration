---
title: Graph Laplacian
page_id: concepts/graph-laplacian
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- linear-algebra
- graphs
- spectral-methods
- graph-signal-processing
related:
- concepts/graph-signal-processing
- concepts/graph-fourier-transform
- concepts/spectral-graph-filters
- sources/shi-2024-graph-laplacian-learning
schema_version: 2
uuid: 8b4fc2fa-5a83-5998-8eb8-9ad0ca6251c6
content_hash: sha256:a0fe3c2ea2a02b3174a54476bb9ff7f954a37e694faf0012c1225cf208368665
---

<!-- AUTHORED REGION START -->
# Graph Laplacian

The graph Laplacian is a fundamental matrix representation of a graph that encodes its structure and serves as the discrete analog of the continuous Laplace operator. It is central to [[concepts/graph-signal-processing|graph signal processing]], spectral clustering, and [[concepts/graph-neural-networks|graph neural networks]].

## Definitions

### Combinatorial Laplacian
For an undirected weighted graph $G = (V, E)$ with adjacency matrix $\mathbf{A}$ and degree matrix $\mathbf{D}$:

$$\mathbf{L} = \mathbf{D} - \mathbf{A}$$

where:
- $\mathbf{D} = \text{diag}(d_1, ..., d_N)$ with $d_i = \sum_j A_{ij}$
- $\mathbf{A}_{ij}$ is the edge weight between nodes $i$ and $j$

### Normalized Laplacians

**Symmetric normalized:**
$$\mathbf{L}_{sym} = \mathbf{D}^{-1/2}\mathbf{L}\mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$$

**Random walk normalized:**
$$\mathbf{L}_{rw} = \mathbf{D}^{-1}\mathbf{L} = \mathbf{I} - \mathbf{D}^{-1}\mathbf{A}$$

## Properties

### Spectral Properties
- **Positive semi-definite:** All eigenvalues $\lambda_i \geq 0$
- **Smallest eigenvalue:** $\lambda_1 = 0$ with eigenvector $\mathbf{1}$ (constant vector)
- **Multiplicity of zero:** Number of connected components
- **Eigenvalue ordering:** $0 = \lambda_1 \leq \lambda_2 \leq ... \leq \lambda_N$

### Quadratic Form
For any signal $\mathbf{x}$:
$$\mathbf{x}^T\mathbf{L}\mathbf{x} = \frac{1}{2}\sum_{i,j} A_{ij}(x_i - x_j)^2$$

This measures the **smoothness** of signal $\mathbf{x}$ on the graph.

### Analogy to Continuous Laplacian
The graph Laplacian is the discrete approximation of the continuous Laplace operator:
$$\Delta = \sum_i \frac{\partial^2}{\partial x_i^2} \longleftrightarrow \mathbf{L}$$

This connection underlies [[concepts/graph-signal-processing|graph signal processing]] theory.

## Eigendecomposition

$$\mathbf{L} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^T$$

where:
- $\mathbf{U} = [\mathbf{u}_1, ..., \mathbf{u}_N]$: eigenvectors (graph Fourier basis)
- $\mathbf{\Lambda} = \text{diag}(\lambda_1, ..., \lambda_N)$: eigenvalues (frequencies)

## Applications

### Spectral Clustering
Using the Fiedler vector (eigenvector of $\lambda_2$) for graph partitioning.

### [[concepts/graph-fourier-transform|Graph Fourier Transform]]
$$\hat{\mathbf{x}} = \mathbf{U}^T\mathbf{x}$$

### [[concepts/spectral-graph-filters|Spectral Graph Filtering]]
$$g(\mathbf{L}) = \mathbf{U}g(\mathbf{\Lambda})\mathbf{U}^T$$

### Graph Regularization
Smoothness penalty in optimization:
$$\min_\mathbf{x} \|\mathbf{y} - \mathbf{x}\|^2 + \alpha \mathbf{x}^T\mathbf{L}\mathbf{x}$$

### [[concepts/graph-neural-networks|Graph Neural Networks]]
- GCN layer: $\mathbf{H}^{(l+1)} = \sigma(\tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}\mathbf{H}^{(l)}\mathbf{W}^{(l)})$
- ChebNet: polynomial filters of $\mathbf{L}$

## Graph Laplacian Learning

[[sources/shi-2024-graph-laplacian-learning|Graph Laplacian learning]] methods infer the Laplacian from smooth signal observations:

$$\min_{\mathbf{L}} \text{tr}(\mathbf{X}^T\mathbf{L}\mathbf{X}) + \text{regularization}$$

subject to Laplacian constraints (positive semi-definite, zero row-sum, non-positive off-diagonal).

### Extensions
- **GLEN:** Learning from non-Gaussian data (exponential family)
- **Product graphs:** Cartesian, Kronecker, strong product structures
- **Multi-way signals:** Tensor data on product graphs

## Variants

### [[concepts/sheaf-laplacian|Sheaf Laplacian]]
Higher-order generalization with restriction maps on edges.

### Magnetic Laplacian
For directed graphs with complex edge weights.

### Signless Laplacian
$\mathbf{Q} = \mathbf{D} + \mathbf{A}$ (uses sum instead of difference).

## Computational Considerations

- **Full eigendecomposition:** $O(N^3)$ - expensive for large graphs
- **Sparse methods:** Lanczos algorithm for top-$k$ eigenvectors
- **Polynomial approximations:** Avoid eigendecomposition (ChebNet)

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-fourier-transform|Graph Fourier Transform]]
- [[concepts/spectral-graph-filters|Spectral Graph Filters]]
- [[concepts/sheaf-laplacian|Sheaf Laplacian]]
- [[sources/shi-2024-graph-laplacian-learning|Graph Laplacian Learning]]

<!-- AUTHORED REGION END -->
