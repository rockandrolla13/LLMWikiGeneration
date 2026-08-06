---
title: Factor momentum
page_id: concepts/factor-momentum
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [factor-momentum, momentum, asset-pricing, quant-equity, empirical-finance]
sources: [sources/ehsani-2022-factor-momentum-and-the-momentum-factor]
related: [concepts/cross-sectional-momentum, concepts/factor-timing, concepts/autocorrelation-time-series, concepts/momentum-trend-following]
mind_map_priority: medium
---

# Factor momentum

**Factor momentum** is the tendency of asset-pricing factor returns to be positively autocorrelated, so a factor's prior-year return predicts its next-month return. A time-series factor-momentum strategy goes long factors with positive prior-year returns and short those with negative returns; a cross-sectional version is long above-median and short below-median factors. The paper argues individual-stock momentum is an aggregation of these factor autocorrelations transmitted through dispersion in factor loadings.

## Overview

Ehsani and Linnainmaa document that most equity factors are positively autocorrelated: the average nonmomentum factor earns 6 bps/month after a losing year and 51 bps after a winning year. Trading factors on their own past returns therefore generates a robust strategy whose profits subsume standard, industry, intermediate, Sharpe-ratio, and residual momentum. Because stocks load on these factors with dispersed betas, the aggregation of factor autocorrelation reproduces individual-stock momentum, implying momentum is a dynamic factor-timing strategy rather than a distinct risk factor.

## Sources

- [[sources/ehsani-2022-factor-momentum-and-the-momentum-factor]] — introduces the concept, documents factor autocorrelation, and shows factor momentum subsumes the Carhart UMD factor and its variants.

## Related Concepts

- [[concepts/cross-sectional-momentum]]
- [[concepts/factor-timing]]
- [[concepts/autocorrelation-time-series]]
- [[concepts/momentum-trend-following]]
