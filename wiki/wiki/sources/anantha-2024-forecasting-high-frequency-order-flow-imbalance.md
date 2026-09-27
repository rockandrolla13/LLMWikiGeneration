---
authors:
- Aditya Nittur Anantha
- Shashi Jain
content_hash: sha256:860af7da5c594bf33559145421203614931c07d0f86835882e5c68636930d3a4
created: 2026-09-27 01:47:00+00:00
page_id: sources/anantha-2024-forecasting-high-frequency-order-flow-imbalance
page_type: source
related:
- concepts/sampling-clocks
- concepts/hawkes-processes
- concepts/order-flow-imbalance
- concepts/order-flow-prediction
- concepts/trade-classification
- concepts/informed-trading
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/order-flow
- entities/aditya-nittur-anantha
- entities/shashi-jain
revision_id: 1
schema_version: 2
source_hash: sha256:4732d7532714c8915855a4c3094fe9029802069cc0f59bfb48dd377a945d4e95
source_path: markdown_output/anantha-2024-forecasting-high-frequency-order-flow-imbalance.md
source_type: paper
tags:
- hawkes-processes
- order-flow-imbalance
- market-microstructure
- tick-data
- model-comparison
- nse-futures
- clock-compares
- asset-futures
- harvest-relevant
title: Forecasting high frequency order flow imbalance using Hawkes processes
updated: '2026-09-27T01:47:00Z'
uuid: e6111799-f4ed-5854-bd9d-56d58442c4ae
year: 2024
---

<!-- AUTHORED REGION START -->
# Forecasting high frequency order flow imbalance using Hawkes processes

## Summary

The paper asks how to forecast the near-term distribution of Order Flow Imbalance (OFI) at high frequency without relying on a trade-classification algorithm, and how to compare an arbitrarily large number of candidate forecasting models against each other. OFI here is computed directly from exchange-provided order identifiers that mark each trade as buy- or sell-initiated, rather than estimated with the Lee-Ready or bulk-volume rules used in most prior work.

The authors model buy and sell market-order arrivals as a bivariate Hawkes process, which captures both self-excitation (buy trades triggering further buy trades) and cross-excitation (buy trades triggering sell trades and vice versa). Several parametric Hawkes kernels (exponential, sum-of-exponential, power-law), two non-parametric kernels (a conditional-law estimator and an EM-based estimator), a plain Poisson process, and a Vector Auto Regression (VAR) model fitted on minute-aggregated buy/sell counts are all fitted on a rolling window and used to simulate a one-minute-ahead forecast distribution of OFI. Model quality is judged by the negative log-likelihood of the realized OFI value under each model's simulated distribution, and models are ranked using Hansen's test for superior predictive ability, which extends the Diebold-Mariano idea to more than two competing forecasts.

On a single day of NIFTY futures tick data from the National Stock Exchange of India, the sum-of-exponential Hawkes kernel and the non-parametric conditional-law kernel are statistically indistinguishable as the best performers, both ahead of the plain exponential kernel, the power-law kernel, a Poisson benchmark, and the VAR model. The authors favor the sum-of-exponential kernel in practice because its Markovian structure makes fitting and simulation much cheaper.

What is new here relative to prior OFI studies is the combination of (a) computing OFI from realized trade classification instead of an estimated one, (b) forecasting a full near-term distribution of OFI rather than a point forecast, and (c) a general procedure for ranking many competing forecasting models rather than comparing just two.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

OFI is computed from the realized buy/sell classification of each individual trade tick (no estimation algorithm is used), and Hawkes kernels are fitted directly on the continuous arrival times of buy and sell market orders within a rolling one-hour window. In parallel, a VAR model is fitted on the same data aggregated into fixed one-minute buy/sell trade counts, discarding inter-arrival time information. Both approaches forecast one minute ahead, and the paper's central empirical question is whether keeping the exact inter-trade arrival times (as the Hawkes models do) improves the forecast relative to the minute-aggregated VAR approach.

## Data

- **Asset class:** Futures
- **Instruments:** NIFTY futures contract expiring 27 September 2018, traded on the National Stock Exchange of India
- **Venue:** National Stock Exchange (NSE), India
- **Period:** single trading day, 19 September 2018
- **Granularity:** tick-by-tick trade, new/modify/cancel order messages; OFI aggregated into one-minute values for the day (315 usable one-minute observations after the initial one-hour fitting window)

## Features and Measures

- **Order Flow Imbalance (OFI).** The difference between the number of sell-classified and buy-classified market order trades over a window of length h, computed here from the exchange's own order-identifier fields rather than an estimated classification rule.
- **Bivariate Hawkes process on buy/sell trade arrivals.** A self- and cross-exciting counting process with one dimension for buy-classified trades and one for sell-classified trades, whose kernel matrix describes how past buy and sell trades raise the future arrival intensity of both sides.
- **Vector Auto Regression (VAR) of minute buy/sell counts.** A linear time-series model in which the minute counts of buy and sell trades are each regressed on their own and each other's recent lagged values, with order selected by the Akaike Information Criterion.

## Method

Hawkes kernel parameters are estimated by maximum likelihood using a stochastic gradient descent procedure, and simulated forward using Ogata's modified thinning algorithm (with the TICK library used for some kernels). For each rolling one-hour fitting window the fitted model is simulated 500 times to build an empirical distribution of one-minute-ahead OFI, and the probability the model assigns to the value that actually occurred is recorded. The VAR model is instead fitted to minute-level buy/sell counts and simulated forward using the Gaussian error distribution of its coefficients.

Model comparison converts each window's assigned probability into a negative log-likelihood loss, aggregates these losses over ten-minute blocks across all 315 one-minute windows in the day, and applies Hansen's test for superior predictive ability, iterating over every candidate model as the benchmark, to determine which models cannot be statistically rejected as inferior to the others.

## Results

- Among parametric Hawkes kernels tested jointly with all others, the sum-of-exponential kernel scores 0.743 under the superior-predictive-ability test versus 0.002 for the plain exponential kernel, while the power-law kernel and the Poisson benchmark both score 0.0.
- Among non-parametric kernels, the Hawkes conditional-law kernel scores 0.257 in the joint test and 0.518 in a non-parametric-only test, clearly ahead of the EM-based kernel and Poisson, both at 0.0.
- The VAR model, fitted on minute-aggregated buy/sell counts, scores 0.101 in the joint test: worse than the sum-of-exponential and conditional-law Hawkes kernels but not statistically rejected outright.
- Realized one-minute OFI over the test day (315 observations) has mean -0.076, standard deviation 0.323, ranging from -0.779 to 0.765.
- An augmented Dickey-Fuller test rejects a unit root in realized OFI, with test statistic -12.878.
- Forecasts use a rolling one-hour fitting window, a one-minute forecast horizon, and 500 simulated paths per window to build the empirical OFI distribution.
- Because the sum-of-exponential kernel is Markovian, the authors argue it is far cheaper to fit and simulate than the conditional-law kernel, and prefer it in practice even though the superior-predictive-ability test cannot separate the two outright.

## Limitations

- The empirical study uses a single trading day of a single futures contract, so the model ranking is not shown to generalize across days or instruments.
- Reader note: no out-of-sample test across multiple days or a cross-section of instruments is reported, which limits confidence that the sum-of-exponential kernel would remain the best choice in other regimes.
- The paper notes that results over the full day may be biased in favor of the sum-of-exponential model given the nature of the superior-predictive-ability test.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow|order flow]]
- [[entities/aditya-nittur-anantha|Aditya Nittur Anantha]]
- [[entities/shashi-jain|Shashi Jain]]

## Citation

Aditya Nittur Anantha, Shashi Jain (2024). Forecasting high frequency order flow imbalance using Hawkes processes.

DOI: 10.48550/arxiv.2408.03594

Text ingested: `markdown_output/anantha-2024-forecasting-high-frequency-order-flow-imbalance.md`, converted from `raw/ofi-event-clock/anantha-2024-forecasting-high-frequency-order-flow-imbalance.pdf`.

Coverage of this summary: Read the whole markdown file end to end, including the introduction, data section, model descriptions, methodology, results, conclusion, references, and both numeric appendices.

Known problems with the input: Most of the paper's mathematical definitions (OFI, Hawkes intensity, likelihood, gradient expressions, VAR equations) were rendered by the PDF-to-markdown converter as omitted picture placeholders rather than text, so exact formula forms could not be verified beyond what survives in the surrounding prose and tables.
<!-- AUTHORED REGION END -->