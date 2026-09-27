---
authors:
- Raffaele Giuseppe Cestari
- Filippo Barchi
- Riccardo Busetto
- Daniele Marazzina
- Simone Formentin
content_hash: sha256:c528ed8e0808b0cd0281052eb643cad9c41b01aa8b6079d8200b253131047c07
created: 2026-09-27 01:47:00+00:00
page_id: sources/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order
page_type: source
related:
- concepts/event-clock
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/order-flow-prediction
- concepts/queue-imbalance
- entities/riccardo-busetto
- entities/daniele-marazzina
- entities/simone-formentin
revision_id: 1
schema_version: 2
source_hash: sha256:a7d3681e357635acce82f26949a9e7101f22c54ef8a73d5e86636e3bac6cca58
source_path: markdown_output/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order.md
source_type: paper
tags:
- hawkes-processes
- limit-order-book
- cryptocurrency
- point-processes
- high-frequency-trading
- return-prediction
- clock-event
- asset-crypto
- harvest-core
title: Hawkes-based cryptocurrency forecasting via Limit Order Book data
updated: '2026-09-27T01:47:00Z'
uuid: e0637315-0fb2-5278-820a-b5f882f949f0
year: 2023
---

<!-- AUTHORED REGION START -->
# Hawkes-based cryptocurrency forecasting via Limit Order Book data

## Summary

The paper addresses forecasting the sign of returns in high-frequency cryptocurrency trading using limit order book (LOB) data, building on prior work that predicted return sign from a 'base imbalance' regressor but assumed the timing of the next LOB event was already known. This paper removes that assumption by predicting the next event's arrival time itself.

The approach models LOB event arrivals as a Hawkes process, a self-exciting point process whose intensity rises after recent events and decays afterward; maximum likelihood estimation on a rolling training window gives the baseline, self-excitation, and decay parameters, which are then used to draw a predicted next-event time from an exponential distribution. That predicted event time, together with the current base-imbalance value, feeds into a continuous output error (COE) model, estimated via a refined instrumental-variable method, that forecasts the sign of the next return. The full pipeline is compared against three alternatives for the next-event-time input: an Oracle with perfect knowledge, a Naive one-second-ahead rule, and a 60-second moving average.

Using LOB data for Tether (USDT) against the US dollar from the Bitfinex exchange, the correlation between decile-average base imbalance and decile-average return was -0.96, confirming the regressor's relevance outside the stock market it was originally built for. Across 50 two-minute validation scenarios, the Hawkes-based pipeline was the closest to the Oracle in both return-sign accuracy and cumulative trading profit, ahead of the Naive and Moving Average benchmarks.

What is new is coupling a Hawkes-process forecast of the next LOB event time with the existing COE return-sign model, removing the need to assume the next event time is known in advance, and showing that the base-imbalance regressor transfers from equities to a stablecoin cryptocurrency market.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The base series is indexed by LOB event times (order arrivals and updates), which are irregularly spaced in calendar time; a Hawkes process models the intensity of the next LOB event and is used to draw a predicted next-event time from an exponential distribution with mean given by the current intensity. The forecast horizon is therefore not a fixed calendar interval but the predicted time to the next LOB event, constrained to fall within a forecast window of 5 seconds; the predicted event time then feeds a continuous output error model that forecasts the sign of the return realized at that event.

## Data

- **Asset class:** Crypto
- **Instruments:** Tether (USDT) against the US dollar
- **Venue:** Bitfinex exchange (LOB data supplied by the provider CryptoTick)
- **Period:** April 13, 2019 to May 7, 2019 (25 days); hyperparameters tuned on a held-out validation day, May 3, 2019
- **Granularity:** LOB records with event resolution of at least 1 second, up to 50 price levels; 1,615,982 total LOB records

## Features and Measures

- **Base imbalance (BI).** A regressor computed from the limit order book capturing the imbalance of the book, used (following Busetto and Formentin, 2023) as the main predictor of future return sign.
- **Hawkes process intensity model.** A self-exciting point process whose arrival intensity for new LOB events rises after recent events and decays exponentially afterward, used here to predict the next LOB event's arrival time from baseline, self-excitation, and decay parameters.
- **Continuous Output Error (COE) model.** A continuous-time linear model connecting the base-imbalance regressor to future returns, with parameters estimated via a refined instrumental-variable method (SRIVC) suited to irregularly-sampled data.

## Method

Hawkes process parameters (baseline, self-excitation weight, decay rate) are identified by maximum likelihood on a rolling training window of historical LOB event times, then used each second to draw a predicted next-event time from an exponential distribution with mean given by the current intensity. This predicted event time, together with the most recent base-imbalance value, is fed into a continuous output error (COE) model relating base imbalance to future returns, whose parameters are estimated via the SRIVC instrumental-variable algorithm on a separate rolling training window. The predicted return sign is compared against the actual return closest in absolute time distance to the predicted event. The full pipeline is benchmarked against three alternatives for predicting the next event time: an Oracle with perfect knowledge, a Naive rule (next event exactly 1 second ahead), and a Moving Average of the last 60 seconds of inter-event times; each is evaluated over 50 Monte Carlo validation scenarios of 2 minutes each, on both return-sign classification accuracy and cumulative trading profit from a long/short strategy sized at $10,000 per trade with no transaction costs.

## Results

- Across 50 validation scenarios, the Oracle (perfect next-event-time knowledge) achieved the highest return-sign accuracy, as expected, with the Hawkes-based prediction next best, ahead of the Naive and Moving Average benchmarks.
- The same ranking held for cumulative trading profit: Oracle earned the most with the smallest spread between best and worst outcomes, Hawkes came close to Oracle, and Naive/Moving Average trailed.
- The decile Pearson correlation between base imbalance and return was -0.96, supporting base imbalance as a predictor of return sign on cryptocurrency LOB data, not only on the stock data it was originally developed for.
- 80% of records had a zero return and were excluded as uninformative; among the remaining non-zero-return records, 34% had one minute of missing data.
- The dataset spans 1,615,982 LOB records over 25 days (April 13 to May 7, 2019), with LOB depth up to 50 levels and event resolution of at least 1 second.
- Simulation hyperparameters (20-minute Hawkes training window, 50-minute COE training window, 2.5-minute warm-up, 5-second forecast window, 8 LOB depth levels used) were tuned on a held-out validation day (May 3, 2019) to minimize the average error between predicted and actual event times.

## Limitations

- The authors state they discard all zero-return records (80% of the data), possibly losing information content.
- The authors note that matching a predicted return to the nearest actual event by absolute time distance is an approximation; other choices (previous vs. following event) could be made instead.
- The authors state the procedure cannot be applied to all records in the dataset because of the specific timing constraints used (minimum and maximum inter-event time bounds).
- The authors state transaction fees are not included in the reported trading profit.
- Reader note: validation is limited to 50 short (2-minute) scenarios on a single trading pair (USDT-USD) over 25 days, so it is unclear how the method performs over longer horizons or other assets.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/queue-imbalance|Queue Imbalance]]
- [[entities/riccardo-busetto|Riccardo Busetto]]
- [[entities/daniele-marazzina|Daniele Marazzina]]
- [[entities/simone-formentin|Simone Formentin]]

## Citation

Raffaele Giuseppe Cestari, Filippo Barchi, Riccardo Busetto, Daniele Marazzina, Simone Formentin (2023). Hawkes-based cryptocurrency forecasting via Limit Order Book data.

DOI: 10.48550/arxiv.2312.16190

Text ingested: `markdown_output/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order.md`, converted from `raw/ofi-event-clock/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order.pdf`.

Coverage of this summary: Read the entire paper: introduction and literature review, notation, exploratory data analysis and correlation analysis, the point-process/Hawkes/COE mathematical formulation, the full algorithm, simulation settings, return-sign and trading-simulation results, and the limitations/conclusion section.

Known problems with the input: No explicit publication venue or standalone publication year is printed for this paper itself; year from file metadata (year_hint 2023), consistent with the arXiv id (2312.16190v1) referenced for a figure; Several equations are rendered as picture placeholders or with corrupted symbol spacing in the markdown, so exact mathematical notation could not be fully verified beyond the surrounding prose.
<!-- AUTHORED REGION END -->