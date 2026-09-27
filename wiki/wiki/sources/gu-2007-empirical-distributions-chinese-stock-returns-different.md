---
authors:
- Gao-Feng Gu
- Wei Chen
- Wei-Xing Zhou
content_hash: sha256:697ba0775d606c81f3dc31e0d009f60658bb45c34347c47a2917e2cc3031b49b
created: 2026-09-27 01:47:00+00:00
page_id: sources/gu-2007-empirical-distributions-chinese-stock-returns-different
page_type: source
publication_venue: Physica A (preprint)
related:
- concepts/sampling-clocks
- concepts/stylized-facts
- concepts/high-frequency-data
- concepts/limit-order-book
- concepts/event-clock
revision_id: 1
schema_version: 2
source_hash: sha256:d58e138725b1381ca103e7d1964f4b7ea59b81ec96be40c3b2e5d433c2d7f53c
source_path: markdown_output/gu-2007-empirical-distributions-chinese-stock-returns-different.md
source_type: paper
tags:
- chinese-stocks
- event-time
- clock-time
- power-law-tails
- inverse-cubic-law
- ultra-high-frequency-data
- student-distribution
- clock-compares
- asset-equity
- harvest-relevant
title: Empirical distributions of Chinese stock returns at different microscopic timescales
updated: '2026-09-27T01:47:00Z'
uuid: 0d9fd284-ceab-5a13-9ee3-6d7a15869ab0
year: 2018
---

<!-- AUTHORED REGION START -->
# Empirical distributions of Chinese stock returns at different microscopic timescales

## Summary

The paper's question is what probability distribution best describes very short-horizon stock returns, and whether that distribution changes depending on whether returns are sampled by counting trades (event time) or by fixed wall-clock intervals (clock time), and on how many trades or minutes are aggregated. It works from ultra-high-frequency, transaction-level limit order book data for 23 stocks traded on the Shenzhen Stock Exchange during 2003.

The approach defines the midprice from the best bid and best ask after each trade, then builds event-time returns as the log change in midprice over a fixed number of trades (1, 2, 4, 8, 16 or 32 trades) and clock-time returns as the log change in midprice over a fixed number of minutes (1 through 5 minutes). Each stock's returns are standardized by that stock's own mean and standard deviation before pooling all 23 stocks into one sample, and the pooled empirical density is fit with a Student distribution, whose degrees-of-freedom parameter doubles as a tail exponent; the positive and negative tails are also fit directly and separately as power laws from the empirical cumulative distribution.

The main finding is that single-trade event-time returns closely follow the inverse cubic law, with positive and negative tail exponents both near 3, while at every coarser sampling scale examined, whether measured in more trades or more minutes, the tails become thinner (the exponent rises) and the kurtosis falls as the scale grows; the positive tail exponent is consistently a bit larger than the negative one, matching the returns' positive skew.

What is new is doing this comparison at the individual-transaction level for a Chinese market, where prior Chinese studies had mostly used daily data; the paper positions its scale-dependent thinning of the tails as consistent with a turbulence-inspired variational picture in which return distributions move from power-law to more Gaussian-like as the sampling scale grows.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper explicitly builds and compares two clocks: an event-time (trade-count) clock, where the return over Delta-t is the log midprice change measured after every Delta-t trades for Delta-t = 1, 2, 4, 8, 16 or 32 trades, and a clock-time clock, where the return is the log midprice change over a fixed Delta-t of 1 to 5 minutes. Returns on each clock are standardized per stock (subtracting that stock's mean and dividing by its standard deviation) before being pooled across the 23 stocks, and the paper notes that the mapping between the two clocks is nonlinear because it depends on each stock's own trading frequency.

## Data

- **Asset class:** Equities
- **Instruments:** 23 individual stocks listed on the Shenzhen Stock Exchange
- **Venue:** Shenzhen Stock Exchange (SZSE)
- **Period:** the whole year 2003
- **Granularity:** Ultra-high-frequency, transaction-level limit order book data with timestamps accurate to 0.01 second; per-stock trade counts over the year range from under a hundred thousand to close to a million trades.

## Features and Measures

- **Standardized event-time return.** The logarithmic change in a stock's midprice over a fixed number of trades, standardized by that stock's own mean and standard deviation so returns from different stocks can be pooled.
- **Standardized clock-time return.** The logarithmic change in a stock's midprice over a fixed wall-clock interval (in minutes), standardized the same way as the event-time return.
- **Fitted Student density.** A Student distribution with a degrees-of-freedom (tail exponent), location and scale parameter, fit by nonlinear least squares to the pooled empirical return density; its tails asymptotically decay as a power law.
- **Empirical tail exponent.** A power-law exponent fit separately to the positive and negative tails of the empirical cumulative return distribution over an identified scaling range, used to check the inverse cubic law and its breakdown at coarser scales.

## Method

The midprice after each trade is defined from the prevailing best bid and best ask. Event-time returns are formed as the log midprice change measured every Delta-t trades, for Delta-t = 1, 2, 4, 8, 16 and 32 trades, using the transaction records of the 23 SZSE stocks in 2003; clock-time returns are formed the same way but over fixed Delta-t = 1 to 5 minute intervals. In both cases returns are standardized per stock and then pooled into one 23-stock ensemble.

For each Delta-t, the pooled empirical density is fit by nonlinear least squares to a Student distribution, and separately the empirical cumulative distribution's positive and negative tails are fit to power laws over an identified scaling range, giving two tail exponent estimates with standard errors. Performance and comparison across scales is judged by tracking how the fitted Student scale and degrees-of-freedom parameters, the separately estimated positive and negative tail exponents, and the sample kurtosis change as Delta-t increases, for both the event-time and clock-time versions of the return.

## Results

- At the single-trade event-time scale, the fitted tail exponents are 3.14 (plus or minus 0.02) for the positive tail and 3.00 (plus or minus 0.02) for the negative tail, consistent with the inverse cubic law; the corresponding Student density fit has degrees-of-freedom parameter 3.1 and scale 1.9.
- As the event-time aggregation scale grows from 1 to 32 trades, kurtosis falls from 34.21 to 13.62 while the tail exponents rise, reaching 4.11 (plus or minus 0.06) for the positive tail and 3.96 (plus or minus 0.07) for the negative tail at 32 trades.
- For clock-time returns, kurtosis stays roughly flat across 1 to 5 minute intervals (about 17.79 down to 17.24) even as the tail exponents still rise with Delta-t, from 3.48 (plus or minus 0.02) at 1 minute to 4.22 (plus or minus 0.07) at 5 minutes for the positive tail.
- In both the event-time and clock-time cases, the positive tail exponent is consistently larger than the negative tail exponent at a given scale, which the paper links to the returns' positive skewness.
- The inverse cubic law (tail exponent close to 3) is found to hold only for the single-trade event-time return; every coarser scale examined, in trades or in minutes, decays faster than the inverse cubic law.
- The paper notes that clock-time returns aggregated over a few minutes show kurtosis comparable to event-time returns aggregated over roughly 8 to 16 trades, suggesting the two clocks give broadly similar distributional behavior once matched on this basis.

## Limitations

- Reader note: the sample covers a single calendar year (2003) on a single exchange (Shenzhen), so the reported tail exponents may not generalize to other periods or markets.
- Reader note: the paper is a purely descriptive statistical characterization of the return distribution; it does not test a trading signal or predictive model.
- The paper itself notes that whether the sign of the difference between the positive and negative tail exponents is universal across stock markets is unresolved, pointing to mixed evidence from other markets.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/event-clock|Event Clock]]

## Citation

Gao-Feng Gu, Wei Chen, Wei-Xing Zhou (2018). Empirical distributions of Chinese stock returns at different microscopic timescales. Physica A (preprint).

DOI: 10.1016/j.physa.2007.10.012

Text ingested: `markdown_output/gu-2007-empirical-distributions-chinese-stock-returns-different.md`, converted from `raw/ofi-event-clock/gu-2007-empirical-distributions-chinese-stock-returns-different.pdf`.

Coverage of this summary: Read the entire converted markdown, from abstract through the conclusion, tables and references.

Known problems with the input: The document's only printed date is a preprint submission line reading '29 October 2018' (for Physica A); this is used as the year field per the extraction rule of using the year printed on this version, even though the references and data (Shenzhen Stock Exchange data from 2003, latest cited references from 2007) indicate the underlying research and original writing predate 2018, matching the job file's year_hint of 2007.
<!-- AUTHORED REGION END -->