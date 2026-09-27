---
authors:
- Sophon Tunyavetchakit
content_hash: sha256:8bcb9e1bf8e556852cc4ff950bbec809fb4177f357a38da1dd8bd1827f0bbf25
created: 2026-09-27 01:47:00+00:00
page_id: sources/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility
page_type: source
publication_venue: Inaugural dissertation, Ruprecht-Karls-Universität Heidelberg (Naturwissenschaftlich-Mathematische
  Gesamtfakultät)
related:
- concepts/stochastic-time-change
- concepts/market-microstructure-noise
- concepts/high-frequency-data
- concepts/realized-variance
- concepts/autocorrelation-time-series
revision_id: 1
schema_version: 2
source_hash: sha256:2057d5a2f76f8fca69b89d8b185016660d0e4bc99feb881d8f5d4dcdd1fdc69b
source_path: markdown_output/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility.md
source_type: paper
tags:
- spot-volatility
- market-microstructure-noise
- pre-averaging
- tick-time
- trading-intensity
- high-frequency-data
- clock-time-change
- asset-equity
- harvest-relevant
title: Volatility Decomposition and Nonparametric Estimation of Spot Volatility of
  Models with Poisson Sampling under Market Microstructure Noise
updated: '2026-09-27T01:47:00Z'
uuid: 758e5440-3988-56e0-8958-9a1715ee3d9f
year: 2016
---

<!-- AUTHORED REGION START -->
# Volatility Decomposition and Nonparametric Estimation of Spot Volatility of Models with Poisson Sampling under Market Microstructure Noise

## Summary

Existing estimators of spot volatility under market microstructure noise are mostly developed for diffusion price models sampled in calendar time. This dissertation instead studies spot volatility of a time-changed price model based on transaction (tick) times, and asks whether decomposing calendar-time (clock-time) volatility into a tick-time volatility curve and a trading-intensity curve, each estimated separately, can improve estimation quality and convergence, especially in the presence of microstructure noise.

The price is modeled as a Brownian motion subordinated (time-changed) by a point process of transaction arrivals with a time-varying intensity, so that clock-time spot volatility equals the product of tick-time volatility and trading intensity. Tick-time volatility under microstructure noise is estimated with a pre-averaging technique adapted from existing noise-robust diffusion estimators, and trading intensity is estimated by nonparametric kernel smoothing of transaction arrival times; multiplying the two curves gives an 'alternative' clock-time volatility estimator, whose asymptotic properties (rate of convergence, asymptotic variance) are derived and compared to those of the classical, non-decomposed clock-time estimator using an infill-asymptotic approach as the observation time span grows.

Theoretically and in Monte Carlo simulation, the decomposition-based estimator can achieve a faster rate of convergence than the classical estimator, particularly when tick-time volatility varies more smoothly than trading intensity, though the benefit depends on choosing an appropriately longer smoothing window for the tick-time component. Applying both estimators to real intraday transaction data for several DJIA stocks traded on NASDAQ in April 2014, the tick-time volatility curve is consistently smoother than both trading intensity and clock-time volatility, the familiar intraday U-shape (volatility smile) is shown to be mainly a feature of trading intensity rather than tick-time volatility, and the effect of microstructure noise on spot volatility estimation in this data is found to be very small.

What is new is the volatility decomposition itself as a concrete estimation device (rather than only a conceptual observation), its theoretical treatment via infill asymptotics for both noiseless and noisy transaction-time models, a pre-averaging based tick-time volatility estimator adapted to this setting, and an empirical demonstration on real ultra-high-frequency equity data that tick-time volatility and trading intensity can be separated and interpreted individually.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

Prices are modeled as a Brownian motion time-changed (subordinated) by a nonhomogeneous Poisson point process of transaction arrivals with intensity function lambda(t); calendar-time (clock-time) spot volatility is decomposed as the product of a tick-time (per-transaction) volatility curve and this trading intensity. Both component curves, and the standard clock-time volatility, are estimated nonparametrically (kernel smoothing and pre-averaging) from transaction-time observations and compared to each other. There is no fixed prediction horizon: the goal is estimating the instantaneous (spot) volatility curve over a trading day, not forecasting a future value.

## Data

- **Asset class:** Equities
- **Instruments:** Simulated transaction-time price paths (Monte Carlo study); real data: intraday transaction data for stocks listed in the Dow Jones Industrial Average (40 symbols, Table 6.3), with detailed results reported for Cisco Systems (CSCO), Citigroup (C), General Motors (GM), Microsoft (MSFT) and Intel (INTC)
- **Venue:** NASDAQ stock exchange (General Motors also compared on NYSE); real-data vendor QuantQuote TickView
- **Period:** Simulation: 500 Monte Carlo repetitions (no calendar period); real data: April 1-30, 2014, with day-by-day detail for April 1-4, 2014
- **Granularity:** Transaction (tick) level data, timestamped to 1-second resolution; e.g. Cisco Systems had 35,056 transactions on NASDAQ on April 1, 2014, and Microsoft had 49,521 on April 4, 2014, with heavily traded DJIA stocks generally exceeding 15,000 transactions per day

## Features and Measures

- **tick-time (transaction-time) volatility.** The diffusion volatility measured per transaction rather than per unit of calendar time; estimated with a noise-robust pre-averaging technique adapted to the transaction-time model.
- **trading intensity.** The instantaneous rate of transaction arrivals, modeled as the (time-varying) intensity of a nonhomogeneous Poisson point process and estimated by nonparametric kernel smoothing.
- **decomposition-based (alternative) clock-time volatility estimator.** The calendar-time spot volatility formed by multiplying separately estimated tick-time volatility and trading intensity curves, rather than estimating clock-time volatility directly.
- **classical clock-time volatility estimator.** The standard nonparametric spot volatility estimator applied directly to calendar-time price observations, without decomposing it into tick-time volatility and intensity.

## Method

The dissertation constructs a diffusion process subordinated by a point process (a time-changed Brownian motion) to represent transaction-time price dynamics, then derives the asymptotic properties (rate of convergence, asymptotic variance) of both the classical clock-time volatility estimator and the new decomposition-based estimator using an infill-asymptotic approach as the observation time span grows, for both noiseless and noisy (microstructure-contaminated) versions of the model. Tick-time volatility under noise is estimated via a pre-averaging technique adapted from existing noise-robust diffusion estimators; trading intensity is estimated by kernel smoothing of transaction arrival times, using an Epanechnikov kernel chosen for giving a smaller mean integrated squared error than a triweight kernel in simulation. Performance is first assessed in a Monte Carlo simulation: 500 repetitions of a simulated transaction-time price process generating about 23,000 trades per day, evaluated by numerical bias, variance and mean squared/integrated squared error across nine time points spanning the trading day, under several additive-noise levels and bandwidth/segment-length choices, and benchmarked against a filtering-based estimator from Dahlhaus and Neddermeyer. The estimators are then applied to real intraday transaction data for DJIA stocks traded on NASDAQ (and NYSE for one comparison) in April 2014, obtained from QuantQuote TickView, after removing pre- and after-market trades, restricting to a single exchange, and filtering outliers and abnormal sale conditions.

## Results

- The main theoretical comparison (Table 4.2) shows the decomposition-based estimator can achieve a faster rate of convergence than the classical clock-time estimator in many cases, particularly when tick-time volatility is smoother than trading intensity.
- With an unfavourable segment-length choice in simulation, the decomposition-based estimator's numerical MSE beat the classical estimator's at only 43 out of 99 tested time points, showing no clear advantage.
- Using a longer smoothing window for tick-time volatility (segment length N ~ 0.012T instead of matching the clock-time window), the decomposition-based estimator's numerical MSE improved at 97 out of 99 time points and its numerical MISE fell by about 30%.
- The Epanechnikov kernel gave a smaller mean integrated squared error than the triweight kernel in simulation, e.g. 1.502683e-8 versus 1.970044e-8 for the clock-time volatility estimator.
- In real intraday data for DJIA stocks (CSCO, C, GM, MSFT, INTC) traded on NASDAQ in April 2014, the tick-time volatility curve was consistently smoother than both the clock-time volatility curve and the trading intensity curve.
- The well-known intraday U-shape (volatility smile) was found to be mainly a feature of the trading intensity curve, not the tick-time volatility curve.
- The effect of market microstructure noise on spot volatility estimation was very small for the real DJIA data studied, since the pre-averaging, noiseless realized-volatility, and Dahlhaus-Neddermeyer benchmark estimators produced very similar curves.
- For General Motors, the tick-time volatility estimate was rougher on the less liquid NYSE than on NASDAQ, attributed to the smaller number of transactions on the NYSE.

## Limitations

- The pre-averaging estimator performs poorly (high finite-sample variance) in small samples despite its theoretical robustness to noise, as the simulation study shows.
- The advantage of the decomposition-based estimator over the classical one depends strongly on the choice of smoothing window/segment length; the thesis does not implement a fully automatic, data-driven bandwidth selection method and defers this to future work.
- The core asymptotic theory is developed for deterministic (not stochastic) volatility and intensity curves; extensions to stochastic curves and to a leverage effect between price, volatility and market activity are only briefly discussed, not fully worked out.
- Detailed real-data results are reported for only 5 of the 40 DJIA stocks listed, over a roughly one-month window (April 2014).
- Reader note: the real-data analysis is a set of illustrative case studies on a handful of highly liquid, large-cap US stocks over one month, rather than a systematic evaluation across many assets, periods or markets.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]

## Citation

Sophon Tunyavetchakit (2016). Volatility Decomposition and Nonparametric Estimation of Spot Volatility of Models with Poisson Sampling under Market Microstructure Noise. Inaugural dissertation, Ruprecht-Karls-Universität Heidelberg (Naturwissenschaftlich-Mathematische Gesamtfakultät).

DOI: 10.11588/heidok.00021450

Text ingested: `markdown_output/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility.md`, converted from `raw/ofi-event-clock/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility.pdf`.

Coverage of this summary: Read the title page, German and English abstracts, acknowledgments, and table of contents; the full Introduction (Chapter 1) including its chapter-by-chapter summary; the opening framing of Chapter 2 (Preliminaries) on realized volatility and Poisson processes; and the full Chapter 6 (Empirical Analysis and Simulation) and Chapter 7 (Conclusion). The detailed theoretical development and proofs in Chapters 2-5 (and the Appendices) were not read section-by-section beyond what the Introduction summarizes.

Known problems with the input: This is a+ PhD dissertation; per the reading guidance for long documents, only the abstract, introduction, empirical/real-data chapter and conclusion were read in full, not the intervening theoretical chapters in section-by-section detail, so some derivations and assumptions there are not directly verified here; No explicit publication/submission year is printed on the title or abstract pages read (the oral-defense date field is blank in the converted text); year taken from the job file's year_hint; Most mathematical formulas throughout the document are rendered as omitted images in the converted markdown, so model and estimator definitions here are reconstructed from the surrounding prose rather than the equations themselves.
<!-- AUTHORED REGION END -->