---
title: Request for Quotes
page_id: concepts/request-for-quotes
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- rfq
- market-microstructure
- corporate-bonds
- market-making
- otc-markets
sources:
- sources/fermanian-2017-md2c-corporate-bonds
- sources/gueant-2019-particle-filtering-bonds
related:
- concepts/market-microstructure
- concepts/market-making
- concepts/bond-liquidity
mind_map_priority: medium
schema_version: 2
uuid: 2fd0333a-a163-53fd-ae2d-6762e01caa6f
content_hash: sha256:f2aae68588f56f109b4473a652f3098df977953dfdbb57ee706b4a9a69e51b93
---

<!-- AUTHORED REGION START -->
# Request for Quotes

The trading protocol of a quote-driven market: a client asks a set of dealers for a price on a specific instrument, the dealers who choose to respond quote, and the client trades with one of them or with nobody. There is no order book. Corporate bonds trade this way.

## The Mechanics on MD2C Platforms

[[sources/fermanian-2017-md2c-corporate-bonds|Fermanian, Guéant & Pu (2017)]] model the process on multi-dealer-to-client platforms using roughly 209,000 buy and 272,000 sell RFQs from 2014–15. Clients on Bloomberg FIT may poll **up to six dealers**. Not every dealer polled answers — response probability is below one, and is modelled as binomial.

Each RFQ has a latent side and an observed side. Dealer quotes are modelled with a skew exponential power distribution — fat-tailed, asymmetric, spiky around the composite price — and normalised by the CBBT bid-to-mid spread. The client's **reservation value**, the price threshold above which they will not trade, is Gaussian and never observed. Both distributions are recovered by maximum likelihood from outcomes and cover prices.

The dealer's problem falls out of this: quote aggressiveness trades off against hit ratio, and the right trade-off depends on how many competitors were asked. See [[concepts/market-making|Market Making]].

## RFQs as Data

An RFQ that trades away is still information. [[sources/gueant-2019-particle-filtering-bonds|Guéant & Pu (2019)]] use exactly this for mid-price estimation: a traded-away RFQ is a **censored observation** — you learn the price was beaten, not what it was. Their five observation types are D2C buy, D2C sell, traded-away buy, traded-away sell, and D2D trade, with truncated Gaussian likelihoods for the censored ones.

This censoring is why they use particle filtering rather than a Kalman filter: Kalman handles linear observations, and a censored RFQ is not one.

## See Also

[[concepts/market-microstructure|Market Microstructure]] · [[concepts/market-making|Market Making]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/corporate-bonds|Corporate Bonds]] · [[concepts/sequential-monte-carlo|Sequential Monte Carlo]] · [[concepts/limit-order-book|Limit Order Book]] · [[entities/olivier-gueant|Olivier Guéant]]

**Not yet written:** `concepts/cover-price`, `concepts/hit-ratio`, `concepts/reservation-price`, `concepts/particle-filtering`

<!-- AUTHORED REGION END -->
