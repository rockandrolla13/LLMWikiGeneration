---
authors:
- David Hirnschall
content_hash: sha256:27bcf8dde509f27a390d35a89af33d3abdae0bbb50a4bf49907e5c4df4d42a43
created: 2026-09-27 01:47:00+00:00
page_id: sources/hirnschall-2020-deep-learning-approach-analyzing-limit-order
page_type: source
publication_venue: Diplomarbeit (Diploma Thesis), Institut für Stochastik und Wirtschaftsmathematik,
  TU Wien
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/realized-variance
- concepts/market-microstructure-noise
- concepts/bid-ask-spread
- concepts/order-flow-prediction
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:4072da783aa84bb49f310bbd65de04d72e0efed2a5fe7e54fd889deced4dd070
source_path: markdown_output/hirnschall-2020-deep-learning-approach-analyzing-limit-order.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- volatility-forecasting
- feature-selection
- realized-volatility
- mid-price-prediction
- nasdaq-equities
- clock-event
- asset-equity
- harvest-relevant
title: A Deep Learning Approach for Analyzing the Limit Order Book
updated: '2026-09-27T01:47:00Z'
uuid: 0b178bb3-81c5-5824-b35a-bcd963149226
year: 2020
---

<!-- AUTHORED REGION START -->
# A Deep Learning Approach for Analyzing the Limit Order Book

## Summary

The thesis asks whether a purely data-driven, assumption-free machine-learning approach can extract useful signal from limit order book (LOB) data for two tasks investors care about: predicting the near-term direction of the midprice, and forecasting realized volatility. It works with LOBSTER-supplied NASDAQ order book data for four stocks, AMZN, AAPL, GOOGL and TSLA, over date ranges given in Table 5.1 (roughly 8.Jan.2018 through 6.Aug.2019-23.Aug.2019 depending on the stock, i.e. 397 to 410 trading days).

For each task, handcrafted feature sets are built directly from the raw order-book message and orderbook files, covering per-level bid/ask prices and volumes, spreads, midprices, price and volume derivatives, and simple moving-average momentum features. These are trimmed with feature-selection methods (Pearson correlation, univariate selection, recursive feature elimination, tree-based importance, and the Boruta algorithm) before training deep feedforward neural networks whose depth, width and learning rate are chosen by grid search with 3-fold cross-validation. For the volatility task the prediction target is the two-scales realized volatility (TSRV) estimator, a bias-corrected estimator that combines realized variance computed on coarse subgrids of observation times with the full-grid estimator to cancel market-microstructure-noise bias, applied to intraday snapshots.

Grid-searched deep multilayer perceptrons outperformed both a single-layer perceptron and a scikit-learn logistic regression baseline on midprice-direction classification for all four stocks, and the Boruta algorithm generally gave more stable cross-validated accuracy than recursive feature elimination. For volatility forecasting, the multilayer perceptron produced better long-term (fixed-calibration) forecasts than ARIMA models measured by mean absolute percentage error, but a continuously re-calibrated ARIMA model beat it for two of the three stocks tested, pointing to a trade-off between prediction precision and re-calibration cost.

The contribution is less a new model than a systematic empirical pipeline: a from-scratch feature set and feature-selection comparison applied consistently across four stocks and two distinct prediction tasks, paired with a formal mathematical treatment of both the limit order book and the TSRV estimator used as the volatility target.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are order-book snapshots sampled after a fixed count of order-book events rather than at fixed wall-clock intervals: for price-movement prediction only every 20th event is kept for AMZN, GOOGL and TSLA and every 70th for AAPL, and six consecutive feature vectors are concatenated into one input sample. For volatility forecasting every 100th event is kept for AMZN and GOOGL and every 150th for AAPL, each trading day is split into 3 intraday snapshots, and the model predicts the two-scales realized volatility of the next snapshot from 8 equidistant feature vectors of the previous snapshot plus the 8 most recent intraday volatility values.

## Data

- **Asset class:** Equities
- **Instruments:** AMZN, AAPL, GOOGL, TSLA (NASDAQ-listed common stocks)
- **Venue:** NASDAQ (order book data supplied by the LOBSTER data provider)
- **Period:** AMZN 8.Jan.2018-6.Aug.2019 (397 trading days); AAPL 8.Jan.2018-8.Aug.2019 (399 days); GOOGL 8.Jan.2018-23.Aug.2019 (410 days); TSLA 8.Jan.2018-23.Aug.2019 (410 days), per Table 5.1
- **Granularity:** Order-book message and orderbook event files with nanosecond-precision timestamps and up to 5 non-zero levels per side, sub-sampled to every 20th-150th event depending on the experiment and stock

## Features and Measures

- **Basic LOB feature set (v1).** Bid and ask prices and volumes at each of the top order-book levels, taken directly from the raw orderbook file.
- **Time-insensitive feature set (v2-v5).** Bid-ask spread, midprice, price differences between levels, mean prices/volumes across levels, and accumulated bid/ask depth differences, all computed at a single point in time.
- **Time-sensitive derivative features (v6).** Average per-event derivatives (rates of change) of price and volume computed over the 5 most recent order-book events, plus the change since the previous observation.
- **Recent-window mean features (v7-v8).** Mean prices, volumes, first-level bid-ask spread and midprice, each averaged over the m most recent observations.
- **Momentum/trend oscillator feature (v9).** Difference between a short-window moving average and a long-window moving average of the midprice, intended to capture short-term market momentum.
- **Two-scales realized volatility (TSRV).** A bias-corrected realized-volatility estimator that averages the realized variance computed on several coarse, non-overlapping subgrids of observation times and combines this average with the full-grid estimator to cancel market-microstructure-noise bias.

## Method

Price-movement prediction is framed as three-class classification (up, down, flat) of the midprice, labeled either by a simple percentage-change threshold alpha or by a smoothing filter averaged over the next N future price observations. Deep feedforward neural networks with a grid-searched depth (4 to 7 hidden layers) and width (32 to 256 nodes per layer) are trained with the Adam optimizer and a weighted cross-entropy loss to counter class imbalance, with the best architecture per stock chosen via 3-fold cross-validated grid search over these settings and over a set of candidate learning rates, then evaluated on an 80%/20% train/test split against a single-layer perceptron and a scikit-learn logistic regression baseline using classification accuracy.

Volatility forecasting targets the square root of the TSRV estimate computed on intraday snapshots, using input vectors that concatenate order-book features from equidistant points within a snapshot together with the 8 most recent intraday volatility values (yielding 1008-dimensional inputs). Models are again tuned by 3-fold cross-validated grid search over depth, width and learning rate, then compared to auto-selected ARIMA(p,d,q) models under two regimes, a model calibrated once on the first 90% of the data and a model re-calibrated at every one-step-ahead prediction, using root mean squared error (RMSE) and mean absolute percentage error (MAPE).

## Results

- The deep multilayer perceptron beat both a single-layer perceptron and scikit-learn's logistic regression on held-out midprice-movement test accuracy for all four stocks, e.g. 0.406 vs 0.396 (SLP) and 0.41 (logistic regression) for AMZN, and 0.454 vs 0.42 (logistic regression) for GOOGL.
- For volatility forecasting, the multilayer perceptron produced lower long-term MAPE than a once-calibrated ARIMA model for all three stocks tested (51.607 vs 77.097 for AMZN, 27.760 vs 39.375 for AAPL, 35.349 vs 39.079 for GOOGL), but was beaten by an ARIMA model re-calibrated at every step for two of the three stocks (26.921 for AMZN, 25.918 for GOOGL).
- The Boruta feature-selection algorithm gave equal or more cross-validation-stable accuracy than recursive feature elimination (RFE) for three of the four stocks in the price-movement task; RFE was only marginally ahead for AAPL.
- For volatility forecasting, using no feature-selection algorithm at all outperformed RFE-based feature selection, despite the high dimensionality (1008) of the input vectors.
- Concatenating six consecutive LOB feature vectors (each 111-dimensional) into a single 666-dimensional input, instead of using only the current snapshot, was used to give the model temporal context for the price-movement task.
- TSLA's order-book data quality was judged insufficient for some days, so TSLA was excluded from the volatility-forecasting experiment.

## Limitations

- Authors state that computational constraints forced sub-sampling of the available LOB data (e.g. every 20th to 150th event) rather than using the full event stream.
- Authors state that the largest available time series spans only 410 trading days, which they say limits how much the neural networks can benefit from more data.
- Authors acknowledge that a basic feedforward network cannot capture the long-term evolution of financial markets nor quantify the financial risk of an incorrect prediction.
- Reader note: results are reported for only four large-cap US stocks (AMZN, AAPL, GOOGL, TSLA), so generalization to other names, sectors or market regimes is untested.
- Reader note: the markdown conversion of Tables 5.5 and 5.7 (preferred layers/nodes-per-layer per stock) shows Layers and Nodes-per-Layer values that fall outside the stated grid-search ranges for those columns, suggesting a column-order issue in the converted table; this summary therefore does not repeat those per-stock layer/node figures as fact.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

David Hirnschall (2020). A Deep Learning Approach for Analyzing the Limit Order Book. Diplomarbeit (Diploma Thesis), Institut für Stochastik und Wirtschaftsmathematik, TU Wien.

DOI: 10.34726/hss.2020.81841

Text ingested: `markdown_output/hirnschall-2020-deep-learning-approach-analyzing-limit-order.md`, converted from `raw/ofi-event-clock/hirnschall-2020-deep-learning-approach-analyzing-limit-order.pdf`.

Coverage of this summary: Read the full markdown of the thesis end to end: abstract, the neural-network background chapters, the limit-order-book and two-scales-realized-volatility theory chapters, the complete experiments chapter (price-movement prediction and volatility forecasting, including all tables), the conclusion, and the reference list.

Known problems with the input: All mathematical formulas and figures are rendered in the markdown as image placeholders ('picture... intentionally omitted') or garbled OCR fragments, so exact equation forms and plot values could not be checked beyond what the surrounding prose states; Tables 5.5 and 5.7 (preferred hyperparameter settings per stock) show Layers and Nodes-per-Layer numbers that fall outside the stated grid-search ranges for those respective columns (e.g. '32' listed under Layers when the searched layer range was {4,5,6,7}), indicating a likely column-order artifact from the table-to-markdown conversion; those specific per-stock figures were therefore left out of the summary rather than asserted as fact.
<!-- AUTHORED REGION END -->