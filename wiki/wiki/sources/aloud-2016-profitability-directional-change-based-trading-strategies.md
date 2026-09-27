---
authors:
- Monira Essa Aloud
content_hash: sha256:a007cf4720f1e62a92516e4ccaa14ab64342cb11079707fc633dff04a9efca9a
created: 2026-09-27 01:47:00+00:00
page_id: sources/aloud-2016-profitability-directional-change-based-trading-strategies
page_type: source
publication_venue: International Journal of Economics and Financial Issues, 2016,
  6(1), 87-95
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:071229979a716777dace4ae50db271b8a984dac8e1556bb10a033aa58e2a22e8
source_path: markdown_output/aloud-2016-profitability-directional-change-based-trading-strategies.md
source_type: paper
tags:
- directional-change
- intrinsic-time
- agent-based-simulation
- technical-trading
- saudi-stock-market
- trend-following
- contrarian-trading
- clock-intrinsic
- asset-equity
- harvest-relevant
title: 'Profitability of Directional Change Based Trading Strategies: The Case of
  Saudi Stock Market'
updated: '2026-09-27T01:47:00Z'
uuid: 2a93d802-fd3c-5f02-82d0-2df3066d13e3
year: 2016
---

<!-- AUTHORED REGION START -->
# Profitability of Directional Change Based Trading Strategies: The Case of Saudi Stock Market

## Summary

The paper asks whether trading strategies built on the directional-change (DC) event approach, which samples price movement in intrinsic (event-based) time rather than physical time, are profitable in the Saudi Stock Market, and whether adding a learning mechanism to choose the DC threshold and trading style improves on a strategy that commits to a fixed threshold. Three strategies are formulated and compared: ZI-DCT0, which commits to one fixed price-move threshold and one trading style (trend-following or contrarian) for the whole run; DCT1, which learns the best-performing threshold and trading style from a historical training window before trading; and DCT2, a new strategy proposed in this paper that extends DCT1 by periodically retraining, both on a fixed weekly schedule and whenever the agent's wealth falls to half its starting level.

All three strategies are implemented as trading agents inside an agent-based stock market simulation, fed historical high-frequency tick price data (bid and ask) for five Saudi Stock Market indices spanning the Banks and Financial Services sector and the Telecommunications and Information Technology sector, over a roughly six-month test period. Each agent starts with a fixed cash endowment and no shares, invests its full cash or share position on each trade, and is evaluated by its rate of investment (ROI) over the test period; results are averaged over ten independent simulation runs with different random seeds and threshold search ranges.

DCT2 achieves the highest average ROI across the five indices, ahead of DCT1 and both variants of ZI-DCT0, and its improvement over DCT1 is attributed to its ability to adapt its threshold and trading style as market conditions change during the run rather than fixing them once at the start. The learned thresholds chosen by DCT1 and DCT2 are similar in magnitude across the five indices, which the author reads as evidence that Saudi equity price series exhibit periodic directional-change patterns that a learning strategy can exploit.

What is new is the introduction of DCT2 itself (a directional-change strategy with both scheduled and wealth-triggered retraining) and its first application, together with ZI-DCT0 and DCT1, to the Saudi Stock Market, which the author states had not previously been examined for this class of automated trading strategy.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Prices are sampled in intrinsic time defined by directional-change (DC) events: a new event occurs whenever price moves by a fixed percentage threshold from the last local price extreme, alternating between upturn and downturn events, so the sampling frequency adapts to how active the market currently is rather than following a fixed clock interval. Trading decisions (buy or sell) are triggered at each DC event, with the direction depending on whether the agent trades trend-following or contrarian style. DCT1 learns its threshold and trading style from a two-month historical training window by testing 50 randomly generated thresholds under both trading styles and picking the combination with the highest observed ROI; DCT2 additionally retrains on a fixed weekly schedule and whenever its wealth falls to half its starting value.

## Data

- **Asset class:** Equities
- **Instruments:** five Saudi Stock Market indices: Saudi American Bank (SAMBA), Saudi British Bank (SABB), Al Rajhi Bank (RAJHI), Saudi Telecom Company (STC), and ZAIN Mobile Telecommunications Company (ZAIN)
- **Venue:** Saudi Stock Market (Tadawul)
- **Period:** 1 December 2014 to 25 May 2015
- **Granularity:** high-frequency tick data (timestamped bid and ask prices), resampled into intrinsic time via directional-change events

## Features and Measures

- **Directional Change (DC) event.** A price move of magnitude equal to a fixed percentage threshold from the last local price extreme, marking a shift between an upward and a downward price run and defining one step of intrinsic time.
- **Overshoot (OS) event.** The continuation of a price move in the same direction beyond the point where a DC event was triggered, ending when the next DC event (in either direction) occurs.
- **Rate of Investment (ROI).** The trading agent's total investment return over the test period divided by the cost of its investments, expressed as a percentage; the paper's sole performance measure.

## Method

Strategies are implemented as agents in an agent-based stock market simulation (ABSM) with one tradable asset per run, fed a historical price series through a market-maker. Each agent starts with 10,000 units of cash and no shares, may hold at most one open order at a time, invests its full cash balance when buying and its full share position when selling, and the market clears market orders immediately while limit orders execute once their price constraint is met.

ZI-DCT0 commits to one randomly chosen fixed threshold and one trading style for the whole run. DCT1 first searches 50 randomly generated thresholds under both trend-following and contrarian styles over a two-month training window and selects the combination with the highest realized ROI before trading live. DCT2 repeats this search on a fixed weekly schedule and additionally re-triggers the search whenever the agent's wealth falls to half its most recent reference wealth level. Results for all three strategies are averaged over ten independent simulation runs with different random seeds and threshold search ranges to check robustness.

## Results

- Averaged over the five Saudi stock indices, DCT2 achieves the highest mean return on investment (58%), ahead of ZI-DCT0 contrarian (31%), DCT1 (30%), and ZI-DCT0 trend-following (4%).
- For SAMBA, ZI-DCT0 contrarian and DCT1 both reach a return on investment of 74.11% using thresholds of 7% and 7.1%, and DCT2 improves further to 84.9% with a 5.9% threshold.
- For RAJHI, DCT2 reaches a 55.1% return on investment at a 4.2% contrarian threshold, well above ZI-DCT0's 30% and DCT1's 21.3%.
- For STC, DCT2 reaches a 79.96% return on investment versus 14.11% for DCT1 and 12.7% and 2.21% for the two ZI-DCT0 variants.
- ZAIN is the only index where a strategy variant loses money: ZI-DCT0 trend-following returns a loss of 6.1% at a 6% threshold, while the contrarian variant, DCT1 and DCT2 all remain positive, at 6.61%, 10.2% and 11.51% respectively.
- The thresholds selected by the learning strategies (DCT1 and DCT2) are similar in magnitude across the five indices, which the author reads as evidence of periodic directional-change patterns in Saudi equity prices.
- Results are averaged over 10 independent simulation runs per strategy, each with different random seeds and threshold search ranges, over a test period from 1 December 2014 to 25 May 2015.

## Limitations

- The study tests only one market (the Saudi Stock Market) over one roughly six-month period, so profitability is not shown to generalize to other markets or periods.
- The DCT2 retraining rules (a fixed weekly schedule and a wealth-halving trigger) are choices set by the author rather than tuned or justified against alternatives.
- Reader note: only five indices from two sectors (banking and telecommunications) are tested, so sector generalization is unclear.
- Reader note: the six simplifying assumptions about agent behavior (single open order, full-balance trades, no transaction fees) reduce realism relative to actual market participants.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Monira Essa Aloud (2016). Profitability of Directional Change Based Trading Strategies: The Case of Saudi Stock Market. International Journal of Economics and Financial Issues, 2016, 6(1), 87-95.

Text ingested: `markdown_output/aloud-2016-profitability-directional-change-based-trading-strategies.md`, converted from `raw/ofi-event-clock/aloud-2016-profitability-directional-change-based-trading-strategies.pdf`.

Coverage of this summary: Read the whole markdown file end to end, including the introduction, the DC event approach definition, the ZI-DCT0, DCT1 and DCT2 strategy descriptions, the experimental design, the ROI results table, and the conclusion.

Known problems with the input: The pseudo-code for Algorithms 1-3 and several inline mathematical expressions were partially garbled or rendered as omitted picture placeholders by the PDF-to-markdown converter, so exact algorithmic notation could not be fully verified beyond the surrounding prose.
<!-- AUTHORED REGION END -->