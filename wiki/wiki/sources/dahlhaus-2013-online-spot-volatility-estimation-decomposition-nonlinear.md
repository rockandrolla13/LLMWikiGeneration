---
authors:
- Rainer Dahlhaus
- Jan C. Neddermeyer
content_hash: sha256:b2b601bb9259a47ecf4ab0599bf6269f535ce2946f55fa8da248411c81da83b1
created: 2026-09-27 01:47:00+00:00
page_id: sources/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear
page_type: source
related:
- concepts/stochastic-time-change
- concepts/market-microstructure-noise
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/bid-ask-spread
- concepts/particle-filter
revision_id: 1
schema_version: 2
source_hash: sha256:19a87523b70ddb7d68a7dd31ede4bf70801fa849cb0109e579aa09a4e08546a0
source_path: markdown_output/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear.md
source_type: paper
tags:
- spot-volatility
- particle-filter
- market-microstructure-noise
- transaction-time
- volatility-decomposition
- on-line-estimation
- trading-intensity
- clock-time-change
- asset-equity
- harvest-relevant
title: On-line Spot Volatility-Estimation and Decomposition with Nonlinear Market
  Microstructure Noise Models
updated: '2026-09-27T01:47:00Z'
uuid: 2b350bcb-df8e-532f-a2da-45dd3643b65e
year: 2012
---

<!-- AUTHORED REGION START -->
# On-line Spot Volatility-Estimation and Decomposition with Nonlinear Market Microstructure Noise Models

## Summary

The paper asks how to estimate time-varying spot volatility on-line from raw tick-by-tick transaction data, updating the estimate the instant a new trade arrives, without assuming evenly spaced trade times and without interpolating prices. The authors treat the unobserved efficient log-price as a latent state in a nonlinear state-space model and propose a family of nonlinear market microstructure noise models in which the observed transaction price is a generalized rounding of the efficient price onto a discrete, possibly time-varying set of feasible levels (nearest cent, order-book levels, or dealer bid/ask quotes). A computationally efficient particle filter approximates the filtering distribution of the efficient price given the trade history, and a sequential (on-line) Expectation-Maximization-type recursion turns those particles into a running volatility estimate, with an adaptive step-size scheme (SAGES) for handling time-varying volatility.

A central methodological contribution is a decomposition of clock-time (per-calendar-time) volatility into volatility per transaction multiplied by the trading intensity (the rate of transactions per unit time), obtained by treating the transaction count as a random time change (subordination) applied to the efficient-price diffusion. This lets the authors estimate and compare a transaction-time volatility curve and a clock-time volatility curve for the same underlying security.

On simulated data the proposed recursive estimator has lower variance than a simpler additive-noise benchmark recursive estimator, and the deterministic-rounding version of the noise model reproduces the autocorrelation and partial-autocorrelation pattern of real transaction returns better than a stochastic-rounding version. On real TAQ transaction and quote data for Citigroup, transaction-time volatility is close to constant through most of the trading day while clock-time volatility shows the well-known intraday U-shape; the paper attributes that U-shape mainly to the pattern of trading intensity rather than to the per-transaction volatility itself. What is new relative to prior spot-volatility work is the combination of a general, history-dependent rounding-noise model, a fully sequential particle filter that avoids equidistant-time or interpolation assumptions, and the explicit transaction-time/clock-time volatility decomposition.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

Observations are individual transaction prices, arriving at irregular real trade times; the efficient log-price is modeled as a random walk in transaction time (one increment per trade) and the sequence of trade times is treated as a stochastic point process that subordinates (random-time-changes) this process to calendar time. The volatility estimate is updated immediately after each new transaction rather than on a fixed calendar or forecast horizon; the paper separately derives an estimator of volatility per transaction and, via the random-time-change relationship, an estimator of volatility per calendar-time unit, and compares the two on the same data.

## Data

- **Asset class:** Equities
- **Instruments:** Citigroup common stock (ticker C), transactions and market-maker/NYSE quotes; also purely simulated efficient-price and transaction-price data
- **Venue:** NYSE, via the TAQ database
- **Period:** 3rd September 2007 (single trading day, real-data example); simulations use no calendar period
- **Granularity:** tick-by-tick / per-transaction data (transaction and quote time stamps with one-second precision in the real data)

## Features and Measures

- **generalized rounding noise model.** A model of the observed transaction price as a deterministic or stochastic rounding of the unobserved efficient price onto a discrete set of feasible levels (nearest cent, order-book levels, or dealer quotes), where the feasible set can depend on past trades and exogenous information.
- **transaction-time spot volatility estimator.** An on-line estimator of the volatility of the efficient log-price increment per transaction, produced by a sequential EM-type recursion applied to particle-filter output.
- **clock-time spot volatility estimator (decomposed).** An estimator of per-calendar-time volatility obtained as the product of the transaction-time volatility estimator and an estimated trading intensity (transactions per unit time), derived from the random-time-change relationship between transaction time and clock time.
- **trading intensity estimator.** A recursive estimate of the local rate of transactions per unit calendar time, computed from the inverse of averaged inter-trade durations with a bias correction.
- **SAGES adaptive step size.** Spatially aggregated exponential smoothing: several versions of the on-line volatility recursion are run in parallel with different fixed step sizes, and a convex combination of them is taken at each step to adapt locally to how fast volatility is changing.

## Method

The efficient log-price is the latent state of a nonlinear state-space model; the observation equation is the generalized rounding noise model described above, and the state equation is a random walk in transaction time with a (possibly time-varying) volatility parameter. A particle filter approximates the filtering distribution of the efficient price given the trade history; because the noise model implies a truncated-normal optimal importance-sampling proposal, the filter is computationally cheap and needs relatively few particles. A sequential EM-type recursion then uses the particle approximation to update a covariance/volatility estimate after every transaction, with different step-size rules for the time-constant case (a decaying step size) and the time-varying case (a fixed or SAGES-adaptive step size).

Performance is judged in two ways. On simulated data with known true volatility, the proposed estimator is compared, via box plots over independent simulation runs, against a simpler recursive benchmark estimator (based on an additive, linear microstructure-noise correction) and against an infeasible 'optimal' estimator that uses the true latent efficient prices; the same simulated data are also used to check that the deterministic-rounding noise model reproduces the autocorrelation and partial-autocorrelation shape of real returns better than stochastic rounding. On real TAQ data for a single stock and day, the method is applied first to raw transaction data only (levels estimated from past trades) and then to a hand-matched subset with real dealer quotes available, and the resulting transaction-time and clock-time volatility curves are inspected visually and compared to the benchmark estimator.

## Results

- The particle filter needs only about 500 particles to reach adequate precision, keeping the method computationally cheap enough for real-time, per-trade updating.
- In the time-constant simulation the recursive estimator is closest to the infeasible optimal estimator when the step-size decay parameter is set to 0.9, and the benchmark estimator shows larger variance than the proposed estimator across all settings tried.
- Resampling in the particle filter, using an effective-sample-size threshold of 0.2, was triggered only about every 15th iteration, because the optimal importance-sampling proposal keeps particle weights from degenerating quickly.
- In a simulation of 15,000 transactions (representative of one trading day for a liquid stock), the proposed estimator and its SAGES-adaptive version tracked a time-varying volatility path more closely than the benchmark recursive estimator, and recovered within about a minute after an injected price jump of 8 cents at transaction 5,000.
- On the real Citigroup data for 3rd September 2007, transaction-time (per-trade) volatility is estimated to be almost constant after about 11:00, while clock-time volatility shows the familiar intraday U-shape, indicating the U-shape is driven mainly by the pattern of trading intensity rather than by the per-transaction volatility itself.
- The deterministic-rounding version of the noise model produced volatility estimates at the same overall level as the (differently specified) benchmark estimator, which the authors read as evidence that deterministic rounding is the better-specified noise model, versus stochastic rounding which gave a visibly different, lower estimated level.

## Limitations

- Validated on a single stock (Citigroup) and a single trading day, so intraday-pattern findings (e.g. the U-shape attribution) are drawn from one case rather than a broad cross-section.
- The authors state that a complete asymptotic theory (consistency, rate of convergence) for the sequential EM-type estimator under time-varying volatility is not derived and is expected to be hard to obtain, especially once the adaptive SAGES step-size scheme is used.
- The multivariate extension is presented only for synchronous trading times; the authors explicitly flag non-synchronous multi-asset trading as unresolved future work.
- Reader note: the paper reports a volatility-estimation and decomposition method rather than a trading signal or return-prediction test, so it offers no evidence on whether the transaction-time/trading-intensity decomposition improves any downstream forecasting or trading objective.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/particle-filter|particle filter]]

## Citation

Rainer Dahlhaus, Jan C. Neddermeyer (2012). On-line Spot Volatility-Estimation and Decomposition with Nonlinear Market Microstructure Noise Models.

DOI: 10.1093/jjfinec/nbt008

Text ingested: `markdown_output/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear.md`, converted from `raw/ofi-event-clock/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear.pdf`.

Coverage of this summary: Read the paper in full from the abstract and introduction through the noise-model section, particle filter and sequential EM sections, the clock-time decomposition, implementation and adaptation details, both simulation studies and the real-data (TAQ Citigroup) application, and the concluding remarks and references.

Known problems with the input: Nearly all mathematical equations were rendered as omitted picture placeholders rather than text in the markdown conversion, so model equations are described qualitatively rather than reproduced; No journal or conference venue name is printed anywhere in the extracted text (only an acknowledgement to a journal co-editor), so venue is left blank rather than guessed; The job file's year_hint (2013) differs from the year printed on the paper itself ('July 2012'); the printed year was used.
<!-- AUTHORED REGION END -->