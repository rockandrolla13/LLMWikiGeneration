---
title: "Why Do ETF Flows Move Prices?"
page_id: sources/chao-2019-etf-flows-prices
page_type: source
source_type: report
revision_id: 1
created: 2026-05-06T23:30:00Z
updated: 2026-05-06T23:30:00Z
authors: [Alex Chao, Ronnie Shah, Hallie Martin, Shuan Wei, Jessica Zhang]
year: 2019
venue: Deutsche Bank Quantitative Strategy Research
tags: [etf-flows, flow-decomposition, index-reconstitution, allocation-flows, weight-reconstitution, contraflow, return-predictability]
related: [concepts/etf-flows, concepts/flow-decomposition, concepts/index-reconstitution, sources/petit-2025-data-driven-flow-etf, sources/optiver-2025-corporate-bond-etf-contraflow]
mind_map_priority: high
---

# Why Do ETF Flows Move Prices?

**Authors:** Alex Chao, Ronnie Shah, Hallie Martin, Shuan Wei, Jessica Zhang

**Year:** 2019

**Venue:** Deutsche Bank Securities - The Quant View

**Date:** May 9, 2019

## Summary

This research decomposes ETF flows into three components: (i) allocation, (ii) weight reconstitution, and (iii) index reconstitution. The analysis reveals that the "ETF Contraflow effect" (positioning against ETF flows) is largely driven by index reconstitution, with weight reconstitution contributing in recent years. Allocation flows show less consistent impact on stock prices.

## Key Contributions

### 1. ETF Flow Decomposition
- **Allocation flows**: Investor allocation changes to ETFs (frequent, small, affect many stocks)
- **Weight reconstitution flows**: Periodic rebalancing for non-cap-weighted indices (periodic, variable size, many stocks)
- **Index reconstitution flows**: Stock additions/deletions from indices (periodic, variable size, few stocks)

### 2. Variance Decomposition
- Over entire sample: Allocation (29%), Index reconstitution (45%), Weight reconstitution (25%)
- Allocation flows spike during market stress periods
- Index reconstitution larger in H2 vs H1
- Weight reconstitution increased substantially (39% of recent variation)

### 3. ETF Contraflow Strategy Performance
- Long: Bottom decile (largest ETF outflow)
- Short: Top decile (largest ETF inflow)
- Strong performance in 2009 and recent 5 years
- Sharpe ratio: 1.29 (Jan 2006 - Dec 2018)
- 6-month window focus for more recent flows

### 4. Return Attribution
- Index reconstitution: Primary driver of contraflow effect
- Weight reconstitution: Secondary driver (increasing in recent years)
- Allocation flows: Less consistent price impact evidence

## Data and Methods

- Russell 3000 stocks sorted into deciles by 6-month ETF flow
- Sector-neutral equal-weight long-short portfolios
- Sample: January 2006 - December 2018
- ETF flow = (Dollar change in ETF ownership) / (Market cap)

## Key Claims

1. ETF flows are negatively related to expected returns
2. Index reconstitution is the dominant driver of the contraflow effect
3. Weight reconstitution effects have grown with smart-beta ETF popularity
4. Allocation flows have minimal systematic price impact

## See Also

- [[concepts/etf-flows|ETF Flows]]
- [[concepts/flow-decomposition|Flow Decomposition]]
- [[concepts/index-reconstitution|Index Reconstitution]]
- [[sources/petit-2025-data-driven-flow-etf|Petit et al. (2025) Data-Driven Flow Decomposition]]
- [[sources/optiver-2025-corporate-bond-etf-contraflow|Optiver (2025) Corporate Bond ETF Contraflow]]
