---
content_hash: sha256:c46f99e369dc865c22423dcb2d79565e4de2017120a856414f7e87251ffeab5f
created: 2026-05-06 23:35:00+00:00
mind_map_priority: medium
page_id: concepts/index-reconstitution
page_type: concept
related:
- concepts/etf-flows
- concepts/flow-decomposition
revision_id: 5
schema_version: 2
sources:
- sources/chao-2019-etf-flows-prices
- sources/optiver-2025-corporate-bond-etf-contraflow
- sources/bendor-2021-systematic-investing-in-credit
- sources/marks-2001-safety-first-but-where
- sources/marks-2018-investing-without-people
- sources/marks-2023-fewer-losers-or-more-winners
- sources/marks-2017-there-they-go-again-again
- sources/marks-2017-yet-again
tags:
- etf
- index-investing
- passive-investing
- price-impact
- russell-reconstitution
title: Index Reconstitution
updated: '2026-11-21T02:50:17Z'
updated_by: op_5915427acbe6
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

## In Howard Marks's Memos

- [[sources/marks-2001-safety-first-but-where|Safety First . . . But Where?]] (2001)
- [[sources/marks-2018-investing-without-people|Investing Without People]] (2018)
- [[sources/marks-2023-fewer-losers-or-more-winners|Fewer Losers, or More Winners?]] (2023)
- [[sources/marks-2017-there-they-go-again-again|There They Go Again . . . Again]] (2017)
- [[sources/marks-2017-yet-again|Yet Again?]] (2017)
<!-- AUTHORED REGION END -->