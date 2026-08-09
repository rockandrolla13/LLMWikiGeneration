---
created: 2026-04-26 02:25:00+00:00
page_id: concepts/residual-momentum
page_type: concept
source_path: markdown_output/ssrn_id2932937_code158781.md
related:
- concepts/bond-momentum
- concepts/spillover-effect
- concepts/style-premia
- sources/haesen-2017-momentum-spillover
revision_id: 2
tags:
- momentum
- residual-returns
- idiosyncratic
- risk-management
- corporate-bonds
title: Residual Momentum
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: a5b66ad3-9e58-5268-913b-27a594f2d184
content_hash: sha256:b96282114982590ace0916f3870733701d35e72cd4a1b4349b4d15bd8fd0829f
---

<!-- AUTHORED REGION START -->
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
| Total momentum spillover | 0.35 | -80% | 8.85% |
| Residual momentum spillover | **0.77** | **-25%** | **4.80%** |

Verified against the source document 2026-08-09. An earlier version of this table
reported Sharpe ratios of 0.45/0.55/0.65 and drawdowns of -60%/-30% for four
strategy variants; none of those figures appears in the paper, and the only 0.45
in it is a leverage statistic. The paper reports one comparison, the one above.

Hedging default risk *after* forming a total-momentum portfolio is less effective
than residualising before: volatility falls only to at most 6.17%, against 4.80%
for residual momentum spillover.

The winner-minus-loser portfolio has a Sharpe ratio of 0.42 in investment grade
and 0.44 in high yield. In IG it returns 1.73% per annum, or 14bp per month,
which the authors note is the same order as the 11bp per month in Gebhardt et al.
(2005) on 1973-1996 data — so their 1994-2013 result is an out-of-sample
confirmation. Across the full universe, decile Sharpe ratios fall monotonically
from 0.59 (winners) to 0.06 (losers), with annual alphas from 1.94% to -2.86%.

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

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/style-premia|style-premia]]
<!-- AUTHORED REGION END -->
