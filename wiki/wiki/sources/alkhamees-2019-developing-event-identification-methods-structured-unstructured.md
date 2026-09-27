---
authors:
- Nora Alkhamees
content_hash: sha256:d965f110585098d619b81e4e1412bbe75ab6455816384ae212454c72c9f6201e
created: 2026-09-27 01:47:00+00:00
page_id: sources/alkhamees-2019-developing-event-identification-methods-structured-unstructured
page_type: source
publication_venue: University of Essex
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/high-frequency-trading
- concepts/backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:78bf796cbd639db42b77b85dba3d8d1e55174316e1ecaf85baf3ec798a53088d
source_path: markdown_output/alkhamees-2019-developing-event-identification-methods-structured-unstructured.md
source_type: paper
tags:
- directional-change
- event-detection
- dynamic-threshold
- trading-strategy
- twitter
- frequent-pattern-mining
- ftse-100
- high-frequency-data
- clock-intrinsic
- asset-equity
- harvest-relevant
title: Developing event identification methods for structured and unstructured data
  streams
updated: '2026-09-27T01:47:00Z'
uuid: e2e638ba-db1b-5051-8c91-17f90f75dc79
year: 2019
---

<!-- AUTHORED REGION START -->
# Developing event identification methods for structured and unstructured data streams

## Summary

The thesis asks how to detect meaningful 'events' - significant price transitions in a high-frequency financial price stream, and emerging topics in a social-media text stream - when the fixed, a-priori thresholds and support values conventionally used by existing methods do not adapt to how the volume and pace of the underlying stream changes over time, and whether events detected in one stream relate to events detected in the other.

For the price stream, the author extends the Directional Change (DC) framework, which marks a price 'event' once price moves by a threshold amount from the last confirmed high or low, by replacing the fixed threshold with one recomputed each trading day from the price move already made in the current run, the previous day's open-to-close change, and the overnight change, combined with weights and a decision rule (built from a J48 decision tree) for which components to include on a given day. This dynamic threshold is then built into a trading strategy, the Dynamic Threshold-Trading Strategy (DT-TS), which chooses a trend-following or a contrarian trading rule depending on whether the prior day's or overnight move is judged extreme. For the text stream, a Frequent Pattern Mining (FPM) topic-detection method is extended with a support threshold recomputed for every daily window-batch from the average and median term frequency in that batch, rather than a single fixed support value used across the whole stream. Both methods are tested on FTSE 100 minute-by-minute and daily prices and on Twitter streams collected around the UK 2015 general election and the 2015 Greece crisis, with detected events checked against BBC News headlines as an external indicator of whether an event was 'true'. Finally, Pearson correlation and Granger causality are used to test whether events detected in the price stream and events or volume in the text stream are related.

The dynamic DC threshold detects price events that line up with same-day published news more consistently than any of several fixed thresholds tried, and the resulting DT-TS trading strategy is more profitable than the same strategy run with fixed thresholds and than Trend Following, Contrarian and Backlash Agent baselines, in both a training period and a held-out testing period; it also performs better on the higher-frequency minute-by-minute stream than on the daily stream. The dynamic-support FPM method likewise outperforms a fixed-support benchmark topic-detection method on precision and on a combined precision/recall measure, with similar recall. Cross-referencing the two streams through Pearson correlation and Granger causality finds only weak and inconsistent links between price-stream events and text-stream events or tweet volume.

The contribution is a general recipe for replacing a fixed, a-priori threshold or support value in two established event-detection methods, DC for price streams and FPM for text streams, with a value recomputed for each new unit of the stream from recent history, so that event detection adapts to how active or quiet the stream currently is; this is combined with a DC-based dynamic-threshold trading strategy evaluated across two data frequencies, and with an attempt to link financial-market and social-media event streams together, which the thesis finds only weak evidence for.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Price observations are sampled in Directional Change intrinsic time: starting from the last confirmed high or low price, a new event (an upturn or a downturn) is marked once the current price moves away from that extreme by at least a threshold percentage, and the interval until the next such event is an 'overshoot' period. The thesis's core contribution replaces DC's usual fixed, a-priori threshold with one recomputed once per trading day from the percentage move already made since the last extreme, the previous day's open-to-close change, and the overnight (previous close to current open) change, each weighted, with a decision tree choosing which components to include for that day. The DT-TS trading strategy defines its holding horizon the same way: a trading rule opened at a new high/low update within an overshoot period is closed when the next DC event is confirmed, so the holding period is one DC run rather than a fixed clock duration.

## Data

- **Asset class:** Equities
- **Instruments:** FTSE 100 index price level (minute-by-minute and daily open/high/low/close); Twitter text-post streams collected around the UK 2015 General Election (GE 2015) and the 2015 Greece sovereign-debt crisis
- **Venue:** London Stock Exchange index prices sourced from Reuters Thomson One; Twitter, via the Twitter API
- **Period:** FTSE 100 minute-by-minute and daily prices spanning July 2015 to October 2016, with an additional sample from November 2016 to May 2017 used to train a threshold decision tree; separate Twitter streams collected around the UK General Election 2015 and the Greece Crisis 2015, cross-referenced against FTSE 100 prices from March to May 2015
- **Granularity:** Minute-by-minute and daily (open, high, low, close) FTSE 100 index prices; Twitter text posts grouped into daily window-batches

## Features and Measures

- **Dynamic Directional Change threshold.** A daily threshold for the DC event-detection rule, computed from the percentage price change since the last confirmed high or low, the previous day's open-to-close change, and the overnight close-to-open change, weighted and combined depending on whether a decision tree judges the previous day's or overnight move to have been extreme.
- **Dynamic FPM support value.** A per-window-batch minimum-frequency (support) threshold for retaining terms in Frequent Pattern Mining, computed as the average term frequency in that day's text-post batch multiplied by the median term frequency, doubled for batches a logistic regression model classifies as small.
- **DT-TS trading rule.** A trading rule triggered whenever the running high or low price updates during a Directional Change overshoot period, choosing a trend-following or a contrarian action depending on whether the previous day's or overnight price change was judged extreme by a trained threshold.

## Method

For the price stream, the DC algorithm detects upturn/downturn events from a threshold; the thesis's dynamic-threshold algorithm replaces the fixed threshold with a daily value built from three percentage-change components (the move since the last extreme, the previous day's move, and the overnight move), with the choice of which components to sum decided by a J48/C4.5 decision tree trained on a labelled dataset of FTSE 100 days marked as 'news event' days or not from BBC headlines, and with component weights chosen by testing a grid of values against detected/false/missed event counts. The DT-TS trading strategy layers trading rules on top of this: buy or sell decisions trigger at each new high/low within an overshoot period, choosing a contrarian action if the previous day's or overnight move exceeded trained threshold values (set via a second decision tree) and a trend-following action otherwise; positions use all available cash or shares and transaction costs are not modelled.

For the text stream, an FP-Growth frequent-pattern-mining algorithm identifies daily topics from a bag-of-words representation of each day's tweets, with the minimum support threshold computed per window-batch from that batch's average and median term frequency (doubled for batches a logistic regression model classifies as small), rather than one fixed support value for the whole stream. Detected topics and DC price events are both validated against whether a matching BBC News headline appeared on the same day, using precision, recall and F-measure against this news-based ground truth, and the text-stream method is additionally compared against a fixed-support benchmark topic-detection method.

Trading-strategy performance is judged by total net profit, profit factor, percent profitable, maximum drawdown and average trade net profit, compared across the DT-TS, fixed-threshold (FT-TS), Trend Following, Contrarian Trading and Backlash Agent strategies, on both a training period and a held-out testing period, and separately on minute-by-minute versus daily FTSE 100 streams. Cross-stream relationships between DC-detected price events and FPM-detected topics or Twitter volume are tested with Pearson correlation and Granger causality at multiple day lags using the Eviews statistical package.

## Results

- Using the dynamic daily threshold, the DC approach detected 20 price events on the FTSE 100 minute-by-minute stream from July 2015 to February 2016, all matching a same-day published news headline (precision 1, recall 0.9), while fixed thresholds tested over the same period scored as low as precision 0.3.
- On the minute-by-minute FTSE 100 stream, the DT-TS trading strategy reached 65% total net profit in the training period and 47% in the held-out testing period, outperforming the same strategy run with fixed thresholds (up to 62% in training and 35% in testing) and the Trend Following, Contrarian and Backlash Agent baselines in both periods.
- On the daily FTSE 100 stream over the same period, DT-TS reached 37% profit versus 65% on the minute-by-minute stream, indicating the dynamic-threshold trading strategy performs better at higher observation frequency.
- Using a daily prices stream, a threshold-definition approach based only on current-day prices missed more than 75% of the news-confirmed price events, while the best of the six daily-threshold variants tested still missed more than 35% of events.
- For the Twitter topic-detection method using the dynamic support value, more than 88% of identified topics matched a same-day published news article, with precision roughly three times higher than a fixed-support benchmark method and a similarly higher F-measure at comparable recall.
- Cross-referencing the FTSE 100 price stream with the GE 2015 Twitter stream via Granger causality found only a weak link: financial-stream events Granger-caused text-stream events at 2-3 day lags, and daily price changes Granger-caused daily tweet volume at 1-4 day lags, but tweet volume did not clearly Granger-cause price events, and the Greece Crisis period showed no comparable price-to-tweet-volume link.
- Pearson correlation between events detected in the FTSE 100 price stream and events or tweet volume detected in the Twitter stream was generally low across both the GE 2015 and Greece Crisis periods, and no clear cross-stream relationship could be established.

## Limitations

- The DC dynamic-threshold and DT-TS methods rely on a well-defined daily open/close price structure, so as written they are not directly applicable to markets that trade continuously without daily opening and closing prices, such as the Foreign Exchange market; the author names this as a direction for future work.
- Ground truth for a 'true' event is same-day publication of a BBC News headline about the FTSE 100, a proxy that may miss events not covered by major news outlets, particularly for individual stocks rather than a headline index.
- Trading-strategy results ignore transaction costs and assume the trader can deploy all available cash or shares on every trade.
- Reader note: all empirical work uses a single equity index (FTSE 100) and two Twitter event studies (UK GE 2015, Greece Crisis 2015) over roughly 2015-2017, so the profitability and correlation findings are not shown to generalise to other markets, assets, or time periods.
- Reader note: several threshold-tuning choices (the previous-day/overnight weighting values and the 'something happened' decision-tree cutoffs) were fit on the same FTSE 100 data later used for evaluation, which is a form of in-sample calibration the thesis does not treat as a separate validation concern.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/backtesting|backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Nora Alkhamees (2019). Developing event identification methods for structured and unstructured data streams. University of Essex.

Text ingested: `markdown_output/alkhamees-2019-developing-event-identification-methods-structured-unstructured.md`, converted from `raw/ofi-event-clock/alkhamees-2019-developing-event-identification-methods-structured-unstructured.pdf`.

Coverage of this summary: Read the abstract, introduction (Chapter 1), the literature review sections on stream reasoning, frequent pattern mining, the Directional Change approach and Twitter-market studies (Chapter 2), the text-stream event detection method and its dynamic support definition (Chapter 3, sections 3.1-3.2 and the chapter summary), the Directional Change dynamic-threshold method and its FTSE 100 experiments in full (Chapter 4), the DT-TS trading strategy, its training/testing experiments and performance metrics in full (Chapter 5), the variable-frequency comparison in full (Chapter 6), the cross-stream Pearson correlation and Granger causality analysis (Chapter 7, introduction, method and summary), and the conclusions and future work (Chapter 8). Did not read the appendices (tweet collection screenshots, gold-standard lists, and detailed news-article listings) or the glossary/bibliography.

Known problems with the input: This is a long PhD thesis; per the instructions for long documents, some detailed intermediate tables in Chapter 3's experimental section and Chapter 7's correlation section were skimmed for their stated conclusions rather than read cell by cell, and the appendices were not read; The markdown conversion replaces mathematical display equations with '==> picture... omitted <==' placeholders, so the exact algebraic definitions of the DC threshold equations, the six daily-stream threshold approaches, and the trading/Granger-causality equations could not be transcribed and are described here only qualitatively; The thesis itself states inconsistent numeric values for the DT-TS decision thresholds previous_v and overnight_v: the Chapter 5 body text gives 0.7% and 0.8%, while the Chapter 5 summary gives 0.07 and 0.08 for the same quantities; these values were therefore omitted from this summary rather than guessed at.
<!-- AUTHORED REGION END -->