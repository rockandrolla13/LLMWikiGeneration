---
authors:
- Ran Tao
content_hash: sha256:deb6143fa7cee0a0d4f18a9350402e811c270e8e769aea8d6075bc208c7def64
created: 2026-09-27 01:47:00+00:00
page_id: sources/tao-2018-directional-change-information-extraction-financial-market
page_type: source
publication_venue: University of Essex, PhD thesis (Centre for Computational Finance
  and Economic Agents)
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/high-frequency-trading
- concepts/stylized-facts
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:97bc293f1c2d6c7109de864ac6a5dec51c1f44421726fcf94de97f8d02d32c97
source_path: markdown_output/tao-2018-directional-change-information-extraction-financial-market.md
source_type: paper
tags:
- directional-change
- intrinsic-time
- event-based-sampling
- fx-markets
- commodity-futures
- market-profiling
- volatility-measurement
- phd-thesis
- clock-intrinsic
- asset-multi
- harvest-relevant
title: Using Directional Change for Information Extraction in Financial Market Data
updated: '2026-09-27T01:47:00Z'
uuid: 14365cbb-bbfd-5e7c-b79f-9dece33878e3
year: 2018
---

<!-- AUTHORED REGION START -->
# Using Directional Change for Information Extraction in Financial Market Data

## Summary

The thesis asks whether sampling prices by threshold-triggered directional change (DC), rather than at fixed calendar intervals, can reveal market information that standard time series analysis misses. It defines DC events (upturns and downturns confirmed once price moves by a fixed percentage threshold theta) and the overshoot period that follows each confirmed event, then proposes a vocabulary of indicators for summarizing a single market and metrics for comparing two markets under this framework.

Two programs are built to operationalize the framework: TR1 computes per-trend indicators (frequency, overshoot magnitude, trend duration, scale of price movement, a coastline measure of cumulative potential profit, a time-adjusted return, and up/down-trend asymmetry measures) and produces a DC profile from a price series. TR2 takes two DC profiles built with the same threshold and computes six bounded distance metrics covering price-change magnitude, timing and their asymmetries. Both tools are applied to minute-by-minute currency and commodity data from 2011 to 2015, to FTSE 100 equity tick data from two 2014/2015 snapshots, and to multi-year FX data spanning 2009 to 2016.

The empirical work finds that energy commodities (oil, gas) show far larger DC coastlines than currency pairs, indicating more potential profit and volatility under this framework, while metal commodities (gold, copper) track currency-market dynamics more closely than energy commodities do. It also shows that DC-based coastlines capture markedly more potential profit than time-series coastlines computed over the same period and sample size, and that pairs of markets can look very similar under DC metrics while looking very different under ordinary time-series volatility, or vice versa.

The contribution is presented as a general, reusable DC vocabulary (indicators plus metrics) that is complementary to, not a replacement for, time series analysis: it captures volatility, potential profit, and up/down-trend asymmetry from an event-driven, intrinsic-time clock, and gives a bounded, quantitative way to compare DC profiles across markets or time periods.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are recorded only when price moves by a fixed percentage threshold theta from the last confirmed extreme price, alternating between upturn and downturn directional-change events; each confirmed event is followed by an overshoot period that lasts until the next threshold-triggered event. A smaller sub-threshold is optionally used to detect extra directional-change events inside each larger trend. There is no single fixed prediction horizon; instead, trend-completion time (T) and time-adjusted return (RDC) are themselves reported as indicators, and cross-market or cross-period comparisons are built from repeated DC profiles (e.g. quarterly or seasonal windows) rather than a single forecast horizon.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Five currency pairs (AUD/USD, GBP/USD, EUR/USD, CHF/USD, JPY/USD), four commodities against USD (gold, oil, copper, natural gas), and four FTSE 100 equities (AstraZeneca/AZN, BT Group/BT, HSBC Holdings/HSBA, Marks & Spencer/MKS); worked examples also use USD/CNY and EUR/USD.
- **Venue:** not stated (data supplied by Thomson Reuters and Kibot; no specific exchange or trading platform named)
- **Period:** Primary currency/commodity analysis: minute-by-minute open prices from 2011 to 2015. Illustrative examples: EUR/USD second-by-second data from October 2009; USD/AUD, USD/JPY and USD/CHF minute data spanning 2009 to 2016; AZN/BT/HSBA/MKS tick data from September 2014 and February 2015.
- **Granularity:** Minute-by-minute open prices for the main currency/commodity study; second-by-second and tick-level data for the illustrative FX and equity examples.

## Features and Measures

- **NDC (Number of directional change events).** Total count of DC events over a profiled period, used as a measure of the frequency or volatility of DC events.
- **OSVEXT (Overshoot value at extreme points).** The price distance from the theoretical directional-change confirmation point to the next extreme point, normalized by the threshold, measuring how far price overshoots beyond confirmation.
- **TMV (Total price movements value at extreme points).** The normalized price distance between two consecutive DC extreme points, measuring the scale of price change in each trend.
- **T / TDC (time for completion of a trend).** The physical time elapsed between two consecutive directional-change extreme points.
- **CDC (time-independent coastline).** The sum of the absolute TMV values over a profiling period, representing the maximum possible profit captured by DC sampling.
- **RDC (time-adjusted return of DC).** The ratio of TMV to trend duration T, giving a return-per-unit-time measure for each DC trend.
- **AT and AR (up/down trend asymmetry).** Bounded [-1,1] measures of the difference between uptrends and downtrends in, respectively, trend duration (AT) and time-adjusted return (AR).
- **Sub-NDC and USVEXT_s.** Sub-threshold indicators counting the number and magnitude of smaller directional-change events that occur inside each larger DC trend.
- **DC metrics (DP1, DP2, DT, DTA, DR, DRA).** Six bounded distance measures (after taking absolute value, between 0 and 1) comparing two DC profiles on majority price change, extreme price change, trend timing, timing asymmetry, time-adjusted return and return asymmetry.

## Method

DC events and the overshoot period that follows them are defined from a user-chosen percentage threshold theta, giving an event-driven, data-led clock instead of a fixed-time clock. Chapter 3 defines ten single-market DC indicators and the program TR1, which reads a time-stamped price file and outputs a DC-Data file plus a Profile Summary File of these indicators. Chapter 4 defines six DC metrics and the program TR2, which reads two DC-Data files built with the same threshold and outputs their pairwise distance on each metric, bounding all metrics between -1 and 1 (reported as absolute values, 0 to 1, in the empirical chapters).

Performance and usefulness are judged qualitatively and by comparison rather than by a predictive backtest: DC indicators/metrics are computed on real currency, commodity and equity data and contrasted against matched time-series statistics computed on the same underlying data (same sample size or same period), to show where DC surfaces information (volatility, potential profit, trend asymmetry) that time-series measures do not.

## Results

- An EUR/USD example spanning October 2009 recorded 43 directional-change events under a 0.4% threshold, with a price-curve coastline of 77.42177, implying about 30.9687% of potential profit over the month.
- Across nine currency and commodity assets profiled from 2011 to 2015, natural gas had the longest coastline at 2862.18%, more than 19 times the shortest coastline of 150.07% recorded for GBP/USD.
- Comparing USD/AUD and USD/JPY DC profiles, the time-interval asymmetry metric DTA reached 0.914524269, the largest of the six metrics tested, indicating a strong difference in how long up-trends and down-trends last between the two currencies.
- For AstraZeneca (AZN) share prices in February 2015, the DC-based coastline was 305%, over six times the 49% coastline obtained from a matched time-series sample covering the same tick data.
- The median time to complete a trend was 88.44 minutes for HSBC in February 2015, over four times the 19.7-minute median recorded for AZN in the same month.
- In the same AZN February 2015 sample, the mean directional-change time-adjusted return was 2.22%, compared with a 0.36% mean absolute return computed from the matched time-series sample.
- Gold and copper showed the smallest DC-metric distances to the five currency markets, while natural gas showed the largest, especially against GBP/USD, suggesting metal commodities track currency-market dynamics more closely than energy commodities do.
- The thesis defines ten DC indicators (including NDC, OSVEXT, TMV, T, CDC and RDC) and six DC metrics (DP1, DP2, DT, DTA, DR, DRA), all bounded between 0 and 1 in the reported comparisons, as a reusable vocabulary for profiling and comparing markets under an event-driven clock.

## Limitations

- The empirical comparisons cover only five currency pairs, four commodities and four FTSE 100 equities, over 2009-2016 (currencies/commodities mainly 2011-2015); broader asset coverage is not tested.
- The choice of threshold and sub-threshold is set by the researcher and materially affects results; the thesis notes Sub-NDC and USVEXT_s become uninformative once the threshold used is very small.
- Reader note: the thesis is a descriptive profiling and comparison exercise; it does not test an explicit trading strategy or report out-of-sample forecasting accuracy for the DC indicators or metrics.
- Reader note: as a single-author PhD thesis relying on data supplied by Thomson Reuters and Kibot, no independent replication of the empirical results is reported within the extracted sections.
- No bond or fixed-income instrument is included in the empirical study; coverage is limited to FX, commodity futures and single-name equities.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/directional-change|Directional Change]]

## Citation

Ran Tao (2018). Using Directional Change for Information Extraction in Financial Market Data. University of Essex, PhD thesis (Centre for Computational Finance and Economic Agents).

Text ingested: `markdown_output/tao-2018-directional-change-information-extraction-financial-market.md`, converted from `raw/ofi-event-clock/tao-2018-directional-change-information-extraction-financial-market.pdf`.

Coverage of this summary: Read in full: abstract, Chapter 1 (introduction), Chapter 2 (background and DC definitions), Chapter 3 (DC indicators, TR1, equity example), Chapter 4 (DC metrics, TR2, FX example), Chapter 5 (single-market results), the introduction and closing summary of Chapter 6 (profile comparisons), Chapter 7 (conclusions, contributions, future work), and the reference list; skimmed the table of contents and lists of figures/tables/algorithms; did not fully read the detailed numeric appendix tables (Appendix 8.1-8.15) or every subsection of Chapter 6.

Known problems with the input: The markdown conversion replaced inline equation images with placeholder text ('picture... intentionally omitted'), so several indicator and metric formulas (e.g. OSVEXT, TMV, DP1-DRA) are described in prose from surrounding text rather than read directly from the rendered equations; OCR introduced minor artifacts (stray characters, duplicated table cells, split words) in places; content was still interpretable from context.
<!-- AUTHORED REGION END -->