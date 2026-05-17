---
title: "Index Reconstitution"
page_id: concepts/index-reconstitution
page_type: concept
revision_id: 1
created: 2026-05-06T23:35:00Z
updated: 2026-05-06T23:35:00Z
tags: [etf, index-investing, passive-investing, price-impact, russell-reconstitution]
sources: [sources/chao-2019-etf-flows-prices, sources/optiver-2025-corporate-bond-etf-contraflow]
related: [concepts/etf-flows, concepts/flow-decomposition]
mind_map_priority: medium
---

# Index Reconstitution

Index reconstitution refers to the periodic addition and deletion of securities from benchmark indices, creating predictable trading flows as passive funds adjust their holdings.

## Mechanism

When a security is **added** to an index:
- Tracking ETFs must buy the security
- Creates buying pressure regardless of price
- Temporary overvaluation relative to fundamentals

When a security is **deleted** from an index:
- Tracking ETFs must sell the security
- Creates selling pressure regardless of price
- Temporary undervaluation relative to fundamentals

## Economic Impact

### ETF Flow Contribution
- **45% of total ETF flow variance** (Chao et al. 2019)
- Larger in second half of year (Russell reconstitution in June)
- Affects relatively few stocks but with large magnitude

### Return Predictability
- **Strongest driver** of the ETF contraflow effect
- Deleted securities outperform additions post-reconstitution
- Effect persists for several months

## Key Examples

### Russell Reconstitution (June)
- Annual rebalancing of Russell 1000, 2000, 3000
- Largest predictable flow event in US equities
- Migration between Russell 1000 and 2000 creates cross-sectional effects

### S&P 500 Additions/Deletions
- Less frequent but larger individual impact
- Widely studied announcement effect

### Bond Index Reconstitution
- Monthly rebalancing for most bond indices
- Fallen angels (IG → HY) and rising stars (HY → IG)
- Creates contraflow opportunities in corporate bonds

## Trading Strategies

### Contraflow Strategy
- Long deleted securities, short added securities
- Profits from mean reversion after forced flows
- Sharpe ratio ~1.29 for equity contraflow (Chao et al.)

## See Also

- [[concepts/etf-flows|ETF Flows]]
- [[concepts/flow-decomposition|Flow Decomposition]]
- [[sources/chao-2019-etf-flows-prices|Chao et al. (2019)]]
- [[sources/optiver-2025-corporate-bond-etf-contraflow|Optiver (2025)]]
