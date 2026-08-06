---
title: Mean-reversion/momentum combination strategy
page_id: concepts/mean-reversion-momentum-combination-strategy
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [momentum, mean-reversion, trading-strategies, currency-strategy, sharpe-ratio]
sources: [sources/serban-2010-mean-reversion-momentum-fx]
related: [concepts/mean-reversion, concepts/cross-sectional-momentum, concepts/contrarian-market-timing, concepts/half-life-of-adjustment]
mind_map_priority: medium
---

# Mean-reversion/momentum combination strategy

**Mean-reversion/momentum combination strategy** is a parametric zero-investment strategy (Balvers-Wu) that jointly estimates a mean-reversion component and a momentum component of returns, forming a long-Max/short-Min portfolio from model-predicted returns; combining the two effects yields higher risk-adjusted returns than either pure strategy.

## Overview

The strategy models log values as the sum of a random-walk drift, a stationary [[concepts/mean-reversion|mean-reverting]] component (speed 1−d), and a [[concepts/cross-sectional-momentum|momentum]] term (strength q over J lags). Serban (2010) estimates the model on the first third of the sample, predicts each currency's return, then goes long the highest-expected-return currency (Max) and short the lowest (Min), holding for K months and rolling the estimation window forward. Because the two effects are negatively correlated (≈ −0.35), omitting either one biases the parameters — pure mean reversion inflates the [[concepts/half-life-of-adjustment|half-life]] from 45 to 124 months, and pure momentum understates q. In FX the combination strategy produces zero-investment returns of about 10–12% per year and Sharpe ratios roughly 2.5 times those of the equity version, beating both pure strategies and traditional FX benchmarks.

## Sources

- [[sources/serban-2010-mean-reversion-momentum-fx]] — ports the Balvers–Wu parametric combination strategy from equities to FX UIP deviations.

## Related Concepts

- [[concepts/mean-reversion]]
- [[concepts/cross-sectional-momentum]]
- [[concepts/contrarian-market-timing]]
- [[concepts/half-life-of-adjustment]]
