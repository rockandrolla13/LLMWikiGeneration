---
title: "Gaussian Processes on Graphs (Zhi 2024)"
page_id: sources/zhi-2024-gaussian-processes-graphs
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [gaussian-processes, graph-signal-processing, spectral-methods, machine-learning, bayesian-inference]
authors: [Yin-Cong Zhi]
year: 2024
institution: University of Oxford
degree: DPhil
supervisor: Xiaowen Dong
related: [concepts/gaussian-processes, concepts/graph-signal-processing, concepts/graph-laplacian, concepts/spectral-graph-wavelets, concepts/sheaf-laplacian, entities/xiaowen-dong, entities/yin-cong-zhi]
---

# Gaussian Processes on Graphs

**Author:** [[entities/yin-cong-zhi|Yin-Cong Zhi]]
**Supervisor:** [[entities/xiaowen-dong|Xiaowen Dong]]
**Institution:** University of Oxford, St Anne's College
**Year:** 2024 (DPhil Thesis)

## Summary

This doctoral thesis develops a series of [[concepts/gaussian-processes|Gaussian processes]] (GPs) for graph-structured data, leveraging [[concepts/graph-signal-processing|graph signal processing]] tools to handle smoothness modeling on graphs. The work addresses the limited availability of probabilistic and Bayesian methods for graph data compared to the abundance of [[concepts/graph-neural-networks|graph neural network]] literature.

## Key Contributions

### 1. Spectral Kernel Learning for Graph Signal Prediction
- Uses kernels defined from the [[concepts/graph-laplacian|graph Laplacian]] with learnable spectral filters
- Predicts graph signal evolution using multi-output Gaussian processes
- Enables smoothness levels to adapt to data characteristics
- Published in *Transactions on Signal and Information Processing over Networks* (2022)

### 2. Adaptive GP via Spectral Graph Wavelets
- Novel utilization of [[concepts/spectral-graph-wavelets|spectral graph wavelets]] for semi-supervised classification
- Captures multi-scale properties in graph data
- Learns optimal wavelet scales for data-driven adaptation
- Uses polynomial approximation for scalability (avoiding expensive eigendecomposition)
- Published at AISTATS 2022

### 3. Transductive Kernels for Attributed Graphs
- Unified definition of kernels combining graph structure and node features
- Derives kernels from regularization theory using both Laplace operator and [[concepts/graph-laplacian|graph Laplacian]]
- Enables transductive learning using distribution of full dataset
- Presented at GSP Workshop 2023

### 4. Sheaf Laplacian Gaussian Processes
- Introduces [[concepts/sheaf-laplacian|sheaves]] as higher-order graph representation
- Learns restriction maps via neural network within GP training
- Provides stronger separation power for heterophilic graphs
- Addresses over-smoothing limitations of standard graph methods

## Technical Highlights

- **Spectral Function Learning:** Learning discrete kernels via their spectral function using constrained polynomial optimization
- **Multi-scale Modeling:** Wavelets as band-pass filters capture spectral patterns at different scales (cluster of eigenvalues)
- **Transductive Properties:** Kernels that leverage test and unlabeled data distribution for improved prediction
- **Sheaf Learning:** One-dimensional sheaves modify graph structure during training for better classification

## Key Equations

The graph Laplacian spectral decomposition:
$$\mathbf{L} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^T$$

Graph spectral kernel:
$$k(\mathbf{x}, \mathbf{x}') = g(\mathbf{L})$$

where $g$ is a learnable polynomial function of eigenvalues.

## Applications

- Graph signal prediction
- Semi-supervised node classification (Cora, Citeseer, Pubmed)
- Multi-scale graph analysis

## Related Work

This thesis builds on and extends:
- [[sources/dong-2020-gsp-for-ml|Graph Signal Processing for Machine Learning]] review
- Multi-output Gaussian process literature
- [[concepts/graph-neural-networks|Graph neural network]] architectures

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/gaussian-processes|Gaussian Processes]]
- [[concepts/spectral-graph-wavelets|Spectral Graph Wavelets]]
- [[concepts/transductive-learning|Transductive Learning]]
- [[concepts/sheaf-laplacian|Sheaf Laplacian]]
