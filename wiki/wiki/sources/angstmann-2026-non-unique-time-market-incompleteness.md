---
authors:
- Chris Angstmann
- Tim Gebbie
content_hash: sha256:dcdff65b6f29d83b7c6598d44e3a93796e6139d50369639286fb9055d469d234
created: 2026-09-27 01:47:00+00:00
page_id: sources/angstmann-2026-non-unique-time-market-incompleteness
page_type: source
related:
- concepts/sampling-clocks
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/order-flow
- concepts/hawkes-processes
- concepts/market-microstructure-noise
- concepts/limit-order-book
- concepts/event-clock
- concepts/trade-clock
- entities/tim-gebbie
revision_id: 1
schema_version: 2
source_hash: sha256:06a7fe5dad591e6bb17f83cf9dc54704a4befe581fcb63d590a815fdf55b797b
source_path: markdown_output/angstmann-2026-non-unique-time-market-incompleteness.md
source_type: paper
tags:
- event-time
- market-incompleteness
- ctrw
- dtrw
- no-arbitrage
- clock-choice
- epps-effect
- market-microstructure-theory
- clock-compares
- asset-none
- harvest-relevant
title: Non-unique time and market incompleteness
updated: '2026-09-27T01:47:00Z'
uuid: c6d3ebfb-c4ae-5404-b1f1-95e8cd0fe4b9
year: 2026
---

<!-- AUTHORED REGION START -->
# Non-unique time and market incompleteness

## Summary

The paper asks whether financial markets are better described as a single latent price process running in calendar time, or as a discrete event system (orders, trades, quotes, cancellations) from which any continuous-time price process is only an emergent approximation. It contrasts the price-first tradition (Bachelier, Black-Scholes, Harrison-Kreps martingale pricing) with an event-first tradition rooted in market microstructure and point-process models of order flow.

Methodologically the paper is a conceptual and mathematical synthesis rather than an empirical study: it traces the history of stochastic time in finance from Clark's business-time subordination model, through the transaction-clock and volume-clock literature (Epps and Epps, Copeland, Tauchen and Pitts, Harris, Ane and Geman), to autoregressive conditional duration and Hawkes-process models of trade timing, and then to continuous-time random walk (CTRW) and discrete-time random walk (DTRW) constructions. It uses this lineage to re-derive no-arbitrage, no-dynamic-arbitrage, and risk-neutral pricing results directly in event time, without assuming a global calendar-time filtration.

The main claim is that the map from a discrete event system to any continuum-time limit is not unique: different waiting-time distributions and synchronization choices can yield different effective continuous-time models, such as ordinary diffusion, subordinated Brownian motion, or fractional diffusion. The authors call this representation-level incompleteness, a form of market incompleteness one level below the usual claim-spanning incompleteness, because the market may not even fix a unique clock or state description.

What is new is less a formal theorem than a reframing: known results, including Clark's subordination model, the Epps effect, and DTRW non-uniqueness results, are assembled into an explicit argument that calendar time is a useful but non-canonical low-frequency approximation, with effective completeness emerging only at coarser, aggregated horizons.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper is a conceptual comparison, not an empirical test, of clocks used in finance: calendar time (classical semimartingale models), event time (a discrete counting sequence of orders, trades, quotes, cancellations), business time (Clark's activity-linked stochastic clock), transaction-count time (Ane and Geman's cumulative trade count), and volume time (cumulative trading volume). It argues that the map from any discrete event clock to a calendar-time continuum limit, via CTRW or DTRW constructions, is not unique, so no single clock or resulting continuous-time representation is canonical.

## Data

- **Asset class:** No data (theory or survey)
- **Instruments:** not stated
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated

## Features and Measures

- **business time (stochastic subordination).** Price changes are modelled as increments in a random clock tied to trading activity rather than uniform calendar time, following Clark's original subordination model.
- **transaction clock (trade-count time).** Cumulative number of trades used as the time index for returns, proposed by Ane and Geman as an alternative to volume for recovering approximate normality.
- **volume clock.** Cumulative trading volume used as the mixing or time variable for security price changes, following Epps and Epps and later authors linking return variance to trading activity.
- **event-time index.** A discrete counting sequence of market events (orders, trades, quotes, cancellations) used as the primitive index for prices and trading strategies, in place of continuous calendar time.

## Method

The paper is a conceptual and mathematical review rather than an empirical study. It draws a strict distinction between the price-first ontology, in which a single latent continuous-time semimartingale is primitive, and the event-first ontology, in which orders, trades, quotes and cancellations are primitive and price is an emergent, derived object. It traces the historical lineage from Clark's business-time subordination, through the mixture-of-distributions and transaction-clock literature, to autoregressive conditional duration (Engle and Russell) and Hawkes-process models of trade and quote timing, and then to continuous-time random walk (CTRW) and discrete-time random walk (DTRW) constructions.

Using this lineage, the authors revisit three pricing-theory results, no-arbitrage, no-dynamic-arbitrage, and risk-neutral or martingale pricing, and show each can be restated with predictable strategies and gains defined over a discrete event filtration, without assuming a global calendar-time semimartingale structure. They then argue, drawing on DTRW results by Angstmann et al. and Nichols et al., that the map from a discrete event system to a continuum limit is not generally unique: different waiting-time laws and synchronization schemes can produce different effective continuous-time models. No dataset is analysed and no predictive or statistical test is run; the argument is evaluated by internal consistency with the cited no-arbitrage, duration, and point-process literature.

## Results

- No-arbitrage and no-dynamic-arbitrage can each be formulated directly in event time, indexed by a discrete counting sequence, without assuming a global calendar-time filtration.
- The map from a discrete event system to a continuum limit (via CTRW or DTRW) is not unique; different waiting-time laws and synchronization schemes can yield different effective continuous-time models, including ordinary diffusion, subordinated Brownian motion, or fractional diffusion.
- This non-uniqueness is proposed as 'representation-level incompleteness', a form of market incompleteness the authors argue is more foundational than the standard claim-spanning notion of incompleteness.
- The Epps effect (decline in measured cross-asset correlation as sampling interval shortens) is reinterpreted as evidence that dependence is itself clock-relative, rather than only a sampling bias to be corrected.
- Distinct clocks proposed in the literature, calendar time, transaction-count time, volume time, and event time, are argued not to be generally equivalent to one another.
- Coarse-grained calendar-time models can still work well for lower-frequency portfolio construction and risk management; the authors describe this as 'effective completeness' emerging from aggregation even though the underlying event system is irregular.
- A risk-neutral pricing measure is argued to be attached to a chosen event-to-continuum representation rather than to the market in an absolute, representation-independent sense.

## Limitations

- Reader note: the paper presents no new dataset, empirical test, or formal proof; it is a literature synthesis and conceptual argument.
- Reader note: the central claims (clock non-equivalence, representation-level incompleteness) are argued qualitatively rather than established by a new mathematical theorem specific to this paper.
- The argument depends on the DTRW/CTRW non-uniqueness results of other cited papers (Angstmann et al., Nichols et al.) rather than a self-contained derivation within this paper.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/event-clock|Event Clock]]
- [[concepts/trade-clock|Trade Clock]]
- [[entities/tim-gebbie|Tim Gebbie]]

## Citation

Chris Angstmann, Tim Gebbie (2026). Non-unique time and market incompleteness.

DOI: 10.48550/arxiv.2604.23608

Text ingested: `markdown_output/angstmann-2026-non-unique-time-market-incompleteness.md`, converted from `raw/ofi-event-clock/angstmann-2026-non-unique-time-market-incompleteness.pdf`.

Coverage of this summary: Read the entire paper (under): abstract, all numbered sections from the introduction through the conclusion, and the reference list.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->