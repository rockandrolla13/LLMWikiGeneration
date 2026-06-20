---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/random-forest-proximity
page_type: concept
related:
- concepts/decision-trees
- concepts/factor-models
- concepts/nelson-siegel-model
revision_id: 2
sources:
- sources/technical-2025-bond-similarity
tags:
- machine-learning
- random-forests
- similarity-measures
- ensemble-methods
title: Random Forest Proximity
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 63bcc2c2-17e4-5928-9284-2ce57d5c7900
content_hash: sha256:421e4836e632d1628ec7afcacd1b5788e7d99af682322160820b1e25f55eaa74
---

<!-- AUTHORED REGION START -->
# Random Forest Proximity

Random forest proximity is a similarity measure derived from ensemble tree methods, capturing how often two observations land in the same leaf node across trees.

## Definition

For observations $i$ and $j$ across $T$ trees:

$$\text{Proximity}(i, j) = \frac{1}{T} \sum_{t=1}^{T} \mathbf{1}[\text{leaf}_t(i) = \text{leaf}_t(j)]$$

Ranges from 0 (never in same leaf) to 1 (always in same leaf).

## Properties

- **Non-parametric**: Captures complex, non-linear relationships
- **Feature-agnostic**: Works with mixed data types
- **Robust**: Ensemble averaging reduces noise
- **Interpretable**: Based on decision tree logic

## Computation

1. Train random forest on dataset
2. For each pair of observations:
   - Run both through all trees
   - Count proportion of times they share a leaf
3. Results in n × n proximity matrix

## Applications

### Clustering and Visualization
- Proximity → distance → MDS/t-SNE visualization
- Outlier detection via low average proximity

### Missing Value Imputation
- Weight observed values by proximity to missing case

### Bond Similarity (Technical Paper, 2025)
- Identify similar bonds for relative value
- Feature space: duration, spread, rating, sector
- Proximity captures non-linear similarity structure

## Comparison to Other Similarity Measures

| Measure | Strengths | Weaknesses |
|---------|-----------|------------|
| Euclidean | Simple, fast | Assumes linear scaling |
| Cosine | Angle-based | Ignores magnitude |
| RF Proximity | Non-parametric, handles mixed types | Requires training |
| Mahalanobis | Accounts for correlation | Assumes Gaussian |

## See Also

- [[concepts/nelson-siegel-model|Nelson-Siegel Model]]
- [[concepts/factor-models|Factor Models]]
- [[sources/technical-2025-bond-similarity|Bond Similarity Framework (2025)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/decision-trees|decision-trees]]
<!-- AUTHORED REGION END -->
