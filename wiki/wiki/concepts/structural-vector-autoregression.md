---
title: "Structural Vector Autoregression"
page_id: concepts/structural-vector-autoregression
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [time-series, causal-inference, econometrics, dag-learning]
related: [concepts/graph-signal-processing, sources/misiakos-2025-dag-tfrc, entities/markus-puschel]
---

# Structural Vector Autoregression

Structural Vector Autoregression (SVAR) models extend standard VAR models to capture contemporaneous causal relationships between time series variables, enabling causal inference from observational data.

## Definition

### Standard VAR Model
$$\mathbf{x}_t = \sum_{k=1}^p \mathbf{A}_k \mathbf{x}_{t-k} + \boldsymbol{\varepsilon}_t$$

where:
- $\mathbf{x}_t \in \mathbb{R}^N$: vector of $N$ time series at time $t$
- $\mathbf{A}_k$: autoregressive coefficient matrices
- $\boldsymbol{\varepsilon}_t$: error terms (correlated)

### Structural Form (SVAR)
$$\mathbf{B}_0 \mathbf{x}_t = \sum_{k=1}^p \mathbf{B}_k \mathbf{x}_{t-k} + \mathbf{u}_t$$

where:
- $\mathbf{B}_0$: contemporaneous effect matrix
- $\mathbf{u}_t$: structural shocks (uncorrelated)
- Relationship: $\boldsymbol{\varepsilon}_t = \mathbf{B}_0^{-1}\mathbf{u}_t$

## Causal Interpretation

### DAG Structure
$\mathbf{B}_0$ encodes a directed acyclic graph (DAG):
- $(\mathbf{B}_0)_{ij} \neq 0$: variable $j$ has contemporaneous effect on $i$
- Diagonal elements typically normalized to 1
- Off-diagonal elements are causal coefficients

### Window Graph
[[sources/misiakos-2025-dag-tfrc|Misiakos & Püschel (2025)]] extend to **window graphs**:
- Nodes: $\{x_i^{(t-k)}\}$ for each variable $i$ and lag $k$
- Edges: both contemporaneous ($\mathbf{B}_0$) and lagged ($\mathbf{B}_k$)
- Full temporal causal structure

## Identification Problem

### Challenge
Standard VAR estimation gives reduced form:
$$\mathbf{x}_t = \sum_k \mathbf{A}_k \mathbf{x}_{t-k} + \boldsymbol{\varepsilon}_t$$

But infinitely many $\mathbf{B}_0$ satisfy $\boldsymbol{\Sigma}_\varepsilon = \mathbf{B}_0^{-1}\boldsymbol{\Sigma}_u \mathbf{B}_0^{-T}$

### Identification Strategies

**Short-run restrictions:**
- Cholesky decomposition (recursive structure)
- Zero restrictions on $\mathbf{B}_0$
- Sign restrictions

**Long-run restrictions:**
- Permanent vs transitory shocks
- Blanchard-Quah decomposition

**Non-Gaussianity (LiNGAM):**
- Assumes non-Gaussian shocks
- Achieves unique identification
- Basis for [[sources/misiakos-2025-dag-tfrc|DAG-TFRC]]

**Few Root Causes:**
- Sparse driving signals
- [[sources/misiakos-2025-dag-tfrc|DAG-TFRC]] approach

## DAG-TFRC Method

[[sources/misiakos-2025-dag-tfrc|Misiakos & Püschel (2025)]] introduce:

### Model
$$\mathbf{x}_t = \sum_{k=0}^p \mathbf{W}_k \mathbf{x}_{t-k} + \mathbf{s}_t$$

where $\mathbf{s}_t$ is sparse (few root causes).

### Optimization
$$\min_{\mathbf{W}, \mathbf{s}} \sum_t \|\mathbf{s}_t\|_1 \quad \text{s.t.} \quad \mathbf{W}_0 \in \text{DAG}$$

### Advantages
- Scales to thousands of nodes
- Identifiability guarantees
- No distributional assumptions (beyond sparsity)

## Connection to GSP

### Graph Structure
SVAR coefficients define a directed graph:
- Weighted adjacency from $\mathbf{B}_0$ and $\{\mathbf{B}_k\}$
- [[concepts/graph-signal-processing|GSP]] tools applicable after DAG learned

### Spectral Analysis
[[sources/yu-2024-graph-learning-financial|Financial network analysis]]:
- Learn SVAR structure from returns
- Apply spectral methods for clustering
- Identify market regimes

## Estimation Methods

### Maximum Likelihood
Assuming Gaussian errors:
$$\mathcal{L}(\mathbf{B}) = -\frac{T}{2}\log|\boldsymbol{\Sigma}_u| - \frac{1}{2}\sum_t \mathbf{u}_t^T\boldsymbol{\Sigma}_u^{-1}\mathbf{u}_t$$

### Bayesian Methods
Prior distributions on $\mathbf{B}_k$ matrices:
- Minnesota prior (shrinkage)
- Spike-and-slab (sparsity)

### Score-based Methods
Optimize score function + acyclicity constraint (NOTEARS, DAG-GNN).

## Applications

### Macroeconomics
- Monetary policy transmission
- Fiscal multipliers
- Business cycle analysis

### Finance
- [[sources/yu-2024-graph-learning-financial|Stock return networks]]
- Volatility spillovers
- Contagion analysis

### Neuroscience
- Effective connectivity
- Brain region interactions
- Stimulus response

## Code Example (Conceptual)

```python
import numpy as np
from scipy.linalg import solve_triangular

def estimate_svar_cholesky(X, p=1):
    """
    Estimate SVAR with Cholesky identification.
    X: (T, N) time series data
    """
    T, N = X.shape

    # Estimate reduced form VAR
    Y = X[p:]  # (T-p, N)
    Z = np.hstack([X[p-k-1:T-k-1] for k in range(p)])  # (T-p, N*p)

    # OLS: Y = Z @ A.T + E
    A = np.linalg.lstsq(Z, Y, rcond=None)[0].T  # (N, N*p)
    E = Y - Z @ A.T

    # Residual covariance
    Sigma = E.T @ E / (T - p)

    # Cholesky identification
    B0_inv = np.linalg.cholesky(Sigma)  # Lower triangular

    return A, B0_inv

```

## See Also

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[sources/misiakos-2025-dag-tfrc|DAG-TFRC Paper]]
- [[entities/markus-puschel|Markus Püschel]]
- [[sources/yu-2024-graph-learning-financial|Financial Network Analysis]]
