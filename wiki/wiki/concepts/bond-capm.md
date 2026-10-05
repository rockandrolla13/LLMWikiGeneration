---
content_hash: sha256:880cdac989c0260be1541050d0fdcaa94f19f010019b40035850fa10ee3081a5
created: 2026-04-25 22:00:00+00:00
mind_map_priority: high
page_id: concepts/bond-capm
page_type: concept
related:
- concepts/factor-models
- concepts/liquidity-risk
- concepts/credit-spread-curve
revision_id: 2
schema_version: 2
sources:
- sources/dickerson-2023-bond-risk
- sources/dickerson-2026-co-pricing-factor-zoo
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
tags:
- fixed-income
- asset-pricing
- factor-models
- risk-premium
title: Bond CAPM
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 71771b3f-cac2-505c-8ef1-5cab67be2f9a
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

## Sources

- [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|The Corporate Bond Factor Replication Crisis]]
- [[sources/dickerson-2026-co-pricing-factor-zoo|The Co-Pricing Factor Zoo]]
<!-- AUTHORED REGION END -->