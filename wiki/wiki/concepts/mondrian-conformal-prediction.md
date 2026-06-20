---
title: Mondrian Conformal Prediction
page_id: concepts/mondrian-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-24 16:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- conditional-validity
- taxonomy
- mondrian
sources:
- sources/vovk-2005-algorithmic-learning
- sources/shafer-2007-cp-tutorial
- sources/fontana-2023-cp-unified-review
related:
- concepts/conformal-prediction
- concepts/conditional-validity
- concepts/conditional-coverage
- concepts/group-balanced-conformal-prediction
- concepts/class-conditional-conformal-prediction
- concepts/mask-conditional-validity
mind_map_priority: medium
schema_version: 2
uuid: 6a6d0530-45a3-5eb5-9b6d-a50317d2a50b
content_hash: sha256:1c15f3ae9f43653b4d47643c4c6249d2c28be1dc86798ad0cc698b56ac20ac0f
---

<!-- AUTHORED REGION START -->
# Mondrian Conformal Prediction

**Mondrian conformal prediction** (Vovk, Lindsay, Nouretdinov, Gammerman, 2003) is a category-conditional variant of [[concepts/conformal-prediction|CP]] that partitions the data via a user-chosen taxonomy and applies the conformal recipe within each cell. Each cell has its own [[concepts/nonconformity-score|nonconformity quantile]], so the coverage guarantee holds *conditional on cell membership* rather than just marginally.

## The Construction

Given a taxonomy function `K(x, y)` mapping each labelled point to a discrete category:

1. Partition the calibration scores by category: `{s_i : K(x_i, y_i) = k}` for each `k`.
2. For each category `k`, compute the per-category empirical quantile `q̂_k`.
3. At test time, given `(x, y)` candidate, look up `K(x, y) = k` and check whether `s(x, y) ≤ q̂_k`.

Guarantee: `P(Y_test ∈ Ĉ(X_test) | K(X_test, Y_test) = k) ≥ 1 − α` for every category `k`.

## Special Cases

- **[[concepts/group-balanced-conformal-prediction|Group-balanced CP]].** Taxonomy = an observed discrete feature (e.g., demographic group).
- **[[concepts/class-conditional-conformal-prediction|Class-conditional CP]].** Taxonomy = the ground-truth class label.
- **Exchangeability-within-label model.** [[sources/shafer-2007-cp-tutorial|Shafer & Vovk (2007)]]'s name for class-conditional CP; the on-line compression model interpretation.
- **[[concepts/mask-conditional-validity|Mask-conditional validity]].** Taxonomy = the missing-data pattern (Zaffran et al.).

## The "Problem of the Reference Class"

The classical trade-off: categories large enough for stable per-cell sample sizes (low-variance `q̂_k`) versus small enough for informative conditioning (cells matching the practical question of interest). [[sources/fontana-2023-cp-unified-review|Fontana et al. (2023)]] flag this as still lacking a principled solution.

## Why It Matters

[[concepts/conditional-coverage|Distribution-free conditional coverage]] is provably impossible at the level of individual `x`. Mondrian CP is the canonical *partial* answer: pick a coarse enough partition to support estimation, and you get conditional validity at that coarseness. Most fairness audits, class-imbalanced classification, and missing-data CP variants are Mondrian instantiations under different names.

## Sources

- [[sources/vovk-2005-algorithmic-learning]] — original treatment (Ch. 4).
- [[sources/shafer-2007-cp-tutorial]] — on-line / compression-model framing.
- [[sources/fontana-2023-cp-unified-review]] — modern theoretical treatment.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/conditional-coverage]]
- [[concepts/group-balanced-conformal-prediction]]
- [[concepts/class-conditional-conformal-prediction]]
- [[concepts/mask-conditional-validity]]

<!-- AUTHORED REGION END -->
