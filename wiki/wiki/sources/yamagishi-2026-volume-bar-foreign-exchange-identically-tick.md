---
authors:
- ⼭岸 勇輝（Yuuki YAMAGISHI）
content_hash: sha256:5751670ae901bebffdec856ff6afdab221b5255484a677f8867845848bc7d69f
created: 2026-09-27 01:47:00+00:00
page_id: sources/yamagishi-2026-volume-bar-foreign-exchange-identically-tick
page_type: source
related:
- concepts/sampling-clocks
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/volume-clock
- concepts/trade-clock
revision_id: 1
schema_version: 2
source_hash: sha256:7b2a1a22865caaf2d556b27b3fbb475e295ccb8fc8faea0eb81a9f68fbeab2ab
source_path: markdown_output/yamagishi-2026-volume-bar-foreign-exchange-identically-tick.md
source_type: paper
tags:
- forex
- tick-bars
- volume-bars
- range-bars
- sampling-clocks
- market-microstructure
- dukascopy
- clock-compares
- asset-multi
- harvest-relevant
title: 為替の「出来⾼⾜」は、ティック⾜と恒等的に同じものである [F053]
updated: '2026-09-27T01:47:00Z'
uuid: 4253635d-c8ad-57e7-ae2b-993cfc9af7ed
year: 2026
---

<!-- AUTHORED REGION START -->
# 為替の「出来⾼⾜」は、ティック⾜と恒等的に同じものである [F053]

## Summary

The paper asks a narrow, definitional question: are foreign-exchange 'volume bars' actually the same object as tick bars, or merely similar in practice? The author argues from first principles that because retail/institutional FX data has no central exchange and 'volume' in these feeds is simply a count of price-update ticks, a bar that closes after a fixed cumulative volume is, by definition, identical to a bar that closes after a fixed number of ticks.

This is tested empirically on tick data for USDJPY, EURUSD, GBPUSD and XAUUSD from 2019 to 2024 (Dukascopy), by checking what fraction of bar-closing tick indices coincide between a tick-count bar, a volume bar, and a third bar type that instead accumulates the absolute path length of price moves (a range/move bar). A synthetic random-number benchmark, in which price moves are replaced with random draws while real timestamps are kept, is used to confirm which agreements are logical identities versus genuinely empirical facts.

The tick-bar and volume-bar closing points coincide exactly (agreement rate 1.0000, with identical bar counts) for all four instruments, including in the synthetic-random-number version, confirming this agreement is a tautology rather than a discovery. Switching the accumulated quantity to absolute price-path length instead produces a completely different bar boundary set, with agreement dropping to a median of 0.0135 - about 74 times lower - even when the two bar types are set to produce a similar number of bars.

The author also corrects an initial claim: accumulating price-path length per bar does not make the net one-bar price move constant, since price moves that reverse within a bar add to the path length without changing the net displacement, so the dispersion of net per-bar moves only falls modestly (from 16.85 to 15.36) rather than collapsing toward uniformity. The paper's stated contribution is conceptual rather than a new law: it isolates 'what quantity is accumulated' as the variable that changes a bar's identity, as distinct from the step size chosen for that quantity.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper defines and compares three bar-construction rules on FX/gold tick data: a tick bar that closes every N ticks; a volume bar that closes when cumulative volume reaches N, where FX volume is defined as one unit per tick; and a range/path-length bar that closes when the cumulative absolute price move since the last close reaches a threshold S. Agreement between bar types is measured as the fraction of tick indices at which their bar-closing points coincide, across four instruments.

## Data

- **Asset class:** Several asset classes
- **Instruments:** USDJPY, EURUSD, GBPUSD, XAUUSD
- **Venue:** Dukascopy (tick data feed)
- **Period:** 2019-2024
- **Granularity:** raw tick data (millisecond timestamps, bid/ask), aggregated into bars by tick count, cumulative volume (=tick count), or cumulative absolute price-path length

## Features and Measures

- **Tick bar.** A bar that closes after a fixed number N of ticks (quote updates) have occurred, where N is set per instrument/year as the total tick count divided by the number of one-minute bars.
- **Volume bar (FX).** A bar that closes once cumulative volume reaches a threshold N; in this FX tick data, volume is defined as one unit per tick, so a volume bar closes at exactly the same points as a tick bar by construction.
- **Range / path-length bar.** A bar that closes once the cumulative absolute price movement (the sum of absolute mid-price differences between successive ticks, i.e. the path length) since the last close reaches a threshold S, rather than closing on a fixed count of ticks or volume.
- **Bar-boundary agreement rate.** The fraction of tick indices at which two different bar-construction rules close a bar at the same tick, used to measure whether two clocks are effectively the same sampling rule.

## Method

For USDJPY, EURUSD, GBPUSD and XAUUSD tick data from Dukascopy (2019-2024), the author fixes a tick-bar step size N per instrument/year (from the average number of ticks per one-minute bar) and a range-bar path-length threshold S calibrated to match the median per-bar path length of the tick bars, then builds tick bars, volume bars, and range bars over the same tick stream. Bar-boundary agreement is measured as the overlap between the sets of tick indices at which each bar type closes, and dispersion of per-bar duration, net price move, and tick count is summarized as the ratio of the 90th to 10th percentile.

To separate a logical identity from an empirical finding, the author repeats the tick-bar/volume-bar and tick-bar/range-bar agreement calculations on a synthetic dataset in which the sequence of price moves is replaced by random draws (three synthetic series) while the real tick timestamps are kept, and compares the synthetic agreement rates to the empirical ones. All predictions are stated before the corresponding calculation is run.

## Results

- Tick-bar and volume-bar closing points agree exactly (agreement rate 1.0000) for all four instruments, with identical bar counts: 2,183,483 (USDJPY), 2,184,429 (EURUSD), 2,183,491 (GBPUSD) and 2,090,836 (XAUUSD).
- Tick-bar and range-bar agreement is far lower: 0.0140 (USDJPY), 0.0139 (EURUSD), 0.0131 (GBPUSD) and 0.0074 (XAUUSD), a median of 0.0135, about 74.2 times smaller than the 1.0000 tick/volume agreement.
- Range-bar counts (2,393,506 / 2,309,241 / 2,331,643 / 2,285,825) were calibrated to a similar order of magnitude as the tick-bar counts, yet their boundaries barely coincide, showing the low agreement is not just a step-size effect.
- Per-bar dispersion (90th/10th percentile ratio, medians across instruments): tick and volume bars have duration dispersion 7.04 (median duration 42.3 seconds), price-move dispersion 16.85 (median 0.9750 pips) and tick-count dispersion 1.00 (median 83 ticks); range bars have duration dispersion 12.28 (median 37.1 seconds), price-move dispersion 15.36 (median 1.0500 pips) and tick-count dispersion 2.25 (median 76 ticks).
- With price moves replaced by synthetic random numbers (real timestamps kept), the tick-bar/volume-bar agreement remains exactly 1.0000, and the tick-bar/range-bar agreement (0.0124, 0.0132, 0.0124, 0.0066 for the four instruments) is close to the empirical values, indicating the difference is a property of the bar definitions rather than of market dynamics.
- Tick-bar step sizes of 86, 76, 80 and 151 ticks and range-bar path-length thresholds of 8.4000, 5.5750, 8.0000 and 28.7475 pips were used for the four instruments respectively.

## Limitations

- The author states an earlier claim was imprecise: a range bar keeps the accumulated path length constant per bar, not the net one-bar price move, so the net-move dispersion only falls from 16.85 to 15.36 rather than converging to near-uniformity.
- Tick counts are specific to one data vendor (Dukascopy); the paper notes tick counts vary by data source, so results may not carry over to other feeds.
- The tick-bar step size N and range-bar threshold S were each fixed to one value rather than varied.
- Only three bar types (tick, volume, range) were compared; calendar-time bars and other bar types (e.g. renko) were excluded.
- The study does not evaluate trading performance, profit, or loss.
- Reader note: scope is limited to four instruments over 2019-2024; results are not claimed to generalize to other markets or periods.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/trade-clock|Trade Clock]]

## Citation

⼭岸 勇輝（Yuuki YAMAGISHI） (2026). 為替の「出来⾼⾜」は、ティック⾜と恒等的に同じものである [F053].

DOI: 10.5281/zenodo.22898174

Text ingested: `markdown_output/yamagishi-2026-volume-bar-foreign-exchange-identically-tick.md`, converted from `raw/ofi-event-clock/yamagishi-2026-volume-bar-foreign-exchange-identically-tick.pdf`.

Coverage of this summary: Read the whole converted markdown: abstract/summary, notation and question section, all measurement sections (3 through 6), the limitations section, conclusion, data/reproducibility table, and reference list.

Known problems with the input: This is a Japanese-language self-published research note (part of the author's numbered personal series; this entry is [F053]) rather than a peer-reviewed journal article; classified as source_type 'paper' as the closest fit; No DOI or venue is printed for this specific note in the extracted text (DOIs are given only for the author's earlier, related notes referenced as [F018], [F033], [F043]); venue left blank; The four-instrument sample mixes FX pairs (USDJPY, EURUSD, GBPUSD) with a precious metal (XAUUSD/gold); asset_class is recorded as 'multi' to reflect this; Some OCR/conversion artifacts remain in Japanese characters (e.g. Kangxi-radical variants of common kanji); these are carried through from the source markdown rather than corrected.
<!-- AUTHORED REGION END -->