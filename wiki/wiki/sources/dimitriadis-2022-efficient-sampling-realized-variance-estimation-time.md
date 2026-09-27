---
authors:
- Timo Dimitriadis
- Roxana Halbleib
- Jeannine Polivka
- Jasper Rennspies
- Sina Streicher
- Axel Friedrich Wolter
content_hash: sha256:df20059cd8e5ab16fa0e922d5f7cb861fa44893a2d14349e3b903588e9785ae7
created: 2026-09-27 01:47:00+00:00
page_id: sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time
page_type: source
related:
- concepts/sampling-clocks
- concepts/realized-variance
- concepts/high-frequency-data
- concepts/market-microstructure-noise
- concepts/hawkes-processes
- concepts/market-microstructure
- concepts/intrinsic-time
- concepts/stochastic-time-change
revision_id: 1
schema_version: 2
source_hash: sha256:cd51c8ead6424181250a9e9c88357a0f08e5d0e5eb0b2728ffbe03f56d901086
source_path: markdown_output/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time.md
source_type: paper
tags:
- realized-variance
- sampling-schemes
- high-frequency-econometrics
- market-microstructure-noise
- hawkes-processes
- volatility-forecasting
- clock-compares
- asset-equity
- harvest-relevant
title: Efficient Sampling for Realized Variance Estimation in Time-Changed Diffusion
  Models
updated: '2026-09-27T01:47:00Z'
uuid: 1640f285-5f52-53d3-b674-c6233c1094d0
year: 2025
---

<!-- AUTHORED REGION START -->
# Efficient Sampling for Realized Variance Estimation in Time-Changed Diffusion Models

## Summary

The paper asks how intraday returns should be sampled, in what kind of clock, to make the realized variance (RV) estimator of daily integrated variance as efficient as possible, given that trading activity and price variability both move unevenly through the day rather than at a constant calendar pace.

The authors build a joint model for trade arrivals and log-prices, called the tick-time stochastic volatility (TTSV) model, in which the price is a diffusion time-changed by a jump process representing ticks, with a separately evolving trading-intensity process and tick-variance process. Using this model they derive closed-form finite-sample mean-squared-error formulas for the RV estimator under different classes of sampling rule: schemes that may use the full observed (and possibly noisy) price path, and more restricted schemes that may only use estimated trading intensity, tick variance, and the count of observed ticks. They validate the theory with simulations of thousands of trading days under two process specifications, one with independent trading-intensity and tick-variance processes and one Hawkes-type version with a leverage effect and added microstructure noise, and then apply the sampling schemes to real NYSE trade data.

Hitting-time sampling (sample whenever the absolute price move since the last sample exceeds a threshold) attains the theoretical efficiency lower bound when the sampling rule can see the raw price, but this scheme is also the most exposed to microstructure noise. When sampling cannot use the noisy observed price directly, the newly proposed realized business-time sampling scheme (sample once a fixed amount of estimated tick variance has accumulated) is the most efficient. In simulations and on 27 NYSE stocks, both schemes clearly beat calendar-time and simple transaction-count sampling; hitting-time sampling wins at coarser sampling frequencies (around 5-minute intervals and longer) while realized business-time sampling wins at finer frequencies, and the same ranking carries through to one-day-ahead volatility forecasts.

What is new is the joint tick-arrival/price model that cleanly separates trading intensity from tick-level price variance, finite-sample (rather than only asymptotic) efficiency results for a broad class of sampling schemes, and the realized business-time scheme itself, which the authors show is a natural byproduct of the model.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Observations are resampled under several intrinsic-time clocks and compared against calendar time: transaction time (fixed counts of observed or expected trades), business time (fixed amounts of estimated or realized price variance), and hitting time (whenever the absolute price move exceeds a threshold). Each scheme is calibrated so the expected or realized number of intraday returns per day is held fixed at one of several values (13 to 390). The estimation target is the daily integrated variance; the same schemes are also used to build a next-day realized-variance forecast from the Corsi HAR model, evaluated out-of-sample over 1000 trading days after an 803-day rolling estimation window.

## Data

- **Asset class:** Equities
- **Instruments:** 27 liquid NYSE-listed stocks: AA, AXP, BA, BAC, CAT, DIS, GE, GS, HD, HON, HPQ, IBM, IP, JNJ, JPM, KO, MCD, MMM, MO, MRK, NKE, PFE, PG, UTX, VZ, WMT, XOM
- **Venue:** NYSE TAQ database
- **Period:** January 1, 2012 to March 31, 2019 for the realized-variance estimation-accuracy comparison; forecast evaluation covers 1000 trading days from March 28, 2015 to March 29, 2019 with an 803-day rolling estimation window
- **Granularity:** Trade-level (tick) data resampled to a fixed number of intraday returns per day, M in {13, 26, 39, 78, 130, 260, 390}, corresponding to intrinsic-time intervals of about 390/M minutes

## Features and Measures

- **Tick-Time Stochastic Volatility (TTSV) model.** A joint model where the log-price follows a Brownian motion that is time-changed by a jump process representing trade arrivals, with a separately evolving stochastic tick-variance process controlling the size of each price jump.
- **Calendar Time Sampling (CTS).** Sampling intraday returns at fixed, equally spaced clock-time intervals, ignoring trading activity or volatility patterns.
- **Transaction Time Sampling (TTS).** Sampling equidistant in the number of observed trades (realized TTS) or in the estimated trading-intensity process (intensity TTS).
- **Business Time Sampling (BTS).** Sampling equidistant in accumulated price variance, using either the estimated integrated variance path (intensity BTS) or the newly proposed combination of observed ticks and estimated tick variance (realized BTS).
- **Hitting Time Sampling (HTS).** Sampling whenever the observed absolute price change since the last sample exceeds a fixed threshold, without needing any estimated intensity process.

## Method

The TTSV model represents ticks as a doubly-stochastic Poisson or Hawkes-type jump process with intensity governing trading activity, and log-price jumps at each tick with a separate, time-varying tick-variance process; under stated independence assumptions the authors prove the RV estimator is unbiased for any adapted sampling scheme and derive closed-form finite-sample MSE expressions, showing that a Cauchy-Schwarz argument favors homogenizing either raw returns (hitting-time sampling), realized tick variance (realized business/transaction-time sampling), or estimated integrated variance (intensity business/transaction-time sampling), depending on what information the sampling rule is allowed to use.

They validate the theory in simulations of 5000 trading days from two TTSV specifications (an independent-process version and a Hawkes-type version with a leverage effect), adding i.i.d. or ARMA(1,1) microstructure noise at several magnitudes, and compare bias and RMSE of RV across calendar-time, realized/intensity transaction-time, realized/intensity business-time, and hitting-time schemes.

Empirically, they use trade data on 27 NYSE stocks and evaluate estimators with Patton's data-based ranking method and Diebold-Mariano tests using a stationary bootstrap, comparing to calendar-time and realized business-time baselines and to a pre-averaging RV estimator; they then test whether the same sampling schemes improve one-day-ahead volatility forecasts from the Corsi HAR model, judged by MSE and QLIKE loss and by inclusion in the model confidence set.

## Results

- The RV estimator is unbiased under any adapted sampling scheme, so schemes differ only in estimation variance, not bias.
- Hitting-time sampling attains the theoretical lower bound for the RV estimator's mean squared error when the sampling rule may depend on the observed price path.
- When sampling cannot use the noisy observed price directly, the newly proposed realized business-time scheme is the most efficient among the schemes considered.
- In simulations with no microstructure noise, hitting-time sampling gives the lowest RMSE at every sampling frequency tested; as noise increases its RMSE deteriorates fastest of all schemes.
- The sampling frequency at which realized business-time sampling starts to beat hitting-time sampling depends on the noise level and falls between about 30 seconds and 10 minutes of intrinsic time.
- On 27 NYSE stocks from 2012 to 2019, the more elaborate sampling schemes (realized/intensity transaction- and business-time, hitting-time) show far more significant loss improvements over calendar-time sampling than losses, especially under the QLIKE loss function.
- Hitting-time sampling beats realized business-time sampling at coarser sampling (around 5-minute intervals and longer, M up to 78); realized business-time sampling wins at finer sampling (M above 78) for most stocks.
- In one-day-ahead HAR forecasts, hitting-time sampling achieves the best average rank and win rate at low sampling frequencies (M below 78); no single scheme consistently wins at higher frequencies.

## Limitations

- The finite-sample efficiency results for realized and intensity business/transaction-time sampling require strong independence conditions on the underlying trading-intensity, tick-variance, and jump processes.
- The empirical application uses data from only 27 liquid NYSE stocks, and the underlying TAQ data files cannot be shared, so only the simulation code is fully replicable.
- Hitting-time sampling cannot fix the exact number of samples per day (only its expectation), which the authors note makes practical calibration and comparison to other schemes harder.
- Reader note: all empirical evidence is from equities on a single US exchange (NYSE); the paper does not test other asset classes or venues.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]

## Citation

Timo Dimitriadis, Roxana Halbleib, Jeannine Polivka, Jasper Rennspies, Sina Streicher, Axel Friedrich Wolter (2025). Efficient Sampling for Realized Variance Estimation in Time-Changed Diffusion Models.

DOI: 10.48550/arxiv.2212.11833

Text ingested: `markdown_output/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time.md`, converted from `raw/ofi-event-clock/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time.pdf`.

Coverage of this summary: Read the abstract, introduction, Sections 2.1-2.4 (TTSV model and definitions of the six sampling schemes), Section 3 (simulation study), Section 4 (empirical applications: estimation accuracy and forecast performance), and the conclusion; did not read Appendices A-G (proofs and supplementary simulation/empirical results) or the full reference list.

Known problems with the input: The paper header prints 'October 23, 2025' as its date, which differs from the year embedded in the job slug/year_hint (2022); 2025 is used as the year printed on this version of the paper.
<!-- AUTHORED REGION END -->