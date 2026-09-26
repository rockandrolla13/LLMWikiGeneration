---
title: E-value
page_id: concepts/e-value
page_type: concept
concept_type: definition
abstraction_level: foundational
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- e-value
- hypothesis-testing
- betting
- anytime-valid
sources:
- sources/vovk-2020-evalues-calibration-combination
- sources/wang-2025-admissible-merging-evalues
- sources/wang-2021-fdr-control-evalues
- sources/blier-wong-2024-improved-thresholds
related:
- concepts/e-process
- concepts/testing-by-betting
- concepts/anytime-valid-inference
- concepts/p-value-merging
- concepts/false-discovery-rate
- concepts/multiple-testing
- concepts/null-hypothesis-significance-testing
mind_map_priority: high
schema_version: 2
uuid: ac4b2159-6a4f-5c39-9f57-e3cb665dd5dc
content_hash: sha256:ffa2dde05028a973edb79a5eee6c7ce6c00f9f5bc393dc05a804552f49f94418
---

<!-- AUTHORED REGION START -->
# E-value

## Definition

An **e-variable** is a non-negative extended random variable $E$ with
\[
\mathbb{E}[E]\le 1
\]
under the null hypothesis. An **e-value** is a realised value of one. The value $\infty$ is permitted and licenses outright rejection.

Compare the p-value, defined by a tail probability, $\mathbb{P}(P\le\alpha)\le\alpha$. The e-value is defined by an **expectation**, and that single change is the source of everything else.

## The betting reading

An e-value is the payoff of a bet against the null at fair odds: stake 1, and under the null you cannot expect to profit. An e-value of 20 means your stake multiplied twenty-fold in a game the null said was fair. Large values are evidence, and the scale is interpretable without reference to a sampling distribution.

Markov's inequality gives the basic test: reject when $E\ge 1/\alpha$, and the type-I error is at most $\alpha$.

## Why it is worth the conversion

- **Merging needs no dependence model.** A weighted average of e-values is always an e-value, whatever the dependence. [[sources/wang-2025-admissible-merging-evalues|Wang (2025)]] shows weighted averaging is the *only* admissible rule under arbitrary dependence, so nothing better is waiting to be found. Merging p-values, by contrast, requires constants that are often only available numerically ([[sources/vovk-2021-admissible-merging-pvalues|Vovk, Wang & Wang, 2022]]).
- **Multiplication over time.** Because the constraint is an expectation, e-values compose into [[concepts/e-process|e-processes]] and support optional stopping.
- **Multiple testing without corrections.** [[sources/wang-2021-fdr-control-evalues|e-BH]] controls the false discovery rate under arbitrary dependence with no penalty.

## Calibration

You can convert between the two currencies, at a cost. A decreasing $f:[0,1]\to[0,\infty]$ with $\int_0^1 f\le 1$ turns p-values into e-values; the reverse direction has a unique admissible choice, $e\mapsto\min(1,1/e)$. Round trips lose: a p-value of 0.5% returns as 7.2%.

[[sources/wang-2023-p-star-values|P\*-values]] sit between the two, and contain mid p-values.

## Reading the number

The cluster uses Jeffreys's scale: below 1 supports the null; up to $\sqrt{10}\approx3.16$ barely worth mentioning; up to 10 substantial; up to $10^{3/2}\approx31.6$ strong; up to 100 very strong; above 100 decisive. Roughly, $e=10$ corresponds to $p=1\%$ and $e=\sqrt{10}$ to $p=5\%$.

The threshold $1/\alpha$ is conservative, because Markov is loose. [[sources/blier-wong-2024-improved-thresholds|Blier-Wong & Wang]] show that a decreasing density halves it and log-concavity improves it far more — at $\alpha=0.05$, from 20 down to about 3.15.

## Sources

- [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]] — the founding paper: definitions, calibration, merging.
- [[sources/wang-2025-admissible-merging-evalues|Wang (2025)]] — weighted averaging is the only admissible merge.
- [[sources/wang-2021-fdr-control-evalues|Wang & Ramdas (2022)]] — e-BH.
- [[sources/blier-wong-2024-improved-thresholds|Blier-Wong & Wang]] — sharper thresholds.

## Related Concepts

[[concepts/e-process|E-process]] · [[concepts/testing-by-betting|Testing by Betting]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/null-hypothesis-significance-testing|Null Hypothesis Significance Testing]]
<!-- AUTHORED REGION END -->
