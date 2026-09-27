---
authors:
- Chris Angstmann
- Tim Gebbie
content_hash: sha256:38d749e4e4ec61bc1d35cc2c2a4a174269d71444919c23025c7f5635b7ee6747
created: 2026-09-27 01:47:00+00:00
page_id: sources/angstmann-2026-revisiting-trade-sign-long-memory-square
page_type: source
related:
- concepts/stochastic-time-change
- concepts/long-memory
- concepts/square-root-law
- concepts/price-impact
- concepts/metaorder
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-flow
- concepts/autocorrelation-time-series
- entities/tim-gebbie
revision_id: 1
schema_version: 2
source_hash: sha256:49988e4ec262b5d6bff218528069308d158d9bb5ce0f6be7726c20d14b630697
source_path: markdown_output/angstmann-2026-revisiting-trade-sign-long-memory-square.md
source_type: paper
tags:
- trade-sign-long-memory
- square-root-law
- reaction-diffusion
- event-time
- subordination
- meta-orders
- order-splitting
- clock-time-change
- asset-none
- harvest-relevant
title: Revisiting Trade-sign Long-memory and Square-root Law price impact
updated: '2026-09-27T01:47:00Z'
uuid: a5f12d10-84a1-552b-aee3-ac3aaf42c739
year: 2026
---

<!-- AUTHORED REGION START -->
# Revisiting Trade-sign Long-memory and Square-root Law price impact

## Summary

This is a purely theoretical, derivation-based paper with no dataset. It starts from a discrete, non-uniform-event-time reaction-diffusion model of bid and ask liquidity, with cancellation, replenishment from lit and latent sources, and signed meta-order forcing at the price front. The paper's structural motivation is that two well-known market-microstructure results, the concave square-root law (SQRL) of meta-order price impact and the Lillo-Mike-Farmer (LMF) long-memory of trade signs, are usually derived in separate literatures (reaction-diffusion/latent-order-book theory for impact; order-splitting/renewal theory for sign memory), even though both are driven by the same underlying signed order flow.

The paper reduces the discrete bid/ask system to an exact imbalance equation, in which the nonlinear local-matching term cancels exactly, and takes a continuum limit to obtain a linear inhomogeneous reaction-diffusion PDE with a moving front identified as the mid-price. Using a local-linear approximation of the order book near the front (LLOB) and a Green-function representation, it derives the standard nonlinear Volterra equation for the front trajectory, and shows that under weak cancellation, small displacement and constant participation-rate execution this yields the familiar square-root law: transient impact proportional to the square root of elapsed time, and completion impact proportional to the square root of meta-order size.

Separately, the paper gives a renewal-theoretic derivation showing that i.i.d., Pareto-tailed meta-order lengths generate an exact trade-sign autocorrelation formula whose large-lag behaviour recovers the LMF exponent relation. It also compares three distinct notions of trade sign (the meta-order's own sign, a source-based sign from the local forcing near the front, and a flux-based sign from the change in imbalance flux through the front), showing they coincide only under a one-step force-domination and monotone-flux-response assumption.

The paper's central reinterpretation is a three-clock distinction: event time (the count of child-order arrivals, the natural domain of the LMF sign process), operational time (the continuum clock of the reaction-diffusion front and Volterra equation), and physical/calendar time (in which participation rates, execution horizons and realized impact are actually measured). Calendar time is obtained from event time by subordination through the cumulative waiting-time process between order-book events (a discrete-time random walk/CTRW construction); the paper argues that heavy-tailed waiting times can make this event-to-calendar-time mapping anomalous even though the event-time LMF law is unaffected, so that the square-root law's calendar-time form is a physical-time statement, not an event-time one.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

The paper explicitly separates three clocks: event time m, an integer index over child-order/order-book events, which is the natural domain of the trade-sign process and the LMF renewal law; operational time, the continuum limit of the discrete event-time dynamics in which the reaction-diffusion front and its Volterra impact equation are written; and physical/calendar time t, the clock in which participation rates, execution horizons and realized meta-order impact are actually measured. Calendar time is constructed from event time by subordination: cumulative waiting times between events define an inverse counting process N_t, and the physical-time front process is the event-time process evaluated at N_t, so that heavy-tailed waiting times can make the calendar-time impact trajectory anomalous even when the event-time sign-memory law is unchanged.

## Data

- **Asset class:** No data (theory or survey)
- **Instruments:** not stated
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated

## Features and Measures

- **Imbalance field (phi).** The signed difference between bid-side and ask-side order density on a discretized log-price grid, whose zero-crossing defines the moving price front (mid-price).
- **Local Linear Order Book (LLOB) approximation.** A first-order Taylor approximation of the stationary imbalance profile near the price front, characterized by a single liquidity slope parameter, used to linearize the free-boundary front dynamics.
- **Volterra impact equation.** A non-linear integral equation for the front (mid-price) trajectory derived via a Green-function representation, in which each past child-order increment contributes to the current price through a diffusion kernel.
- **Primary, source-based and flux-based trade-sign conventions.** Three distinct ways to assign a sign to a child-order event: the sign of the meta-order itself, the sign of the net local forcing near the front, and the sign of the event-induced change in imbalance flux through the front; they agree only under a local force-domination and monotone-flux assumption.
- **Event-time / operational-time / calendar-time subordination.** A construction in which the event-time order-flow and front process is mapped to a physical calendar-time process via an inverse counting process built from the cumulative waiting times between order-book events.

## Method

The paper is a mathematical derivation with no empirical estimation. It defines a discrete, non-uniform event-time reaction-diffusion model for bid and ask order density with diffusion, cancellation, lit/latent replenishment sources and signed meta-order forcing at the front, reduces it to an exact imbalance equation in which the nonlinear local-matching term cancels, and passes to a continuum limit to obtain a linear inhomogeneous reaction-diffusion PDE. Near the moving front it applies a local-linear order-book approximation and a Green-function/Duhamel representation to derive the standard nonlinear Volterra equation for the front trajectory, then specializes to constant-participation-rate execution in the weak-cancellation, small-displacement regime to recover the square-root transient and completion impact laws. Independently, it derives a renewal-theoretic formula for the event-time trade-sign autocorrelation from an i.i.d., Pareto-tailed meta-order-length distribution, recovering the LMF exponent relation, and analyses when the meta-order sign, the source-based sign and the flux-based sign coincide. Finally it introduces a discrete-time random walk (DTRW)/subordination argument to relate the event-time sign process to the calendar-time impact trajectory via the cumulative inter-event waiting-time process.

## Results

- The exact discrete bid/ask imbalance equation is linear once the nonlinear local-matching term cancels, and its continuum limit is a linear inhomogeneous reaction-diffusion PDE for the moving price front.
- Under the local-linear order-book approximation and the weak-cancellation, small-displacement regime, transient impact at fixed participation rate scales with the square root of elapsed time, and completion impact scales with the square root of meta-order size.
- Heavy-tailed (Pareto) meta-order lengths generate, via a renewal argument, a trade-sign autocorrelation that decays as a power law, recovering the Lillo-Mike-Farmer exponent relation linking the sign-memory exponent to the meta-order-length tail exponent.
- The primary meta-order sign, the source-based (forcing) sign and the flux-based (front-flux) sign coincide only under a one-step force-domination and monotone-flux-response assumption; otherwise the three conventions can have different autocorrelations and different long-memory exponents.
- Persistent event-time sign memory need not produce persistent calendar-time return autocorrelation, because diffusion, replenishment and front-slope adaptation filter the linear propagator response.
- The Lillo-Mike-Farmer long-memory law is identified as fundamentally an event-time statement, while the square-root impact law is identified as fundamentally an operational/physical-time statement, so that heavy-tailed inter-event waiting times can make the event-count-to-calendar-time mapping anomalous without changing the event-time sign-memory law.

## Limitations

- This is a purely theoretical derivation; no empirical data, calibration, or numerical simulation is presented to test the model against real order-book or trade data.
- The square-root law derivation relies on a local-linear (LLOB) order-book approximation and on weak-cancellation, small-displacement regimes; the paper itself notes that the pure square-root scaling breaks down once cancellation is not negligible over long horizons.
- The renewal derivation of the LMF law assumes independent, symmetric signs across non-overlapping meta-orders with i.i.d. lengths, whereas the paper notes that in reality meta-orders mix and overlap.
- Reader note: the paper positions itself as a reinterpretation and unification of existing derivations (from the LLOB/Volterra and LMF/renewal literatures) within an explicit three-clock framework, rather than as a new empirically tested result.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/long-memory|long memory]]
- [[concepts/square-root-law|square root law]]
- [[concepts/price-impact|price impact]]
- [[concepts/metaorder|metaorder]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow|order flow]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[entities/tim-gebbie|Tim Gebbie]]

## Citation

Chris Angstmann, Tim Gebbie (2026). Revisiting Trade-sign Long-memory and Square-root Law price impact.

DOI: 10.48550/arxiv.2606.16269

Text ingested: `markdown_output/angstmann-2026-revisiting-trade-sign-long-memory-square.md`, converted from `raw/ofi-event-clock/angstmann-2026-revisiting-trade-sign-long-memory-square.pdf`.

Coverage of this summary: Read the full paper end to end: introduction and motivation, the discrete non-uniform reaction-diffusion model and its continuum limit, the local-linear order-book and square-root impact derivation, the trade-sign process section (source-based, flux-based and interface representations, LMF renewal derivation, weak return autocorrelations, subordination), the discussion and conclusion. There is no separate data or empirical section because the paper is purely theoretical.

Known problems with the input: This paper contains no dataset or empirical section (it is a purely theoretical/derivation paper); the 'data' fields are marked not stated/none accordingly; No explicit publication year is printed on the paper's own title/abstract material; the year field uses the job file's year_hint (2026), which is consistent with the paper's own self-citation to a companion 2026-dated paper in the reference list.
<!-- AUTHORED REGION END -->