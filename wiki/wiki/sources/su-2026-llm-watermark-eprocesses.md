---
title: Online LLM watermark detection via e-processes
page_id: sources/su-2026-llm-watermark-eprocesses
page_type: source
source_path: markdown_output/su-2026-llm-watermark-eprocesses.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Weijie Su
- Ruodu Wang
- Zinan Zhao
year: 2026
venue: Working paper, arXiv:2602.14286 (13 April 2026)
tags:
- e-process
- anytime-valid
- llm-watermarking
- sequential-testing
- calibrator
sources: []
related:
- concepts/e-process
- concepts/e-value
- concepts/anytime-valid-inference
- concepts/testing-by-betting
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: 464cce9b-aa5b-5ee9-a8f5-612b6d3a8f53
content_hash: sha256:90edee2958f7e3ef1952a0f08ac453e4841448fb6614e84fe7d872ab0a44800e
---

<!-- AUTHORED REGION START -->
# Online LLM Watermark Detection via E-processes

**Authors:** Weijie Su, [[entities/ruodu-wang|Ruodu Wang]], Zinan Zhao (listed alphabetically)

**Year:** 2026 · **Venue:** Working paper, arXiv:2602.14286

## Summary

Watermarked text from a language model carries a statistical fingerprint: each token depends on a pseudo-random vector the detector also knows. Detection is therefore a sequential independence test. The problem with fixed-sample detectors is that text arrives as a stream and you want to check continuously, which inflates false positives.

This paper builds the detector as an [[concepts/e-process|e-process]], so checking after every token is legitimate.

## Construction

For each token a pivotal statistic $Y_t$ is computed — for the Gumbel-max scheme, $Y_t=U_{t,W_t}$ — which is uniform under the null of unwatermarked text and stochastically smaller under the alternative. The detector is the product
\[
M_t=\prod_{s\le t} f_s\bigl(1-Y_s\bigr),
\]
where each $f_s$ is a **predictable calibrator**: decreasing, non-negative, integrating to one on $[0,1]$, and determined only by $Y_1,\dots,Y_{s-1}$. Three variants are studied: a non-adaptive calibrator; a weight-adaptive one that tunes its bet by maximising a running criterion; and an **online Grenander** calibrator, the left derivative of the least concave majorant of the empirical distribution of past $Y$ values. The recommended detector is the arithmetic mean of the Grenander and weight-adaptive versions.

## Results

- **Theorem 1:** $M$ is an unbiased e-process and a martingale, so Ville's inequality gives type-I error control at any stopping time.
- **Theorem 2:** this product form is the only admissible unbiased e-process under the natural filtration — essentially the only reasonable sequential test.
- **Theorems 3 and 4:** the process grows exponentially under the alternative, so the test has power one.
- **Proposition 1:** the information bound is the entropy of the next-token distribution, and so does not depend on which watermark scheme is used.

**Experiments.** A simulated vocabulary of 1,000 tokens, 700 tokens per sequence, 1,000 repetitions; then OPT-1.3B at temperatures 0.5 and 1 with 500 repetitions; then human-edit experiments where each token is edited with probability 0.1, 0.3 or 0.5 after the first 50. The finding as stated: only the e-process methods control sequential type-I error, while for sum-based detectors "the Type I error quickly explodes". Some sum-based detectors have better raw power at a fixed sample size, but the recommended average e-process can exceed them in some settings.

## Why It Matters

The machinery is exactly that of [[sources/wang-2022-e-backtesting|E-backtesting]]: a product of predictable bets, stopped by Ville's inequality. Only the payoff differs. That makes it a clean second example of the same pattern in a completely different domain, which is useful when deciding whether the pattern fits a problem of your own.

## See Also

[[concepts/e-process|E-process]] · [[concepts/e-value|E-value]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/testing-by-betting|Testing by Betting]]

[[sources/wang-2022-e-backtesting|E-backtesting]] uses the same betting construction for risk forecasts.

**Not yet written:** `concepts/p-to-e-calibrator`, `entities/weijie-su`.
<!-- AUTHORED REGION END -->
