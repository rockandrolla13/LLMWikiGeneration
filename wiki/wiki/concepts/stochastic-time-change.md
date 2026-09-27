---
content_hash: sha256:e09e22c000593cbaa9904657481490eb284232fcf529938b38640736359a8f22
created: 2026-09-27 01:47:00+00:00
mind_map_priority: medium
page_id: concepts/stochastic-time-change
page_type: concept
related:
- concepts/sampling-clocks
- concepts/trade-clock
- concepts/volume-clock
- concepts/stylized-facts
- concepts/realized-variance
- concepts/long-memory
revision_id: 1
schema_version: 2
sources:
- sources/aldrich-2014-random-walk-high-frequency-trading
- sources/angstmann-2026-event-time-order-flow-memory-operational
- sources/angstmann-2026-revisiting-trade-sign-long-memory-square
- sources/berardi-2005-time-foreign-exchange-markets
- sources/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear
- sources/dahlhaus-2016-volatility-decomposition-estimation-time-changed-price
- sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time
- sources/gillemot-2006-there-s-more-volatility-than-volume
- sources/oomen-2004-properties-realized-variance-pure-jump-process
- sources/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed
- sources/scheiber-2017-new-strategies-asset-classes-increased-performance
- sources/silva-2005-applications-physics-finance-economics-returns-trading
- sources/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate
- sources/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility
- sources/turkoglu-2015-natural-time-crash-risk
- sources/vliet-2026-information-arrival-stochastic-clock-intraday-trading
tags:
- time-change
- subordination
- business-time
- stochastic-clock
- stylized-facts
title: Stochastic Time Change
updated: '2026-09-27T01:47:00Z'
uuid: 82dcc429-5f66-5c5a-b23a-4c910adc7d58
---

<!-- AUTHORED REGION START -->
# Stochastic Time Change

A stochastic time change treats the market's clock as a random process. Prices are assumed to follow a simple process, such as a random walk, when measured in an internal operational time. That operational time runs fast or slow relative to the wall clock, depending on how active the market is. The idea is also called subordination, and the internal clock is often called business time.

## What it explains

Returns over fixed intervals of wall-clock time have fat tails and volatility that comes in clusters. Under a time change, both can arise from the randomness of the clock alone. If so, returns measured in operational time should be close to a normal distribution.

## How it connects to sampling

The internal clock cannot be observed, so an observable stand-in is used: the number of trades, the traded volume, or the number of quotes. Sampling on a [[concepts/trade-clock|trade clock]] or [[concepts/volume-clock|volume clock]] is then a test of whether that stand-in is the right one.

## Difference from the other clock pages

The other [[concepts/sampling-clocks|sampling clocks]] are ways of cutting data. A stochastic time change is a modelling assumption about how prices are generated. A paper can use one without the other.

## Caveats

Which observable best stands in for the internal clock is disputed, and the sources here do not agree. A time change that restores normality in one market or period may fail in another. A single clock also cannot account for every feature of returns, so it is a partial explanation.

## Sources in This Wiki

- [[sources/aldrich-2014-random-walk-high-frequency-trading|The Random Walk of High Frequency Trading]] (Eric M. Aldrich, Indra Heckenbach, Gregory Laughlin, 2014). Models high-frequency E-mini S&P 500 futures returns by combining a Gaussian trade-time return distribution with a duration model of trade arrivals, then studies market stability limits.
- [[sources/angstmann-2026-event-time-order-flow-memory-operational|Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market Observables]] (Christopher Angstmann, Tim Gebbie, 2026). Builds a discrete-time random-walk order book model separating event, operational, and calendar time, showing trade-sign memory and square-root price impact are distinct laws linked only by time subordination.
- [[sources/angstmann-2026-revisiting-trade-sign-long-memory-square|Revisiting Trade-sign Long-memory and Square-root Law price impact]] (Chris Angstmann, Tim Gebbie, 2026). Derives the square-root impact law and the Lillo-Mike-Farmer trade-sign long-memory law from one discrete bid/ask reaction-diffusion model, arguing they are physical-time and event-time statements respectively.
- [[sources/berardi-2005-time-foreign-exchange-markets|Time and foreign exchange markets]] (Luca Berardi, Maurizio Serva, 2005). Tests whether FX price dynamics fit calendar-time or business-time (quote-count) models using one year of DEM/USD tick quotes.
- [[sources/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear|On-line Spot Volatility-Estimation and Decomposition with Nonlinear Market Microstructure Noise Models]] (Rainer Dahlhaus, Jan C. Neddermeyer, 2012). A particle-filter and sequential EM method updates spot volatility after every transaction and splits clock-time volatility into per-transaction volatility times trading intensity.
- [[sources/dahlhaus-2016-volatility-decomposition-estimation-time-changed-price|Volatility Decomposition and Estimation in Time-Changed Price Models]] (Rainer Dahlhaus, Sophon Tunyavetchakit, 2018). Decomposes clock-time spot volatility into tick-time volatility times trading intensity in a transaction-time price model, and shows the resulting estimator converges faster under microstructure noise.
- [[sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time|Efficient Sampling for Realized Variance Estimation in Time-Changed Diffusion Models]] (Timo Dimitriadis, Roxana Halbleib, Jeannine Polivka and others, 2025). Derives finite-sample efficiency theory for realized variance under intrinsic-time sampling schemes and shows empirically that hitting-time and a new realized business-time scheme beat calendar-time sampling.
- [[sources/gillemot-2006-there-s-more-volatility-than-volume|There’s more to volatility than volume]] (László Gillemot, J. Doyne Farmer, Fabrizio Lillo, 2006). Empirical study showing that neither trade count nor volume, but the order and size of individual price changes, drives clustered volatility and heavy tails in NYSE and LSE stock returns.
- [[sources/oomen-2004-properties-realized-variance-pure-jump-process|Properties of Realized Variance for a Pure Jump Process: Calendar Time Sampling versus Business Time Sampling]] (Roel C.A. Oomen, 2004). Derives closed-form bias and MSE of realized variance for a compound-Poisson price process under calendar-time vs business-time sampling, and finds business-time sampling reduces MSE using IBM transaction data.
- [[sources/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed|Asymptotic results and statistical procedures for time-changed Lévy processes sampled at hitting times]] (Mathieu Rosenbaum, Peter Tankov, 2010). Proves that a Lévy process, rescaled and observed at first hitting times of a shrinking symmetric barrier, converges to a stable process, yielding consistent estimators of the time change and the Blumenthal-Getoor jump index.
- [[sources/scheiber-2017-new-strategies-asset-classes-increased-performance|New Strategies and Asset Classes for Increased Performance]] (Matthias Scheiber, 2017). Thesis with three strands: a time-varying stock 'temperature' factor from transaction-time subordination, a Kalman-filter/agent-based copper price model, and a study of Chinese inventory financing versus the Theory of Storage.
- [[sources/silva-2005-applications-physics-finance-economics-returns-trading|Applications of Physics to Finance and Economics: Returns, Trading Activity and Income]] (A. Christian Silva, 2005). A physics-style empirical study of stock log-returns across time scales, using a Heston-model closed form and a trade-count subordination clock, plus a study of the evolving distribution of US personal income.
- [[sources/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate|Stochastic volatility of financial markets as the fluctuating rate of trading: an empirical study]] (A. Christian Silva, Victor M. Yakovenko, 2006). An empirical test of the subordination hypothesis, showing Intel stock return distributions are close to Gaussian per trade but exponential-tailed over fixed time, driven by the trade-count clock.
- [[sources/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility|Volatility Decomposition and Nonparametric Estimation of Spot Volatility of Models with Poisson Sampling under Market Microstructure Noise]] (Sophon Tunyavetchakit, 2016). Introduces a spot volatility estimator for high-frequency transaction data that factors clock-time volatility into tick-time volatility times trading intensity, improving convergence under microstructure noise.
- [[sources/turkoglu-2015-natural-time-crash-risk|Natural Time and Crash Risk]] (Ata Türkoğlu, 2015). A PhD thesis that recovers near-normal high-frequency stock returns via order-book-based subordination in transaction time, then reuses the same order-book variables to predict flash crashes and G10 currency crashes.
- [[sources/vliet-2026-information-arrival-stochastic-clock-intraday-trading|Information Arrival as a Stochastic Clock for Intraday Trading]] (Benjamin Van Vliet, 2026). Proposes a compound Hawkes stochastic-clock model in which trade feedback and squared news pressure drive trading intensity, giving news equal-magnitude activity effects but opposite price effects.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/long-memory|long memory]]
<!-- AUTHORED REGION END -->