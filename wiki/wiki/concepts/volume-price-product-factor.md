---
title: Volume-Price-Product Factor (VPPMA)
page_id: concepts/volume-price-product-factor
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [quant-finance, futures, trend-following, moving-average, volume-price, technical-analysis]
sources: [sources/chen-2024-volume-price-product-factor]
related: [concepts/trend-following, concepts/momentum-trend-following, concepts/directional-forecasting, concepts/market-timing]
mind_map_priority: medium
---

# Volume-Price-Product Factor (VPPMA)

**Volume-Price-Product Factor (VPPMA)** is a price-volume signal in which the closing price C_i is replaced by the product S_i = V_i * C_i (trading volume times close) inside a simple moving average, yielding the Volume-Price-Product Moving Average used for futures trend forecasting; distinct from Li's volume-weighted PVMA by dropping volume as a normalizing denominator weight.

## Overview

Chen and Yuan construct the VPPMA by substituting the volume-price product S_i = V_i * C_i directly into the standard simple moving average formula in place of the closing price. Unlike W. H. Li's price-volume moving average (PVMA), which uses volume as a normalizing denominator weight, the VPPMA keeps the raw product, arguing this makes the resulting line more sensitive to genuine market trends. In the paper the model uses four VPPMA lines alongside two ordinary SMA lines, whose periods are optimized so that the resulting crossover system maximizes annualized return across six Chinese commodity futures.

## Sources

- [[sources/chen-2024-volume-price-product-factor]] — introduces the VPP factor and the VPPMA as the paper's central trend-forecasting construct.

## Related Concepts

- [[concepts/trend-following]]
- [[concepts/momentum-trend-following]]
- [[concepts/directional-forecasting]]
- [[concepts/market-timing]]
