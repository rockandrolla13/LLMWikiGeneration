---
title: Post-selection inference for e-value based confidence intervals
page_id: sources/xu-2024-post-selection-evalue-ci
page_type: source
source_path: markdown_output/xu-2024-post-selection-evalue-ci.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Ziyu Xu
- Ruodu Wang
- Aaditya Ramdas
year: 2024
venue: Electronic Journal of Statistics (2024)
tags:
- e-value
- confidence-intervals
- post-selection-inference
- false-coverage-rate
- multiple-testing
sources: []
related:
- concepts/e-value
- concepts/false-discovery-rate
- concepts/anytime-valid-inference
- entities/ziyu-xu
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: 652ef8ae-2dac-5c7f-b638-c047a2de529c
content_hash: sha256:c5b0a154db0a566f55ca9f7017073805493f2e2c69acb1f344aeba3a80713241
---

<!-- AUTHORED REGION START -->
# Post-selection Inference for E-value Based Confidence Intervals

**Authors:** [[entities/ziyu-xu|Ziyu Xu]], [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2024 · **Venue:** Electronic Journal of Statistics

## Summary

You build a confidence interval for each of $K$ parameters, then report only the interesting subset. That selection destroys coverage: the reported intervals are chosen because they looked extreme. The standard fix, the Benjamini–Yekutieli procedure, needs either an independence-style assumption or a restricted selection rule, and otherwise pays a $\log K$ penalty.

This paper shows that if the intervals are built from [[concepts/e-value|e-values]], the penalty disappears. The procedure is one line, and it holds under any dependence and any selection rule.

## Construction

An **e-confidence interval** is
\[
C(\alpha)=\bigl\{\theta\in\Theta : E(\theta) < 1/\alpha \bigr\},
\]
where $E(\theta)$ is an e-value for the hypothesis that the parameter equals $\theta$. Proposition 1 notes that every e-CI is a valid confidence interval, straight from Markov's inequality.

The **e-BY procedure** is then: for each selected index $i\in S$, report the $\bigl(1-\delta|S|/K\bigr)$ confidence interval. That is the whole method.

## Results

- **Theorem 2:** e-BY controls the false coverage rate at $\delta$ under *any* dependence and *any* selection rule.
- **Theorem 3:** the bound is sharp.
- **Theorem 4:** e-BY is admissible among confidence-interval reporting procedures.
- **Theorem 1:** any confidence interval can be turned into an e-CI through the dual of a p-to-e calibrator, and doing so recovers classical BY as a special case.
- **Corollary 1:** a post-hoc bound on the realised false coverage proportion, even when $\delta$ is chosen after seeing the data.

The comparison the paper draws: BY may use $\alpha_i=\delta|S|/K$ only under independence or PRDS *and* a restricted selection rule. Otherwise it must use $\delta|S|/(K\ell_K)$, where $\ell_K=\sum_{i=1}^{K} i^{-1}\approx\log K$. e-BY keeps $\delta|S|/K$ unconditionally.

**Empirical study.** Twitter A/B tests over an 18-month period, each running at least two weeks: 263 experiments, 15 metrics with control and treatment counted separately so $K=30$, sample sizes on the order of $10^6$ users even on the first day. At $\delta=0.1$, e-BY justified shipping decisions for 127 experiments against 122 for BY, and took 1.2 days on average to satisfy the shipping criteria against 1.5 days for BY.

## Why It Matters

The practical shape of this result is that sequential experimentation and selective reporting stop being in tension. Because the intervals are e-value based, they are already valid at arbitrary stopping times, and the selection correction does not need to know how the selection was made.

## See Also

[[concepts/e-value|E-value]] · [[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]]

**Not yet written:** `concepts/false-coverage-rate`, `concepts/p-to-e-calibrator`.
<!-- AUTHORED REGION END -->
