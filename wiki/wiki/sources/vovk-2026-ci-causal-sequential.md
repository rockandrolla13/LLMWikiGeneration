---
title: Confidence intervals for causal effects in sequential decision making
page_id: sources/vovk-2026-ci-causal-sequential
page_type: source
source_path: markdown_output/vovk-2026-ci-causal-sequential.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2026
venue: Working paper, arXiv:2605.25687 (26 June 2026)
tags:
- causal-inference
- confidence-sequence
- anytime-valid
- back-door
- front-door
sources: []
related:
- concepts/anytime-valid-inference
- concepts/causal-inference
- concepts/e-value
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: 81406e15-9430-5dea-9380-0ca79c759554
content_hash: sha256:0ff9c1ff2c8bb5406f1375a9937b7fff61b3f18d8d84d64f2412196a259b9fb3
---

<!-- AUTHORED REGION START -->
# Confidence Intervals for Causal Effects in Sequential Decision Making

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2026 · **Venue:** Working paper, arXiv:2605.25687

## Summary

Causal inference results usually assume the data are IID. In sequential decision making they are not: each intervention may be chosen in light of everything seen so far. This paper gives finite-sample confidence intervals for a causal effect in that setting.

Notably, and unlike most of this cluster, it does **not** use e-values. It builds ordinary Hoeffding intervals for each constituent probability, upgrades them to confidence sequences, and then propagates them through the causal formula using interval arithmetic.

## Construction

The causal effect under the back-door criterion is a polynomial in estimable probabilities,
\[
P\bigl(y \mid do(\tilde x)\bigr)=\sum_z P(y\mid \tilde x, z)\,P(z).
\]
Each factor gets its own interval: Proposition 8 for the fixed-sample case, and Proposition 9 for a confidence *sequence*, built by splitting the error budget $\delta$ across dyadic blocks $n_k=2^k$ with $\delta_k\propto 1/k^2$. The intervals are then combined by interval arithmetic. Corollary 11 gives the propagation rule: for a polynomial expression, the half-width of the result is obtained by replacing every multiplication with addition.

The midpoints are the plug-in estimates; the half-width expressions were dropped as images by the converter and are not restated here.

## Results

- **Theorems 1 and 2:** the tightest intervals, for back-door and front-door adjustment respectively, in the IID case. The error budget is split across $2|Z|$ constituent probabilities for back-door, and $K=(|X|+1)(|Z|+1)-1$ for front-door.
- **Theorems 3 and 4:** the adaptive fixed-horizon case, and an anytime-valid confidence sequence. Both carry a law-of-the-iterated-logarithm term.
- **Theorem 6:** that term is unavoidable.

In the binary case the budget is split by 3 rather than 4. The paper notes its constants follow from $\zeta(2)=\pi^2/6$, with $\pi^2/3\approx 3.29$ rounded to 3.3, and 9.9 rounded to 10 in the binary case.

## Why It Matters

The design decision worth borrowing is the separation of concerns: estimate each ingredient with an anytime-valid interval, then propagate through the identification formula mechanically. Nothing in that recipe is specific to causal inference; it applies to any quantity that is a polynomial in estimable probabilities.

## Relation to the Companion Note

Section 7 compares this paper with [[sources/vovk-2026-conformal-e-confounding|Conformal e-prediction in the presence of confounding]]. That note gives e-prediction sets under the IID and Y-oblivious settings. This paper gives traditional confidence intervals and prediction sets, which it expects to be "much more conservative" in the IID setting, but it works under the strong interpretation, which the e-prediction note cannot handle.

The authors state that they used OpenAI Codex for literature search and brainstorming.

## See Also

[[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/causal-inference|Causal Inference]] · [[concepts/e-value|E-value]]

**Not yet written:** `concepts/confidence-sequence`, `concepts/front-door-criterion`, `concepts/do-calculus`.
<!-- AUTHORED REGION END -->
