---
title: True and false discoveries with independent and sequential e-values
page_id: sources/vovk-2024-true-false-discoveries-evalues
page_type: source
source_path: markdown_output/vovk-2024-true-false-discoveries-evalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2024
venue: Canadian Journal of Statistics (2024)
tags:
- e-value
- discovery-matrix
- multiple-testing
- u-statistics
sources: []
related:
- concepts/e-value
- concepts/multiple-testing
- concepts/false-discovery-rate
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: 9e357e44-f564-5365-8566-6b2e6ea5f8bf
content_hash: sha256:5f204b53e949db540d726425b8382461335b77a7368b010abb5e26216ea13109
---

<!-- AUTHORED REGION START -->
# True and False Discoveries with Independent and Sequential E-values

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2024 · **Venue:** Canadian Journal of Statistics

## Summary

The discovery-matrix machinery of [[sources/vovk-2019-confidence-discoveries-evalues|Vovk & Wang (2023)]] was built for arbitrarily dependent e-values, where averaging is all you can do. When the e-values are independent or sequential you can multiply, and this paper shows how much that buys: substantially tighter confidence bounds on the number of true discoveries.

## Construction

The merging functions are U-statistics: the average of all products of $n$ distinct e-values,
\[
U_n(e_1,\dots,e_K)=\binom{K}{n}^{-1}\sum_{\{k_1,\dots,k_n\}} e_{k_1}\cdots e_{k_n},
\]
with $U_1$ the arithmetic mean (valid under arbitrary dependence) and $U_2$ the paper's workhorse. These remain valid for sequential e-values, not only independent ones.

A convenient identity makes the comparison concrete: $U_2$ beats $U_1$ exactly when the relative variance of the e-values is below $1-1/U_1$ — so with a mean e-value of 10, any relative variance under 0.9 favours multiplying.

## Results

The $U_2$ matrices are far tighter than the arbitrary-dependence $U_1$ matrices, and they beat the p-value procedure even after the crude calibration $p=\min(1/e,1)$. The reason is structural: combining independent e-values lets evidence multiply, while Simes-type procedures never return anything smaller than the smallest input p-value.

Computation costs $O(K^2)$ for one row of the $U_2$ matrix and $O(K^3)$ overall.

## Numbers

In a simulation with $K=200$ and half the observations drawn from a shifted normal, and on the `prostate` dataset (6,033 genes, 50 controls and 52 patients, with permutation e-values from 10,000 permutations), the measured relative variances are about 0.24 for likelihood-ratio e-values and about 0.035 for the Monte Carlo e-values — far below the threshold, so $U_2$ dominates comfortably.

## Why It Matters

It identifies the condition under which multiplying beats averaging, in a form you can check on your own e-values before choosing a merging rule.

## See Also

[[concepts/e-value|E-value]] · [[concepts/multiple-testing|Multiple Testing]] · [[concepts/false-discovery-rate|False Discovery Rate]]

Sharpens [[sources/vovk-2019-confidence-discoveries-evalues|Vovk & Wang (2023)]] and cites [[sources/vovk-2024-merging-sequential-evalues|Merging sequential e-values via martingales]] for the structure of sequential merging.
<!-- AUTHORED REGION END -->
