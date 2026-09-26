---
title: False discovery rate control with e-values
page_id: sources/wang-2021-fdr-control-evalues
page_type: source
source_path: markdown_output/wang-2021-fdr-control-evalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Ruodu Wang
- Aaditya Ramdas
year: 2021
venue: Journal of the Royal Statistical Society Series B (2022)
tags:
- e-value
- false-discovery-rate
- multiple-testing
- e-bh
- arbitrary-dependence
sources: []
related:
- concepts/e-value
- concepts/false-discovery-rate
- concepts/multiple-testing
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: high
schema_version: 2
uuid: 7c788431-7f06-585e-9f9e-b382f834084e
content_hash: sha256:d6ee7492b1ca771b1ec6758cbbc4e4b5b91a093b529c1daacb27d3c57d924199
---

<!-- AUTHORED REGION START -->
# False Discovery Rate Control with E-values

**Authors:** [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** preprint 2021 · **Venue:** JRSS-B (2022)

## Summary

This paper introduces **e-BH**, the e-value counterpart of Benjamini–Hochberg, and proves it controls the false discovery rate under *arbitrary dependence* with no correction. That is the result the rest of the multiple-testing cluster is built on.

The contrast with p-values is stark. BH needs a positive-dependence condition; without it you must pay the Benjamini–Yekutieli factor $\ell_K=\sum_{k=1}^{K}1/k\approx\log K$, which is known to be unimprovable in general. e-BH pays nothing.

## The procedure

Let $e_{[k]}$ be the $k$-th largest of $e_1,\dots,e_K$. The base e-BH procedure rejects the $k^*_e$ largest e-values, where
\[
k^*_e=\max\Bigl\{k : \frac{k\,e_{[k]}}{K}\ge \frac{1}{\alpha}\Bigr\},
\]
with $\max\emptyset=0$.

**Theorem 2:** the false discovery rate is at most $K_0\alpha/K$, where $K_0$ is the number of true nulls, under arbitrary dependence.

The proof goes through a more general property. Any **self-consistent** procedure — one where every rejected $e_k$ satisfies $e_k\ge K/(\alpha R)$ with $R$ the number of rejections — controls FDR at $\alpha K_0/K$ for arbitrary dependence. Theorem 5 adds an optimality statement: among increasing rules that control FDR for arbitrary e-value configurations, e-BH is the largest.

## Boosting

Because e-BH gives nothing away to dependence, it can *gain* when dependence assumptions do hold. The full procedure multiplies each e-value by a boosting factor $b_k\ge 1$ before applying the rule. The paper reports that "a boosting factor between 1.3 and 10 is common in stylized settings", with worked values: $b\approx 6.32$ at $\alpha=0.05$ for a square-root calibrator, $b\approx 8.94$ under positive dependence, and $b\approx 1.37$ and $1.11$ for log-normal e-values with $\delta=3$ and $\delta=4$.

This is the exact opposite trade to BH, where assumptions buy validity rather than power.

## Robustness and variants

The FDR bound degrades linearly in the error of the e-values: if $\mathbb{E}[E_i]\le 1+\varepsilon_i$ the bound becomes $(\alpha/K)(K_0+\sum\varepsilon_i)$. Structured, post-selection, grouped and focused variants all inherit validity with no assumptions on dependence, structure or filtering. Proposition 4 recovers BH and BY themselves as special cases of e-BH via calibration.

## Empirical study

A cryptocurrency screening exercise: 496 coins listed in January 2015, of which 126 survived to June 2021. Under a 50% rebalancing strategy at the 5% level, e-BH selects 42 coins against 15 for BY; at 10%, 60 against 25. e-BH beats BY in almost every configuration tested.

## Why It Matters

For anyone screening a large number of candidate signals, the dependence structure across tests is usually unknown and certainly not positive-orthant. This is the procedure that survives that, and the reason the e-value machinery is worth the conversion cost.

## See Also

[[concepts/e-value|E-value]] · [[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/multiple-testing|Multiple Testing]]

Built on [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]]. Extended by [[sources/ignatiadis-2023-evalues-unnormalized-weights|Ignatiadis et al. (2023)]] to weighted testing, by [[sources/ignatiadis-2024-asymptotic-compound-evalues|compound e-values]], and used as the engine in [[sources/xu-2021-bandit-multiple-testing|bandit multiple testing]].
<!-- AUTHORED REGION END -->
