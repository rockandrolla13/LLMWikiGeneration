---
authors:
- Jeremie Gypteau
- Fernando E. B. Otero
- Michael Kampouridis
content_hash: sha256:d0e93e124e0d7603a1d423317a92f275081f697245af53ef4cf5eb9a8d2728b5
created: 2026-09-27 01:47:00+00:00
page_id: sources/gypteau-2015-generating-directional-change-based-trading-strategies
page_type: source
publication_venue: 18th European Conference on Applications of Evolutionary Computation,
  EvoStar 2015
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/alpha-signal
- concepts/feature-engineering
- concepts/directional-change
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:ab3179aefbd7a5afae71f68433787b8bf31abdfdca9c383e800191de705b45fd
source_path: markdown_output/gypteau-2015-generating-directional-change-based-trading-strategies.md
source_type: paper
tags:
- directional-change
- genetic-programming
- intrinsic-time
- trading-strategy
- event-based-clock
- backtesting
- clock-intrinsic
- asset-equity
- harvest-relevant
title: Generating Directional Change Based Trading Strategies with Genetic Programming
updated: '2026-09-27T01:47:00Z'
uuid: 00e0f63a-1d7b-53fb-af97-dc500b12146b
year: 2015
---

<!-- AUTHORED REGION START -->
# Generating Directional Change Based Trading Strategies with Genetic Programming

## Summary

The paper asks whether an intrinsic, event-based time scale built from Directional Change (DC) events can generate profitable trading strategies, as an alternative to strategies built on fixed physical-time intervals such as daily closing prices. A DC event is triggered when price moves by a chosen threshold from the last confirmed extreme; the period between one DC event and the next is split into a DC phase and an Overshoot (OS) phase, and prior work had shown that the OS phase following a DC event of threshold theta tends to last about twice as long as the DC phase itself, without previously being used to build trading rules.

The authors use tree-based genetic programming (GP) to evolve boolean expressions that combine the buy/sell signals of several randomly initialised DC thresholds using AND, OR, NOR, XOR and NOT functions. Each evolved individual is a trading strategy: its fitness is the cash-plus-stock profit it earns by buying or selling one unit at each training-period data point according to its boolean output. The evolved GP strategies are compared against the best single fixed DC threshold chosen from a fixed candidate list on the same training data.

On four daily closing-price datasets (Barclays and Marks & Spencer shares, and the NASDAQ and NYSE indices), GP-evolved multi-threshold strategies produced higher profit than the best fixed single threshold in the held-out test period for all four datasets, and unlike the fixed-threshold strategies the GP strategies never produced a loss. This is presented as evidence that combining multiple DC thresholds through GP captures more of the market's directional-change structure than any single fixed threshold, and that the DC/intrinsic-time paradigm can be turned into a practical, profitable forecasting and trading tool rather than only a descriptive statistical curiosity.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are triggered by Directional Change (DC) events: a DC event is confirmed when price moves by a fixed percentage threshold away from the last confirmed price extreme, and is followed by an Overshoot (OS) phase that lasts until the next opposite DC event fires. Multiple DC thresholds are evaluated in parallel and their boolean up/down outputs are combined by a GP-evolved expression to produce a single buy or sell decision at each point in the underlying daily closing-price series. The prediction horizon is one trading decision per data point in a 1000-day training period, with performance then judged on a separate 500-day test period; there is no other explicit forecast horizon.

## Data

- **Asset class:** Equities
- **Instruments:** Barclays and Marks & Spencer shares (UK FTSE 100); NASDAQ and NYSE indices
- **Venue:** not stated
- **Period:** not stated (only relative lengths of 1000 training days and 500 test days are given, not calendar dates)
- **Granularity:** Daily closing prices

## Features and Measures

- **Directional Change (DC) event.** An event confirmed when price moves by a fixed threshold from the last confirmed price extreme, classified as an upturn or downturn event.
- **Overshoot (OS) event.** The phase following a confirmed DC event, lasting until the next opposite DC event is confirmed; combined with the preceding DC event it forms a downward or upward 'run'.
- **GP multi-threshold boolean indicator.** A tree-structured boolean expression, evolved by genetic programming, that combines the current up/down output of several randomly chosen DC thresholds (as terminal nodes) via AND, OR, NOR, XOR and NOT functions into a single buy/sell decision.

## Method

A tree-based genetic programming algorithm evolves populations of boolean expressions whose terminal nodes are randomly generated DC thresholds (each outputting true for an upturn/overshoot-up event and false for a downturn/overshoot-down event) and whose internal nodes are boolean functions (AND, OR, NOR, XOR, NOT). Each individual's fitness is the profit it would have earned by buying or selling one stock at each point of the training period according to its boolean output, subject to available cash and stock balance; fitness equals ending cash plus stock balance valued at the last price. The GP is run with tree depth up to 8, population size 300, for 300 generations, repeated 30 times per dataset, and the reported training fitness is the average over these runs. For comparison, a set of fixed DC thresholds is also evaluated on the training data, and the single fixed threshold with the highest training profit is selected per dataset as the benchmark. Both the GP-evolved strategies and the chosen fixed threshold are then evaluated once on a separate 500-day test period, with GP test results reported as the average profit over the 30 runs.

## Results

- In the test period, GP-evolved strategies produced higher profit than the best fixed DC threshold on all four datasets: 3,663.47 versus 3,007.55 for Barclays, 150,832.33 versus 149,501.30 for Marks & Spencer, 262,344.39 versus 254,450.72 for NASDAQ, and 1,073,190.19 versus 1,048,095.45 for NYSE.
- Relative to the initial budget, the GP strategies increased profit by 163.47 units (4.67%) for Barclays, 832.33 units (0.55%) for Marks & Spencer, 12,344.39 units (4.93%) for NASDAQ, and 73,109.19 units (7.31%) for NYSE.
- GP produced a profit on all 4 test datasets, whereas the best fixed DC threshold produced losses on Barclays and Marks & Spencer in the test period.
- In training, GP-found strategies achieved higher fitness (profit) than any single fixed threshold across all four markets, and fitness improved over the 300 generations.
- The GP algorithm was run 30 times per dataset; fixed thresholds, being deterministic, were run once per dataset.

## Limitations

- Only 4 datasets are tested (two individual stocks and two market indices), all using daily closing prices from a single unspecified historical period.
- The fixed-threshold benchmark is selected as the single best-in-training threshold from a predefined candidate list, which the authors themselves note may favor the GP comparison.
- Authors state the current GP does not exploit Overshoot (OS) events, and each trading decision is limited to one unit of stock per action.
- Reader note: no statistical significance test or confidence interval is reported for the profit differences between GP and fixed-threshold strategies.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/directional-change|Directional Change]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Jeremie Gypteau, Fernando E. B. Otero, Michael Kampouridis (2015). Generating Directional Change Based Trading Strategies with Genetic Programming. 18th European Conference on Applications of Evolutionary Computation, EvoStar 2015.

DOI: 10.1007/978-3-319-16549-3_22

Text ingested: `markdown_output/gypteau-2015-generating-directional-change-based-trading-strategies.md`, converted from `raw/ofi-event-clock/gypteau-2015-generating-directional-change-based-trading-strategies.pdf`.

Coverage of this summary: Read the entire converted markdown file, including the repository cover page, abstract, related work, the Directional Changes and GP-strategy sections, the experiments and results, and the conclusion.

Known problems with the input: OCR/conversion artifacts appear in mathematical notation and pseudocode (e.g. superscripted variable names, spaced-out symbols), so exact pseudocode and fitness-formula rendering could not be fully verified from the text alone; the picture showing the fitness formula itself was omitted from conversion; Monetary units for profit and budget figures are described only as 'monetary units' in the text, without a named currency.
<!-- AUTHORED REGION END -->