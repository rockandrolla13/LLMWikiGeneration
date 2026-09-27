---
authors:
- Monira Essa Aloud
content_hash: sha256:e285b391a6cde2b91b83e415ac143c4bed97e812235580ddf3e7ce6cb92e7b05
created: 2026-09-27 01:47:00+00:00
page_id: sources/aloud-2016-time-series-analysis-indicators-under-directional
page_type: source
publication_venue: International Journal of Economics and Financial Issues, Vol. 6,
  Issue 1, 2016, pp. 55-64
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:7bbadc0290e9305dc7b8abc2a051e6c40469a40203514645f9b422f7dccae2e3
source_path: markdown_output/aloud-2016-time-series-analysis-indicators-under-directional.md
source_type: paper
tags:
- directional-change
- intrinsic-time
- saudi-stock-market
- high-frequency-data
- price-curve-coastline
- overshoot
- time-series-indicators
- clock-intrinsic
- asset-equity
- harvest-relevant
title: 'Time Series Analysis Indicators under Directional Changes: The Case of Saudi
  Stock Market'
updated: '2026-09-27T01:47:00Z'
uuid: 15963494-bf07-51e8-ac41-75f6ab5f62ed
year: 2016
---

<!-- AUTHORED REGION START -->
# Time Series Analysis Indicators under Directional Changes: The Case of Saudi Stock Market

## Summary

The paper asks whether an event-based intrinsic-time framework, directional changes (DC), can give more informative time series analysis indicators for financial markets than the usual physical fixed-time-interval analysis (daily or hourly closing prices). It uses the DC framework, in which a fixed percentage threshold dissects a price series into alternating DC events and overshoot (OS) events, and proposes a set of new indicators for profiling a price series under this framework: NDC (number of DC events), NOS (number of OS events), OSM (average overshoot magnitude), TT (average trend time), and PCC (price curve coastline, the cumulative price distance travelled).

These indicators are applied empirically to two groups of Saudi Stock Market (SSM) indices: Banks and Financial Services (SAMBA, SABB, RAJHI) and Telecommunication and Information Technology (STC, ZAIN), covering December 1, 2014 to May 25, 2015, with tick-level bid and ask price data acquired via Bloomberg DataStream. Each indicator is computed per index at two fixed DC thresholds, 3% and 9%, and the results are compared across indices and thresholds; no forecasting model or trading strategy is estimated or backtested.

Across both thresholds, the overshoot magnitude (OSM) for downtrends exceeded that for uptrends for every index tested, and the price curve coastline (PCC) grew as the threshold increased, for example SABB's PCC was 7.60% at a 3% threshold versus 22.63% at a 9% threshold. The paper also reports that the number of DC events fell as the threshold rose (172 DC events for SABB at 3% versus 86 at 9%, in the discussion text), and that average trend time (TT) varied sharply by index, with RAJHI's average trend time about twice that of SAMBA and about half that of SABB at the 9% threshold. The paper also points to an 8.91% intraday price drop in the SAMBA index that a daily or hourly fixed-interval view would have missed entirely.

What is new is not the DC/intrinsic-time concept itself, which the paper attributes to prior FX-market work by Guillaume et al. and Glattfelder et al., but a proposed catalogue of summary indicators (NDC, NOS, OSM, TT, PCC) for profiling any price series under this framework, together with its first application here to Saudi equity indices rather than FX data.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are directional-change (DC) events defined by a fixed percentage price threshold, with results reported at 3% and 9% thresholds: the mid-price (bid plus ask, divided by two) is tracked until it moves by at least the threshold from the last local extreme, confirming a DC event, which is followed by an overshoot (OS) event lasting until the next opposite DC event. The paper does not forecast a fixed horizon ahead; instead it computes summary indicators (counts and magnitudes of DC and OS events, average trend time, and cumulative price-curve length) per index and per threshold over the whole sample period, rather than making point predictions.

## Data

- **Asset class:** Equities
- **Instruments:** SAMBA (Saudi American Bank), SABB (Saudi British Bank), RAJHI (Al Rajhi Bank), STC (Saudi Telecom Company), ZAIN (Zain Mobile Telecommunications Company)
- **Venue:** Saudi Stock Market (SSM); tick data acquired via Bloomberg DataStream
- **Period:** December 1, 2014 to May 25, 2015
- **Granularity:** tick data (time-stamped bid and ask price records)

## Features and Measures

- **NDC (number of directional-change events).** Count of upturn and downturn DC events of a given threshold magnitude occurring over a defined period.
- **NOS (number of overshoot events).** Count of upturn and downturn overshoot (OS) events of a given threshold magnitude occurring over a defined period.
- **OSM (overshoot magnitude).** Average size of the overshoot event, measured as the price distance between the DC event confirmation point and the next price extreme, for a given threshold.
- **TT (trend time).** Average physical time taken to complete a full price trend, from the start price extreme to the end price extreme of a DC-plus-OS run, for a given threshold.
- **PCC (price curve coastline).** Cumulative price distance travelled by the series, summed across all DC and OS trend legs at a given threshold; used as a proxy for the profit potential of trading at that threshold.

## Method

The paper is empirical and descriptive rather than model-based: it applies the pre-existing directional-change (DC) event framework, a fixed threshold lambda applied to the mid-price, to dissect each index's price series into alternating DC and overshoot (OS) events, then computes five proposed summary indicators, NDC, NOS, OSM, TT and PCC, separately per index and per threshold. Two threshold magnitudes are used throughout, 3% and 9%.

No forecasting model, regression, or trading strategy is estimated or backtested; performance is not judged by predictive accuracy or trading return. Instead, the indicators are compared descriptively across the five indices and the two thresholds, and against physical fixed-time-interval analysis (daily and hourly closing prices), to argue that DC-based indicators reveal patterns, such as asymmetric overshoot magnitude between uptrends and downtrends, and large intraday moves like an 8.91% price drop, that fixed-interval sampling misses.

## Results

- For all five indices and both thresholds, the average overshoot magnitude (OSM) was higher for downtrends than for uptrends, interpreted as downtrends carrying more potential profit and less risk for arbitrage.
- The price curve coastline (PCC) grew as the DC threshold increased: for SABB, PCC was 7.60% at a 3% threshold versus 22.63% at a 9% threshold.
- The discussion text reports that the number of DC events fell as the threshold increased: 172 DC events for SABB at a 3% threshold versus 86 DC events at a 9% threshold; these figures do not match the NDC values printed in the paper's own Tables 1 and 3 for SABB (39 and 157).
- At the 9% threshold, average trend time (TT) differed sharply by index: RAJHI's average trend time was about twice that of SAMBA and about half that of SABB.
- At the 9% threshold, average PCC was 6.80% (SAMBA), 22.63% (SABB) and 23.61% (RAJHI) for the banking indices, and 18.62% (STC) and 7.62% (ZAIN) for the telecom indices.
- A daily/hourly fixed-time-interval view was shown to miss a large intraday price move: an 8.91% price drop within a single hour on the SAMBA index was not reflected in that day's daily or hourly returns.
- The paper concludes the DC indicators have a consistent hierarchical structure suitable for multi-scale profiling of price series, and proposes them as tools for future volatility, risk-management, forecasting and automated-trading work, without testing any such application here.

## Limitations

- Only two threshold magnitudes (3% and 9%) and five Saudi stock indices over about six months (December 1, 2014 to May 25, 2015) are examined.
- No forecasting model or trading strategy is built or tested; the indicators are proposed and profiled descriptively only.
- Reader note: the paper states two different NDC counts for SABB (86 and 172 DC events in the discussion text) that do not match the NDC values printed in its own Tables 1 and 3 (39 and 157); this internal inconsistency was not resolved in the text.
- Reader note: single-market, single-country study (Saudi Stock Market) with no out-of-sample or cross-market validation of the proposed indicators.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/directional-change|Directional Change]]

## Citation

Monira Essa Aloud (2016). Time Series Analysis Indicators under Directional Changes: The Case of Saudi Stock Market. International Journal of Economics and Financial Issues, Vol. 6, Issue 1, 2016, pp. 55-64.

Text ingested: `markdown_output/aloud-2016-time-series-analysis-indicators-under-directional.md`, converted from `raw/ofi-event-clock/aloud-2016-time-series-analysis-indicators-under-directional.pdf`.

Coverage of this summary: Read the entire paper (under): abstract, introduction, related works, dataset description, the DC framework sections, the DC indicators definitions, results, discussion, and conclusion.

Known problems with the input: The discussion text gives SABB DC-event counts of 86 (at 9% threshold) and 172 (at 3% threshold) that contradict the NDC values printed in the paper's own Tables 1 and 3 for SABB (39 and 157); this contradiction is in the source and is noted rather than resolved.
<!-- AUTHORED REGION END -->