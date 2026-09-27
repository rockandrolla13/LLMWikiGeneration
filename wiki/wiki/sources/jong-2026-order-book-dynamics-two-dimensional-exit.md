---
authors:
- J.M. de Jong
content_hash: sha256:c942e5f6c27ae391d017811adb5d09875d6bcae068e7028148a25e7cec631a50
created: 2026-09-27 01:47:00+00:00
page_id: sources/jong-2026-order-book-dynamics-two-dimensional-exit
page_type: source
publication_venue: Erasmus University Rotterdam, Erasmus School of Economics - Master
  Thesis, Quantitative Finance Programme
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow-prediction
- concepts/order-flow
- concepts/market-microstructure
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:1e975bc2ddb29f6664ed58da12a081da02f7222fb29122483b215d472edf559f
source_path: markdown_output/jong-2026-order-book-dynamics-two-dimensional-exit.md
source_type: paper
tags:
- limit-order-book
- cryptocurrency
- order-flow
- drift-diffusion
- price-direction-prediction
- high-frequency-trading
- clock-event
- asset-crypto
- harvest-core
title: Order Book Dynamics - Two-Dimensional Exit Problems on a Cryptocurrency Exchange
updated: '2026-09-27T01:47:00Z'
uuid: 2dc65ab4-9cd9-57eb-97d5-898c79c7adc3
year: 2020
---

<!-- AUTHORED REGION START -->
# Order Book Dynamics - Two-Dimensional Exit Problems on a Cryptocurrency Exchange

## Summary

The thesis asks whether adding drift, correlation and better filtering to reduced-form Level-1 limit order book models can improve short-horizon prediction of the next mid-price direction on a cryptocurrency exchange, and whether that prediction can be turned into a trading rule that survives transaction costs. It builds on the Cont-Stoikov-Talreja and Avellaneda-Reed-Stoikov queue models, which treat only the best bid and ask queue volumes as a two-dimensional stochastic process and compute the probability that one queue depletes before the other.

Using about a month of Level-1 BitMEX Bitcoin-USD order book messages, the author defines cumulative bid and ask order-flow processes that extend the bid/ask queue volumes to an unbounded domain, exponentially filters them to remove a spurious upward drift caused by missing information about multi-level trades, and fits drift, standard deviation and correlation parameters either over the full sample or over rolling windows measured in numbers of messages. Four exit-probability models are compared: independent diffusions, correlated diffusions, and their drift-extended counterparts, the latter solved with a convection-diffusion result for a rotated sector domain. Predictions are scored against baseline predictors by RMSE at fixed times before an observed price change, then turned into an up/down classifier and, with a further no-prediction region, into a precision-favoring classifier and a simple long/short trading rule.

The diffusion-only models beat both the drift-extended models and the baselines; adding drift or correlation, or shortening the estimation window, did not help and often hurt accuracy, which the author attributes to the Level-1 book losing volume information during trades that sweep multiple price levels. As a classifier, the best model reached high precision close to a price change, and excluding low-volume, near-balanced situations pushed precision higher still at the cost of recall. The resulting trading rule was profitable before transaction costs, and remained profitable if the exit leg could be executed as a limit order to earn BitMEX's maker rebate, but turned loss-making once both legs paid the market-order taker fee.

What is new is the extension of the Avellaneda-Reed-Stoikov/Cont-De Larrard queue framework to imbalanced (drifting), possibly correlated order flow using the convection-diffusion solutions of Lopez and Sinusia, the cumulative-order-flow-with-exponential-filtering construction used to fit that framework on real exchange data, and a percentile-based classifier that explicitly trades recall for precision. The author also flags a previously unrecognized potential use of the resulting exit probabilities for pricing certain two-asset barrier options.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Cumulative bid and ask order-flow processes are updated at every Level-1 order book event (message); model parameters are estimated either as full-sample averages or via rolling windows measured in numbers of messages (1e3 to 5e6). Prediction performance and the trading rule are evaluated at fixed real-time horizons before an observed mid-price change (1 ms up to 5000 ms), so the prediction horizon is calendar time counted backward from the next price move.

## Data

- **Asset class:** Crypto
- **Instruments:** Bitcoin-U.S. Dollar (XBT-USD) market on BitMEX
- **Venue:** BitMEX
- **Period:** Full logged data set 2019-07-23 to 2019-10-13 (81 days); the modeling subset used runs 2019-09-09 to 2019-10-13
- **Granularity:** Message-level (order book update) data for the first three book levels, average inter-arrival time about 28 ms; the abstract reports 78M order book updates over one month of logging

## Features and Measures

- **cumulative order flow processes A_t, B_t.** Running sums of Level-1 bid and ask order arrivals, cancellations, and price-level transitions that extend the bounded bid/ask queue-volume process to an unbounded domain, so that queue-depletion jumps at a price change do not distort the estimated flow.
- **exponential filtering of order flow.** Subtracting an exponentially weighted moving average from the cumulative order flow to remove a positive drift bias and expose mean-reverting local dynamics, with the weighting parameter chosen from a grid between 1e-4 and 5e-2.
- **drift-diffusion and diffusion-only exit-probability models (Models 1-4).** Analytic solutions of a two-asset Black-Scholes-type PDE giving the probability that the ask queue depletes before the bid queue (price rises), under independent or correlated, drift-free or drifting bid/ask queue dynamics.
- **Up-Down-No Prediction classifier.** A binary price-direction classifier built on the probability models that abstains when the scaled queue radius is below a threshold or the polar angle between bid and ask volume falls in a middle band, trading recall for precision.

## Method

Order-flow parameters (drift, standard deviation and correlation of the filtered bid and ask cumulative flow processes) are estimated either as full-sample averages or via simple moving windows over 1e3 to 5e6 messages, after exponential filtering with weighting parameters between 1e-4 and 5e-2. The four probability models solve a stationary two-asset Black-Scholes-type PDE under boundary conditions that a queue depleting means the price has moved: Models 1 and 2 are drift-free (independent and correlated) diffusions extending Cont-De Larrard and Avellaneda-Reed-Stoikov, while Models 3 and 4 add drift and are solved via a convection-diffusion result for a rotated sector domain from Lopez and Sinusia.

Predictions are compared against 'Always Up', 'Always Down' and 'Previous Direction' baseline predictors using RMSE, with a normal-approximation confidence interval used because no convergence results exist for the theoretically more appropriate truncated chi-squared error distribution. Models are then thresholded at 50% to build up/down classifiers, and further restricted by excluding a low-radius, near-45-degree region to build the Up-Down-No-Prediction classifier, evaluated by precision, recall and F1 at a range of exclusion percentiles. The trading strategy enters a position 5000 ms after a price change if the classifier predicts a direction and the spread is minimal, and exits once the opposing best price moves, with results reported under no transaction costs, two market-order legs, and one market-order plus one limit-order leg.

## Results

- Diffusion-only Models 1 and 2 beat drift-extended Models 3 and 4, likely because Level-1 data cannot reliably pin down drift.
- All four order-flow models beat baseline predictors: best-model RMSE ranged 9.18-30.52% across horizons versus 53.80% for the best baseline (Previous Direction).
- Adding correlation (Models 2 and 4) worsened RMSE by up to 0.59% relative to the independent versions.
- Rolling-window parameter estimation did not improve on full-sample parameters; differences became statistically indistinguishable once the window reached about 1e6 messages.
- As a binary classifier at the 50% threshold, precision ranged 87.69-99.00% across horizons; excluding low-radius and near-diagonal points raised precision to 93.83-99.64% at the cost of recall falling to 72.10-90.54%.
- A trading rule based on the most selective classifier opened and closed 38376 trades over about one month, averaging 5.547 USD (0.062%) per round trip with no transaction costs.
- With both legs as market orders, BitMEX's 0.075% commission turned the strategy loss-making; using a limit order for the exit leg to earn the 0.025% maker rebate left an average profit of 1.061 USD (0.012%) per round trip.
- The bid-ask spread sat at the minimum tick (0.50 USD) 99.64% of the time, and Level-1 volume was several times larger than deeper levels, supporting the Level-1-only model choice.

## Limitations

- The Level-1-only order book description discards volume at deeper levels, which the author states causes a systematic positive bias in estimated order-flow drift during trades that deplete multiple price levels.
- The trading-strategy backtest covers a single asset (BitMEX XBT-USD) over about one month.
- RMSE confidence bounds use an untruncated normal approximation because no convergence results exist for the more appropriate truncated chi-squared distribution, which the author notes likely overstates the confidence interval.
- The trading rule ignores order-book depth beyond Level 1 and does not model the execution risk of limit orders used on the exit leg.
- Reader note: this is a single-author master's thesis and has not gone through peer review.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/order-flow|order flow]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

J.M. de Jong (2020). Order Book Dynamics - Two-Dimensional Exit Problems on a Cryptocurrency Exchange. Erasmus University Rotterdam, Erasmus School of Economics - Master Thesis, Quantitative Finance Programme.

DOI: 10.2139/ssrn.6364598

Text ingested: `markdown_output/jong-2026-order-book-dynamics-two-dimensional-exit.md`, converted from `raw/ofi-event-clock/jong-2026-order-book-dynamics-two-dimensional-exit.pdf`.

Coverage of this summary: Read the full thesis markdown: abstract, literature review, data chapter, methodology, all four model derivations, the entire results chapter (data selection through the trading strategy), the conclusion, all appendix results tables (B-1 to B-7), the trading-strategy algorithm, references and glossary.

Known problems with the input: Table 5-1 (model parameter overview) and the Appendix B performance tables render with merged or misaligned columns after PDF-to-markdown conversion; numbers used above were taken from the surrounding prose (which restates the same figures), not read directly off those garbled table cells.
<!-- AUTHORED REGION END -->