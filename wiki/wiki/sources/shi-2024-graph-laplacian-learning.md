---
title: "Generalizing Graph Laplacian Learning (Shi 2024)"
page_id: sources/shi-2024-graph-laplacian-learning
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [graph-learning, graph-laplacian, graph-signal-processing, exponential-family, product-graphs]
authors: [Changhao Shi]
year: 2024
institution: UC San Diego
degree: PhD
supervisor: Gal Mishne
related: [concepts/graph-laplacian, concepts/graph-signal-processing, concepts/graph-fourier-transform, entities/changhao-shi, entities/gal-mishne]
---

# Generalizing Graph Laplacian Learning: A Graph Signal Processing Perspective

**Author:** [[entities/changhao-shi|Changhao Shi]]
**Supervisor:** [[entities/gal-mishne|Gal Mishne]]
**Institution:** University of California San Diego
**Year:** 2024 (PhD Dissertation)

## Summary

This dissertation expands the scope of graph learning beyond Gaussian-distributed data, introducing methods for learning [[concepts/graph-laplacian|graph Laplacians]] from various data types and imposing structural priors such as product graphs. The work also presents a deep learning framework for defending against adversarial attacks using manifold geometry.

## Key Contributions

### 1. Graph Learning with Exponential Family Noise (GLEN)
- Extends graph inference beyond Gaussian noise models
- Uses conditional exponential family distributions for diverse data types
- Jointly infers the combinatorial [[concepts/graph-laplacian|graph Laplacian]] and latent smooth signal representations
- Supports binary, count, and other non-Gaussian data types
- Published in *IEEE Transactions on Signal and Information Processing over Networks*

### 2. Multi-way Graph Learning (MWGL)
- Addresses graph inference from multi-way (tensor) signals
- Handles signals on Cartesian product graphs
- Provides theoretical guarantees: existence, uniqueness, consistency
- Published at AISTATS 2024

### 3. Kronecker Structured Graph Learning (KSGL)
- Learns product graphs with Kronecker structure
- Efficiently handles strong product graphs
- Proves asymptotic convergence to true [[concepts/graph-laplacian|graph Laplacian]]
- Applications to EEG data analysis (brain connectivity)

### 4. Self-Supervised Online Adversarial Purification (SOAP)
- Uses manifold geometry to defend against adversarial attacks
- Characterizes underlying manifold via self-supervised auxiliary tasks
- Retracts malicious samples back to data manifold
- Published at ICLR 2021

## Technical Framework

### GLEN Noise Model
The observed signal $\mathbf{y}$ is generated from a latent smooth signal $\mathbf{x}$:
$$p(\mathbf{y}|\mathbf{x}) = \exp\left(\theta(\mathbf{x})^T T(\mathbf{y}) - A(\theta(\mathbf{x}))\right)$$

where $\theta$ is the natural parameter linked to $\mathbf{x}$ via a link function.

### Product Graph Structure
For Cartesian products:
$$\mathbf{L} = \mathbf{L}_1 \oplus \mathbf{L}_2 = \mathbf{L}_1 \otimes \mathbf{I}_2 + \mathbf{I}_1 \otimes \mathbf{L}_2$$

For Kronecker products:
$$\mathbf{L} = \mathbf{L}_1 \otimes \mathbf{L}_2$$

## Applications

- **Chicago Crime Dataset:** Learning crime type relationships from spatial count data
- **Animals Dataset:** Inferring taxonomic structure from feature similarities
- **Neural Spiking Data:** Denoising with temporal variation penalties
- **Molene Weather Data:** Learning station connectivity from temperature readings
- **EEG Analysis:** Brain connectivity inference from epileptic signals

## Key Results

- GLEN outperforms Gaussian-based methods (CGL, GLS) on non-Gaussian synthetic data
- Product graph methods achieve better sample efficiency than unstructured learning
- Theoretical consistency bounds: $\|\hat{\mathbf{L}} - \mathbf{L}^*\| = O(n^{-1/2})$

## Related Work

- [[sources/dong-2020-gsp-for-ml|GSP for Machine Learning]]
- [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]

## See Also

- [[concepts/graph-laplacian|Graph Laplacian]]
- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/graph-fourier-transform|Graph Fourier Transform]]
