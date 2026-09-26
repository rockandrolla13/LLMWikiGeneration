---
title: Admissible ways of merging p-values under arbitrary dependence
page_id: sources/vovk-2021-admissible-merging-pvalues
page_type: source
source_path: markdown_output/vovk-2021-admissible-merging-pvalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Bin Wang
- Ruodu Wang
year: 2021
venue: Annals of Statistics (2022)
tags:
- p-value-merging
- admissibility
- arbitrary-dependence
- harmonic-mean
- simes
sources: []
related:
- concepts/p-value-merging
- concepts/e-value
- concepts/multiple-testing
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: high
schema_version: 2
uuid: 553149ea-20b1-563a-9176-3481a2402375
content_hash: sha256:0b6b6262b2e3fd5b1e777f2a21aa60148ddc4b818939565337c58bd597fe5bd4
---

<!-- AUTHORED REGION START -->
# Admissible Ways of Merging P-values Under Arbitrary Dependence

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], Bin Wang, [[entities/ruodu-wang|Ruodu Wang]]

**Year:** preprint 2021 · **Venue:** Annals of Statistics (2022)

## Summary

Which rules for combining $K$ p-values into one valid p-value cannot be improved on, when nothing is assumed about how the inputs depend on each other? This is the p-value counterpart to the e-value merging theory, and the answer is far messier — which is itself the argument for e-values.

## Results

**The floor.** The Simes function $S_K(\mathbf{p})=\min_k (K/k)\,p_{(k)}$ is the minimum of all symmetric p-merging functions: nothing valid can be uniformly smaller. Simes itself is not valid under arbitrary dependence, so the floor is not attainable.

**The characterisation.** Every admissible homogeneous merging function arises from calibrators: $F(\mathbf{p})\le\varepsilon$ exactly when $\sum_k \lambda_k f_k(p_k/\varepsilon)\ge 1$, with weights on the simplex and each $f_k$ an admissible p-to-e calibrator. If the function is also symmetric, one calibrator and equal weights suffice. So p-merging is governed by e-value machinery underneath.

**The grid harmonic.** A specific calibrator yields the grid harmonic function $H^*_K$, which strictly dominates Hommel's classical $H_K=\ell_K\min_k (K/k)p_{(k)}$ for all $K\ge 4$, where $\ell_K=\sum_{k\le K}1/k$. It is always admissible among symmetric functions, and admissible outright when $K$ is not prime. For $K=2$ it is beaten by an asymmetric rule, which shows symmetry is a real restriction.

**The M-family.** Generalised means of order $r$ require multiplicative constants to be valid: $b_{r,K}=((r+1)\wedge K)^{1/r}$ for $r\ge 1/(K-1)$, with $b_{-\infty,K}=K$ (Bonferroni) and $b_{\infty,K}=1$. Each member is strictly dominated by a refinement, admissible except at $r=1$.

## Why It Matters

Compare with e-values. Merging e-values under arbitrary dependence needs no constant at all and has a single admissible answer, a weighted average. Merging p-values needs constants that are often only available numerically, and the admissible class is a zoo indexed by calibrators. If you are combining evidence across tests whose dependence you cannot model, that asymmetry is the practical case for converting to e-values first.

## See Also

[[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/e-value|E-value]] · [[concepts/multiple-testing|Multiple Testing]]

The duality result is the base for [[sources/gasparin-2025-combining-exchangeable-pvalues|Gasparin et al. (2025)]]; [[sources/wang-2023-p-star-values|Wang (2024)]] uses its geometric-mean result and the uniqueness of the e-to-p calibrator.
<!-- AUTHORED REGION END -->
