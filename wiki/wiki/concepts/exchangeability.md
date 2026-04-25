---
title: Exchangeability
page_id: concepts/exchangeability
page_type: concept
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [probability-theory, statistical-assumption, conformal-prediction]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/adaptive-conformal-inference]
mind_map_priority: medium
---

# Exchangeability

**Exchangeability** is a probabilistic assumption that the joint distribution of a sequence of random variables is invariant to permutation. It is the key assumption underlying [[concepts/conformal-prediction|conformal prediction]].

## Formal Definition

Random variables (Z₁, Z₂, ..., Zₙ) are **exchangeable** if for any permutation π:

P(Z₁, Z₂, ..., Zₙ) = P(Z_π(1), Z_π(2), ..., Z_π(n))

In other words, the order of the observations carries no information about their distribution.

## Relationship to i.i.d.

- **i.i.d. ⟹ exchangeable**: Independent and identically distributed data is always exchangeable
- **exchangeable ⟹̸ i.i.d.**: Exchangeable data need not be independent (e.g., sampling without replacement)

Exchangeability is a **weaker assumption** than i.i.d., making conformal prediction more broadly applicable.

## Why It Matters for Conformal Prediction

The validity of conformal prediction relies on exchangeability:
- Under exchangeability, the conformity score of the test point is uniformly distributed among all scores
- This uniform ranking property yields the finite-sample coverage guarantee

## When Exchangeability Fails

Exchangeability does not hold for:
- **Time series**: Temporal ordering matters
- **Distribution shift**: Test data differs from training
- **Spatial data**: Location matters

This motivates extensions like [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]].

## De Finetti's Theorem

Infinitely exchangeable sequences can be represented as mixtures of i.i.d. sequences:
- There exists a random distribution Θ such that, conditional on Θ, the Zᵢ are i.i.d.
- This provides a Bayesian interpretation of exchangeability

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
