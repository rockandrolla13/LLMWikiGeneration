---
title: "Residual Momentum"
page_id: concepts/residual-momentum
page_type: concept
created: 2026-04-26T02:25:00Z
updated: 2026-04-26T02:25:00Z
tags: [momentum, residual-returns, idiosyncratic, risk-management, corporate-bonds]
related: [concepts/bond-momentum, concepts/spillover-effect, sources/haesen-2017-momentum-spillover]
---

# Residual Momentum

## Definition

Residual momentum uses firm-specific (idiosyncratic) returns rather than total returns to construct momentum signals. By removing systematic risk exposure, residual momentum strategies achieve better risk-adjusted returns with significantly reduced drawdowns.

## Construction

### Step 1: Factor Regression
Regress individual returns on systematic factors:
```
R_i,t = α + β₁·MKT + β₂·TERM + β₃·CREDIT + ε_i,t
```

### Step 2: Extract Residuals
Use regression residuals (ε) as the momentum signal instead of total returns.

### Step 3: Rank and Form Portfolios
Rank securities by cumulative residual returns and form long-short portfolios.

## Advantages

### Reduced Drawdowns
| Strategy | Max Drawdown |
|----------|--------------|
| Total Momentum | -60% to -80% |
| Residual Momentum | -20% to -30% |

### Lower Volatility
- Removes systematic factor exposure
- More stable performance across regimes
- Less correlation with market conditions

### Better Risk-Adjusted Returns
- Higher Sharpe ratios
- Lower tail risk
- More consistent alpha

## Application to Bonds

### Direct Bond Residual Momentum
- Regress bond returns on duration and credit factors
- Use residuals for momentum ranking
- Reduces interest rate and credit beta exposure

### Residual Spillover (Equity → Bond)
- Use idiosyncratic equity returns
- Predict bond returns
- Best performing variant in Haesen et al. (2017)

## Performance Comparison

From Haesen et al. (2017):

| Strategy | Sharpe | Max DD | Skew |
|----------|--------|--------|------|
| Total Bond Mom | 0.45 | -60% | Negative |
| Residual Bond Mom | 0.55 | -25% | Neutral |
| Total Spillover | 0.55 | -80% | Negative |
| Residual Spillover | 0.65 | -30% | Neutral |

## Factor Models for Residualization

### For Equities
- Fama-French factors (MKT, SMB, HML)
- Carhart momentum factor
- Industry factors

### For Bonds
- Term structure factors
- Credit spread factors
- Liquidity factors

## Related Concepts

- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/spillover-effect|Momentum Spillover Effect]]
- [[concepts/factor-investing|Factor Investing]]

## Sources

- [[sources/haesen-2017-momentum-spillover|Haesen et al. (2017)]]
