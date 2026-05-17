---
title: "Spectral Graph Wavelets"
page_id: concepts/spectral-graph-wavelets
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [graph-signal-processing, wavelets, spectral-methods, multi-scale-analysis]
related: [concepts/graph-signal-processing, concepts/graph-fourier-transform, concepts/graph-laplacian, concepts/spectral-graph-filters, sources/zhi-2024-gaussian-processes-graphs]
---

# Spectral Graph Wavelets

Spectral graph wavelets extend classical wavelet analysis to graph-structured data, enabling multi-scale analysis of graph signals through localized frequency decomposition.

## Definition

Graph wavelets are constructed via spectral filtering of the [[concepts/graph-laplacian|graph Laplacian]]. For a wavelet generating kernel $g(\lambda)$ and scaling function $h(\lambda)$:

**Wavelet at scale $s$ centered at node $n$:**
$$\psi_{s,n} = g(s\mathbf{L})\delta_n = \mathbf{U}g(s\mathbf{\Lambda})\mathbf{U}^T\delta_n$$

**Scaling function:**
$$\phi_n = h(\mathbf{L})\delta_n$$

where $\delta_n$ is a Kronecker delta at node $n$.

## Wavelet Transform

**Forward Transform:**
$$W_f(s, n) = \langle f, \psi_{s,n} \rangle = [g(s\mathbf{L})f]_n$$

**Scaling Coefficients:**
$$S_f(n) = \langle f, \phi_n \rangle = [h(\mathbf{L})f]_n$$

The transform captures signal content at different scales and locations on the graph.

## Common Wavelet Designs

### Mexican Hat Wavelet
$$g(\lambda) = \lambda e^{-\lambda}$$

Band-pass behavior, sensitive to local variations.

### Heat Kernel Wavelet
$$g_s(\lambda) = e^{-s\lambda} - e^{-2s\lambda}$$

Derived from heat diffusion on graphs.

### Spectral Graph Wavelet (SGWT)
Hammond et al. design with polynomial approximation:
$$g(\lambda) = \lambda^{\alpha} e^{-\lambda/\beta}$$

Efficient computation via Chebyshev polynomials.

## Properties

### Localization
- **Spectral localization:** Wavelet concentrates around frequency $1/s$
- **Spatial localization:** Energy decreases with graph distance from center node
- **Trade-off:** Uncertainty principle applies - cannot perfectly localize in both domains

### Frame Properties
The wavelet system forms a frame if:
$$A\|f\|^2 \leq \|S_f\|^2 + \sum_s \|W_f(s,\cdot)\|^2 \leq B\|f\|^2$$

Tight frames ($A = B$) allow perfect reconstruction.

### Multi-scale Decomposition
Reveals structure at different scales:
- **Large $s$:** Low-frequency, global patterns
- **Small $s$:** High-frequency, local details

## Computational Methods

### Direct Computation
Requires eigendecomposition: $O(N^3)$ preprocessing, $O(N^2)$ per transform.

### Chebyshev Polynomial Approximation
$$g(s\mathbf{L}) \approx \sum_{k=0}^K c_k T_k(\tilde{\mathbf{L}})$$

- **Cost:** $O(K|E|)$ per scale
- **No eigendecomposition needed**
- Basis for scalable implementations

### Fast Graph Wavelet Transform
Exploits sparsity and polynomial approximations for large graphs.

## Applications

### [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]
Multi-scale kernels via wavelet spectral functions:
$$k(\mathbf{x}, \mathbf{x}') = \sum_s \psi_s(\mathbf{x})^T \psi_s(\mathbf{x}')$$

### Signal Denoising
- Threshold wavelet coefficients
- Preserve edges while removing noise
- Scale-selective processing

### Community Detection
- Large-scale wavelets capture community structure
- Small-scale wavelets reveal local connectivity

### Graph Classification
- Wavelet signatures as graph features
- Multi-scale structural descriptors

### Anomaly Detection
- High wavelet coefficients indicate irregularities
- Scale determines anomaly size

## Comparison with Classical Wavelets

| Aspect | Classical | Graph |
|--------|-----------|-------|
| Domain | Regular grid | Arbitrary graph |
| Translation | Shift operator | Graph shift |
| Dilation | Scale by factor | Spectral scaling |
| Basis functions | Predefined (Haar, Daubechies) | Graph-adapted |
| Implementation | FFT-based | Polynomial approximation |

## Extensions

### Diffusion Wavelets
Based on powers of diffusion operator rather than spectral filtering.

### Lifting Scheme
Graph wavelets via prediction and update steps.

### Vertex-Frequency Analysis
Windowed graph Fourier transform for joint analysis.

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-fourier-transform|Graph Fourier Transform]]
- [[concepts/spectral-graph-filters|Spectral Graph Filters]]
- [[concepts/graph-laplacian|Graph Laplacian]]
- [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]
