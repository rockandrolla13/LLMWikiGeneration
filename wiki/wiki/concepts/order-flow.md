---
content_hash: sha256:96424b6641cc1d2f56869289c5d6c7c884821c6adf1e6817dc8781ac23ee53b1
created: 2026-08-06 00:00:00+00:00
mind_map_priority: high
page_id: concepts/order-flow
page_type: concept
related:
- concepts/long-memory
- concepts/limit-order-book
- concepts/hurst-exponent
- concepts/market-microstructure
- concepts/stylized-facts
- concepts/order-flow-imbalance
- concepts/metaorder
- concepts/square-root-law
- concepts/propagator-model
- concepts/price-impact
revision_id: 2
schema_version: 2
sources:
- sources/gould-2016-long-memory-fx
- sources/xu-2020-mlofi
- sources/koukorinis-stylized-facts
- sources/wang-2018-cross-responses
- sources/maitrier-2026-square-root-impact-framework
- sources/maitrier-2025-artificial-market-generator
tags:
- order-flow
- long-memory
- limit-order-book
- price-formation
- hurst-exponent
- market-microstructure
title: Order Flow
updated: '2026-08-13T00:00:00Z'
uuid: 7eb42b82-0296-55ab-bd0c-d12c2def1750
---

<!-- AUTHORED REGION START -->
# Order Flow

The stream of orders arriving at a market — market orders, limit orders and cancellations — together with their signs. Its central empirical property is that it is **persistent**: the sign of the next trade is predictable from the signs of previous ones, far further back than a random-walk model allows.

## Long Memory in Trade Signs

[[sources/gould-2016-long-memory-fx|Gould, Porter & Howison (2016)]], on FX spot from a major electronic platform:

- Hurst exponent **H ≈ 0.7** across three currency pairs.
- Estimated *within* single days, so the result is not an artefact of aggregating across trading days.
- Concatenating adjacent intra-day series gives no significant difference — memory persists across daily boundaries.
- Structural-break tests reject the alternative that apparent memory is caused by breaks.

[[sources/koukorinis-stylized-facts|Koukorinis, Peters & Germano (2022)]] treat this persistence as one of the core [[concepts/stylized-facts|stylized facts]], and examine it alongside dependence between arrival rates and price variations. See [[concepts/long-memory|Long Memory]] and [[concepts/hurst-exponent|Hurst Exponent]].

## Imbalance and Price Formation

Net order flow, not raw volume, is what moves price.

[[sources/xu-2020-mlofi|Xu, Gould & Howison (2020)]] extend scalar Order-Flow Imbalance to **Multi-Level OFI**, a vector measuring net flow across M price levels of the [[concepts/limit-order-book|limit order book]], counting limit arrivals, cancellations and market orders. On LOBSTER Nasdaq data (six stocks, 2016), adding deeper levels improved out-of-sample RMSE by 65–75% for large-tick and 15–30% for small-tick stocks. Ridge regression was needed; OLS over-fitted and understated deep levels.

## Why Persistence Matters

Correlated signs, rather than direct cross-impact, explain co-movement between stocks: [[sources/wang-2018-cross-responses|Wang & Guhr (2018)]] attribute roughly 90% of the cross-response to cross-stock sign correlation.

Two standard readings of sign persistence — order splitting by large traders, and herding — are not distinguished by the evidence collected here.

## Where the Long Memory Comes From

The persistence documented above has a proposed cause: **[[concepts/metaorder|metaorder]] splitting**. A large parent order worked over an hour emits same-signed children throughout, so a power-law distribution of parent sizes mechanically produces long-memory signs, with the tail exponents related by $\gamma = \mu - 1$ (Lillo, Mike & Farmer).

That would settle the splitting-versus-herding question this page leaves open — except that [[sources/maitrier-2026-square-root-impact-framework|Maitrier & Bouchaud (2025)]] reopen it. They show that with transient square-root impact, splitting alone gives **sub-diffusive** prices. Recovering diffusion requires the signs of *distinct* metaorders to be long-range correlated too. If that is right, herding in some form is doing part of the work after all.

For the measurement side of order flow, see [[concepts/order-flow-imbalance|Order Flow Imbalance]].

## Open Questions

- Does H ≈ 0.7 hold across asset classes, or is it specific to liquid FX and equities?
- Has the growth of algorithmic trading changed the persistence, as [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]] ask?

## See Also

[[concepts/long-memory|Long Memory]] · [[concepts/hurst-exponent|Hurst Exponent]] · [[concepts/limit-order-book|Limit Order Book]] · [[concepts/market-microstructure|Market Microstructure]] · [[concepts/stylized-facts|Stylized Facts]] · [[entities/martin-gould|Martin Gould]]

**Not yet written:** `concepts/price-formation`

<!-- AUTHORED REGION END -->