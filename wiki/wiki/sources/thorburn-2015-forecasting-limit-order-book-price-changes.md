---
authors:
- Sebastian Thorburn
content_hash: sha256:d4bf4cadd639e76635554c46f3f320fc1b84c65e32e92fde9974392e5ee27835
created: 2026-09-27 01:47:00+00:00
page_id: sources/thorburn-2015-forecasting-limit-order-book-price-changes
page_type: source
publication_venue: 'Lund University, Master Essay, Course NEKN01 (Supervisor: Hossein
  Asgharian)'
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/order-flow-prediction
- concepts/high-frequency-data
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:a292b450ac25fea4571f1320a0bf0c238b72a9a3bd49f32288084766c207fa2e
source_path: markdown_output/thorburn-2015-forecasting-limit-order-book-price-changes.md
source_type: paper
tags:
- limit-order-book
- change-point-detection
- cusum
- order-imbalance
- nordic-equities
- master-thesis
- clock-compares
- asset-equity
- harvest-core
title: Forecasting limit order book price changes using change point detection
updated: '2026-09-27T01:47:00Z'
uuid: 733914f1-8bdf-5e01-8042-8af41ab44f73
year: 2015
---

<!-- AUTHORED REGION START -->
# Forecasting limit order book price changes using change point detection

## Summary

The thesis asks whether a significant shift in the shape of the limit order book carries information about the direction of the next mid-price move, and whether detecting such shifts is a better way to reduce a noisy, irregularly-timed order book data set than sampling it at a fixed calendar interval. The author builds a limit order imbalance measure from the volume-weighted price of resting orders on the top twenty levels of the book relative to the mid price, then feeds this signal into a CUSUM (cumulative sum) algorithm that raises an alarm, and records a change point, whenever the running sum of positive or negative deviations crosses a threshold set at one tenth of the stock's opening price. Each change point is coded as an upward or downward alarm and used as the sole regressor in a simple dummy-variable regression forecasting the mid-price change to the next change point. As a benchmark, the same imbalance measure is instead computed on a fixed 5-minute grid and used in an equivalent regression.

The data are complete order book snapshots (top twenty levels each side) for the thirty least-liquid constituents of the Swedish, Finnish and Danish blue-chip indices, drawn from NasdaqOMX's Nordic Historical View product for February 2012, with liquidity and stock selection performed on the first trading day of that sample.

Across the thirty stocks, the change-point-based regressions produced coefficient signs in the direction implied by the imbalance measure for the large majority of stocks and had lower model p-values than the 5-minute benchmark regressions, which came close to a coin-flip on sign direction. The author concludes that the change-point data series retains more predictive information than fixed-interval sampling of the same underlying signal, even though the estimated price moves following a detected change point are small in absolute terms.

What is new here is not the imbalance measure itself, which builds directly on earlier order-book imbalance work, but the idea of using an online change-point detector (CUSUM) as the sampling rule for reducing a high-frequency limit order book data set, in place of an arbitrary fixed time interval.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The primary series samples the book only when a CUSUM statistic built on the limit order imbalance measure crosses an alarm threshold, producing an irregularly time-spaced series of upward/downward change-point flags; the forecast horizon is the gap to the next detected change point. The benchmark series instead samples the imbalance measure on a fixed 5-minute calendar grid, with the forecast horizon fixed at 5 minutes. The alarm threshold for each stock was set, without optimization, to one tenth of that stock's share price at the first observation of the sample.

## Data

- **Asset class:** Equities
- **Instruments:** 30 Nordic equities: the ten least-liquid constituents of each of OMXS30 (Sweden), OMXH25 (Finland) and OMXC20 (Denmark), selected via a constructed order-book liquidity measure
- **Venue:** NasdaqOMX (Stockholm, Copenhagen, Helsinki), Nordic Historical View data product
- **Period:** February 2012, described as a 20 trading-day sample
- **Granularity:** full limit order book updates, top 20 bid/ask price levels, heterogeneous in time

## Features and Measures

- **Limit order imbalance measure.** The volume-weighted average price of resting bid and ask orders across the top twenty book levels, minus the mid price; used as a scalar proxy for the shape of the order book.
- **Liquidity measure.** The average, over a trading day, of the total nominal value of all resting orders on the top twenty price levels; used only to rank and select stocks.
- **CUSUM change-point detector.** An online cumulative-sum algorithm that tracks positive and negative deviations of the imbalance measure from a reference level and flags a change point (coded up or down) whenever either running sum exceeds a fixed alarm threshold, after which both sums reset.

## Method

Stocks are first narrowed to the ten least liquid names in each of three national indices using the constructed liquidity measure computed from day-one order book data. The limit order imbalance measure is then computed at every book update and passed through a CUSUM detector with a per-stock alarm threshold fixed at one tenth of the initial share price; every threshold crossing produces a binary (up/down) change-point observation. A single regression per stock uses this binary series as its only explanatory variable to forecast the mid-price change to the next change point. A second, benchmark regression per stock instead uses the continuous imbalance measure sampled every 5 minutes to forecast the 5-minute-ahead mid-price change. Performance is judged by the sign of each regression's slope relative to the sign implied by the imbalance measure's intuition, and by the p-value of the overall regression fit, compared across the two sampling schemes.

## Results

- In the change-point regressions, 90% of the 30 stocks had coefficient signs in the direction implied by the imbalance measure, versus 57% for the 5-minute benchmark regressions.
- 70% of stocks had a change-point regression model p-value below 10%, 63% below 5%, and 47% below 1%, compared with 50%, 43% and 33% respectively for the 5-minute benchmark.
- The change-point sample averaged 1995 data points per stock over the sample, versus a fixed 2020 observations per stock for the 5-minute benchmark.
- 27 out of the 30 stocks in the change-point sample had coefficient signs consistent with the model's intuition, and most stocks with the 'wrong' sign also had comparatively few detected change points.
- The author concludes the estimated price move following a detected change point is small in magnitude, though potentially still useful in an automated liquidity-provision context.

## Limitations

- The CUSUM alarm threshold was set once, arbitrarily, per stock (one tenth of the initial share price) with no optimization, which the author suggests may explain why some stocks show weak significance.
- The sample covers a single calendar month (February 2012) of Nordic equity data.
- No search for outliers or data-quality checks was performed beyond removing auction periods, since the exchange data was assumed to be clean.
- Reader note: only equities are studied; no fixed income or multi-asset evidence is offered.
- Reader note: the reported forecast is a simple two-parameter dummy/linear regression per stock, not a walk-forward or held-out test.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Sebastian Thorburn (2015). Forecasting limit order book price changes using change point detection. Lund University, Master Essay, Course NEKN01 (Supervisor: Hossein Asgharian).

Text ingested: `markdown_output/thorburn-2015-forecasting-limit-order-book-price-changes.md`, converted from `raw/ofi-event-clock/thorburn-2015-forecasting-limit-order-book-price-changes.pdf`.

Coverage of this summary: Read the entire thesis markdown (all sections: introduction, theoretical framework, method, results, analysis, conclusion, references, appendix).

Known problems with the input: The converted markdown drops most inline mathematical formulas as omitted pictures or garbled OCR text, so several formal equation definitions (mid price, CUSUM recursion, regression specification) could not be verified beyond the plain-language description already given in the text.
<!-- AUTHORED REGION END -->