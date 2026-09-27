---
authors:
- Patrick Chang
- Etienne Pienaar
- Tim Gebbie
content_hash: sha256:a9212dcc1373235c585a52f81befdde99d147e587cb87d9672e55abdf5c3a3d9
created: 2026-09-27 01:47:00+00:00
page_id: sources/chang-2021-epps-effect-under-alternative-sampling-schemes
page_type: source
related:
- concepts/sampling-clocks
- concepts/high-frequency-data
- concepts/hawkes-processes
- concepts/market-microstructure-noise
- concepts/autocorrelation-time-series
- concepts/realized-variance
- concepts/realized-covariance
- concepts/stylized-facts
- concepts/epps-effect
- concepts/volume-clock
- entities/tim-gebbie
revision_id: 1
schema_version: 2
source_hash: sha256:5975bd469ca06ac5c744b6de39d424bb6c9cd8a61699a749fae5830893033f87
source_path: markdown_output/chang-2021-epps-effect-under-alternative-sampling-schemes.md
source_type: paper
tags:
- epps-effect
- volume-time
- calendar-time
- trade-time
- hawkes-process
- correlation-estimation
- sampling-schemes
- clock-compares
- asset-equity
- harvest-relevant
title: The Epps effect under alternative sampling schemes
updated: '2026-09-27T01:47:00Z'
uuid: d0f12b55-b620-59d0-9d63-c950bff48399
year: 2021
---

<!-- AUTHORED REGION START -->
# The Epps effect under alternative sampling schemes

## Summary

The paper asks how the choice of time definition, calendar time, event (trade) time, or volume time, affects the Epps effect, the well-known tendency for measured cross-asset return correlation to change with the sampling time scale. Prior work on the Epps effect had studied calendar-time sampling almost exclusively; this paper directly compares all three time definitions using the same underlying price process, and contrasts a Fourier-domain estimator (Malliavin-Mancino, MM) against the classical realized-volatility (RV) estimator and the Hayashi-Yoshida (HY) asynchrony-correction estimator as a baseline.

To generate a realistic but controlled price process, the authors simulate a bivariate Hawkes process (the Bacry et al. fine-to-coarse model) for trade arrivals and log-prices, pairing it with an independent power-law distribution for trade volumes. They compute the Epps curve, correlation as a function of sampling interval, under each time definition and estimator, then repeat the exercise on real transaction data for four banking stocks on the Johannesburg Stock Exchange (JSE).

The main finding is that the Epps effect is present under all three time definitions, but its shape differs: correlations emerge with a similar concave, exponential-like shape under calendar and event time, but emerge faster (over fewer units) under event time, whereas under volume time correlations emerge linearly and reach a markedly lower level at large sampling intervals. This linear volume-time pattern appears regardless of which distribution generates the trade volumes. The empirical JSE results reproduce these simulated patterns for sufficiently correlated stock pairs, but the paper notes the results become ambiguous, and in one case the correlation turns negative, for less correlated pairs, so the generalization is confirmed only for correlated assets.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper directly contrasts three time definitions applied to the same simulated and empirical price series: calendar time (fixed wall-clock sampling intervals, using previous-tick interpolation for RV and raw event timestamps for MM/HY), event/trade time (time incremented by one unit per transaction, shared across the pair via a common event clock and previous-tick interpolated for RV), and volume time (time incremented by one unit per unit of volume traded, implemented via volume buckets so each security yields the same number of homogeneous, synchronous samples). The prediction horizon in each case is the correlation measured at sampling intervals ranging from 1 up to 100 (simulation) or 300 (empirical) time units, not a fixed forecast horizon.

## Data

- **Asset class:** Equities
- **Instruments:** Simulated: a bivariate Hawkes-process price pair. Empirical: Standard Bank Group (SBK), Nedbank Group (NED), Absa Group (ABG) and FirstRand (FSR), with Anglo American (AGL) and British American Tobacco (BTI) used in an uncorrelated-pair appendix check
- **Venue:** Johannesburg Stock Exchange (JSE); empirical data sourced from Bloomberg Pro
- **Period:** Simulation: 100 replications of a Hawkes price path over T = 72,000 seconds, plus a single illustrative pair over T = 300 seconds. Empirical: five trading days, 24/06/2019 to 28/06/2019
- **Granularity:** Simulation: individual Hawkes-process event (trade) times. Empirical: transaction-level data reported only to second-level accuracy (09:00-16:50 trading session), so same-second trades for a security are aggregated by a volume-weighted average

## Features and Measures

- **Malliavin-Mancino (MM) Fourier estimator.** A Fourier-coefficient-based covariance estimator that lets the analyst probe different sampling time scales by choosing the number of Fourier coefficients used, without resampling the raw asynchronous observations onto a common grid.
- **Hayashi-Yoshida (HY) estimator.** A cumulative covariance estimator that corrects for asynchronous trade arrival between two assets, used here as a baseline that removes the asynchrony source of the Epps effect but cannot itself probe different time scales.
- **Realized Volatility (RV) estimator.** The standard sum-of-squared/cross returns estimator computed on a synchronous, homogeneous grid obtained via previous-tick interpolation, used as the classical benchmark under each time definition.
- **Calendar, event and volume time.** Three alternative ways to index observations: fixed wall-clock intervals (calendar time), a shared count of transactions across the pair (event/trade time), and a count that increments with cumulative traded volume, aggregated into equal-sized volume buckets (volume time).

## Method

A four-dimensional mutually-exciting Hawkes process (the Bacry et al. fine-to-coarse model) is used to simulate a correlated bivariate log-price pair, with trade volumes drawn independently from a power-law distribution. The RV, MM and HY estimators are each computed on this simulated pair under calendar time, event time and volume time, and the resulting Epps curves (correlation versus sampling interval) are compared against the model's own theoretical and limiting correlation expressions. The same three estimators and three time definitions are then applied to five days of JSE transaction data for four banking stocks, with correlations computed separately per trading day and averaged across days, and additional volume-generating distributions (uniform, normal, beta) tested in simulation to check whether the volume-time pattern depends on the volume distribution.

## Results

- The Epps effect (a change in measured correlation with sampling interval) is present under all three time definitions, in both the simulation and the JSE data.
- Correlations emerge faster (over fewer sampling units) under event/trade time than under calendar time, for both the MM and RV estimators.
- Under volume time, correlations emerge linearly rather than with the concave shape seen in calendar and event time, and reach a markedly lower correlation level at large sampling intervals.
- All three estimators (RV, MM and HY) recover numerically the same correlation estimates under volume-time sampling.
- The HY estimate under event time is identical to the HY estimate under calendar time, because the underlying asynchronous observations used in its computation are unchanged by the event-time relabeling.
- The linear Epps effect under volume time appears regardless of whether trade volumes are generated by a power-law, uniform, normal, or symmetric beta distribution.
- The empirical JSE results reproduce the simulated pattern (event time fastest, volume time linear) for sufficiently correlated stock pairs, such as SBK/FSR and NED/ABG.
- For weaker or uncorrelated pairs (e.g. NED/AGL, NED/BTI), the calendar-time Epps curve can turn negative at longer lags and the calendar-versus-event-time comparison becomes ambiguous; the NED/FSR pair's correlation also goes negative under volume time in the empirical data.

## Limitations

- The empirical study covers only five trading days on four (plus two appendix) JSE stocks.
- Trade timestamps are only resolved to the second, so the true within-second and within-block ordering of events could not be recovered, requiring same-second trades to be treated as simultaneous and volume-weight-averaged.
- The generalization of the simulated patterns to empirical data is confirmed only for sufficiently correlated asset pairs; uncorrelated or weakly correlated pairs show ambiguous or anomalous behavior.
- The underlying mechanism that produces the linear Epps effect under volume time is not explained by the paper, only documented empirically and in simulation.
- Reader note: the simulation model does not encode intraday seasonality of volatility, transactions or volumes, which the authors themselves flag as a possible source of unmodeled dynamics, particularly under volume time.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/realized-covariance|realized covariance]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/epps-effect|Epps Effect]]
- [[concepts/volume-clock|Volume Clock]]
- [[entities/tim-gebbie|Tim Gebbie]]

## Citation

Patrick Chang, Etienne Pienaar, Tim Gebbie (2021). The Epps effect under alternative sampling schemes.

DOI: 10.1016/j.physa.2021.126329

Text ingested: `markdown_output/chang-2021-epps-effect-under-alternative-sampling-schemes.md`, converted from `raw/ofi-event-clock/chang-2021-epps-effect-under-alternative-sampling-schemes.pdf`.

Coverage of this summary: Read the full paper including the abstract, introduction, the section on temporal metrics, the estimator definitions (Malliavin-Mancino, Hayashi-Yoshida, Realized Volatility), the full simulation experiments section (Hawkes process, calendar/event/volume time), the empirical JSE section, conclusion and the uncorrelated-assets appendix.

Known problems with the input: No publication year is printed on this version of the paper itself (no date line, and the body text gives no year); the year field uses the job file's year_hint (2021), which is consistent with the paper's own self-citations of a related dataset and code repository dated 2020.
<!-- AUTHORED REGION END -->