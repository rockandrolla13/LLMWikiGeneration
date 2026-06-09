---
authors:
- Robert Carver
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/carver-2015-systematic-trading
page_type: source
publication_date: '2015'
publication_venue: Harriman House
related:
- concepts/ewmac-carry-trading-rules
- concepts/forecast-scaling-and-combination
- concepts/law-of-active-management
- concepts/overfitting-backtesting
- concepts/robust-portfolio-optimisation
- concepts/systematic-trading-framework
- concepts/volatility-targeting
- entities/daniel-kahneman
- entities/harriman-house
- entities/robert-carver
revision_hash: sha256:65d1466519689a76d1ad0f34cd007e65c93375b4cfd48d506bf5eb32fded0fd0
revision_id: 1
source_hash: sha256:43e1066fe7c787c6d88324eba2c853dd0f7bcd0739dc57bc5d7551d0b17d0bf2
source_path: raw/creditmacro/Systematic Trading - A unique new method for designing
  trading and investing systems (Robert Carver) (z-library.sk, 1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- systematic-trading
- trend-following
- carry
- risk-management
- position-sizing
- portfolio-construction
- behavioral-finance
title: 'Systematic Trading: A unique new method for designing trading and investing
  systems'
updated: '2026-06-09T12:00:00Z'
updated_by: op_4e728a91977f
---

# Systematic Trading: A unique new method for designing trading and investing systems

**Authors:** Robert Carver · **Year:** 2015 · **Venue:** Harriman House · **Type:** book

## Summary

Robert Carver presents a complete, modular framework for designing systematic trading and investing systems for individuals and professionals. The central thesis is that human discretionary decision-making is undermined by cognitive bias, so financial decisions should be partly or fully systematised; crucially, the most valuable part of a system is not the price-prediction rules but the position-sizing and risk-management framework. The book is organised in four parts (Theory, Toolbox, Framework, Practice) and rescales every trading rule's output into a comparable 'forecast' (averaging absolute value 10, capped at +/-20), combines forecasts with weights, then converts the combined forecast into a position scaled to a fixed volatility target. Carver warns against over-fitting and unrealistic Sharpe expectations, citing the law of active management.

## Key Claims

1. The position-sizing and risk-management framework matters more than the price-forecasting rules; even discretionary traders should systematise risk management.
2. Volatility targeting: positions should be scaled so the portfolio targets a chosen annualised volatility, adjusted to recent estimated price volatility.
3. Trading-rule outputs should be rescaled into standardised forecasts averaging absolute value 10 and capped at +/-20, so heterogeneous rules become comparable.
4. Over-fitting is the dominant danger in back-testing; single-instrument back-tested Sharpe ratios of 2-3 are mirages.
5. Equal-weighting all rule variations typically outperforms selecting the apparently best variation each period.
6. The law of active management implies Sharpe ratio is proportional to the square root of the number of independent bets, so diversification raises achievable Sharpe.

## Questions Raised

- How should forecast weights and instrument weights be chosen when only short or noisy return histories are available?
- When is fully systematic forecasting preferable to a discretionary forecast placed inside the systematic framework?
- How much of the diversification benefit survives realistic time-varying correlations and trading costs?

## Concepts

- [[concepts/systematic-trading-framework|Modular Systematic Trading Framework]]
- [[concepts/volatility-targeting|Volatility Targeting]]
- [[concepts/forecast-scaling-and-combination|Forecast Scaling and Combination]]
- [[concepts/overfitting-backtesting|Over-fitting in Back-testing]]
- [[concepts/law-of-active-management|Law of Active Management]]
- [[concepts/robust-portfolio-optimisation|Robust Portfolio Optimisation]]
- [[concepts/ewmac-carry-trading-rules|EWMAC and Carry Trading Rules]]

## Entities

- [[entities/robert-carver|Robert Carver]]
- [[entities/daniel-kahneman|Daniel Kahneman]]
- [[entities/harriman-house|Harriman House]]

## Source

- **Path:** `raw/creditmacro/Systematic Trading - A unique new method for designing trading and investing systems (Robert Carver) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:43e1066fe7c787c6d...`