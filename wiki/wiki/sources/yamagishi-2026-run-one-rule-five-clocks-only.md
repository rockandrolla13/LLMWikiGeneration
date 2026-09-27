---
authors:
- Yuuki Yamagishi
content_hash: sha256:c3e741ad439138167ef46eb80059870cfc6576fd6089181564b4297d7e763d1b
created: 2026-09-27 01:47:00+00:00
page_id: sources/yamagishi-2026-run-one-rule-five-clocks-only
page_type: source
related:
- concepts/sampling-clocks
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/backtesting
- concepts/volume-clock
- concepts/trade-clock
revision_id: 1
schema_version: 2
source_hash: sha256:9e8ae10e294a0dd6cb390f66aee82e362c93b5504b36adf2b312c2adabd5d569
source_path: markdown_output/yamagishi-2026-run-one-rule-five-clocks-only.md
source_type: paper
tags:
- intraday-bars
- volume-bars
- tick-bars
- range-bars
- fx
- trading-rule-backtest
- clock-choice
- clock-compares
- asset-multi
- harvest-relevant
title: 'Run One Rule on Five Clocks and Only the Direction and the Cost Agree [F055]:
  The direction stays below a cost of 0.7123 to 0.7304 pips on all five and the cost
  differs by only 1.0254 times, yet the count differs by 57.4639 times and the duration
  of a bar by 62.5735 times'
updated: '2026-09-27T01:47:00Z'
uuid: 34413449-0d64-55a5-a53a-743c9efaf64b
year: 2026
---

<!-- AUTHORED REGION START -->
# Run One Rule on Five Clocks and Only the Direction and the Cost Agree [F055]: The direction stays below a cost of 0.7123 to 0.7304 pips on all five and the cost differs by only 1.0254 times, yet the count differs by 57.4639 times and the duration of a bar by 62.5735 times

## Summary

The paper asks, holding a single trading rule fixed, what changes and what stays the same when the definition of 'a bar' is switched across five common intraday clocks: fixed-time bars (minute and hourly), event-count (tick) bars, volume bars, and absolute-move (range) bars.

Using tick-level bid/ask data for USDJPY, EURUSD, GBPUSD and XAUUSD over 2019-2024, the author builds bars under each of the five clocks with step sizes chosen so that the tick, volume and range bar counts are matched against the hourly bar count, then runs one identical rule on every clock: enter in the direction of the previous bar's close-minus-open and exit 24 bars later. A directional edge (D), a day-clustered t-statistic, and the median in-bar bid-ask spread (cost) are compared across clocks, alongside bar count, bar duration and per-bar move, with a synthetic random walk used as a control baseline.

The directional edge and median trading cost were similar across all five clocks, but bar count and bar duration differed by roughly sixty-fold across clocks. Only minute bars reached a day-clustered t-statistic above 2, yet the measured edge on minute bars was smaller than the trading cost per bar. A pre-registered prediction that the per-bar move would spread out least on range bars did not hold: tick and volume bars had a smaller spread of move than range bars, which the author attributes to range bars holding path length, not net displacement, constant.

The stated contribution is narrow: it adds a fifth clock (volume bars) to a companion paper's four-clock comparison and produces a single table of which measured quantities are invariant to clock choice and which are not, arguing that describing a result by which bar type it appeared on is less informative than stating the measured size next to its trading cost.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Five clocks are directly compared: minute bars and hourly bars (fixed calendar time), tick bars (every N ticks, with N chosen so the tick bar count matches the hourly bar count), volume bars (every time cumulative volume reaches N, where FX volume is defined as tick count), and range bars (every time the cumulative absolute price path reaches a fixed distance S). One rule is run identically on all five: enter in the direction of the previous bar (sign of close minus open) and close the position 24 bars later, with no separate exit rule, so the prediction horizon is fixed at 24 bars of whichever clock is in use rather than a fixed calendar time.

## Data

- **Asset class:** Several asset classes
- **Instruments:** USDJPY, EURUSD, GBPUSD, and XAUUSD (gold), from Dukascopy-derived tick data.
- **Venue:** Not stated (data vendor is Dukascopy; no exchange or ECN is named).
- **Period:** 2019-2024 (six years).
- **Granularity:** Tick-level bid/ask price data aggregated into five different bar-sampling schemes: minute bars, hourly bars, tick-count bars, volume bars, and range bars.

## Features and Measures

- **Minute and hourly bars (clock-based).** Bars closed at fixed calendar intervals (every minute or every hour), holding elapsed time constant per bar.
- **Tick bars (event-count based).** Bars closed every N ticks, holding the elapsed tick count constant per bar, with N set so the total tick-bar count matches the hourly bar count.
- **Volume bars.** Bars closed every time cumulative volume reaches a fixed threshold N; in this FX dataset volume is defined as the tick count, so volume bars are numerically identical to tick bars.
- **Range bars.** Bars closed every time the cumulative absolute price path reaches a fixed distance S (S set to the tick bars' median per-bar path length), holding path length rather than net displacement constant.
- **D (mean directional edge).** The mean of the previous bar's direction multiplied by the price move over the next 24 bars, in pips, used as the outcome of the fixed trading rule.
- **Cost.** The median bid-ask spread observed inside a bar, in pips, used as a trading-friction benchmark to compare against the measured directional edge.
- **Spread of a quantity.** The ratio of a distribution's ninetieth percentile to its tenth percentile, used to measure how variable bar duration or per-bar move is within a given clock.

## Method

For each instrument and clock, the author computes D (the mean directional return over the next 24 bars), a t-statistic clustered by day, and the median in-bar spread (cost), then reports the median of these statistics across the four instruments per clock.

A second analysis computes the maximum-to-minimum ratio across the five clocks for seven quantities (D, cost, count, bar duration, move per bar, spread of move, spread of duration) to identify which quantities are stable and which vary strongly with clock choice.

A synthetic random walk, generated down to the tick level across three draws with the real data's observed times and spreads left as measured, is run through the same five-clock, same-rule procedure as a null-model baseline for comparison against the real-data results.

## Results

- Across all five clocks, D (the rule's directional edge) ranged from -0.0540 to +0.2789 pips and stayed below a median cost of 0.7123 to 0.7304 pips, a cost ratio (maximum over minimum) of only 1.0254.
- The bar count differed by 57.4639 times and bar duration by 62.5735 times across clocks, despite tick, volume and range bar step sizes being calibrated to match the hourly bar count.
- Only minute bars passed a daily t-statistic threshold of 2 (t = -2.9864), but the associated size (-0.0540 pips) was smaller than the median in-bar cost (0.7129 pips), so the statistically distinguishable edge was not economically larger than the trading cost.
- Tick bars and volume bars produced identical count, D, t and cost values, because in this FX dataset volume is defined as tick count, making the two clocks the same rule by construction.
- The pre-registered prediction that range bars would have the smallest spread of per-bar move failed: tick and volume bars had a spread of 14.92 versus 15.01 for range bars, because range bars hold path length rather than net displacement constant.
- On a synthetic random walk matched to the same instruments, D ranged from -0.1598 to +0.0222 pips and the daily t reached only 0.1044 in absolute value, versus 2.9864 for the real minute-bar result.

## Limitations

- One trading rule (previous-bar-direction entry, fixed 24-bar exit) is tested; no alternative entry or exit rules are examined.
- The measurement runs to a fixed bar-count horizon with no separate exit rule, and no profit-and-loss or performance measure is computed.
- The step sizes (N ticks and S price-path distance) are fixed by a single declared calibration method (matched to the hourly bar count) rather than varied.
- Only four instruments (USDJPY, EURUSD, GBPUSD, XAUUSD) over six years (2019-2024) are used; the author states nothing is claimed about other markets or periods.
- Reader note: the paper is self-published by an independent researcher and references five companion papers ([F019], [F033], [F049], [F053], [F054]) by DOI without reproducing their content, so several supporting claims about what those companion papers measured could not be independently checked from this document alone.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/backtesting|backtesting]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/trade-clock|Trade Clock]]

## Citation

Yuuki Yamagishi (2026). Run One Rule on Five Clocks and Only the Direction and the Cost Agree [F055]: The direction stays below a cost of 0.7123 to 0.7304 pips on all five and the cost differs by only 1.0254 times, yet the count differs by 57.4639 times and the duration of a bar by 62.5735 times.

DOI: 10.5281/zenodo.22898302

Text ingested: `markdown_output/yamagishi-2026-run-one-rule-five-clocks-only.md`, converted from `raw/ofi-event-clock/yamagishi-2026-run-one-rule-five-clocks-only.pdf`.

Coverage of this summary: Read the entire paper start to end (abstract through references); it is short so no sections were skipped.

Known problems with the input: The paper's title, abstract and body use an unusual annotation style (star-rated observations, warning symbols, per-claim references to a private working-paper series identified only by Zenodo DOIs) rather than standard academic prose; the underlying numeric claims are internally consistent and clearly defined, so they were extracted as stated, but the referenced companion papers ([F019], [F033], [F049], [F053], [F054]) could not be checked against this document alone.
<!-- AUTHORED REGION END -->