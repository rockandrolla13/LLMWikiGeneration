---
authors:
- Davide Raffaelli
- Raffaele Giuseppe Cestari
- Daniele Marazzina
- Simone Formentin
content_hash: sha256:ff99183de602d52c79880c069d4a7af5927be2536df598cbff4840af0d7e4b1e
created: 2026-09-27 01:47:00+00:00
page_id: sources/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes
page_type: source
publication_venue: Decisions in Economics and Finance
related:
- concepts/event-clock
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/order-flow-imbalance
- concepts/order-flow-prediction
- concepts/queue-imbalance
- entities/daniele-marazzina
- entities/simone-formentin
revision_id: 1
schema_version: 2
source_hash: sha256:9996ccefbf6e1bfdf0388825cbdab0501009c73ba2c49be2e0e71068c632e9bf
source_path: markdown_output/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes.md
source_type: paper
tags:
- bitcoin
- hawkes-processes
- limit-order-book
- high-frequency-trading
- return-sign-prediction
- continuous-time-modeling
- cryptocurrency-trading
- clock-event
- asset-crypto
- harvest-core
title: Forecasting Bitcoin price movements using multivariate Hawkes processes and
  limit order book data
updated: '2026-09-27T01:47:00Z'
uuid: 0809ae29-1aeb-549a-a7a8-043ef559cc75
year: 2026
---

<!-- AUTHORED REGION START -->
# Forecasting Bitcoin price movements using multivariate Hawkes processes and limit order book data

## Summary

The paper asks whether event-level limit order book (LOB) dynamics on a cryptocurrency exchange can be used to forecast both the timing and the direction of the next mid-price change, and whether modelling cross-excitation among several event types (not just self-excitation within one event type) improves that forecast.

The authors build event streams from Bitfinex BTC/USD LOB updates, defining event types such as mid-price increase/decrease, liquidity increase/decrease, and buy/sell pressure. They fit multivariate Hawkes processes (MHP) with exponential kernels to these event types using a regularized least-squares estimator solved with an accelerated proximal-gradient method and a greedy search over decay parameters. Two forecasting pipelines are then compared. HawkesTime forecasts the time of the next mid-price-change event with the MHP and feeds that timing, together with the current Base Imbalance (a bid/ask volume asymmetry measure), into a separate continuous-time output-error (COE) model to estimate the return's sign and magnitude. HawkesSign instead uses only an MHP defined over directional/pressure event types to jointly forecast timing and sign in a single step.

The MHP forecasts next-event timing more accurately than a univariate Hawkes process, a moving average, a Poisson model, and a naive baseline. HawkesTime is consistently more accurate at predicting return sign than HawkesSign and a moving-average benchmark, and only HawkesTime produces a steadily rising simulated trading profit; HawkesSign and the benchmark fluctuate near zero profit. This advantage for HawkesTime holds up in a later robustness sample from a different market regime and on a second asset (ETH/USD).

The main contribution is applying multivariate (rather than univariate) Hawkes modelling to cryptocurrency LOB forecasting, which the authors say is a first for this market, extending prior univariate-Hawkes work to a more volatile trading pair and to explicit cross-excitation between heterogeneous LOB event types.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are the sequence of irregular LOB events (mid-price changes, liquidity increases/decreases, buy/sell pressure) as they occur; the Hawkes intensities driving the forecast are estimated from the preceding 150 seconds of event history. The prediction horizon is the next mid-price-change event: HawkesTime first forecasts that event's arrival time and then estimates the return over that horizon with the COE model, while HawkesSign forecasts the arrival time and the return's sign jointly in one step.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC/USD (primary); ETH/USD (robustness check)
- **Venue:** Bitfinex, a centralized cryptocurrency exchange, via its WebSocket API
- **Period:** January 1-31, 2024 (main sample); July 1-31, 2025 (robustness sample, BTC/USD and ETH/USD)
- **Granularity:** tick-by-tick, event-level LOB updates at millisecond resolution; about 3 million updates in the main sample, of which about 375,000 are mid-price changes

## Features and Measures

- **Base Imbalance (BI).** An asymmetry measure between bid and ask volumes across multiple LOB levels, used as the explanatory variable for future mid-price returns.
- **Multivariate Hawkes Process (MHP).** A point-process model over several LOB event types with self- and cross-excitation, used to forecast when the next relevant LOB event will occur.
- **Continuous-time Output Error (COE) model.** A continuous-time linear dynamical model relating the Base Imbalance signal to future returns, designed to work with irregularly sampled LOB data.
- **HawkesTime.** A two-stage pipeline that uses the MHP to forecast the next mid-price-change time and then feeds that timing and the current BI into the COE model to estimate the return's magnitude and sign.
- **HawkesSign.** A single-stage pipeline that uses an MHP defined over directional/pressure event types to jointly forecast the timing and sign of the next return, without a separate dynamic model.

## Method

MHP parameters (background intensities, excitation matrix, decay matrix) are estimated by regularized least squares with an l1 sparsity penalty, minimized via an accelerated proximal-gradient method (FISTA), with a greedy outer loop that searches over a grid of decay values. The COE model is estimated separately with an iterative simulation-error scheme adapted from prior instrumental-variable methods for irregularly sampled continuous-time systems. Future event times for both pipelines are simulated with Ogata's thinning algorithm. The dataset is split into three equal, time-ordered subsets used respectively for hyperparameter tuning, timing-accuracy evaluation, and trading simulation; each subset is divided into 32-minute periods, 50 of which are randomly sampled and each split into a 30-minute training window and a 2-minute test window. Timing accuracy is judged by the median relative prediction error of the forecast event time; return-sign accuracy is judged by classification accuracy; trading performance is judged from simulated cumulative capital under a fixed-notional long/short rule driven by the predicted sign, assuming no transaction costs.

## Results

- MHP had the lowest median relative prediction error (RE) for the next mid-price-change time across all training-time settings tested, reaching 0.747 at a 300-second training window, versus a best of 1.525 for the univariate Hawkes process (at an 1800-second window) and 4.098 for the naive baseline.
- A 30-minute COE training window gave 0.671 return-sign accuracy, versus 0.640 for a 15-minute window and 0.631 for a 5-minute window.
- Using LOB depth level 5 for the Base Imbalance gave the best return-sign accuracy (0.671), versus 0.667 at level 10, 0.665 at level 3, and 0.635 at level 15.
- Across 50 test scenarios in the January 2024 sample, HawkesTime's average accuracy (0.67) beat HawkesSign's (0.55) and the moving-average benchmark, and only HawkesTime produced a consistently rising simulated cumulative profit.
- HawkesTime needed more average training time (6.9s vs 4.9s) but less average inference time (1.8ms vs 2.6ms) and fewer parameters (24 vs 36) than HawkesSign.
- HawkesTime's advantage over HawkesSign held in a July 2025 robustness test on BTC/USD, despite average BTC price rising from about $42,900 (std 1,941) to $114,172 (std 5,041) and minimum tick size widening from $1 to $10, and it also held on a July 2025 ETH/USD sample, with a narrower gap.
- The Pearson correlation between Base Imbalance and next return was only -0.11 at the tick level but -0.97 once observations were grouped into deciles of Base Imbalance.

## Limitations

- The trading simulation ignores transaction costs, so reported profits are described by the authors as an upper bound rather than realizable returns.
- The study does not filter out periods of possible spoofing activity, so results may reflect market conditions where manipulative order flow is present.
- Reported training and inference times are described as conservative upper bounds because the current implementation bridges separate Python and MATLAB components rather than being a single optimized pipeline.
- Reader note: the robustness check covers only one additional month and one additional asset (ETH/USD), both drawn from the same July 2025 period.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/queue-imbalance|Queue Imbalance]]
- [[entities/daniele-marazzina|Daniele Marazzina]]
- [[entities/simone-formentin|Simone Formentin]]

## Citation

Davide Raffaelli, Raffaele Giuseppe Cestari, Daniele Marazzina, Simone Formentin (2026). Forecasting Bitcoin price movements using multivariate Hawkes processes and limit order book data. Decisions in Economics and Finance.

DOI: 10.1007/s10203-026-00570-z

Text ingested: `markdown_output/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes.md`, converted from `raw/ofi-event-clock/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, LOB data analysis, Hawkes/COE methodology, all experimental-results subsections (temporal accuracy, return-sign accuracy, trading simulation, robustness), and the discussion/conclusion.
<!-- AUTHORED REGION END -->