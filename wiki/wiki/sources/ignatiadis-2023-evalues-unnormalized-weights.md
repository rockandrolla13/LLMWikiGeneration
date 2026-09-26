---
title: E-values as unnormalized weights in multiple testing
page_id: sources/ignatiadis-2023-evalues-unnormalized-weights
page_type: source
source_path: markdown_output/ignatiadis-2023-evalues-unnormalized-weights.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Nikolaos Ignatiadis
- Ruodu Wang
- Aaditya Ramdas
year: 2023
venue: Biometrika 111(2), 417-439 (2024)
tags:
- e-value
- multiple-testing
- weighted-testing
- false-discovery-rate
- meta-analysis
sources: []
related:
- concepts/e-value
- concepts/multiple-testing
- concepts/false-discovery-rate
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: high
schema_version: 2
uuid: 386ab344-8062-55f5-8c17-080b0135bab2
content_hash: sha256:eb94c10313b5aa6d8aa50d064f88b36523e6041a1a4603e3fe9b33a7b3c27487
---

<!-- AUTHORED REGION START -->
# E-values as Unnormalized Weights in Multiple Testing

**Authors:** Nikolaos Ignatiadis, [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** preprint 2023 · **Venue:** Biometrika 111(2), 417–439 (2024)

## Summary

Suppose each hypothesis carries both a p-value from a primary dataset and an e-value from a secondary one. How do you use both? This paper's answer is disarmingly simple: divide.

## The combiner

Set
\[
Q_k=\Bigl(\frac{P_k}{E_k}\Bigr)\wedge 1
\]
and feed the $Q_k$ into any ordinary p-value procedure, giving ep-BH, ep-Simes, ep-Bonferroni and ep-Hochberg. Equivalently, the e-values act as **weights** on the p-values — and crucially they need not be normalised to sum to $K$, which every classical weighted procedure requires.

That freedom is the point. Normalisation forces the weights to be a fixed budget shared out among hypotheses; an e-value is already calibrated on its own terms, so the total can be whatever the evidence says.

## Guarantees

If the e-vector is independent of the p-vector and the p-values are positively dependent, ep-BH controls FDR at $\pi_0\alpha$ — with **arbitrary dependence among the e-values**. Weaker conditions give weaker but still useful bounds: with per-null independence and arbitrary dependence, the factor $\ell_K\approx\log K$ reappears; ep-Bonferroni controls the family-wise error rate at $\alpha$. An adaptive variant, ep-Storey, estimates the null proportion from the p-values and controls FDR at $\alpha$ under p-independence.

## Numbers

On a gene-expression study at $\alpha=0.01$ — 24,906 RNA-Seq p-values combined with 15,875 microarray e-values — the discovery counts are: BH 1,973 against **ep-BH 2,387**; normalized-weight wBH 1,310; IHW 2,016. Among adaptive methods, Storey-BH 2,147 against **ep-Storey 2,540**. The average weight budget used by the ep methods is 18.11 and 24.35, against 1.00 for the normalized methods — a direct measure of what normalisation costs.

Efficiency of the simple divide-and-threshold combiner against the full likelihood ratio is 0.989 in the paper's asymptotic comparison, so very little is lost by not modelling the joint structure.

## Why It Matters

The pattern generalises past meta-analysis: any time you have a principal test plus side information that can be expressed as a bet, this converts the side information into power without assuming how the two sources relate.

## See Also

[[concepts/e-value|E-value]] · [[concepts/multiple-testing|Multiple Testing]] · [[concepts/false-discovery-rate|False Discovery Rate]]

Builds on [[sources/wang-2021-fdr-control-evalues|e-BH]]; the compound e-value view is developed in [[sources/ignatiadis-2024-asymptotic-compound-evalues|Ignatiadis et al.]] and applied to adaptive BH in [[sources/ignatiadis-2026-compound-adaptive-bh|the 2026 paper]]. Cites [[sources/xu-2021-bandit-multiple-testing|Xu et al. (2021)]] as a source of e-value lists.
<!-- AUTHORED REGION END -->
