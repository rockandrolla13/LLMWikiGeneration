---
title: "Credit Spread Puzzle"
page_id: concepts/credit-spread-puzzle
page_type: concept
created: 2026-04-26T02:20:00Z
updated: 2026-04-26T02:20:00Z
tags: [credit-spreads, structural-models, Merton-model, bond-pricing, liquidity]
related: [concepts/structural-models, concepts/bond-liquidity, sources/huang-2025-global-credit-spread-puzzle]
---

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

- [[sources/huang-2025-global-credit-spread-puzzle|Huang et al. (2025)]]
- [[sources/krishnan-2007-credit-spread-forecast|Krishnan et al. (2007)]]
