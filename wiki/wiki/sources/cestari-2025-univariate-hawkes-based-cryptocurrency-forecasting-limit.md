---
authors:
- Raffaele G. Cestari
- Filippo Barchi
- Riccardo Busetto
- Daniele Marazzina
- Simone Formentin
content_hash: sha256:612116b31c906857870534d062efdb626367a91011fd2b13b240b8f795cb1873
created: 2026-09-27 01:47:00+00:00
page_id: sources/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit
page_type: source
publication_venue: 2025 23rd European Control Conference (ECC), Thessaloniki, Greece
related:
- concepts/event-clock
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/order-flow-prediction
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/queue-imbalance
- entities/riccardo-busetto
- entities/daniele-marazzina
- entities/simone-formentin
revision_id: 1
schema_version: 2
source_hash: sha256:fafa4e107d90632ff3f47f2a95fb4a5695cf500ae5350f9ae11caf45de9ff880
source_path: markdown_output/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit.md
source_type: paper
tags:
- hawkes-process
- limit-order-book
- cryptocurrency
- return-sign-prediction
- point-process
- event-time-prediction
- trading-simulation
- high-frequency-trading
- clock-event
- asset-crypto
- harvest-core
title: Univariate Hawkes-based cryptocurrency forecasting via Limit Order Book data
updated: '2026-09-27T01:47:00Z'
uuid: 91ed6fa9-b896-5878-b359-4466ecc65567
year: 2025
---

<!-- AUTHORED REGION START -->
# Univariate Hawkes-based cryptocurrency forecasting via Limit Order Book data

## Summary

The paper asks whether the sign of very short-horizon cryptocurrency returns can be forecast without assuming, as prior work did, that the exact time of the next order book event is known in advance. It builds on an existing continuous output error (COE) model that links a base imbalance (BI) regressor built from the limit order book to future returns, but removes that model's dependence on knowing the next event time ahead of time.

The fix is to model the arrival times of order book events with a univariate, first-order Hawkes process, a self-exciting point process fit by least squares on a rolling training window using the open-source Tick library. At each step the fitted intensity function is used to draw a random waiting time to the next predicted event, which is then fed, together with the most recent base imbalance value, into the COE model (estimated with a refined instrumental-variable method) to produce a predicted return sign. The whole pipeline is tested on order book data for the Tether (USDT) stablecoin traded against the US dollar on a centralized exchange, and compared against three baselines for guessing the next event time: an Oracle with perfect timing knowledge, a Naive rule using the minimum tick resolution, and a moving-average rule.

Across 50 held-out two-minute validation windows, the Hawkes-based timing model gives return-sign accuracy and cumulative trading profit that are close to the Oracle and clearly better than the Naive and moving-average baselines. The paper also finds a strong decile-level correlation between base imbalance and returns in the Tether data, echoing what the base imbalance regressor's original authors found for stock data.

What is new relative to the paper's own reference work is dropping the assumption that the next event time is known, replacing it with a learned point-process forecast, and showing that the base imbalance regressor still carries useful information outside the equity market it was originally built for.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are individual limit order book events with non-zero returns, sampled at whatever irregular times they actually occur rather than on a fixed grid; zero-return events are dropped before analysis. A Hawkes process fit on a rolling training window is used to draw a random forecast of the time of the next such event, and the prediction horizon is therefore this predicted inter-event gap (capped by a forecast window) rather than a fixed calendar interval. The realized return used to score each forecast is the return of whichever actual event turns out to be closest in absolute time to the predicted event time.

## Data

- **Asset class:** Crypto
- **Instruments:** Tether (USDT) traded against the US dollar
- **Venue:** a centralized cryptocurrency exchange (Bitfinex), with limit order book data supplied by the provider CryptoTick
- **Period:** April 13, 2019 to May 7, 2019
- **Granularity:** Limit order book records with sub-second timestamps and depth to 50 price levels; 1,615,982 records in total; events are shown to occur no faster than about once per second.

## Features and Measures

- **Base imbalance (BI).** A regressor computed from the limit order book's ask and bid side spread, carried over from a prior continuous-time return model and used here as the input driving predicted returns.
- **Hawkes intensity function.** A self-exciting event-rate function with a baseline, self-excitation weight and exponential decay rate, fit by least squares to recent order book event times and used to sample the time of the next event.
- **Continuous output error (COE) model.** A continuous-time input-output model, estimated by a refined instrumental-variable method, that maps the history of base imbalance and past returns onto the next return, so that plugging in a predicted event time and the latest base imbalance yields a predicted return sign.

## Method

The algorithm couples two components. First, a first-order univariate Hawkes process is identified by least-squares estimation on a rolling training window of historical inter-event times (using the Tick Python library), and its fitted intensity is used to draw the next event time from an exponential waiting-time distribution; the model is refit every second in a moving window. Second, a continuous output error model relating base imbalance to future returns is estimated on a separate rolling training window using the simplified refined instrumental variable method for continuous-time models (SRIVC); given the Hawkes-predicted event time and the latest base imbalance, it outputs a predicted return whose sign is the trading signal.

Performance is judged by comparing this Hawkes-based timing model against three alternative ways of guessing the next event time, all paired with the same COE model: an Oracle with exact knowledge of the next event time, a Naive rule that always predicts the minimum system time resolution, and a moving-average rule based on the average event gap over a trailing window. All hyperparameters (training window lengths, warm-up period, forecast window, simulation length, order book depth used) were chosen by a sensitivity analysis that minimized the average absolute error between predicted and actual event times on a held-out validation day, with the COE hyperparameters separately tuned to maximize return-sign accuracy on that same validation day.

The four strategies are then compared on two metrics over 50 two-minute validation scenarios drawn from the dataset: classification accuracy of the predicted return sign, and cumulative dollar profit from a simple trading rule that buys or sells 10,000 dollars of USDT according to the predicted sign, with no transaction costs included.

## Results

- Excluding the 80% of records with a zero return, and after further removing 34% of the remaining records that had one minute of missing data, the decile-level Pearson correlation between base imbalance and return in the Tether data was -0.96.
- In return-sign accuracy over 50 two-minute validation scenarios, the Oracle strategy performed best as expected, with the Hawkes-based strategy next, ahead of both the moving-average and Naive baselines.
- In a paired trading simulation using the same COE model and the same 50 validation scenarios, the same ranking held: the Oracle produced the highest median cumulative profit with the narrowest spread, the Hawkes-based strategy approached that performance, and the moving-average and Naive strategies trailed.
- The hyperparameter set found by sensitivity analysis used a 20-minute Hawkes training window, a 50-minute COE training window, a 2.5-minute Hawkes warm-up period, a 5-second Hawkes forecast window, a 2-minute simulation length, and an order book depth of 8 levels.
- The Naive baseline's minimum resolution of 1 second and the moving-average baseline's 60-second trailing window were both outperformed by the Hawkes-based next-event-time prediction.

## Limitations

- The authors note that dropping zero-return events, needed to make the point-process approach tractable, may discard useful information.
- Matching a predicted event time to the nearest actual event in absolute time is described by the authors as an approximation; other matching choices (nearest preceding or following event) were not tried.
- The authors state the procedure could only be applied to portions of the data meeting specific timing constraints, not the whole dataset.
- Transaction costs were not included in the reported trading profit.
- Reader note: validation covers only 50 two-minute windows on a single instrument (USDT-USD) over a roughly three-week span, a narrow test of generalization.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/queue-imbalance|Queue Imbalance]]
- [[entities/riccardo-busetto|Riccardo Busetto]]
- [[entities/daniele-marazzina|Daniele Marazzina]]
- [[entities/simone-formentin|Simone Formentin]]

## Citation

Raffaele G. Cestari, Filippo Barchi, Riccardo Busetto, Daniele Marazzina, Simone Formentin (2025). Univariate Hawkes-based cryptocurrency forecasting via Limit Order Book data. 2025 23rd European Control Conference (ECC), Thessaloniki, Greece.

DOI: 10.23919/ecc65951.2025.11187051

Text ingested: `markdown_output/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit.md`, converted from `raw/ofi-event-clock/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit.pdf`.

Coverage of this summary: Read the entire converted markdown, from abstract through the concluding remarks and references.
<!-- AUTHORED REGION END -->