---
title: E-process
page_id: concepts/e-process
page_type: concept
concept_type: definition
abstraction_level: foundational
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- e-process
- martingale
- optional-stopping
- sequential-testing
sources:
- sources/vovk-2019-confidence-discoveries-evalues
- sources/vovk-2024-merging-sequential-evalues
- sources/fan-2024-testing-mean-variance-eprocesses
- sources/wang-2022-e-backtesting
related:
- concepts/e-value
- concepts/anytime-valid-inference
- concepts/testing-by-betting
mind_map_priority: high
schema_version: 2
uuid: d77bfebb-61e0-540f-b09d-2244da4deee0
content_hash: sha256:24529a60d79a3e38dfcfe0b61aff4de43a09ddaced1e1be49eb079ebcf97ce20
---

<!-- AUTHORED REGION START -->
# E-process

## Definition

An **e-process** is a sequence $(E_t)$ adapted to a filtration such that $E_\tau$ is an [[concepts/e-value|e-variable]] for **every** stopping time $\tau$ — not merely at a fixed horizon.

The canonical construction is a wealth process. Starting from capital 1 and betting a predictable fraction $\lambda_t\in[0,1]$ on each incoming e-value $X_t$,
\[
M_t=\prod_{s\le t}\bigl(1-\lambda_s+\lambda_s X_s\bigr),
\]
which is a non-negative supermartingale under the null. Ville's inequality then gives
\[
\mathbb{P}\Bigl(\sup_t M_t\ge 1/\alpha\Bigr)\le\alpha ,
\]
so you may watch the process continuously and reject the first time it crosses $1/\alpha$.

## Why it matters

This is the property that makes continuous monitoring honest. With a classical fixed-sample test, checking after every observation and stopping at the first rejection inflates the error rate badly. With an e-process it does not: the guarantee is uniform over stopping times, so the sample size may be data-dependent, unbounded, or chosen by someone else.

That is what [[sources/wang-2022-e-backtesting|E-backtesting]] exploits for risk forecasts, [[sources/fan-2024-testing-mean-variance-eprocesses|Fan, Jiao & Wang]] for conditional means and variances, [[sources/su-2026-llm-watermark-eprocesses|Su, Wang & Zhao]] for streaming text, and [[sources/xu-2021-bandit-multiple-testing|Xu, Wang & Ramdas]] for adaptive sampling.

## Choosing the bet

The stake $\lambda_t$ decides how fast the process grows under the alternative, and it must be chosen from the past only. [[sources/vovk-2024-merging-sequential-evalues|Vovk & Wang (2024)]] show every admissible way of merging sequential e-values *is* such a gambling strategy, and warn against the obvious default: staking everything ($\lambda=1$, the plain product) maximises variance and is not optimal when the expected log e-value is negative.

Adaptive rules — plug-in maximum likelihood, Bayes updates, or the GREE-style rules used in the risk papers — beat fixed misspecified stakes in the long run.

## Not everything with e-values is an e-process

[[sources/vovk-2024-nonparametric-e-tests-symmetry|Nonparametric e-tests of symmetry]] are fixed-sample conditional e-variables, computed given the observed magnitudes. They are not e-processes and carry no optional-stopping claim.

## Sources

- [[sources/vovk-2019-confidence-discoveries-evalues|Vovk & Wang (2023)]] — the definition used here.
- [[sources/vovk-2024-merging-sequential-evalues|Vovk & Wang (2024)]] — betting is the only admissible sequential merge.
- [[sources/fan-2024-testing-mean-variance-eprocesses|Fan, Jiao & Wang (2024)]] — mean and variance testing.
- [[sources/wang-2022-e-backtesting|Wang, Wang & Ziegel]] — risk backtesting.

## Related Concepts

[[concepts/e-value|E-value]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/testing-by-betting|Testing by Betting]]
<!-- AUTHORED REGION END -->
