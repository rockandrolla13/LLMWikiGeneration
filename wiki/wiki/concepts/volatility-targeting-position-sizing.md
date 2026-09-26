---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/volatility-targeting-position-sizing
page_type: concept
related:
- concepts/minimum-variance-portfolio
- concepts/value-at-risk
- concepts/volatility-targeting
- concepts/duration-times-spread
revision_id: 1
sources:
- sources/carver-2023-advanced-futures-trading-strategies
- sources/bendor-2007-dts
tags: []
title: Volatility-Based Position Sizing
updated: '2026-09-15T00:00:00Z'
updated_by: creditmacro-batch
schema_version: 2
uuid: 15ca38b6-681d-5f2c-9754-19911499c53f
content_hash: sha256:de100e0055ca3e06d09daec44e90a96aeb64a8af5e0f69ccb73c39a1840da6df
---

<!-- AUTHORED REGION START -->
# Volatility-Based Position Sizing

## Definition

A position-management methodology sizing each position so its expected risk contribution matches a target volatility, allowing heterogeneous strategies and instruments to be combined consistently.

## Forecasting Volatility for Credit

Sizing needs a volatility forecast. For corporate bonds, [[sources/bendor-2007-dts|Ben Dor et al. (2007)]] show that [[concepts/duration-times-spread|DTS]] times the historical volatility of relative spread changes gives near-unbiased excess-return volatility forecasts (normalised standard deviation 1.01). Forecasts based on absolute spread changes give 1.14 or 0.92, depending on the window. Because the DTS forecast uses the current spread, it adjusts immediately when spreads move.

## Sources

- [[sources/carver-2023-advanced-futures-trading-strategies|Advanced Futures Trading Strategies]]
- [[sources/bendor-2007-dts|DTS (Duration Times Spread) (2007)]]

## Related Concepts

- [[concepts/minimum-variance-portfolio|minimum-variance-portfolio]]
- [[concepts/value-at-risk|value-at-risk]]
- [[concepts/volatility-targeting|volatility-targeting]]
<!-- AUTHORED REGION END -->
