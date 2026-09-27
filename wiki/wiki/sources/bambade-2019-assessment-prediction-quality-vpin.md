---
authors:
- Antoine Bambade
- Kesheng Wu
content_hash: sha256:d0604187a7fda2a4133187694b92ac574d42e98884ca811fba8399f5dd62e962
created: 2026-09-27 01:47:00+00:00
page_id: sources/bambade-2019-assessment-prediction-quality-vpin
page_type: source
publication_venue: Advanced Analytics and Artificial Intelligence Applications (IntechOpen)
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/trade-classification
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/vpin
- concepts/bulk-volume-classification
- entities/kesheng-wu
revision_id: 1
schema_version: 2
source_hash: sha256:7d23a4f8b476f1aeba0151c1d2955c38a3f34c190cc9d48a9464d5aa215c03de
source_path: markdown_output/bambade-2019-assessment-prediction-quality-vpin.md
source_type: book
tags:
- vpin
- flash-crash
- order-flow-toxicity
- futures
- precision-recall
- volume-clock
- bulk-volume-classification
- clock-volume
- asset-futures
- harvest-core
title: An Assessment of the Prediction Quality of VPIN
updated: '2026-09-27T01:47:00Z'
uuid: fbb775eb-9f40-5a10-99e1-8aec6d6c199a
year: 2019
---

<!-- AUTHORED REGION START -->
# An Assessment of the Prediction Quality of VPIN

## Summary

The chapter asks whether VPIN, a volume-based measure of order flow toxicity introduced after the May 6, 2010 flash crash, actually has useful predictive power for such extreme events, or whether earlier claims about it were never properly quantified. The authors note that prior critics had raised doubts about VPIN's reliability but had not measured its prediction quality directly in terms of precision and recall.

To test this, the authors build their own empirical definition of a flash crash based on the maximum intermediate return (MIR) of a price series over a short rolling window, calibrated so that it captures the May 6, 2010 event. VPIN itself is recomputed from tick data using the standard bar/bucket construction: trades are grouped into fixed-size bars, bars into buckets, and buy/sell volume within each bar is estimated via bulk volume classification rather than by classifying individual trades. They then run a large grid search over bar-price convention (mean, median, first, last), the VPIN support window, the classifier used for bulk volume classification, the flash-crash amplitude threshold, the VPIN decision threshold, and the prediction window length, scoring each combination by precision and recall against the MIR-defined crash labels and against a naive classifier that predicts crashes at random.

The data set is 67 months of tick data (January 2007 to July 2012) for five of the most liquid futures contracts across asset classes, sourced from the vendor TickWrite. At the traditional VPIN decision threshold, the authors find that prediction quality for true, large flash-crash-scale events is weak and, for some contracts, no better than the naive classifier; VPIN performs noticeably better at flagging smaller-magnitude price swings than at flagging genuine flash-crash-sized moves, and results differ a lot by futures contract and by which bar-price convention is used.

The chapter's other contribution is a direct test of VPIN's known sensitivity to the point in the data set where computation begins: removing an increasing number of leading bars does shift the best-fit parameters and their precision/recall scores, confirming earlier critiques, but the authors find the size of that shift is modest, and that using the last-trade bar-price convention makes VPIN's local best parameters least sensitive to this starting-point effect.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Trades are grouped into fixed-size bars (a set number of successive trades), bars are grouped into buckets of m bars, and VPIN is computed as a rolling estimate of buy/sell volume imbalance over n successive buckets (the VPIN support), with buy/sell volume within each bar estimated via bulk volume classification rather than per-trade classification. A prediction is scored by checking, in a window of omega buckets before or after a VPIN threshold crossing, whether a matching MIR-defined flash-crash event occurs, so omega sets the prediction horizon in bucket units.

## Data

- **Asset class:** Futures
- **Instruments:** E-mini S&P 500 (ES), Euro FX (EC), light crude oil NYMEX (CL), Nasdaq 100 (NQ), and E-mini Dow Jones (YM) futures
- **Venue:** CME (ES, EC, NQ), NYMEX (CL), and CBOT (YM)
- **Period:** January 2007 to July 2012 (67 months)
- **Granularity:** tick-by-tick trade data (about 45.1 GB across five CSV files), sourced from the data vendor TickWrite

## Features and Measures

- **VPIN.** A volume-bucket-based estimate of the probability of informed trading, computed as the average absolute buy/sell volume imbalance across a rolling window of buckets, normalized to lie between 0 and 1.
- **Bulk volume classification (BVC).** A way of splitting a bar's total trading volume into estimated buy and sell volume using a cumulative distribution function (Student or normal) of standardized price changes, instead of classifying each individual trade.
- **Maximum intermediate return (MIR).** A statistic that captures the largest price swing within a short rolling time window, used here as the paper's own operational definition of a flash crash.
- **Bars and buckets (VPIN's volume clock).** The two-level volume-based sampling scheme underlying VPIN, where a bar is a fixed number of successive trades and a bucket is a fixed number of successive bars, replacing calendar-time sampling.

## Method

The authors treat VPIN's prediction quality as a classification problem: a VPIN threshold crossing is a true positive if a matching MIR-defined flash-crash event falls within a following or preceding window of omega buckets, and a false positive/negative otherwise. They perform a grid (deep) search over bar-price convention, the flash-crash amplitude threshold, VPIN support window length, classifier choice, prediction window omega, and the VPIN decision threshold, keeping the parameter combination that maximizes precision plus recall for each of the five futures contracts and each bar-price convention. Results are benchmarked against a naive classifier that flags a crash independently at random for each bucket, using the same grid of amplitude and window parameters. A separate sensitivity analysis reruns the same search after deleting the first 1000, 2000, or 3000 bars of each series, to quantify how much the optimal parameters and their precision/recall change.

## Results

- At the traditional VPIN decision threshold of 0.99, the best precision+recall score for E-mini S&P 500 (ES) futures was only 1.1908, with recall 0.9737 but precision just 0.2171.
- For Euro FX (EC) and light crude oil (CL) futures at the same threshold, VPIN reached much higher precision (0.9644 and 0.9045) with recall of 0.9080 and 0.9406, but a naive random classifier matched or beat VPIN's results on these two contracts.
- Raising the VPIN threshold as high as 0.99999 improved ES precision to 0.4677, but did not make VPIN consistently and uniformly better than the naive classifier across all five futures.
- Lowering the flash-crash amplitude threshold to about 1.5% (theta_MIR=0.015) with the last-bar-price convention raised ES recall to 0.9421 and precision to 0.9541, indicating VPIN discriminates smaller, more frequent price swings better than true flash-crash-scale moves.
- Erasing the first 1000 to 3000 bars of a series changed the local best precision+recall score by as much as 6.727% depending on which bar-price convention was used, confirming the previously reported sensitivity to the starting point of computation, though the authors judge the size of the effect to be modest.
- Of the four bar-price conventions tested (mean, median, first, last), last-bar pricing was the least sensitive to the starting-point effect on the local best parameters.

## Limitations

- Only one confirmed flash crash (May 6, 2010) exists in the sample, so precision and recall are ultimately scored against a single labeled ground-truth event plus the MIR-defined lower-amplitude analogues the authors construct around it.
- The volume-clock (bar/bucket) construction does not allow control over how long a bar or bucket takes to fill in calendar time, which the authors note forced them to use an approximate rule for capturing the 10-minute May 6, 2010 window.
- Reader note: the parameter grid and conclusions are calibrated to five specific futures contracts over 2007-2012 and may not generalize to other instruments, sampling frequencies, or crash episodes.
- Reader note: the study does not report out-of-sample validation of the tuned parameters on a separate period; the grid search and reported best precision/recall are evaluated on the same data set.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]
- [[entities/kesheng-wu|Kesheng Wu]]

## Citation

Antoine Bambade, Kesheng Wu (2019). An Assessment of the Prediction Quality of VPIN. Advanced Analytics and Artificial Intelligence Applications (IntechOpen).

DOI: 10.5772/intechopen.86532

Text ingested: `markdown_output/bambade-2019-assessment-prediction-quality-vpin.md`, converted from `raw/ofi-event-clock/bambade-2019-assessment-prediction-quality-vpin.pdf`.

Coverage of this summary: Read the full markdown text of the chapter, including the abstract, all numbered sections, all data and results tables, the appendix, and the reference list.

Known problems with the input: Several formula graphics (the PIN, VPIN, bulk-volume-classification, and MIR equations) are rendered as 'picture... intentionally omitted' placeholders in the markdown, so their exact mathematical form could not be verified from the text and is described here only qualitatively; Some inline symbols are OCR-garbled (e.g. 'thetaVPIN = 0:99' for 'thetaVPIN = 0.99'); numeric values used in this file were cross-checked against places where the digits render cleanly, such as the abstract and the data tables.
<!-- AUTHORED REGION END -->