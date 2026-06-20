---
title: Graph Fourier Transform
page_id: concepts/graph-fourier-transform
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- graph-signal-processing
- spectral-methods
- fourier-analysis
- transforms
related:
- concepts/graph-signal-processing
- concepts/graph-laplacian
- concepts/spectral-graph-filters
- concepts/spectral-graph-wavelets
schema_version: 2
uuid: afddfada-3aa5-554a-aed9-8cbc16609058
content_hash: sha256:6ba5b010ded45b01b3f7a8f2331992aade662777177bbcd882846f401b1d9a15
---

<!-- AUTHORED REGION START -->
# Graph Fourier Transform

The Graph Fourier Transform (GFT) extends the classical Fourier transform to signals defined on graphs, enabling frequency-domain analysis of graph-structured data.

## Definition

For a graph signal $\mathbf{x} \in \mathbb{R}^N$ on a graph with [[concepts/graph-laplacian|graph Laplacian]] $\mathbf{L}$ and eigendecomposition $\mathbf{L} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^T$:

**Forward GFT:**
$$\hat{\mathbf{x}} = \mathbf{U}^T\mathbf{x}$$

**Inverse GFT:**
$$\mathbf{x} = \mathbf{U}\hat{\mathbf{x}}$$

The $k$-th Fourier coefficient $\hat{x}_k = \langle \mathbf{x}, \mathbf{u}_k \rangle$ represents the component of $\mathbf{x}$ at graph frequency $\lambda_k$.

## Interpretation

### Frequency on Graphs
- **Low frequencies** (small $\lambda_k$): Smooth signal components varying slowly across edges
- **High frequencies** (large $\lambda_k$): Signal components with rapid variation between neighbors

### Analogy to Classical Fourier
| Classical | Graph |
|-----------|-------|
| Complex exponentials $e^{i\omega t}$ | Laplacian eigenvectors $\mathbf{u}_k$ |
| Frequency $\omega$ | Eigenvalue $\lambda_k$ |
| Laplace operator $\Delta$ | Graph Laplacian $\mathbf{L}$ |

## Properties

### Parseval's Identity
$$\|\mathbf{x}\|^2 = \|\hat{\mathbf{x}}\|^2$$

Energy is preserved in the transform.

### Smoothness in Spectral Domain
The quadratic form relates to frequency content:
$$\mathbf{x}^T\mathbf{L}\mathbf{x} = \sum_{k=1}^N \lambda_k |\hat{x}_k|^2$$

Smooth signals have energy concentrated in low frequencies.

### Convolution Theorem
Graph convolution in vertex domain equals multiplication in spectral domain:
$$\mathbf{y} = g(\mathbf{L})\mathbf{x} \Leftrightarrow \hat{\mathbf{y}} = g(\mathbf{\Lambda})\hat{\mathbf{x}}$$

## Applications

### [[concepts/spectral-graph-filters|Spectral Graph Filtering]]
Design filters by specifying frequency response:
$$g(\mathbf{L}) = \mathbf{U}g(\mathbf{\Lambda})\mathbf{U}^T$$

Common filters:
- **Low-pass:** $g(\lambda) = \frac{1}{1+\alpha\lambda}$ (smooth signals)
- **High-pass:** $g(\lambda) = \frac{\alpha\lambda}{1+\alpha\lambda}$ (edges/anomalies)
- **Band-pass:** [[concepts/spectral-graph-wavelets|Graph wavelets]]

### [[concepts/graph-neural-networks|Graph Neural Networks]]
- **Spectral CNN:** Learnable frequency response $g_\theta(\lambda)$
- **ChebNet:** Polynomial approximation avoiding explicit GFT
- **[[concepts/graph-convolutional-networks|GCN]]:** Simplified first-order approximation

### Signal Analysis
- Frequency decomposition of network data
- Anomaly detection (high-frequency content)
- Denoising (low-pass filtering)

### [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]
Kernels defined via spectral functions:
$$k(\mathbf{L}) = g(\mathbf{L}) = \mathbf{U}g(\mathbf{\Lambda})\mathbf{U}^T$$

## Computational Considerations

### Direct Computation
- Requires eigendecomposition: $O(N^3)$
- Matrix-vector multiply for GFT: $O(N^2)$
- Impractical for large graphs ($N > 10^4$)

### Efficient Alternatives

**Polynomial Approximation:**
$$g(\mathbf{L}) \approx \sum_{k=0}^K c_k T_k(\tilde{\mathbf{L}})$$

where $T_k$ are Chebyshev polynomials. Cost: $O(K|E|)$.

**Random Features:**
Approximate spectral filtering without eigendecomposition.

**Lanczos Methods:**
Compute only top-$k$ eigenvectors for bandlimited signals.

## Variants

### Adjacency-based GFT
Using eigenvectors of adjacency matrix $\mathbf{A}$ instead of Laplacian (Sandryhaila & Moura approach).

### Directed Graph GFT
For directed graphs, uses Jordan decomposition or considers asymmetric operators.

### Windowed GFT
Localized frequency analysis on graphs using vertex localization.

## Limitations

1. **Ordering ambiguity:** Eigenvector sign and ordering can vary
2. **Computational cost:** Full eigendecomposition expensive
3. **Non-uniqueness:** Different bases for same eigenspace
4. **Directed graphs:** Laplacian not symmetric, eigenvectors complex

## Code Example (Conceptual)

```python
import numpy as np
from scipy.linalg import eigh

def graph_fourier_transform(L, x):
    """Compute GFT of signal x on graph with Laplacian L."""
    eigenvalues, U = eigh(L)
    x_hat = U.T @ x
    return x_hat, eigenvalues, U

def inverse_gft(x_hat, U):
    """Inverse GFT."""
    return U @ x_hat
```

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-laplacian|Graph Laplacian]]
- [[concepts/spectral-graph-filters|Spectral Graph Filters]]
- [[concepts/spectral-graph-wavelets|Spectral Graph Wavelets]]

<!-- AUTHORED REGION END -->
