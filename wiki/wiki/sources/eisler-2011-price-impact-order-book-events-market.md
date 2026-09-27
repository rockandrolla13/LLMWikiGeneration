---
authors:
- Zoltan Eisler
- Jean-Philippe Bouchaud
- Julien Kockelkoren
content_hash: sha256:724edbbb7018310e0279b8c12bfc6c3c4a958f894fdb4d577bbfc5d47be63c48
created: 2026-09-27 01:47:00+00:00
page_id: sources/eisler-2011-price-impact-order-book-events-market
page_type: source
related:
- concepts/event-clock
- concepts/price-impact
- concepts/order-flow
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/bid-ask-spread
- concepts/high-frequency-data
- concepts/autocorrelation-time-series
- concepts/trade-classification
- entities/zoltan-eisler
- entities/jean-philippe-bouchaud
revision_id: 1
schema_version: 2
source_hash: sha256:9c4a2f25c9af31c9f01810d9a359478f7a2f61774032c1103b3a8c8e87f73a74
source_path: markdown_output/eisler-2011-price-impact-order-book-events-market.md
source_type: paper
tags:
- order-book-events
- price-impact
- market-orders
- limit-orders
- cancellations
- tick-size
- autoregressive-model
- spread-dynamics
- clock-event
- asset-equity
- harvest-relevant
title: 'The price impact of order book events: market orders, limit orders and cancellations'
updated: '2026-09-27T01:47:00Z'
uuid: 3bf7d20c-0775-511d-8193-8d2f44c5383d
year: 2018
---

<!-- AUTHORED REGION START -->
# The price impact of order book events: market orders, limit orders and cancellations

## Summary

The paper asks how market orders, limit orders and cancellations at the best quotes jointly drive price changes, since prior price-impact studies mostly looked at market orders alone and left the impact of limit orders and cancellations largely unexamined.

Using event-level order book data for a sample of NASDAQ stocks split into large-tick and small-tick groups, the authors classify every event into six types (market order, limit order, cancellation, each further split by whether it changes the best price) and measure the autocorrelations between these event types as well as their response functions on the price. They invert these empirical correlation and response functions to recover the 'bare' impact each event type would have if it occurred in isolation, first under a model where each event type's impact is constant over time, and then, to fix the discrepancies found for small-tick stocks, under a linear regression model that lets the size of the price gap behind the quotes depend on recent signed order flow.

For large-tick stocks, a simple constant, permanent-impact-per-event-type model reproduces both the measured response functions and the long-run price variance well, because the spread and the gaps behind the best quotes barely fluctuate for these stocks. For small-tick stocks the same constant-impact model underestimates the long-run price variance, and the gap between model and data closes once the model lets realized gaps and future event rates depend, through a linear regression, on the recent history of signed order flow.

What is new is a single, largely model-free empirical framework that treats market orders, limit orders and cancellations symmetrically, extracts each type's individual bare impact, decomposes an event's total effect into an instantaneous jump plus an induced change in future event rates and gap sizes, and extends the same logic to describe bid-ask spread dynamics in an appendix.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Time is measured in events, defined as any change to the bid or ask price or to the volume quoted at those prices; physical clock time is not used as the unit of analysis. Lags (denoted ell) between events are counted as numbers of events. The paper notes that the signed event-direction autocorrelation dies out after 10-100 trades, corresponding to typically 10 seconds of physical trading time, while the signed event-side autocorrelation decays much more slowly, as a power law.

## Data

- **Asset class:** Equities
- **Instruments:** 14 randomly selected liquid stocks traded on NASDAQ, split into a large-tick group (e.g. AMAT, CMCSA, CSCO, DELL, INTC, MSFT, ORCL) and a small-tick group (e.g. AAPL, AMZN, APOL, COST, ESRX, GILD).
- **Venue:** NASDAQ
- **Period:** 03/03/2008 to 19/05/2008, a total of 53 trading days; the authors state similar results were also checked on other markets and periods (CME futures, US Treasury bonds, London Stock Exchange) but are not reproduced in the paper.
- **Granularity:** Event-level best-quote data (trades and quotes), classified into six event types by whether the event is a market order, limit order or cancellation and whether it changes the best price; only the usual trading hours 9:30-16:00 are used.

## Features and Measures

- **Event sign (epsilon) and event side (s).** Two sign conventions for each event: epsilon reflects the event's expected long-term directional effect on price, while s reflects which side of the book (bid or ask) the event occurred on; the two differ because limit orders add volume rather than remove it.
- **Six event types (MO0, MO', LO0, LO', CA0, CA').** A classification of every order book event into market order, limit order or cancellation, each split into a version that changes the best price (prime) and one that does not (superscript 0).
- **Signed event-event correlation function.** The normalized correlation between the signed indicator of one event type and the signed indicator of another event type at a given lag, used to characterise how event types influence each other over time.
- **Response (impact) function.** The expected price change some number of events after an event of a given type, normalized by that event type's unconditional probability.
- **Bare event propagator.** The individual, 'undressed' impact an event type would have on the price if it occurred alone, obtained by inverting the system of equations relating response functions to correlation functions.
- **Quote gap history-dependence regression.** A linear regression of the realized quote gap and of future event indicators on past signed order flow, used to model how liquidity fluctuations make single-event impact appear time-dependent for small-tick stocks.

## Method

The approach is empirical and phenomenological rather than built from an agent-based economic model. Every observed order book event at the best quotes is assigned a type (one of six categories) and a sign, and the paper measures signed and unsigned event-event correlation functions together with the response function of price to each event type. These empirical quantities are related through an extension of an earlier propagator-based impact model, and the system is inverted (using a cutoff of L=1000 events, accurate to about lag 300) to solve for the underlying bare propagator of each event type from the observed response and correlation functions; this is also related formally to Hasbrouck's Vector Autoregression framework.

Two versions of the impact model are then tested against the data. A constant/permanent impact model replaces each event's time-varying gap by its long-run average realized gap and is checked against both the response functions and the diffusion curve D(l)/l (the variance of the price change per lag). Because this constant model fits large-tick stocks well but not small-tick stocks, the authors extend it with a linear regression (a VAR-type kernel) that lets the realized gap and the future event indicators depend on past signed order flow; this final model is fit and validated by comparing predicted and empirical response functions and diffusion curves for both stock groups, and the same machinery is extended in an appendix to model bid-ask spread dynamics.

## Results

- Events that change the best price occur with about 3% combined probability for large-tick stocks but with up to 40% probability for small-tick stocks.
- The signed event-side autocorrelation decays as a power law with exponent gamma approximately 0.7, while the signed event-direction autocorrelation is short-ranged, dying out after 10-100 trades (about 10 seconds of trading).
- A constant, non-fluctuating impact model reproduces the empirical diffusion curve D(l)/l well for large-tick stocks but fits small-tick stocks poorly; the fit for small-tick stocks improves once gaps are allowed to depend on past order flow.
- For price-moving events, the realized quote gap conditional on the event exceeds the unconditional average gap; the ratio reaches 1.85 for ESRX (a small-tick stock) versus close to 1.00 for large-tick stocks such as AMAT.
- A model using only market-order impact with a single non-fluctuating propagator accounts for only about two thirds (2/3) of the observed long-term volatility for small-tick stocks.
- The bare impact of limit orders is measurably smaller than that of market orders, particularly for small-tick stocks.

## Limitations

- The authors state that events deeper in the order book and events occurring on other trading platforms (liquidity fragmentation) are unobserved and can still 'dress' the impact of the observed best-quote events.
- The model neglects the dependence of impact on trade volume, treating events only by type rather than by size.
- The authors note that the simplified spread model in Appendix A produces an exponential autocorrelation decay, in contrast to the long-memory decay actually observed in the data.
- Reader note: the sample is limited to 53 trading days in a single 2008 window on NASDAQ; no discussion is given of robustness across other market regimes within the paper's main text.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-flow|order flow]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/trade-classification|trade classification]]
- [[entities/zoltan-eisler|Zoltán Eisler]]
- [[entities/jean-philippe-bouchaud|Jean-Philippe Bouchaud]]

## Citation

Zoltan Eisler, Jean-Philippe Bouchaud, Julien Kockelkoren (2018). The price impact of order book events: market orders, limit orders and cancellations.

DOI: 10.1080/14697688.2010.528444

Text ingested: `markdown_output/eisler-2011-price-impact-order-book-events-market.md`, converted from `raw/ofi-event-clock/eisler-2011-price-impact-order-book-events-market.pdf`.

Coverage of this summary: Read the full markdown from the abstract through the conclusion and references, including both appendices (spread dynamics in Appendix A and additional correlation-function plots in Appendix B).

Known problems with the input: The document header prints a revision date '(Dated: October 23, 2018)'; this is used for the year field per instructions, though the job file's slug and year_hint (2011) suggest an earlier working-paper version, and the earliest publication year is not stated anywhere in this markdown; No journal or working-paper series name is printed anywhere in the read markdown; venue is left blank.
<!-- AUTHORED REGION END -->