---
title: Algorithmic trading in a microstructural limit order book model
page_id: sources/abergel-2017-algorithmic-trading-lob
page_type: source
source_type: preprint
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Frederic Abergel
- Come Hure
- Huyen Pham
year: 2017
venue: arXiv preprint
tags:
- market-making
- limit-order-book
- stochastic-control
- high-frequency-trading
- markov-decision-process
- hawkes-processes
related:
- concepts/limit-order-book
- concepts/market-making
- concepts/hawkes-processes
- concepts/markov-decision-process
- sources/lu-2018-market-making
- entities/frederic-abergel
mind_map_priority: high
schema_version: 2
uuid: d0174cac-ad33-5007-be36-0f9efe8eafd1
content_hash: sha256:60082e00248072f982d47ea0140532b1ddb173894a855215bc196168687b6a6f
---

<!-- AUTHORED REGION START -->
# Algorithmic Trading in a Microstructural Limit Order Book Model

**Authors:** Frederic Abergel, Come Hure, Huyen Pham

**Year:** 2017

**Venue:** arXiv preprint (1705.01446)

**Institutions:** CentraleSupelec (MICS Laboratory), Paris 7 Diderot University (LPSM), CREST-ENSAE

## Summary

This paper proposes a microstructural modeling framework for optimal market-making in a FIFO limit order book. Order arrivals are modeled as point processes with state-dependent intensities. The framework uses Markov Decision Processes and dynamic programming to characterize optimal strategies, with numerical solutions via control randomization and quantization methods.

## Key Contributions

### 1. Microstructural Order Book Model
- Limit orders, market orders, and cancel orders modeled as point processes
- Intensities depend only on the current state of the order book
- High-dimensional but realistic from a microstructure perspective
- Extension to Hawkes processes with exponential kernel

### 2. Market Maker Optimization
- Market maker maximizes P&L penalized by inventory
- Strategies constrained to a compact control space
- Positions tracked by limit locations and queue ranks
- FIFO (First In First Out) matching rule

### 3. Theoretical Framework
- Piecewise Deterministic Markov Decision Process (PDMDP) formulation
- Value function characterized via fixed-point dynamic programming
- Analytical characterization of optimal strategies
- Connection to non-finite horizon MDP

### 4. Numerical Methods
- Control randomization combined with quantization
- Fast approximate nearest neighbors algorithms
- Computational tests on simulated order books
- Comparison with naive strategies

## Model Details

The order book is described by K limits on each side (bid and ask):
- Vectors (a_t, b_t) describe available shares at each limit
- Constant boundary conditions ensure book is never empty
- Order arrivals: market (M), limit (L), cancel (C) with corresponding intensities

## Applications

- Market making with constant/symmetric/asymmetric intensities
- State-dependent intensity models
- Inventory risk management

## Key Claims

1. Microstructural models better capture short-term order book behavior
2. PDMDP formulation is natural for order book dynamics
3. Quantization methods effectively handle high-dimensional state spaces
4. Optimal strategies significantly outperform naive approaches

## See Also

- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/market-making|Market Making]]
- [[concepts/hawkes-processes|Hawkes Processes]]
- [[concepts/markov-decision-process|Markov Decision Process]]
- [[sources/lu-2018-market-making|Lu & Abergel (2018) Order-book Modelling]]

<!-- AUTHORED REGION END -->
