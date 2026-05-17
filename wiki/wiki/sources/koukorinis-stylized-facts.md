---
title: "Revisiting stylised facts: information clock, persistence, long memory and dependence"
page_id: sources/koukorinis-stylized-facts
page_type: source
source_type: working-paper
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Andreas Koukorinis, Gareth W. Peters, Guido Germano]
year: 2022
venue: Working Paper
tags: [stylized-facts, high-frequency-trading, mfdfa, information-clock, long-memory, copulas, futures-markets, cryptocurrency]
related: [concepts/stylized-facts, concepts/information-clock, concepts/long-memory, concepts/mfdfa, concepts/copulas, sources/guillaume-1997-stylized-facts-fx, entities/gareth-peters, sources/aslam-2020-covid-mfdfa, sources/murphy-2006-order-flow-critique, entities/andreas-koukorinis, sources/koukorinis-2026-draci]
mind_map_priority: high
---

# Revisiting Stylised Facts: Information Clock, Persistence, Long Memory and Dependence

**Authors:** Andreas Koukorinis, Gareth W. Peters, Guido Germano

**Year:** 2022

**Venue:** Working Paper

**Institutions:** University College London, UC Santa Barbara

## Summary

This paper examines stylised empirical facts in price and volume processes across financial instruments including cryptocurrencies and futures. It focuses on persistence (long memory), arrival rates, and dependence using empirical copulas, applying kernel two-sample tests and MFDFA analysis to data transformed using information clocks.

## Key Contributions

### 1. Information Clock Analysis
- Sampling based on trading activity rather than calendar time
- More natural for high-frequency microstructure
- Captures arrival of new information
- Uses subordinated processes (Bochner framework)

### 2. MFDFA Application
- Multi-fractal detrended fluctuation analysis
- Derives quantities for time-varying inefficiency detection
- Central element of the empirical study
- Applied across different information clock transformations

### 3. Kernel Two-Sample Testing
- Compares distributions across days
- Tests information clock transformations
- Compares across instruments of same asset class
- Detects systematic differences in data distributions

### 4. Empirical Findings
- Long-memory (persistence) in order flow
- Dependence between arrival rates and price variations
- Analysis of futures markets (largely unexplored previously)
- Cryptocurrency market comparison

## Methodology

### Subordinated Processes
- Subordinator Q(t): right-continuous non-decreasing process
- Independent and homogeneous increments
- Transforms calendar time to information time
- W(Q(t)) as composite process

### Key Variables Analyzed
- Price changes distribution
- Realised variance and bi-power variation
- Inter-arrival rates and volumes
- Order imbalance
- Persistence of trade flow

## Key Questions Addressed

1. Can we identify the same phenomena across different markets?
2. Has behavior changed with increased algorithmic trading?
3. Do similar phenomena exist in cryptocurrency markets?
4. Can information clocks create more stable/stationary quantities?

## Contributions Summary

1. Use MFDFA for time-varying short-term inefficiencies
2. Apply kernel methods across transformed data
3. Categorize stylised facts in terms of long-memory
4. Test memory/persistence concepts in futures markets
5. Examine relationship between trade sizes, arrival rates, and returns using copulas

## See Also

- [[concepts/stylized-facts|Stylized Facts]]
- [[concepts/information-clock|Information Clock]]
- [[concepts/long-memory|Long Memory]]
- [[concepts/mfdfa|MFDFA]]
- [[concepts/copulas|Copulas]]
- [[sources/guillaume-1997-stylized-facts-fx|Guillaume et al. (1997) Stylized Facts]]
- [[sources/aslam-2020-covid-mfdfa|Aslam et al. (2020) COVID-19 MFDFA]]
- [[sources/murphy-2006-order-flow-critique|Murphy & Izzeldin (2006) Transaction Clock Critique]]
- [[entities/andreas-koukorinis|Andreas Koukorinis]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper (2026)]]
