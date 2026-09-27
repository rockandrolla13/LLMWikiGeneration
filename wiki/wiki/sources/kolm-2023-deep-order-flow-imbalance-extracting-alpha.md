---
authors:
- Petter N. Kolm
- Jeremy Turiel
- Nicholas Westray
content_hash: sha256:8c90dbebb461034d3513404fca276896acd85a7680eada87a815b8b48cf1e5de
created: 2026-09-27 01:47:00+00:00
page_id: sources/kolm-2023-deep-order-flow-imbalance-extracting-alpha
page_type: source
publication_venue: Mathematical Finance
related:
- concepts/event-clock
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/limit-order-book
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
- concepts/high-frequency-data
- entities/jeremy-turiel
revision_id: 1
schema_version: 2
source_hash: sha256:0fab98455276c82e1ddb532a8575ec0eff3e300a81cff3a53f08c38fbec2f368
source_path: markdown_output/kolm-2023-deep-order-flow-imbalance-extracting-alpha.md
source_type: paper
tags:
- order-flow
- limit-order-book
- deep-learning
- lstm
- high-frequency-trading
- alpha-forecasting
- multi-horizon
- nasdaq
- clock-event
- asset-equity
- harvest-core
title: 'Deep order flow imbalance: Extracting alpha at multiple horizons from the
  limit order book'
updated: '2026-09-27T01:47:00Z'
uuid: 823416a7-c83d-5d57-bcf6-a535f6377258
year: 2023
---

<!-- AUTHORED REGION START -->
# Deep order flow imbalance: Extracting alpha at multiple horizons from the limit order book

## Summary

The paper asks whether deep learning can extract short-horizon alpha from the most granular limit order book data, and how the choice of network architecture and input representation affects that predictability. It also asks why some stocks are easier to forecast than others.

Using nanosecond-timestamped order book updates from LOBSTER for 115 Nasdaq-listed stocks, the authors train six model types (a linear ARX benchmark, an MLP, a single LSTM, an LSTM feeding an MLP, a three-layer stacked LSTM, and a CNN-LSTM) separately for each stock, on either raw order-book states or a stationary order-flow transformation of them. Rather than a single-horizon classification task, each model outputs a 10-horizon vector of mid-price return forecasts, termed an alpha term structure, with horizons defined relative to a stock-specific characteristic time based on how often that stock's price actually moves. Models are trained and re-evaluated on a rolling basis across many months of data, and out-of-sample forecast accuracy is measured against an average-return benchmark.

The main finding is that, regardless of network architecture, models trained on order-flow inputs clearly and consistently outperform the same models trained on raw order-book states, and that once a model includes an LSTM component, the exact architecture (single LSTM versus deeper stacked or convolutional variants) matters comparatively little. Forecasting power builds up to roughly two average price changes ahead before declining, and cross-sectional regressions show that stocks with a higher ratio of order-book updates to price changes ('information-rich' stocks) are forecast more accurately.

What is new relative to earlier LOB deep-learning work is the reframing of the problem as multi-horizon regression rather than single-horizon classification, a much larger and non-downsampled dataset evaluated with genuine rolling out-of-sample testing, and the explicit link between forecasting accuracy and measurable market-microstructure characteristics of each stock, rather than a single pooled or 'universal' model across stocks.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each stock's model consumes the full irregularly spaced sequence of order book updates (every limit order arrival, market order, and cancellation, timestamped to nanosecond precision), using a lookback window of 100 past updates as input. The forecast target is a 10-horizon vector of mid-price returns, where each horizon is a multiple of a stock-specific time increment equal to the number of milliseconds in a trading day divided by the average number of non-zero tick-by-tick price changes that day, plus a 10 ms latency buffer, so the horizon adapts to each stock's own pace of price change rather than a fixed calendar interval.

## Data

- **Asset class:** Equities
- **Instruments:** 115 Nasdaq-listed stocks meeting Nasdaq-100 membership, minimum trading-day, and no-corporate-action criteria (e.g. Amazon, American Airlines, Facebook, Google, Microsoft, Netflix)
- **Venue:** Nasdaq (order book data sourced from LOBSTER)
- **Period:** January 1, 2019 through January 31, 2020 (January 9, 2019 excluded)
- **Granularity:** Full order-book depth for the top 10 non-empty bid and ask levels, updated at every order book event

## Features and Measures

- **Order book state (LOB).** The vector of bid and ask prices and share volumes for the top 10 non-empty levels of the limit order book at a given update time.
- **Order flow (OF).** A stationary transformation of two consecutive order book states into separate bid-side and ask-side flow vectors describing net additions, cancellations, and executions at each level, keeping bid and ask sides distinct.
- **Order flow imbalance (OFI).** The concatenated difference between bid and ask order flow, weighting both sides equally; a coarser version of order flow used in earlier work linking it to price changes.
- **Alpha term structure.** A 10-dimensional vector produced by each stock-level model giving mid-price return forecasts at ten increasing horizons, used to see how predictive strength builds and decays over time.
- **Stock-specific characteristic time increment.** A per-stock duration equal to the number of milliseconds in a trading day divided by the average number of non-zero tick-by-tick mid-price changes that day, used to scale each stock's forecast horizons.
- **Information-rich stock measure (log of updates over price changes).** The logarithm of the ratio of the number of order-book updates to the number of price changes for a stock, used as a cross-sectional explanatory variable for forecasting accuracy.

## Method

For each of 115 stocks separately, six model types are trained to map a 100-step lookback window of either order-book states or order-flow vectors onto the 10-horizon alpha term structure, minimizing mean-squared error with stochastic gradient descent (Adam optimizer) and early stopping. Training follows a rolling-window scheme with a 1-week validation block, 4 weeks of training data, and 1 week of out-of-sample testing, repeated across 48 weeks and moved forward 3 weeks each time, giving about 25K individual model fits across 115 stocks, 12 model-and-input combinations, and 18 rolling windows.

Model performance at each horizon is judged by an out-of-sample R-squared relative to a benchmark of the average realized out-of-sample return; a positive value means the model beats that benchmark. Differences between models, inputs, and horizons are assessed with t- and F-statistics computed from heteroskedasticity-consistent standard errors, and a stock's forecasting performance is later related, via cross-sectional regressions, to characteristics such as tick size and the log ratio of updates to price changes.

## Results

- Across nearly all 115 stocks, models trained on order-flow (OF) inputs outperform the same architecture trained on raw order-book (LOB) states, at almost every forecast horizon.
- Any architecture that includes an LSTM module (LSTM, LSTM-MLP, three-layer stacked LSTM, CNN-LSTM) clearly beats the linear ARX and plain MLP baselines; among LSTM-based models the deeper stacked and convolutional variants add little over a single-layer LSTM.
- Average out-of-sample R-squared rises with the forecast horizon up to about 2.0 average price changes, then declines, and the effect plateaus once the horizon range is extended up to 10 average price changes.
- A cross-sectional regression of LSTM out-of-sample R-squared on the log ratio of order-book updates to price changes achieves an adjusted R-squared of 0.746, the strongest of the stock-characteristic regressions tried.
- Tick size and the log ratio of updates to price changes are correlated at 0.95 across stocks, and both are associated with higher forecasting accuracy for 'information-rich' large-tick names.
- The full study trains and evaluates about 25K individual models (115 stocks, 12 model-and-input combinations, 18 rolling windows across 48 weeks).

## Limitations

- The models are trained and tested only on 115 Nasdaq-listed US equities over about one year, so results may not carry over to other markets, asset classes, or longer horizons.
- The authors note there is little theoretical explanation for why the observed order-flow predictability exists; the paper offers conjectures rather than a tested causal mechanism.
- Reader note: reported forecasts are not evaluated net of transaction costs or under a specific execution strategy, which the authors themselves say would be needed before any profitability claim.
- Stock-specific forecast horizons are set using a simple average-price-change scaling that ignores intraday volume and volatility patterns, a simplification the authors flag for future work.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/jeremy-turiel|Jeremy Turiel]]

## Citation

Petter N. Kolm, Jeremy Turiel, Nicholas Westray (2023). Deep order flow imbalance: Extracting alpha at multiple horizons from the limit order book. Mathematical Finance.

DOI: 10.1111/mafi.12413

Text ingested: `markdown_output/kolm-2023-deep-order-flow-imbalance-extracting-alpha.md`, converted from `raw/ofi-event-clock/kolm-2023-deep-order-flow-imbalance-extracting-alpha.pdf`.

Coverage of this summary: Read the full markdown from abstract and introduction through the model descriptions, data and methodology, all empirical results sections (short- and long-horizon predictability, cross-sectional regressions), the discussion, conclusion, and the appendices on LOBSTER preprocessing and robustness checks.

Known problems with the input: Several equations in the markdown are replaced by '==> picture... intentionally omitted <==' placeholders from PDF conversion, so exact equation forms are described in prose rather than reproduced.
<!-- AUTHORED REGION END -->