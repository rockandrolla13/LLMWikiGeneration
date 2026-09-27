---
authors:
- Vygintas Gontis
content_hash: sha256:055635d1cd1dab7526b9941570c36f0631189a1639f637df2f50b0cdd4974b40
created: 2026-09-27 01:47:00+00:00
page_id: sources/gontis-2023-discrete-q-exponential-limit-order-cancellation
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-imbalance
- concepts/long-memory
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/market-microstructure
- concepts/autocorrelation-time-series
revision_id: 1
schema_version: 2
source_hash: sha256:ea475214870478e47a1d105db953671efa260629b885a0cd2ca6be02c1850413
source_path: markdown_output/gontis-2023-discrete-q-exponential-limit-order-cancellation.md
source_type: paper
tags:
- limit-order-book
- order-cancellation
- q-exponential
- tsallis-statistics
- long-memory
- order-disbalance
- lobster-data
- event-time
- clock-event
- asset-equity
- harvest-relevant
title: Discrete q-Exponential Limit Order Cancellation Time Distribution
updated: '2026-09-27T01:47:00Z'
uuid: 1337cba0-c9b5-581d-ad84-f05cee36f220
year: 2023
---

<!-- AUTHORED REGION START -->
# Discrete q-Exponential Limit Order Cancellation Time Distribution

## Summary

The paper asks what statistical distribution governs the time a submitted limit order waits before it is cancelled or executed, and whether that distribution can explain why empirical order-disbalance time series are bounded (mean-reverting) rather than behaving like the unbounded fractional Lévy or ARFIMA processes the author had proposed in earlier work.

Using LOBSTER limit-order-book data reconstructed from NASDAQ TotalView-ITCH messages for ten stocks (NVDA, HD, AMZN, NFLX, MA, LLY, TSLA, ADBE, V, JNJ) over 21 trading days in August 2020, the author measures every limit order's cancellation time (the gap between submission and cancellation/execution) in discrete event time, fits the empirical histograms with a discrete Tsallis q-exponential probability mass function via maximum likelihood, and builds an order-disbalance series that pairs each order's volume with its cancellation time. Mean-squared-displacement and Hurst-exponent estimates, plus an auto-codifference analysis, are used to characterize memory in the order-disbalance series, a pure limit-order-submission series, and reshuffled control versions of both; the fitted q-exponential cancellation-time distribution is then combined with a fractional-Lévy-noise volume-generating process to build an artificial order-disbalance model for comparison against the empirical series.

The discrete q-exponential distribution fits cancellation times well and consistently across all ten stocks, with mean fitted parameters lambda = 0.3 and q = 1.5. The order-disbalance series that includes cancellations is bounded and anti-persistent (Hurst well below 0.5), while the pure limit-order-submission series (excluding cancellations) is unbounded and persistent, consistent with fractional-Lévy-stable-motion-like behavior with a stability parameter around alpha = 1.8. The artificial model built from a q-exponential cancellation-time process and a fractional-Lévy volume process reproduces the empirical MSD, Hurst exponent and auto-codifference reasonably closely.

This is presented as a new stylized fact about limit order cancellation times, and as a specific mechanism (pairing of opposite-sign volume increments through cancellation) that generates the previously puzzling bounded, anti-persistent behavior of order-disbalance series, resolving contradictions the author found when applying fractional Lévy stable motion directly to order disbalance in earlier work.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Time is measured in event steps: every message that updates the limit order book (submission, cancellation, execution) advances the clock by one integer step, avoiding calendar-time seasonality. Cancellation time for an order is the number of such event steps between its submission and its cancellation or execution; the order-disbalance and limit-order-flow series are built by summing signed order volumes over this same event-time index rather than over calendar time.

## Data

- **Asset class:** Equities
- **Instruments:** Ten NASDAQ-traded stocks: NVDA, HD, AMZN, NFLX, MA, LLY, TSLA, ADBE, V, JNJ
- **Venue:** NASDAQ (via LOBSTER-reconstructed TotalView-ITCH data)
- **Period:** 3 to 31 August 2020 (21 trading days)
- **Granularity:** Full limit order book message-level (event-time) data up to the ten best price levels on both sides

## Features and Measures

- **Discrete Tsallis q-exponential distribution.** A discretized version of the continuous Tsallis q-exponential density, with parameters lambda and q, fit by maximum likelihood to the histogram of limit order cancellation times; it reduces to a geometric distribution as q approaches 1.
- **Order disbalance series X(j).** A running sum, in event time, of the signed volumes of all live limit orders (positive for buy, negative for sell) that have been submitted but not yet cancelled or executed.
- **Limit order flow series XL(j).** A running sum of signed limit order submission volumes only, excluding the cancellation/execution offsets, so the series is not bounded by pairing.
- **Auto-codifference.** A dependence measure for time series with heavy-tailed, alpha-stable increments, used here to quantify memory in the order-disbalance increments and compare it against the theoretical form implied by fractional Lévy noise.

## Method

The author derives a discrete probability mass function from the continuous Tsallis q-exponential density and fits it by maximum likelihood to histograms of limit order cancellation times pooled over 21 trading days for each of ten stocks, checking sensitivity of the fitted parameters to price level and order-volume group. He then reconstructs, from LOBSTER message data, the list of live limit orders at every event step and defines an order-disbalance series as the running signed sum of their volumes, contrasting it with a simplified limit-order-flow series that ignores cancellations.

Memory in these series is characterized using the sample mean squared displacement and two Hurst-exponent estimators (the absolute-value estimator and Higuchi's method), each computed on the raw series and on two randomized control versions - one with only the order-volume sequence reshuffled, one with all increments reshuffled - to isolate how much of the measured dependence comes from the volume sequence versus the cancellation-time pairing. A separate auto-codifference calculation is fit to the theoretical asymptotic form implied by fractional Lévy noise to estimate a memory parameter d. Finally, an artificial order-disbalance model is simulated by combining an ARFIMA-generated fractional-Lévy-stable volume sequence with a cancellation-time sequence drawn from the fitted q-exponential distribution, and its MSD, Hurst-exponent and auto-codifference statistics are compared against the empirical series for three stocks.

## Results

- The mean fitted discrete q-exponential parameters across the ten stocks are lambda = 0.3 and q = 1.5
- Per-stock fitted values range from lambda = 0.14 (JNJ) to lambda = 0.5 (ADBE), and from q = 1.45 (MA) to q = 1.54 (TSLA)
- The limit-order-flow series stability parameter alpha, fit to the tail of the volume distribution, is stable around 1.8 for all ten stocks, ranging from 1.79 to 1.80
- Memory-parameter estimates for the limit-order-flow series across three methods are similar for each stock, for example dMSD = 0.30, dCD = 0.29 and dH = 0.32 for NVDA
- The artificial model with memory parameter d = 0.2 closely matches stock MA (model Hurst H(X) = 0.20 versus MA's 0.17), while d = 0.3 is closer to NFLX and TSLA
- Auto-codifference fits give an average memory parameter close to d = 0.3 for NFLX, with daily estimates dCD = {0.28, 0.31, 0.26, 0.34, 0.28}

## Limitations

- Reader note: the cancellation-time and order-disbalance analysis covers only ten large NASDAQ stocks over one month (August 2020), so it is unclear whether the fitted q-exponential parameters generalize to other stocks, periods or venues.
- The paper notes that the q to 1 limit of an alternative discrete PMF form is unclear, so only one specific PMF form is used throughout.
- The Lévy-stable fit to limit-order volumes is only approximate, since the empirical volume distribution shows a distinct resonance structure not captured by a stable distribution.
- Reader note: the artificial model's cancellation-time and volume sequences are generated independently, so any real dependence between an order's size and how long it survives before cancellation is not modeled.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/long-memory|long memory]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]

## Citation

Vygintas Gontis (2023). Discrete q-Exponential Limit Order Cancellation Time Distribution.

DOI: 10.3390/fractalfract7080581

Text ingested: `markdown_output/gontis-2023-discrete-q-exponential-limit-order-cancellation.md`, converted from `raw/ofi-event-clock/gontis-2023-discrete-q-exponential-limit-order-cancellation.pdf`.

Coverage of this summary: Read the full preprint: abstract, introduction, sections 2-7 (distribution definition, cancellation-time empirical fits, order disbalance and limit order flow analysis, artificial model, discussion/conclusion), all tables, and the abbreviations list.

Known problems with the input: Most equations are rendered as omitted images in the markdown (e.g. the PMF definitions and the MSD/Hurst formulas); their forms were inferred only from the surrounding prose, not verified against the actual displayed equations; OCR artifacts split several decimals across characters (e.g. '0 _._ 3' for 0.3); these were read as the single intended number, consistent with the stated convention for split decimals.
<!-- AUTHORED REGION END -->