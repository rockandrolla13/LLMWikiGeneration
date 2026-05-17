---
title: "Multi-Level Order-Flow Imbalance in a Limit Order Book"
page_id: sources/xu-2020-mlofi
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Ke Xu, Martin D. Gould, Sam D. Howison]
year: 2020
venue: Market Microstructure and Liquidity
tags: [order-flow-imbalance, limit-order-book, price-formation, market-microstructure, ridge-regression, nasdaq]
related: [concepts/limit-order-book, concepts/order-flow, concepts/price-formation, concepts/market-microstructure, sources/gould-2016-long-memory-fx, entities/martin-gould]
mind_map_priority: high
---

# Multi-Level Order-Flow Imbalance in a Limit Order Book

**Authors:** Ke Xu, Martin D. Gould, Sam D. Howison

**Year:** 2020

**Venue:** Market Microstructure and Liquidity, Vol. 4, Nos. 3&4

**Institution:** Mathematical Institute, University of Oxford

## Summary

This paper extends the Order-Flow Imbalance (OFI) framework of Cont et al. (2014) by studying Multi-Level Order-Flow Imbalance (MLOFI) - a vector quantity measuring net order flow at multiple price levels in a limit order book. Using high-quality LOBSTER data for six Nasdaq stocks, the authors demonstrate that order-flow activity deep in the LOB significantly influences price formation, contrary to earlier conclusions.

## Key Contributions

### 1. MLOFI Framework
- Vector-valued extension of scalar OFI
- Captures net order flow at M price levels
- Includes limit order arrivals, cancellations, and market orders
- More complete picture of order-flow dynamics

### 2. Regression Methodology
- OLS regression produces weak statistical significance for deep levels
- Ridge regression reveals strong significance at all levels
- Evidence of OLS over-fitting for some stocks
- Out-of-sample validation critical for assessment

### 3. Empirical Findings
- Out-of-sample RMSE improves with additional price levels
- Large-tick stocks: 65-75% improvement
- Small-tick stocks: 15-30% improvement
- Order-flow deep in LOB materially impacts price formation

## Methodology

### Data
- LOBSTER database (Nasdaq)
- 6 stocks: AMZN, TSLA, NFLX (small-tick); ORCL, CSCO, MU (large-tick)
- Full year 2016
- Event-by-event LOB reconstruction
- Trading hours: 10:00-15:30 (excluding open/close)

### MLOFI Definition
For time interval (tk-1, tk]:
```
MLOFI_m(tk-1, tk) = Σ e_n^m
```
Where e_n^m captures changes in queue sizes at level m

### Regression Models
**OLS (baseline):**
```
ΔP = α + Σ β_m × MLOFI_m + ε
```

**Ridge regression (recommended):**
- Addresses multicollinearity between MLOFI components
- More stable parameter estimates
- Better out-of-sample performance

## Key Results

### OFI vs MLOFI Comparison
| Stock | OFI R² | MLOFI R² (M=10) | Improvement |
|-------|--------|-----------------|-------------|
| AMZN | ~65% | Higher | Significant |
| MU | ~65% | Higher | Significant |

### Stock Characteristics
| Stock | Mean Price | Spread | Tick Size |
|-------|-----------|--------|-----------|
| AMZN | $699.22 | 37 ticks | Small |
| MU | $14.16 | 1 tick | Large |

### Order-Flow Distribution
- Small-tick stocks: >50% order flow beyond level-1
- Large-tick stocks: ~70% at level-1 bid/ask
- Deep LOB activity more relevant for small-tick stocks

## Implications

1. **Price Formation:** Order-flow beyond best quotes materially impacts mid-price changes
2. **Market Making:** Consider deep LOB information for quote optimization
3. **Execution:** Multi-level order-flow predicts short-term price movements
4. **Model Design:** Ridge regression preferred over OLS for correlated inputs

## Comparison with Prior Work

### Cont et al. (2014)
- Concluded deep LOB has little influence
- Used OLS regression only
- TAQ data (less precise timestamps)

### This Paper
- Ridge regression reveals significant deep-level effects
- LOBSTER data (nanosecond precision)
- Out-of-sample validation prevents over-fitting conclusions

## See Also

- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/order-flow|Order Flow]]
- [[concepts/price-formation|Price Formation]]
- [[concepts/market-microstructure|Market Microstructure]]
- [[sources/gould-2016-long-memory-fx|Gould et al. (2016) Long Memory in FX]]
