---
authors:
- Qi Zhao
content_hash: sha256:5087760fa7e6c483466ab9a823b1f60e39c97c10798493216007dc7929588942
created: 2026-09-27 01:47:00+00:00
page_id: sources/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time
page_type: source
publication_venue: Centre for Computational Finance and Economic Agents (CCFEA), University
  of Essex (PhD thesis)
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/high-frequency-data
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/overfitting-backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:d26e412f6d085028aebc285e78ed1d2815455decdd5e6dd43f69f41d11ee47f6
source_path: markdown_output/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time.md
source_type: paper
tags:
- directional-change
- intrinsic-time
- fx-trading
- reinforcement-learning
- overshoot-prediction
- trend-following
- phd-thesis
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Novel Trading Algorithms augmented by Intrinsic Time and Machine Learning
updated: '2026-09-27T01:47:00Z'
uuid: 21cb91dd-3cad-55c6-b3f7-cdfa1119d493
year: 2026
---

<!-- AUTHORED REGION START -->
# Novel Trading Algorithms augmented by Intrinsic Time and Machine Learning

## Summary

The thesis is organized around the Directional Change (DC) framework, which samples price series on an event-driven 'intrinsic time' clock: instead of fixed calendar intervals, a new observation is recorded only when price reverses by at least a preset threshold from its last extreme. Each such trend segment splits into a Directional Change (DC) event, which marks the reversal itself, and an Overshoot (OS) event, the continuation that follows it. The central question across three linked research chapters is whether this event-based representation of FX price dynamics can be turned into profitable, risk-controlled trading strategies, first on its own, then combined with supervised machine learning, then combined with reinforcement learning.

Chapter 3 builds two DC-based strategies -- trend-following (DC-TF) and counter-trend (DC-CT) -- directly from documented DC/OS scaling-law relationships, and adds a DC-derived dynamic stop-loss. Chapter 4 uses five machine-learning classifiers (Random Forest, SVM, ANN, LSTM, CNN), trained on lagged DC/OS event statistics, to predict the type or length of the next overshoot event and use that prediction to size DC-TF positions. Chapter 5 replaces this simpler prediction layer with a reinforcement-learning agent: a ResNet-style policy network observes a multi-threshold DC-based state and learns, via a two-part reward and CPU-parallel training, how much to size each DC-TF trade.

Across all three chapters the trend-following variant of the DC strategy is the more profitable but riskier one, and each successive layer (stop-loss, then ML, then RL) trades some raw profit for better risk-adjusted or more consistent performance. The reinforcement-learning strategy is reported as the strongest of the three approaches on out-of-sample data, generating positive returns on every tested currency pair.

The thesis frames its contribution as demonstrating that the DC/intrinsic-time framework is a viable foundation for combining event-driven market representation with machine learning and reinforcement learning, rather than claiming any single strategy variant has universal superiority; it repeatedly stresses that all findings are drawn from FX data over a specific historical window and specific thresholds.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Time only advances ('ticks') when price moves by at least a preset percentage threshold θDC from the most recent local extreme; each tick alternates between a Directional Change (DC) event, marking the reversal, and an Overshoot (OS) event, the continuation of the trend until the next reversal. Trading and prediction horizons are defined in these event units (e.g. a position exits at the next DC confirmation, or once price has moved θDC further, or after twice the average DC event duration) rather than in fixed calendar time, and the underlying minute-level FX price series is converted into this event sequence before any strategy, ML or RL step is applied.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** Eight FX currency pairs: AUD/NZD, EUR/GBP, EUR/JPY, EUR/USD, USD/CAD, USD/CHF, USD/JPY, NZD/JPY
- **Venue:** not stated (over-the-counter FX market; minute-level data obtained from histdata.com)
- **Period:** January 2006 to December 2020 overall; Chapter 3 backtests 2006-2014; Chapters 4 and 5 train on 2006-2016 and test out-of-sample on 2017-2020
- **Granularity:** Minute-level FX midprices, converted into event-based Directional Change / Overshoot sequences

## Features and Measures

- **Directional Change (DC) event.** A recorded price reversal of at least a preset threshold θDC from the most recent extreme (peak in an uptrend, trough in a downtrend), used to mark trend confirmation points and as the 'tick' of intrinsic time.
- **Overshoot (OS) event / Overshoot value (OSV).** The continuation of price beyond a DC confirmation point, ending at the next reversal; OSV expresses how far the current move has gone relative to the DC threshold.
- **DC-based dynamic stop-loss.** A stop-loss level and time limit derived from the average and standard deviation of past DC and OS event durations at the chosen θDC, rather than a fixed price distance or fixed time.
- **OS-event features for ML (SMA/WMA averages).** Simple and weighted moving averages of the previous 10 DC/OS events' length, duration, price and speed (rate of event), used as tabular inputs to Random Forest, SVM and ANN models to predict the type or length of the next overshoot.
- **DC-derived RL state and ResNet policy network.** A multi-threshold snapshot of recent DC/OS event statistics used as the state for a reinforcement-learning agent, processed by a residual convolutional neural network (ResNet) policy that decides position sizing at each DC-based trend-following entry.

## Method

Chapter 3 defines the DC-TF and DC-CT strategies directly from DC/OS scaling-law relationships, backtests them across eight currency pairs and a range of θDC values (2006-2014), evaluates them with annualized rate of return, maximum drawdown and Sharpe ratio, tests whether DC-TF's edge over DC-CT is statistically significant with a paired t-test, and then adds a DC-derived dynamic stop-loss to both strategies. Chapter 4 trains five machine-learning classifiers (Random Forest, SVM, ANN, LSTM, CNN) on lagged DC/OS event statistics (2006-2016) to predict the type/length of the next overshoot event, uses each model's prediction to scale DC-TF position size, and evaluates the resulting strategies out-of-sample (2017-2020) against a buy-and-hold benchmark using P&L and maximum drawdown. Chapter 5 replaces the ML sizing layer with a reinforcement-learning agent: a ResNet-based policy network observes a multi-scale DC-derived state, is trained with a two-component (short-term plus long-term) reward using a multi-core CPU-parallel experience-generation scheme, and is evaluated out-of-sample (2017-2020) against buy-and-hold, a moving-average strategy, and the best machine-learning strategy from Chapter 4.

## Results

- In an eight-currency-pair backtest from 2006 to 2014, the DC-based trend-following (DC-TF) strategy earned an average cumulative return of 39.74% versus 13.22% for the DC-based counter-trend (DC-CT) strategy, but with a larger average maximum drawdown (31.49% versus 11.67%).
- A paired t-test on 160 currency-pair/θDC combinations found DC-TF significantly outperformed DC-CT (t = 13.12, p < 0.0001), though the average edge per observation was modest (0.167 percentage points of annualized return).
- Adding a DC-based dynamic stop-loss cut average drawdown sharply (to 0.17% for DC-TF and 0.10% for DC-CT) and raised Sharpe ratios (to 3.61 and 3.09), but also cut average P&L (to 2.67% and 1.84%).
- Using five ML models to size DC-TF positions from 2017 to 2020, ANN gave the most consistent improvement (average P&L of 13.65% versus 8.49% for the unmodified strategy), while SVM tended to reduce profitability.
- The DC-based reinforcement-learning strategy achieved positive out-of-sample returns (2017-2020) on all eight currency pairs (average P&L 25.24%, average MDD 6.17%), versus 13.65% for the best ML strategy, 1.81% for a moving-average strategy, and -3.48% for buy-and-hold.
- The RL strategy's returns across currency pairs had a standard deviation of about 10.1% (a coefficient of variation of 0.40), which the author reads as evidence of reasonably stable, not pair-specific, performance.

## Limitations

- All empirical work is confined to eight FX currency pairs from 2006-2020; the author states results may not generalize to other asset classes, thresholds, or ML/RL architectures.
- DC thresholds (θDC) are fixed and chosen in advance rather than adapted to market conditions in real time.
- The RL environment simplifies real trading: transaction costs are modelled only as a fixed 0.3% commission, market impact and liquidity constraints are not modelled, and position sizing is the only action available to the agent.
- The machine-learning chapter's own conclusion states that overshoot-event prediction accuracy is 'suboptimal', i.e. the predictive power obtained from DC-derived features alone is limited.
- Reader note: this is a single-author PhD thesis rather than a peer-reviewed paper, and comparisons between the author's own strategy variants (e.g. DC-TF vs DC-CT, ML vs RL) are not checked against an independently designed benchmark strategy.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Qi Zhao (2026). Novel Trading Algorithms augmented by Intrinsic Time and Machine Learning. Centre for Computational Finance and Economic Agents (CCFEA), University of Essex (PhD thesis).

DOI: 10.5526/err-00043797

Text ingested: `markdown_output/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time.md`, converted from `raw/ofi-event-clock/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time.pdf`.

Coverage of this summary: Long PhD thesis: read the abstract, acknowledgements, table of contents, the full introduction (Chapter 1), the Directional Change/intrinsic-time/scaling-law and research-dataset sections of the literature review (2.2, 2.5), and for Chapters 3, 4 and 5 read the introduction, data/method sections and full results/analysis/conclusion sections; read Chapter 6 (overall conclusions, contributions, limitations, future work) in full. Did not read the ML/RL background subsections (2.3, 2.4) or the detailed mathematical derivation subsections of Chapter 5 (5.4.1-5.4.7) line by line.

Known problems with the input: year from file metadata (no explicit publication/submission year is printed in the thesis front matter; year taken from job file year_hint).
<!-- AUTHORED REGION END -->