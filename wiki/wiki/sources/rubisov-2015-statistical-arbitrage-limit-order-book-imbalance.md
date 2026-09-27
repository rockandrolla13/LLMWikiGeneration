---
authors:
- Anton D. Rubisov
content_hash: sha256:bd53b6c4bdd38b875ca9acb0141da8eba2a777b38c61a445f3c7a7bbdc4a040c
created: 2026-09-27 01:47:00+00:00
page_id: sources/rubisov-2015-statistical-arbitrage-limit-order-book-imbalance
page_type: source
publication_venue: University of Toronto (Master of Applied Science thesis)
related:
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/adverse-selection
- concepts/optimal-execution
- concepts/backtesting
- concepts/market-making
revision_id: 1
schema_version: 2
source_hash: sha256:c769c057e219288072ea7cc961423fda532f6b7c930357928faa277030657b54
source_path: markdown_output/rubisov-2015-statistical-arbitrage-limit-order-book-imbalance.md
source_type: paper
tags:
- limit-order-book
- order-imbalance
- stochastic-optimal-control
- market-making
- high-frequency-trading
- dynamic-programming
- nasdaq-itch
- backtesting
- clock-calendar
- asset-equity
- harvest-relevant
title: Statistical Arbitrage Using Limit Order Book Imbalance
updated: '2026-09-27T01:47:00Z'
uuid: 94759a6e-3c8a-5f94-b75f-57b8fb1b86ab
year: 2015
---

<!-- AUTHORED REGION START -->
# Statistical Arbitrage Using Limit Order Book Imbalance

## Summary

The thesis asks whether the imbalance between buy-side and sell-side liquidity in the limit order book can be exploited as a state variable to construct a profitable statistical arbitrage strategy. Working with NASDAQ Historical TotalView-ITCH order-level data reconstructed into the full limit order book, the author first explores whether imbalance predicts the sign of subsequent midprice moves in an exploratory analysis, modelling the joint evolution of a discretized imbalance measure and the price-change sign as a continuous-time Markov chain whose transition rates and market-order arrival intensities are estimated by maximum likelihood.

From this exploratory model, simple market-order and limit-order trading rules are tested and compared to isolate why posting resting limit orders in quiet, no-change-expected states outperformed reacting to an already-observed price move with market orders. The core contribution is then to formalize the problem as a stochastic optimal control problem that chooses when to fire a market order and at what depth to post limit orders in order to maximize expected terminal wealth, solved with the dynamic programming principle in both continuous time and discrete time.

The resulting optimal controls are calibrated on 2013 data (using same-day, week-offset, and full-year calibration windows) and backtested out-of-sample on 2014 data for two liquid NASDAQ names, generating a combined 877% return on investment before recurring infrastructure costs, falling to 359% once colocation and data-feed subscription fees of roughly $15,000 per month each are subtracted. Performance improves with stock liquidity and tighter bid-ask spreads, and the four control variants (continuous and discrete time, with and without an alternative calibration method) produce essentially uncorrelated but cointegrated return series.

What is new is treating imbalance and price-change sign jointly as a single Markov chain state, rather than imbalance as an exogenous predictor feeding a separately designed execution rule, and deriving optimal limit-order posting depths as functions of time, inventory and imbalance regime directly from the dynamic programming equation.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Imbalance is computed from the live limit order book but smoothed into a state variable by taking its time-weighted average over a trailing window ΔtI; the predicted quantity is the sign of the midprice change over a forward window ΔtS. The two windows are calibrated to be equal (for example 1000ms) per ticker and trading day. The control and backtesting chapters step through the trading day at these fixed calendar-time intervals rather than sampling per order-book event, trade, or volume bucket, even though the underlying order flow used to reconstruct the book is itself event-driven.

## Data

- **Asset class:** Equities
- **Instruments:** NASDAQ-listed common stocks: FARO, MMM, NTAP, ORCL and INTC in the exploratory and stochastic-control backtesting stages, plus AAPL added for the final out-of-sample test
- **Venue:** NASDAQ
- **Period:** 2013 (calibration and in-sample backtesting), 2014 (out-of-sample backtesting)
- **Granularity:** Millisecond-timestamped NASDAQ Historical TotalView-ITCH order messages (add/execute/cancel/delete events) used to reconstruct the full limit order book

## Features and Measures

- **Order imbalance I(t).** A ratio bounded in [-1,1] of exponentially depth-weighted bid versus ask limit order volumes at the three lowest non-zero depths, meant to capture short-term buy/sell pressure in the book.
- **Smoothed imbalance state ρ(t).** The raw imbalance I(t), time-weighted-averaged over a trailing window and then discretized into a fixed number of percentile bins symmetric around zero, used as one coordinate of the Markov chain state.
- **Price-change sign ΔS(t).** The sign (down, flat, up) of the midprice change over a forward-looking window, used as the second coordinate of the joint Markov chain and as the prediction target.
- **Two-dimensional imbalance/price-change CTMC.** A continuous-time Markov chain over the joint state (ρ(t), ΔS(t)), whose transition rates are estimated by maximum likelihood and used to derive conditional probabilities of the next price-change sign.

## Method

The exploratory chapter estimates a continuous-time Markov chain over the discretized, time-weighted-average imbalance measure and the sign of forward midprice change, using maximum-likelihood formulas for the generator matrix and for regime-conditional buy/sell market order arrival rates (a Markov-modulated Poisson process). Time-homogeneity of the chain is cross-validated with a chi-squared test comparing transition probabilities estimated on the full year against those from repeated subsamples of the data; the test rejects homogeneity at the conventional cutoff. The stochastic-control chapters recast the same state process as the driver of an agent's cash, inventory and wealth dynamics under market-order execution and limit-order fills, the latter modelled with an exponential fill-probability function governed by a constant κ, and solve for the value function and optimal controls via the dynamic programming equation in both continuous and discrete time. Global backtesting parameters fixed the imbalance discretization at 5 bins and κ at 100. Strategies are calibrated separately per ticker under three schemes (same trading day, a one-week-ahead offset, and the full prior year) and judged by average end-of-day return, risk-adjusted return (mean divided by standard deviation of daily returns), share of winning days, and trade counts, benchmarked against three simpler 'naive' imbalance-based rules from the exploratory chapter.

## Results

- The Naive market-order rule lost money on average, while the Naive+ rule (posting resting limit orders when no price change was expected) made money on average.
- Same-day calibration of the discrete-time optimal control on INTC attained a risk-adjusted return of 2.5.
- A chi-squared time-homogeneity test on the fitted Markov chain rejected the homogeneity hypothesis at the standard 0.05 cutoff for every ticker and bin count tested.
- The four stochastic-control variants had pairwise return correlations near zero yet were shown to be cointegrated, with Engle-Granger cointegration test p-values of 0.001.
- Illiquid FARO produced negative average returns under most calibration schemes, while the more liquid ORCL and INTC produced positive end-of-day P&L on more than 90% of trading days under same-day calibration.
- Out-of-sample backtesting on 2014 data for INTC and AAPL produced an estimated combined return on investment of 877% before fees.
- Deducting approximate colocation and ITCH-feed subscription costs of $15,000 per month each reduced the estimated return on investment to 359%.

## Limitations

- The dynamic programming formulation ignores the exchange fee for executing market orders, so realized returns would likely be lower than modelled.
- Optimal posting depths are solved as continuous real numbers, but real exchanges require limit orders in discrete tick increments, so the derived controls cannot be posted exactly as computed.
- The authors' own back-of-envelope trade-size calculation implies contributing more than 1% of AAPL's daily volume, which would create price impact that the backtest does not model.
- The paper's own cross-validation test rejects the time-homogeneity assumption used throughout the calibration and backtesting.
- Reader note: limit order fills in the backtest are generated from an assumed exponential fill-probability function rather than from tracking the strategy's actual queue position in the reconstructed order book, and no order-transmission latency is modelled.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/backtesting|backtesting]]
- [[concepts/market-making|market making]]

## Citation

Anton D. Rubisov (2015). Statistical Arbitrage Using Limit Order Book Imbalance. University of Toronto (Master of Applied Science thesis).

Text ingested: `markdown_output/rubisov-2015-statistical-arbitrage-limit-order-book-imbalance.md`, converted from `raw/ofi-event-clock/rubisov-2015-statistical-arbitrage-limit-order-book-imbalance.pdf`.

Coverage of this summary: Read the abstract, acknowledgements, introduction (Chapter 1), the entire exploratory data analysis chapter (Chapter 2) on modelling imbalance and the naive strategies, the opening system-description pages of the stochastic-control chapters (start of Chapter 3), the entire results chapter (Chapter 5: calibration, in-sample and out-of-sample backtesting), the conclusion (Chapter 6) and the bibliography; the detailed dynamic-programming derivations inside Chapters 3 and 4 were not read line by line.

Known problems with the input: Markdown conversion garbles several sentences (scrambled word order) and replaces all equations and figures with '==> picture... omitted <==' placeholders; numbers used here were checked only against clearly legible table cells and prose; The detailed stochastic-control derivations in Chapters 3 and 4 were skimmed rather than read in full because they are equation-heavy and the placeholders make the formulas unreadable; the method summary relies on the chapter introductions and on the results chapter's cross-references back to those chapters.
<!-- AUTHORED REGION END -->