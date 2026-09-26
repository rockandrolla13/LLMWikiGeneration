---
title: 'Asymptotic and compound e-values: multiple testing and empirical Bayes'
page_id: sources/ignatiadis-2024-asymptotic-compound-evalues
page_type: source
source_path: markdown_output/ignatiadis-2024-asymptotic-compound-evalues.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Nikolaos Ignatiadis
- Ruodu Wang
- Aaditya Ramdas
year: 2024
venue: Working paper, arXiv:2409.19812 (version dated July 2025)
tags:
- compound-e-value
- e-value
- empirical-bayes
- false-discovery-rate
- multiple-testing
sources: []
related:
- concepts/e-value
- concepts/false-discovery-rate
- concepts/multiple-testing
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: high
schema_version: 2
uuid: 1d916fb3-faa2-5f17-a079-1fe9d9e0cabf
content_hash: sha256:d9b4bb229294dbd7b53f5dfcd86cfeb38d6702acb56b777a0feaddae0d40dc0c
---

<!-- AUTHORED REGION START -->
# Asymptotic and Compound E-values

**Authors:** Nikolaos Ignatiadis, [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2024 · **Venue:** Working paper, arXiv:2409.19812

## Summary

Several papers had been quietly using objects that were not quite e-values — statistics whose expectations are bounded only *on average* across hypotheses. This paper names them **compound e-values**, shows they are the natural currency of multiple testing, and proves a striking universality result.

## Definitions

A family $E_1,\dots,E_K$ are **compound e-variables** if
\[
\sum_{k} \mathbb{E}[E_k] \le K,
\]
rather than each having expectation at most 1. Approximate and asymptotic versions relax this to $K(1+\varepsilon)$ on an event of probability at least $1-\delta$, with $\varepsilon,\delta\to0$ along a triangular array.

## Results

**e-BH still works.** Applied to compound e-values, e-BH controls FDR at $\alpha$ under arbitrary dependence; with the approximate version the bound becomes $\alpha(1+\varepsilon)+\delta$; with the asymptotic version, asymptotic control.

**Universality.** Any procedure that controls FDR at a known level can be reproduced exactly by running e-BH on some compound e-values, and for admissible procedures those e-values can be taken tight. In other words compound e-values are not one method among many — they are a normal form for FDR control.

**Optimal construction.** Maximising expected log-value subject to the compound constraint gives the ratio of mixture likelihoods under alternative and null, which is exactly the statistic of Storey's optimal discovery procedure. Two feasible constructions follow: compound universal inference, which profiles nuisance parameters over a localised empirical distribution, and an empirical-Bayes version that estimates the mixing distribution by nonparametric maximum likelihood. The latter is the first data-driven optimal discovery procedure with a theoretical guarantee.

## Numbers

Simultaneous normal t-tests with $K=2000$, $n\in\{5,10\}$, 1,800 nulls and 200 alternatives, $\alpha=0.1$, 200 replications. The empirical-Bayes construction "has by far the largest power" among data-driven methods and is indistinguishable from its oracle counterpart. Compound universal inference is weaker than the empirical-Bayes version but stronger than plain universal inference.

## Why It Matters

If you are designing a screening procedure, this says you may as well think in compound e-values: whatever valid procedure you invent is one anyway, and the framework tells you which construction is optimal.

## See Also

[[concepts/e-value|E-value]] · [[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/multiple-testing|Multiple Testing]]

Formalises what was implicit in [[sources/wang-2021-fdr-control-evalues|e-BH]]; supplies the weights for [[sources/ignatiadis-2023-evalues-unnormalized-weights|ep-BH]]; its approximation framework is used throughout [[sources/ignatiadis-2026-compound-adaptive-bh|the adaptive-BH paper]].
<!-- AUTHORED REGION END -->
