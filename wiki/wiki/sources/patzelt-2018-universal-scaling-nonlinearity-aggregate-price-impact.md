---
authors:
- Felix Patzelt
- Jean-Philippe Bouchaud
content_hash: sha256:6ad94b373f9e6b2e16df0098aa0abbd9fcd437b1190356438a79788e8eb7a995
created: 2026-09-27 01:47:00+00:00
page_id: sources/patzelt-2018-universal-scaling-nonlinearity-aggregate-price-impact
page_type: source
related:
- concepts/trade-clock
- concepts/price-impact
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/square-root-law
- concepts/market-microstructure
- concepts/long-memory
- concepts/metaorder
- entities/jean-philippe-bouchaud
revision_id: 1
schema_version: 2
source_hash: sha256:c514321c9e3e0b3eb6893bf47377fac3b3d35841bb2e266fbba53f3ee53b0723
source_path: markdown_output/patzelt-2018-universal-scaling-nonlinearity-aggregate-price-impact.md
source_type: paper
tags:
- price-impact
- order-flow
- market-microstructure
- scaling-laws
- high-frequency-data
- multi-asset
- limit-order-book
- clock-trade
- asset-multi
- harvest-relevant
title: Universal scaling and nonlinearity of aggregate price impact in financial markets
updated: '2026-09-27T01:47:00Z'
uuid: 0341a1df-592c-5f1f-ab08-23b55d91d1f5
year: 2018
---

<!-- AUTHORED REGION START -->
# Universal scaling and nonlinearity of aggregate price impact in financial markets

## Summary

The paper asks how the average price impact of many market orders, aggregated together over a window of trades, behaves as that window grows, and why extreme buy or sell order-sign imbalance does not translate into large price moves.

Using anonymized trade-level tick data for 12 US Nasdaq technology stocks, 13 high-turnover Nasdaq OMX Nordic stocks, and 6 EUREX interest-rate and index futures, the authors reconstruct mid-prices and trade signs and compute two conditional-average-return curves for many different trade-count window sizes: the aggregate-volume impact (return conditioned on total signed traded volume in the window) and the aggregate-sign impact (return conditioned on the sum of trade signs in the window). Each curve is fit with a two-parameter sigmoidal scaling function after rescaling the volume/sign axis and the return axis by separate power laws of the window size, and the resulting rescaling exponents are compared to Hurst exponents of returns, signed volumes, and trade signs. The authors also measure the probability that a trade changes the mid-price as a function of the local average trade sign.

For window sizes above roughly 10 trades, the rescaled impact curves for all instruments collapse onto one master curve per aggregation type. The aggregate-volume impact curve saturates for large imbalances rather than growing without bound, contradicting a simple linear-impact assumption, while the aggregate-sign impact curve instead reverts back toward zero at extreme sign imbalances, meaning strongly one-sided order flow is on average followed by very small price changes. The authors trace this to episodes where the price is effectively pinned near a level by large opposing liquidity; correspondingly, the probability that a trade moves the mid-price falls toward zero as local order-sign bias grows, tracing an almost invariant tent-shaped curve across window sizes and instruments.

What is new is showing a single rescaled master curve for aggregate impact holding simultaneously across many intraday timescales and three quite different trading venues and instrument types, and quantitatively documenting that price-change probability and local order-sign bias offset each other almost exactly. The authors read this as evidence that markets operate in a continuous state of bilateral adaptation between liquidity takers and providers rather than a fixed linear-impact regime, and they leave a full theoretical (propagator-model) explanation of the master curve to a companion paper.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are formed by grouping consecutive individual trades (not calendar time) into windows of N successive same-day transactions, for a wide range of window sizes N from about 10 trades up to roughly a full day of trading. The 'horizon' being studied is the trade-count window N itself: the paper examines how the conditional average return and its scale change as N is varied, rather than forecasting a single fixed future point in time.

## Data

- **Asset class:** Several asset classes
- **Instruments:** 12 US Nasdaq technology stocks (including Apple and Microsoft), 13 high-turnover Nasdaq OMX Nordic stocks, and 6 EUREX futures (BOBL, BUND, DAX, EUROSTOXX, SCHATZ, SMI)
- **Venue:** Nasdaq; Nasdaq OMX Nordic (Stockholm, Helsinki, Copenhagen); EUREX
- **Period:** Nasdaq stocks 2011 to 2016; OMX stocks October 2011 to September 2015; EUREX futures October 2014 to end of 2015
- **Granularity:** Individual trades with millisecond timestamps, aggregated into windows of N consecutive same-day trades

## Features and Measures

- **Aggregate-volume impact.** The average mid-price return over a window of N consecutive same-day trades, conditioned on the total signed traded volume in that window.
- **Aggregate-sign impact.** The average mid-price return over a window of N trades, conditioned instead on the sum of the trade signs in that window, i.e. how one-sided the buying or selling was, independent of size.
- **Sigmoidal master-curve scaling function.** A two-parameter sigmoidal function that, once the volume/sign axis and the return axis are each rescaled by power laws of the window size N, fits the aggregate impact curve for effectively any window size and instrument.
- **Hurst exponent (of returns, signed volume, and trade signs).** An exponent describing how the standard deviation of the sum of N successive values of a variable scales with N, used here to relate the impact-curve rescaling exponents to the underlying persistence of returns, order volumes, and trade signs.
- **Price-change probability curve.** The probability that the mid-price differs between two consecutive trades, plotted against the mean trade sign within the window; it is highest near a balanced order flow and falls toward zero for strongly one-sided flow.
- **Implied-spread parameter.** A measure computed from the ratio of continuation to alternation price movements, describing how much an instrument's tick size distorts an underlying diffusive price process; small values indicate large-tick instruments.

## Method

For each instrument, trades executed the same day are grouped into windows of N consecutive transactions across a wide range of window sizes; the first and last 30 minutes of each trading day and days with shortened hours are excluded, as are trades priced exactly at the mid-price. For each window size, the conditional average return curve (against total signed volume, and separately against total sign imbalance) is fit with the sigmoidal scaling function by alternating between fitting the curve's shape parameters and its scale factors, using only a random 80 percent of the window sizes in each pass; the resulting volume/return scale factors are then fit as power laws of the window size using robust regression. Hurst exponents for returns, signed volumes, and trade signs are estimated from how the standard deviation of sums of N successive values scales with N, a method the authors found more robust than a rescaled-range analysis given the heavy-tailed distributions involved. The paper is purely empirical: it compares master-curve exponents and shapes across instruments and periods but does not fit or test a structural/theoretical impact model, leaving that to a companion paper.

## Results

- Rescaled aggregate-volume impact curves for window sizes above about 10 trades collapse onto a single master curve per instrument, well described by a sigmoidal function with shape parameters averaging 1.2 and 1.3 across the sample of instruments.
- The volume-impact width exponent averages about 0.75 and the height exponent about 0.5 across instruments (for AAPL specifically, 0.84 and 0.53), so the width of the impact curve grows faster than its height as the window size increases.
- The aggregate-sign impact curve reverts back toward zero at extreme order-sign imbalances rather than saturating, meaning strongly one-sided order flow is on average associated with very small price changes.
- The probability that a trade changes the mid-price falls toward zero as the local trade-sign bias becomes extreme, forming an almost invariant tent-shaped curve for window sizes above roughly 50 trades across all instruments studied.
- Large local order-sign imbalances tend to occur when the price is effectively pinned near a level by opposing liquidity, illustrated by an AAPL episode of more than 100 consecutive market sell orders around trade 9100 moving the mid-price only about half a tick.
- Order-sign persistence (Hurst exponent above 0.7 for order signs) is closely related to the volume-impact and sign-impact width exponents, while the height exponents track the near-diffusive Hurst exponent of returns.
- Instrument tick-size character (the implied-spread parameter) ranges widely across the sample, from about 0.03 to 0.73, and correlates with several of the scaling exponents studied.

## Limitations

- The analysis covers only three trading venues (Nasdaq, Nasdaq OMX Nordic, EUREX), and trade signs are reconstructed from mid-price crossing rather than exchange-labeled for two of the three, though the authors report similar results using exchange-provided signs where available.
- Trader identity is not available in the anonymized data, so the study describes aggregate order-flow impact rather than the impact of any single trader's metaorder.
- The paper is explicitly descriptive rather than explanatory: the authors defer a theoretical or propagator-model account of the master curve to a companion paper.
- Reader note: only intraday windows are studied; overnight and multi-day effects are excluded from the aggregation windows by design.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/square-root-law|square root law]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/long-memory|long memory]]
- [[concepts/metaorder|metaorder]]
- [[entities/jean-philippe-bouchaud|Jean-Philippe Bouchaud]]

## Citation

Felix Patzelt, Jean-Philippe Bouchaud (2018). Universal scaling and nonlinearity of aggregate price impact in financial markets.

DOI: 10.1103/physreve.97.012304

Text ingested: `markdown_output/patzelt-2018-universal-scaling-nonlinearity-aggregate-price-impact.md`, converted from `raw/ofi-event-clock/patzelt-2018-universal-scaling-nonlinearity-aggregate-price-impact.pdf`.

Coverage of this summary: Read the full markdown: abstract, introduction, data description, all results sections (aggregate impact, scaling and Hurst exponents, large order imbalances and pinned prices), the discussion, and the appendices covering single-trade impacts and the multi-instrument impact and change-probability curves.

Known problems with the input: No publication venue or explicit publication year is printed on this document; year is taken from the job file's year_hint as instructed; Most equations and all figures are replaced by '==> picture... intentionally omitted <==' placeholders in the markdown conversion, so equation forms and figure content are described from the surrounding prose rather than reproduced exactly; Decimal numbers throughout the markdown are split by the PDF converter (e.g. '1 _._ 2' for 1.2); these are treated as present per the extraction instructions and written in standard decimal form.
<!-- AUTHORED REGION END -->