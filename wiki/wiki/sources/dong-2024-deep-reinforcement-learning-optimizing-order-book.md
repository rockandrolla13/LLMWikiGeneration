---
authors:
- Boyang Dong
- Daiyang Zhang
- Jing Xin
content_hash: sha256:9432bb143377ef1737bcecb1438a57c8e06dded3edd3811a34d51baf75590c0f
created: 2026-09-27 01:47:00+00:00
page_id: sources/dong-2024-deep-reinforcement-learning-optimizing-order-book
page_type: source
publication_venue: Computing Innovations and Applications
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/limit-order-book
- concepts/market-making
revision_id: 1
schema_version: 2
source_hash: sha256:d489062251599abc6ccf9fef2a5579817088a9fa7a0c48e47394fd8b34f0aa4b
source_path: markdown_output/dong-2024-deep-reinforcement-learning-optimizing-order-book.md
source_type: paper
tags:
- high-frequency-trading
- order-book-imbalance
- deep-reinforcement-learning
- deep-q-network
- backtesting
- equity-trading
- clock-calendar
- asset-equity
- harvest-relevant
title: Deep Reinforcement Learning for Optimizing Order Book Imbalance-Based High-Frequency
  Trading Strategies
updated: '2026-09-27T01:47:00Z'
uuid: 4ea080d7-a507-5a7f-8a55-fcabc28bde59
year: 2024
---

<!-- AUTHORED REGION START -->
# Deep Reinforcement Learning for Optimizing Order Book Imbalance-Based High-Frequency Trading Strategies

## Summary

The paper's stated question is whether order book imbalance (the difference between buy- and sell-side volumes at the best price levels) can be built into a deep reinforcement learning (DRL) agent to make better high-frequency trading decisions than fixed rule-based or statistical strategies, and how such an agent performs across different DRL choices and market conditions. The approach frames trading as a Markov Decision Process: at each step a state vector is built from the order-book imbalance ratio, the bid-ask spread, the volume at the best bid and best ask, a short-term price trend, and a rolling average of historical imbalance; a Deep Q-Network (DQN) with three hidden layers then estimates the value of a buy, sell, or hold action from that state, and the network is trained with an experience replay buffer and a periodically updated target network.

The method is tested on one year of tick-level AAPL order book data from NASDAQ, sampled at one-second intervals using the top order-book levels. The trained agent is compared against three fixed benchmarks: a moving-average crossover rule, a market-making strategy that quotes both sides of the book, and a random buy/sell/hold baseline, using cumulative return, Sharpe ratio, maximum drawdown, and the Calmar ratio as the performance measures.

The reported finding is that the DQN agent produced a higher cumulative return and Sharpe ratio, and a smaller maximum drawdown, than all three benchmarks over the test period. The authors frame the contribution as showing that order-book imbalance can be embedded directly into a DRL agent's state rather than used only in a static rule, and they present the result as a reproducible template for further DRL-based trading work.

Input problems: the converted markdown contains leftover text describing how the document itself was generated in word-count-limited chunks 'emulating the style of IEEE reference papers,' which raises doubt about whether this is an independently authored, peer-reviewed experimental study rather than templated or synthetic text; the numeric results below are reported exactly as printed but should be treated with caution given this.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order book state is sampled at fixed one-second wall-clock intervals from the top order-book levels, rather than per event or per trade. The state also includes a short-term price trend computed as the mean price change over the prior 10 one-second steps and a 5-minute rolling average of the imbalance ratio. The agent acts once per one-second step, with each simulated trading day represented as 10,000 steps, and is evaluated over a full one-year backtest rather than a single fixed short horizon.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL (Apple Inc.)
- **Venue:** NASDAQ
- **Period:** 1 January 2022 to 31 December 2022 (12 months)
- **Granularity:** Order book snapshots at 1-second intervals, using the top 10 bid and ask levels

## Features and Measures

- **Order book imbalance ratio.** The difference between cumulative bid and ask volumes across the top n price levels, divided by their sum; the paper sets n = 5 as a balance between capturing enough depth and avoiding noise.
- **Bid-ask spread.** The difference between the best ask price and the best bid price, used as a proxy for how liquid the market currently is.
- **Volume at best bid / best ask.** The total resting volume at the best bid and at the best ask price, used to capture immediate buying and selling pressure.
- **Short-term price trend.** The average price change over the previous 10 time steps, included in the state vector to capture recent momentum.
- **Historical imbalance.** A 5-minute rolling average of the imbalance ratio, included in the state vector to capture whether an imbalance signal is persistent rather than momentary.

## Method

Trading is modelled as a Markov Decision Process. At each one-second step the agent observes a 6-feature state vector (imbalance, spread, best-bid volume, best-ask volume, short-term price trend, historical imbalance) and a Deep Q-Network estimates the value of three possible actions: buy, sell, or hold. The network has an input layer for the 6-feature state, three fully connected hidden layers of 128, 64, and 32 ReLU-activated units, and an output layer producing one Q-value per action. Training uses an experience replay buffer holding 100,000 past transitions and a separate target network updated every 1000 steps for stability; hyperparameters (a learning rate of 0.001, a discount factor of 0.99, and a batch size of 64) were chosen by grid search. The agent trains for 200 episodes of 10,000 steps each (approximating one trading day per episode), using an epsilon-greedy exploration policy that decays from 1.0 to 0.01 over the first 50 episodes.

Performance is judged against three benchmark strategies (a 50/200-period moving-average crossover, a two-sided market-making strategy, and a random action baseline) using cumulative return, Sharpe ratio, maximum drawdown, and the Calmar ratio (return divided by maximum drawdown), computed over the same one-year backtest period.

## Results

- The DQN strategy's cumulative return was 15.2%, versus 8.5% for the moving-average crossover, 10.3% for market-making, and -2.1% for random trading.
- The DQN strategy's Sharpe ratio was 1.8, versus 1.2, 1.4, and -0.3 for the three benchmarks respectively.
- Maximum drawdown for the DQN strategy was 5.3%, lower than 7.8% (moving average), 6.5% (market-making), and 12.4% (random trading).
- The Calmar ratio for the DQN strategy was 2.9, versus 1.1, 1.6, and -0.2 for the three benchmarks.
- A simulated $10,000 starting portfolio was reported to grow to $11,520 under the DQN strategy, versus $10,850 and $11,030 under the moving-average and market-making strategies, while the random-trading baseline fell to $9,790.
- The imbalance feature was computed over the top 5 bid/ask levels (n = 5), which the authors say balances information depth against noise.

## Limitations

- The study tests only a single instrument (AAPL) over a single 12-month period, so the authors say behavioural differences in liquidity, volatility, and microstructure across other instruments remain unaddressed.
- The backtest assumes a frictionless market: transaction costs, slippage, and market impact were excluded, which the authors say may inflate the reported performance.
- Training required a high-performance GPU cluster, which the authors flag as a potential barrier to smaller users or individual practitioners.
- Hyperparameters and the DQN architecture were selected via a grid search over a limited space; the authors suggest alternative algorithms such as Proximal Policy Optimization might perform better.
- External factors such as regulatory changes or market interventions are not modelled.
- Reader note: the source markdown contains leftover generation instructions describing the text being produced in ~500-word chunks 'emulating the style of IEEE reference papers' to hit a word-count target, and contains two broken cross-references; this casts doubt on whether the reported figures come from an independently run, genuine experiment, and they could not be independently verified from the method description alone.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-making|market making]]

## Citation

Boyang Dong, Daiyang Zhang, Jing Xin (2024). Deep Reinforcement Learning for Optimizing Order Book Imbalance-Based High-Frequency Trading Strategies. Computing Innovations and Applications.

DOI: 10.63575/cia.2024.20204

Text ingested: `markdown_output/dong-2024-deep-reinforcement-learning-optimizing-order-book.md`, converted from `raw/ofi-event-clock/dong-2024-deep-reinforcement-learning-optimizing-order-book.pdf`.

Coverage of this summary: Read the whole converted markdown: abstract, introduction (research background, questions and objectives), literature review, the methodology section covering feature extraction and state representation and the DQN architecture, the experimental setup and dataset description, the results and benchmark comparison section, the conclusions, limitations, and future work sections, and all five tables.

Known problems with the input: The markdown contains text that appears to be leaked generation instructions rather than authored prose, e.g. a passage stating the section was written 'in two parts' to hit 'the requirement of splitting the 1000-word target into two parts' and 'emulating the style of IEEE reference papers.' This strongly suggests the document was produced by an LLM from a prompt rather than being a conventional peer-reviewed research paper, so its dataset and performance claims are reported here as printed but should be treated with strong scepticism; Two instances of a broken Word cross-reference ('Error! Reference source not found.') appear in the converted text, consistent with a corrupted source document; The acknowledgments section thanks other unrelated papers on fraud detection and financial risk monitoring in a way that reads as generic/templated rather than paper-specific.
<!-- AUTHORED REGION END -->