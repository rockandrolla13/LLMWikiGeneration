---
title: 'Testing with p*-values: between p-values, mid p-values, and e-values'
page_id: sources/wang-2023-p-star-values
page_type: source
source_path: markdown_output/wang-2023-p-star-values.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Ruodu Wang
year: 2023
venue: Bernoulli (2024)
tags:
- p-star-value
- mid-p-value
- e-value
- calibration
- stochastic-dominance
sources: []
related:
- concepts/e-value
- concepts/p-value-merging
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: 448716fd-adf0-5c6f-ab94-9898f0d3e96c
content_hash: sha256:cf1e832b9c3a91a5da862628414367c4c577bd2c8b2cbe5c590ded85e78ab148
---

<!-- AUTHORED REGION START -->
# Testing with p*-values

**Author:** [[entities/ruodu-wang|Ruodu Wang]]

**Year:** preprint 2023 · **Venue:** Bernoulli (2024)

## Summary

Mid p-values, which arise whenever the test statistic is discrete, are not p-values: they do not satisfy the defining inequality. This paper identifies the object that contains them — the **p\*-value** — and shows it sits exactly between p-values and e-values.

## Definitions

With $U$ uniform on $[0,1]$, and $\le_1$, $\le_2$ denoting first- and second-order stochastic dominance:

- $P$ is a **p-variable** if $U \le_1 P$;
- $P$ is a **p\*-variable** if $U \le_2 P$;
- $E$ is an **e-variable** if $0 \le_2 E \le_2 1$.

Every p-variable is a p\*-variable, and so is every mid p-variable. Every p\*-variable has mean at least $1/2$.

## Results

**Structure.** P\*-variables are exactly the convex combinations of p-variables, and any p\*-variable is the arithmetic average of three p-variables — three being minimal.

**Turning them into p-values.** The sum of two p\*-variables is a p-variable, so $2P^*$ is always a p-value, and the multiplier 2 is optimal. That justifies testing a p\*-value at threshold $\alpha/2$.

**Merging.** Under arbitrary dependence, $e\cdot\prod_k P_k^{w_k}$ is a p-variable for arbitrary, possibly random weights summing to 1 — the critical value is $\alpha/e$ with $e\approx 2.718$. Both the arithmetic average and Bonferroni are admissible p\*-merging functions, which is notable because the average is invalid for p-merging and Bonferroni is inadmissible for e-merging.

**The bridge.** A convex p-to-e calibrator is a p\*-to-e calibrator, and an admissible p-to-e calibrator is one exactly when it is convex. Composing the e-to-p\* calibrator $e\mapsto (2e)^{-1}\wedge 1$ with the p\*-to-p calibrator $u\mapsto (2u)\wedge 1$ recovers the unique admissible e-to-p calibrator $e^{-1}\wedge 1$. That is the precise sense in which p\*-values sit between the two.

## Why It Matters

Discrete data are common and mid p-values are widely used despite being invalid as p-values. This gives them a proper home, with a clean decision rule: compare to $\alpha/2$.

## See Also

[[concepts/e-value|E-value]] · [[concepts/p-value-merging|Merging P-values and E-values]]

Uses the calibrator theory of [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]] and the geometric-mean result of [[sources/vovk-2021-admissible-merging-pvalues|Vovk, Wang & Wang (2022)]]. [[sources/blier-wong-2024-improved-thresholds|Blier-Wong & Wang]] contrast their decreasing-density result with this paper's.
<!-- AUTHORED REGION END -->
