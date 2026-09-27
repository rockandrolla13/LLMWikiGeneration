---
authors:
- Antonio Briola
- Jeremy Turiel
- Riccardo Marcaccioli
- Alvaro Cauderan
- Tomaso Aste
content_hash: sha256:f1ab453652f5d5921128b1fe5339365d7a882eeaef48a01c3a6a54273e54dae5
created: 2026-09-27 01:47:00+00:00
page_id: sources/briola-2021-deep-reinforcement-learning-active-high-frequency
page_type: source
related:
- concepts/event-clock
- concepts/high-frequency-trading
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/square-root-law
- entities/antonio-briola
- entities/jeremy-turiel
- entities/tomaso-aste
revision_id: 1
schema_version: 2
source_hash: sha256:261604ab7d60d38a242f98d95b90e36b7a5078ce53b2fbe345a9b85458bcea56
source_path: markdown_output/briola-2021-deep-reinforcement-learning-active-high-frequency.md
source_type: paper
tags:
- reinforcement-learning
- limit-order-book
- high-frequency-trading
- ppo
- market-microstructure
- single-asset-trading
- clock-event
- asset-equity
- harvest-relevant
title: Deep Reinforcement Learning for Active High Frequency Trading
updated: '2026-09-27T01:47:00Z'
uuid: 082a953a-3f83-5d51-a487-d6cf7389b52e
year: 2021
---

<!-- AUTHORED REGION START -->
# Deep Reinforcement Learning for Active High Frequency Trading

## Summary

The paper asks whether an end-to-end deep reinforcement learning (DRL) agent can learn a profitable single-asset high-frequency trading strategy directly from raw limit order book data, trading only one unit of stock at a time.

Its approach is a Proximal Policy Optimization (PPO) agent that chooses among sell/hold/buy/stop-loss actions at every order book update (tick time). Training uses a continual-learning scheme built from the day's largest price-swing windows, to raise the signal-to-noise ratio, with the learning rate and entropy coefficient tuned by Bayesian, sequential model-based optimization on a held-out validation month. Three state definitions are compared: a base state of recent order-book volumes and current position, a version that adds the mark-to-market value of any open position, and a version that further adds the current bid-ask spread.

All three state definitions produce net positive profit out of sample over a held-out test month. Adding the mark-to-market value is the single biggest driver of improvement, producing far more trades and much higher cumulative profit than the base state, while adding the spread on top does not help further for this large-tick stock.

What is new is positioning this as the first end-to-end DRL framework trained and evaluated on real (not simulated) high-frequency limit order book data for active trading, in contrast to prior DRL trading work that used daily data or simulated order books.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The agent observes the state and can act at every limit order book update (tick time), not on a fixed calendar clock; training samples are drawn from the periods of each day with the largest mid-price swings, and a trade's profit or loss (the reward) is only realized when a position is later closed, at whatever future tick that occurs.

## Data

- **Asset class:** Equities
- **Instruments:** Intel Corporation stock (INTC)
- **Venue:** NASDAQ (LOBSTER dataset)
- **Period:** training: 4 Feb 2019 to 30 Apr 2019; validation: 1 May 2019 to 31 May 2019; test: 3 Jun 2019 to 28 Jun 2019
- **Granularity:** tick-by-tick limit order book snapshots to a depth of 10 price levels per side (LOBSTER); an initial and final portion of each trading day is excluded from training and test data to avoid open/close volatility

## Features and Measures

- **State definitions Sc201/Sc202/Sc203.** Three versions of the agent's observed state: Sc201 uses only the last several ticks of 10-level bid/ask volumes plus current position; Sc202 adds the mark-to-market value of any open position; Sc203 further adds the current bid-ask spread.
- **Mark-to-market value.** The profit the agent would realize if it closed its current open position immediately, given to the agent as part of its state in Sc202 and Sc203.
- **Reward function.** The realized dollar profit or loss when a position is closed (the bid/ask price difference net of the spread paid), used as the agent's training reward for every action except the stop-loss.

## Method

The agent is trained with the Proximal Policy Optimization algorithm using a clipped surrogate objective (clip parameter $\epsilon=0.2$) to bound each policy update, with a simple two-hidden-layer (64 neurons each) multilayer perceptron shared between the actor and critic. Training uses a continual-learning setup: for each of the 82 available trading days, several candidate windows containing the day's largest mid-price swings are located, of which 25 in total are sampled across the dataset and turned into vectorized training environments, each run for 30 epochs. Hyperparameters (learning rate and entropy coefficient) are tuned on the validation month using Bayesian optimization with a Gaussian-process surrogate and the Expected Improvement acquisition function. The trained policy is then evaluated once, out of sample, on every day of the held-out test month, tracking cumulative daily profit, the mean and standard deviation of daily profit and loss across ensemble runs, and the distribution of individual trade returns.

## Results

- Agents under all three state definitions produced profitable strategies on average, net of trading costs (the spread paid to open and close each unit trade), across the test period.
- State Sc202 (adding mark-to-market value) reached cumulative profit an order of magnitude higher than the other two state definitions and executed roughly two orders of magnitude more trades than Sc201.
- State Sc203 (adding bid-ask spread on top of Sc202) outperformed Sc201 but underperformed Sc202, suggesting spread information added little because the spread is close to constant for this large-tick stock.
- Trade return distributions were broadly similar in shape across all three states -- positively skewed with a peak near zero -- differing mainly in trading frequency rather than in the quality of individual trades.
- Most test days showed positive average returns, and positive trade returns were larger on average than negative ones, across all state definitions.

## Limitations

- The reward is only received when a position closes, so feedback is sparse (positions are sometimes held for tens to thousands of ticks), which the authors say slows convergence.
- The agent sometimes converges to a degenerate policy of not trading at all, which the authors attribute to PPO's exploration behavior early in training.
- The agent trades only one unit of stock at a time, so the reported results ignore the price impact that trading larger size would create.
- Reader note: all results are for a single stock (INTC) over a three-month train/validation/test span, so generalization to other assets, tick sizes, or periods is untested.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/square-root-law|square root law]]
- [[entities/antonio-briola|Antonio Briola]]
- [[entities/jeremy-turiel|Jeremy Turiel]]
- [[entities/tomaso-aste|Tomaso Aste]]

## Citation

Antonio Briola, Jeremy Turiel, Riccardo Marcaccioli, Alvaro Cauderan, Tomaso Aste (2021). Deep Reinforcement Learning for Active High Frequency Trading.

DOI: 10.48550/arxiv.2101.07107

Text ingested: `markdown_output/briola-2021-deep-reinforcement-learning-active-high-frequency.md`, converted from `raw/ofi-event-clock/briola-2021-deep-reinforcement-learning-active-high-frequency.pdf`.

Coverage of this summary: Read the full markdown file: introduction, background (LOB and PPO), related work, data, models, training-test pipeline, results and discussion, limitations, and conclusion.

Known problems with the input: No publication year or venue name is printed in the visible text; used the job file's year_hint (2021) for year, and left venue not stated.
<!-- AUTHORED REGION END -->