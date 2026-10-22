---
content_hash: sha256:6719c2ebcdccc233772eb90f857423aaf0d556e88391cfbb5cb6a0e3f559bb7a
created: 2026-05-06 23:35:00+00:00
mind_map_priority: medium
page_id: concepts/index-reconstitution
page_type: concept
related:
- concepts/etf-flows
- concepts/flow-decomposition
revision_id: 2
schema_version: 2
sources:
- sources/chao-2019-etf-flows-prices
- sources/optiver-2025-corporate-bond-etf-contraflow
- sources/bendor-2021-systematic-investing-in-credit
tags:
- etf
- index-investing
- passive-investing
- price-impact
- russell-reconstitution
title: Index Reconstitution
updated: '2026-10-22T15:27:29Z'
updated_by: op_955147eb8c65
uuid: 6e36961f-58a0-50e1-bd20-9a0b05dfb194
---

<!-- AUTHORED REGION START -->
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

## Sources

- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)
<!-- AUTHORED REGION END -->