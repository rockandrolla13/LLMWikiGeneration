---
title: "Market Microstructure Noise"
page_id: concepts/market-microstructure-noise
page_type: concept
created: 2026-04-26T02:20:00Z
updated: 2026-04-26T02:20:00Z
tags: [market-microstructure, bid-ask-spread, TRACE, corporate-bonds, data-quality]
related: [concepts/trace-data, concepts/look-ahead-bias, sources/dickerson-2024-bond-pitfalls, entities/alexander-dickerson]
---

# Market Microstructure Noise (MMN)

## Definition

Market microstructure noise refers to deviations between observed transaction prices and true fundamental values, primarily caused by bid-ask bounce and other trading frictions. In corporate bonds, MMN is particularly severe due to lower liquidity compared to equities.

## Sources of MMN

### Bid-Ask Bounce
- Transaction prices alternate between bid and ask
- Creates artificial negative autocorrelation in returns
- Bid-ask averaged prices still contain bias

### Other Sources
- Discrete price changes
- Information asymmetry
- Dealer inventory effects
- Stale prices in illiquid bonds

## Impact on Bond Research

### Spurious Predictability
Price-based signals from month t-1 are mechanically linked to month t returns, creating false predictability.

### Affected Strategies
- **Short-term reversal**: Premium drops >90% after MMN correction
- **Credit spreads**: 50-65% reduction in premia
- **Yields and prices**: Significant bias in signals

### Example: Reversal Strategy
| Metric | Before MMN Correction | After MMN Correction |
|--------|----------------------|---------------------|
| Monthly Premium | 0.90% | ~0% |

## MMN Correction Methods

### Implementation Gap
Use end-of-month t-1 prices with beginning-of-month t prices to purge bid-ask bias.

### Quote-Based Data
Industry-grade dealer quote data (expensive) avoids transaction-based bias.

### Data Resources
- **openbondassetpricing.com**: MMN-corrected TRACE data
- **PyBondLab**: Open-source correction code

## Implications

1. Many published bond anomalies may be spurious
2. Price-based signals require careful handling
3. Ex-ante filtering essential (not ex-post)
4. Corporate bond market inherently noisier than equities

## Related Concepts

- [[concepts/trace-data|TRACE Data]]
- [[concepts/look-ahead-bias|Look-ahead Bias]]
- [[concepts/trade-classification|Trade Classification]]

## Sources

- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]
- [[sources/fedenia-2021-ml-trade-classifier|Fedenia et al. (2021)]]
