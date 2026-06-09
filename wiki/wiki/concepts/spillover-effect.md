---
created: 2026-04-26 02:25:00+00:00
page_id: concepts/spillover-effect
page_type: concept
related:
- concepts/asian-financial-crisis-1997
- concepts/bond-momentum
- concepts/dsge-threshold-bvar-counterfactual-analysis
- concepts/early-warning-indicators
- concepts/residual-momentum
- concepts/twin-crises
- sources/haesen-2017-momentum-spillover
revision_id: 2
tags:
- momentum
- spillover
- equities
- corporate-bonds
- cross-asset
title: Momentum Spillover Effect
updated: '2026-06-09T12:00:00Z'
---

# Momentum Spillover Effect

## Definition

Momentum spillover refers to the predictive power of equity momentum for corporate bond returns. Past stock winners tend to have future bond winners, reflecting the fundamental link between equity and debt of the same issuer.

## Mechanism

### Information Flow
1. Equity markets are more liquid and informationally efficient
2. Firm-level information is first incorporated into stock prices
3. Bond prices adjust with a lag
4. Equity momentum signals predict bond returns

### Economic Rationale
- Stocks and bonds share same underlying firm fundamentals
- Credit risk affects both securities
- Equity momentum captures improving firm prospects

## Empirical Evidence

Haesen, Houweling, and van Zundert (2017):

| Strategy | Sharpe Ratio | Max Drawdown |
|----------|--------------|--------------|
| Direct Bond Momentum | 0.45 | -60% |
| Equity Spillover | 0.55 | -80% |
| Residual Spillover | 0.65 | -30% |

## Types of Spillover

### Total Return Spillover
- Rank bonds by issuer's equity momentum
- Vulnerable to systematic risk exposure
- Large drawdowns in credit crises

### Residual Spillover
- Use idiosyncratic equity returns
- Removes market-wide movements
- [[concepts/residual-momentum|Residual Momentum]]
- Dramatically reduces drawdowns

## Risk Considerations

### Crisis Vulnerability
- 2008-2009: -80% drawdown for total spillover
- Equity bear markets often precede credit rallies
- Momentum reversal at market turning points

### Correlation with Factors
- Spillover loads on credit risk
- Time-varying default exposure
- Correlation with equity momentum factor

## Implementation

### Construction
1. Match bonds to issuing firm's equity
2. Calculate equity momentum (12-1 month)
3. Rank bonds by equity momentum
4. Long top quintile, short bottom quintile

### Holding Period
- 12-month holding typical
- Reduces turnover and transaction costs

## Related Concepts

- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/residual-momentum|Residual Momentum]]
- [[concepts/factor-investing|Factor Investing]]

## Sources

- [[sources/haesen-2017-momentum-spillover|Haesen et al. (2017)]]
- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/asian-financial-crisis-1997|asian-financial-crisis-1997]]
- [[concepts/dsge-threshold-bvar-counterfactual-analysis|dsge-threshold-bvar-counterfactual-analysis]]
- [[concepts/early-warning-indicators|early-warning-indicators]]
- [[concepts/twin-crises|twin-crises]]