---
title: A unified framework for bandit multiple testing
page_id: sources/xu-2021-bandit-multiple-testing
page_type: source
source_path: markdown_output/xu-2021-bandit-multiple-testing.md
source_type: conference-paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Ziyu Xu
- Ruodu Wang
- Aaditya Ramdas
year: 2021
venue: Advances in Neural Information Processing Systems (NeurIPS 2021)
tags:
- e-process
- multi-armed-bandits
- multiple-testing
- false-discovery-rate
- anytime-valid
sources: []
related:
- concepts/e-process
- concepts/anytime-valid-inference
- concepts/multiple-testing
- concepts/false-discovery-rate
- entities/ziyu-xu
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: 2bd7d411-5edc-55fb-8c7c-45c040107d18
content_hash: sha256:1376345906c6a55203464bb4617fdeca489c4dee6c183d8ee4354d9957161529
---

<!-- AUTHORED REGION START -->
# A Unified Framework for Bandit Multiple Testing

**Authors:** [[entities/ziyu-xu|Ziyu Xu]], [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2021 · **Venue:** NeurIPS 2021

## Summary

In bandit multiple testing each arm carries its own hypothesis, and an adaptive algorithm decides which arms to pull and when to stop. Both decisions depend on the data, which wrecks the dependence assumptions that p-value procedures need. Using [[concepts/e-process|e-processes]] instead makes the problem disappear.

## The framework

Each round splits into two components: an **exploration** rule choosing which arms to query, and an **evidence** component updating each arm's e-process from its new rewards. The candidate rejection set is whatever e-BH returns from the current e-values. At any stopping time you output the current set.

Because $E_\tau$ is a valid e-variable at every stopping time, and e-BH controls FDR for arbitrarily dependent e-values, the guarantee
\[
\sup_{\tau}\ \mathrm{FDR}(\mathcal{S}_\tau)\le \delta
\]
holds **with no correction at all**. It is agnostic to the exploration rule, the stopping rule, composite nulls, querying several arms at once, and even multiple cooperating or competing agents.

The p-value route needs a different correction in each setting: none for non-adaptive independent rewards, a factor $\log k$ under arbitrary dependence, a smaller but still real factor for adaptive sampling with independence.

## Results

With sub-Gaussian arms, UCB exploration and a discrete-mixture e-process, the sample complexity matches the best known p-value bound for this problem. Simulations use $\delta=0.05$ and three sparsity regimes. Under uniform sampling, e-BH with e-values outperforms BH with p-values, by a margin that narrows as the number of arms grows; under UCB sampling the two are comparable.

## Why It Matters

This is the cleanest demonstration of what e-values buy: not more power in a fixed design, but freedom from having to model how adaptivity and stopping distort the evidence. Any sequential screening problem where the sampling policy responds to results has the same shape.

## See Also

[[concepts/e-process|E-process]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/multiple-testing|Multiple Testing]] · [[concepts/false-discovery-rate|False Discovery Rate]]

Built directly on [[sources/wang-2021-fdr-control-evalues|e-BH]]; cited by [[sources/ignatiadis-2023-evalues-unnormalized-weights|Ignatiadis et al.]] as a source of e-value lists.
<!-- AUTHORED REGION END -->
