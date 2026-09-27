---
content_hash: sha256:7a6a0b94f774dfe26661579c33c39f260abcda016bedf5a99ac4cbab2f3af1f3
created: 2026-09-27 01:47:00+00:00
mind_map_priority: medium
page_id: concepts/micro-price
page_type: concept
related:
- concepts/queue-imbalance
- concepts/bid-ask-spread
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/market-making
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
sources:
- sources/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure
- sources/bilokon-2023-transformers-versus-lstms-electronic-trading
- sources/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure
- sources/rola-2025-boltzmann-price-toward-understanding-fair-price
- sources/zhang-2019-deeplob-deep-convolutional-neural-networks-limit
tags:
- micro-price
- weighted-mid-price
- fair-value
- limit-order-book
- queue-imbalance
title: Micro-Price
updated: '2026-09-27T01:47:00Z'
uuid: d0734ef6-99ef-536b-8210-481d833b7033
---

<!-- AUTHORED REGION START -->
# Micro-Price

The micro-price is an estimate of the fair price of an asset at a given instant, built from the best bid and ask and the sizes resting at each. It adjusts the mid-price toward the side of the book that is more likely to be traded through next.

## Two forms

- **The weighted mid-price.** The bid and ask prices are averaged, each weighted by the size on the opposite side. A large bid size pulls the estimate toward the ask.
- **The micro-price proper.** The mid-price is adjusted by the expected next move, given the current spread and [[concepts/queue-imbalance|queue imbalance]]. It is built so that its expected future value equals its current value.

## Why it is used

The mid-price changes only when a quote changes, and ignores how much is resting at each quote. The micro-price moves as the queues change, so it responds earlier.

## How it is used

- As a reference price for valuing positions and measuring trading costs.
- As an input feature to price prediction models.
- As the centre around which a market maker sets quotes.

## Caveats

It uses only the top of the book unless deeper levels are added. It inherits the weakness of queue imbalance: resting sizes can be withdrawn. The weighted mid-price in particular can jump when the spread changes, which is one reason the second form was proposed.

## Sources in This Wiki

- [[sources/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure|Explainable Patterns in Cryptocurrency Microstructure]] (Bartosz Bieganowski, Robert Slepaczuk, 2026). Shows engineered order-book/trade features have similar SHAP importance and shapes across five cryptocurrencies of different market cap, and tests tradability through an October 2025 flash crash.
- [[sources/bilokon-2023-transformers-versus-lstms-electronic-trading|Transformers versus LSTMs for Electronic Trading]] (Paul Bilokon, Yitao Qiu, 2023). Compares LSTM- and Transformer-based models on high-frequency limit order book prediction tasks and introduces DLSTM, a decomposition-based LSTM that wins on price-movement classification and simulated trading profitability.
- [[sources/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure|Volatility Estimation in Agricultural Futures Markets: A Microstructure Approach]] (Xianglin Kong, 2025). Compares GARCH with a GARCH-X model using limit-order-book variables to forecast intraday volatility in lean hog and corn futures, testing whether book depth and spread help.
- [[sources/rola-2025-boltzmann-price-toward-understanding-fair-price|Boltzmann Price: Toward Understanding the Fair Price in High-Frequency Markets]] (Przemysław Rola, 2025). Derives a maximum-entropy 'Boltzmann price' from bid/ask volume imbalance and shows it can explain excess kurtosis and market impact better than mid-price benchmarks.
- [[sources/zhang-2019-deeplob-deep-convolutional-neural-networks-limit|DeepLOB: Deep Convolutional Neural Networks for Limit Order Books]] (Zihao Zhang, Stefan Zohren, Stephen Roberts, 2019). Introduces DeepLOB, a CNN plus Inception plus LSTM network that predicts short-horizon price direction from raw limit order book snapshots and tests it on FI-2010 and a year of LSE data.

## Related

- [[concepts/queue-imbalance|Queue Imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/market-making|market making]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
<!-- AUTHORED REGION END -->