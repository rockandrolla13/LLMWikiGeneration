---
authors:
- László Gillemot
- J. Doyne Farmer
- Fabrizio Lillo
content_hash: sha256:fbf9cb2a77a03eb8f9c4fa3c598769c132448fb62054d7e85fc96ae4c4a9888a
created: 2026-09-27 01:47:00+00:00
page_id: sources/gillemot-2006-there-s-more-volatility-than-volume
page_type: source
related:
- concepts/sampling-clocks
- concepts/long-memory
- concepts/stylized-facts
- concepts/autocorrelation-time-series
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/volume-clock
- concepts/trade-clock
- concepts/stochastic-time-change
- entities/fabrizio-lillo
revision_id: 1
schema_version: 2
source_hash: sha256:e5e0138df2eb25191a876cbe837bd5869a40589d078d9a95a3a4003f299f2a83
source_path: markdown_output/gillemot-2006-there-s-more-volatility-than-volume.md
source_type: paper
tags:
- volatility-clustering
- heavy-tails
- transaction-clock
- volume-clock
- long-memory
- hurst-exponent
- subordination
- clock-compares
- asset-equity
- harvest-relevant
title: There’s more to volatility than volume
updated: '2026-09-27T01:47:00Z'
uuid: 56c949dc-3acd-5637-a339-df3413e2c499
year: 2006
---

<!-- AUTHORED REGION START -->
# There’s more to volatility than volume

## Summary

The paper tests the widely held view, going back to the subordinated-process model of Mandelbrot and Taylor and Clark, that clustered volatility and heavy-tailed returns are mainly caused by fluctuations in trading volume or the number of transactions. Using tick-by-tick data from the New York and London Stock Exchanges, the authors ask how much of real-time volatility's clustering and long memory survive once volume or transaction count is held fixed.

The approach resamples prices in transaction time (fixed number of trades per interval) and in volume time (fixed traded volume per interval), and compares the resulting volatility series to real-time volatility. As a control, the authors build shuffled surrogate series that match the transaction count or volume realized in each real-time interval but randomly reorder the underlying transaction returns, destroying temporal structure while preserving the count or volume. They compare correlations with real-time volatility, compare full return distributions under each clock, and estimate Hurst exponents via detrended fluctuation analysis to test long memory. They also directly test the normalization procedure of Ane and Geman and the power-law price-impact theory of Gabaix et al.

Across all three data sets, clustered volatility survives strongly in transaction time and in volume time, and correlates far more closely with real-time volatility than the shuffled controls do; Hurst exponents computed in transaction and volume time track the real-time Hurst exponent closely, while the shuffled versions are systematically lower. Distributions of returns conditioned on constant volume or transaction count remain heavy-tailed and close to the unconditional distribution, contradicting the Ane-Geman normalization result and undercutting the Gabaix et al. account of how volume fluctuations generate heavy-tailed returns.

What is new is a direct, cross-market test (using much larger samples than earlier single-market studies) of two specific rival subordination theories, concluding that the ordering and size of individual non-zero price changes, tied to the shifting balance of liquidity supply and demand, is the dominant proximate driver of both clustered volatility and heavy tails, with transaction frequency and volume playing only a supporting role.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Real-time volatility uses fixed calendar intervals (15 minutes in most comparisons). Transaction-time volatility samples every K transactions (K=24 in the paper's illustrative example, averaging about 15 minutes per interval). Volume-time volatility samples the smallest interval whose cumulative traded volume exceeds a fixed threshold chosen so the number of volume-time intervals roughly matches the number of real-time intervals. Shuffled surrogate series match either the transaction count or the volume realized in each real-time interval but randomly reorder individual transaction returns, isolating the effect of event ordering from the effect of event count or size. There is no forecasting horizon; the object of study is the contemporaneous correlation and autocorrelation (long-memory) structure of volatility under each clock, not prediction.

## Data

- **Asset class:** Equities
- **Instruments:** 20 high-capitalization stocks in each of three samples: NYSE1 (AHP, AIG, BMY, CHV, DD, GE, GTE, HWP, IBM, JNJ, KO, MO, MOB, MRK, PEP, PFE, PG, T, WMT, XON), NYSE2 (AIG, BA, BMY, DD, DIS, G, GE, IBM, JNJ, KO, LLY, MO, MRK, MWD, PEP, PFE, PG, T, WMT, XOM), and LSE (AZN, REED, HSBA, LLOY, ULVR, RTR, PRU, BSY, RIO, ANL, PSON, TSCO, AVZ, BLT, SBRY, CNA, RB., BASS, LGEN, ISYS)
- **Venue:** New York Stock Exchange (NYSE) and London Stock Exchange (LSE)
- **Period:** NYSE1: January 1, 1995 to June 23, 1997 (626 trading days). NYSE2: January 29, 2001 to December 31, 2003 (734 trading days). LSE: May 2000 to December 2002 (675 trading days)
- **Granularity:** Tick-by-tick transaction and quote data; about 7 million transactions in NYSE1, 36 million in NYSE2, and 5.7 million in the LSE sample

## Features and Measures

- **transaction time.** a stochastic clock that advances by one unit per transaction, used to resample the price series so each interval contains a fixed number of trades
- **volume time.** a stochastic clock that advances with cumulative traded volume, used to resample the price series so each interval contains approximately a fixed amount of traded volume
- **shuffled transaction/volume real-time volatility.** a surrogate volatility series built by randomly reordering individual transaction returns while preserving the transaction count or volume realized in each real-time interval, used to isolate the effect of ordering from the effect of count or volume
- **Hurst exponent via detrended fluctuation analysis.** a measure of long memory in a time series, estimated by regressing the log root-mean-square deviation of an integrated series from a fitted trend against the log window size, used to compare persistence of volatility across real time, transaction time, volume time, and their shuffled counterparts

## Method

For each stock, the authors build real-time, transaction-time, volume-time, and shuffled versions of the volatility series, then linearly interpolate the discretely sampled series to a common continuous-time basis so correlations between clocks can be computed. They summarize these correlations, and their ratios to the corresponding shuffled-series correlations, across all stocks in each of the three data sets. Long memory is measured by estimating a Hurst exponent for each series using detrended fluctuation analysis, and cross-sectional regressions of alternative-clock Hurst exponents against the real-time Hurst exponent are run for each data set to test consistency. Separately, the paper reproduces Ane and Geman's transaction-count normalization test with a Bera-Jarque normality test, and fits Gabaix et al.'s power-law relation between squared returns and volume by least squares to compare predicted versus empirical return distributions.

## Results

- Correlation between real-time and transaction-time volatility ranged from 35% to 49% across the three data sets, compared with only 6% to 17% for the corresponding shuffled transaction real-time volatility.
- The ratio of average correlation with volume-time volatility to average correlation with shuffled volume real-time volatility ranged from 1.4 to 3.6 across the three data sets, showing volume time tracks real-time volatility far more closely than its shuffled counterpart.
- For the LSE stock Astrazeneca, the Hurst exponent of real-time volatility and of transaction-time volatility were both about 0.70 (plus or minus 0.07), while the shuffled transaction real-time volatility had a lower Hurst exponent of about 0.59 (plus or minus 0.03).
- Across a cross-sectional regression of alternative Hurst exponents on the real-time Hurst exponent for each stock, the slope was positive for transaction-time and volume-time volatility in all but one of six data-set/clock combinations, while four of six shuffled-volatility cases had negative slopes.
- Cumulative distributions of returns conditioned on constant volume or constant transaction count were close to the unconditional real-time return distribution and remained heavy-tailed in almost every stock and data set tested.
- Reproducing the Bera-Jarque normality test on transaction-count-normalized returns for Cisco, Intel and Procter & Gamble rejected normality in every case, with p-values below 10^-23, contradicting Ane and Geman's claimed normalization result.
- Fitting the power-law relation between squared return and volume proposed by Gabaix et al. gave a volume exponent of about 1.2 and a proportionality constant of about 0.61, but the resulting predicted return distribution had a much thinner tail than the empirical distribution.
- Out of 60 stock/data-set combinations examined for long memory, only one showed a higher Hurst exponent for the shuffled volume series than for the true volume-time series, and only one showed the analogous result for transaction time.

## Limitations

- The authors note that standard error bars for the Hurst exponent assume an IID normal process and are likely too optimistic given the long memory present in the data; the only known correction (the variance plot method) is described as unreliable and tedious, so a cross-sectional test across many stocks is used instead.
- The reconstruction of Ane and Geman's normalization procedure is the authors' own best interpretation of an unclear original method, and is only checked against the same two stocks used in that earlier study plus one additional stock.
- All three data sets are restricted to 20 heavily traded, high-capitalization stocks; smaller or less liquid names are not tested.
- Reader note: causal language throughout is explicitly limited to correlation; the authors state they assume any nonlinearity between the variables is small enough that low correlation implies a lack of strong causal connection.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/long-memory|long memory]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[entities/fabrizio-lillo|Fabrizio Lillo]]

## Citation

László Gillemot, J. Doyne Farmer, Fabrizio Lillo (2006). There’s more to volatility than volume.

DOI: 10.1080/14697680600835688

Text ingested: `markdown_output/gillemot-2006-there-s-more-volatility-than-volume.md`, converted from `raw/ofi-event-clock/gillemot-2006-there-s-more-volatility-than-volume.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, the data and market-structure section, all subsections on volatility under alternative time clocks, the distributional-properties section (including the comparisons to Ane and Geman and to Gabaix et al.), the long-memory section, the conclusions, and the reference list.

Known problems with the input: The PDF-to-markdown conversion garbled diacritics in the first author's name (rendered as 'L´aszl´o Gillemot'); reconstructed here as 'László Gillemot' based on the mangled character pattern; No journal name, working-paper series, or identifier is printed anywhere in the extracted text, so venue is left blank; year from file metadata; Several equations (transaction-time and volume-time definitions, the Gabaix et al. price-impact formula) are rendered as omitted pictures in the markdown, so their exact algebraic form is described only in prose, not reproduced as equations.
<!-- AUTHORED REGION END -->