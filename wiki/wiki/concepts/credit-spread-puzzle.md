---
content_hash: sha256:cdf342da8da873a9beb42286e4a0eff90f17547ec7459d4e3e242adf035c6f34
created: 2026-04-26 02:20:00+00:00
page_id: concepts/credit-spread-puzzle
page_type: concept
related:
- concepts/baa-corporate-bond-spread
- concepts/banking-crisis-early-warning-indicators
- concepts/bond-liquidity
- concepts/cds-bond-basis
- concepts/corporate-bonds
- concepts/credit-default-swap-spread
- concepts/credit-hedge-ratios-equity-options
- concepts/credit-risk-premium
- concepts/credit-spread-changes
- concepts/credit-spread-curve
- concepts/credit-spread-forecasting
- concepts/merton-model
- concepts/option-implied-credit-information
- concepts/structural-models
- sources/huang-2025-global-credit-spread-puzzle
revision_id: 3
schema_version: 2
sources:
- sources/avramov-2007-changes-corporate-credit-spreads
- sources/cremers-2008-individual-stock-option-prices-credit-spreads
- sources/wang-2013-cds-spreads-variance-risk-premia
tags:
- credit-spreads
- structural-models
- Merton-model
- bond-pricing
- liquidity
title: Credit Spread Puzzle
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 682793b6-7cd9-5f31-9199-3f410c921991
---

<!-- AUTHORED REGION START -->
# Credit Spread Puzzle

## Definition

The credit spread puzzle refers to the empirical observation that structural credit risk models (Merton-family) systematically underpredict investment-grade corporate bond spreads. Default risk alone cannot explain observed spreads.

## The Puzzle

### What Models Predict
Standard structural models (Black-Cox, Collin-Dufresne-Goldstein) calibrated to historical defaults predict relatively low IG spreads.

### What We Observe
Actual investment-grade credit spreads are substantially higher than model-implied spreads.

### The Gap
The unexplained portion suggests additional risk factors or frictions beyond pure default risk.

## Geographic Evidence

Huang, Nozawa, and Shi (2025) document the puzzle across eight developed economies:

| Country | CSP Evidence |
|---------|-------------|
| Australia | Strong |
| Canada | Strong |
| France | Strong |
| Germany | Strong |
| Italy | Strong |
| UK | Strong |
| US | Strong |
| **Japan** | **Little/None** |

## Potential Explanations

### Liquidity
- OTC market search/bargaining frictions
- He-Milbradt model incorporates endogenous liquidity
- Substantially mitigates the puzzle (R² from 19-35% to 34-79%)

### Tax Effects
- Municipal bond spreads vs corporate spreads
- State tax differentials

### Jump Risk
- Rare but severe default events
- Fat-tailed distributions

### Recovery Rate Uncertainty
- Uncertain loss given default
- Time-varying recovery rates

## Model Performance

| Model | Cross-sectional R² |
|-------|-------------------|
| Black-Cox (baseline) | 19-35% |
| He-Milbradt (liquidity) | 34-79% |

## Japan Exception

Japan shows little evidence of the credit spread puzzle, warranting further investigation:
- Different corporate governance
- Unique banking relationships
- Market structure differences

## Related Concepts

- [[concepts/structural-models|Structural Models]]
- [[concepts/bond-liquidity|Bond Liquidity]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]

## Sources

- [[sources/wang-2013-cds-spreads-variance-risk-premia|Credit Default Swap Spreads and Variance Risk Premia]]
- [[sources/cremers-2008-individual-stock-option-prices-credit-spreads|Individual Stock-Option Prices and Credit Spreads]]
- [[sources/huang-2025-global-credit-spread-puzzle|Huang et al. (2025)]]
- [[sources/krishnan-2007-credit-spread-forecast|Krishnan et al. (2007)]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/avramov-2007-changes-corporate-credit-spreads]]
<!-- AUTHORED REGION END -->