---
created: 2026-04-26 02:20:00+00:00
page_id: concepts/bond-momentum
page_type: concept
related:
- concepts/carry-rolldown
- concepts/cross-sectional-momentum
- concepts/ewmac-carry-trading-rules
- concepts/factor-investing
- concepts/momentum-trend-following
- concepts/residual-momentum
- concepts/spillover-effect
- concepts/style-premia
- concepts/trend-following
- sources/haesen-2017-momentum-spillover
- sources/houweling-2017-factor-investing
revision_id: 2
tags:
- momentum
- corporate-bonds
- factor-investing
- anomalies
title: Bond Momentum
updated: '2026-06-09T12:00:00Z'
---

# Bond Momentum

## Definition

Bond momentum refers to the tendency of corporate bonds with high past returns to continue outperforming bonds with low past returns. Unlike equity momentum, the effect is primarily documented in high-yield bonds, with investment-grade bonds showing weak or no momentum.

## Key Characteristics

### High-Yield vs Investment-Grade
- **High-Yield**: Strong momentum effect documented
- **Investment-Grade**: Weak or absent momentum
- **After MMN Adjustment**: IG shows weak reversal; NIG shows momentum

### Formation and Holding Periods
Typical implementation uses 12-month holding periods rather than 1-month (common in equities) to reduce turnover and transaction costs.

## Types of Bond Momentum

### Direct Bond Momentum
Ranking bonds on their own past returns

### Momentum Spillover
Past equity winners → future bond winners
- [[concepts/spillover-effect|Spillover Effect]]

### Residual Momentum
Using firm-specific (idiosyncratic) returns rather than total returns
- [[concepts/residual-momentum|Residual Momentum]]
- Dramatically reduces volatility and drawdowns

## Empirical Evidence

| Study | Finding |
|-------|---------|
| Jostova et al. (2013) | Momentum in high-yield bonds |
| Houweling & van Zundert (2017) | Significant alpha, 12-month holding |
| Haesen et al. (2017) | Residual momentum superior |
| Dickerson et al. (2024) | Some momentum spurious (MMN) |

## Risk Considerations

- Time-varying default risk exposure
- Vulnerable to equity bear → credit bull transitions
- 2009 drawdown of -80% for spillover strategy

## Related Concepts

- [[concepts/factor-investing|Factor Investing]]
- [[concepts/market-microstructure-noise|Market Microstructure Noise]]
- [[concepts/spillover-effect|Spillover Effect]]

## Sources

- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]]
- [[sources/haesen-2017-momentum-spillover|Haesen et al. (2017)]]
- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/carry-rolldown|carry-rolldown]]
- [[concepts/cross-sectional-momentum|cross-sectional-momentum]]
- [[concepts/ewmac-carry-trading-rules|ewmac-carry-trading-rules]]
- [[concepts/momentum-trend-following|momentum-trend-following]]
- [[concepts/style-premia|style-premia]]
- [[concepts/trend-following|trend-following]]