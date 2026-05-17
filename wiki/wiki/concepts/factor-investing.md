---
title: "Factor Investing in Corporate Bonds"
page_id: concepts/factor-investing
page_type: concept
created: 2026-04-26T02:25:00Z
updated: 2026-04-26T02:25:00Z
tags: [factor-investing, corporate-bonds, quantitative-investing, size, value, momentum, low-risk]
related: [concepts/bond-momentum, concepts/credit-spread-curve, sources/houweling-2017-factor-investing]
---

# Factor Investing in Corporate Bonds

## Definition

Factor investing applies systematic, rules-based strategies to corporate bond markets, targeting persistent risk premia associated with specific characteristics. Unlike equities, bond factor investing must account for credit risk, interest rate sensitivity, and lower liquidity.

## Key Factors

### Size (Small Issuer)
- Small issuers earn premium over large issuers
- Measured by amount outstanding or issuer size
- 12-month holding periods typical

### Low-Risk
- Low-beta bonds outperform on risk-adjusted basis
- Measured by credit rating, duration, or beta
- Related to betting-against-beta phenomenon

### Value
- Cheap bonds (high spread relative to fundamentals) outperform
- Measured by spread vs. model-implied spread
- Credit spread deviation from curve

### Momentum
- Past winners continue outperforming
- Strong in high-yield, weak in investment-grade
- [[concepts/bond-momentum|Bond Momentum]]

## Empirical Evidence

| Factor | Monthly Alpha | Significance |
|--------|---------------|--------------|
| Size | 0.10-0.15% | Moderate |
| Low-Risk | 0.15-0.25% | Strong |
| Value | 0.20-0.30% | Strong |
| Momentum | 0.15-0.20% | High-Yield only |

## Implementation Considerations

### Transaction Costs
- Corporate bonds have higher transaction costs than equities
- 12-month holding periods reduce turnover
- Bid-ask spreads vary significantly by credit quality

### Data Quality
- [[concepts/trace-data|TRACE Data]] enables US research
- [[concepts/market-microstructure-noise|Market Microstructure Noise]] affects signals
- Look-ahead bias from bond filtering

### Multi-Factor Portfolios
- Factors have low correlations with each other
- Combined portfolios show improved Sharpe ratios
- Robeco research shows 0.5+ Sharpe achievable

## Related Concepts

- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/market-microstructure-noise|Market Microstructure Noise]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]

## Sources

- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]]
- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]
