---
title: Bond CAPM
page_id: concepts/bond-capm
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- fixed-income
- asset-pricing
- factor-models
- risk-premium
sources:
- sources/dickerson-2023-bond-risk
related:
- concepts/factor-models
- concepts/liquidity-risk
- concepts/credit-spread-curve
mind_map_priority: high
schema_version: 2
uuid: 71771b3f-cac2-505c-8ef1-5cab67be2f9a
content_hash: sha256:7446dbc2b4ef7e87ba45ee84651a3bf762fd95d4ebe32d0fb7494793292d7a58
---

<!-- AUTHORED REGION START -->
# Bond CAPM

The Bond CAPM extends the Capital Asset Pricing Model framework to corporate bonds, examining whether systematic risk factors explain bond returns.

## Motivation

Unlike equities, corporate bond returns depend on:
- **Interest rate risk**: Duration exposure to rate changes
- **Credit risk**: Default and spread risk
- **Liquidity risk**: Transaction costs and market depth
- **Systematic factors**: Market-wide risk exposures

## Key Findings (Dickerson et al., 2023)

Traditional factor models fail to explain corporate bond risk premia:
- **Negative R²** in out-of-sample tests
- Factor exposures don't capture return variation
- Suggests missing risk factors or model misspecification

## Standard Specification

$$E[R_i] - R_f = \beta_{i,m}(E[R_m] - R_f) + \sum_k \beta_{i,k} \lambda_k$$

Where:
- $R_i$ = Bond return
- $R_m$ = Market return (equity or bond market)
- $\beta_{i,k}$ = Factor loadings
- $\lambda_k$ = Factor risk premia

## Common Factors Tested

| Factor | Description |
|--------|-------------|
| DEF | Default spread (Baa-Aaa) |
| TERM | Term spread (10y-1y) |
| MKT | Equity market excess return |
| SMB/HML | Fama-French equity factors |
| LIQ | Liquidity factor |

## Implications

- Bond pricing may be more issuer-specific than systematic
- Need for better bond-specific factors
- Liquidity effects may dominate credit effects

## See Also

- [[concepts/factor-models|Factor Models]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[sources/dickerson-2023-bond-risk|Corporate Bond Risk Factor Pricing (2023)]]

<!-- AUTHORED REGION END -->
