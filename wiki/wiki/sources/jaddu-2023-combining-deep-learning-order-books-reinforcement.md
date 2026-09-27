---
authors:
- Koti S. Jaddu
- Paul A. Bilokon
content_hash: sha256:ab2041ba1dc0582fdc708867e84a6cd11f73ed8d5d2eb473f25b923b0e92fb42
created: 2026-09-27 01:47:00+00:00
page_id: sources/jaddu-2023-combining-deep-learning-order-books-reinforcement
page_type: source
related:
- concepts/event-clock
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/deep-learning-for-finance
- concepts/backtesting
- concepts/order-flow-prediction
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:a870d13a9f000ea5829674d930eaa79a7d4a2cfe1761f54a48b5fabc3dba25f7
source_path: markdown_output/jaddu-2023-combining-deep-learning-order-books-reinforcement.md
source_type: paper
tags:
- reinforcement-learning
- order-flow-imbalance
- deep-learning
- high-frequency-trading
- alpha-extraction
- backtesting
- forward-testing
- retail-trading
- clock-event
- asset-multi
- harvest-relevant
title: Combining Deep Learning on Order Books with Reinforcement Learning for Profitable
  Trading
updated: '2026-09-27T01:47:00Z'
uuid: ec3f4fb5-6044-5770-8284-3bb9b14c13c1
year: 2023
---

<!-- AUTHORED REGION START -->
# Combining Deep Learning on Order Books with Reinforcement Learning for Profitable Trading

## Summary

The thesis asks whether combining a deep-learning model that forecasts short-horizon returns from order flow imbalance with reinforcement-learning trading agents can produce a profitable, reproducible high-frequency trading system that a retail trader could realistically run, as an alternative to large end-to-end deep-learning trading models.

It reuses Kolm et al.'s multi-layer-perceptron alpha-extraction design, which predicts mid-price change over six future timesteps from order flow imbalance at the first ten book levels, and feeds the predicted returns into three temporal-difference reinforcement-learning agents from Bertermann's work: tabular Q Learning, Deep Q Network (DQN), and Double Deep Q Network (DDQN). Ten weeks of order-book data were collected from the CTrader FXPro retail platform for five instruments (GBPUSD, EURUSD, DE40, FTSE100 and XAUUSD), hyperparameters for both components were tuned by grid search, and the resulting 15 agent-instrument combinations were evaluated first through backtesting with retail transaction costs and then, for the most promising ones, through short live forward tests.

The alpha-extraction component reproduces Kolm et al.'s order of performance across asset classes and its out-of-sample R2 is of a similar small magnitude. Among the reinforcement-learning agents, Q Learning is the most profitable and least volatile in backtesting, ahead of DDQN and DQN, and using true historical alphas the combined system is statistically better than a random-action benchmark. However, once the agents are fed the model's own predicted alphas rather than true ones, most instrument-agent combinations become unprofitable, and even the best case (Q Learning on GBPUSD and EURUSD) turns unprofitable again in live forward testing, mainly because of processing latency that causes the agent to act on data that is no longer current.

The contribution is a lightweight, reproducible decomposition of an end-to-end deep-reinforcement-learning trading pipeline into a separately trained forecasting stage and a decision stage, evaluated specifically under retail trading costs and infrastructure rather than institutional conditions, together with a heatmap-based explanation of which return horizons drive each agent's decision to reverse a position.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are order-book snapshots taken whenever the observable limit-order-book state changes, i.e. one record per book update rather than per fixed time interval. The alpha-extraction model's prediction horizon is six discrete future timesteps (book updates) ahead, and the reinforcement-learning agents make a buy/sell decision at every such update, holding a single position until a reversal signal is generated.

## Data

- **Asset class:** Several asset classes
- **Instruments:** GBPUSD and EURUSD (foreign exchange pairs), DE40 and FTSE100 (equity indices), and XAUUSD (gold)
- **Venue:** CTrader FXPro retail trading platform
- **Period:** 23/5/2023 to 3/7/2023 and 25/7/2023 to 21/8/2023, with a gap from 4/7/2023 to 24/7/2023 due to a technical issue
- **Granularity:** irregular event time, one record per limit-order-book update, storing order flow imbalance at the first ten book levels and the mid-price

## Features and Measures

- **Order flow (OF).** The change in aggregated limit-order volume at a given book level between two consecutive order-book snapshots, separated into ask-side and bid-side components.
- **Order flow imbalance (OFI).** The difference between the ask-side and bid-side order flow at each of the first ten book levels, used as the network's input feature.
- **Alpha (return forecast).** The supervised model's predicted change in mid-price at each of six future timesteps, trained by regression on order flow imbalance.
- **Volume delta / cumulative volume delta.** The difference between aggregated bid and ask volumes at a snapshot, and its change across snapshots, described in the literature review as a simpler alternative order-book feature.

## Method

The alpha-extraction network is a multi-layer perceptron trained with ADAM and L2 regularisation to regress six-horizon mid-price changes onto order flow imbalance, using an 80% training, 10% validation, 10% test split, early stopping on a validation set, and a grid search over layer width, learning rate, batch size and patience. Its predicted or true alphas, together with the agent's current position, form the state fed to three separately trained temporal-difference agents: tabular Q Learning, DQN and DDQN, each tuned by grid search over exploration-rate decay, discount factor, network size, batch size and (for DQN/DDQN) target-network update frequency, with reward defined as the change in profit and loss at each step. Performance is judged first by backtesting on held-out historical data in a custom Gym-style environment that applies retail commissions and spreads, using metrics such as daily average profit, volatility, profit/loss ratio, profitability percentage and maximum drawdown, compared against a random-action benchmark with a Mann-Whitney U-test, and second by short forward tests that connect the trained agents to the live CTrader platform through a Flask web application.

## Results

- The tuned alpha-extraction models reach average out-of-sample R2 (as a percentage) of 0.045 for XAUUSD, 0.149 for GBPUSD, 0.132 for EURUSD, 0.206 for FTSE100 and 0.231 for DE40, close to the 0.181 average that Kolm et al. report for equities.
- Using true historical alphas in backtesting, Q Learning earned £8,030 total profit versus losses of £29,800 for DQN and £5,460 for DDQN, with Q Learning ranked best, then DDQN, then DQN.
- When agents were instead fed the alpha-extraction model's own predictions, performance fell across the board; only Q Learning on GBPUSD (£2,210 average daily profit) and EURUSD (an average daily loss of £120) stayed close to breakeven.
- A Mann-Whitney U-test comparing each trained agent's daily backtested profit to a random-action benchmark gave a U statistic of 0 for every agent, rejecting the null hypothesis that the trained agents are no better than random.
- One-hour live forward tests of Q Learning lost £2,400 on GBPUSD and £2,640 on EURUSD, a £240 larger loss, which the authors attribute mainly to processing latency causing the agent to act on stale order-book states.
- Q-value heatmaps show the first return horizon dominates the decision to reverse a position for most agents, which the authors link to the forward-testing losses since that first horizon often elapses before a live order can be placed.

## Limitations

- Only ten weeks of order flow imbalance data were collected per instrument, split 80% training, 10% validation and 10% testing.
- Forward testing was run for only one hour per instrument, so the live results rest on a very small sample.
- Reader note: the paper itself notes overlap between the data used to train the alpha-extraction model and the data used to train the reinforcement-learning agents on true alphas, which the authors say could make the alpha model look more accurate on data it has already seen.
- Data collection depended on a single retail broker's feed and a single VPS, so results may not transfer to other venues, brokers or execution latencies.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/backtesting|backtesting]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]

## Citation

Koti S. Jaddu, Paul A. Bilokon (2023). Combining Deep Learning on Order Books with Reinforcement Learning for Profitable Trading.

DOI: 10.2139/ssrn.4611708

Text ingested: `markdown_output/jaddu-2023-combining-deep-learning-order-books-reinforcement.md`, converted from `raw/ofi-event-clock/jaddu-2023-combining-deep-learning-order-books-reinforcement.pdf`.

Coverage of this summary: Read the whole paper end to end: abstract, background on supervised and reinforcement learning and limit order markets, the literature review, data collection and design sections, hyperparameter optimisation, the evaluation section (tuning, backtesting, benchmarking, forward testing, explainability), the conclusion, and the appendix tables of feature statistics.

Known problems with the input: Most mathematical formulas are shown as 'picture intentionally omitted' placeholders, so exact equations for order flow, OFI and the R2_OS metric could not be verified beyond the surrounding prose; OCR artifacts appear in table headers, e.g. 'Proft' for 'Profit', 'Proftability' for 'Profitability', and 'Confgurations' for 'Configurations'; these were not treated as content; The paper is styled as an arXiv-style preprint ('A PREPRINT') but its GitHub link is named 'MastersProject' and no journal or conference name is given, so it looks like a university project report rather than a peer-reviewed or archived preprint; venue is left blank; The paper states two different train/validation/test split ratios for the same pipeline (an 80/10/10 split described in Section 3.1.1 and a 7:1:2 ratio shown in Algorithm 4's pipeline steps); this inconsistency in the source could not be resolved from the text alone.
<!-- AUTHORED REGION END -->