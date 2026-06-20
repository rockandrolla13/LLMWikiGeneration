---
title: Multi-scale Representation of High Frequency Market Liquidity
page_id: sources/golub-2014-multiscale-liquidity
page_type: source
source_type: preprint
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Anton Golub
- Gregor Chliamovitch
- Alexandre Dupuis
- Bastien Chopard
year: 2014
venue: arXiv preprint
tags:
- market-microstructure
- liquidity
- information-theory
- high-frequency-trading
- intrinsic-time
- foreign-exchange
related:
- concepts/intrinsic-time
- concepts/directional-change
- concepts/market-liquidity
- concepts/limit-order-book
- entities/anton-golub
- sources/murphy-2006-order-flow-critique
- sources/koukorinis-stylized-facts
- concepts/stylized-facts
mind_map_priority: high
schema_version: 2
uuid: 900f970b-dd00-5198-b73d-d05dff36a656
content_hash: sha256:131d71489f89da654e2e27b780087c86972f3c64fb97ed2b3deb98bc4fd191b5
---

<!-- AUTHORED REGION START -->
# Multi-scale Representation of High Frequency Market Liquidity

**Authors:** Anton Golub, Gregor Chliamovitch, Alexandre Dupuis, Bastien Chopard

**Year:** 2014

**Venue:** arXiv preprint (1402.2198)

**Institutions:** Olsen Ltd, University of Geneva

## Summary

This paper introduces an event-based framework using directional changes and overshoots to analyze high-frequency market data. The approach maps continuous financial data into an "Intrinsic Network" - a state-based discretization that enables multi-scale analysis. An information-theoretic liquidity measure is proposed that can detect and predict market stress.

## Key Contributions

### 1. Intrinsic Time Framework
- Moves away from physical (clock) time to event-based time
- Uses directional changes (price reversals of threshold delta) as natural dissection points
- Overshoots continue the trend until the next directional change
- Multiple thresholds can be applied simultaneously for multi-scale analysis

### 2. Fundamental Intrinsic Theorem
For Brownian motion price processes:
- Expected overshoot length E[omega] equals the directional change threshold delta
- This relationship is completely insensitive to volatility
- Establishes a scaling law between overshoot length and threshold

### 3. Intrinsic Network
- State-based discretization of price trajectory movement
- Consistent hierarchical structure allowing multi-scale analysis
- Modeled as a multi-scale Markov chain

### 4. Information-Theoretic Liquidity Measure
- Characterizes the "unlikeliness" of price trajectories
- Based on transition probabilities in the intrinsic network
- Can detect and predict stress in financial markets
- Acts as an early warning signal

## Empirical Applications

- 2007 Yen carry trade unwind
- Swiss National Bank August 2011 intervention (EUR/CHF floor at 1.20)
- Foreign Exchange market analysis

## Key Claims

1. Traditional liquidity measures (volume-based, spread-based) are insufficient
2. Event-based intrinsic time better captures market microstructure
3. Long overshoots indicate liquidity stress
4. The intrinsic network has consistent multi-scale properties
5. Maximum Entropy Principle can determine optimal scale choices

## Methodology

- Directional change detection algorithm
- State contraction for multi-scale analysis
- Markov chain modeling of state transitions
- Information entropy calculations

## See Also

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/directional-change|Directional Change]]
- [[concepts/market-liquidity|Market Liquidity]]
- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/stylized-facts|Stylized Facts]]
- [[sources/murphy-2006-order-flow-critique|Murphy & Izzeldin (2006) Transaction Clock Critique]]
- [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022) Stylized Facts]]

<!-- AUTHORED REGION END -->
