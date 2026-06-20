---
title: Max-p Aggregation
page_id: concepts/max-p-aggregation
page_type: concept
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- p-values
- aggregation
- multi-source
sources:
- sources/yang-2026-multi-distribution-robust-cp
related:
- concepts/multi-distribution-robust-cp
- concepts/conformal-prediction
- concepts/worst-case-coverage
mind_map_priority: medium
schema_version: 2
uuid: 464136ff-97c8-571b-81f8-4140f9019e1a
content_hash: sha256:71948a5df7b015852606b8475007461ca9083a954cafffcd1fb293c378b068d6
---

<!-- AUTHORED REGION START -->
# Max-p Aggregation

**Max-p aggregation** is a simple but powerful mechanism for constructing prediction sets that are simultaneously valid across multiple data sources. It works by taking the maximum of per-source conformal p-values and inverting to obtain a prediction set.

## Definition

Given K data sources with conformal p-values p^(1)(y), ..., p^(K)(y) for candidate value y:

> p(y) = max_{k=1,...,K} p^(k)(y)

The aggregated prediction set is:

> Ĉ(x) = {y : p(y) ≥ α}

## Key Property: Set Union

The max-p prediction set equals the union of per-source sets:

> Ĉ(x) = ∪_{k=1}^K Ĉ^(k)(x)

where Ĉ^(k)(x) = {y : p^(k)(y) ≥ α} is the conformal set for source k.

**Proof**: y ∈ Ĉ(x) ⟺ max_k p^(k)(y) ≥ α ⟺ ∃k : p^(k)(y) ≥ α ⟺ y ∈ ∪_k Ĉ^(k)(x)

## Finite-Sample Validity

**Theorem**: For any mixture distribution P = Σ_k π_k P^(k) and any weights π_k ≥ 0 with Σ_k π_k = 1:

> P(Y ∈ Ĉ(X)) ≥ 1 - α

This holds because:
1. Each p^(k)(Y) is a valid p-value under P^(k)
2. max_k p^(k)(Y) ≥ p^(k*)(Y) for the true source k*
3. P(p^(k*)(Y) ≥ α) ≥ 1-α by conformal validity

## Optimality

Max-p aggregation is optimal when paired with properly chosen conformity scores. Specifically, using scores:

> s_k(x,y) = -Σ_ℓ λ*_ℓ(x) f_ℓ(y|x)

where λ*(x) are optimal dual weights, the resulting set achieves:
1. **Minimum size** among all uniformly valid sets
2. **Exact coverage** for at least one source (tightness)

## Efficiency Considerations

### Without Score Learning
Naive max-p (using standard per-source scores) can be inefficient:
- Fully nested sources: Acceptable (matches largest source)
- Partially overlapping: Set may be larger than necessary
- Disjoint sources: Very inefficient (union of disjoint regions)

### With Score Learning
[[concepts/multi-distribution-robust-cp|MDCP]] learns a shared score that:
- Finds overlapping regions satisfying all constraints
- Reduces to near-optimal size
- Maintains finite-sample validity

## Comparison with Other Aggregation Methods

| Method | Formula | Validity | Conservatism |
|--------|---------|----------|--------------|
| **Max-p** | max_k p^(k) | All sources | Minimal |
| Min-p | min_k p^(k) | None guaranteed | - |
| Average-p | mean_k p^(k) | Training mixture only | Variable |
| Bonferroni | K · max_k p^(k) | All sources | Over-conservative |

## Applications

1. **Multi-source learning**: Valid coverage regardless of test source
2. **Fairness**: Coverage guarantee for all demographic groups
3. **Federated conformal**: Aggregate predictions without sharing data
4. **Subpopulation robustness**: Protection against distribution shift

## Implementation Notes

- Compute per-source p-values using standard conformal procedures
- Take elementwise maximum for each candidate y
- Threshold at α to obtain prediction set
- For efficiency, learn shared conformity score via dual optimization

## See Also

- [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/worst-case-coverage|Worst-Case Coverage]]
- [[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin (2026)]]

<!-- AUTHORED REGION END -->
