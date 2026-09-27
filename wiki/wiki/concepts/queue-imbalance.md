---
content_hash: sha256:8ede5963f11676992013d550bb21ac59d773926e82af1f4abc0d933138d19a84
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/queue-imbalance
page_type: concept
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/micro-price
- concepts/event-clock
- concepts/mid-price-prediction
- concepts/bid-ask-spread
revision_id: 1
schema_version: 2
sources:
- sources/busetto-2023-continuous-time-modeling-financial-returns-based
- sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability
- sources/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order
- sources/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit
- sources/corradi-2015-liquidity-crises-different-time-scales
- sources/hu-2025-volatility-aware-temporal-transformer-intraday-risk
- sources/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes
tags:
- queue-imbalance
- order-book-imbalance
- limit-order-book
- price-prediction
- market-microstructure
title: Queue Imbalance
updated: '2026-09-27T01:47:00Z'
uuid: cf556465-1c76-5534-b5a0-fecba42fde48
---

<!-- AUTHORED REGION START -->
# Queue Imbalance

Queue imbalance compares the volume resting on the bid side of the order book with the volume resting on the ask side. In its simplest form it is the difference between the best bid size and the best ask size, divided by their sum. It is also called order book imbalance, depth imbalance or volume imbalance.

## What it measures

It is a snapshot of the state of the book. A large bid queue and a small ask queue mean the ask is more likely to be used up first, which would move the price up.

## How it differs from order flow imbalance

- Queue imbalance is a **state**. It is read from the book at one instant.
- [[concepts/order-flow-imbalance|Order flow imbalance]] is a **flow**. It is built from the changes to the book over a window.

The two carry related information, and a feature set often includes both.

## How it is used

- To predict the direction of the next price move.
- To predict the side of the next trade.
- To adjust the mid-price into a [[concepts/micro-price|micro-price]].
- To decide whether to post a limit order or cross the spread.

## Caveats

The signal is strongest when the spread is one tick wide and the queues are long. Resting orders can be cancelled before they trade, so a large queue is not a commitment. The measure can be extended to deeper levels of the book, and the sources here differ on how much those levels add.

## Sources in This Wiki

- [[sources/busetto-2023-continuous-time-modeling-financial-returns-based|Continuous-time modeling of financial returns based on Limit Order Book data]] (Riccardo Busetto, Simone Formentin, 2023). Proposes a new order-book imbalance regressor, Base Imbalance, and fits a continuous-time dynamical model on irregularly-spaced, price-change-triggered observations to predict short-term equity returns.
- [[sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability|Microstructural changes before Macroeconomic Announcements: Predictability of Economic Surprises in the U.S. market]] (Rita Dias Barreto Calçada, 2015). Tests whether pre-announcement order and depth imbalances (VPIN, DI) in S&P 500 and 10-year Treasury futures predict the sign of U.S. macroeconomic surprises.
- [[sources/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order|Hawkes-based cryptocurrency forecasting via Limit Order Book data]] (Raffaele Giuseppe Cestari, Filippo Barchi, Riccardo Busetto and others, 2023). Combines a Hawkes point-process model of limit order book event timing with a continuous-output-error model of the base-imbalance regressor to forecast cryptocurrency return signs and drive a trading strategy.
- [[sources/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit|Univariate Hawkes-based cryptocurrency forecasting via Limit Order Book data]] (Raffaele G. Cestari, Filippo Barchi, Riccardo Busetto and others, 2025). Predicts the timing of the next limit order book event with a univariate Hawkes process, then feeds that predicted timing into a continuous output error model to forecast cryptocurrency return sign and improve trading profit.
- [[sources/corradi-2015-liquidity-crises-different-time-scales|Liquidity crises on different time scales]] (Francesco Corradi, Andrea Zaccaria, Luciano Pietronero, 2018). Studies large price fluctuations in a limit order book, finding order-flow imbalance drives jumps at a 15-minute scale while static book depletion drives them at 30 seconds.
- [[sources/hu-2025-volatility-aware-temporal-transformer-intraday-risk|A Volatility-Aware Temporal Transformer for Intraday Risk Forecasting with Market Microstructure Signals]] (Zhiming Hu, 2025). Introduces a volatility-gated Transformer that uses order flow imbalance and depth-weighted spread to forecast intraday realized volatility, beating GARCH and LSTM baselines.
- [[sources/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes|Forecasting Bitcoin price movements using multivariate Hawkes processes and limit order book data]] (Davide Raffaelli, Raffaele Giuseppe Cestari, Daniele Marazzina and others, 2026). Compares two multivariate-Hawkes pipelines for forecasting BTC/USD mid-price return timing and sign from LOB events; the hybrid Hawkes-plus-continuous-time model beats the pure-Hawkes classifier on accuracy and profit.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/micro-price|Micro-Price]]
- [[concepts/event-clock|Event Clock]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[concepts/bid-ask-spread|bid ask spread]]
<!-- AUTHORED REGION END -->