---
title: Confidence and discoveries with e-values
page_id: sources/vovk-2019-confidence-discoveries-evalues
page_type: source
source_path: markdown_output/vovk-2019-confidence-discoveries-evalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2019
venue: Statistical Science (2023)
tags:
- e-value
- e-process
- multiple-testing
- discovery-matrix
- confidence-regions
sources: []
related:
- concepts/e-value
- concepts/e-process
- concepts/multiple-testing
- concepts/false-discovery-rate
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: 084e7dc1-738b-5551-9631-b689c1470711
content_hash: sha256:3246998eba9ee783d5b5a5425573ee46ec06d01d3af41e187d0ce69f379f0af4
---

<!-- AUTHORED REGION START -->
# Confidence and Discoveries with E-values

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** preprint 2019 · **Venue:** Statistical Science (2023)

## Summary

Two things at once: e-value analogues of confidence regions, and a way of reporting multiple-testing results that is stronger than controlling the false discovery rate. Instead of an expectation of the false discovery proportion, you get **lower confidence bounds on the number of true discoveries** in any rejection set, valid under arbitrary dependence.

## E-processes

The paper gives the definition this cluster uses throughout: an **e-process** is a sequence $(E_t)$ such that $E_\tau$ is an e-variable for *every* stopping time $\tau$ with respect to a pre-specified filtration. That single property is what licenses continuous monitoring.

## Discovery matrices

For a rejection set $R$, the **discovery e-vector** reports, for each $j$, the merged e-value of the least favourable configuration in which $R$ contains exactly $j$ true discoveries. Computing it over all rejection sets of each size gives the **discovery e-matrix**, whose entry $D_{r,j}$ answers: how much evidence is there that the top $r$ hypotheses contain more than $j$ true discoveries?

Because the merging step is an arithmetic mean, the whole construction is valid under arbitrary dependence of the base e-values. Complexity is $O(K^4)$ for the full matrix in general, reduced to $O(K^3)$, and a single row in $O(K)$.

## Numbers

Reading e-values against p-values: an e-value of 20 corresponds to a p-value of 5%, and Jeffreys's equivalences put $p=5\%$ at $e=10^{1/2}$ and $p=1\%$ at $e=10$. A round trip through the calibrators costs: a p-value of 0.5% comes back as 7.2%.

In a simulation with 100 false and 100 true nulls, the lower confidence bounds on true discoveries in the top 50 hypotheses are 40 at the "strong" level ($e>10$) and 46 at "substantial" ($e>10^{1/2}$). Read as false discovery proportions, the top 31 contain at most 3 false discoveries, about 9.7%.

On the BRCA gene expression data, Benjamini–Hochberg rejects 88 nulls at $q=0.05$ and 1 at $q=0.01$, while Benjamini–Yekutieli rejects 1 even at 0.05 — the gap that motivates dependence-free methods.

## Why It Matters

FDR is an average over repetitions. A confidence bound on the number of true discoveries is a statement about the data in front of you, which is usually what you actually want when deciding how many of a screen's hits to follow up.

## See Also

[[concepts/e-value|E-value]] · [[concepts/e-process|E-process]] · [[concepts/multiple-testing|Multiple Testing]] · [[concepts/false-discovery-rate|False Discovery Rate]]

Uses the arithmetic-mean merging result of [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]] and sits alongside [[sources/wang-2021-fdr-control-evalues|e-BH]] as the stronger, non-FDR way of reporting discoveries. [[sources/vovk-2024-true-false-discoveries-evalues|Vovk & Wang (2024)]] sharpens the matrices for independent and sequential e-values.
<!-- AUTHORED REGION END -->
