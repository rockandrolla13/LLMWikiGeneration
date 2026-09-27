---
authors:
- Luca Mucciante
- Alessio Sancetta
content_hash: sha256:1b0b9db0517be1065b26fca2851b056f519a8ef51e8fdfae62170a6abd3abc7e
created: 2026-09-27 01:47:00+00:00
page_id: sources/mucciante-2023-estimation-order-book-dependent-hawkes-process
page_type: source
related:
- concepts/trade-clock
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/order-flow
- concepts/high-frequency-trading
- concepts/order-imbalance
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/high-frequency-data
- entities/alessio-sancetta
revision_id: 1
schema_version: 2
source_hash: sha256:f9ed2d0dc4d2253e0e42596791792f2544d02c2678584f64fef20354502aedad
source_path: markdown_output/mucciante-2023-estimation-order-book-dependent-hawkes-process.md
source_type: paper
tags:
- hawkes-process
- order-book
- point-process
- high-frequency-trading
- high-dimensional-estimation
- self-excitation
- one-hot-encoding
- trade-arrivals
- clock-trade
- asset-equity
- harvest-relevant
title: Estimation of an Order Book Dependent Hawkes Process for Large Datasets
updated: '2026-09-27T01:47:00Z'
uuid: 085a18c2-2e25-5027-95a3-b00023dceca3
year: 2023
---

<!-- AUTHORED REGION START -->
# Estimation of an Order Book Dependent Hawkes Process for Large Datasets

## Summary

The paper builds a point-process model for the arrival of trading events in high-frequency markets in which the intensity is the product of a self-exciting Hawkes kernel and a nonlinear, high-dimensional function of order book covariates such as volume imbalance, spread, trade imbalance and trade durations. The aim is to let order book information modulate the endogenous, self-exciting dynamics of event arrivals, with covariates allowed to take continuous values and to have a possibly complex nonlinear impact, rather than being restricted to a small number of discrete states as in some prior order-book-dependent Hawkes models.

Because the covariate space can run into the hundreds or thousands of dimensions once nonlinear encodings are used, and event counts can reach hundreds of millions, the authors propose a two-step, coordinate-descent estimation algorithm that alternates a standard Hawkes-type quadratic-loss estimation of the kernel with a quadratic-programming estimation of the covariate coefficients under non-negativity and sum constraints. They state conditions under which the process is stationary and ergodic, show in simulation that the algorithm converges within a few iterations, and establish consistency of the high-dimensional coefficient estimator with only a logarithmic dependence on the number of covariates. A sample-splitting log-likelihood-ratio test statistic is developed to compare competing intensity specifications out of sample, extended here to cover unbounded intensities.

The method is applied to Level 3 Lobster order book data for four NYSE stocks (Amazon, Cisco, Disney, Coca-Cola) plus the S&P500 ETF as an auxiliary instrument, over a two-month sample. Both self-excitation and order book information turn out to matter: restricted models that drop either the Hawkes self-excitation term or the order book covariates are rejected out of sample, the impact of the order book covariates is found to be nonlinear rather than linear, and a two-exponential kernel improves out-of-sample fit relative to a single exponential kernel for some, though not all, stocks.

What is new relative to prior order-book-dependent Hawkes models is the combination of continuous, high-dimensional, nonlinearly-parametrized order book covariates with a self-exciting Hawkes baseline, together with an estimation procedure and consistency theory purpose-built for datasets of hundreds of millions of observations, without needing an explicit penalty term.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

The modeled counting process is trade arrivals (studied separately as 'Any Trade Arrivals' and 'Large Trade Arrivals', and separately for buy and sell sides). The intensity is a Hawkes self-exciting kernel multiplied by a function of order book covariates that are sampled at each order book or trade update ('reference time') and then lagged by one update so they remain predictable at the time of the next event. There is no fixed prediction horizon: the model forecasts the instantaneous arrival intensity of the next trade event, and competing specifications are compared out of sample via a likelihood-ratio test on held-out trading days.

## Data

- **Asset class:** Equities
- **Instruments:** Amazon (AMZN), Cisco (CSCO), Disney (DIS), Coca-Cola (KO); S&P500 ETF (SPY) used as an auxiliary instrument
- **Venue:** New York Stock Exchange (NYSE)
- **Period:** 01/March/2019-30/April/2019, 9:30am to 4:30pm each trading day, 42 trading days
- **Granularity:** Level 3 order book data from the Lobster dataset, querying the first ten levels of the book (first three levels used in estimation); covariates computed at every book/trade update and one-hot encoded into quantile-based bins.

## Features and Measures

- **Volume Imbalance (levels 1-3).** The normalized difference between bid size and ask size at a given order book level, taking values in [-1, 1] and used as a raw covariate in the intensity.
- **Spread.** The gap between the best ask and best bid price, expressed in basis points, used as a raw covariate.
- **Trade Imbalance.** An exponentially weighted moving average of signed traded volume divided by the EWMA of unsigned traded volume, updated at each trade.
- **Durations.** The time between trades in seconds, smoothed with EWMA filters using two different smoothing parameters, used as raw covariates capturing trading pace.
- **Seasonal component.** A time-of-day indicator standardized to [0, 1] over the trading session, included as a raw covariate without smoothing.
- **One-hot encoded covariate bins.** A quantile-based discretization of each raw covariate into bins (dummy variables), used to let the model capture a nonlinear, sign-constrained impact of the covariate on the intensity.

## Method

The intensity of the trade-arrival counting process is modeled as the product of a Hawkes kernel (a sum of exponential terms capturing self-excitation from past event arrivals) and a term that is linear in high-dimensional, non-negative covariates with non-negative, bounded-sum coefficients. In the empirical application, raw order book covariates (volume imbalance at three levels, spread, trade imbalance, two duration measures at different smoothing levels, a time-of-day seasonal term, and covariates from the auxiliary SPY instrument) are mapped into a higher-dimensional space via one-hot encoding based on empirical quantile bins, and lagged by one update to remain predictable. Estimation alternates two steps: fixing the covariate term and estimating the Hawkes kernel by minimizing a quadratic loss equivalent to standard Hawkes estimation, then fixing the kernel and estimating the covariate coefficients by quadratic programming under the non-negativity and sum constraints; this coordinate-descent procedure is shown in simulation to converge within two or three iterations. Buy and sell trade arrivals are estimated separately. Several restricted model specifications are compared (no self-excitation; single- versus two-exponential kernel; with and without order book information; one-hot-encoded versus purely linear covariates), and out-of-sample fit is judged using a sample-splitting log-likelihood-ratio test statistic, asymptotically standard normal, evaluated on the last trading days held out from estimation.

## Results

- For AMZN, the sample had more than 17 million book updates and in excess of 400 thousand trades over 42 trading days.
- The number of parameters to estimate reached up to 177 in principle, reduced to 168 once tied quantiles for the spread were merged.
- For the model with order book information and a single-exponential kernel (H1), the average share of nonzero estimated coefficients was roughly between 20% and 30% across the four stocks, for both Any Trade Arrivals and Large Trade Arrivals.
- Test statistics comparing pure-Hawkes baselines (no order book information) against the order-book-augmented model were large and negative, for example -20.28 (H01-H1) and -20.96 (H02-H1) for AMZN buy trades, rejecting the simpler models.
- The E-H1 test statistic, which drops self-excitation entirely, was strongly negative across stocks, for example -109.88 for AMZN buy trades, indicating self-excitation remains important once order book information is included.
- The H2-H1 test statistic (two-exponential versus one-exponential kernel) was large and positive for DIS and KO buy trades (63.92 and 27.65 respectively), showing a richer kernel fit better for those stocks, though not universally.
- Linear-covariate model variants were rejected against the one-hot-encoded nonlinear model, for example an H1L-H1 statistic of -27.75 for AMZN buy trades, indicating the order book's impact on the intensity is nonlinear.

## Limitations

- The paper models buy- and sell-side trade arrival intensities separately rather than jointly, for tractability with large samples, rather than estimating a full multivariate model.
- The empirical application covers only four NYSE stocks and one auxiliary ETF over a two-month sample (01/March/2019-30/April/2019).
- The authors note that one-hot encoding can create linearly dependent covariate columns, and that estimation relies on the non-negativity constraint to remain tractable in that case.
- Reader note: all instruments trade on a single venue (NYSE) during a single two-month window, so the paper does not itself establish how the results generalize to other venues or market regimes.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/alessio-sancetta|Alessio Sancetta]]

## Citation

Luca Mucciante, Alessio Sancetta (2023). Estimation of an Order Book Dependent Hawkes Process for Large Datasets.

DOI: 10.1093/jjfinec/nbad021

Text ingested: `markdown_output/mucciante-2023-estimation-order-book-dependent-hawkes-process.md`, converted from `raw/ofi-event-clock/mucciante-2023-estimation-order-book-dependent-hawkes-process.pdf`.

Coverage of this summary: Read the full markdown text: abstract, introduction and literature remarks (Sections 1-1.2), the model and regularity conditions (Section 2), the estimation algorithm and choice of B including the convergence simulation (Section 3), the asymptotic consistency results and the out-of-sample test statistic (Section 4), the entire empirical application including data, covariates, one-hot encoding, model specifications and results (Section 5), and the conclusion (Section 6); skipped only the reference list and appendix proofs/details beyond Section 6.
<!-- AUTHORED REGION END -->