---
authors:
- Edward P. K. Tsang
- Shuai Ma
- V. L. Raju Chinthalapati
content_hash: sha256:2f322ec9082d84565ceae48fe0085f9991daeafeffb8fb8cf4a974e6a344aa49
created: 2026-09-27 01:47:00+00:00
page_id: sources/tsang-2024-nowcasting-directional-change-high-frequency-fx
page_type: source
publication_venue: Intelligent Systems in Accounting, Finance and Management
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/high-frequency-trading
- concepts/stylized-facts
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:0e9453413082e3de8fde8a653b9fbc6d281c0d7e51da007c61afc4a9cc8899e2
source_path: markdown_output/tsang-2024-nowcasting-directional-change-high-frequency-fx.md
source_type: paper
tags:
- directional-change
- fx
- intrinsic-time
- nowcasting
- tick-data
- trend-reversal
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Nowcasting directional change in high frequency FX markets
updated: '2026-09-27T01:47:00Z'
uuid: 570d57e1-7d4a-5969-b2fc-438143902c7a
year: 2024
---

<!-- AUTHORED REGION START -->
# Nowcasting directional change in high frequency FX markets

## Summary

Directional change (DC) records a new observation only when price reverses from the prevailing trend by a fixed threshold, and such a reversal can only be confirmed retrospectively, at a later 'DC confirmation point.' The paper asks whether it is possible to 'nowcast' that a reversal has already happened before that confirmation point arrives, which would let a trader act earlier than the DC framework normally allows.

The authors define two threshold-normalized indicators computed purely from historical DC statistics: aTMV, the current price's movement from the last confirmed extreme point expressed as a multiple of the DC threshold, and BM, how far price has retraced from the highest aTMV seen so far in the current trend. They propose a Nowcast Constant Algorithm (NCA) that flags a reversal once aTMV exceeds a fixed cutoff and BM exceeds a second fixed cutoff, with both cutoffs chosen from the empirical distribution of a training period rather than optimized or learned. NCA is tested on tick-to-tick EUR/USD, USD/JPY and GBP/USD data, split into a training period (used to set the two thresholds) and a later nowcasting/test period, under two DC thresholds (0.0016 and 0.0032).

The main finding is that this deliberately simple, untuned rule works: the majority of its nowcasts on EUR/USD are correct (made after the true reversal), and among correct nowcasts the large majority are also useful (made before the DC confirmation point), with broadly similar precision found when the method is repeated on USD/JPY and GBP/USD. Timeliness varies a lot across nowcasts, but on average nowcasts arrive well before confirmation, both in price terms and in elapsed time.

What is new is the demonstration that a crude, non-machine-learning, purely historical-distribution rule can already distinguish a real reversal from noise before DC's own hindsight-based confirmation mechanism does, which the authors present as an early proof of concept rather than a tuned trading system, leaving parameter optimization and additional indicators to future work.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations follow directional-change (DC) intrinsic time: a new 'event' of interest is not a fixed calendar interval but a price reversal of at least a fixed percentage threshold from the current trend, confirmed only in hindsight at a later transaction. The paper's nowcasting task has no fixed prediction horizon either; instead the Nowcast Constant Algorithm continuously checks, transaction by transaction, whether two threshold conditions on the aTMV and BM indicators are met, and if so declares (before the DC confirmation point) that the trend has already reversed.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** EUR/USD, USD/JPY, and GBP/USD tick-to-tick exchange rate data
- **Venue:** not stated
- **Period:** Training period September 2009 to December 2013; nowcasting/test period January 2014 to December 2015 (same split structure used for all three pairs)
- **Granularity:** Tick-to-tick (every transaction), analyzed under a directional-change threshold of 0.0016 or 0.0032

## Features and Measures

- **Absolute Total Movement (aTMV).** The absolute price change from the last confirmed extreme point to the current price, divided by the directional-change threshold, so that trend magnitudes observed under different thresholds can be compared on the same scale.
- **Below Max (BM).** A bounded measure of how far the current price has retraced from the highest aTMV value reached so far in the ongoing trend; it is 0 at that maximum and would reach 1 exactly where a directional change is formally confirmed.

## Method

The Nowcast Constant Algorithm (NCA) declares that a new trend has started once, within the current trend, the transaction recording the maximum aTMV exceeds a fixed cutoff PTMV and the current transaction's BM exceeds a fixed cutoff PBM. Both cutoffs are read off the empirical distribution of aTMV and BM observed in a training period (e.g. picking the value historically exceeded only 1% or so of the time), rather than fitted or optimized, so the method is entirely data-driven but deliberately untuned. Performance is judged with a precision measure (the share of nowcasts that are 'correct,' i.e. made after the true reversal, and the share of correct nowcasts that are also 'good,' i.e. made before the DC confirmation point) and with two timeliness measures, one in price terms (aTMV distance from the confirmation point) and one in elapsed time, computed separately for EUR/USD, USD/JPY and GBP/USD and for two DC thresholds.

## Results

- On EUR/USD under a 0.0016 threshold, of 3,452 nowcasts made in the test period, 2,300 (66.63%) were correct.
- Of those correct EUR/USD nowcasts, 2,264 (98.43%) were also good, i.e. made before the DC confirmation point.
- Under the larger EUR/USD threshold 0.0032, correctness precision was lower at 59.80%, but goodness precision was higher at 99.63%.
- Average TimelinessPrice on EUR/USD was 0.336 threshold-units under 0.0016 and 0.399 under 0.0032, showing the price-based timeliness is stable once normalized by the threshold.
- Average TimelinessTime on EUR/USD under 0.0016 was 1,967 seconds, with a maximum of 221,194 seconds for a single nowcast.
- On USD/JPY under threshold 0.0016, 81.39% of nowcasts were correct and all correct nowcasts (100%) were also good.
- On GBP/USD under threshold 0.0032, 77.78% of nowcasts were correct and all correct nowcasts (100%) were also good.

## Limitations

- The parameters PTMV and PBM were chosen almost arbitrarily from the training-period distribution and were not fine-tuned or optimized, by the authors' own statement.
- The algorithm relies on only two indicators (aTMV and BM); the authors state more indicators should help.
- Testing is limited to three FX pairs and tick data from a single data source.
- Reader note: no comparison is reported against a baseline forecasting or nowcasting model, so it is unclear how much of the reported precision is attributable to the DC framework itself versus the specific NCA rule.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/directional-change|Directional Change]]

## Citation

Edward P. K. Tsang, Shuai Ma, V. L. Raju Chinthalapati (2024). Nowcasting directional change in high frequency FX markets. Intelligent Systems in Accounting, Finance and Management.

DOI: 10.1002/isaf.1552

Text ingested: `markdown_output/tsang-2024-nowcasting-directional-change-high-frequency-fx.md`, converted from `raw/ofi-event-clock/tsang-2024-nowcasting-directional-change-high-frequency-fx.pdf`.

Coverage of this summary: Read the whole paper: abstract, introduction, DC indicator definitions (aTMV, BM), the NCA algorithm design, the EUR/USD empirical results (Table 3), the additional USD/JPY and GBP/USD experiments (Tables 4-7), and the concluding summary.

Known problems with the input: Several tables (Tables 2, 4, 5) are rendered by the markdown conversion with jumbled row/column structure; the summary numbers used here were cross-checked against the surrounding prose rather than read directly off those table layouts.
<!-- AUTHORED REGION END -->