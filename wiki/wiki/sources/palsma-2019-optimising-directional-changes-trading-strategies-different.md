---
authors:
- Jurgen Palsma
- Adesola Adegboye
content_hash: sha256:fd48131105909a94c751e428666dc195b74929ec13c941bac23988f11009f810
created: 2026-09-27 01:47:00+00:00
page_id: sources/palsma-2019-optimising-directional-changes-trading-strategies-different
page_type: source
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/high-frequency-trading
- concepts/stylized-facts
- concepts/directional-change
- entities/adesola-adegboye
revision_id: 1
schema_version: 2
source_hash: sha256:388cadcebdd9f3c209be6ee19e6cdd132c64c629f81119fcd10eb3bd15f90ba5
source_path: markdown_output/palsma-2019-optimising-directional-changes-trading-strategies-different.md
source_type: paper
tags:
- forex
- directional-changes
- particle-swarm-optimization
- shuffled-frog-leaping-algorithm
- genetic-algorithm
- event-based-sampling
- trading-strategy-optimization
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Optimising Directional Changes trading strategies with different algorithms
updated: '2026-09-27T01:47:00Z'
uuid: 7673647d-ffc4-56db-a2f6-730116870d50
year: 2019
---

<!-- AUTHORED REGION START -->
# Optimising Directional Changes trading strategies with different algorithms

## Summary

The paper asks whether machine-learning optimisers other than a genetic algorithm (GA) can improve a previously proposed directional-change (DC) based FX trading strategy. That strategy runs several DC price-change thresholds in parallel, each voting buy, hold or sell, with the votes weighted and combined into a single trading decision; the weights were originally tuned by a GA.

The authors replace the GA with two nature-inspired metaheuristics, particle swarm optimisation (PSO) and a continuous shuffled frog leaping algorithm (CSFLA), keeping the same multi-threshold DC strategy, the same five thresholds, and the same fitness function (total return minus a drawdown penalty). Both optimisers are tuned via a horse-race procedure over dozens of parameter combinations, then evaluated on 12 months of 10-minute FOREX data across four currency pairs, with the first three months used for tuning and each remaining month split 70/30 into training and testing data.

PSO produced the highest average return across the four pairs and ranked first in a Friedman test, ahead of CSFLA and a genetic-programming technical-analysis benchmark (tied for second) and the original GA (last); however a Holm post-hoc test found the ranking differences not statistically significant at the 5% level.

The contribution is empirical rather than methodological: it is, by the authors' account, the first work to test optimisers other than a GA on this specific multi-threshold DC strategy, and it shows both alternatives can match or exceed the GA's profitability while remaining broadly competitive with a technical-analysis strategy optimised separately by genetic programming.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are triggered by directional-change (DC) events: whenever price moves by a preset percentage threshold θ a DC event is confirmed, followed by an overshoot (OS) event that lasts until the next opposite DC event. Five thresholds (0.01%, 0.013%, 0.015%, 0.018%, 0.02%) are run in parallel over 10-minute interval FX price data, each producing its own event series; each threshold's current buy/hold/sell recommendation is combined into a single decision via a weighted vote, rather than a fixed prediction horizon.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** Four currency pairs: EUR/USD, EUR/GBP, GBP/CHF, GBP/USD (Euro/US Dollar, Euro/British Pound, British Pound/Swiss Franc, British Pound/US Dollar).
- **Venue:** not stated
- **Period:** 12 months, June 2013 to May 2014
- **Granularity:** 10-minute interval data

## Features and Measures

- **Directional Change (DC) event.** A confirmed price move of a preset percentage threshold θ, marking the start of a new up- or down-trend under the DC price-summarisation scheme.
- **Overshoot (OS) event.** The period following a confirmed DC event, lasting until the next opposite DC event is confirmed.
- **Multi-threshold weighted-vote strategy.** A trading rule that runs several DC thresholds in parallel, each recommending buy, hold or sell, and combines the recommendations into one decision by summing threshold-specific weights and following the majority-weighted action.
- **Fitness function (return minus drawdown).** The optimisation objective used to score a candidate parameter set: total return minus the maximum drawdown scaled by a risk-aversion tuning parameter α.

## Method

The multi-threshold DC strategy's parameters (trade size per action, the value of each DC threshold, and the weight given to each threshold) are optimised in turn by particle swarm optimisation (PSO) and a continuous shuffled frog leaping algorithm (CSFLA), replacing the genetic algorithm (GA) used in the strategy's original proposal. PSO moves candidate solutions ('particles') through the parameter space using a velocity term combining inertia, memory of each particle's own best position, and the neighbourhood's best position, with added early-stopping, velocity clamping and a low-fitness reset rule. CSFLA divides a population of candidate solutions ('frogs') into memeplexes and sub-memeplexes, evolving the weakest individual in each sub-memeplex toward the best individual in its group or, failing that, toward the best individual in the whole population. Both algorithms are scored with a fitness function equal to total return minus the maximum drawdown scaled by a tuning parameter α, and both are configured via a horse-race tuning process over a set of candidate parameter combinations, with the best configuration chosen using the non-parametric Friedman test. Results are compared against the original GA configuration and against a genetic-programming technical-analysis benchmark strategy.

## Results

- PSO had the highest mean return across the four currency pairs, 0.010381, versus 0.005303 for CSFLA, 0.00005 for the genetic-programming benchmark, and -0.023077 for the GA.
- In the Friedman ranking of average monthly returns, PSO ranked first (average rank 1.75), CSFLA and the genetic-programming benchmark tied for second (2.5), and the GA ranked last (3.25).
- Across the 36 monthly currency-pair datasets, the genetic-programming benchmark was the best performer 12 times, CSFLA 9 times, the GA 8 times, and PSO 7 times.
- A Holm post-hoc test found the ranking differences between the four algorithms were not statistically significant at the 5% level.
- Horse-race tuning tested over 50 PSO parameter combinations and over 40 CSFLA parameter combinations on three months of tuning data before selecting final configurations.
- Both PSO and CSFLA produced average returns comparable to the genetic-programming technical-analysis benchmark, while clearly outperforming the original GA-tuned strategy.

## Limitations

- The authors report that the ranking differences among the four algorithms were not statistically significant at the 5% level (Holm post-hoc test).
- Reader note: only four currency pairs and a single data granularity (10-minute FOREX bars) over one 12-month period were tested.
- Reader note: fitness evaluation requires a full trading simulation, which the authors describe as costly and which limited the tuning search to a few dozen parameter combinations per algorithm.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/directional-change|Directional Change]]
- [[entities/adesola-adegboye|Adesola Adegboye]]

## Citation

Jurgen Palsma, Adesola Adegboye (2019). Optimising Directional Changes trading strategies with different algorithms.

DOI: 10.1109/cec.2019.8790222

Text ingested: `markdown_output/palsma-2019-optimising-directional-changes-trading-strategies-different.md`, converted from `raw/ofi-event-clock/palsma-2019-optimising-directional-changes-trading-strategies-different.pdf`.

Coverage of this summary: Read the full markdown file, including the introduction, background/literature review, methodology, experimental setup, results and analysis, and conclusion.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->