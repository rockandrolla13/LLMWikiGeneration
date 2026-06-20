---
title: The Long Memory of Order Flow in the Foreign Exchange Spot Market
page_id: sources/gould-2016-long-memory-fx
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Martin D. Gould
- Mason A. Porter
- Sam D. Howison
year: 2016
venue: Market Microstructure and Liquidity
tags:
- long-memory
- order-flow
- foreign-exchange
- market-microstructure
- hurst-exponent
- autocorrelation
related:
- concepts/long-memory
- concepts/order-flow
- concepts/hurst-exponent
- concepts/limit-order-book
- concepts/market-microstructure
mind_map_priority: high
schema_version: 2
uuid: aa018536-bade-5bd9-9132-1e30d5956566
content_hash: sha256:5421bc9f162f69f1fa11ad40bb329a38c9befb4bb9d9cdd37934a915c8f9ca03
---

<!-- AUTHORED REGION START -->
# The Long Memory of Order Flow in the Foreign Exchange Spot Market

**Authors:** Martin D. Gould, Mason A. Porter, Sam D. Howison

**Year:** 2016

**Venue:** Market Microstructure and Liquidity, Vol. 2, No. 1

**Institutions:** CFM-Imperial Institute, University of Oxford (Mathematical Institute, Oxford-Man Institute)

## Summary

This paper provides strong empirical evidence for long memory in order flow in the FX spot market. Using high-quality data from a major electronic trading platform, the authors find a Hurst exponent H ~ 0.7 across three currency pairs, rejecting the hypothesis that apparent long memory is an artifact of data aggregation across trading days.

## Key Contributions

### 1. Intra-day Long Memory Evidence
- Statistically stable estimation without aggregating across days
- High activity levels enable within-day analysis
- Hurst exponent H ~ 0.7 for all three currency pairs
- Results consistent across all trading days in sample

### 2. Cross-day Analysis
- Concatenated adjacent intra-day series
- No significant difference from intra-day results
- Long memory persists across daily boundaries
- Rejects Axioglou and Skouras (2011) criticism

### 3. Structural Break Tests
- Hypothesis: apparent long memory caused by structural breaks
- Alternative: true long memory process
- Tests reject structural break hypothesis
- Confirms genuine long-memory property

### 4. Methodological Rigor
- Multiple estimators employed for robustness
- Wide range of statistical techniques
- Comparison of different estimation approaches
- Single-estimator studies can be misleading

## Key Findings

1. Long memory in order flow is a robust empirical property
2. Hurst exponent H ~ 0.7 (significantly above 0.5)
3. Property persists within days and across daily boundaries
4. Not an artifact of data aggregation or structural breaks
5. FX market shows similar properties to equities markets

## Implications

- Present order flow correlated with distant future values
- Useful for forecasting applications
- Long-range autocorrelations may explain:
  - Price impact
  - Volatility patterns
  - Heavy-tailed return distributions
- Insights into trader decision-making processes

## Comparison with Other Markets

- First comprehensive FX market study (previous work focused on equities)
- FX market microstructure differs from equities
- Despite differences, similar long-memory properties observed
- Extremely high activity enables within-day estimation

## See Also

- [[concepts/long-memory|Long Memory]]
- [[concepts/order-flow|Order Flow]]
- [[concepts/hurst-exponent|Hurst Exponent]]
- [[concepts/limit-order-book|Limit Order Book]]

<!-- AUTHORED REGION END -->
