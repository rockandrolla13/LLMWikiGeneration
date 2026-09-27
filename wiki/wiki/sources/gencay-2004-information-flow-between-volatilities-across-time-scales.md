---
authors:
- Ramazan Gençay
- Faruk Selçuk
- Brandon Whitcher
content_hash: sha256:fd271dd35ab75b13b6f6126b0f2fefcc599e87679cc2dd46da54fa0102036b29
created: 2026-09-27 01:47:00+00:00
page_id: sources/gencay-2004-information-flow-between-volatilities-across-time-scales
page_type: source
publication_venue: Munich Personal RePEc Archive (MPRA Paper No. 10355)
related:
- concepts/autocorrelation-time-series
- concepts/long-memory
- concepts/realized-variance
- concepts/stylized-facts
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:42ddb21b7867186b36117b33f28cd89bc44919a9171e16f40504c8d3d06bc8c0
source_path: markdown_output/gencay-2004-information-flow-between-volatilities-across-time-scales.md
source_type: paper
tags:
- wavelets
- volatility-regimes
- hidden-markov-model
- multiresolution-analysis
- fx-volatility
- realized-volatility
- time-scales
- stylized-facts
- clock-calendar
- asset-multi
- added-by-hand
title: Information Flow Between Volatilities Across Time Scales
updated: '2026-09-27T01:47:00Z'
uuid: 44aa153f-285c-599d-890b-0ae9407a7939
year: 2004
---

<!-- AUTHORED REGION START -->
# Information Flow Between Volatilities Across Time Scales

## Summary

The paper asks whether volatility observed at one time horizon tells us anything about volatility at another, shorter or longer, horizon, and specifically whether that relationship is symmetric between high- and low-volatility states.

The authors define coarse and fine realized volatility from high-frequency squared returns, use the discrete wavelet transform (a Haar/D(4)/LA(8) family of filters, with LA(8) chosen for the main analysis) to decompose volatility into dyadic time scales, and fit a two-state Gaussian-mixture wavelet hidden Markov tree (HMT) model whose scale-dependent transition probabilities describe how a high- or low-volatility regime at one scale propagates to the next finer scale. The model is applied to 5-min USD-Deutsche Mark FX returns and to Dow Jones Industrial Average index returns, the latter spanning the September 11, 2001 shock.

In both markets, low-volatility states are very likely to be followed by low-volatility states at shorter horizons across almost every scale, while high-volatility states are far less likely to persist down to shorter horizons, and this asymmetry is more pronounced in the DJIA than in the FX series. Applied to specific episodes, the model shows the 1992 European currency crisis as an extended high-volatility regime at coarse scales that shrinks to only a few days at the finest intraday scale, while the September 11 shock to DJIA volatility appears comparatively short-lived.

The contribution is the introduction and estimation of this 'asymmetric vertical dependence' property of volatility across time horizons, complementing the previously known horizontal-dependence properties (clustering, long memory), together with a wavelet-based realized-volatility construction that the authors show reproduces the autocorrelation structure of conventionally aggregated realized volatility.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Returns are sampled at fixed 5-min intervals (USD-DEM FX) or fixed 5-min/1-hour aggregated intervals (DJIA); squared 5-min returns define realized volatility, and a discrete wavelet transform decomposes this volatility series into dyadic scales corresponding to fixed time horizons from minutes up to weeks. The wavelet hidden Markov tree model classifies each scale's coefficient into a high- or low-volatility state and models how a state at a longer (coarser) horizon propagates down to shorter (finer) horizons, rather than predicting a single fixed horizon ahead.

## Data

- **Asset class:** Several asset classes
- **Instruments:** USD-Deutsche Mark (USD-DEM) foreign exchange rate; Dow Jones Industrial Average (DJIA) index
- **Venue:** Not stated for the FX interbank data (sourced from Olsen & Associates); New York Stock Exchange for the DJIA constituents
- **Period:** USD-DEM: 5-min FX returns spanning 1987 to 1998 (901,152 observations over 3,129 days), sourced from Olsen & Associates. The main wavelet HMT model is estimated on the first 524,288 of these observations (1987-1993); a second check re-estimates the model on the last 524,288 observations (1992-1998). DJIA: 5-min index returns from 1999 to 2002 (75,446 observations, 955 trading days), aggregated to 6287 hourly volatilities, with the wavelet HMT fit on the last 4096 hourly observations (2000-2002).
- **Granularity:** 5-min returns aggregated via wavelet multiresolution analysis to dyadic time scales, plus 1-hour aggregated returns for the DJIA wavelet HMT estimation

## Features and Measures

- **coarse and fine volatility (vc, vf).** Two aggregation levels of squared returns, synchronized in time, used to represent the views and actions of long-term (coarse) versus short-term (fine) traders.
- **actual realized volatility.** The sum of squared high-frequency returns over a fixed number of periods (a chosen sampling rate), the standard way of aggregating volatility to a coarser, fixed time horizon.
- **wavelet realized volatility.** The wavelet 'smooth' component from a multiresolution analysis of squared 5-min returns, constructed to match a given sampling rate without discretely re-aggregating the raw series.
- **wavelet hidden Markov tree (HMT) state.** A hidden discrete regime (high or low volatility) attached to each wavelet coefficient at each scale, modelled as a zero-mean Gaussian mixture and linked vertically across scales by scale-dependent transition probabilities.

## Method

The paper builds on the discrete wavelet transform (DWT), introduced via Haar and Daubechies (D(4), LA(8)) wavelet and scaling filters and computed efficiently with Mallat's pyramid algorithm, to produce a multiresolution analysis (MRA) that additively decomposes a time series into scale-specific 'detail' and 'smooth' components.

Realized volatility is defined from squared high-frequency returns aggregated over a chosen sampling rate; a 'wavelet realized volatility' is instead built from the wavelet smooth at the matching scale, and the two are compared via their sample autocorrelation functions.

A wavelet hidden Markov tree (HMT) model, following Crouse, Nowak and Baraniuk (1998), represents each wavelet coefficient as a two-state, zero-mean Gaussian mixture, links states vertically across scales through scale-dependent transition matrices, and is estimated by an EM-type upward-downward algorithm; the Viterbi algorithm then classifies each coefficient into a high- or low-volatility state.

## Results

- Wavelet realized volatility is nearly indistinguishable from actual realized volatility in autocorrelation at 20-minute, hourly and daily USD-DEM sampling rates, except at the first lag.
- In the USD-DEM model, low-to-low volatility transition probabilities are close to one at almost every scale (e.g. 0.96 from the 4-7 day to the 2-4 day horizon, 0.99 from the 3-5 hour to the 1-3 hour horizon).
- USD-DEM high-to-high volatility persistence is markedly weaker and scale-dependent (0.78 and 0.55 for the same two transitions), with the probability of switching from high to low volatility around 0.50 at horizons of about 12 hours or less.
- For the DJIA, low-to-low transition probabilities are all at least 0.90 (e.g. 0.97 from the 8-16 hour to 4-8 hour scale, 0.90 from the 2-4 week to 1-2 week scale).
- DJIA high-to-high persistence is weaker than in the FX case (0.25 and 0.17 for the same two transitions), and the probability of switching from high to low volatility reaches about 0.82 at the 2-4 week to 1-2 week transition.
- The 1992 European currency-crisis period appears as an extended high-volatility regime at coarse (roughly 7-30 day) scales but only a few days of high volatility at the finest (10-20 minute) scale.
- The DJIA volatility shock around September 11, 2001 is estimated to have been comparatively short-lived relative to other volatility bursts in the sample.
- The USD-DEM analysis uses 901,152 5-min return observations (3,129 days) from 1987 to 1998, and the DJIA analysis uses 75,446 5-min observations (955 trading days) aggregated to 6287 hourly volatilities, with the wavelet HMT fit on the last 4096 of these.

## Limitations

- The wavelet HMT as specified only allows dependence between scales, not within a scale, so within-scale volatility clustering is not modeled directly; the authors note within-scale hidden Markov chains as future work.
- The analysis relies on only two markets (USD-DEM FX and the DJIA equity index), so the claimed asymmetric vertical dependence is not demonstrated across a broader cross-section of assets.
- Reader note: the DJIA wavelet-HMT estimation truncates the data to the largest available dyadic sample size (4096 hourly observations), discarding earlier data rather than using the full sample.
- Reader note: the paper is from 2004 and compares against a limited alternative set (ARCH/GARCH and Markov-switching models), predating later realized-volatility and jump-based literature.

## Related

- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/long-memory|long memory]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Ramazan Gençay, Faruk Selçuk, Brandon Whitcher (2004). Information Flow Between Volatilities Across Time Scales. Munich Personal RePEc Archive (MPRA Paper No. 10355).

Text ingested: `markdown_output/gencay-2004-information-flow-between-volatilities-across-time-scales.md`, converted from `raw/ofi-event-clock/gencay-2004-information-flow-between-volatilities-across-time-scales.pdf`.

Coverage of this summary: Read the entire paper end-to-end: abstract, introduction, the wavelet methodology (Sections 2-3), the wavelet hidden Markov tree model (Section 4), the FX and DJIA applications (Section 5), the conclusions (Section 6), all footnotes, and the reference list.

Known problems with the input: Nearly all equations and several figures are converted as 'picture omitted' placeholders with garbled surrounding notation (mangled exponents and subscripts); prose describing these was used instead of the underlying formulas; OCR renders the authors' names without cedillas (e.g. 'Gen¸cay', 'Sel¸cuk'); the accented spellings Gençay and Selçuk are reconstructed from context.
<!-- AUTHORED REGION END -->