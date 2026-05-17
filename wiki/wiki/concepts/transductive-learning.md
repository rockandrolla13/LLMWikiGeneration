---
title: "Transductive Learning"
page_id: concepts/transductive-learning
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [machine-learning, semi-supervised-learning, graph-learning, statistical-learning]
related: [concepts/graph-neural-networks, concepts/graph-convolutional-networks, concepts/graph-signal-processing, sources/dong-2020-gsp-for-ml, sources/zhi-2024-gaussian-processes-graphs]
---

# Transductive Learning

Transductive learning is a machine learning paradigm where the model reasons directly from training examples to specific test examples, without constructing a general predictive function.

## Definition

In transductive learning:
- **Training data:** Labeled examples $\{(\mathbf{x}_i, y_i)\}_{i=1}^l$
- **Test data:** Unlabeled examples $\{\mathbf{x}_j\}_{j=l+1}^{l+u}$ **known at training time**
- **Goal:** Predict labels for the specific test examples

Unlike inductive learning, which learns a function $f: \mathcal{X} \to \mathcal{Y}$, transductive learning directly predicts test labels.

## Comparison with Inductive Learning

| Aspect | Inductive | Transductive |
|--------|-----------|--------------|
| Test data | Unknown at training | Known at training |
| Output | General function $f$ | Labels for specific points |
| Generalization | To any new example | Only to given test set |
| Philosophy | Learn rule, then apply | Reason case-by-case |
| Graph methods | Inductive GNNs (GraphSAGE) | [[concepts/graph-convolutional-networks|GCN]], label propagation |

## Theoretical Foundation

### Vapnik's Principle
"When solving a problem of interest, do not solve a more general problem as an intermediate step."

Transduction avoids the harder problem of function estimation when only specific predictions are needed.

### Sample Complexity
For fixed test set, transduction can require fewer labeled examples than induction, especially when:
- Test distribution matches training
- Unlabeled data provides structure information

## Methods

### Graph-based Methods
Most natural for transduction - exploit manifold structure.

**Label Propagation:**
$$\mathbf{Y}^{(t+1)} = \alpha \mathbf{S}\mathbf{Y}^{(t)} + (1-\alpha)\mathbf{Y}^{(0)}$$

where $\mathbf{S}$ is normalized affinity matrix.

**[[concepts/graph-convolutional-networks|Graph Convolutional Networks]]:**
Semi-supervised node classification is inherently transductive:
- All nodes (labeled + unlabeled) present in graph
- Information propagates through edges
- Test nodes inform representations

**[[concepts/gaussian-processes|Gaussian Processes]]:**
[[sources/zhi-2024-gaussian-processes-graphs|GPs on graphs]] are naturally transductive:
$$p(\mathbf{f}_* | \mathbf{X}, \mathbf{y}, \mathbf{X}_*) = \mathcal{N}(\boldsymbol{\mu}_*, \boldsymbol{\Sigma}_*)$$

Posterior depends on both train and test inputs.

### Transductive SVM
Maximize margin while assigning labels to unlabeled points:
$$\min_{\mathbf{w}, b, \mathbf{y}_u} \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_i \xi_i$$

subject to margin constraints for all points.

### Semi-supervised Approaches
Many semi-supervised methods are transductive:
- Manifold regularization
- Co-training (with fixed unlabeled pool)
- Self-training

## Connection to GSP

[[sources/dong-2020-gsp-for-ml|Graph signal processing]] provides theoretical grounding:

### Smoothness Assumption
Transductive methods assume labels vary smoothly on the data manifold:
$$\min_\mathbf{f} \sum_{i: y_i \text{ known}} (f_i - y_i)^2 + \lambda \mathbf{f}^T\mathbf{L}\mathbf{f}$$

The graph Laplacian regularizer encourages smooth solutions.

### Spectral Perspective
Label propagation is [[concepts/spectral-graph-filters|spectral filtering]]:
$$\mathbf{f}^* = (\mathbf{I} + \alpha\mathbf{L})^{-1}\mathbf{y}_0$$

This is a low-pass filter on the initial label signal.

## Advantages

1. **Efficiency:** Avoid learning unnecessary function complexity
2. **Data utilization:** Unlabeled test data provides structure
3. **Small sample:** Can work with very few labels
4. **Graph structure:** Natural fit for networked data

## Limitations

1. **No generalization:** Cannot predict new examples
2. **Scalability:** Some methods require all test data in memory
3. **Concept drift:** If test distribution changes, must retrain
4. **Fixed test set:** Assumes test examples known upfront

## Applications

### Citation Networks
Classify papers using citation graph:
- Training: labeled papers
- Test: unlabeled papers in same network
- [[concepts/graph-convolutional-networks|GCN]] propagates labels through citations

### Social Networks
Community detection, user classification with partial labels.

### Biological Networks
Protein function prediction in interaction networks.

### [[sources/zhi-2024-gaussian-processes-graphs|Spatial Interpolation]]
Predict values at specific unobserved locations using GP with graph kernel.

## Code Example (Label Propagation)

```python
import numpy as np

def label_propagation(W, y_labeled, labeled_mask, alpha=0.5, max_iter=100):
    """
    Transductive label propagation.
    W: affinity matrix
    y_labeled: initial labels (0 for unlabeled)
    labeled_mask: boolean mask for labeled nodes
    """
    # Normalize
    D = np.diag(W.sum(axis=1))
    D_inv_sqrt = np.diag(1.0 / np.sqrt(np.diag(D) + 1e-10))
    S = D_inv_sqrt @ W @ D_inv_sqrt

    Y = y_labeled.copy()
    Y_0 = y_labeled.copy()

    for _ in range(max_iter):
        Y = alpha * S @ Y + (1 - alpha) * Y_0
        Y[labeled_mask] = Y_0[labeled_mask]  # Clamp labeled

    return Y
```

## See Also

- [[concepts/graph-convolutional-networks|Graph Convolutional Networks]]
- [[concepts/graph-neural-networks|Graph Neural Networks]]
- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[sources/dong-2020-gsp-for-ml|GSP for Machine Learning Review]]
- [[sources/zhi-2024-gaussian-processes-graphs|Gaussian Processes on Graphs]]
