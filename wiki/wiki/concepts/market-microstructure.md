---
content_hash: sha256:049f22ea4edb5a4ae96adafd3996e0cca48127f48e776e9b6e8813d7852a9f52
created: 2026-08-06 00:00:00+00:00
mind_map_priority: high
page_id: concepts/market-microstructure
page_type: concept
related:
- concepts/limit-order-book
- concepts/stylized-facts
- concepts/long-memory
- concepts/market-making
- concepts/fill-probability
- concepts/optimal-execution
- concepts/price-impact
- concepts/cross-impact
- concepts/order-flow-imbalance
- concepts/square-root-law
- concepts/metaorder
revision_id: 2
schema_version: 2
sources:
- sources/guillaume-1997-stylized-facts-fx
- sources/xu-2020-mlofi
- sources/wang-2018-cross-responses
- sources/lokin-2024-fill-probabilities
- sources/fermanian-2017-md2c-corporate-bonds
- sources/cont-2023-cross-impact-ofi
- sources/maitrier-2026-square-root-impact-framework
- sources/hu-2025-ofi-csi300-ou
tags:
- market-microstructure
- limit-order-book
- price-formation
- liquidity
- high-frequency
title: Market Microstructure
updated: '2026-08-13T00:00:00Z'
uuid: 32fd6571-1456-5608-972d-aaa16cdfce5e
---

<!-- AUTHORED REGION START -->
# Market Microstructure

The study of how prices form from the actual mechanics of trading — order arrival, the matching rules, dealer behaviour — rather than from equilibrium arguments over aggregate supply and demand. It is the level at which the [[concepts/stylized-facts|stylized facts]] of high-frequency data become visible.

## Why the Mechanics Matter

[[sources/guillaume-1997-stylized-facts-fx|Guillaume et al. (1997)]] found that below roughly 10–15 minutes the price process has distinct characteristics: quote arrival and spread dynamics become first-order effects, and returns show negative first-order autocorrelation from bid-ask bounce. Aggregated data hides this.

## Two Market Designs

The sources here cover both, and they behave differently.

**Order-driven** — a [[concepts/limit-order-book|limit order book]] matches orders by price-time priority.

- [[sources/xu-2020-mlofi|Xu, Gould & Howison (2020)]] show order flow *deep* in the book materially affects price formation, contrary to earlier conclusions. Out-of-sample RMSE improves as levels are added: 65–75% for large-tick stocks, 15–30% for small-tick. OLS understated this; ridge regression revealed significance at all levels.
- [[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]] model the book as state-dependent queueing systems, deriving [[concepts/fill-probability|fill probabilities]] at multiple levels via Laplace transforms and continued fractions.

**Quote-driven** — clients request quotes from dealers.

- [[sources/fermanian-2017-md2c-corporate-bonds|Fermanian, Guéant & Pu (2017)]] model the RFQ process on European corporate bond MD2C platforms (~209k buy and ~272k sell RFQs, 2014–15). Clients may poll up to six dealers; dealers trade off quote aggressiveness against hit ratio. The market remains quote-driven rather than order-driven. See [[concepts/market-making|Market Making]].

## Correlated Order Flow, Not Cross-Impact

[[sources/wang-2018-cross-responses|Wang & Guhr (2018)]] decompose cross-responses between stocks (TAQ, 96 liquid NYSE names, 2008). Self-impact decays as a power law; cross-impact is much smaller. Roughly 90% of the cross-response comes from **correlated trade signs**, not from one stock's trades directly impacting another. Stocks co-move because order flow is correlated.

## Impact at Three Scales

Price impact does not have one shape; it has a different one at each scale, and much apparent disagreement in this literature is scale confusion. See [[concepts/price-impact|Price Impact]] for the full table.

Briefly: at the level of book events, [[concepts/order-flow-imbalance|OFI]] against same-interval return is **linear** and explains 84–90% of variation out of sample. At the level of a [[concepts/metaorder|metaorder]], impact is **concave** — the [[concepts/square-root-law|square-root law]] — and decays after execution. These are reconciled by treating the linear aggregate relation as the shadow of many overlapping square-root-impact metaorders.

The Wang & Guhr finding above — that ~90% of cross-response comes from correlated trade signs rather than direct [[concepts/cross-impact|cross-impact]] — is independently corroborated by [[sources/cont-2023-cross-impact-ofi|Cont, Cucuringu & Zhang (2023)]] on different data and by a different route: once a stock's own book is integrated across depth, other stocks' order flow adds essentially nothing to explaining its contemporaneous return.

## Open Questions

- How far does the deep-book result in [[sources/xu-2020-mlofi|Xu et al. (2020)]] generalise beyond six Nasdaq names?
- Do quote-driven and order-driven venues share the same stylized facts, or only some?

## See Also

[[concepts/limit-order-book|Limit Order Book]] · [[concepts/stylized-facts|Stylized Facts]] · [[concepts/long-memory|Long Memory]] · [[concepts/market-making|Market Making]] · [[concepts/fill-probability|Fill Probability]] · [[concepts/optimal-execution|Optimal Execution]] · [[entities/martin-gould|Martin Gould]] · [[entities/olivier-gueant|Olivier Guéant]]

**Not yet written:** `concepts/price-formation`, `concepts/request-for-quotes`, `concepts/cross-correlations`

<!-- AUTHORED REGION END -->