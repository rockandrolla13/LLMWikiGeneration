---
title: Price-Volume Alpha
page_id: concepts/price-volume-alpha
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [price-volume, formulaic-alpha, statistical-arbitrage, mean-reversion]
sources: [sources/kakushadze-2015-101-formulaic-alphas]
related: [concepts/alpha-signal, concepts/mean-reversion, concepts/statistical-arbitrage, concepts/high-frequency-trading]
mind_map_priority: medium
---

# Price-Volume Alpha

**Price-Volume Alpha** is an alpha signal constructed predominantly from daily price and volume data (open, close, high, low, volume, vwap, close-to-close returns, and average daily dollar volume) rather than fundamental data, capturing short-horizon predictive patterns in market microstructure and technical variables.

## Overview

Nearly all of the 101 alphas cataloged by [[entities/zura-kakushadze|Zura Kakushadze]] are price-volume alphas, drawing on a small set of standardized daily inputs — open, close, high, low, volume, vwap, returns, and average daily dollar volume. Their short holding periods (roughly 0.6–6.4 days) reflect the fast-decaying, technical patterns such data captures. A handful of the signals augment price-volume inputs with fundamental or industry-classification data, but the core vocabulary is technical. This grounding in price and volume is what makes the signals broadly applicable and reproducible across liquid equity universes.

## Sources

- [[sources/kakushadze-2015-101-formulaic-alphas]] — its 101 alphas are built almost entirely from daily price-volume inputs.

## Related Concepts

- [[concepts/alpha-signal]]
- [[concepts/mean-reversion]]
- [[concepts/statistical-arbitrage]]
- [[concepts/high-frequency-trading]]
