---
title: Spread
page_id: concepts/spread
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- spread
- pairs-trading
- mean-reversion
- statistical-arbitrage
- fixed-income
sources:
- sources/moura-2016-pairs-trading-kalman
- sources/triantafyllopoulos-2011-mean-reverting-spreads
- sources/zhang-2021-pairs-general-ssm
related:
- concepts/pairs-trading
- concepts/mean-reversion
- concepts/credit-spread-curve
mind_map_priority: medium
schema_version: 2
uuid: ce2ae689-dd3d-53ba-a382-41ef8e909b9e
content_hash: sha256:4a07a1edf4e84d855e9d971b0f76143e1a271e2e03b80a120d5867a9481eaf7c
---

<!-- AUTHORED REGION START -->
# Spread

A difference between two prices or rates, held as a position in its own right. The wiki uses the word in two distinct senses, and the pages that link here mean the first.

## The Constructed Spread

In [[concepts/pairs-trading|pairs trading]] the spread is a synthetic instrument built from two securities:

S_t = P_A,t − γ · P_B,t

where γ is the hedge ratio. It can be set to 1, to the price ratio, estimated by OLS or a [[concepts/kalman-filter|Kalman filter]], or taken as the cointegration vector from a Johansen test. The choice of γ is what makes the spread tradable rather than merely observable.

The strategy assumes the spread mean-reverts:

dS_t = κ(μ − S_t)dt + σ dW_t

with κ the speed of reversion, μ the long-term mean and σ the volatility. Half-life is H = ln(2)/κ — the time for the spread to revert halfway. Entry is on deviation (|z| above a threshold, a Bollinger band break, a reversion probability, or an expected profit that clears transaction costs); exit is on the spread crossing zero, a time limit, a stop-loss, or a reverse signal.

State-space methods act on the spread directly: dynamic hedge ratios, conditional probabilities that the spread crosses its mean within k steps ([[sources/moura-2016-pairs-trading-kalman|de Moura et al. 2016]]), regime-change detection in the reversion itself ([[sources/triantafyllopoulos-2011-mean-reverting-spreads|Triantafyllopoulos & Montana 2011]]), and heteroscedasticity-aware position sizing ([[sources/zhang-2021-pairs-general-ssm|Zhang 2021]]).

## The Credit Spread

The other sense is the yield a risky bond pays above the risk-free rate. That is a different object with its own term structure — see [[concepts/credit-spread-curve|Credit Spread Curve]] and [[concepts/z-spread|Z-Spread]]. A third, narrower use is the bid-ask spread, which appears here mainly as a transaction cost and as a source of measurement bias.

## See Also

[[concepts/pairs-trading|Pairs Trading]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/cointegration|Cointegration]] · [[concepts/statistical-arbitrage|Statistical Arbitrage]] · [[concepts/kalman-filter|Kalman Filter]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/z-spread|Z-Spread]]

**Not yet written:** `concepts/hedge-ratio`, `concepts/half-life`, `concepts/ornstein-uhlenbeck-process`, `concepts/bid-ask-spread`

<!-- AUTHORED REGION END -->
