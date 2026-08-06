---
title: Vapnik-Chervonenkis Dimension
page_id: concepts/vapnik-chervonenkis-dimension
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [quant-finance, statistical-learning-theory, machine-learning, overfitting, generalization]
sources: [sources/chen-2024-volume-price-product-factor]
related: [concepts/structural-risk, concepts/bias-variance-tradeoff, concepts/overfitting-in-alpha-research]
mind_map_priority: medium
---

# Vapnik-Chervonenkis Dimension

**Vapnik-Chervonenkis Dimension** is a measure of the capacity of a hypothesis space equal to the largest number of points it can shatter into all possible binary labelings; the paper argues the moving-average classifier has infinite VC dimension yet zero empirical error, bounding generalization error via statistical-learning theory.

## Overview

Chen and Yuan frame the moving-average model as a binary classifier that labels each closing price as above or below the line. Because such a line can separate points in arbitrarily many configurations, they claim the hypothesis space has infinite VC dimension while attaining zero empirical (classification) loss. This framing is used to argue, via statistical-learning theory, that the model generalizes well — a claim the authors treat as favorable, though large VC dimension conventionally signals overfitting risk rather than robustness.

## Sources

- [[sources/chen-2024-volume-price-product-factor]] — invokes VC dimension to justify the moving-average classifier's generalization behavior.

## Related Concepts

- [[concepts/structural-risk]]
- [[concepts/bias-variance-tradeoff]]
- [[concepts/overfitting-in-alpha-research]]
