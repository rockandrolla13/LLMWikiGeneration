---
authors:
- Luca Berardi
- Maurizio Serva
content_hash: sha256:592a786580b2c8f22064b742fdebbf7bd4c10f9493fa0b08aa63a3b83bb957f6
created: 2026-09-27 01:47:00+00:00
page_id: sources/berardi-2005-time-foreign-exchange-markets
page_type: source
related:
- concepts/sampling-clocks
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/autocorrelation-time-series
- concepts/stochastic-time-change
revision_id: 1
schema_version: 2
source_hash: sha256:35ac75633e4c28bf724babd681b6fb1ed7bf96d9d8e9add67a918271f42f56e6
source_path: markdown_output/berardi-2005-time-foreign-exchange-markets.md
source_type: paper
tags:
- business-time
- calendar-time
- foreign-exchange
- tick-data
- clock-choice
- high-frequency-data
- clock-compares
- asset-fx
- harvest-relevant
title: Time and foreign exchange markets
updated: '2026-09-27T01:47:00Z'
uuid: 0170d3fa-377e-554e-a202-ec9347dc38a9
year: 2005
---

<!-- AUTHORED REGION START -->
# Time and foreign exchange markets

## Summary

The paper asks whether high-frequency foreign exchange price dynamics are better described by a calendar-time model, in which prices are continuous-time random processes sampled at random moments, or a business-time model, in which time is simply the ordinal sequence of successive quotes and randomness enters only through prices, not through the timing of quotes.

To distinguish the two, the authors build two competing return series from a year of DEM/USD quotes: one that sums a fixed number of consecutive quote-to-quote returns (a fixed business-time lag) while only keeping cases whose total elapsed calendar time falls near a chosen value, and one that instead sums consecutive returns until a fixed amount of calendar time has elapsed regardless of how many quotes that took. Comparing the variance and empirical probability density of returns computed the two ways lets them test the calendar-time hypothesis (variance and density depend only on elapsed calendar time) against the business-time hypothesis (variance and density depend on the number of quotes, not on elapsed calendar time).

The evidence favors the business-time hypothesis: when the number of quotes is held fixed, return variance stays roughly constant as calendar time lag changes, but when calendar time is held fixed, variance grows with the number of quotes; return probability densities computed with a fixed quote count look similar across different calendar-time spans, whereas densities computed with a fixed calendar-time span but a varying quote count are visibly fatter-tailed. What is new is a direct statistical comparison of the two clock hypotheses on tick-level FX quote data, arguing that the pace of trading activity, not elapsed wall-clock time, is the more natural independent variable for modeling FX price dynamics.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper explicitly tests two competing clocks against each other: calendar time, the continuous elapsed wall-clock lag between quotes, versus business time, a discrete clock equal to the ordinal count of successive quote arrivals (the business-time lag m counts consecutive quotes). Two return series are constructed from tick quotes: one retains sums of a fixed number m of consecutive returns whose total elapsed calendar time falls within a window around a chosen lag, and the other sums consecutive returns until a chosen calendar-time lag has elapsed regardless of the number of quotes involved. There is no forecasting horizon; the comparison is a descriptive/hypothesis-testing exercise on the variance and density of realized returns rather than a prediction of future price moves.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** DEM/USD (USD/DM) exchange rate, mid-price of bid and ask quotes
- **Venue:** Reuters EFX pages, quote data supplied by Olsen & Associates
- **Period:** January to December 1998
- **Granularity:** Tick-by-tick bid/ask quotes, with a minimum inter-quote lag of 2 seconds

## Features and Measures

- **Business time lag (m).** A discrete clock defined by the count of consecutive quote arrivals; the business-time lag m is the number of consecutive quotes summed into a return.
- **Calendar time lag variance estimator v(Delta, m).** The sample variance of returns formed by summing m consecutive quote-to-quote returns, retaining only those whose total elapsed calendar time falls within a window around a chosen lag Delta; used to test whether variance depends on Delta (calendar hypothesis) or is roughly constant once m is fixed (business hypothesis).
- **Calendar-time-only variance estimator v(Delta).** The sample variance of returns accumulated by summing consecutive quote-to-quote returns until the elapsed calendar time reaches a chosen lag Delta, regardless of how many quotes that required; used to test whether variance grows linearly with Delta.

## Method

The authors split the two competing hypotheses formally: under the calendar-time hypothesis (H1), returns over a calendar lag Delta have a variance that grows linearly with Delta and is insensitive to the number of quotes counted in that interval; under the business-time hypothesis (H2), returns over a fixed number of quotes m have a variance that grows with m but is roughly insensitive to how much calendar time that took. Using mid-price quotes for DEM/USD over 1998, they construct the two return series described above and estimate their variances (via linear and constant curve fits) and empirical probability density functions for chosen values of the calendar lag and the quote-count lag, then compare which pattern (linear-in-Delta/flat-in-m, versus flat-in-Delta/linear-in-m) actually holds in the data. No formal significance testing, forecasting model, or backtest is used; the method is descriptive curve fitting and pdf comparison.

## Results

- Holding the business-time lag fixed at m = 40, the variance estimator v(Delta, m) is roughly constant across calendar lags Delta (constant fit of about 4.83E-7), while the calendar-time-only estimator v(Delta) grows linearly with Delta (linear fit with slope about 6.16E-10 and intercept about 8.26E-8).
- Holding the calendar lag fixed at Delta = 1000 (plus or minus 50), the variance estimator v(Delta, m) grows as the business-time lag m increases, consistent with the business-time hypothesis rather than the calendar-time hypothesis.
- The minimum lag between two consecutive quotes in the dataset is 2 seconds, so the two return series exactly coincide when Delta = 2 seconds and m = 1.
- For Delta = 100 seconds, the return probability density for m = 1 is close to the Delta = 2 second density, while the density for Delta = 100 seconds with m left free is visibly fatter-tailed, contradicting the equality predicted under the calendar-time hypothesis.
- The full dataset covers January to December 1998 and contains 1,620,843 recorded DEM/USD quote entries in the EFX system.

## Limitations

- The authors state they neglect possible autocorrelation between successive returns and between successive quote lags, treating any such effect as a second-order correction.
- Only one currency pair (DEM/USD) and one calendar year (1998) are examined.
- The authors note their results do not rule out a continuous-time (calendar) model entirely, only that it would require correlation between the quote-arrival process and the price process to fit the data.
- Reader note: no confidence intervals or significance tests are reported for the linear versus constant variance fits.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]

## Citation

Luca Berardi, Maurizio Serva (2005). Time and foreign exchange markets.

DOI: 10.1016/j.physa.2005.01.049

Text ingested: `markdown_output/berardi-2005-time-foreign-exchange-markets.md`, converted from `raw/ofi-event-clock/berardi-2005-time-foreign-exchange-markets.pdf`.

Coverage of this summary: Read the entire converted markdown file, including abstract, introduction, both time-model sections, the statistical estimators section, the data analysis and conclusions.

Known problems with the input: The paper does not print an explicit publication year anywhere in the converted text (only the 1998 data period); year taken from job file metadata (year_hint); Venue is not stated in the converted text; Most equations in the paper were replaced by 'picture... intentionally omitted' placeholders during conversion, so the exact algebraic forms of Eq. (1)-(11) could not be verified directly from the text, only inferred from the surrounding prose.
<!-- AUTHORED REGION END -->