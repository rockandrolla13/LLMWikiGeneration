---
title: "The Global Credit Spread Puzzle"
page_id: sources/huang-2025-global-credit-spread-puzzle
page_type: source
created: 2026-04-26T01:45:00Z
updated: 2026-04-26T01:45:00Z
tags: [credit-spreads, structural-models, liquidity, corporate-bonds, merton-model]
authors: [Jing-Zhi Huang, Yoshio Nozawa, Zhan Shi]
year: 2025
journal: Journal of Finance
related: [concepts/credit-spread-puzzle, concepts/structural-models, concepts/bond-liquidity, entities/jing-zhi-huang]
---

# The Global Credit Spread Puzzle

## Summary

This landmark paper examines whether structural models can predict credit spreads in eight developed economies (Australia, Canada, France, Germany, Italy, Japan, UK, US) using global default data from 1970-2017 and security-level credit spread data from 1997-2017.

## Key Findings

- **Global Credit Spread Puzzle (GCSP)**: Standard structural models (Black-Cox, Collin-Dufresne-Goldstein) systematically underpredict investment-grade credit spreads in most developed markets
- **Japan Exception**: Japan is the only market where little evidence of CSP exists
- **Liquidity Solution**: The He-Milbradt model incorporating endogenous liquidity in secondary debt markets substantially mitigates the puzzle
- **Improved Fit**: Cross-sectional R² jumps from 19-35% (BC model) to 34-79% (HM model) across countries

## Methodology

- Uses Black-Cox (1976) model as baseline with flat default boundary
- Implements Collin-Dufresne-Goldstein (2001) model with stationary leverage
- Tests He-Milbradt (2014) variant with search and bargaining frictions
- Three alternative estimates of default boundary (d^FS, d^BGY, d^HNS)

## Key Concepts Introduced

- [[concepts/credit-spread-puzzle|Credit Spread Puzzle]] - structural models underpredict IG spreads
- [[concepts/structural-models|Structural Models]] - Merton-family bond pricing
- [[concepts/bond-liquidity|Bond Liquidity]] - OTC market frictions

## Notable Quotes

> "Once calibrated to historical default data and equity risk premia, standard structural models generate similar credit spreads and tend to substantially underpredict investment-grade corporate-Treasury spreads"

## Implications

1. Default risk alone insufficient to explain IG credit spreads
2. Liquidity component crucial for bond pricing models
3. Country-specific factors matter for credit spread analysis
4. Japan's unique position warrants further investigation

## Related Sources

- [[sources/dickerson-2023-bond-pitfalls|Dickerson et al. (2024)]] - microstructure issues
- [[sources/feng-2025-predicting-bond-returns|Feng et al. (2025)]] - ML bond prediction
