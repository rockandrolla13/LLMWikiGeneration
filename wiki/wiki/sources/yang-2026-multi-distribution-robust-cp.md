---
title: Multi-Distribution Robust Conformal Prediction
page_id: sources/yang-2026-multi-distribution-robust-cp
page_type: source
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Yuqi Yang
- Ying Jin
publication: arXiv
year: 2026
arxiv: '2601.02998'
tags:
- conformal-prediction
- multi-distribution
- robustness
- fairness
- distributionally-robust-optimization
related:
- concepts/conformal-prediction
- concepts/multi-distribution-robust-cp
- concepts/worst-case-coverage
- concepts/distributionally-robust-optimization
- concepts/max-p-aggregation
mind_map_priority: high
schema_version: 2
uuid: 79f5e921-f246-5ab6-baf1-af85b2a9f4f6
content_hash: sha256:e1c8067f46da873d914355c75007c34ad4888a049f2f6409f3b7075a141b99dd
---

<!-- AUTHORED REGION START -->
# Multi-Distribution Robust Conformal Prediction

## Summary

This paper introduces **Multi-Distribution Conformal Prediction (MDCP)**, a framework for constructing prediction sets that achieve valid coverage simultaneously across multiple heterogeneous source distributions. The key insight is a **max-p aggregation** scheme that combines per-source conformal p-values to guarantee finite-sample uniform validity, paired with an optimization approach to learn efficient conformity scores.

## Key Contributions

1. **Max-p aggregation scheme**: A simple mechanism that delivers finite-sample, multi-distribution coverage by taking the maximum of per-source p-values
2. **Optimality characterization**: Proves that max-p aggregation is optimal and tight when paired with properly learned conformity scores
3. **End-to-end learning algorithm**: Provides practical algorithms for both classification and regression that learn efficient scores via dual optimization
4. **Theoretical foundations**: Establishes connections to distributionally robust optimization and group fairness

## Problem Setting

Given labeled data D = ∪ᵢ D⁽ᵏ⁾ from K heterogeneous sources, each with i.i.d. samples from distribution P⁽ᵏ⁾, construct prediction set Ĉ(X_{n+1}) with **uniform coverage**:

> min_k P_{D×P^(k)} (Y_{n+1} ∈ Ĉ(X_{n+1})) ≥ 1 - α

This ensures valid coverage regardless of which source the test point comes from.

## Core Method

### Max-p Aggregation
For each source k, compute conformal p-values:
- p⁽ᵏ⁾(y) = (1/(n_k+1)) Σᵢ 1{s_k(X_i⁽ᵏ⁾, Y_i⁽ᵏ⁾) ≥ s_k(x,y)}

The aggregated prediction set is:
- Ĉ(x) = {y : max_k p⁽ᵏ⁾(y) ≥ α} = ∪_k Ĉ⁽ᵏ⁾(x)

### Theorem 1: Finite-Sample Uniform Validity
For any mixture distribution P = Σ_k π_k P⁽ᵏ⁾:
> P(Y_{n+1} ∈ Ĉ(X_{n+1})) ≥ 1 - α

### Optimal Score Learning
The optimal conformity score has the form:
- h*(x,y) = Σ_k λ*_k(x) f_k(y|x)

where λ*(x) are dual weights from solving:
- max_{λ≥0} ∫ [(h_λ(x,y) - 1)_+] dμ(y) - (1-α) Σ_k λ_k(x)

### Theorem 2: Conditional Optimality
The optimal prediction set C*(x) takes the form:
- C*(x) = {y : h_{λ*}(x,y) > 1} ∪ S(x)

Complementary slackness ensures at least one source achieves exactly 1-α coverage (tightness).

## Theoretical Results

### Key Properties
1. **Tightness**: The worst-case coverage is exactly 1-α for at least one source
2. **Efficiency**: Max-p with optimal scores achieves minimal prediction set size
3. **Consistency**: Under mild conditions, learned scores converge to optimal

### Theorem 3: Asymptotic Optimality
Under consistent estimation of f_k and λ*:
> lim sup |Ĉ⁽ⁿ⁾| - |C*| ≤ ρ(T)

where T is the boundary tie-region with measure ρ(T).

## Practical Algorithm

1. **Train per-source models**: Fit classifiers p̂_k(y|x) or density estimators f̂_k(y|x)
2. **Learn dual weights**: Solve empirical dual objective using splines/neural networks
3. **Construct MDCP set**: Apply max-p aggregation with learned scores s_k(x,y) = -Σ_ℓ λ̂_ℓ(x)f̂_ℓ(y|x)

## Motivating Applications

1. **Fairness without protected attributes**: Achieve group-conditional coverage without knowing test group membership
2. **Subpopulation shift**: Protection against arbitrary mixture of subpopulations at test time
3. **Multi-source data**: Valid coverage for data from any individual source in federated settings

## Comparison with Related Work

| Setting | Method | Test Distribution | Coverage |
|---------|--------|-------------------|----------|
| Single-source | Standard CP | Same as training | Marginal |
| Group-known | Group-conditional CP | Known group at test | Per-group |
| **Multi-source** | **MDCP (this paper)** | Any source/mixture | Uniform |

## Notable Quotes

> "Any prediction set obeying uniform coverage guarantees valid coverage under any subpopulation shift."

> "The max-p aggregation is both optimal and tight: it achieves oracle-optimal size and exact 1-α coverage for the hardest source."

## Questions Raised

- How does efficiency scale with the number of sources K?
- Can the method handle sources with different feature spaces?
- What happens when sources have significant overlap vs. separation?

## Related Concepts

- [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]]
- [[concepts/max-p-aggregation|Max-p Aggregation]]
- [[concepts/worst-case-coverage|Worst-Case Coverage]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/distributionally-robust-optimization|Distributionally Robust Optimization]]

## Related Entities

- [[entities/yuqi-yang|Yuqi Yang]] - University of Pennsylvania
- [[entities/ying-jin|Ying Jin]] - Stanford/UPenn, conformal prediction researcher

<!-- AUTHORED REGION END -->
