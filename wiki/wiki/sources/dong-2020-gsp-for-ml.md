---
title: 'Graph Signal Processing for Machine Learning: A Review and New Perspectives'
page_id: sources/dong-2020-gsp-for-ml
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- graph-signal-processing
- machine-learning
- graph-neural-networks
- spectral-methods
- review-paper
authors:
- Xiaowen Dong
- Dorina Thanou
- Laura Toni
- Michael Bronstein
- Pascal Frossard
year: 2020
journal: IEEE Signal Processing Magazine
volume: 37
issue: 6
pages: 117-127
doi: 10.1109/MSP.2020.3014591
related:
- concepts/graph-signal-processing
- concepts/graph-fourier-transform
- concepts/spectral-graph-filters
- concepts/graph-convolutional-networks
- concepts/graph-neural-networks
- entities/xiaowen-dong
schema_version: 2
uuid: 857e1857-d1fe-53b3-aed8-3ae3499dc246
content_hash: sha256:0b65b708fe13befc0883ec1e69fa6d63243152ab9bb6937c7db555c9173689cc
---

<!-- AUTHORED REGION START -->
# Graph Signal Processing for Machine Learning: A Review and New Perspectives

**Authors:** [[entities/xiaowen-dong|Xiaowen Dong]], Dorina Thanou, Laura Toni, Michael Bronstein, Pascal Frossard
**Journal:** IEEE Signal Processing Magazine
**Year:** 2020

## Summary

This comprehensive review surveys the application of [[concepts/graph-signal-processing|graph signal processing]] (GSP) concepts and tools to machine learning, highlighting three key contributions: (1) exploiting data structure and relational priors, (2) improving data and computational efficiency, and (3) enhancing model interpretability.

## Core GSP Concepts for ML

### Graph Fourier Transform
The [[concepts/graph-fourier-transform|graph Fourier transform]] is defined via the [[concepts/graph-laplacian|graph Laplacian]] eigendecomposition:
$$\mathbf{L} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^T$$

where $\mathbf{U}$ contains eigenvectors and $\mathbf{\Lambda}$ contains eigenvalues (frequencies).

### Graph Filtering
[[concepts/spectral-graph-filters|Spectral graph filters]] enable convolution-like operations:
$$\mathbf{y} = g_\theta(\mathbf{L})\mathbf{x} = \mathbf{U}g_\theta(\mathbf{\Lambda})\mathbf{U}^T\mathbf{x}$$

## GSP for Exploiting Data Structure

### Regression for Multiple Response Variables
- Graph regularization for multivariate regression
- Low-pass filtering interpretation: $\mathbf{y} = (\mathbf{I} + \alpha\mathbf{L})^{-1}\mathbf{x}$
- Gaussian process kernels on graphs

### Graph-based Classification
Key architectures:
1. **Spectral CNN** (Bruna et al.): Learned spectral filters, computationally expensive
2. **ChebNet** (Defferrard et al.): K-hop polynomial filters, localized in space
3. **[[concepts/graph-convolutional-networks|GCN]]** (Kipf & Welling): Simplified 1-hop averaging, semisupervised learning

### Clustering and Dimensionality Reduction
- Spectral clustering via graph Laplacian eigenvectors
- [[concepts/spectral-graph-wavelets|Spectral graph wavelets]] for multiscale clustering
- Graph autoencoders for representation learning

## GSP for Efficiency and Robustness

### Data Efficiency
- Graph regularization for improved generalization
- DNN layer regularization via smoothness constraints
- Few-shot and zero-shot learning with graph priors

### Computational Efficiency
- Compressive spectral clustering via graph filtering
- Product graph decomposition for large-scale analysis
- Parallel/vectorized GFT computation

### Robustness
- Stability of spectral graph filters under perturbation
- Lipschitz bounds on GNN output changes
- Robustness against topological noise

## GSP for Model Interpretability

### Hidden Structure Inference
- Graph learning from smooth signals
- Topology inference for understanding complex systems
- Applications: brain connectivity, weather patterns, mobility

### A Posteriori Interpretation
- **MARGIN framework:** Uses high-pass graph filtering to identify influential samples
- Layer-wise DNN interpretation via smoothness analysis
- Graph attention mechanisms for edge importance

## Open Challenges Identified

1. **GSP and Probabilistic Modeling:** Uncertainty in graph topology, Bayesian approaches
2. **GSP and Decision-Making:** Reinforcement learning with graph-structured states
3. **GSP and Model Interpretability:** Relational learning, anisotropic filters
4. **GSP and Higher-Order Structures:** Motifs, simplicial complexes, hypergraphs

## Key References

The paper references foundational GSP works:
- Shuman et al. (2013) - "The emerging field of signal processing on graphs"
- Sandryhaila & Moura (2013) - "Discrete signal processing on graphs"
- Ortega et al. (2018) - "Graph signal processing: Overview, challenges, and applications"

## Impact

This review has been highly influential in bridging GSP and machine learning communities, providing a unified perspective on how signal processing concepts inform neural network design.

## Related Work

- [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]
- [[sources/shi-2024-graph-laplacian-learning|Graph Laplacian Learning]]

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-fourier-transform|Graph Fourier Transform]]
- [[concepts/spectral-graph-filters|Spectral Graph Filters]]
- [[concepts/graph-convolutional-networks|Graph Convolutional Networks]]
- [[concepts/graph-neural-networks|Graph Neural Networks]]

<!-- AUTHORED REGION END -->
