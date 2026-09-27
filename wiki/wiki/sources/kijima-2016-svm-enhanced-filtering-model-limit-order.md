---
authors:
- Hayato Kijima
- Hideyuki Takada
- Takayuki Tomiya
content_hash: sha256:d6556ace207937aa406519ed109e13ecd0485bdd9fc4301c0c7945693f990124
created: 2026-09-27 01:47:00+00:00
page_id: sources/kijima-2016-svm-enhanced-filtering-model-limit-order
page_type: source
publication_venue: Proceedings of the 47th ISCIE International Symposium on Stochastic
  Systems Theory and Its Applications, Honolulu
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-flow-prediction
- concepts/high-frequency-data
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:521c9c3a9225eda0086cc6ca98249bf98837786a3d4258d79194b3c4ddedf5b7
source_path: markdown_output/kijima-2016-svm-enhanced-filtering-model-limit-order.md
source_type: paper
tags:
- limit-order-book
- stochastic-filtering
- particle-filter
- support-vector-machine
- queueing-model
- latent-factors
- nikkei-225-futures
- clock-event
- asset-futures
- harvest-relevant
title: SVM-Enhanced Filtering Model for Limit Order Book Dynamics
updated: '2026-09-27T01:47:00Z'
uuid: 26ab4f8f-9d0a-5455-81ec-129ed7de97ef
year: 2015
---

<!-- AUTHORED REGION START -->
# SVM-Enhanced Filtering Model for Limit Order Book Dynamics

## Summary

The paper's question is how to model the time-varying arrival rates of limit orders, cancellations and executions in a way that reflects both the book's own recent history and its current shape, when the true drivers of order flow (how eager buyers and sellers are) cannot be observed directly. It extends an existing queueing model of the limit order book in which incoming and cancelled orders arrive as independent Poisson processes, removing that model's restriction that every order has unit size and instead letting arrival rates depend on two unobservable latent factors representing selling and buying pressure.

The approach treats the latent buy/sell pressure factors as a two-dimensional diffusion (an SDE) and estimates their posterior distribution from the observed order book history using nonlinear (Kushner-Stratonovich) filtering, approximated numerically with a branching particle filter. The paper's main addition is to let a Support Vector Machine, trained on a ten-dimensional snapshot of the current book shape, classify whether the mid price is more likely to move up or down next; that classification is then used to switch the target reverting level of the latent factors' drift, so the model becomes a regime-switching, SVM-informed Ornstein-Uhlenbeck-type process.

Using intraday tick data for Nikkei 225 futures from a single trading morning, the paper shows filtered percentile paths of the two latent factors alongside the mid-price path, computed once per second; visually, downward mid-price moves tend to coincide with the selling-pressure factor rising and the buying-pressure factor falling, though the authors note this pattern does not always hold. The paper reports the particle filter's per-step computation time but does not report a quantitative accuracy or backtest of the resulting up/down move probabilities, describing that validation as future work.

What is new relative to the underlying Cont et al. queueing model is allowing variable order sizes and, more centrally, coupling a machine-learned, book-shape-conditioned classifier into the drift of the latent state-estimation model, rather than treating the latent factors' dynamics as fixed.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The underlying model is driven by the arrival of individual limit order book events (new limit orders, cancellations, and executions inferred from depletion of the best quotes), each modeled as a marked point process with an intensity depending on the latent state. For numerical computation the continuous-time filter is discretized into fixed 20-millisecond steps, and in the reported example the filtered output is additionally sampled once every 1 second; there is no explicit forward return-prediction horizon, since the model's output is a filtered estimate of the current latent state and an instantaneous up/down move intensity rather than a return over a stated future window.

## Data

- **Asset class:** Futures
- **Instruments:** Nikkei 225 futures
- **Venue:** Osaka stock market, Japan (intraday tick data supplied by Rakuten Securities Co., Ltd.)
- **Period:** 1st June 2012, from market open at 9:00 am to 9:30 am
- **Granularity:** Intraday tick-level limit order book data, with the filter discretized at 20-millisecond time steps and its output plotted at 1-second intervals.

## Features and Measures

- **Latent selling/buying pressure factors.** A two-dimensional unobservable state process whose two components represent, respectively, the current overheating of sell orders and of buy orders; it drives the arrival and cancellation rates of limit orders and is estimated from the observed order book by nonlinear filtering.
- **10-dimensional limit order book snapshot.** A vector describing the shape of the order book at a given time step, used as the input features for the Support Vector Machine.
- **SVM mid-price direction label.** A plus/minus one label produced by a Support Vector Machine trained on the current book-shape vector, predicting whether the first subsequent mid-price move will be up or down, which is then used to switch the target reverting level of the latent factors' drift.

## Method

Order book dynamics are modeled as a high-dimensional queueing system in which six types of order events (limit sell, cancellation of limit sell, limit buy, cancellation of limit buy, market sell, market buy) arrive with conditionally independent, exponentially distributed inter-arrival times whose rates depend on distance from the best quote and on the two latent factors, via parametric functions chosen for tractability (e.g. exponential in the difference between the two factors). The latent factors themselves evolve as a bivariate stochastic differential equation. Because the latent factors are not directly observable, their posterior distribution given the observed order book history is characterized by the Kushner-Stratonovich filtering equation, which is approximated numerically with a branching particle filter following an approach adapted from prior work by one of the authors, discretized into 20-millisecond time steps.

The paper's extension trains a Support Vector Machine, with a Gaussian kernel and a margin-maximizing quadratic program, on the ten-dimensional book-shape vector at each step, labeled by the direction of the next mid-price move; the SVM's predicted label is then used to set which of two reverting levels (positive or negative) the latent factors' drift targets, making each latent factor a regime-switching mean-reverting process whose regime is chosen by the SVM.

The method is illustrated rather than formally backtested: filtered percentile paths of the two latent factors are computed and plotted against the intraday mid-price path, and the paper separately derives, but does not empirically validate, formulas for the instantaneous intensity of an upward or downward mid-price move implied by the filtered state.

## Results

- Filtered percentile paths of both latent factors were computed once per second for the Nikkei 225 futures order book from market open (9:00 am) to 9:30 am on 1st June 2012.
- Downward moves in the mid price tended to coincide with the selling-pressure factor rising and the buying-pressure factor falling, and vice versa for upward moves, but the paper states this correspondence is not always observed.
- The particle filter used 5000 initial particles and a 20-millisecond time step, and took about 10 milliseconds of computation per step on a Core i7 3.5GHz CPU.
- The authors report that computation time scales roughly linearly with the number of particles, which they suggest can guide the choice of particle count.
- The paper derives formulas for the instantaneous intensity of an upward or downward mid-price move from the filtered latent state but explicitly leaves empirical validation of these intensities to future research.

## Limitations

- The authors state that investigating the validity of the derived up/down move intensities is left for future research, i.e. no quantitative validation of the model's predictive intensities is given in this paper.
- Reader note: the numerical example covers a single 30-minute window on a single trading day and a single instrument, with no out-of-sample test or accuracy metric reported for the SVM or the filter.
- Reader note: the SVM's kernel parameter and margin trade-off parameter are not reported, and no measure of SVM classification accuracy is given.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Hayato Kijima, Hideyuki Takada, Takayuki Tomiya (2015). SVM-Enhanced Filtering Model for Limit Order Book Dynamics. Proceedings of the 47th ISCIE International Symposium on Stochastic Systems Theory and Its Applications, Honolulu.

DOI: 10.5687/sss.2016.181

Text ingested: `markdown_output/kijima-2016-svm-enhanced-filtering-model-limit-order.md`, converted from `raw/ofi-event-clock/kijima-2016-svm-enhanced-filtering-model-limit-order.pdf`.

Coverage of this summary: Read the entire converted markdown, from abstract through the numerical results, acknowledgements and references.
<!-- AUTHORED REGION END -->