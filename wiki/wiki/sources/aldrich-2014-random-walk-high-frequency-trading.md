---
authors:
- Eric M. Aldrich
- Indra Heckenbach
- Gregory Laughlin
content_hash: sha256:750a2c86f2c6c091450e79545ec8e8483b88f03be59178d4ae204b4ead5bd47e
created: 2026-09-27 01:47:00+00:00
page_id: sources/aldrich-2014-random-walk-high-frequency-trading
page_type: source
related:
- concepts/stochastic-time-change
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/market-microstructure
- concepts/autocorrelation-time-series
- concepts/long-memory
- concepts/trade-clock
revision_id: 1
schema_version: 2
source_hash: sha256:9e55f25db1174c9904a1282ecf6cc1d8fdffa451f00265788c664777862a9bc8
source_path: markdown_output/aldrich-2014-random-walk-high-frequency-trading.md
source_type: paper
tags:
- high-frequency-trading
- trade-time
- duration-model
- subordination
- e-mini-futures
- volatility-clustering
- fat-tails
- news-events
- clock-time-change
- asset-futures
- harvest-relevant
title: The Random Walk of High Frequency Trading
updated: '2026-09-27T01:47:00Z'
uuid: 35943ed4-ace7-5a60-8b80-4d8c8beb32ca
year: 2014
---

<!-- AUTHORED REGION START -->
# The Random Walk of High Frequency Trading

## Summary

The paper asks why high-frequency asset returns look fat-tailed and volatility-clustered even though a Gaussian random walk is the natural theoretical benchmark. Using millisecond tick data on the CME E-mini S&P 500 futures contract, the authors split observations into an 'active' subsample (trading in a window following pre-scheduled macroeconomic news announcements) and a 'passive' subsample (matched windows with no scheduled announcement), and compare returns measured in ordinary clock time against returns measured in trade time (a fixed count of transactions). They find that passive-period, trade-time returns are close to Gaussian, while clock-time returns and active-period returns keep heavy tails and volatility persistence.

To explain this, the authors build a hierarchical (subordinated) model: trade-time returns are drawn from a Gaussian distribution, and the number of trades executed within a clock-time interval is drawn from a duration model of inter-trade waiting times. They extend the Markov-Switching Multifractal Duration (MSMD) model of Chen, Diebold and Schorfheide by truncating it with an Exponential component fitted to the longest observed inter-trade duration, producing a Truncated MSMD (TMSMD) model. Trade-count distributions implied by TMSMD are combined with the trade-time Gaussian via Monte Carlo simulation to generate simulated clock-time returns, which are compared against the observed passive-period data using quantile plots, chi-squared goodness-of-fit tests, Kullback-Leibler divergence, autocorrelation functions, and Ljung-Box tests.

The main finding is that the TMSMD-Gaussian compound model reproduces both the fat tails and the volatility clustering of observed clock-time returns much more closely than either a simple compound Poisson (Exponential-duration) model or the untruncated MSMD model, even though none of the models is accepted by a formal chi-squared test given the size of the sample. The paper also documents that price changes in the E-mini lead corresponding price changes in the SPY ETF, consistent with price formation occurring mainly at the futures exchange, and separately estimates the light-speed-limited round-trip time between the Chicago futures venue and New Jersey equities venues.

What is new is the use of trade arrivals, rather than an ad hoc distributional assumption, as the sole mechanism generating fat tails and volatility clustering in clock time once news-driven periods are excluded, and the use of the fitted duration/volatility relationship to extrapolate how trading speed and physical distance between exchanges could bound systemic volatility.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

The model treats trade-time (returns sampled once every m transactions) as the base clock on which returns are Gaussian, and treats clock-time returns as the compound/subordinated object obtained by mixing that Gaussian with the distribution of the number of trades occurring in a fixed wall-clock interval. Trade counts are generated from a fitted inter-trade duration model (Exponential, MSMD, or the paper's Truncated MSMD). Both clock-time and trade-time returns are examined empirically across a range of intervals (250, 500, 1000, 5000/4000, 10000, 30000 ms and m = 1, 2, 4, 40, 400, 4000 trades), so the paper also explicitly compares behavior across clocks.

## Data

- **Asset class:** Futures
- **Instruments:** CME E-mini S&P 500 near-month futures contract (ticker ES); SPY ETF trades used for a lead-lag comparison
- **Venue:** Chicago Mercantile Exchange (CME) FIX historical files; SPY trades from NYSE TAQ Consolidated Market System data (NASDAQ, NYSE, NYSE Arca, BATS BZX, BATS BYX, EDGX, CBSX, NSX, CHX)
- **Period:** 18 May 2013 to 18 August 2013 (main estimation sample); 27 April 2010 to 17 August 2012, 577 trading sessions (out-of-sample volatility and price-formation analysis)
- **Granularity:** millisecond-stamped tick-by-tick trades; multiple trades within the same millisecond are aggregated into one transaction using the final in-force price

## Features and Measures

- **active/passive period split.** Trades are grouped into active windows (1000 seconds following a pre-scheduled macroeconomic news announcement, identified from the EconoDay calendar) and passive windows (the same time-of-day intervals on days without a scheduled announcement), to separate news-driven return behavior from ordinary quiescent trading.
- **trade-time return.** A return computed over a fixed number of transactions (m trades) rather than a fixed amount of wall-clock time, used to test whether subordinating returns by trade count restores Gaussianity.
- **Truncated Markov-Switching Multifractal Duration (TMSMD) model.** A modification of the MSMD inter-trade duration model that combines it with an independent Exponential distribution calibrated so its expected maximum matches the largest inter-trade duration observed in the sample, producing durations equal to the minimum of the two components.
- **compound TMSMD/Gaussian process.** A hierarchical model of clock-time returns in which the number of trades occurring in an interval is drawn from the TMSMD-implied counting distribution (via Monte Carlo simulation) and the corresponding return is the sum of that many independent draws from the trade-time Gaussian distribution.
- **median inter-trade duration vs. volatility relationship.** A mapping, built from simulating the compound TMSMD model at varying trade-arrival intensity, between the median inter-trade duration in a trading session and the annualized volatility implied by that trading rate, used to extrapolate volatility under faster trading conditions.

## Method

Component distributions are estimated separately and then combined. Trade-time returns for m = 1 are assumed i.i.d. Gaussian and estimated by sample mean and standard deviation. Inter-trade durations are estimated three ways: as an Exponential (equivalent to Poisson trade arrivals, estimated by maximum likelihood with parametric bootstrap standard errors), as an MSMD process (estimated by maximizing the likelihood via Hamilton's nonlinear filtering with a hill-climbing algorithm, searching over the number of latent multifractal components), and as the TMSMD process (the same MSMD estimates truncated by an Exponential whose scale is chosen numerically so its expected maximum equals the sample's longest observed duration).

Given the fitted component distributions, the authors Monte Carlo simulate the implied clock-time return distribution for each duration model at several clock-time intervals, since no closed-form density is available once the MSMD/TMSMD counting process is used. Simulated clock-time returns are discretized to the E-mini's minimum tick increment and compared against the empirical passive-period distribution.

Model fit is judged with quantile-quantile plots, chi-squared goodness-of-fit tests against the empirical return histogram, Kullback-Leibler divergence between simulated and empirical return distributions, sample autocorrelation functions of returns and squared returns, and Ljung-Box statistics on those autocorrelations, each computed across the same set of clock-time intervals.

## Results

- Passive-period trade-time returns closely match a Gaussian distribution in density, Q-Q, and autocorrelation comparisons, while active-period returns and all clock-time returns retain heavy tails.
- The main sample contains 6,832,305 aggregated transactions; the news-event subsample has 191,127 records from 43 announcement windows and the non-event subsample has 174,041 records from 54 matched windows.
- Chi-squared goodness-of-fit statistics for simulated clock-time returns are uniformly smaller for the TMSMD model than for the plain MSMD model, which in turn is uniformly smaller than for the Exponential/Poisson model, though all three are formally rejected at the 5% level.
- Kullback-Leibler divergence between simulated and empirical returns favors the TMSMD model at longer clock-time intervals (e.g. much lower divergence at 10000 ms and 30000 ms), while the plain Exponential model is closest at the shortest intervals (250 ms and 500 ms).
- The TMSMD model reproduces the slow-decaying autocorrelation of squared returns (volatility clustering) seen in the data far better than the Exponential model, which shows none.
- A composite lead-lag analysis of 14,078,656 price-changing E-mini trades shows the E-mini leading the SPY ETF: the ratio of cumulative positive-lag to negative-lag SPY price response is 6.26.
- The compound TMSMD model implies that an 8 ms inter-trade duration (the light-speed round-trip time between Chicago and New Jersey exchanges) corresponds to an annualized S&P 500 volatility of about 36 percent for k=5, rising to 45 percent or higher for k<=4.
- The estimated Poisson/Exponential trade-arrival intensity is gamma = 0.003326 per millisecond, and the fitted maximum-duration Exponential component of the TMSMD model has scale nu_max = 5866, calibrated against a longest observed inter-trade duration of 56315 ms.

## Limitations

- The compound model is only claimed to apply to quiescent, non-news trading periods; the authors state it is not tuned to describe returns during regimes of market stress.
- All three duration models (Exponential, MSMD, TMSMD) are formally rejected by the chi-squared goodness-of-fit test at the 5% level for every clock-time interval considered, given the very large sample size.
- The empirical analysis is confined to a single, exceptionally liquid instrument (the E-mini S&P 500 futures contract); the authors note the Gaussian trade-time result may be specific to this heavily traded asset.
- Reader note: the core estimation sample spans only three months (18 May-18 August 2013), which is short for fitting tail and long-memory-like duration behavior.
- Reader note: the volatility-extrapolation exercise in Section 6 relies on extending the fitted model outside the range of trading rates actually observed in-sample.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/long-memory|long memory]]
- [[concepts/trade-clock|Trade Clock]]

## Citation

Eric M. Aldrich, Indra Heckenbach, Gregory Laughlin (2014). The Random Walk of High Frequency Trading.

DOI: 10.48550/arxiv.1408.3650

Text ingested: `markdown_output/aldrich-2014-random-walk-high-frequency-trading.md`, converted from `raw/ofi-event-clock/aldrich-2014-random-walk-high-frequency-trading.pdf`.

Coverage of this summary: Read the full markdown file end to end, including abstract, data, empirical distribution, model, estimation/results, application, and conclusion sections; equation images were omitted by the converter and not used.

Known problems with the input: The PDF-to-markdown conversion replaces all equations and several figures with placeholder text ('picture... intentionally omitted'), so equation forms could not be verified beyond the surrounding prose; The author/affiliation block in the converted markdown is jumbled (names and department lines are interleaved out of column order); author order and affiliations were reconstructed from the footnote email markers rather than read directly in a clean list.
<!-- AUTHORED REGION END -->