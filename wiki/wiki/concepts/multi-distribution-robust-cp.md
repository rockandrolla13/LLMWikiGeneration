---
title: Multi-Distribution Robust Conformal Prediction
page_id: concepts/multi-distribution-robust-cp
page_type: concept
revision_id: 1
created: 2026-04-26T12:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [conformal-prediction, robustness, fairness, multi-source, distribution-shift]
sources: [sources/yang-2026-multi-distribution-robust-cp]
related: [concepts/conformal-prediction, concepts/max-p-aggregation, concepts/worst-case-coverage, concepts/distributionally-robust-optimization, concepts/conditional-validity]
mind_map_priority: high
---

# Multi-Distribution Robust Conformal Prediction

**Multi-Distribution Robust Conformal Prediction (MDCP)** is a framework for constructing prediction sets that achieve valid coverage uniformly across multiple heterogeneous source distributions. This ensures reliability when the test distribution is unknown but comes from one of the sources or a mixture thereof.

## Problem Setting

Given data from K sources: D = ∪_{k=1}^K D^(k), where each D^(k) contains i.i.d. samples from P^(k), construct a prediction set Ĉ(X) satisfying **uniform coverage**:

> min_k P_{P^(k)}(Y ∈ Ĉ(X)) ≥ 1 - α

This guarantees coverage for any source, unlike standard conformal prediction which only ensures coverage under the training mixture.

## Key Insight: Max-p Aggregation

The [[concepts/max-p-aggregation|max-p aggregation]] scheme provides finite-sample uniform validity:

1. For each source k, compute conformal p-value p^(k)(y)
2. Aggregate: p(y) = max_k p^(k)(y)
3. Prediction set: Ĉ(x) = {y : p(y) ≥ α}

This yields Ĉ(x) = ∪_k Ĉ^(k)(x), the union of per-source sets.

## Optimality and Tightness

A key theoretical contribution is that max-p aggregation is both **optimal** and **tight**:

- **Optimal**: When paired with optimal conformity scores, achieves minimum prediction set size
- **Tight**: The worst-case coverage is exactly 1-α for at least one source

## Optimal Conformity Score

The optimal score function has the form:

> h*(x,y) = Σ_k λ*_k(x) f_k(y|x)

where:
- f_k(y|x) is the conditional density for source k
- λ*_k(x) are dual weights solving a convex optimization problem

The optimal prediction set is: C*(x) = {y : h*(x,y) > 1}

## Learning the Score

MDCP learns scores via empirical dual optimization:

1. **Estimate** per-source models f̂_k(y|x)
2. **Parameterize** λ(x) using splines or neural networks
3. **Optimize** empirical Lagrangian objective
4. **Calibrate** using max-p aggregation

## Applications

### Fairness Without Protected Attributes
When sources represent protected groups, MDCP ensures:
- Valid coverage for all groups
- No need to observe group membership at test time
- Protection against algorithmic discrimination

### Subpopulation Shift
For test distribution P_test = Σ_k π'_k P^(k) with unknown weights:
- Standard CP valid only for training mixture
- MDCP valid for any mixture of sources

### Multi-Source/Federated Learning
When data comes from multiple sites (hospitals, sensors):
- Each site has different characteristics
- MDCP ensures reliability regardless of which site a test point resembles

## Comparison with Related Methods

| Method | Test Distribution | Coverage Type | Requires Group Label? |
|--------|------------------|---------------|----------------------|
| Standard CP | Same as training | Marginal | N/A |
| Group-conditional CP | Known group | Per-group | Yes |
| **MDCP** | Any source/mixture | Uniform worst-case | No |

## Efficiency Considerations

The efficiency-validity tradeoff depends on source heterogeneity:

1. **Nested sources**: One source dominates; efficient set matches larger source
2. **Partially overlapping**: Union may be larger than any single-source set
3. **Well-separated**: Max-p aggregation can be very inefficient without score learning

MDCP's score learning addresses cases (2) and (3) by finding overlapping regions that satisfy all constraints.

## Theoretical Guarantees

1. **Finite-sample validity**: Uniform coverage holds exactly in finite samples
2. **Asymptotic optimality**: With consistent score estimation, set size converges to oracle optimal
3. **Tightness**: At least one source achieves exact 1-α coverage (no over-conservatism)

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/max-p-aggregation|Max-p Aggregation]]
- [[concepts/worst-case-coverage|Worst-Case Coverage]]
- [[concepts/distributionally-robust-optimization|Distributionally Robust Optimization]]
- [[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin (2026)]]
