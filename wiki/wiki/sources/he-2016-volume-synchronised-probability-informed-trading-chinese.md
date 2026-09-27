---
authors:
- Zhongzhi (Lawrence) He
- Jinzhi Jiang
- Martin Kusy
- Samir Trabelsi
content_hash: sha256:b0954abaa31cbdee651ac85339274f9f0f06f4ec82118aef7290f36752de7408
created: 2026-09-27 01:47:00+00:00
page_id: sources/he-2016-volume-synchronised-probability-informed-trading-chinese
page_type: source
publication_venue: China Accounting and Finance Review, Volume 18, Number 2 (June
  2016)
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/adverse-selection
- concepts/trade-classification
- concepts/high-frequency-trading
- concepts/order-imbalance
- concepts/vpin
- concepts/bulk-volume-classification
revision_id: 1
schema_version: 2
source_hash: sha256:f96890545008ab22e5b515f2736ce1f634d313821eb32086e605fe1d66f22ff6
source_path: markdown_output/he-2016-volume-synchronised-probability-informed-trading-chinese.md
source_type: paper
tags:
- vpin
- informed-trading
- trade-classification
- order-flow-toxicity
- chinese-futures
- risk-warning
- clock-volume
- asset-futures
- harvest-core
title: 'Volume-Synchronised Probability of Informed Trading on Chinese Index Futures:
  A Comparative Approach'
updated: '2026-09-27T01:47:00Z'
uuid: 5a66ea78-dcd2-57d7-bf20-3db32d1ca099
year: 2016
---

<!-- AUTHORED REGION START -->
# Volume-Synchronised Probability of Informed Trading on Chinese Index Futures: A Comparative Approach

## Summary

The paper asks which of three ways of building the Volume-Synchronised Probability of Informed Trading (VPIN) metric, tick rule (TR), Lee-Ready (LR), and bulk volume (BV) trade classification, gives the most reliable early warning of extreme volatility, testing this out-of-sample on the Chinese market rather than the US market where the original VPIN debate took place.

Using tick-level transaction data on China's stock index futures from 2012 to 2013, the authors build BV-VPIN, TR-VPIN and LR-VPIN following the same four-step procedure: aggregate 1-minute time bars, form volume buckets, classify buy/sell volume by each rule, then compute VPIN as a rolling average of bucket order imbalance. They compare the resulting cumulative distribution functions (CDFs) around two China-specific volatility events, the June 2013 Money Shortage Event and the 16 August 2013 Fat Finger Event.

BV-VPIN's CDF rose to a high level well before both events and stayed high throughout, while TR-VPIN and LR-VPIN showed no stable early-warning pattern, in some cases rising only after the event or even declining beforehand. This ranking held up across eight different combinations of time-bar length, bucket size and sample length.

The paper extends the ongoing US-focused TR-versus-BV VPIN debate by adding the Lee-Ready algorithm as a third comparison point and by testing it out-of-sample on a market argued to be more speculative and manipulative than the US, concluding this supports using BV-VPIN as a practical risk-warning tool in a high-frequency trading setting.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Transactions are first aggregated into 1-minute time bars (price change and total volume per bar), then time bars are grouped into fixed-size volume buckets, with bucket size set as average daily volume divided into 50 buckets. Each bucket's buy and sell volume is classified by the tick rule, Lee-Ready rule, or bulk-volume rule, and VPIN is the rolling-window average of order imbalance across a sample of buckets, with a sample length of 50 buckets as the default and other bar/bucket/sample-length combinations tested for robustness.

## Data

- **Asset class:** Futures
- **Instruments:** China Shanghai Shenzhen 300 stock index futures
- **Venue:** China Financial Futures Exchange (underlying transaction data from the Shanghai Stock Exchange)
- **Period:** January 2012 to December 2013, trading hours 9:30 a.m. to 3:00 p.m.
- **Granularity:** 500-microsecond tick-level transaction data, aggregated into 1-minute time bars and volume buckets

## Features and Measures

- **BV-VPIN.** VPIN computed using bulk-volume trade classification, which splits each time bar's volume into buy and sell portions using the normal CDF of the standardized price change over the bar.
- **TR-VPIN.** VPIN computed using the tick rule, which classifies a trade as buyer- or seller-initiated by comparing its price to the previous trade price, resolving zero-tick trades from the closest prior non-zero price change.
- **LR-VPIN.** VPIN computed using the Lee-Ready algorithm, a quote-based rule that classifies a trade relative to the midpoint of the prevailing best bid and ask quotes.
- **Order imbalance (volume bucket).** The absolute difference between classified buy volume and sell volume within a fixed-size volume bucket, the building block that VPIN averages over a rolling sample of buckets.

## Method

For each of the three classification rules, transactions are aggregated into 1-minute time bars, volume is grouped into buckets sized as average daily volume divided by 50, buy/sell volume within each bucket is split by the rule-specific classification, and VPIN is the rolling average of the resulting order imbalance over a sample of buckets (50 by default).

Effectiveness is judged via CDF thresholds: for each metric, the authors check whether its CDF rises to a high level in advance of, and stays high through, two known highly volatile episodes, the June 2013 Money Shortage Event and the 16 August 2013 Fat Finger Event, and repeat this check for eight combinations of time-bar length, bucket-computation window and sample length to test robustness.

## Results

- BV-VPIN's CDF crossed 0.8 about 15 minutes before the Fat Finger Event's price surge of 5.62% at 11:05 a.m. on 16 August 2013 and stayed elevated through the afternoon plunge, while TR-VPIN and LR-VPIN showed no stable early-warning pattern around that event.
- In the Money Shortage Event, BV-VPIN's CDF had already exceeded 0.9 before the 24 June plunge, when the index fell 7.1%, from 2,296 to 2,133 points, and remained high through the two-week period 17-28 June, whereas TR-VPIN and LR-VPIN did not show a consistently high level.
- Over the full 2012-2013 sample, BV-VPIN's empirical distribution spans a wider range than TR-VPIN or LR-VPIN: its CDF reaches 50% around a VPIN value of 0.3, 80% around 0.39, and 90% above 0.5, versus much lower VPIN levels for TR-VPIN (50% around 0.13, 80% around 0.17, 90% around 0.24) and LR-VPIN.
- Mean BV-VPIN in the Chinese sample is 0.2961 with a standard deviation of 0.0861, higher than the 0.2251 mean reported for the US market in prior work, which the authors interpret as reflecting more severe information asymmetry in the Chinese market.
- Across eight robustness combinations of time bar, bucket size and sample length, BV-VPIN's CDF still crossed the 80% threshold before both volatile events in every specification tested.

## Limitations

- Chinese index futures data lack directly signed buy/sell identifiers, so all three classification rules are themselves approximations rather than ground truth.
- The comparison is limited to two specific volatile episodes on one instrument over a two-year window.
- Authors' conclusion rests on visual/threshold comparison of CDFs around two episodes rather than a formal statistical predictive test.
- Reader note: some tables and figures (numeric table bodies and chart images) did not survive PDF-to-markdown conversion; the results above rely on the surrounding prose rather than reconstructed table cells.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]

## Citation

Zhongzhi (Lawrence) He, Jinzhi Jiang, Martin Kusy, Samir Trabelsi (2016). Volume-Synchronised Probability of Informed Trading on Chinese Index Futures: A Comparative Approach. China Accounting and Finance Review, Volume 18, Number 2 (June 2016).

DOI: 10.7603/s40570-016-0005-6

Text ingested: `markdown_output/he-2016-volume-synchronised-probability-informed-trading-chinese.md`, converted from `raw/ofi-event-clock/he-2016-volume-synchronised-probability-informed-trading-chinese.pdf`.

Coverage of this summary: Read the whole paper end to end, including the abstract (English and Chinese), literature review, data and methodology section, both event studies, the robustness section, and the conclusion.

Known problems with the input: Several tables (e.g., Tables 1-7) and figure images render as captions only in the converted markdown, with numeric table bodies missing or garbled; figures and results reported here rely on numbers stated in the surrounding prose, not on reconstructing missing table cells.
<!-- AUTHORED REGION END -->