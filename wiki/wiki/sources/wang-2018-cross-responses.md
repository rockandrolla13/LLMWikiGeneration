---
title: Microscopic Understanding of Cross-Responses Between Stocks
page_id: sources/wang-2018-cross-responses
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Shanshan Wang
- Thomas Guhr
year: 2018
venue: Market Microstructure and Liquidity
tags:
- price-impact
- cross-correlations
- trade-signs
- limit-order-book
- high-frequency
- stocks
related:
- concepts/price-impact
- concepts/cross-correlations
- concepts/limit-order-book
- concepts/market-microstructure
- sources/xu-2020-mlofi
mind_map_priority: high
schema_version: 2
uuid: 01142fc0-d0ea-5aa3-9d33-042bb92a69e7
content_hash: sha256:06463b01a3d0390e36a23ab7fd93eaa5fe1604d221286ac48d30458d2faccfcc
---

<!-- AUTHORED REGION START -->
# Microscopic Understanding of Cross-Responses Between Stocks

**Authors:** Shanshan Wang, Thomas Guhr

**Year:** 2018

**Venue:** Market Microstructure and Liquidity, Vol. 3, No. 2

**Institution:** University of Duisburg-Essen

## Summary

This paper develops a microscopic understanding of cross-responses between stocks by analyzing how a trade in one stock affects the price of another. The authors decompose cross-responses into self-impact and cross-impact components, showing that cross-responses primarily arise from correlated trade signs rather than direct cross-impact.

## Key Contributions

### 1. Two-Component Price Impact Model
- Decomposes price impact into self-impact and cross-impact
- Self-impact function G(τ) decays as power law ~τ^(-γ)
- Cross-impact function much smaller than self-impact
- Model: R_i(t,τ) = Σ_j [G_ij(τ) × ε_j(t) + cross-impact terms]

### 2. Trade Sign Correlators
- Same-stock correlator: correlated (positive autocorrelation)
- Cross-stock correlator: anti-correlated (negative cross-correlation)
- Sign correlations persist across hundreds of trades
- Long-memory in trade signs explains price dynamics

### 3. Cross-Response Decomposition
- Cross-response = self-impact × cross-sign-correlation + cross-impact × self-sign-correlation
- First term dominates: ~90% of cross-response
- Cross-impact contribution is minor
- Explains why stocks co-move despite trading independently

## Methodology

### Data
- TAQ database (NYSE)
- 96 highly liquid stocks
- Year 2008
- Trade-by-trade level analysis

### Key Definitions
- **Response function:** R_i(t,τ) = ⟨r_i(t+τ) × ε_i(t)⟩
- **Cross-response:** R_ij(t,τ) = ⟨r_i(t+τ) × ε_j(t)⟩
- **Trade sign ε:** +1 for buyer-initiated, -1 for seller-initiated
- **Impact function G_ij(τ):** Price change in stock i due to trade in stock j

### Analysis Framework
- Trade time (event time) analysis
- Sector-level aggregation
- Power-law fitting for decay exponents
- Statistical tests for significance

## Key Results

### Self-Impact Properties
- Power-law decay: G(τ) ~ τ^(-0.5)
- Universal across stocks
- Consistent with prior literature

### Cross-Impact Properties
- Much smaller than self-impact
- Decays faster than self-impact
- Often not statistically significant

### Trade Sign Correlations
| Correlator Type | Sign | Magnitude | Interpretation |
|-----------------|------|-----------|----------------|
| Same-stock | Positive | ~0.3 | Momentum in trading |
| Cross-stock | Negative | ~-0.1 | Competition/arbitrage |

### Decomposition Results
- Self-impact × cross-sign: ~90% contribution
- Cross-impact × self-sign: ~10% contribution
- Cross-responses explained by correlated order flow

## Implications

1. **Price Co-movement:** Stocks co-move primarily due to correlated trading, not direct price linkages
2. **Market Making:** Cross-hedging should account for trade sign correlations
3. **Execution:** Trading in correlated stocks affects prices beyond direct impact
4. **Risk Management:** Cross-correlations in returns trace back to order flow patterns

## Theoretical Framework

### Response Function Decomposition
```
R_ij(τ) = G_ii(τ) × C_ij(τ) + G_ij(τ) × C_ii(τ)
```
Where:
- G_ii = self-impact function
- G_ij = cross-impact function
- C_ij = cross-sign correlator
- C_ii = self-sign correlator

### Key Insight
Cross-responses are primarily a "spillover effect" of self-impact through correlated trading activity, rather than direct cross-market price impact.

## See Also

- [[concepts/price-impact|Price Impact]]
- [[concepts/cross-correlations|Cross-Correlations]]
- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/market-microstructure|Market Microstructure]]
- [[sources/xu-2020-mlofi|Xu et al. (2020) MLOFI]]

<!-- AUTHORED REGION END -->
