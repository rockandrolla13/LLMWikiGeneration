---
title: Multiple testing under negative dependence
page_id: sources/chi-2024-multiple-testing-negative-dependence
page_type: source
source_path: markdown_output/chi-2024-multiple-testing-negative-dependence.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Ziyu Chi
- Aaditya Ramdas
- Ruodu Wang
year: 2024
venue: Bernoulli (2024)
tags:
- negative-dependence
- multiple-testing
- false-discovery-rate
- simes
- benjamini-hochberg
sources: []
related:
- concepts/multiple-testing
- concepts/false-discovery-rate
- concepts/e-value
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: 7ff24919-4e81-5bc8-a2b5-a1d721d2e3b0
content_hash: sha256:c85e2be3dbc753bb3358b579f8f432ec2308e6d7b5977a2d1e801b8996a3d74d
---

<!-- AUTHORED REGION START -->
# Multiple Testing Under Negative Dependence

**Authors:** Ziyu Chi, [[entities/aaditya-ramdas|Aaditya Ramdas]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2024 · **Venue:** Bernoulli

## Summary

Multiple testing theory covers independence, positive dependence and arbitrary dependence. **Negative** dependence had nothing, even though it arises naturally — sampling without replacement, allocation of a fixed budget, tournament scores — and even though Simes and BH are known empirically to be anti-conservative there. The Benjamini–Yekutieli fix costs a factor of about $\log K$, which practitioners refuse to pay.

This paper supplies the missing theory, with corrections that do not grow with $K$.

## Results

**Simes.** For weakly negatively dependent p-values, $(3.4\wedge\ell_K)\,S_K(\mathbf{P})$ is a valid p-value for any $K$ — the inflation factor is bounded independently of the number of hypotheses. The correction is mild in the range that matters: the ratio is at most 1.26 for $\alpha\le 0.1$, and at most 3.4 for any $\alpha$. For $K=2$ the exact bound is $\alpha+\alpha^2$, which is 0.0525 at $\alpha=0.05$.

**Benjamini–Hochberg.** If the *null* p-values are weakly negatively dependent — with arbitrary dependence allowed between nulls and non-nulls — BH at level $\alpha$ controls FDR at
\[
\alpha\bigl((-\log\alpha+3.18)\wedge \ell_K\bigr),
\]
and the bound is asymptotically tight. At $\alpha=0.05$ this is 0.3087.

**E-values.** Under negative upper orthant dependence the **product** of e-values is itself an e-value, as is the betting form $\prod_k(1-\lambda_k+\lambda_k E_k)$, along with convex combinations and U-statistics. That is the same multiplicative gain normally reserved for independence.

## Numbers

Global-null simulations use $K=100$ with pairwise correlation uniform on $[-1/(K-1),0]$, 10,000 repetitions; FDR simulations use $K=10{,}000$ and $K=100{,}000$ with $\pi_0=80\%$ and a target of 0.1. The product e-value is strong when all nulls are false but degrades as the null proportion rises; Simes with the negative-dependence correction "performs very well in all cases"; BH with the correction beats both BH with the $\ell_K$ correction and e-BH.

## Why It Matters

Negative dependence is the case most likely to arise when tests share a fixed resource — a budget, a portfolio weight, a normalisation. Before this, the only safe option was the $\log K$ penalty. Now there is a constant.

## See Also

[[concepts/multiple-testing|Multiple Testing]] · [[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/e-value|E-value]]

Uses [[sources/wang-2021-fdr-control-evalues|e-BH]] as the arbitrary-dependence comparator.
<!-- AUTHORED REGION END -->
