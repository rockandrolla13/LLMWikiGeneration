---
authors:
- Kesheng Wu
- E. Wes Bethel
- Ming Gu
- David Leinweber
- Oliver Ruebel
content_hash: sha256:c540b80b565bed6dc5b5a372d12a51464bf84c477b54f17d0414551068eaf38c
created: 2026-09-27 01:47:00+00:00
page_id: sources/wu-2013-testing-vpin-big-data-response-reflecting
page_type: source
publication_venue: Lawrence Berkeley National Laboratory
related:
- concepts/market-microstructure
- concepts/vpin
- entities/kesheng-wu
- entities/e-wes-bethel
- entities/david-leinweber
revision_id: 1
schema_version: 2
source_hash: sha256:b66f27d153368c75aef0fdbf4d31cdc7634ac5e1f40ae43ccf41bbcd99bb3633
source_path: markdown_output/wu-2013-testing-vpin-big-data-response-reflecting.md
source_type: article
tags:
- vpin
- flash-crash
- futures
- false-positive-rate
- market-microstructure
- big-data
- rebuttal
- clock-unstated
- asset-futures
- harvest-relevant
title: Testing VPIN on Big Data -- Response to "Reflecting on the VPIN Dispute"
updated: '2026-09-27T01:47:00Z'
uuid: 7be8c307-795a-52dd-9519-1ea1e04c6b55
year: 2013
---

<!-- AUTHORED REGION START -->
# Testing VPIN on Big Data -- Response to "Reflecting on the VPIN Dispute"

## Summary

This is a short response note by a group of Lawrence Berkeley National Laboratory computer scientists and mathematicians who had earlier tested VPIN as a leading indicator of unusual market volatility, including around the 2010 Flash Crash. It answers a critique by Andersen and Bondarenko (AB), titled "Reflecting on the VPIN Dispute," which questioned the validity of the false positive rate the authors used to judge VPIN.

The authors argue that AB's version of the false positive rate mishandles test cases where no VPIN event occurred: dividing zero false positives by zero total events, AB recorded a rate of 0.0, whereas the authors' own convention records 0.5 false events out of 0.5 total events in that case, which is equivalent to reporting a false positive rate of 1, not 0. They say their reported average false positive rate of 7%, computed over 16,000 parameter combinations across 94 of the most liquid futures contracts from the start of 2007 to the middle of 2012, is therefore mathematically sound. They also dispute AB's expectation that a 0.99 CDF threshold would produce a VPIN event roughly every two days, showing instead that the observed average event count over the 66-month sample is far lower, because VPIN values in neighbouring time buckets are highly correlated and a whole run of above-threshold values is counted as a single event.

The note closes by rejecting two non-technical claims AB made: that the LBNL work might be biased by an author's affiliation with Marcos Lopez de Prado, and that AB's request to exchange data series with the LBNL group had gone unanswered. The authors say the affiliation began after the VPIN work started and that they replied to AB's email within a day, with data-exchange discussions ongoing about a month before AB's note was published.

## Clock and Sampling

**Not stated in the paper.**

The note describes VPIN values sampled on a time-series of 'time buckets'; it does not restate here how those buckets are defined. An event begins when the VPIN value's CDF crosses a chosen threshold (for example 0.9 or 0.99), and the event horizon is the following window of time buckets in which the authors check whether trading volatility is higher than average; a run of consecutive above-threshold buckets within that window is counted as one event rather than many.

## Data

- **Asset class:** Futures
- **Instruments:** 94 of the most liquid futures contracts, described as spanning equity, energy, precious metal, commodity and interest-rate instruments
- **Venue:** not stated
- **Period:** beginning of 2007 to middle of 2012 (66 months)
- **Granularity:** not stated in this note; described only as trading records aggregated into time buckets for VPIN computation

## Features and Measures

- **false positive rate (VPIN event test).** the share of declared VPIN events not followed by higher-than-average trading volatility in the event horizon; when a test case produces no event, the authors record 0.5 total events and 0.5 false-positive events rather than 0 divided by 0, which is equivalent to reporting a rate of 1 rather than 0 for that case.
- **event horizon.** a time window following the moment a VPIN value's CDF crosses a chosen threshold, within which the authors test whether volatility is elevated; consecutive above-threshold time buckets inside this window are grouped into a single event.

## Method

The note re-derives the false positive rate definition used in the authors' earlier large-scale VPIN study, which tested 16,000 combinations of VPIN control parameters, event horizon length and CDF threshold across 94 futures contracts over 66 months. It contrasts this with the false positive rate table given by Andersen and Bondarenko, arguing that AB's zero entries at high volatility percentiles are undefined 0/0 ratios rather than genuine zero false-positive rates, and that the authors' own convention avoids this by assigning 0.5/0.5 in such cases.

To address AB's claim that a 0.99 CDF threshold implies a VPIN event roughly every two days, the authors report the observed average number of events at CDF thresholds of 0.99 and 0.9, for both a well-chosen and a randomly chosen set of VPIN control parameters, and explain the discrepancy by the serial correlation of VPIN values across neighbouring time buckets.

The note also responds point by point to non-technical allegations in AB's paper concerning the independence of the LBNL researchers and the timeliness of their reply to a data-sharing request.

## Results

- Averaged over 94 futures contracts and 66 months, and across 16,000 combinations of control parameters, the false positive rate for VPIN-based volatility signals is about 7%.
- Andersen and Bondarenko's table reported false positive rates of 10.8, 3.0, 1.2, 0.0 and 0.0 at the 70th, 80th, 90th, 95th and 99th volatility percentiles; the authors argue the 0.0 entries reflect an undefined 0/0 division rather than a true zero rate.
- With a CDF threshold of 0.99, the average number of VPIN events across the 66-month sample is less than 20, not one every two days as AB's reasoning implied.
- With a CDF threshold of 0.9, the average number of events is about 40 using a well-chosen set of VPIN control parameters, and about 140 using a randomly chosen set.
- The authors state that a run of consecutive VPIN values above threshold is counted as a single event because nearby time-bucket values are highly correlated, which is why observed event counts are much lower than a naive CDF-based expectation.
- The authors say they responded to Andersen and Bondarenko's data-exchange request within 24 hours, and that discussions on exchanging data series were ongoing in July 2013, about a month before AB's note was published.

## Limitations

- The note is a rebuttal to a published critique rather than a self-contained empirical study; the underlying VPIN computation and full test methodology are described in a separate cited report, not reproduced here.
- Reported false positive rates and event counts are given only as averages across all 94 contracts and 66 months, with no per-contract or per-period breakdown in this note.
- Reader note: the section explaining the false-positive-rate figure is garbled by the document's PDF-to-text conversion, with what appear to be chart axis labels and a legend merged into the prose; those garbled fragments were not used as evidence.

## Related

- [[concepts/market-microstructure|market microstructure]]
- [[concepts/vpin|VPIN]]
- [[entities/kesheng-wu|Kesheng Wu]]
- [[entities/e-wes-bethel|E. Wes Bethel]]
- [[entities/david-leinweber|David Leinweber]]

## Citation

Kesheng Wu, E. Wes Bethel, Ming Gu, David Leinweber, Oliver Ruebel (2013). Testing VPIN on Big Data -- Response to "Reflecting on the VPIN Dispute". Lawrence Berkeley National Laboratory.

DOI: 10.2172/1165210

Text ingested: `markdown_output/wu-2013-testing-vpin-big-data-response-reflecting.md`, converted from `raw/ofi-event-clock/wu-2013-testing-vpin-big-data-response-reflecting.pdf`.

Coverage of this summary: Read the full text of this short response note: disclaimer, VPIN background, the false-positive-rate rebuttal, the VPIN-event-count rebuttal, the non-technical response, acknowledgements and references.

Known problems with the input: The document carries two dates: an eScholarship 'Publication Date' of 2014-01-31 and a response dateline of 8/30/2013; year was set to 2013 from the response's own dateline, consistent with the job's year_hint; The passage explaining the false-positive-rate figure is garbled by OCR/PDF conversion (chart axis numbers and a legend interleaved with prose); those fragments were excluded from the extraction.
<!-- AUTHORED REGION END -->