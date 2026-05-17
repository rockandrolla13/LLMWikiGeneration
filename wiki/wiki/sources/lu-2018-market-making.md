---
title: "Order-book modelling and market making strategies"
page_id: sources/lu-2018-market-making
page_type: source
source_type: preprint
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Xiaofei Lu, Frederic Abergel]
year: 2018
venue: arXiv preprint
tags: [market-making, limit-order-book, queue-reactive-model, non-markovian, high-frequency-trading, backtesting]
related: [concepts/limit-order-book, concepts/market-making, concepts/queue-reactive-model, sources/abergel-2017-algorithmic-trading-lob, entities/frederic-abergel]
mind_map_priority: high
---

# Order-book Modelling and Market Making Strategies

**Authors:** Xiaofei Lu, Frederic Abergel

**Year:** 2018

**Venue:** arXiv preprint (1806.05101)

**Institution:** CentraleSupelec

## Summary

This paper addresses the gap between theoretical optimal market-making strategies and practical implementation. It identifies important statistical properties of order-driven markets that advocate against purely Markovian models, then designs and compares market-making strategies using both simulation and backtesting on real data.

## Key Contributions

### 1. Queue-Reactive Model Analysis
- Extension of Huang et al. (2015) queue-reactive model
- Three regimes identified for queue sizes:
  - Small queues (<70): limit orders slightly dominate
  - Medium queues (70-300): equilibrium
  - Large queues (>300): cancellations dominate
- Unit order size limitation identified

### 2. Non-Markovian Features
- Event type matters beyond current state
- Different order types leading to the same state have different subsequent dynamics
- Key insight: the history of how we reached a state affects future behavior

### 3. Enhanced Order Book Models
- Model 1: Incorporates order size distributions
- Model 2: Tracks event type that led to current state
- Both models improve market-making performance

### 4. Backtesting Framework
- Uses Eurostoxx 50 futures data (June-November 2016)
- Large tick instrument with ~1 tick spread
- Out-of-sample validation

## Key Findings

1. Pure Markovian models fail to reproduce real market participant behavior
2. Non-Markovian features significantly improve strategy performance
3. Event-type conditioning is crucial for realistic simulation
4. Simple enhancements to queue-reactive model yield substantial gains

## Data Characteristics

- Eurostoxx 50 futures (large tick instrument)
- Average spread close to 1 tick
- Multiple-limit trades very rare (<0.5%)
- Focus on best bid/ask limits only

## Practical Implications

- Theoretical "optimal" strategies require model improvements
- Historical order type information should be incorporated
- Backtesting on real data essential for validation

## See Also

- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/market-making|Market Making]]
- [[concepts/queue-reactive-model|Queue-Reactive Model]]
- [[sources/abergel-2017-algorithmic-trading-lob|Abergel et al. (2017) Algorithmic Trading]]
