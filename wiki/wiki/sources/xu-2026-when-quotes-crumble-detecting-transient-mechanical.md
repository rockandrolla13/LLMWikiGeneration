---
authors:
- Haohan Xu
- Jason Bohne
- Paweł Polak
- Yurij Baransky
- Ajay Alva
- Violetta Fedotova
- Gary Kazantsev
- David Rosenberg
content_hash: sha256:4aeded68bc3ad877e0c2beb55e8a72a5422d4ddcc21e655436c810c58dd93b23
created: 2026-09-27 01:47:00+00:00
page_id: sources/xu-2026-when-quotes-crumble-detecting-transient-mechanical
page_type: source
publication_venue: ICLR 2026 Workshop on Advances in Financial AI
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/adverse-selection
- concepts/high-frequency-trading
- concepts/order-flow
- concepts/hawkes-processes
- concepts/informed-trading
- concepts/market-making
revision_id: 1
schema_version: 2
source_hash: sha256:37c5f8ee977031e21b2c061de9373e6491142e89a6d848765a180912b5c19cdc
source_path: markdown_output/xu-2026-when-quotes-crumble-detecting-transient-mechanical.md
source_type: paper
tags:
- limit-order-book
- market-microstructure
- agent-based-simulation
- liquidity-detection
- crumbling-quotes
- neural-labeling
- high-frequency-trading
- clock-event
- asset-simulated
- harvest-relevant
title: 'When Quotes Crumble: Detecting Transient Mechanical Liquidity Erosion in Limit
  Order Books'
updated: '2026-09-27T01:47:00Z'
uuid: 606091ee-00fd-5382-a0ed-f4ced9b4067f
year: 2026
---

<!-- AUTHORED REGION START -->
# When Quotes Crumble: Detecting Transient Mechanical Liquidity Erosion in Limit Order Books

## Summary

The paper addresses a measurement problem: short-horizon deterioration of the best bid or ask in a limit order book can come from two different causes that look alike in the data but mean different things for execution. One cause is mechanical removal of displayed liquidity while the underlying value is unchanged; the other is genuine repricing on new information. Real exchange feeds do not reveal which cause produced a given quote move, so any rule built directly on historical data cannot be checked against a known answer.

The authors sidestep this by building their detection and labeling method inside an agent-based market simulator (ABIDES) rather than on real exchange data. They add a regime-switching mechanism to the simulated market maker's quoting policy that biases quoting toward one side of the book for a fixed window, which mechanically withdraws liquidity from that side for a known, side-specific interval; because this is the market maker's own internal state, the start and end of each withdrawal episode is directly observable as ground truth. On top of this they define candidate crumbling events purely from order book quantities (best-quote deterioration steps consistent with depletion of the visible queue, clustered into events), then apply hard, interpretable filters based on order book volume accounting, a smoothed microprice proxy, opposite-side stability, and price reversion to exclude events that look like informational repricing rather than mechanical withdrawal. Events that pass these filters get event-level severity and recovery features, which a small feedforward neural network turns into a continuous, calibrated probability of true crumbling, trained against the simulator's ground truth with a cross-entropy objective.

Across the baseline simulated market and three stressed variants (bull, bear, high volatility), the neural model separates true crumbling episodes from other quote deterioration better than both a simple rule-based detector and a logistic regression baseline, though the advantage narrows under high volatility. Replacing the memoryless regime-switching process with a clustered, self-exciting (Hawkes) process shows the model's output probabilities track the clustering of true crumbling intervals, and adding features describing recent event history further improves discrimination.

What is new is the combination: manufacturing ground truth for a labeling problem that has no ground truth in real markets by using an agent-based simulator, then chaining an interpretable, mechanics-based hard-filter stage with a learned, calibrated probabilistic stage instead of relying on either alone.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are limit order book update events inside a nanosecond-resolution discrete-event market simulator. A deterioration step is flagged at each LOB update time where the best bid or ask worsens by at least one tick; candidate crumbling events are formed by clustering consecutive depletion-consistent deterioration steps within a maximum time gap, subject to a maximum event duration and a minimum number of steps. There is no fixed prediction horizon in the usual sense: each detected event is itself the unit of prediction, classified as mechanically driven crumbling or not using features measured over pre-event, event, and post-event windows.

## Data

- **Asset class:** Simulated data
- **Instruments:** a single simulated equity-like instrument traded in the ABIDES agent-based market simulator
- **Venue:** not stated (agent-based simulator with NASDAQ-style messaging, not a real exchange)
- **Period:** five consecutive simulated trading sessions, 9:30 AM to 4:00 PM ET
- **Granularity:** nanosecond-resolution discrete-event limit order book messages and depth

## Features and Measures

- **walk depth.** How many ticks the best quote on the affected side moves from just before to just after a candidate crumbling event.
- **depletion speed.** Volume removed at the affected price level during the event divided by the event's duration, measuring how fast the queue is exhausted.
- **refill ratio.** Volume added back at the crumbled price level during a short refill window after the event, relative to the volume removed during the event.
- **spread response.** The rise in the bid-ask spread from its pre-event median level to its maximum level during and shortly after the event.
- **efficient-price displacement.** The change in a smoothed microprice benchmark from before the event to after a post-event observation window, used to check whether the event coincided with a genuine change in value.
- **impact decay.** One minus the reversion ratio: how little of the price move that occurred during the event has reverted by the end of a post-event reversion window.
- **recovery interval.** Time since the end of the nearest preceding nearby crumbling event, capturing how much time the market has had to replenish liquidity before the current event.
- **recent event count.** The number of crumbling events recorded in a trailing lookback window before the current event, used to flag persistent rather than isolated liquidity stress.
- **cumulative depletion.** The sum of depletion speed across recent events in the lookback window, used to capture sustained order flow imbalance rather than a single spike.

## Method

The market is simulated in ABIDES, an agent-based limit order book simulator with nanosecond discrete-event scheduling. It combines zero-intelligence noise, value, and volatility agents with strategic momentum agents and an adaptive market maker; the market maker's quoting is perturbed by a stochastic regime-switching skew parameter that biases liquidity provision to one side for a fixed window, giving directly observable, agent-level ground truth for when and on which side liquidity is being mechanically withdrawn.

Candidate crumbling events are built purely from limit order book quantities: consecutive best-quote deterioration steps consistent with depletion of the visible queue are clustered into events, then event-level hard filters (book-volume accounting, a smoothed efficient-price/microprice proxy, opposite-side quote stability, and price reversion after the event) remove cases that look like informational repricing rather than mechanical withdrawal. Events passing these filters receive a binary label plus severity and recovery features. A small feedforward neural network (three layers, hidden dimensions [64, 32], with layer normalization, GELU activations and dropout) maps these features, plus three features describing recent event history, to a probability of true crumbling. It is trained with a binary cross-entropy (KL divergence) objective against the simulator's ground truth regime labels, with its output gated by the hard filters.

Performance is judged by ROC curves and AUC against the simulated ground truth, comparing the neural model to the hard-filter binary rule and to a logistic regression baseline, separately across four simulated market regimes (baseline, bull, bear, high volatility) and under an alternative, self-exciting (Hawkes) regime-switching process used to test robustness to the assumed temporal dependence of crumbling episodes.

## Results

- In the baseline simulated regime, the rule-based binary detector reaches an AUC of 0.67 against ground truth, logistic regression reaches 0.84, and the neural continuous labeling model reaches 0.91.
- The neural model gives about a +36% AUC improvement over rule-based baselines overall.
- The same ranking (binary rule worst, logistic regression better, neural model best) holds in bull, bear, and high-volatility simulated regimes, though the gap to the binary rule narrows in the high-volatility regime.
- When the market maker's crumbling regime is driven by a self-exciting (Hawkes) process instead of memoryless switching, the neural model's output probabilities rise and stay elevated during clustered periods that correspond to ground-truth crumbling intervals.
- Adding three features describing recent event history (recovery interval, recent event count, cumulative depletion) improves discrimination further over the neural model that uses only single-event features.

## Limitations

- Ground truth exists only inside the ABIDES simulator, via the market maker's internal regime state; the detector is not tested on real exchange data.
- The hard-filter thresholds that gate the neural labels are fixed by the authors rather than learned or calibrated against real markets.
- The work explicitly does not study why crumbling occurs in real markets, only how to measure and label it once it is defined in the simulator.
- Reader note: results come from a single simulated instrument and a specific simulated agent population, so generalization to real, multi-instrument order flow (including bonds) is untested.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow|order flow]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/market-making|market making]]

## Citation

Haohan Xu, Jason Bohne, Paweł Polak, Yurij Baransky, Ajay Alva, Violetta Fedotova, Gary Kazantsev, David Rosenberg (2026). When Quotes Crumble: Detecting Transient Mechanical Liquidity Erosion in Limit Order Books. ICLR 2026 Workshop on Advances in Financial AI.

DOI: 10.48550/arxiv.2604.21993

Text ingested: `markdown_output/xu-2026-when-quotes-crumble-detecting-transient-mechanical.md`, converted from `raw/ofi-event-clock/xu-2026-when-quotes-crumble-detecting-transient-mechanical.pdf`.

Coverage of this summary: Read the entire paper markdown (10 pages): abstract, introduction, simulator and ground-truth regime construction, crumbling quotes definition, detection pipeline, neural continuous labeling section, and the experiments/results section including the temporal-dependence ablation.

Known problems with the input: Several equations are rendered as omitted pictures or with mangled subscripts/exponents in the markdown conversion, so exact formula notation could not be transcribed; the surrounding prose was used instead.
<!-- AUTHORED REGION END -->