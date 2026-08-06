---
title: Formulaic Alpha
page_id: concepts/formulaic-alpha
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [quantitative-trading, formulaic-alpha, statistical-arbitrage, alpha-signal]
sources: [sources/kakushadze-2015-101-formulaic-alphas]
related: [concepts/alpha-signal, concepts/automated-alpha-search, concepts/algorithmic-trading, concepts/statistical-arbitrage]
mind_map_priority: medium
---

# Formulaic Alpha

**Formulaic Alpha** is a quantitative trading signal expressed as an explicit mathematical formula that is simultaneously executable computer code, built from a fixed vocabulary of cross-sectional and time-series operators (rank, correlation, delta, delay, decay_linear, ts_rank, stddev, scale, signedpower, indneutralize) applied to standardized inputs. Formulaic alphas are contrasted with coded 'non-formulaic' alphas that are too complex to present in closed form.

## Overview

In *101 Formulaic Alphas*, [[entities/zura-kakushadze|Zura Kakushadze]] catalogs 101 such signals proprietary to [[entities/worldquant|WorldQuant LLC]], each written so the formula and the code coincide. The signals are assembled from a compact, fixed operator set applied to standardized price-volume inputs, which makes them fully reproducible and testable by readers. The paper distinguishes these transparent formulaic alphas from "non-formulaic" alphas whose logic is too complex to reduce to a closed-form expression. Because each alpha is compact and explicit, the set serves as a public reference for how modern quant signals are constructed.

## Sources

- [[sources/kakushadze-2015-101-formulaic-alphas]] — introduces and catalogs 101 formulaic alphas as explicit formulas that double as computer code.

## Related Concepts

- [[concepts/alpha-signal]]
- [[concepts/automated-alpha-search]]
- [[concepts/algorithmic-trading]]
- [[concepts/statistical-arbitrage]]
