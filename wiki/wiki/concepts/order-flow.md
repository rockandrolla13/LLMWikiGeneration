---
title: Order Flow
page_id: concepts/order-flow
page_type: concept
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T17:35:34Z'
tags:
- order-flow
- long-memory
- limit-order-book
- price-formation
- hurst-exponent
- market-microstructure
sources:
- sources/gould-2016-long-memory-fx
- sources/xu-2020-mlofi
- sources/koukorinis-stylized-facts
- sources/wang-2018-cross-responses
related:
- concepts/long-memory
- concepts/limit-order-book
- concepts/hurst-exponent
- concepts/market-microstructure
- concepts/stylized-facts
mind_map_priority: high
schema_version: 2
uuid: 7eb42b82-0296-55ab-bd0c-d12c2def1750
content_hash: sha256:8452faa44779e4aeca5b550708e365dbc03c6fbfccd6eb76947b617da37b2cac
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

## Open Questions

- Does H ≈ 0.7 hold across asset classes, or is it specific to liquid FX and equities?
- Has the growth of algorithmic trading changed the persistence, as [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]] ask?

## See Also

[[concepts/long-memory|Long Memory]] · [[concepts/hurst-exponent|Hurst Exponent]] · [[concepts/limit-order-book|Limit Order Book]] · [[concepts/market-microstructure|Market Microstructure]] · [[concepts/stylized-facts|Stylized Facts]] · [[entities/martin-gould|Martin Gould]]

**Not yet written:** `concepts/order-imbalance`, `concepts/price-impact`, `concepts/price-formation`

<!-- AUTHORED REGION END -->
