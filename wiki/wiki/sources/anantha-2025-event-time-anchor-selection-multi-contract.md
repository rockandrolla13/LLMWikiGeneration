---
authors:
- Aditya Nittur Anantha
- Shashi Jain
- Shivam Goyal
- Dhruv Misra
content_hash: sha256:8a829e3082331643daa91f3f1bb971a8a18613fde09d00fc920513c61bca7bf5
created: 2026-09-27 01:47:00+00:00
page_id: sources/anantha-2025-event-time-anchor-selection-multi-contract
page_type: source
related:
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/order-flow
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/optimal-execution
- entities/aditya-nittur-anantha
- entities/shashi-jain
revision_id: 1
schema_version: 2
source_hash: sha256:ac7409c67e9f9f0440305d7860109e7d6ff54275fc50fe71018a4a525b75f68a
source_path: markdown_output/anantha-2025-event-time-anchor-selection-multi-contract.md
source_type: paper
tags:
- hawkes-processes
- limit-order-book
- quoting
- execution-risk
- calendar-spread
- market-microstructure
- high-frequency-trading
- clock-calendar
- asset-futures
- harvest-relevant
title: Event-Time Anchor Selection for Multi-Contract Quoting
updated: '2026-09-27T01:47:00Z'
uuid: f6ac1351-6204-588b-aa1d-3a0443e89acc
year: 2025
---

<!-- AUTHORED REGION START -->
# Event-Time Anchor Selection for Multi-Contract Quoting

## Summary

When a trader quotes a calendar spread across two futures contracts, one leg is designated the reference and the other is quoted against it; the paper asks how to pick, at each moment, which leg is likely to stay most stable while the other leg's order is still filling, since instability in the reference leg is what causes realized execution cost to deviate from the trader's target spread.

The authors build an infeasible hindsight oracle that, for each short evaluation window, picks whichever leg would have minimized realized slippage on observed calendar-spread trade pairs. They then compare two real-time decision rules against that oracle: a Hawkes-process arrival-ratio rule that forecasts the near-term rate of reference-impacting tick events (trades, cancellations, and downward price modifications) on each leg from a fitted multivariate self-exciting point process, and a Composite Liquidity Factor (CLF) that scores each leg from the current limit order book alone, combining cross-level price gaps with cumulative depth. Both are evaluated tick-by-tick on NIFTY February and March 2022 futures contracts traded on the National Stock Exchange of India, using data from a single trading day.

The Hawkes arrival-ratio rule agrees with the oracle slightly more often overall than the best CLF variant, but the two rules are not interchangeable: the Hawkes rule performs best when the oracle keeps favoring the same leg for long, persistent stretches, while the CLF rule performs best when the oracle switches leg preference frequently. The two rules also frequently agree with the oracle in the same windows, but each also captures agreement the other misses.

What is new is treating reference-leg selection in multi-contract quoting as a formal information-comparison problem, scored against a realized-slippage oracle, rather than as a fixed rule; the paper's contribution is diagnostic, showing that event-history and instantaneous LOB-state signals carry complementary rather than redundant information for this choice.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Decisions are made on fixed, non-overlapping 10-millisecond evaluation windows, stepped forward every 10 ms, and every window's decision must use only information timestamped strictly before that window's start. The Hawkes-based rule fits kernels on the trailing 1,000 ms of tick history and simulates forward paths to forecast reference-impacting event counts over the next 10 ms. The CLF-based rule takes a majority vote of tick-level comparisons of the liquidity factor over the trailing 1,000 ms. Realized slippage observed within each window is used only to score the rules against a hindsight oracle, never as a decision input.

## Data

- **Asset class:** Futures
- **Instruments:** NIFTY index futures: the current-month contract expiring February 24, 2022, and the next-month contract expiring March 31, 2022
- **Venue:** National Stock Exchange (NSE) of India
- **Period:** February 7, 2022 (a single trading day)
- **Granularity:** tick-by-tick order book and trade messages, covering NEW, MODIFY, CANCEL, and TRADE event types

## Features and Measures

- **Arrival ratio (Hawkes).** For a given contract leg and LOB side, the forecast ratio of simulated reference-impacting event counts to simulated total event counts over a short forward horizon, produced by a fitted multivariate Hawkes process.
- **Composite Liquidity Factor (CLF).** A scalar score for one side of one leg's limit order book that contrasts the cross-level price gap to a given depth against the cumulative available quantity through that depth, used as a proxy for near-term price stability on the side that would be consumed.
- **Agreement score.** The fraction of evaluation windows in which a decision rule's chosen reference leg matches the leg chosen by the hindsight oracle.
- **Benchmark persistence bin.** A grouping of oracle decision runs by how many consecutive evaluation windows the oracle keeps selecting the same reference leg, used to condition agreement scores on how stable the oracle's preference is.

## Method

The reference-leg choice is formalized as a binary decision per evaluation window, made separately by two rules that each map information available strictly before the window to a leg choice. The Hawkes-based rule fits a multivariate self-exciting point process to reference-impacting tick events (trades, cancellations, downward price modifications), choosing among four kernel specifications (exponential, sum-of-exponentials, and two non-parametric estimators, EM and conditional-law) via Hansen's test for superior predictive ability, then simulates forward event paths with Ogata's thinning method to obtain the arrival ratio. The CLF-based rule needs no model fitting: it is computed directly from the current LOB snapshot's top depth levels, smoothed with an exponential moving average and combined by majority vote over the trailing history. Both rules are scored against an oracle constructed from the realized slippage of the closest matching pair of opposite-direction calendar-spread trades observed within each window, using the agreement score (share of windows matching the oracle) as the primary metric, computed overall, split by which leg the oracle favored, and split by the oracle's benchmark-persistence bin.

## Results

- The test for superior predictive ability does not reject the EM-based non-parametric Hawkes kernel as best among four candidates, with SPA values 0.017 (exponential), 0.015 (sum-of-exponentials), 0.530 (EM), and 0.000 (conditional law).
- The Hawkes arrival-ratio rule attains an agreement score of 0.6856 with the oracle over the full day; the best CLF variant (CLF4, using the top four depth levels) attains 0.6358.
- Both rules simultaneously agree with the oracle in 41.49% of evaluation windows; the Hawkes rule alone agrees in 27.08% and CLF4 alone in 22.10%; both disagree with the oracle in 9.34% of windows.
- The Hawkes rule agrees with the oracle in about 88% of windows when the oracle favors the current-month leg but only about 18% when it favors the next-month leg; CLF4 agrees in about 61% and 69% of those two cases respectively.
- In the lowest-persistence bin (oracle runs of 1-3 windows), CLF4's agreement score of 0.459 exceeds the Hawkes rule's 0.406; in the highest-persistence bin (runs of at least 59 windows), the ordering reverses, with the Hawkes rule reaching 0.702 versus CLF4's 0.641.
- Collapsing bins into low-persistence (runs up to 58 windows) and high-persistence (runs of 59 or more windows) segments, CLF4 scores 0.5155 against Hawkes's 0.3903 in the low-persistence segment, while the Hawkes rule scores 0.7060 against CLF4's 0.6441 in the high-persistence segment.
- About 94% of the day's evaluation windows fall in the highest-persistence bin, where the oracle keeps the same leg for at least 59 consecutive windows; over the full day the oracle favors the current-month (near) leg in about 72% of windows.
- The number of oracle-selected runs is close to symmetric between the two legs (124 runs on the current-month leg versus 123 on the next-month leg, across all persistence bins).

## Limitations

- Reader note: the empirical illustration uses a single trading day (February 7, 2022) and a single pair of NIFTY futures contracts; no other trading day or instrument pair is reported.
- The authors describe the framework as diagnostic rather than a full trading policy, and explicitly leave embedding the reference-leg choice in an explicit control or loss-minimizing formulation to future work.
- The evaluation oracle is an infeasible hindsight benchmark built from realized post-decision trade prices, so agreement scores measure closeness to an unattainable ideal rather than achievable trading profit.
- The authors state that fee, rebate, and cross-venue routing effects are assumed invariant to the reference-leg choice and are not modeled, an assumption that need not hold in other market settings.

## Related

- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/optimal-execution|optimal execution]]
- [[entities/aditya-nittur-anantha|Aditya Nittur Anantha]]
- [[entities/shashi-jain|Shashi Jain]]

## Citation

Aditya Nittur Anantha, Shashi Jain, Shivam Goyal, Dhruv Misra (2025). Event-Time Anchor Selection for Multi-Contract Quoting.

DOI: 10.48550/arxiv.2507.05749

Text ingested: `markdown_output/anantha-2025-event-time-anchor-selection-multi-contract.md`, converted from `raw/ofi-event-clock/anantha-2025-event-time-anchor-selection-multi-contract.pdf`.

Coverage of this summary: Read the entire markdown file: abstract, introduction, literature review, the worked entry/exit and reference-leg examples, the problem formulation, methodology (execution design, benchmarking framework, tick-based rule, Hawkes forecasting, CLF construction), data section, all of Section 5 (experiment and results, including kernel selection and the Hawkes/CLF comparison), discussion, conclusion, references, and the appendices.

Known problems with the input: Most equations, the log-quote-slope figure, and several tables/figures are OCR-omitted (marked as omitted pictures), so some formal definitions (e.g. the exact CLF formula and the oracle decision rule) are described from surrounding prose rather than the equations themselves; No journal, conference, or working-paper series is printed on the document; venue is left empty.
<!-- AUTHORED REGION END -->