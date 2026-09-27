---
authors:
- Timothée Hornek
- Sergio Potenciano Menci
- Ivan Pavić
content_hash: sha256:1d7925eda032b0f5f00ddc15a35a72975537471c96958706cee97caf572a73e4
created: 2026-09-27 01:47:00+00:00
page_id: sources/hornek-2025-directional-price-forecasting-continuous-intraday-market
page_type: source
publication_venue: 14th DACH+ Conference on Energy Informatics (to appear in ACM SIGEnergy
  Energy Informatics Review)
related:
- concepts/limit-order-book
- concepts/order-flow-prediction
- concepts/high-frequency-data
- concepts/feature-engineering
- concepts/high-frequency-trading
- concepts/diebold-mariano-test
revision_id: 1
schema_version: 2
source_hash: sha256:58f5e9ac10f882da4ec925cb443201f8e60d3697b0ee34b40b9834049c49fa55
source_path: markdown_output/hornek-2025-directional-price-forecasting-continuous-intraday-market.md
source_type: paper
tags:
- electricity-price-forecasting
- limit-order-book
- directional-forecasting
- intraday-market
- gradient-boosting
- algorithmic-trading
- feature-importance
- clock-calendar
- asset-futures
- harvest-relevant
title: Directional Price Forecasting in the Continuous Intraday Market under Consideration
  of Neighboring Products and Limit Order Books
updated: '2026-09-27T01:47:00Z'
uuid: cd13e564-4f7e-591d-8ec9-5299b8d194c5
year: 2025
---

<!-- AUTHORED REGION START -->
# Directional Price Forecasting in the Continuous Intraday Market under Consideration of Neighboring Products and Limit Order Books

## Summary

The paper tackles short-term forecasting of hourly electricity prices in the German-Luxembourgish continuous intraday (CID) market. The authors argue prior work mostly forecasts a single benchmark price per product and largely ignores limit order book (LOB) data and quarter-hourly neighboring products, so they instead frame the task as binary classification of whether the market will rise or fall over the next five minutes, which fits algorithmic trading decisions better than a point forecast.

Their method runs a rolling window that makes a new forecast every calendar minute from three hours to thirty-five minutes before delivery. Each forecast compares a reference VWAP (last four trades) to a future VWAP (next five minutes of trades) to build the classification label. Features include the target product's own lagged one-minute VWAPs, LOB VWAPs computed at different order/volume depths, prices from hourly and quarter-hourly neighboring products, load and renewable generation forecasts, and a grid-imbalance signal. Logistic regression and LightGBM models are trained with weekly cross-validation over roughly one year of EPEX data.

LOB-derived features produced the largest accuracy gains of any feature group, followed by neighboring-product prices, with the biggest benefit coming from neighbors whose delivery starts within the current product's trading period. Fundamentals and the grid-imbalance feature added little or nothing. Gradient boosting had higher overall accuracy, but logistic regression yielded better profit-and-loss (PnL) on the highest-confidence forecasts, and both accuracy and PnL rose as the analysis was restricted to higher-signal-strength forecasts.

What is new is the combination of a directional (classification) formulation with LOB features and, for the first time in this literature, quarter-hourly neighboring-product prices, rather than only hourly neighbors or single-benchmark point forecasts.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The model issues one forecast every calendar minute during the forecasting window (145 steps per product, from three hours to thirty-five minutes before delivery), each time predicting the direction of the five-minute-ahead VWAP relative to a reference VWAP of the last four trades. Historical price features are built from lagged one-minute VWAP bins (up to ten lags) rather than trade counts, so although the underlying transaction data arrives at irregular intervals, the sampling and forecasting clock itself is fixed wall-clock time.

## Data

- **Asset class:** Futures
- **Instruments:** Hourly and quarter-hourly electricity delivery products traded in the German-Luxembourgish continuous intraday (CID) market on EPEX; the paper itself describes these nominally spot products as functioning like futures markets with short lead times to delivery.
- **Venue:** EPEX SPOT SE continuous intraday market (German-Luxembourgish bidding zone); fundamentals sourced from the ENTSO-E transparency platform
- **Period:** Test period April 14, 2024 to April 13, 2025, with 52 weekly cross-validation folds, each retrained on the preceding 30 days of data with a one-day buffer before the test week
- **Granularity:** Tick-level trade and limit order book data aggregated into one-minute VWAP bins; forecasts issued every minute with a five-minute-ahead horizon

## Features and Measures

- **VWAP of last four trades.** Volume-weighted average price over the four most recent transactions before the forecast time, used both as the classification's reference price and as the most recent price feature for the target product.
- **Historical price vector.** Up to ten lagged one-minute VWAP values capturing recent price history for the target product and, without the most-recent-trade term, for its neighboring products.
- **LOB depth VWAPs.** Volume-weighted average prices computed over the top 1, 5, or 10 orders, or over the top 1, 5, or 10 MW of cumulative volume, separately for the bid and ask sides of the current limit order book.
- **Neighboring product prices.** Historical price vectors of hourly and quarter-hourly products whose delivery periods overlap or are adjacent to the current product's trading period, grouped into three sub-periods based on time remaining to delivery.
- **Fundamentals (load and VRE forecasts).** Day-ahead and, for renewables, updated intraday forecasts of load and solar/onshore-wind/offshore-wind generation for the German-Luxembourgish zone.
- **Imbalance (NRV-Saldo).** The most recently published quarter-hourly grid control cooperation balance, indicating the gap between generation and consumption across the four German transmission system operators.

## Method

The forecasting problem is posed as binary classification of five-minute-ahead market direction. A rolling window steps every minute from three hours to thirty-five minutes before delivery, giving 145 forecasts per product; the label compares a past reference VWAP to a future VWAP, and models are retrained on a 30-day lookback with a one-day buffer across 52 consecutive weekly test intervals covering the one-year test period.

Two classifiers are compared: an l2-regularized logistic regression and a LightGBM gradient boosting model, the latter fit on price features after a partial-least-squares transform used to address multicollinearity among lagged and cross-product price variables. Feature groups are added one at a time to a 'Current' (own-product history only) baseline, and a Diebold-Mariano test, preceded by an Augmented Dickey-Fuller stationarity check on the error-difference series, is used to judge whether an added feature group gives a statistically significant accuracy improvement.

Performance is judged with classification accuracy and a simulated PnL that opens a position at the reference price and closes it at the future price according to the predicted direction; results are also broken out by the model's predicted-class probability (signal strength) to see whether higher-confidence forecasts are more accurate and more profitable.

## Results

- Adding LOB features gave the largest accuracy gains of any feature group, reaching 58.22% in the 3h-to-2h period, 55.93% in the 2h-to-1h period, and 57.30% in the 1h-to-half-hour period, versus a Current-only baseline of 51.73%, 51.26%, and 53.00% respectively.
- Quarter-hourly neighboring products consistently gave higher accuracy gains than hourly neighboring products, and neighbors whose delivery started before the current product's trading period helped more than those starting after it (for example 54.25% for QH neighbors starting one hour earlier versus 52.37% for QH neighbors starting one hour later, in the 3h-to-2h period).
- Adding fundamentals (load and VRE forecasts) or the NRV-Saldo imbalance feature did not improve, and in some periods slightly reduced, accuracy relative to the Current baseline.
- Gradient boosting had higher overall classification accuracy than logistic regression, but logistic regression produced higher PnL among the highest-signal-strength forecasts, which the authors attribute to gradient boosting overfitting the training data.
- Restricting the evaluation to the highest-signal-strength forecasts increased both accuracy and PnL across all three forecasting periods, indicating that the model's predicted probability tracks forecast reliability.
- Under perfect foresight, mean PnL per forecast rose from 0.24 in the 3h-to-2h period to 0.29 in the 2h-to-1h period and 0.48 in the 1h-to-half-hour period, tracking rising volatility closer to delivery.
- Weekly accuracy in the shortest-lead-time period stayed relatively stable across the one-year test window, while the two longer-lead-time periods showed accuracy declines around August 2024 and December 2024, coinciding with periods of high solar and wind generation respectively.

## Limitations

- Only logistic regression and gradient boosting were tested as forecasting models; other approaches such as neural networks were left to future work.
- Analysis is restricted to the ID3 trading period (three hours to thirty minutes before delivery) for hourly products only, so results may not generalize to other lead times or to quarter-hourly product forecasting.
- The test period covers only April 2024 to April 2025 in a single market (German-Luxembourgish CID), limiting how far the findings generalize to other periods or markets.
- The authors did not backtest the forecasts as a realistic trading strategy, since that would require further assumptions about order execution, liquidity, and market impact within the LOB.
- Reader note: the simulated PnL opens a position at a non-tradeable past reference price, so the reported profitability likely overstates what a live execution strategy could achieve.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/diebold-mariano-test|diebold mariano test]]

## Citation

Timothée Hornek, Sergio Potenciano Menci, Ivan Pavić (2025). Directional Price Forecasting in the Continuous Intraday Market under Consideration of Neighboring Products and Limit Order Books. 14th DACH+ Conference on Energy Informatics (to appear in ACM SIGEnergy Energy Informatics Review).

DOI: 10.1145/3777518.3777525

Text ingested: `markdown_output/hornek-2025-directional-price-forecasting-continuous-intraday-market.md`, converted from `raw/ofi-event-clock/hornek-2025-directional-price-forecasting-continuous-intraday-market.pdf`.

Coverage of this summary: Read the entire markdown file, including introduction, literature review, methodology, results, limitations, conclusion, and the appendices.
<!-- AUTHORED REGION END -->