---
authors:
- Emmanouil Sfendourakis
- Ioane Muni Toke
content_hash: sha256:14761307335a3ff7bc2bcff936fe5eb1f6e553391205974e611ecc9a6722a769
created: 2026-09-27 01:47:00+00:00
page_id: sources/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent
page_type: source
related:
- concepts/event-clock
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-imbalance
- concepts/order-flow
- concepts/bid-ask-spread
revision_id: 1
schema_version: 2
source_hash: sha256:1b0e150ed1b7d58e626023d6543fafeae5701ccbbac6852f1f17a959dfc52e44
source_path: markdown_output/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent.md
source_type: paper
tags:
- hawkes-processes
- limit-order-book
- market-microstructure
- state-dependent-intensity
- order-imbalance
- point-processes
- clock-event
- asset-equity
- harvest-relevant
title: LOB Hawkes modeling using processes with a state-dependent factor
updated: '2026-09-27T01:47:00Z'
uuid: 85b56319-fab1-5857-87d4-06b6cb06e0cd
year: 2021
---

<!-- AUTHORED REGION START -->
# LOB Hawkes modeling using processes with a state-dependent factor

## Summary

The paper asks how a point-process model of limit order book order flow can capture both the self- and cross-exciting clustering that Hawkes processes are known for, and the empirical fact that order arrival rates depend on the current state of the book (such as the bid-ask spread or the order imbalance), while staying computationally tractable and parsimonious in the number of parameters.

The authors define the msdHawkes process: the intensity of a multi-dimensional order flow (for example bid versus ask market orders, or upward versus downward price moves) equals a standard multi-exponential Hawkes intensity multiplied by an exponential function of a vector of observable, piecewise-constant state variables. They derive recursive, linear-time formulas for the log-likelihood and its gradient that enable fast direct maximum-likelihood estimation, and they also derive an expectation-maximization algorithm based on the Hawkes branching-process representation; both estimators are checked on simulated data, and msdHawkes is compared against two existing state-dependent Hawkes formulations from the literature, one built on a state-varying kernel and one built on queue sizes.

On tick-by-tick data for 36 Euronext Paris stocks in 2015, models that include both imbalance and spread as state variables, together with three exponential terms in the Hawkes kernel, are almost always selected by the Akaike Information Criterion and pass goodness-of-fit tests on the model's residuals more often than simpler alternatives. State-dependence clearly improves fit relative to a standard (state-independent) Hawkes model, and the state-dependent endogeneity coefficient can temporarily exceed the stability threshold of a standard Hawkes process when the spread is at its narrowest.

What is new is the msdHawkes formulation itself, which multiplies a Hawkes kernel by an exponential state factor so that adding a state covariate only adds a handful of parameters, the recursive likelihood and EM estimation machinery built for it, and its use both to fit order flow and to forecast the sign of the next incoming order out of sample.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The model treats order book order flow as a point process observed at the exact arrival times of orders (market orders, or price-moving 'aggressive' events), not on a fixed calendar grid; the conditional intensity at each instant depends on the history of past events (Hawkes excitation) and on the piecewise-constant current state of the book. The prediction task tested empirically is the type of the very next event (e.g. bid or ask, up or down), predicted just before it occurs from the model with the highest current intensity, using parameters fitted on the prior trading day.

## Data

- **Asset class:** Equities
- **Instruments:** 36 stocks traded on Euronext Paris (individual tickers are listed only in a garbled figure caption in the converted text and are not reliably extractable)
- **Venue:** Thomson-Reuters Tick History (TRTH) database, Paris stock exchange (Euronext Paris)
- **Period:** Year 2015
- **Granularity:** Tick-by-tick order book data restricted to the 10:00-14:00 trading window each day, with timestamps precise to the millisecond

## Features and Measures

- **msdHawkes process.** A multivariate Hawkes process whose intensity is multiplied by an exponential function of an observable, piecewise-constant state vector, such as order imbalance or the bid-ask spread, so the excitation dynamics of a standard Hawkes process are scaled up or down by the current book state.
- **Order imbalance (I).** The normalized difference between best bid and best ask queue sizes, taking values in [-1, 1], used as a state covariate in the model.
- **Spread state specifications (S1, S2, S3).** Three alternative ways of turning the bid-ask spread into a bounded state covariate: a median-split indicator, a one-tick-versus-wider indicator, and a covariate built from the empirical probability distribution of the spread in ticks.
- **State-dependent endogeneity coefficient.** The spectral radius of the Hawkes excitation matrix evaluated at a fixed state, measuring the fraction of events that are self- or cross-triggered rather than exogenous, allowed to vary with the current imbalance and spread.

## Method

The msdHawkes intensity is a standard multivariate Hawkes intensity, with a baseline rate and a sum-of-exponentials excitation kernel, multiplied elementwise by an exponential function of a piecewise-constant vector of observed LOB state variables (imbalance and one of three spread transformations). The model is estimated either by direct gradient-based maximization of a recursively computable log-likelihood or by an expectation-maximization algorithm built on the Hawkes branching-process representation; model choice, including the number of exponential kernel terms and which state variables to include, is made with the Akaike Information Criterion and validated with a Kolmogorov-Smirnov test on the model's fitted residuals.

Applications are to two two-dimensional order flows built from Euronext Paris tick data on 36 stocks in 2015, restricted to a 10:00-14:00 window each day: a 'Market' case (bid versus ask market order counts) and an 'Aggressive' case (all order-book events that move the mid-price up versus down). Performance is judged by AIC selection frequency, the share of stock-trading days passing the Kolmogorov-Smirnov residual test, the estimated state-dependent endogeneity coefficient, and an out-of-sample exercise predicting the sign of the next incoming order using only the previous trading day's fitted parameters, benchmarked against a rule that always repeats the previous order's sign and a rule based on the sign of the imbalance.

## Results

- In simulations with two exponential kernel terms and 120 samples, direct gradient-based maximum-likelihood (L-BFGS-B, TNC) and the EM algorithm recover the true parameters with comparable accuracy.
- Direct maximum-likelihood estimation is far faster than EM: L-BFGS-B and TNC take under 1 second per sample, while EM needs 4500 to 11000 seconds on the same hardware.
- AIC almost always selects a state-dependent msdHawkes model over the standard Hawkes and other state-dependent benchmarks, favoring the model using both imbalance and spread on more than 99% of stock-trading days in the 'Market' case and more than 97% in the 'Aggressive' case.
- AIC favors 2 or 3 exponential terms in the Hawkes kernel on 91% of stock-trading days for 'Market' orders, and 3 or 4 terms on 92% of stock-trading days for 'Aggressive' orders.
- State-dependence clearly improves goodness-of-fit relative to standard Hawkes models, as measured by the share of days passing a Kolmogorov-Smirnov test on the model residuals at the 5% level.
- The state-dependent endogeneity coefficient can rise above the critical value of 1 when the spread equals one tick, indicating the process temporarily visits a regime that would be unstable for a standard Hawkes process.
- In the out-of-sample sign-prediction exercise for 'Market' orders, a naive rule that always repeats the previous order's sign is correct 81% of the time on average, and the msdHawkes model using imbalance beats it on 97.5% of stock-trading days, raising accuracy by more than 5% on average.
- In the 'Aggressive' case, the imbalance-sign rule alone is the best predictor at about 79% average accuracy, and msdHawkes models with imbalance do not improve on it, losing about 2% in accuracy on average.

## Limitations

- The authors state that theoretical results on existence, uniqueness and stability of the msdHawkes process are not established and are left to future mathematical work.
- The authors note that coupling between the state process and the counting process is not explicitly modeled, unlike in the ksdHawkes formulation of Morariu-Patrichi and Pakkanen.
- The authors note that duplicate-timestamp events (multiple orders within the same millisecond) are collapsed by keeping only the last one, which can bias kernel parameter estimation.
- Reader note: the empirical application uses only two state covariates (spread and imbalance) and does not test whether other order book variables would improve the state-dependent model.
- Reader note: the state-dependent endogeneity coefficient can exceed the stability threshold of 1 in some states, but the paper does not resolve whether or when the resulting process remains stable.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/bid-ask-spread|bid ask spread]]

## Citation

Emmanouil Sfendourakis, Ioane Muni Toke (2021). LOB Hawkes modeling using processes with a state-dependent factor.

DOI: 10.1142/s2382626620500148

Text ingested: `markdown_output/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent.md`, converted from `raw/ofi-event-clock/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent.pdf`.

Coverage of this summary: Read the abstract, introduction, Section 2 (msdHawkes model, maximum-likelihood and EM estimation, numerical illustrations, and comparison to other state-dependent Hawkes models), Section 3 (LOB applications: data, model selection, estimated parameters, endogeneity, and out-of-sample prediction), and the conclusion; did not work through the technical derivations in Appendices A and B (recursive log-likelihood and EM formulas) or read Appendices C-E.

Known problems with the input: The job file's slug and year_hint say 2020, but the paper's own title-page date reads 'December 6, 2021'; year is set to 2021 from the printed date; No venue or publication outlet (journal, conference, or working-paper series) is printed anywhere in the converted text; venue is left empty; The stock ticker list in Figure 6's caption is run together without separators in the converted text, so individual tickers could not be reliably read off; the instruments field describes the sample without listing tickers.
<!-- AUTHORED REGION END -->