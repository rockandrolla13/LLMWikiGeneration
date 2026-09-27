---
authors:
- Christopher Angstmann
- Tim Gebbie
content_hash: sha256:022349a6d5d6a035a99ea28470df991d28a222aaa66509f74205a337f9c36bc5
created: 2026-09-27 01:47:00+00:00
page_id: sources/angstmann-2026-event-time-order-flow-memory-operational
page_type: source
related:
- concepts/stochastic-time-change
- concepts/long-memory
- concepts/price-impact
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/square-root-law
- concepts/order-flow
- entities/tim-gebbie
revision_id: 1
schema_version: 2
source_hash: sha256:55a65ecbce68d53c4a013614247b036673017e15bf9a7f3e23d47f8533bc944f
source_path: markdown_output/angstmann-2026-event-time-order-flow-memory-operational.md
source_type: paper
tags:
- market-microstructure
- price-impact
- order-flow-memory
- subordination
- anomalous-diffusion
- theoretical-model
- square-root-law
- clock-time-change
- asset-none
- harvest-relevant
title: Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market
  Observables
updated: '2026-09-27T01:47:00Z'
uuid: fd6b8fc0-6ed7-5400-bf79-dda63a114108
year: 2026
---

<!-- AUTHORED REGION START -->
# Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market Observables

## Summary

The paper asks whether two well-known microstructure regularities, the long memory of trade signs and the concave, roughly square-root law of meta-order price impact, actually live on the same notion of time. The authors argue they do not: sign memory is a property of the sequence of order-book events (event time), while the square-root impact law is a property of continuous diffusive front motion in a locally linear latent order book (operational time), and calendar-time observations are obtained only by subordinating these through the random waiting times between events.

Starting from a discrete-time random-walk bid/ask order book with diffusion, cancellation, replenishment, and signed meta-order forcing, they derive an exact event-time recursion for the bid/ask imbalance field, since the shared reaction term cancels exactly. Taking a continuum limit gives an operational-time reaction-diffusion front equation, which in a locally linear, frozen-background, constant-rate-execution regime reduces to an Abel-kernel Volterra equation whose solution is the square-root impact law. Separately, a renewal-theoretic hidden-order-splitting model for trade signs reproduces the Lillo-Mike-Farmer long-memory autocorrelation exactly on the event clock. Calendar-time versions of both are then obtained by subordinating through the inverse of the cumulative waiting-time process.

The main result is that the square-root impact mechanism is unchanged by the choice of clock, but its calendar-time appearance is not: if waiting times have finite mean, ordinary square-root scaling in calendar time is recovered, while for heavy-tailed, stable-index waiting times the calendar-time impact scale becomes anomalous. This also gives a mechanism by which persistent, long-memory order flow can coexist with only weakly autocorrelated returns, because the event-time signal is filtered through diffusive transport and subordination before it is observed.

What is new is not either empirical law itself, but making explicit that fitting a universal square-root or long-memory law on calendar-time data implicitly bakes in a subordination choice, so cross-asset or cross-venue comparisons of fitted coefficients can be comparing different clock projections of the same underlying mechanism rather than the mechanism itself.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

This is a theoretical/derivational paper, not an empirical study: it defines three linked but distinct clocks. Event time (index m) sequences individual child orders and is where the trade-sign renewal law and the exact bid/ask imbalance recursion live. Operational time (continuum variable u) is where the reaction-diffusion imbalance field and its zero-crossing front evolve under a diffusive scaling limit, and where the square-root impact law is derived for a constant-rate execution schedule. Calendar time (t) is obtained by subordinating event or operational time through the inverse of the cumulative random waiting-time process between order-book events; no forecast horizon or empirical dataset is used anywhere.

## Data

- **Asset class:** No data (theory or survey)
- **Instruments:** not stated
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated (purely analytical/theoretical construction; no empirical order book or trade dataset is used)

## Features and Measures

- **Event-time imbalance field.** The discrete difference between the bid- and ask-side liquidity densities at each log-price lattice site after order-book event m; subtracting the bid and ask update equations cancels their shared diffusion/reaction term exactly, giving a closed recursion for this field.
- **Operational-time reaction front.** The continuum-limit price level at which the imbalance field crosses zero (the model's mid-price proxy), which moves under a diffusion-cancellation-forcing partial differential equation in the locally linear latent-order-book approximation.
- **Event-time sign autocorrelation (Lillo-Mike-Farmer relation).** The exact autocorrelation of consecutive child-order trade signs implied by a sequential hidden-order renewal model with i.i.d. order lengths, reproducing the known long-memory exponent relation for trade signs.
- **Operational-time square-root impact law.** For constant-rate execution over an operational-time interval, the completed meta-order's impact on the reaction front is proportional to the square root of the total executed quantity, derived from an Abel-kernel Volterra front equation.
- **Calendar-time subordination.** The mapping of an event- or operational-time process into calendar time via the inverse of the cumulative waiting-time (renewal) process between order-book events; finite-mean waiting times give linear calendar-clock growth (ordinary square-root impact scaling), while heavy-tailed, stable-index waiting times give anomalous calendar-time scaling.

## Method

The paper is purely analytical: it derives results from a discrete-time random-walk bid/ask order-book model rather than fitting anything to data. The main steps are (i) an exact algebraic cancellation showing the event-time imbalance recursion holds independent of the waiting-time distribution; (ii) a diffusive continuum scaling limit yielding an operational-time reaction-diffusion equation for the imbalance field, which is linearized around its stationary front to obtain an Abel-kernel Volterra equation and the square-root impact law under constant-rate execution; (iii) a separate renewal-theoretic derivation of the exact trade-sign autocorrelation under sequential hidden-order splitting; and (iv) a subordination argument mapping event/operational-time processes into calendar time via the inverse of the cumulative waiting-time process, with asymptotic scaling results distinguished by whether the waiting-time distribution has finite mean or is heavy-tailed with a stable index. Performance here means internal mathematical consistency of the derivations under stated approximations (locally linear, frozen-background, weak-cancellation, constant-rate execution), not a fit to observed data.

## Results

- Subtracting the ask- and bid-side discrete-time random-walk update equations cancels their shared reaction/diffusion term exactly, giving a closed event-time recursion for the bid/ask imbalance field that holds regardless of the waiting-time distribution.
- The event-time trade-sign autocorrelation derived from a sequential hidden-order renewal model exactly reproduces the Lillo-Mike-Farmer long-memory relation.
- In the locally linear, frozen-background latent-order-book limit with constant-rate execution, the operational-time front equation reduces to an Abel-kernel Volterra equation whose solution is the square-root impact law at completion.
- If the waiting-time distribution has finite mean, the calendar-time clock grows linearly on average and the ordinary square-root impact law in calendar time is recovered.
- If the waiting-time distribution is heavy-tailed with a stable index between 0 and 1, the calendar-time impact scale instead grows anomalously, an effect driven purely by the clock projection rather than the underlying mechanism.
- The authors argue this clock-separation reconciles why persistent, long-memory order flow signs need not produce persistent, long-memory returns: the signal passes through diffusive transport, cancellation, and replenishment on the operational clock, and through subordination to the calendar clock, before it is observed as a return.

## Limitations

- The impact derivation depends on a locally linear, frozen-background latent-order-book approximation and treats the event clock as exogenous rather than state-dependent.
- The construction is entirely analytical; no order book or trade data is used to estimate parameters or test the derived relations against observations.
- Reader note: because no empirical fit is attempted here, the paper's central practical claim, that fitted calendar-time impact coefficients mix liquidity response with clock projection, is argued theoretically rather than demonstrated on real data in this paper.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/long-memory|long memory]]
- [[concepts/price-impact|price impact]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/square-root-law|square root law]]
- [[concepts/order-flow|order flow]]
- [[entities/tim-gebbie|Tim Gebbie]]

## Citation

Christopher Angstmann, Tim Gebbie (2026). Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market Observables.

DOI: 10.48550/arxiv.2609.13715

Text ingested: `markdown_output/angstmann-2026-event-time-order-flow-memory-operational.md`, converted from `raw/ofi-event-clock/angstmann-2026-event-time-order-flow-memory-operational.pdf`.

Coverage of this summary: Read the entire paper front to back, including the abstract, all seven numbered sections, the acknowledgments, and the reference list; the mathematical derivations are heavily obscured by OCR artifacts (repeated citation-bracket numbers and image placeholders replacing equations), so equations are described only qualitatively as stated in the surrounding prose.

Known problems with the input: year from file metadata: the paper's own text does not print a publication year; year 2026 is taken from the job file's year_hint and is consistent with the paper's own citations to companion works dated 2026 (references [10] and [25]); The markdown conversion replaces essentially every displayed equation with an '==> picture... intentionally omitted <==' placeholder, and inline citation brackets are frequently duplicated or garbled (e.g. '[1,1,, 2,, 3,, 4].]'), so equation forms could not be verified against the source and are described only in prose from the surrounding text.
<!-- AUTHORED REGION END -->