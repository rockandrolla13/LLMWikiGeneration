---
title: Merging sequential e-values via martingales
page_id: sources/vovk-2024-merging-sequential-evalues
page_type: source
source_path: markdown_output/vovk-2024-merging-sequential-evalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2024
venue: Electronic Journal of Statistics 18, 1185-1205 (2024)
tags:
- e-value
- martingale
- merging
- sequential
- betting
sources: []
related:
- concepts/e-value
- concepts/testing-by-betting
- concepts/anytime-valid-inference
- concepts/p-value-merging
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: high
schema_version: 2
uuid: dd02f3a0-bce1-50a0-94b1-9f5374f63489
content_hash: sha256:58abeaaa73abef14b78dd1b6ad58523ec19e722dea019ebfb8cfa398eba37db9
---

<!-- AUTHORED REGION START -->
# Merging Sequential E-values via Martingales

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2024 · **Venue:** Electronic Journal of Statistics 18, 1185–1205

## Summary

If e-values arrive one at a time and each is valid given the past, how should they be combined? The answer is that **betting is the only game in town**: every admissible way of merging sequential e-values is a gambling strategy.

## Construction

A **gambling system** assigns to each history a stake $s\in[0,1]$. The corresponding **game martingale** starts at capital $c$ and evolves as
\[
S_K(\mathbf{e})=S_0\prod_{k=1}^{K}\bigl(1+s(\mathbf{e}_{(k-1)})(e_k-1)\bigr),
\]
so at each step you choose what fraction of current capital to stake on the next e-value. Because the process is a supermartingale, $S_\tau$ is an e-variable at every stopping time — this is where anytime validity comes from.

Special cases: staking everything at every step gives the product $\prod_k E_k$; a constant stake $\lambda$ gives $\prod_k(1-\lambda+\lambda e_k)$; the arithmetic mean and U-statistics are also game martingales.

## Results

**The characterisation.** Every sequential-e-merging function is dominated by a game martingale, so the admissible ones are exactly the game martingales. Equivalently, a function is a game martingale with initial value 1 precisely when it is adapted, anytime valid and precise.

**Independence is different.** For merely independent e-values, betting with an adaptive reading order remains valid but no longer exhausts the admissible rules; the paper gives a counterexample, credited to Zhenyuan Zhang, of an admissible merging function outside the class.

**The product is not the right default.** Among precise sequential merging functions the product has the largest variance, which is undesirable, and when the expected log e-value is negative the optimal stake is strictly interior — betting everything is then the wrong move.

## Numbers

A simulation with IID normal data, a true shift of 0.3, $K=500$ and 1,000 runs compares five stakes: the growth-optimal choice, a misspecified constant, a random one, a Bayes update, and a plug-in maximum likelihood estimate. The adaptive strategies beat the misspecified and random ones for large samples.

## Why It Matters

This is the formal justification for the betting picture that runs through the whole cluster, including [[sources/wang-2022-e-backtesting|E-backtesting]]. It also warns against the obvious default: multiplying every e-value is admissible but often a poor bet.

## See Also

[[concepts/e-value|E-value]] · [[concepts/testing-by-betting|Testing by Betting]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/p-value-merging|Merging P-values and E-values]]

The arbitrary-dependence counterpart is [[sources/wang-2025-admissible-merging-evalues|Wang (2025)]], where weighted averaging is the only admissible rule.
<!-- AUTHORED REGION END -->
