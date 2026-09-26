---
title: Testing by Betting
page_id: concepts/testing-by-betting
page_type: concept
concept_type: framework
abstraction_level: intermediate
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- betting
- game-theoretic-probability
- martingale
- kelly
sources:
- sources/vovk-2024-merging-sequential-evalues
- sources/wang-2022-e-backtesting
- sources/su-2026-llm-watermark-eprocesses
related:
- concepts/e-value
- concepts/e-process
- concepts/anytime-valid-inference
mind_map_priority: medium
schema_version: 2
uuid: 66116c30-5dbe-5ea1-8ee0-36973268682a
content_hash: sha256:07986b132f272fdf3a031071b2113b56cfbe33efb9f109458fe568298fe84a1f
---

<!-- AUTHORED REGION START -->
# Testing by Betting

## The idea

Replace "how unlikely is this data under the null?" with "how much money would I have made betting against the null?". You start with capital 1 and repeatedly place bets that are fair if the null is true. Your wealth is then the test statistic: it cannot systematically grow under the null, so large wealth is evidence against it.

The evidence is the money. No sampling distribution needs to be derived, and the number means the same thing whatever the model.

## Mechanics

Each round converts an observation into a payoff $X_t$ with $\mathbb{E}[X_t\mid\mathcal{F}_{t-1}]\le 1$ — an [[concepts/e-value|e-value]]. You choose in advance what fraction $\lambda_t$ of your capital to stake:
\[
M_t=\prod_{s\le t}\bigl(1-\lambda_s+\lambda_s X_s\bigr).
\]
Staking nothing ($\lambda=0$) keeps your money; staking everything ($\lambda=1$) gives the plain product of the e-values. Keeping some capital back is what makes the process survive a bad round.

Ville's inequality bounds the chance the wealth ever reaches $1/\alpha$, which gives [[concepts/anytime-valid-inference|anytime validity]].

## Choosing stakes

Growth rate under the alternative is the objective, which connects this literature to the Kelly criterion. The risk papers use rules named GRO, GREE, GREL and GREM — an oracle and three empirical approximations. [[sources/vovk-2024-merging-sequential-evalues|Vovk & Wang (2024)]] prove that every admissible way of merging sequential e-values is exactly such a gambling strategy, and that betting everything is usually not the best one.

## Where it shows up here

- [[sources/wang-2022-e-backtesting|E-backtesting]] — betting against a bank's reported Expected Shortfall, with the wealth compared to Basel-style thresholds of 2, 5 and 10.
- [[sources/fan-2024-testing-mean-variance-eprocesses|Testing the mean and variance]] — betting against a claimed conditional variance.
- [[sources/su-2026-llm-watermark-eprocesses|Watermark detection]] — betting that a token stream is not watermarked.

The three use identical machinery with different payoffs, which is the clearest sign that the pattern generalises.

## Related Concepts

[[concepts/e-value|E-value]] · [[concepts/e-process|E-process]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]]
<!-- AUTHORED REGION END -->
