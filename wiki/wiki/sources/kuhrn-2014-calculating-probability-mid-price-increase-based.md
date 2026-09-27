---
authors:
- Sabrina Kuhrn
content_hash: sha256:882cbff6ebbe418ae486b4dcc88cb9803bc72c0b6a36ed9973bc22e9f4e5f590
created: 2026-09-27 01:47:00+00:00
page_id: sources/kuhrn-2014-calculating-probability-mid-price-increase-based
page_type: source
publication_venue: Technische Universität Wien
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/order-flow
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:1bb320866370d6fe9935eda4d0462ac56c59392c016835f418056765ae4672a8
source_path: markdown_output/kuhrn-2014-calculating-probability-mid-price-increase-based.md
source_type: paper
tags:
- limit-order-book
- birth-death-process
- poisson-process
- laplace-transform
- istanbul-stock-exchange
- mid-price-prediction
- order-book-dynamics
- market-microstructure
- clock-event
- asset-equity
- harvest-relevant
title: Calculating the probability of a mid-price increase based on a stochastic model
  for order book dynamics
updated: '2026-09-27T01:47:00Z'
uuid: 846549dd-e1dc-5102-9f45-f9edbfec183a
year: 2014
---

<!-- AUTHORED REGION START -->
# Calculating the probability of a mid-price increase based on a stochastic model for order book dynamics

## Summary

The thesis asks whether having full access to a limit order book, rather than just the top few quotes, lets a trader predict the direction of the next price move, and specifically whether a continuous-time stochastic model of the order book can compute the probability that the next change in the mid-price is an increase, conditional on the current state of the book.

It follows the birth-and-death Markov chain model in which the number of resting orders at each price level is treated as a queue: limit orders arrive and grow the queue (a birth), while market orders and matches shrink it (a death), both modeled as independent Poisson processes. Arrival rates are calibrated to two months of order and trade data for the 30 stocks making up the Istanbul Stock Exchange's ISE-30 index, by fitting a power-law function of price distance from the opposite best quote with nonlinear least squares. The probability of a mid-price increase, conditional on the number of shares at the best bid and ask and the current spread, is then derived from the first-passage time of these queues to zero, via a recursively constructed Laplace transform that is inverted numerically.

The model-implied probabilities track the realized frequencies of a mid-price increase computed directly from the order book reasonably well: in both the model and the data, a deeper bid queue makes an increase more likely and a deeper ask queue makes it less likely, for both one-tick and two-tick spreads, although the model and data values are not identical.

What differs from closely related studies is that the Istanbul exchange, during the sample period, did not permit order cancellations, so the model's death rate is a plain constant rather than depending on queue depth; this changes how quickly the truncated version of the model converges compared with earlier work that did include cancellations. The thesis frames itself mainly as a careful empirical check of the underlying model against real data, and suggests testing whether the computed probabilities could support a profitable trading strategy as future work.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The model runs in continuous time, with every limit order arrival, market order arrival and match treated as an independent Poisson event; there is no fixed sampling interval. The prediction target is the direction of the very next mid-price change, and the horizon is the first-passage time until that change: either the queue at the best ask or best bid depletes to zero, or, when the spread is wider than one tick, a new limit order arrives inside the spread. The probability is computed conditional on the current number of shares resting at the best bid, the current number at the best ask, and the current spread.

## Data

- **Asset class:** Equities
- **Instruments:** 30 stocks making up the ISE-30 index on the Istanbul Stock Exchange (e.g. AKBNK)
- **Venue:** Istanbul Stock Exchange (ISE)
- **Period:** 06-01-2008 until 07-31-2008 (two months)
- **Granularity:** Level-II order-book and trade data reconstructed to the best 10 quotes per side, plus 15-minute LOB snapshots (tau = 1, ..., 21) captured throughout each trading day

## Features and Measures

- **limit order arrival rate function.** The rate at which limit buy or sell orders arrive at a given distance from the opposite best quote, estimated by fitting a power-law function of that distance to the ISE-30 order data.
- **market order arrival rate.** The rate at which market orders arrive and remove volume from the best bid or ask, estimated per unit of trading time and expressed in units of the average limit-order size.
- **first-passage time of the order queue.** The time for the number of orders resting at a price level to fall to zero, computed from the birth-and-death process via a recursively built Laplace transform and used to determine when the best bid or ask will be depleted.
- **conditional probability of a mid-price increase.** The probability that the next change in the mid-price is an increase, given the current number of shares at the best bid, at the best ask, and the current spread, obtained by comparing the first-passage times of the bid and ask queues.

## Method

The thesis follows the birth-and-death Markov chain model of limit order book dynamics, in which the number of resting limit orders at each price level is a queue that grows through limit-order arrivals and shrinks through market orders and matches, with both kinds of event modeled as independent Poisson processes. Arrival rates are calibrated to ISE-30 order and trade data by fitting a power-law function of price distance from the opposite best quote via nonlinear least squares, separately for the buy and sell sides and then pooled, and the market-order arrival rate is estimated in the same units.

To obtain the probability of a mid-price increase, the thesis derives the Laplace transform of the first-passage time of the ask (or bid) queue to zero as a continued fraction, using a truncated-state-space technique to keep the calculation tractable, then inverts the transform numerically with a trapezoidal-rule and Euler-summation algorithm implemented in MATLAB. Combining the first-passage times at the ask and bid, together with the rate of new limit orders arriving inside the spread when the spread is wider than one tick, gives a closed-form expression for the probability that the next mid-price change is an increase, conditional on shares at the bid, shares at the ask, and the spread.

Performance is judged simply by comparing these model-implied probabilities against the realized frequency of a mid-price increase computed directly from the LOB snapshot data, for matching combinations of bid depth, ask depth and spread.

## Results

- The combined (buy- and sell-side) limit-order arrival rate is well fit by a power-law function of distance from the opposite best quote, with parameters k=0.781 and alpha=1.493; fit separately, the buy side gives k=0.785, alpha=1.656 and the sell side gives k=0.777, alpha=1.363, though the fit underestimates the tail of the distribution.
- The estimated market-order arrival rate is mu=1.507 (in units of the average limit-order size); the estimated limit-order arrival rate at distance 1 tick from the opposite quote is 0.780, falling to 0.018 at distance 10 ticks.
- A truncation state of kappa=10 already gives converged first-passage-time Laplace transforms in this model, with full convergence across states holding for kappa>=12, versus kappa>=15 in the closely related model that includes cancellations, a difference attributed to the ISE data having no cancellation orders.
- For a one-tick spread, the model gives a probability of a mid-price increase of 0.886 when there are 4 shares at the bid and 1 at the ask, falling to 0.111 when there is 1 share at the bid and 4 at the ask; the corresponding realized frequencies from the LOB data are 0.670 and 0.276.
- In both the model and the realized LOB frequencies, a deeper bid queue raises the probability of a mid-price increase and a deeper ask queue lowers it, for both one-tick and two-tick spreads.
- The birth-and-death model is reported to predict the LOB-based realized frequencies quite well, although the model and data values are not identical.

## Limitations

- Data cover only 30 stocks over two months (06-01-2008 to 07-31-2008) on a single exchange (the ISE), which at the time was non-anonymous and did not allow order cancellations.
- The order book is reconstructed from only the best 10 quotes per side, and orders are treated as unit-size, so partial fills or multi-lot orders are not modeled separately.
- Reader note: because cancellations were not permitted at the ISE during the sample period, the constant death-rate assumption used here cannot be assumed to carry over to modern exchanges where cancellations dominate order flow.
- Whether the computed probabilities could underlie a profitable trading strategy is left as a suggestion for future work and is not tested in the thesis.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow|order flow]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]

## Citation

Sabrina Kuhrn (2014). Calculating the probability of a mid-price increase based on a stochastic model for order book dynamics. Technische Universität Wien.

DOI: 10.34726/hss.2014.23849

Text ingested: `markdown_output/kuhrn-2014-calculating-probability-mid-price-increase-based.md`, converted from `raw/ofi-event-clock/kuhrn-2014-calculating-probability-mid-price-increase-based.pdf`.

Coverage of this summary: Read the full thesis: preface/abstract, introduction and research question, the entire data description and arrival-rate/interarrival-time estimation steps, the LOB model framework, parameter estimation and first-passage-time derivation, the numerical-inversion method and every results table in the numerical chapter, the conclusion and the data appendix; skipped only the routine textbook derivations of standard Laplace-transform, Poisson-process and Euler-summation identities, which are general mathematical background rather than paper-specific content.

Known problems with the input: The title heading on the source PDF was OCR-scrambled ('the of a Calculating probability mid-price increase...'); the title recorded here follows the corrected reading, matching the job's title_hint; Most equations in the converted markdown are rendered as '[picture... intentionally omitted]' placeholders, so exact formula text could not be transcribed; the method description here relies on the surrounding prose only; The thesis includes a duplicate German-language abstract/preface, which was not used as a separate source of facts.
<!-- AUTHORED REGION END -->