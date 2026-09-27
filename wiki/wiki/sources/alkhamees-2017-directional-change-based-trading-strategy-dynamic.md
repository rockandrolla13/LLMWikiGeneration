---
authors:
- Nora Alkhamees
- Maria Fasli
content_hash: sha256:904bd3049189356df1145064cdf6b44a55f280d1df78ca99a6bfda9b6ca8090b
created: 2026-09-27 01:47:00+00:00
page_id: sources/alkhamees-2017-directional-change-based-trading-strategy-dynamic
page_type: source
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/high-frequency-data
- concepts/alpha-signal
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:d8f7ff3d3def76aa2b8195194833e9eaaed88b2aab49588a73a7f5776e24cc02
source_path: markdown_output/alkhamees-2017-directional-change-based-trading-strategy-dynamic.md
source_type: paper
tags:
- directional-change
- dynamic-threshold
- trading-strategy
- ftse-100
- decision-tree
- overshoot
- equity
- clock-intrinsic
- asset-equity
- harvest-relevant
title: A Directional Change Based Trading Strategy with Dynamic Thresholds
updated: '2026-09-27T01:47:00Z'
uuid: bda04c2f-e708-5c5a-95e4-19c32f736044
year: 2017
---

<!-- AUTHORED REGION START -->
# A Directional Change Based Trading Strategy with Dynamic Thresholds

## Summary

The paper starts from the Directional Change (DC) approach, which summarizes price movements as alternating upturn and downturn events triggered whenever price moves by a fixed threshold, rather than by sampling at fixed calendar intervals. The authors' concern is that a single fixed threshold can miss real, economically meaningful price moves that fall just short of it, or can flag as an event a move that only met the threshold because of gradual drift. Their question is whether a threshold that is recalculated every day, rather than fixed once and for all, produces a more useful trading strategy.

They define a daily dynamic threshold from three pieces of information: the price change already accumulated since the day's open toward the current run's last high or low, the previous day's open-to-close percentage change, and the overnight percentage change between the previous close and the current open, combined with weights chosen so that a large previous-day or overnight move can lower the threshold needed to confirm a new event. On top of this dynamic threshold, they build a trading rule, derived from a J48 (C4.5) decision tree trained on FTSE 100 minute data, that switches between a trend-following and a contrarian order depending on whether the previous day's or overnight's price change was extreme (defined by the tree as at least 0.9%).

Testing on FTSE 100 minute-by-minute prices, they show that all 22 directional-change events detected by the dynamic threshold over a roughly nine-month training period corresponded to a same-day published news headline, whereas fixed thresholds detected either the same or fewer events with a much lower hit-rate against news. Their combined strategy (Dynamic Threshold Trading Strategy, DT-TS) then outperformed every tested fixed threshold and every other trading strategy (Contrarian Trading, Trend Following, and a prior Backlash Agent strategy) in both the training period and an out-of-sample testing period running into late 2016.

What is new here is the daily-adaptive threshold itself, replacing the fixed threshold that most prior Directional Change work uses, plus the specific decision rule for choosing between trend-following and contrarian trading based on the size of the previous day's and overnight's price change. The authors note their test period was dominated by one large macro event (the Brexit referendum), which affected how many trading opportunities arose and how profitable the strategy could be during out-of-sample testing.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Prices are sampled according to Directional Change (DC) events, which are triggered when the price moves by a threshold away from the last confirmed high or low, rather than at fixed time intervals; here the threshold is recalculated once per trading day (a dynamic threshold) from the current run's price move plus the previous day's open-to-close and overnight close-to-open percentage changes. A trading decision is made at every price update during the overshoot (OS) period that follows a DC confirmation, so the prediction/decision horizon is event-driven rather than fixed.

## Data

- **Asset class:** Equities
- **Instruments:** FTSE 100 index
- **Venue:** not stated
- **Period:** training: July 2015 to March 2016 (36+ weeks); testing: April 2016 to end of October 2016
- **Granularity:** minute-by-minute prices (average of open, high, low, and close) from Reuters Thomson One

## Features and Measures

- **Directional Change (DC) event.** A price-based event, either an upturn or a downturn, triggered when the price moves by at least a given threshold away from the last confirmed high or low.
- **Overshoot (OS) event.** The period following a DC confirmation point, lasting until the next DC event, during which the price continues moving in the same direction.
- **Dynamic (daily) threshold.** A directional-change threshold recomputed once per trading day from the current run's price change plus the previous day's open-to-close and overnight close-to-open percentage changes, replacing a single fixed threshold.
- **Backlash Agent (BA) Down-ind/Up-ind thresholds.** A pair of thresholds from a prior contrarian trading strategy, used here as one of the benchmark strategies, that trigger a buy or sell once an overshoot value crosses a tuned level.

## Method

The authors first calculate their dynamic threshold on FTSE 100 minute data and compare the resulting Directional Change events to same-day BBC News headlines, to check whether detected events line up with real news, doing the same for four fixed thresholds (0.03, 0.04, 0.05, 0.06). They then train a J48 (C4.5) decision tree on a labeled training set of minute-level price transitions to learn when a detected event should trigger a trend-following order versus a contrarian order, using the size of the previous day's and overnight's percentage price change as the deciding factor. The resulting rule set, combined with the dynamic threshold, forms their Dynamic Threshold Trading Strategy (DT-TS); trading starts with 100k monetary units and zero shares, and a buy or sell order always uses the full available cash or share balance. They compare DT-TS's cumulative profit to the same trading rules run with each fixed threshold (FT-TS), and to three other published strategies (Contrarian Trading, Trend Following, and the Backlash Agent), separately on the training period and on an out-of-sample testing period.

## Results

- Using the dynamic threshold, all 22 detected Directional Change events in the training period matched a same-day BBC News headline, versus only 12 of the 22 events detected by the closest-performing fixed threshold (0.03).
- In training, the dynamic-threshold strategy (DT-TS) earned 65% profit, versus 62% for the best fixed threshold (0.03) and 34%, 33%, and 38% for the Contrarian Trading, Trend Following, and Backlash Agent benchmark strategies run with the dynamic threshold's events.
- In out-of-sample testing (April-October 2016), DT-TS earned 47% profit, again higher than every fixed threshold tested and higher than Contrarian Trading, Trend Following, and Backlash Agent (23%, 23%, and 21% respectively).
- More than half of the Directional Change events detected in the test period (8 of 14) occurred in June 2016, around the EU Referendum/Brexit vote.
- Larger fixed thresholds generally detected fewer events and were less profitable in training, for example 22 events at threshold 0.03 versus 10 events at threshold 0.06.
- Among the fixed-threshold results, Contrarian Trading performed relatively better at high thresholds while Trend Following performed relatively better at low thresholds.

## Limitations

- The experiment covers a single index (the FTSE 100) over roughly one training year and seven testing months, so generalization to other markets, instruments, or sampling frequencies is untested; the authors list this as future work.
- Money management is simplified to using the entire available cash or share balance on every order, which the authors note can prevent a strategy from acting on a further favorable price move once its balance is already committed.
- The out-of-sample testing period was dominated by a single macro event (the Brexit referendum in June 2016), which the authors say reduced the number of trading opportunities and likely depressed the reported profitability.
- Reader note: transaction costs, slippage, and bid-ask spread are not discussed, so reported profit percentages are gross trading outcomes rather than a fully realistic net return.
- Reader note: no explicit publication venue or year is printed in the converted text, so how and where this version was reviewed cannot be confirmed from the document alone.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/directional-change|Directional Change]]

## Citation

Nora Alkhamees, Maria Fasli (2017). A Directional Change Based Trading Strategy with Dynamic Thresholds.

DOI: 10.1109/dsaa.2017.48

Text ingested: `markdown_output/alkhamees-2017-directional-change-based-trading-strategy-dynamic.md`, converted from `raw/ofi-event-clock/alkhamees-2017-directional-change-based-trading-strategy-dynamic.pdf`.

Coverage of this summary: Read the entire markdown text of the paper, including the abstract, all six numbered sections, both experiment tables (training and testing), the figure captions, and the reference list.

Known problems with the input: No publication venue (conference or journal name) is printed anywhere in the converted markdown; only author affiliations are shown, so venue is left blank; No copyright or publication year is printed in the visible text; year is taken from the job file's year_hint; year from file metadata; Several equation graphics (the DC upturn/downturn conditions, the overshoot-value formula, and the dynamic-threshold formulas) are rendered as omitted pictures, so their exact mathematical form is described here only qualitatively; Tables 2 and 3 in the source markdown contain stray strikethrough-style OCR artifacts (e.g. '~~ee~~') mixed into some cells; these were treated as conversion noise and ignored, not as data.
<!-- AUTHORED REGION END -->