---
title: "Factor Models"
page_id: concepts/factor-models
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [asset-pricing, risk-management, portfolio-theory, quantitative-finance]
sources: [sources/dickerson-2023-bond-risk]
related: [concepts/bond-capm, concepts/liquidity-risk, concepts/credit-spread-curve]
mind_map_priority: medium
---

# Factor Models

Factor models decompose asset returns into systematic components (factors) and idiosyncratic noise, providing a framework for risk attribution and expected return estimation.

## General Form

$$R_i = \alpha_i + \sum_{k=1}^K \beta_{i,k} F_k + \epsilon_i$$

Where:
- $R_i$ = Asset return
- $\alpha_i$ = Unexplained return (alpha)
- $F_k$ = Factor returns
- $\beta_{i,k}$ = Factor loadings (sensitivities)
- $\epsilon_i$ = Idiosyncratic return

## Types of Factor Models

### Statistical Factors
- Extracted via PCA or similar methods
- No economic interpretation required
- Examples: Principal components of yield curve

### Fundamental Factors
- Based on observable characteristics
- Examples: Value, momentum, size, quality

### Macroeconomic Factors
- Economic variables as factors
- Examples: GDP growth, inflation, yield curve changes

## Applications in Fixed Income

| Application | Factors Used |
|-------------|--------------|
| Duration hedging | Key rate durations |
| Credit risk | Rating transitions, sector exposure |
| Relative value | Spread factors, curve factors |
| Risk budgeting | Factor contribution to tracking error |

## Challenges for Bonds

Corporate bond factor models face difficulties:
- Illiquidity creates stale pricing
- Default risk is jump risk, not continuous
- Issue-specific effects dominate
- Limited time series for individual bonds

## See Also

- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[sources/dickerson-2023-bond-risk|Corporate Bond Risk Factor Pricing (2023)]]
