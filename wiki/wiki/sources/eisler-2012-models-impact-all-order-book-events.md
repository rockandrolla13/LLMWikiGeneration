---
authors:
- Zoltán Eisler
- Jean-Philippe Bouchaud
- Julien Kockelkoren
content_hash: sha256:9e8f95214616bb7deadffe1bb07d1291304b475a0049be4074959f456095053f
created: 2026-09-27 01:47:00+00:00
page_id: sources/eisler-2012-models-impact-all-order-book-events
page_type: source
related:
- concepts/event-clock
- concepts/price-impact
- concepts/limit-order-book
- concepts/order-flow
- concepts/market-microstructure
- concepts/high-frequency-data
- entities/zoltan-eisler
- entities/jean-philippe-bouchaud
revision_id: 1
schema_version: 2
source_hash: sha256:456025911424f20b9ed9891d2fc0c512f4ab13dbfb813b4c271476984b9a4ff7
source_path: markdown_output/eisler-2012-models-impact-all-order-book-events.md
source_type: paper
tags:
- price-impact
- limit-order-book
- order-flow
- market-microstructure
- event-time
- impact-modeling
- clock-event
- asset-equity
- harvest-relevant
title: Models for the impact of all order book events
updated: '2026-09-27T01:47:00Z'
uuid: 1b7615a9-c0ba-537e-9373-ff73b64d3f5f
year: 2018
---

<!-- AUTHORED REGION START -->
# Models for the impact of all order book events

## Summary

The paper extends market-impact models beyond market orders alone to include limit orders and cancellations, since these order types also directly move the mid-price. It asks how to model the temporary and permanent impact of all six order-book event types (market orders, limit orders and cancellations, each split into price-changing and non-price-changing) and how well such models reproduce the empirical price-diffusion curve.

Two model classes are proposed. The transient impact model (TIM) assumes each event type carries its own time-dependent temporary impact function, calibrated from empirical response and event-correlation functions. The history-dependent impact model (HDIM) instead assumes only price-changing events have a direct effect, whose size (a 'gap') depends on the past order flow of all event types through a lag-dependent influence matrix, so it also captures how earlier events change the size of later price jumps.

Tested on liquid NASDAQ stocks split into large-tick and small-tick groups, the constant-gap version of HDIM matches large-tick data well. For small-tick stocks, TIM reproduces the empirical price-diffusion curve closely, while HDIM, calibrated with an approximate factorization of three-point correlations, overestimates price diffusion, even though HDIM's underlying mechanism (that aggressive same-side orders shrink same-sign impact but enlarge opposite-sign impact) is confirmed.

The paper's contribution is showing that a theoretically more consistent, richer model (HDIM) can perform worse in practice than a simpler, formally inconsistent one (TIM), because HDIM's calibration relies on an uncontrolled Gaussian-style factorization approximation for three-point correlations; the authors flag this as an open problem for future calibration work.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed by event time, counting order book events (market orders, limit orders and cancellations at the best quotes) rather than clock time; six event types are distinguished (price-changing and non-price-changing market orders, limit orders and cancellations). The response and price-diffusion functions are evaluated as a function of the number of events elapsed after an initial event, excluding the first 30 and last 40 minutes of each trading day.

## Data

- **Asset class:** Equities
- **Instruments:** 14 randomly selected liquid stocks, split into large-tick and small-tick groups
- **Venue:** NASDAQ (results also stated to have been verified on CME Futures, US Treasury Bonds and the London Stock Exchange, without reported figures)
- **Period:** 03/03/2008 to 19/05/2008, 53 trading days
- **Granularity:** Event-by-event order book data (market orders, limit orders, cancellations at best bid/ask), excluding the first 30 and last 40 minutes of each trading day

## Features and Measures

- **Response function.** The average, sign-adjusted price change a given number of events after an event of a particular type, normalized by that event type's unconditional probability; measures the expected directional price impact of each event type.
- **Bare impact function (TIM propagator).** In the TIM, the time-dependent 'bare' impact assigned to a single event of a given type, inferred by inverting the observed response and event-correlation functions.
- **Influence matrix.** In the HDIM, a lag-dependent matrix describing how much an event of one type changes the size of the price 'gap' associated with a later price-changing event of the same sign in the future.
- **Six order-book event types.** Classification of book events into market orders, limit orders and cancellations, each split into price-changing and non-price-changing sub-types, used as the basic unit for building impact models.
- **Price diffusion curve.** The variance of the price change over a number of events, used as the main empirical target that both TIM and HDIM try to reproduce.

## Method

Both models are calibrated stock by stock from event and price data: TIM's impact function is obtained by inverting a system relating it to the observed response functions and event-event correlation functions; HDIM's influence matrix is obtained from the same response matrices under an approximation that factorizes three- and four-point correlations as if the underlying variables were Gaussian.

Performance is judged by how closely each model's predicted price-diffusion curve, derived analytically from the fitted impact function or influence matrix, matches the empirically measured price-diffusion curve, separately for large-tick and small-tick stocks; the authors also run a historical simulation feeding the true sequence of past events through the fitted HDIM to check the factorization approximation independently of the diffusion-curve comparison.

## Results

- For large-tick stocks, where the bid-ask spread is almost always one tick, the constant-gap approximation of HDIM matches the empirical response functions and price diffusion well; TIM performs worse here because small numerical errors in calibrating its impact function are amplified in the diffusion formula.
- For small-tick stocks, TIM's predicted price diffusion agrees closely with the data at long lags, though it underestimates fluctuations at short lags.
- For small-tick stocks, the naively calibrated HDIM overestimates price diffusion by about 15% at large lags; multiplying all calibrated influence-matrix values by a factor of 3 improves the fit substantially, though some discrepancy remains, and a further constant of about 0.04 ticks squared is needed to match short-lag data.
- Aggressive, price-changing market orders tend to reduce ('harden') the gap for a following same-side price-changing event and increase it for an opposite-side one, whereas small, non-price-changing market orders tend to 'soften' the book.
- Events that change the best price account for about 3% of events for large-tick stocks but up to 40% for small-tick stocks.
- A historical simulation using the fitted HDIM reproduces the response functions given the calibrated influence matrix, but this does not resolve the discrepancy in price diffusion, indicating the problem lies in the calibration itself rather than in the diffusion formula's approximation.

## Limitations

- Authors note the models neglect volume dependence of impact, events deeper in the order book and on other trading platforms, and possible higher-order history dependence in the gap dynamics beyond a quadratic term.
- HDIM's calibration relies on an uncontrolled Gaussian-style factorization of three-point correlation functions, which the authors show is not very accurate.
- Reader note: the empirical diffusion-curve results are reported for a set of 14 stocks on a single exchange over a 53-trading-day window; broader validation on other markets is mentioned only qualitatively, without reported diffusion-curve results.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/price-impact|price impact]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/zoltan-eisler|Zoltán Eisler]]
- [[entities/jean-philippe-bouchaud|Jean-Philippe Bouchaud]]

## Citation

Zoltán Eisler, Jean-Philippe Bouchaud, Julien Kockelkoren (2018). Models for the impact of all order book events.

DOI: 10.1002/9781118673553.ch5

Text ingested: `markdown_output/eisler-2012-models-impact-all-order-book-events.md`, converted from `raw/ofi-event-clock/eisler-2012-models-impact-all-order-book-events.pdf`.

Coverage of this summary: Read the entire paper end to end, including the introduction, both model derivations (TIM and HDIM), the data and calibration sections for large- and small-tick stocks, the conclusion, and Appendix A.

Known problems with the input: The paper's own header prints '(Dated: June 4, 2018)', which was used as the printed year even though the job's year_hint was 2012 and the cited references only run through 2011, suggesting the 2018 date may be an automatically stamped compile/revision date rather than the paper's original year; flagged here rather than silently resolved.
<!-- AUTHORED REGION END -->