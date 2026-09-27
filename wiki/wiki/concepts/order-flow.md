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
- sources/abdulkarim-2019-topics-market-microstructure
- sources/anantha-2024-forecasting-high-frequency-order-flow-imbalance
- sources/anantha-2025-event-time-anchor-selection-multi-contract
- sources/angstmann-2026-event-time-order-flow-memory-operational
- sources/angstmann-2026-non-unique-time-market-incompleteness
- sources/angstmann-2026-revisiting-trade-sign-long-memory-square
- sources/bechler-2017-order-flows-limit-order-book-resiliency
- sources/bozzetto-2026-fee-structure-order-flow-informativeness-cryptocurrency
- sources/cartea-2018-enhancing-trading-strategies-order-book-signals
- sources/chomei-2023-empirical-analysis-limit-order-book-modeling
- sources/corradi-2015-liquidity-crises-different-time-scales
- sources/coz-2024-when-cross-impact-relevant
- sources/deep-2025-binary-tree-option-pricing-under-market
- sources/dixon-2017-sequence-classification-limit-order-book-recurrent
- sources/dobrev-2025-order-flow-imbalances-amplification-price-movements
- sources/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered
- sources/eisler-2011-price-impact-order-book-events-market
- sources/eisler-2012-models-impact-all-order-book-events
- sources/evans-2002-order-flow-exchange-rate-dynamics
- sources/fabre-2025-learning-spoofability-limit-order-books-interpretable
- sources/ginebri-2008-order-dynamics-italian-treasury-security-wholesale
- sources/gontis-2023-discrete-q-exponential-limit-order-cancellation
- sources/hellermann-2026-event-based-limit-order-book-representations
- sources/hu-2026-neural-hidden-markov-model-adaptive-granularity
- sources/indriawan-2019-impact-us-stock-market-opening-price
- sources/jaddu-2023-combining-deep-learning-order-books-reinforcement
- sources/jeon-2026-when-does-order-flow-matter-state
- sources/jong-2026-order-book-dynamics-two-dimensional-exit
- sources/jonuzaj-2024-information-content-book-trade-order-flow
- sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
- sources/kijima-2016-svm-enhanced-filtering-model-limit-order
- sources/kolm-2023-deep-order-flow-imbalance-extracting-alpha
- sources/kuhrn-2014-calculating-probability-mid-price-increase-based
- sources/linna-2025-lobert-generative-ai-foundation-model-limit
- sources/lipton-2013-trade-arrival-dynamics-quote-imbalance-limit
- sources/lucchese-2024-short-term-predictability-returns-order-book
- sources/luo-2011-profitable-opportunities-around-macroeconomic-announcements-u
- sources/mertens-2021-liquidity-fluctuations-latent-dynamics-price-impact
- sources/miranda-2019-order-flow-dynamics-prediction-order-cancelation
- sources/mucciante-2022-estimation-high-dimensional-counting-process-without
- sources/mucciante-2023-estimation-order-book-dependent-hawkes-process
- sources/naviglio-2026-explainable-deep-learning-price-trade-dynamics
- sources/nittoor-2025-order-flow-filtration-directional-association-short
- sources/ntakaris-2020-mid-price-prediction-based-machine-learning
- sources/peng-2025-prediction-high-frequency-futures-return-directions
- sources/rahman-2024-hybrid-vector-auto-regression-neural-network
- sources/scheiber-2017-new-strategies-asset-classes-increased-performance
- sources/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent
- sources/shternshis-2023-price-predictability-ultra-high-frequency-entropy
- sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e
- sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability
- sources/takahashi-2025-returns-order-flow-imbalances-intraday-dynamics
- sources/vliet-2026-information-arrival-stochastic-clock-intraday-trading
- sources/wu-2012-information-content-euro-bund-futures-options
- sources/xu-2026-when-quotes-crumble-detecting-transient-mechanical
- sources/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional
- sources/zheng-2013-price-jump-prediction-limit-order-book
- sources/zheng-2022-order-flow-technical-analysis-neural-network
tags:
- order-flow
- long-memory
- limit-order-book
- price-formation
- hurst-exponent
- market-microstructure
title: Order Flow
updated: '2026-09-27T01:47:00Z'
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