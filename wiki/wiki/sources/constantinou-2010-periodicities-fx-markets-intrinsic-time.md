---
authors:
- Wing Lon Ng
- Iacopo Giampaoli
- Nick Constantinou
content_hash: sha256:a0a530a72b7ce751f131640339043c9bb0a259fdc4d90b69117927bc8dc536fc
created: 2026-09-27 01:47:00+00:00
page_id: sources/constantinou-2010-periodicities-fx-markets-intrinsic-time
page_type: source
publication_venue: Essex Business School
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/autocorrelation-time-series
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:8d12968751be9d63d82259cbf567600d6a1dec3bcacddfd6a0b14c82c16f2ac6
source_path: markdown_output/constantinou-2010-periodicities-fx-markets-intrinsic-time.md
source_type: paper
tags:
- fx
- intrinsic-time
- directional-change
- spectral-analysis
- lomb-scargle
- high-frequency-data
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Periodicities of FX Markets in Intrinsic Time
updated: '2026-09-27T01:47:00Z'
uuid: 04471395-6ee5-5f45-bab1-1dbdd0e0d89b
year: 2010
---

<!-- AUTHORED REGION START -->
# Periodicities of FX Markets in Intrinsic Time

## Summary

The paper asks whether foreign exchange tick data, when sampled in an event-based 'intrinsic time' defined by directional-change events, show periodic structure beyond the diurnal patterns already known from calendar-time studies. Intrinsic time advances only when the price moves away from the last local high or low by more than a fixed threshold, producing a series that is irregularly spaced in calendar time.

The approach pairs this directional-change sampling with the Lomb-Scargle Fourier Transform (LSFT), which estimates a spectral density function directly from unevenly-spaced data without resampling or interpolating onto a regular grid, avoiding distortions those steps can cause. Before the spectral step, the authors first estimate, by ordinary least squares, an empirical scaling law linking the average directional-change duration to the size of the threshold, and compare it against a geometric Brownian motion benchmark.

Using tick data for 6 FX pairs from November 1, 2008 to January 31, 2009, the directional-change duration data fit the power-law scaling relationship closely (R-squared above 0.99 for every pair, e.g. 0.9996 for AUD-HKD) and differ from the GBM benchmark at the 99% confidence level. The Lomb-Scargle spectral density of the directional-change event series shows statistically significant peaks concentrated at low frequencies; as the directional-change threshold rises, these peaks shift to still lower frequencies, moving from periods above 8 hours at a small threshold to periods above 100 hours and then 340 hours as the threshold grows to 0.75% and 1.5% for EUR-JPY.

What is new is the joint use of an event-based (intrinsic-time) sampling scheme with the Lomb-Scargle method, which the authors argue avoids the information loss of forcing ultra-high-frequency data onto a regular time grid before spectral estimation, and the finding that periodicities detected at a larger threshold reappear in the spectra of the same series filtered at smaller thresholds, a consequence of the underlying scaling law.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are recorded only at directional-change events: starting from the last local high or low, once price moves against that extreme by more than a fixed threshold, a new event is logged, and the elapsed time since the previous event (the directional-change duration) forms an irregularly-spaced 'intrinsic time' index. The filtering is repeated across threshold sizes from 10bp to 200bp per currency pair, and the resulting event series is studied in the frequency domain rather than used to forecast a single horizon; the object being characterized is the periodicity present in the spectral density of each threshold's directional-change series.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** AUD-HKD, AUD-JPY, EUR-JPY, EUR-USD, HKD-JPY, USD-JPY tick data
- **Venue:** not stated (tick data supplied by OFT per the acknowledgements)
- **Period:** November 1, 2008 to January 31, 2009
- **Granularity:** tick-by-tick (ultra-high-frequency), filtered into an irregularly-spaced directional-change event series

## Features and Measures

- **Directional-change event (intrinsic time).** A price move exceeding a fixed threshold away from the last local extreme, used to define an event-based, irregularly-spaced time index instead of clock time.
- **Directional-change duration scaling law.** A power-law relationship between the average elapsed time between directional-change events and the size of the threshold used to define them, estimated by OLS on the log-linearized relationship across threshold sizes from 10bp to 200bp per currency pair.
- **Lomb-Scargle spectral density function (SDF).** An estimate of a time series' power spectrum computed directly from unevenly-spaced observations by least-squares fitting of sinusoids, together with a false-alarm probability for judging whether a spectral peak is statistically significant.

## Method

The directional-change duration scaling law (average duration versus threshold size, log-linearized) is estimated by ordinary least squares for each currency pair and threshold, and compared against the same regression fit to simulated geometric Brownian motion paths whose drift and volatility are estimated from the data and averaged over repeated simulations. The Lomb-Scargle Fourier Transform is then applied to the irregularly-spaced directional-change event series (the mid-price values at the cutoff points between directional-change and overshoot sections) to estimate a normalized spectral density function for each threshold and currency pair. Statistical significance of spectral peaks is assessed via a false-alarm probability derived from the exponential distribution of the Lomb-Scargle periodogram, evaluated at the 95% confidence level.

## Results

- Directional-change duration follows a power-law relationship with threshold size across all 6 currency pairs, with R-squared above 0.99 in each case (e.g. AUD-HKD R-squared = 0.9996).
- The estimated power-law slopes are statistically different from a geometric Brownian motion benchmark at the 99% level for all currency pairs.
- At small thresholds, the spectral density of the mid-price directional-change series shows significant peaks concentrated at low frequencies, corresponding to periods longer than 8 hours.
- As the directional-change threshold size increases, the significant spectral peaks shift toward still lower frequencies, e.g. beyond 100 hours at a 0.75% threshold and beyond 340 hours at a 1.5% threshold for EUR-JPY.
- Periodicities found at a higher threshold reappear in the spectral density of the same series filtered at lower thresholds, illustrated for EUR-JPY across the 50bp, 75bp and 150bp thresholds.
- Similar periodic patterns, and their shift to lower frequencies as the threshold rises, are observed for the other currency pairs, e.g. AUD-HKD.

## Limitations

- Reader note: The study covers a single 3-month window (November 2008 to January 2009) across only six currency pairs, so it is unclear whether the periodicities generalize to other periods or regimes.
- The paper characterizes spectral periodicities descriptively; it does not test the predictive value of these periodicities for future price moves.
- Reader note: significance of spectral peaks is assessed only at a single false-alarm confidence level (95%), with no discussion of correcting for testing many frequencies and thresholds simultaneously.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/directional-change|Directional Change]]

## Citation

Wing Lon Ng, Iacopo Giampaoli, Nick Constantinou (2010). Periodicities of FX Markets in Intrinsic Time. Essex Business School.

Text ingested: `markdown_output/constantinou-2010-periodicities-fx-markets-intrinsic-time.md`, converted from `raw/ofi-event-clock/constantinou-2010-periodicities-fx-markets-intrinsic-time.pdf`.

Coverage of this summary: Read the entire paper markdown: introduction, methodology sections 2.1-2.2, empirical data and results (section 3, tables 1-3, figures 4-16), and the concluding remarks and reference list.

Known problems with the input: Several equations are rendered as '==> picture... omitted <==' placeholders in the markdown, so their exact mathematical form could not be verified beyond the surrounding prose.
<!-- AUTHORED REGION END -->