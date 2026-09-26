---
title: Anytime-Valid Inference
page_id: concepts/anytime-valid-inference
page_type: concept
concept_type: technique
abstraction_level: intermediate
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- anytime-valid
- optional-stopping
- sequential-testing
- confidence-sequence
sources:
- sources/wang-2022-e-backtesting
- sources/xu-2021-bandit-multiple-testing
- sources/vovk-2026-ci-causal-sequential
- sources/hore-2026-monotone-density-calibration
related:
- concepts/e-process
- concepts/e-value
- concepts/testing-by-betting
mind_map_priority: high
schema_version: 2
uuid: 1c17ff1a-e176-56fd-aa5b-9e858d40b9c3
content_hash: sha256:d2da55642d9afd69d8ba9634f62cebbdd3163c590afe0725625d57ca342ce66d
---

<!-- AUTHORED REGION START -->
# Anytime-Valid Inference

## Definition

An inference is **anytime-valid** if its guarantee holds at every stopping time rather than at one pre-committed sample size. A test is anytime-valid if its type-I error is controlled however long you watch and whenever you decide to stop; a **confidence sequence** is a sequence of intervals that covers the truth simultaneously at all times.

## The problem it solves

Classical guarantees are indexed by a fixed $n$. Look at the data as it arrives, stop when the result becomes significant, and the stated error rate is no longer the real one — the familiar peeking problem. In practice almost every monitoring application peeks: risk backtests are reviewed continuously, experiments are watched daily, detectors run on streams.

Anytime validity removes the tension. The sample size may be random, data-dependent, unbounded, or chosen by another party.

## How it is obtained

Two routes appear in this wiki:

**Via [[concepts/e-process|e-processes]].** A non-negative supermartingale starting at 1 obeys Ville's inequality, which bounds the probability that it *ever* crosses $1/\alpha$. This is the route in [[sources/wang-2022-e-backtesting|E-backtesting]], [[sources/fan-2024-testing-mean-variance-eprocesses|Fan, Jiao & Wang]], [[sources/su-2026-llm-watermark-eprocesses|the watermark detector]] and [[sources/hore-2026-monotone-density-calibration|Hore, Wang & Ramdas]].

**Via union bounds over time.** Split the error budget across dyadic blocks and combine the resulting intervals. [[sources/vovk-2026-ci-causal-sequential|Vovk & Wang (2026)]] take this route for causal effects, and prove the resulting law-of-the-iterated-logarithm term is unavoidable.

## The cost

Anytime validity is not free. Against a correctly specified model at a fixed, honestly pre-committed sample size, a classical test is more powerful — the E-backtesting paper says so plainly. What you buy is freedom from having to commit, and validity when the stopping rule is not under your control.

## Sources

- [[sources/wang-2022-e-backtesting|Wang, Wang & Ziegel]] — continuous monitoring of risk forecasts.
- [[sources/xu-2021-bandit-multiple-testing|Xu, Wang & Ramdas (2021)]] — FDR control at every stopping time under adaptive sampling.
- [[sources/vovk-2026-ci-causal-sequential|Vovk & Wang (2026)]] — confidence sequences for causal effects.

## Related Concepts

[[concepts/e-process|E-process]] · [[concepts/e-value|E-value]] · [[concepts/testing-by-betting|Testing by Betting]]
<!-- AUTHORED REGION END -->
