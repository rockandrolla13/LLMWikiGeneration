---
authors:
- Kairat Mynbaev
content_hash: sha256:f3dd8e88214602d0c88c0e5a86bbe9aac6b6977e585522847516820300481b80
created: 2026-09-27 01:47:00+00:00
page_id: sources/mynbaev-2020-full-limit-order-book-price-jump
page_type: source
publication_venue: Munich Personal RePEc Archive (MPRA Paper No. 101684)
related:
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/stylized-facts
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:45968f3967bcf7872c505de2bf77c5eae6222531f575e76f54fcfbe0c2add7ee
source_path: markdown_output/mynbaev-2020-full-limit-order-book-price-jump.md
source_type: paper
tags:
- limit-order-book
- logistic-regression
- price-jump-prediction
- simulated-market
- high-frequency-trading
- order-book-depth
- curse-of-dimensionality
- stylized-facts
- clock-calendar
- asset-simulated
- harvest-relevant
title: Using full limit order book for price jump prediction
updated: '2026-09-27T01:47:00Z'
uuid: b0e9fa43-c501-586a-bb8e-73d734109891
year: 2020
---

<!-- AUTHORED REGION START -->
# Using full limit order book for price jump prediction

## Summary

The paper asks whether information from limit order book (LOB) price levels far from the best bid and ask, which the author calls the 'silent crowd', adds predictive value for the next price jump beyond the handful of near-touch levels usually kept to avoid the curse of dimensionality: using the full book as regressors otherwise causes multicollinearity, insignificant coefficients, inflated coefficient variance and high computation time.

Because a real LOB only reveals past investor decisions and live-market experiments are costly and risky, the author instead builds a fully simulated order-driven market in Matlab, implemented as 18 program files organized in dependency levels. The simulation posts limit, cancel and market orders one at a time so that each order's effect reflects the current book state, draws limit-order sizes from a distribution intended to reproduce observed empirical patterns (a spread of at least plus/minus 50% of the midprice, declining as a power law out to 100 ticks before being cut to zero), and lets orders of each type arrive independently at exponential rates.

From the simulated book, the author regresses the sign of the next midprice change on the ask and bid sizes at the first I price levels (I = 1 to 24), and separately on the same near-touch sizes plus a weighted 'silent crowd index' summarizing volume beyond level I, using logistic regression in both cases. The R-squared of the two specifications is compared as I varies.

The paper's contribution is this simulated-LOB testbed together with a concrete summary measure of the silent crowd and a quantification of its marginal predictive value: adding it clearly helps prediction when only a handful of near-touch levels are used, but its contribution becomes negligible once enough near-touch levels are already included.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The simulated order book itself evolves as a continuous event stream (independent exponential arrivals of limit, cancel and market orders), but for the logistic-regression prediction task the author samples ask/bid depths at equally spaced moments. The prediction target is the sign of the change in midprice from one sampled moment to the next. The paper notes that very short sampling intervals (on the order of several milliseconds) leave the simulated book 'too poor' for reliable regression, while longer intervals increase computational cost, but does not state the exact interval length used to produce the reported R-squared results.

## Data

- **Asset class:** Simulated data
- **Instruments:** A single simulated limit order book (no real traded instrument); tick size normalized to 1.
- **Venue:** not stated (fully simulated market, not tied to a specific exchange)
- **Period:** not stated (results come from simulation runs rather than calendar dates; the book is reported to stabilize after about 50 orders)
- **Granularity:** Order-by-order simulated arrivals (limit, cancel, market orders), with regressions built from ask/bid depths at the first 1 to 24 price levels from the midprice.

## Features and Measures

- **Silent crowd index.** A weighted sum of ask and bid volumes at price levels beyond the first I levels from the midprice, intended to summarize the information contained in distant, usually-discarded parts of the order book.
- **Ask/bid depth at level i (a_it, b_it).** The total order volume resting at the i-th price level from the best ask/bid, used as the standard near-touch predictors in the logistic regression.
- **Price jump indicator (j_t).** The sign of the change in midprice from one sampled moment to the next, the binary outcome predicted by the logistic regression.
- **Weighted cumulative-sum summary (cumulative sums from the lower end of the book).** A weighting scheme applied when summarizing the silent crowd so that price levels closer to the midprice receive larger weight while the tail of distant resting orders is still represented.

## Method

The author simulates a full limit order book in Matlab, implemented as an 18-program pipeline that generates and posts limit, cancel and market orders one at a time so that each order's market impact reflects the current state of the book. Incoming limit-order sizes are drawn from a distribution designed to reproduce empirically observed patterns, spanning roughly plus/minus 50% of the midprice and declining as a power law out to 100 ticks from the midprice; orders of each type arrive independently at exponential rates. From the simulated book, two logistic regressions are estimated to predict the sign of the next midprice move: one using only ask/bid depths at the first I price levels (I = 1, 2, ..., 24), and a second that adds a weighted silent-crowd index built from all levels beyond I. Model performance is judged by comparing the R-squared of these two regressions as I is varied.

## Results

- After about 50 simulated orders the book stabilizes and reproduces a hump-shaped (two-humped) distribution of resting order sizes similar to what is reported for real limit order books.
- The simulated density of incoming limit orders was set to taper off by about 200 ticks from the initial midprice, after which it is set to zero.
- The order-size distribution used in the simulation spans a spread of at least plus/minus 50% of the midprice and declines as a power law out to 100 ticks from the midprice before being cut to zero.
- Comparing R-squared across models built with the number of included near-touch price levels ranging from 1 to 24, adding the silent-crowd index clearly improves prediction when only a handful of near-touch levels (five or fewer) are used.
- The added contribution of the silent-crowd index falls off and becomes negligible once more than eight near-touch price levels are already included in the regression.
- The full simulation and analysis pipeline was implemented as 18 Matlab program files, organized into dependency levels (A, B, C, ...) according to which lower-level functions each program calls.

## Limitations

- All results are produced on a simulated order book rather than real exchange data, so the finding about the silent crowd's predictive value is not validated against actual market prices.
- The paper does not report the exact time interval used between the 'equally spaced moments' sampled for the logistic regression, only that very short intervals leave the book too poor and longer intervals raise computational cost.
- The simulated midprice stabilizes over time, which the author states is not a feature observed in real markets; a random-walk-like fix is suggested but not implemented.
- Reader note: only one simulated order-arrival and order-size configuration is studied in the extracted sections; no sensitivity analysis across alternative simulation parameters is reported.
- Reader note: the prediction target is only the sign of the next midprice change, not its magnitude, and no out-of-sample or hold-out evaluation is described.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Kairat Mynbaev (2020). Using full limit order book for price jump prediction. Munich Personal RePEc Archive (MPRA Paper No. 101684).

Text ingested: `markdown_output/mynbaev-2020-full-limit-order-book-price-jump.md`, converted from `raw/ofi-event-clock/mynbaev-2020-full-limit-order-book-price-jump.pdf`.

Coverage of this summary: Read the whole paper in full (abstract, introduction, order types and LOB structure, simulation description, simulation results, conclusions, and reference list).
<!-- AUTHORED REGION END -->