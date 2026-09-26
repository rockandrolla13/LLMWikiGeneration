---
title: Improved thresholds for e-values
page_id: sources/blier-wong-2024-improved-thresholds
page_type: source
source_path: markdown_output/blier-wong-2024-improved-thresholds.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Christopher Blier-Wong
- Ruodu Wang
year: 2024
venue: Accepted, Annals of Statistics (2026)
tags:
- e-value
- thresholds
- markov-inequality
- comonotonicity
- false-discovery-rate
sources: []
related:
- concepts/e-value
- concepts/false-discovery-rate
- entities/ruodu-wang
mind_map_priority: high
schema_version: 2
uuid: 4e6dad9a-e104-54bb-99d1-1754c6154210
content_hash: sha256:6ef34c203ce2e63b31a4deed84ac85756897f03043308e8f67715453e4103aa5
---

<!-- AUTHORED REGION START -->
# Improved Thresholds for E-values

**Authors:** Christopher Blier-Wong, [[entities/ruodu-wang|Ruodu Wang]]

**Year:** preprint 2024 · **Venue:** accepted, Annals of Statistics (2026)

## Summary

Rejecting when an e-value exceeds $1/\alpha$ is valid but wasteful, because Markov's inequality is loose. This paper shows how much the threshold can be lowered using cheap distributional facts about the null e-variable that you can check by eye from a histogram — no model required.

The practical answer: a decreasing density halves the threshold, and a decreasing or symmetric *log*-density improves it by roughly a factor of $e$.

## Results

Write $R_\gamma(\mathcal{E})=\sup_{E\in\mathcal{E}}\mathbb{P}(E\ge 1/\gamma)$ for the worst-case type-I error over a class $\mathcal{E}$, and $T_\alpha(\mathcal{E})$ for the smallest valid threshold. Markov gives $R_\gamma=\gamma$ for all e-variables.

**Density shape.** For a decreasing density, $R_\gamma=\gamma/2$; for a unimodal one, $(\gamma/2)\vee(2\gamma-1)$; for a decreasing density supported on $[1,\infty)$, $\gamma/(1+\sqrt{1-\gamma^2})$.

**Log-transformed.** Symmetric $\log E$ gives $\gamma\wedge 1/2$; log-unimodality alone buys nothing; a decreasing log-density improves the ratio towards $1/e$ as $\gamma\downarrow 0$; log-normal gives $\Phi(-\sqrt{-2\log\gamma})$.

**Log-concavity.** A log-concave survival function — the easiest case to check visually — gives the largest improvement of all.

The resulting thresholds, from the paper's table:

| Class | $\alpha=0.05$ | $\alpha=0.01$ | $\alpha=0.001$ |
|---|---|---|---|
| Any e-variable (Markov) | 20 | 100 | 1000 |
| Decreasing or unimodal density | 10 | 50 | 500 |
| Decreasing or log-unimodal-symmetric log-density | 7.49 | 36.82 | 367.88 |
| Log-normal | 3.87 | 14.97 | 118 |
| Log-concave density or survival | 3.15 | 4.65 | 6.91 |

**Comonotonicity.** If a family of e-variables are all increasing functions of a common source, their supremum may be used with the improved threshold and still control type-I error — strictly more powerful than mixing them. Taking the supremum over the maximal comonotonic set recovers exactly the p-value, so the supremum is a middle ground between a single e-value and a p-value. Comonotonicity is not preserved by optional stopping.

**A negative result.** No boosting is possible for e-BH from a decreasing density alone.

## Why It Matters

This is the most directly usable result in the cluster. You do not need a new procedure or a new assumption about dependence: you plot the null e-values, observe the shape, and read a smaller threshold off the table. At $\alpha=0.05$ that can mean rejecting at 3.15 instead of 20.

## See Also

[[concepts/e-value|E-value]] · [[concepts/false-discovery-rate|False Discovery Rate]]

Refines the e-to-p calibrator of [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]], which is smallest over *all* e-variables but beatable on subclasses. Contrasts its decreasing-density result with [[sources/wang-2023-p-star-values|Wang (2024)]].
<!-- AUTHORED REGION END -->
