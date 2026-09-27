---
authors:
- Haochen Li
- Yi Cao
- Maria Polukarov
- Carmine Ventre
content_hash: sha256:1333a1331aa126314053e13c4fcaa49f8e214006fda58a3671f285982d57af23
created: 2026-09-27 01:47:00+00:00
page_id: sources/li-2023-empirical-analysis-financial-markets-insights-application
page_type: source
related:
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/price-impact
- concepts/informed-trading
- concepts/lstm-networks
- concepts/market-microstructure-noise
revision_id: 1
schema_version: 2
source_hash: sha256:8b9cf2b65d0ab57e0ff58a712e586478dbb81860b97aac20398bbf4450436633
source_path: markdown_output/li-2023-empirical-analysis-financial-markets-insights-application.md
source_type: paper
tags:
- crypto
- limit-order-book
- statistical-physics
- volatility-prediction
- vpin
- high-frequency-trading
- clock-calendar
- asset-crypto
- harvest-relevant
title: 'An Empirical Analysis on Financial Markets: Insights from the Application
  of Statistical Physics'
updated: '2026-09-27T01:47:00Z'
uuid: dbc9cf7c-6e74-5310-a06b-e819ee145f5c
year: 2023
---

<!-- AUTHORED REGION START -->
# An Empirical Analysis on Financial Markets: Insights from the Application of Statistical Physics

## Summary

The paper asks whether a physics-style model of the full limit order book can forecast short-term volatility and price direction better than established microstructure tools. Its motivation is that existing measures such as VPIN and the Order Flow Imbalance (OFI) either rely on trade-level data alone or on only the top of the book, while machine-learning alternatives (SVMs, CNNs, deep LSTM models) are hard to interpret and struggle to use deeper book levels because of computing and complexity limits.

The approach treats each limit order as a physical particle moving along the price axis: order size is mass, price displacement over a sampling window is velocity, and an empirically calibrated 'active depth' bounds which order-book levels are treated as informative. Aggregating order velocities within that band gives a scalar 'kinetic energy' for the book and a signed 'momentum'. These are computed from Coinbase Level 3 event feeds for BTC/USD and LUNA/USD, resampled onto a fixed time grid, without any parameter fitting or training sample.

Empirically, kinetic energy Granger-causes Bitcoin's short-horizon realized volatility better than VPIN (though VPIN wins for LUNA at a 5-minute horizon), and the momentum measure has a stronger regression fit to near-term price changes than OFI for both assets. Against a deep LSTM benchmark following Sirignano and Cont, the physics-based model matches or beats next-tick and ten-tick direction accuracy on both BTC/USD and LUNA/USD, without needing a training set.

What is new is the 'active depth' concept for deciding which deeper book levels matter without full machine-learning complexity, plus a descriptive account of the May 2022 LUNA flash crash in which the model's directional measures suggest persistent limit-order selling, rather than market-order buying pressure, drove the decline.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The underlying data is event-driven Level 3 order-book messages (submissions, cancellations, matches) with microsecond timestamps, but the paper resamples these events onto a fixed 0.1-second grid before computing its kinetic-energy and momentum measures. Prediction targets are then defined over fixed calendar horizons: 1-second and 10-second-ahead match-price changes for the momentum/OFI regressions, and 5-minute and 30-second realized-volatility windows (with lags from 1 to 300 seconds) for the VPIN/kinetic-energy Granger-causality tests.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC/USD and LUNA/USD cryptocurrency pairs
- **Venue:** Coinbase exchange (websocket Level 3 order-book feed)
- **Period:** BTC/USD: 15:00-16:00 on 28/11/2022; LUNA/USD: 02:00-03:00 on 12/05/2022 (during its flash crash); a separate BTC/USD window from 23:00 11/08/2023 to 11:00 12/08/2023 (12 hours) was used to train and test a deep LSTM benchmark, with the LOB-snapshot data for 11:00-12:00 on 12/08/2023 used as the comparison test period.
- **Granularity:** Full-channel Level 3 event records (order submission, cancellation, match), resampled to a 0.1-second grid for the physics measures; the LSTM benchmark instead uses 1-second LOB snapshots (20 bid and 20 ask levels).

## Features and Measures

- **Active depth.** An empirically calibrated order-book depth range, found from where the cross-correlation between match-price movement and the change in reacted order volume peaks, used to bound which limit-order levels are treated as informative for price dynamics.
- **Order-book kinetic energy.** A scalar measure computed as half the sum of squared order velocities (the rate at which submitted or cancelled orders move toward their quoted price) within the active-depth range, meant to capture the intensity of order-book activity.
- **Order-book momentum.** A directional measure computed as the sum of order size times order velocity within the active-depth range, meant to capture the net directional force that limit and market orders exert on price.
- **Local volatility (tick-difference).** A volatility estimator computed as the standard deviation of consecutive tick-to-tick price differences rather than of returns, intended to avoid inflated volatility readings when the price is trending.

## Method

Orders are modelled as particles on a one-dimensional price axis; submissions, cancellations and matches are treated as particles entering, exiting or annihilating within the system, giving each order a velocity from which kinetic energy and momentum are aggregated across the active-depth range at each sampling point. The active depth itself is set from where the cross-correlation between match-price movement and the volume of reacted orders peaks (found to be 50 price levels for BTC/USD and 0.2 for LUNA/USD).

Predictive performance is assessed two ways: Granger causality tests of the kinetic-energy series against realized 5-minute and 30-second volatility, benchmarked against VPIN; and ordinary least squares regressions of the momentum measure against subsequent 1-second and 10-second match-price changes, benchmarked against the Order Flow Imbalance (OFI) measure. A separate comparison trains a three-layer deep LSTM model (following Sirignano and Cont) on LOB snapshot data and compares its next-tick and ten-tick direction accuracy against the physics-based model over the same test window. The model is also discussed qualitatively against the Roll measure, Kyle's Lambda and the Amihud measure as alternative liquidity/impact benchmarks.

## Results

- The active depth, calibrated from where cross-correlation between match-price movement and reacted order volume peaks, was 50 price levels for BTC/USD and 0.2 for LUNA/USD, reflecting each market's tick-to-price ratio.
- Comparing kinetic energy against VPIN via Granger causality on 5-minute realized volatility, kinetic energy predicted Bitcoin volatility better than VPIN, while VPIN predicted LUNA volatility better than kinetic energy; at a finer 30-second local-volatility horizon, kinetic energy outperformed VPIN for both assets.
- Regressing momentum change against subsequent match-price change gave R-squared values of 0.168 (Bitcoin, 1-second horizon) and 0.816 (Bitcoin, 10-second horizon), versus 0.094 and 0.019 for OFI over the same horizons; for LUNA, momentum reached R-squared of 0.036 (1-second) and 0.274 (10-second), where OFI could not be computed due to missing data.
- The authors note their Bitcoin OFI regression underperformed the roughly 0.65 R-squared that Cont et al. (2014) reported for OFI on NYSE equities, suggesting weaker OFI performance on this cryptocurrency sample.
- Against a deep LSTM benchmark, the physics-based model reached 60.25% and 78.69% next-tick and ten-tick direction accuracy on BTC/USD, versus 60.12% and 62.57% for the deep LSTM model; on LUNA/USD during the flash crash the physics model still reached 58.70% and 69.82%.
- During the LUNA flash-crash window, the model's separated momentum measures showed market orders repeatedly failing to push the price up while limit orders sold continuously, consistent with the decline being driven by aggressive limit-order selling rather than market-order flow.
- About 98.5% of the open orders in the datasets were eventually cancelled rather than filled.

## Limitations

- The evaluation windows are short: one hour of BTC/USD data, one hour of LUNA/USD data during its flash crash, and a separate roughly 12-hour period used to train and test the deep LSTM comparison.
- The OFI benchmark could not be computed for LUNA/USD because aggregated best-bid/best-ask volume was unavailable in that dataset.
- The authors state the physical model is a measurement tool that describes order-book dynamics but does not by itself explain the economic mechanisms driving trader behaviour.
- Reader note: results rest on two cryptocurrency pairs over very short, partly crisis-specific windows (LUNA during its collapse), so generalisation to calmer periods, other assets, or bonds is untested.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/price-impact|price impact]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/market-microstructure-noise|market microstructure noise]]

## Citation

Haochen Li, Yi Cao, Maria Polukarov, Carmine Ventre (2023). An Empirical Analysis on Financial Markets: Insights from the Application of Statistical Physics.

DOI: 10.48550/arxiv.2308.14235

Text ingested: `markdown_output/li-2023-empirical-analysis-financial-markets-insights-application.md`, converted from `raw/ofi-event-clock/li-2023-empirical-analysis-financial-markets-insights-application.pdf`.

Coverage of this summary: Read the entire converted markdown file front to back: introduction, literature review, data description, the physical-model methodology and active-depth calibration, the empirical findings section, the comparisons with the Roll measure, Kyle's lambda and the Amihud measure, the VPIN-vs-kinetic-energy and OFI-vs-momentum prediction sections, the deep-LSTM comparison, the conclusion and the reference list.

Known problems with the input: The document carries two dates: '(August 2023)' under the title and a 'June 26, 2024 DRAFT' watermark repeated on every page; the printed article date (2023) was used as the year; Equations for order velocity, depth, kinetic energy and momentum are rendered as omitted images in this conversion, so their exact algebraic form could not be verified beyond the surrounding prose description.
<!-- AUTHORED REGION END -->