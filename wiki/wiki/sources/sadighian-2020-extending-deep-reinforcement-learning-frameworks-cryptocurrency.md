---
authors:
- Jonathan Sadighian
content_hash: sha256:a2d2b1d62a5b53126595c74f45c71b39f8a36beca83a54368a148c185f571136
created: 2026-09-27 01:47:00+00:00
page_id: sources/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency
page_type: source
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/market-making
- concepts/high-frequency-trading
- concepts/deep-learning-for-finance
- concepts/order-flow-imbalance
- concepts/intrinsic-time
revision_id: 1
schema_version: 2
source_hash: sha256:428d0360582125c30136e42e2bbbfca7935adb6157c702a0abf207ed2c7a102f
source_path: markdown_output/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency.md
source_type: paper
tags:
- reinforcement-learning
- market-making
- cryptocurrency
- limit-order-book
- event-driven-clock
- reward-function
- actor-critic
- clock-compares
- asset-crypto
- harvest-relevant
title: Extending Deep Reinforcement Learning Frameworks in Cryptocurrency Market Making
updated: '2026-09-27T01:47:00Z'
uuid: 99504e11-2494-569a-8490-b1d5e1641114
year: 2020
---

<!-- AUTHORED REGION START -->
# Extending Deep Reinforcement Learning Frameworks in Cryptocurrency Market Making

## Summary

The paper asks how the choice of reward function and the choice of event clock affect a deep reinforcement learning market-making agent trading Bitcoin perpetual futures. It builds on the author's earlier DRLMM framework, which stepped an agent through a limit order book environment at fixed one-second intervals, and adds a second option: stepping the agent only when the midpoint price moves beyond a small threshold, so the agent reacts to price moves rather than to the clock.

Two policy-based actor-critic algorithms, A2C and Proximal Policy Optimization, are trained on one-second limit order book snapshots from Bitmex, using an observation space built from order book quantities, order and trade flow imbalances, and several hand-crafted indicators. Seven reward functions are compared, grouped into profit-and-loss based, goal-based, and risk-based signals, together with six combinations of input features, under both the time-based and the price-based event environments.

The main finding is that neither event scheme nor reward function dominates outright, but a goal-oriented reward that grants a bounded reward for closing a trade at a target profit-to-loss ratio produced the best single result, and price-based events made learning easier overall, producing profitable outcomes in more of the tested configurations than time-based events. A large, sudden Bitcoin sell-off during the test period caused losses across essentially every configuration, showing the sensitivity of these agents to abrupt price shocks.

What is new relative to the author's prior work is the systematic comparison across seven reward functions (versus two previously) and the introduction of the price-based event environment as an alternative to sampling the limit order book on a fixed clock.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper compares two ways of stepping an agent through the same underlying one-second limit order book snapshots: a time-based environment that reacts every second, and a price-based environment that reacts only when the midpoint price has moved by more than a threshold (0.01%) from the last event. There is no separate multi-step-ahead forecast target; the agent instead takes an action at each event and is judged on the cumulative return realized by end of each 24-hour trading-day episode over the out-of-sample test period.

## Data

- **Asset class:** Crypto
- **Instruments:** Bitcoin perpetual futures (XBTUSD)
- **Venue:** Bitmex
- **Period:** Training: December 27, 2019 to January 3, 2020 (8 days). Testing: January 4 to February 3, 2020 (30 days).
- **Granularity:** One-second limit order book snapshots (first 20 price levels per side), further down-sampled to price-change events in the price-based environment.

## Features and Measures

- **LOB Quantity.** The dollar value resting at each of the first 20 bid and ask price levels of the limit order book.
- **LOB Imbalances.** A per-level order imbalance built from the cumulative dollar value on the bid versus ask side of the book at each of the first 20 levels.
- **Order Flow.** The summed dollar value of cancel, limit and market orders arriving between consecutive limit order book snapshots, tracked separately for bid and ask sides.
- **Trade Flow Imbalance.** A measure of the relative size of buyer-initiated versus seller-initiated trades over rolling 5-, 15- and 30-minute windows.
- **Custom RSI.** A relative-strength-index-style indicator of price-change magnitude computed over rolling 5-, 15- and 30-minute windows, scaled to avoid needing separate normalization.
- **Spread and change in midpoint.** Scalar features giving the current best bid-ask spread and the change in the limit order book midpoint price between consecutive steps.

## Method

Two policy-based, model-free actor-critic algorithms, A2C and PPO, are trained using a shared multilayer perceptron feature extractor with separate actor and critic heads, implemented with the Stable Baselines library. The agent's action space has 17 discrete actions covering no action, symmetric and skewed limit-order quoting at different book levels, and a full-inventory-flattening market order. Seven reward functions are tested, spanning profit-and-loss based signals (unrealized PnL, unrealized PnL with realized fills, two asymmetrically dampened variants, and change in realized PnL), a goal-based trade-completion signal, and a risk-based differential Sharpe ratio, each combined with six different feature-set combinations for the observation space.

Agents are trained for one million environment steps per configuration and evaluated out-of-sample on cumulative return, including transaction costs, against a buy-and-hold Bitcoin benchmark. The simulation enforces maker/taker transaction fees, a maximum inventory of ten open positions, FIFO netting of realized gains and losses, and a fixed slippage percentage applied when the agent liquidates its full inventory at the end of each trading-day episode.

## Results

- The buy-and-hold Bitcoin benchmark returned 16.25% over the 30 out-of-sample trading days used for evaluation.
- The best-performing configuration reached a 17.61% return, using the goal-based Trade Completion reward, the A2C algorithm, and feature Set 3.
- Only 15 of 84 time-based-event experiment configurations were profitable, versus 23 of 84 for the price-based-event configurations.
- A2C outperformed PPO on both cumulative return and the number of profitable configurations.
- On January 19, 2020 Bitcoin fell more than 5% in under 200 seconds, and every experiment configuration lost between 5% and 10% on that trading day.
- A dampening factor of 0.35 in the asymmetrical PnL-with-fills reward gave the most stable out-of-sample performance in a grid search.
- PnL-based rewards that ignore realized gains led to frequent market-order use and short holding periods, while sparse rewards led to prolonged, speculative position holding.

## Limitations

- Tested on a single instrument (Bitcoin perpetual futures) on a single exchange (Bitmex), unlike the multi-currency-pair generalization tests in the author's prior work.
- The 8-day training / 30-day testing split was chosen for data availability rather than chosen empirically, as the authors state.
- Reader note: the 30-day out-of-sample window covers one specific, unusually strong up-trending month for Bitcoin, which limits how far the return figures generalize to other market regimes.
- Reader note: no repeated-seed or statistical-significance testing is reported across the 84 experiment configurations per environment.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-making|market making]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/intrinsic-time|Intrinsic Time]]

## Citation

Jonathan Sadighian (2020). Extending Deep Reinforcement Learning Frameworks in Cryptocurrency Market Making.

DOI: 10.48550/arxiv.2004.06985

Text ingested: `markdown_output/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency.md`, converted from `raw/ofi-event-clock/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency.pdf`.

Coverage of this summary: Read the full paper end to end, including the abstract, all numbered sections, the results tables, the conclusion, and the appendix describing the observation space and hyperparameters.

Known problems with the input: No journal or conference venue is printed on this paper (it presents as a working paper/preprint with no series name); venue recorded as not stated; Several equations and figures are rendered as omitted pictures in the markdown conversion, so some formula details could not be verified beyond the surrounding prose.
<!-- AUTHORED REGION END -->