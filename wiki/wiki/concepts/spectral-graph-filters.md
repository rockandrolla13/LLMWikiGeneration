---
title: Spectral Graph Filters
page_id: concepts/spectral-graph-filters
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- graph-signal-processing
- filtering
- spectral-methods
- signal-processing
related:
- concepts/graph-signal-processing
- concepts/graph-fourier-transform
- concepts/graph-laplacian
- concepts/graph-neural-networks
- concepts/spectral-graph-wavelets
schema_version: 2
uuid: 2de40904-9526-5242-989d-54fb66eacb8d
content_hash: sha256:09ea1b26d06325618df66cac8ad6fc99f7f3b8dfe973e0e19ff49e5b0733b5ea
---

<!-- AUTHORED REGION START -->
# Spectral Graph Filters

Spectral graph filters extend classical frequency-domain filtering to signals on graphs, enabling operations like smoothing, sharpening, and band-pass filtering on irregular domains.

## Definition

A spectral graph filter applies a transfer function $g(\lambda)$ to the eigenvalues of the [[concepts/graph-laplacian|graph Laplacian]]:

$$g(\mathbf{L}) = \mathbf{U}g(\mathbf{\Lambda})\mathbf{U}^T$$

**Filtering operation:**
$$\mathbf{y} = g(\mathbf{L})\mathbf{x} = \mathbf{U}g(\mathbf{\Lambda})\mathbf{U}^T\mathbf{x}$$

Equivalently in the [[concepts/graph-fourier-transform|spectral domain]]:
$$\hat{\mathbf{y}} = g(\mathbf{\Lambda})\hat{\mathbf{x}}$$

## Filter Types

### Low-Pass Filters
Preserve smooth signal components, suppress high-frequency variations.

**Regularized Laplacian:**
$$g(\lambda) = \frac{1}{1 + \alpha\lambda}$$

**Heat kernel:**
$$g(\lambda) = e^{-\alpha\lambda}$$

**Applications:** Denoising, smoothing, averaging over neighborhoods.

### High-Pass Filters
Emphasize rapid variations between neighbors.

**Laplacian filter:**
$$g(\lambda) = \lambda$$

**Bandstop complement:**
$$g(\lambda) = \frac{\alpha\lambda}{1 + \alpha\lambda}$$

**Applications:** Edge detection, anomaly detection, change detection.

### Band-Pass Filters
Select specific frequency bands.

**Wavelet kernels:**
$$g(\lambda) = \lambda^\alpha e^{-\beta\lambda}$$

**Applications:** [[concepts/spectral-graph-wavelets|Graph wavelets]], scale-specific analysis.

### All-Pass (Phase) Filters
Modify phase without changing magnitude.

$$|g(\lambda)| = 1, \quad \angle g(\lambda) = \phi(\lambda)$$

## Polynomial Filters

To avoid expensive eigendecomposition, filters can be approximated by polynomials:

$$g(\mathbf{L}) \approx \sum_{k=0}^K c_k \mathbf{L}^k$$

### Advantages
- **Computational cost:** $O(K|E|)$ vs $O(N^3)$ for exact
- **Localization:** $K$-hop spatial support
- **No eigendecomposition:** Scalable to large graphs

### Chebyshev Approximation
$$g(\mathbf{L}) \approx \sum_{k=0}^K c_k T_k(\tilde{\mathbf{L}})$$

where $\tilde{\mathbf{L}} = \frac{2}{\lambda_{max}}\mathbf{L} - \mathbf{I}$ and $T_k$ are Chebyshev polynomials.

**Benefits:**
- Minimax approximation properties
- Recurrence relation: $T_{k+1}(x) = 2xT_k(x) - T_{k-1}(x)$
- Basis for [[concepts/graph-neural-networks|ChebNet]]

## Connection to Neural Networks

### [[concepts/graph-convolutional-networks|Graph Convolutional Networks]]
GCN layer is a first-order spectral filter:
$$g(\mathbf{L}) = \mathbf{I} - \mathbf{L} = \tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}$$

### ChebNet
Learnable Chebyshev polynomial filters:
$$g_\theta(\mathbf{L}) = \sum_{k=0}^K \theta_k T_k(\tilde{\mathbf{L}})$$

### Spectral CNN
Full spectral filters with learnable frequency response.

## Design Methods

### Ideal Filter Approximation
Design polynomial to approximate desired frequency response:
1. Specify ideal $g(\lambda)$
2. Sample or integrate error
3. Minimize approximation error

### Learning from Data
Learn filter coefficients to optimize task objective:
$$\min_\theta \mathcal{L}(g_\theta(\mathbf{L})\mathbf{X}, \mathbf{Y})$$

### Diffusion-Based Design
Filters derived from random walks or heat diffusion.

## Properties

### Graph Convolution Theorem
Filtering equals pointwise multiplication in spectral domain:
$$g(\mathbf{L})\mathbf{x} \Leftrightarrow g(\mathbf{\Lambda}) \odot \hat{\mathbf{x}}$$

### Shift-Invariance (Graph Sense)
$$g(\mathbf{L})(\mathbf{L}\mathbf{x}) = \mathbf{L}(g(\mathbf{L})\mathbf{x})$$

Filters commute with graph shift.

### Stability
Small perturbations in graph yield small changes in filter output (for continuous $g$).

## Computational Considerations

| Method | Preprocessing | Per-filter Cost | Memory |
|--------|--------------|-----------------|--------|
| Exact spectral | $O(N^3)$ | $O(N^2)$ | $O(N^2)$ |
| Polynomial | None | $O(K|E|)$ | $O(N)$ |
| Chebyshev | $\lambda_{max}$ estimate | $O(K|E|)$ | $O(N)$ |

## Applications

### [[sources/dong-2020-gsp-for-ml|Machine Learning]]
- Feature extraction
- Node embedding
- Semi-supervised learning

### Signal Processing
- Denoising
- Interpolation
- Compression

### [[sources/shi-2024-graph-laplacian-learning|Graph Learning]]
Regularization via spectral filtering:
$$\min_\mathbf{x} \|\mathbf{y} - \mathbf{x}\|^2 + \alpha \mathbf{x}^T g(\mathbf{L}) \mathbf{x}$$

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-fourier-transform|Graph Fourier Transform]]
- [[concepts/graph-laplacian|Graph Laplacian]]
- [[concepts/graph-neural-networks|Graph Neural Networks]]
- [[concepts/spectral-graph-wavelets|Spectral Graph Wavelets]]

<!-- AUTHORED REGION END -->
