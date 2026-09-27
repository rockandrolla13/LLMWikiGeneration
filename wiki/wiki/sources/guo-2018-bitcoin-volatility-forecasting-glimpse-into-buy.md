---
authors:
- Tian Guo
- Albert Bifet
- Nino Antulov-Fantulin
content_hash: sha256:6a9b4f50fa27d8d4db7be681d3a3b7179bf9e6ae856c4bf5989936172a1acf00
created: 2026-09-27 01:47:00+00:00
page_id: sources/guo-2018-bitcoin-volatility-forecasting-glimpse-into-buy
page_type: source
related:
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/lstm-networks
- concepts/recurrent-neural-networks
revision_id: 1
schema_version: 2
source_hash: sha256:5e4263da966ab45f716e2b517b1921782c4dc841777594faca2cdf143044d27e
source_path: markdown_output/guo-2018-bitcoin-volatility-forecasting-glimpse-into-buy.md
source_type: paper
tags:
- bitcoin
- volatility-forecasting
- order-book-features
- mixture-of-experts
- cryptocurrency
- interpretable-models
- time-series-forecasting
- clock-calendar
- asset-crypto
- harvest-relevant
title: Bitcoin Volatility Forecasting with a Glimpse into Buy and Sell Orders
updated: '2026-09-27T01:47:00Z'
uuid: 9d3acca7-1d93-55ee-ac44-c83b11bfd24c
year: 2018
---

<!-- AUTHORED REGION START -->
# Bitcoin Volatility Forecasting with a Glimpse into Buy and Sell Orders

## Summary

The paper studies short-term Bitcoin volatility forecasting using both the history of realized volatility and order-book data (buy and sell orders), motivated by the idea that order-book activity reflects market intention and is closely tied to how volatility evolves. It notes that while many studies examine Bitcoin's economic or statistical properties, few use order-book data directly for forecasting, and that simple feature-concatenation approaches used elsewhere in finance ignore how the influence of order-book information changes over time.

The proposed approach is a temporal mixture model: one component is an autoregressive model of past volatility, the other is a bilinear-regression model over a window of order-book features (spread, depth, volume, weighted spread, and bid/ask slope), and a data-dependent softmax gate learns how much weight to give each component at every point in time. Two variants are built, assuming the volatility is Gaussian or log-normal, and parameters are learned by alternately updating the gate and the component models under an L2-regularized likelihood objective. Models are evaluated with both a rolling (fixed trailing window) and an incremental (ever-expanding window) walk-forward scheme across monthly test intervals, to check robustness to how much training history is used.

The Gaussian mixture model (TM-G) is reported to outperform a wide range of statistical baselines (EWMA, GARCH, Beta-t-EGARCH, structural time series, ARIMA and their order-book-augmented ARIMAX/STRX variants) and machine-learning baselines (random forest, XGBoost, elastic net, Gaussian process regression, and a two-branch LSTM) across most monthly test intervals, and remains comparatively robust under both the rolling and incremental evaluation schemes. Simply adding order-book features to static models such as ARIMAX or STRX did not reliably beat their volatility-only counterparts, which the authors take as evidence that a static, always-on combination of the two data sources is not enough.

What is new is the gated, adaptive combination of the two data sources together with its interpretability: because the gate's weight is observable over time, the authors can point to specific periods where the order-book component dominates the prediction and relate this to features such as depth imbalance or bid/ask slope.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Realized volatility is computed and predicted on a fixed hourly calendar clock, defined as the standard deviation of Bitcoin returns within each hour. Order-book snapshots are collected on a fixed one-minute calendar clock via the exchange API and converted into a feature vector; each hourly volatility observation is paired with the trailing order-book feature window (empirically set to 30 minutes of history) that precedes it. The main prediction horizon is one hour ahead (one-step), with a separate 5-step-ahead (five-hour) example also reported.

## Data

- **Asset class:** Crypto
- **Instruments:** Bitcoin (BTC), exchanged against fiat currencies (USD, EUR, CNY) on a single exchange.
- **Venue:** OKCoin exchange
- **Period:** September 2015 to April 2017
- **Granularity:** Hourly realized-volatility observations (13730 in total) paired with order-book snapshots collected via the exchange API at one-minute granularity (701892 snapshots in total, with negligible gaps from API downtime); snapshots contained up to 1021 ask orders and 965 bid orders.

## Features and Measures

- **Spread.** The difference between the best bid price a buyer will pay and the best ask price a seller will accept.
- **Ask/Bid depth and depth difference.** The number of orders on the ask or bid side of the book, and the difference between the two.
- **Ask/Bid volume and volume difference.** The number of BTC on the ask or bid side, and the difference between the two.
- **Weighted spread.** The difference between the cumulative price over the top 10% of bid depth and the cumulative price over the top 10% of ask depth.
- **Ask/Bid slope.** The volume available up to a price offset from the current traded price, where the offset is set by the price level at which at least 10% of orders on that side lie further from the current price.

## Method

Volatility forecasting is framed as predicting the next (or D-step-ahead) hourly realized-volatility value from a window of past volatility observations plus a window of order-book-derived features. Two temporal mixture models are proposed, assuming volatility is Gaussian or log-normal: each has an autoregressive component over past volatility and a bilinear-regression component over the order-book feature matrix, combined by a softmax gating function whose own parameters (also autoregressive-plus-bilinear) are learned jointly with the component parameters by alternating minimization of an L2-regularized negative log-likelihood, with hinge-loss terms added in the Gaussian case to discourage negative predicted means.

Baselines include statistics-only models fit on volatility or returns alone (EWMA, GARCH, Beta-t-EGARCH, a structural time-series model, ARIMA) and machine-learning models fit on concatenated volatility-and-order-book features (random forest, extreme gradient boosting, elastic net, Gaussian process regression, a two-branch LSTM), plus ARIMAX/STRX variants that add order-book regression terms to ARIMA/STR. Models are compared by RMSE and MAE under a rolling (fixed trailing window) and an incremental (expanding window) walk-forward scheme across 12 monthly test intervals, with the rolling scheme using 3 months of prior data for training and validation; pairwise significance against the mixture model's errors is assessed with a two-sample Kolmogorov-Smirnov test. The learned gate values are also inspected directly over specific test periods to show when the order-book component dominates the prediction.

## Results

- The Gaussian temporal mixture model (TM-G) outperformed the other approaches in most of the 12 rolling test intervals and is reported to achieve up to 50% less error than baselines in some intervals.
- Adding order-book features to static models (ARIMAX, STRX) did not reliably improve on their volatility-only counterparts (ARIMA, STR); the paper states that simply adding order-book features does not necessarily improve performance.
- Testing sensitivity to the order-book lookback horizon (10 to 50 minutes) showed most models' errors changed little across this range, and longer horizons (e.g. 40 or 50 minutes) brought no further improvement for most models, while ARIMAX and STRX were prone to overfit with longer horizons.
- Under the incremental (expanding-window) evaluation, models such as ARIMA, ARIMAX and STRX showed a decreasing-then-increasing error pattern as training data grew, whereas LSTMs, TM-G and TM-LOG stayed comparatively robust across intervals.
- For 5-step-ahead prediction, TM-G continued to outperform the baselines, though all models had higher error than in one-step-ahead prediction.
- The dataset spans 13730 hourly volatility observations and 701892 order-book snapshots from OKCoin between September 2015 and April 2017; OKCoin's BTC trading volume during that period was approximately 40% of total traded BTC volume.
- Visualizing the mixture gate values showed the model shifting weight toward the order-book component in specific episodes, for example one driven by a negative market-depth feature and a wide bid/ask spread, and another driven by an imbalance between bid and ask slope.

## Limitations

- Single cryptocurrency (BTC) on a single exchange (OKCoin); the authors note the framework could be extended with other data sources (blockchain data, social media, other exchanges) but leave this to future work.
- The authors state they deliberately avoid deep-neural-network component models within the mixture framework because it is still difficult to read variable importance out of such models, even though a separate LSTM baseline is included for comparison.
- Full multi-step-ahead results are deferred to future work; only a 5-step-ahead example is shown here due to page limits, as stated by the authors.
- Reader note: statistical-significance markers in the results tables are computed against the mixture model's own error distribution (via a Kolmogorov-Smirnov test), so the reported significance emphasizes comparisons against the authors' model rather than all pairwise baseline comparisons.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]

## Citation

Tian Guo, Albert Bifet, Nino Antulov-Fantulin (2018). Bitcoin Volatility Forecasting with a Glimpse into Buy and Sell Orders.

DOI: 10.1109/icdm.2018.00123

Text ingested: `markdown_output/guo-2018-bitcoin-volatility-forecasting-glimpse-into-buy.md`, converted from `raw/ofi-event-clock/guo-2018-bitcoin-volatility-forecasting-glimpse-into-buy.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction, related work, the volatility/order-book data and problem formulation, both temporal mixture model formulations, the learning and evaluation methodology, all experiment sections and results tables (rolling, incremental, order-book horizon sensitivity, multi-step-ahead, model interpretation), the conclusion, and the reference list.

Known problems with the input: year not printed on this version; year_hint 2018 used; no journal or conference venue name is given anywhere in the converted markdown; several figures and inline equations were rendered as garbled or omitted picture placeholders in the markdown conversion; these were not used for any factual claims.
<!-- AUTHORED REGION END -->