---
title: Tiny but uniform improvements of adaptive BH procedures via compound e-values
page_id: sources/ignatiadis-2026-compound-adaptive-bh
page_type: source
source_path: markdown_output/ignatiadis-2026-compound-adaptive-bh.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Nikolaos Ignatiadis
- Ruodu Wang
- Aaditya Ramdas
year: 2026
venue: Working paper, arXiv:2603.21424 (March 2026)
tags:
- compound-e-value
- adaptive-bh
- null-proportion
- false-discovery-rate
- multiple-testing
sources: []
related:
- concepts/e-value
- concepts/false-discovery-rate
- concepts/multiple-testing
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: 6f3c58fd-f2cc-59db-8797-be1fe1cedd4d
content_hash: sha256:52de49a4ee0bcc346fa68e5259b30ecd377cc1be4a7fe68ee31040b02c37b2ff
---

<!-- AUTHORED REGION START -->
# Tiny but Uniform Improvements of Adaptive BH Procedures

**Authors:** Nikolaos Ignatiadis, [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2026 · **Venue:** Working paper, arXiv:2603.21424

## Summary

Dozens of papers boost Benjamini–Hochberg by estimating the unknown proportion of true nulls, $\pi_0$, and running BH at level $\alpha/\hat\pi_0$. This paper makes an observation that reorganises that whole literature: **most $\pi_0$ estimators are compound e-values in disguise**, so most adaptive procedures are instances of ep-BH — and most are therefore inadmissible.

## The fix

The classical recipe implicitly sets $E_k=1/\hat\pi_0(\mathbf{P})$, the same value for every hypothesis. The improvement replaces it with a **leave-one-out** version,
\[
E_k=\frac{1}{\hat\pi_0(\mathbf{P}_{k\to 0})},
\]
the estimator recomputed with the $k$-th p-value set to zero, then runs ep-BH at level $\alpha$. Because setting a p-value to zero can only lower the estimated null proportion, the new e-value is at least as large, so the improved procedure rejects at least as much as the original. Always.

A second case: when two $\pi_0$ estimators are available, the literature averages the estimators. Averaging the implied compound **e-values** instead is strictly better, because averaging estimators amounts to a harmonic average of the e-values.

## Guarantees

FDR stays at $\alpha$ throughout. The conditions are of two kinds: positively dependent p-values with compound e-values independent of them, allowing arbitrary dependence among the e-values; or p-independence with each e-value coordinatewise non-increasing and dominated by a leave-one-out version. An alternative route via censored p-values avoids the global monotonicity requirement.

## Numbers

$K=200$, $n\in\{2,5,20\}$, between 2 and 100 alternatives, $\alpha=0.1$, 10,000 Monte Carlo replications. All methods hold FDR at the nominal level. The authors are candid that "the improvements are small in practice" and "would be very small" — the point is that they are free, requiring no extra assumptions. Code accompanies the paper.

## Why It Matters

The reframing is more valuable than the power gain. Once you see adaptive BH as ep-BH with a particular compound e-value, the question "is my procedure admissible?" becomes checkable, and the leave-one-out construction is the mechanical answer.

## See Also

[[concepts/e-value|E-value]] · [[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/multiple-testing|Multiple Testing]]

Uses ep-BH from [[sources/ignatiadis-2023-evalues-unnormalized-weights|Ignatiadis et al. (2024)]] and the approximation framework of [[sources/ignatiadis-2024-asymptotic-compound-evalues|the compound e-value paper]], and routes FDR control through [[sources/wang-2021-fdr-control-evalues|e-BH]].
<!-- AUTHORED REGION END -->
