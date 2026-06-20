---
title: RFQ Impact Pricing and Liquidity Dynamics
page_id: sources/bergault-2023-rfq-pricing
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- rfq
- market-making
- micro-price
- liquidity
- markov-modulated-poisson
- corporate-bonds
- otc
authors:
- Philippe Bergault
- Olivier Guéant
year: 2023
related:
- concepts/market-making
- concepts/rfq-markets
- concepts/micro-price
- entities/olivier-gueant
- entities/philippe-bergault
schema_version: 2
uuid: 37b3dc29-c08d-5f6e-a31a-102c5e684794
content_hash: sha256:a6d37bdffb7637d3524b86ef19a9ebfc3a8ead66d7284a176f4c4419ce2ca45f
---

<!-- AUTHORED REGION START -->
# RFQ Impact Pricing and Liquidity Dynamics

## Summary

This paper addresses the challenge of pricing illiquid securities in over-the-counter (OTC) markets based on **requests for quotes (RFQs)**. It extends the concept of micro-price from limit order book markets to RFQ markets and introduces a novel concept: the **Fair Transfer Price**.

## Key Innovations

### 1. Micro-price for RFQ Markets
Extending Stoikov's micro-price concept to RFQ settings where:
- Transaction prices are scarce
- Information comes from RFQ flow patterns
- Liquidity imbalances are common

### 2. Fair Transfer Price
A new concept representing the average between optimal bid and ask quotes when the market maker has zero inventory. This price accounts for current liquidity conditions and can be used for:
- Portfolio valuation
- Transfer pricing between desks
- Mark-to-market in illiquid markets

## Markov-Modulated Poisson Process (MMPP)

The key modeling innovation is using **bidimensional MMPPs** to capture:
- Time-varying liquidity at bid and ask
- Asymmetric flow patterns
- Liquidity regime changes

The intensity process $(\lambda_t^b, \lambda_t^a)$ is a continuous-time Markov chain with:
- Finite state space for each side
- Joint transitions capturing correlated liquidity shocks

## Mathematical Framework

**Price drift proportional to flow imbalance:**
When ask intensity exceeds bid intensity, the micro-price adjusts upward, and vice versa.

**Optimal quotes with MMPP:** Extension of Avellaneda-Stoikov framework where:
- Flow intensities are stochastic
- Market maker adjusts for liquidity regimes
- Quote skewing responds to imbalance

## EM Algorithm for Parameter Estimation

The paper provides a detailed EM algorithm for estimating:
- Intensity levels for each state
- Transition rates of the Markov chain
- Joint dynamics of bid/ask intensities

## Applications

- Corporate bond markets (especially European markets with limited transparency)
- Any OTC market with RFQ-based trading
- Portfolio valuation under illiquidity

## Related Sources

- [[sources/barzykin-2021-fx-dealer-tiers]] - Related market making framework

## Citation

Bergault, P., & Guéant, O. (2023). RFQ Impact Pricing and Liquidity Dynamics.

<!-- AUTHORED REGION END -->
