---
title: Combining e-values using demi-supermartingales
page_id: sources/ming-2026-demi-supermartingales
page_type: source
source_path: markdown_output/ming-2026-optimized-combination-evalues.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Jiahao Ming
- Aaditya Ramdas
- Yi Shen
- Ruodu Wang
- Ian Waudby-Smith
year: 2026
venue: Working paper, arXiv:2603.10329v3 (3 August 2026)
tags:
- e-value
- demi-supermartingale
- merging
- concentration
- multi-armed-bandits
sources: []
related:
- concepts/e-value
- concepts/p-value-merging
- concepts/anytime-valid-inference
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: d74e5ec9-67b3-5892-88ba-f3de8f96ea2f
content_hash: sha256:d0f553237f582e4a0a6679fe5ee0ddecec7e00b38180cfdff784ad719e7aaa0c
---

<!-- AUTHORED REGION START -->
# Combining E-values Using Demi-supermartingales

**Authors:** Jiahao Ming, [[entities/aaditya-ramdas|Aaditya Ramdas]], Yi Shen, [[entities/ruodu-wang|Ruodu Wang]], Ian Waudby-Smith

**Year:** 2026 · **Venue:** Working paper, arXiv:2603.10329v3, 3 August 2026

**Note on metadata.** Ruodu Wang's working paper page lists this entry as "Optimized combination of independent or simultaneous e-values" by Ming, Shen and Wang. The arXiv v3 PDF has a different title, two additional authors and a different central result. The page listing is stale; this page follows the PDF.

## Summary

A new way to combine independent e-values, built on **demi-supermartingales** rather than supermartingales, which settles an old conjecture in nonparametric mean testing and yields a sharper statistic under weaker assumptions.

## The dependence notion

Between independence and sequential validity the paper inserts **co-validity**: $\mathbb{E}[E_i \mid \mathbf{E}_{-i}]\le 1$ for every $i$, conditioning on *all* the others rather than only the past. The inclusions are independent $\subset$ co-valid $\subset$ sequential, and the paper shows by example that co-validity is genuinely stronger than sequential validity.

## The construction

Let $A_k(\mathbf{x})$ be the average term of the elementary symmetric polynomial of degree $k$, with $A_0=1$. For co-valid e-variables, the process $(A_k(\mathbf{E}))_{k=0}^{n}$ is a nonnegative **demi-supermartingale**: it satisfies $\mathbb{E}[(M_{k+1}-M_k)g(M_0,\dots,M_k)]\le 0$ for every decreasing non-negative $g$. Every supermartingale is one; the converse fails, and the paper gives a two-variable example where the symmetric-polynomial process is a demi-martingale but not a supermartingale.

The payoff is a Ville-type inequality for nonnegative demi-supermartingales, giving
\[
\mathbb{P}\Bigl(\max_{0\le k\le n} A_k(\mathbf{E}) \ge x\Bigr)\le \frac{1}{x},
\]
together with the fact that the running maximum dominates the constant-betting wealth $\prod_i(1-\lambda+\lambda E_i)$ for every $\lambda\in[0,1]$. The ordinary supermartingale route cannot prove this, because the wealth process is not a supermartingale in $\lambda$.

## Results

The inequality settles the Wang–Zhao and Gaffke conjectures positively, with a sharper statistic and weaker assumptions, and extends to compound e-values with heterogeneous conditional means. Practically it converts a batch of e-values into a p-value, $P_n = 1/\max_k A_k(\mathbf{E})$, that is uniformly more powerful than the KL-based alternative at a fixed sample size, without the regret inflation an anytime-valid method pays.

There are closed-form confidence intervals for a bounded mean requiring no root-finding, nested inside the optimised-product intervals, with asymptotic width matching: $\sqrt{n}\,w_n \to 2\sigma\sqrt{2\log(2/\alpha)}$. The polynomial evaluation runs in $O(n\log^2 n)$ with FFT-based multiplication.

The authors state that AI tools were used to assist with some technical results and language editing.

## Why It Matters

This is the independence-side counterpart to [[sources/wang-2025-admissible-merging-evalues|Wang (2025)]]. Under arbitrary dependence, weighted averaging is the only admissible rule. Under independence or co-validity, richer rules exist, and this gives one that is not comparable to any weighted average.

## See Also

[[concepts/e-value|E-value]] · [[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]]

Answers a question posed in [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]]; sits in the regime [[sources/wang-2025-admissible-merging-evalues|Wang (2025)]] explicitly excludes.
<!-- AUTHORED REGION END -->
