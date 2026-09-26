---
title: False Discovery Rate
page_id: concepts/false-discovery-rate
page_type: concept
concept_type: definition
abstraction_level: intermediate
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- false-discovery-rate
- multiple-testing
- benjamini-hochberg
- e-bh
sources:
- sources/wang-2021-fdr-control-evalues
- sources/ignatiadis-2024-asymptotic-compound-evalues
- sources/chi-2024-multiple-testing-negative-dependence
- sources/xu-2024-post-selection-evalue-ci
related:
- concepts/multiple-testing
- concepts/e-value
- concepts/p-value-merging
mind_map_priority: high
schema_version: 2
uuid: 41d2d3da-59e5-5d23-9d6e-05dd486b0d16
content_hash: sha256:db07755c5b733402e398c8a5c86b1f084072f37a8da094670091a552f80bd749
---

<!-- AUTHORED REGION START -->
# False Discovery Rate

## Definition

The **false discovery rate** is the expected proportion of rejected hypotheses that are true nulls. Controlling it at $\alpha$ means that, on average over repetitions, at most $\alpha$ of your discoveries are spurious. It is the standard target when screening many candidates, because controlling the family-wise error rate is too strict to leave any power.

## The dependence problem

Benjamini–Hochberg controls FDR under independence and under positive regression dependence. Outside those conditions you must fall back on Benjamini–Yekutieli, which inflates by
\[
\ell_K=\sum_{k=1}^{K}\frac{1}{k}\approx\log K,
\]
a factor known to be unimprovable in general and large enough that practitioners routinely refuse to pay it.

Three results in this wiki attack that problem from different sides:

- **[[sources/wang-2021-fdr-control-evalues|e-BH]]** controls FDR under *arbitrary* dependence with no correction at all, provided the inputs are [[concepts/e-value|e-values]] rather than p-values. It can even gain power through boosting when dependence assumptions do hold.
- **[[sources/chi-2024-multiple-testing-negative-dependence|Chi, Ramdas & Wang (2024)]]** handle negative dependence, where BH is anti-conservative, with a correction bounded independently of the number of hypotheses.
- **[[sources/ignatiadis-2024-asymptotic-compound-evalues|Compound e-values]]** turn out to be a normal form: any procedure controlling FDR at a known level can be reproduced as e-BH run on some compound e-values.

## Beyond an average

FDR is an expectation, so it says nothing about the realised proportion in the data at hand. [[sources/vovk-2019-confidence-discoveries-evalues|Discovery matrices]] give the stronger object — lower confidence bounds on the *number* of true discoveries — and [[sources/xu-2024-post-selection-evalue-ci|the false coverage rate]] is the analogous target when you report intervals rather than rejections.

## Adaptive variants

Estimating the null proportion $\pi_0$ and running BH at $\alpha/\hat\pi_0$ is standard. [[sources/ignatiadis-2026-compound-adaptive-bh|Ignatiadis, Wang & Ramdas (2026)]] show most such estimators are compound e-values in disguise, which makes most adaptive procedures instances of ep-BH — and gives a mechanical way to improve them.

## Sources

- [[sources/wang-2021-fdr-control-evalues|Wang & Ramdas (2022)]] — e-BH.
- [[sources/ignatiadis-2023-evalues-unnormalized-weights|Ignatiadis et al. (2024)]] — e-values as unnormalized weights.
- [[sources/chi-2024-multiple-testing-negative-dependence|Chi, Ramdas & Wang (2024)]] — negative dependence.

## Related Concepts

[[concepts/multiple-testing|Multiple Testing]] · [[concepts/e-value|E-value]] · [[concepts/p-value-merging|Merging P-values and E-values]]
<!-- AUTHORED REGION END -->
