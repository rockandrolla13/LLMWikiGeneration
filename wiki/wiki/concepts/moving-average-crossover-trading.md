---
title: Moving-Average Crossover Trading
page_id: concepts/moving-average-crossover-trading
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [quant-finance, futures, trend-following, moving-average, trading-strategy, technical-analysis]
sources: [sources/chen-2024-volume-price-product-factor]
related: [concepts/trend-following, concepts/momentum-trend-following, concepts/market-timing, concepts/contrarian-market-timing]
mind_map_priority: medium
---

# Moving-Average Crossover Trading

**Moving-Average Crossover Trading** is a rule-based trend-following system that opens and closes positions on golden-cross / death-cross events between short- and long-period moving averages; here generalized to multi-line comparisons among four VPPMA and two SMA lines whose periods are optimized to maximize annualized return.

## Overview

In Chen and Yuan's model, trading signals are not derived from a single fast-slow pair but from pairwise golden-cross and death-cross comparisons among six lines: four VPPMA lines and two SMA lines. The period parameters are chosen by scanning a large grid of permutations to minimize an overall loss function, which the authors treat as equivalent to maximizing annualized return. Notably, adding more lines does not monotonically help — a six-VPPMA combination outperformed a seven-line one — because the pairwise comparisons collapse onto the single pair with the minimum loss value.

## Sources

- [[sources/chen-2024-volume-price-product-factor]] — generalizes classic two-line crossover rules into an optimized six-line VPPMA/SMA signal set.

## Related Concepts

- [[concepts/trend-following]]
- [[concepts/momentum-trend-following]]
- [[concepts/market-timing]]
- [[concepts/contrarian-market-timing]]
