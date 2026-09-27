---
authors:
- George Rayment
content_hash: sha256:c28467da525858478a131f7324eae82b6681af4196c3f9fd0bfa7a3c88f34485
created: 2026-09-27 01:47:00+00:00
page_id: sources/george-2025-deep-reinforcement-learning-trading-strategy-development
page_type: source
publication_venue: University of Essex (PhD thesis, School of Computer Science and
  Electronic Engineering)
related:
- concepts/sampling-clocks
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/bid-ask-spread
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:9fcb922d2b4dcecc4a5d59c80e9c80c65338e593a5cbc6ae115f0ecc3e6ded64
source_path: markdown_output/george-2025-deep-reinforcement-learning-trading-strategy-development.md
source_type: paper
tags:
- directional-change-sampling
- deep-reinforcement-learning
- foreign-exchange
- high-frequency-trading
- trading-agent
- bid-ask-spread
- backtesting
- clock-compares
- asset-fx
- harvest-relevant
title: Deep Reinforcement Learning for Trading Strategy Development on High-Frequency
  Currency Data Using Directional Changes Sampling
updated: '2026-09-27T01:47:00Z'
uuid: a262b8a3-7955-5e76-9d46-2225c22356d9
year: 2025
---

<!-- AUTHORED REGION START -->
# Deep Reinforcement Learning for Trading Strategy Development on High-Frequency Currency Data Using Directional Changes Sampling

## Summary

The thesis asks whether combining directional-change (DC) event-based sampling of foreign-exchange tick data with deep reinforcement learning (DRL) can produce more profitable high-frequency trading agents than fixed-interval technical-analysis benchmarks, and how the answer changes once transaction costs are modelled realistically as the bid-ask spread rather than as a fixed fee. It develops three successive frameworks, each trained per rolling window on tick data for 14 FX pairs sampled at eight DC thresholds. FDRL (Chapter 4) trains Proximal Policy Optimisation (PPO) agents on DC-derived indicators under a fixed transaction cost, using a rule-based filter that restricts trading to periods with no overshoot ('consolidation periods'). PADRL (Chapter 5) adds positional-awareness features (current position, running profit, potential return, spread) to the state so the agent no longer needs the hand-coded filter, at a higher fixed cost. SADRL (Chapter 6) replaces the fixed cost with the actual historical bid-ask spread, swaps the DC-specific indicators for traditional technical indicators computed on DC confirmation points plus a novel two-trend candlestick reframing of the DC data, and compares four DRL algorithms (DQN, A2C, PPO, TRPO).

The main finding is that FDRL and PADRL generate very large returns under fixed transaction-cost assumptions by exploiting rapid alternating buy/sell trades during low-volatility consolidation periods, but this strategy collapses once real bid-ask spreads are applied. SADRL, trained with TRPO under real spreads, instead learns a longer-holding, trend-following style of trading and significantly outperforms both FDRL, PADRL, and a set of technical-analysis benchmarks on risk-adjusted return once realistic costs are imposed, though it struggles when trends reverse. What is new relative to the literature reviewed in the thesis is applying deep (rather than tabular) reinforcement learning to DC-sampled high-frequency FX data, using positional-awareness state features to remove the need for a hand-coded trading filter, and combining a bid-ask-spread-aware DC candlestick reframing with a multi-algorithm (DQN/A2C/PPO/TRPO) comparison aimed at more realistic live-trading feasibility.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

All three frameworks sample raw FX tick data with the directional change (DC) algorithm: a threshold theta on percentage price change from the last confirmed extreme defines alternating 'directional change' and 'overshoot' events on the bid/ask mid-price, and each DC confirmation point is treated as an event-time observation for the agent. SADRL additionally reframes pairs of consecutive DC trends into a candlestick (open/close at the DC confirmation prices, high/low at the DC extreme prices) and computes fixed-interval-style indicators on that DC-event clock rather than physical time. Chapter 6 also directly benchmarks this DC/event clock against calendar-interval sampling, via a fixed-interval DRL control (TADRL) and fixed-interval technical-analysis strategies.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** 14 currency pairs: AUD/JPY, CAD/JPY, CHF/JPY, EUR/CHF, EUR/GBP, EUR/JPY, GBP/JPY, AUD/USD, EUR/USD, GBP/USD, NZD/USD, USD/CAD, USD/CHF, USD/JPY
- **Venue:** Tick data sourced from TrueFX.com
- **Period:** AUD/JPY, CAD/JPY, CHF/JPY, EUR/CHF, EUR/GBP, EUR/JPY, GBP/JPY: 1 May 2022 to 30 April 2023. The seven USD-denominated pairs: 1 January 2022 to 31 December 2022.
- **Granularity:** Raw tick-by-tick bid/ask prices, resampled with DC sampling at eight thresholds from 0.015% to 0.029%. FDRL used 4-week rolling windows (2 training, 1 validation, 1 test week), 49 windows per pair-threshold combination, for 5488 datasets total (14 pairs x 8 thresholds x 49 windows). PADRL and SADRL used 24-week rolling windows (16 training, 4 validation, 4 test weeks), 7 windows per pair-threshold combination, for 784 datasets total.

## Features and Measures

- **TMV (total move).** The ratio of a confirmed DC trend's whole price move to the DC threshold theta, indicating how large the move was relative to the sampling threshold.
- **OSV (overshoot value).** The percentage change between the current and previous DC confirmation prices, normalised by the threshold theta and averaged over the previous 3, 5 or 10 events, capturing how far price continued past confirmation.
- **RDC / TDC / NDC / CDC / AT indicators.** A family of DC-event tick-count and cumulative-move statistics: ticks per event adjusted for the event's return, ticks per event, ticks over a rolling window of prior events, cumulative absolute total-move over a rolling window of events, and the imbalance between ticks spent in up versus down trends, computed over rolling windows of 1 to 50 prior events and combined into a 30-dimensional per-timestep state used by FDRL and PADRL.
- **positional state features.** Features added in PADRL and SADRL giving the agent direct awareness of its own trading state: current position or direction, current running profit, the potential return if the position were closed immediately, and the current bid-ask spread.
- **DC candlestick reframing.** A SADRL-specific construction turning each pair of consecutive DC trends into a candlestick, with open and close set at the two trends' DC confirmation prices and high and low set at their DC extreme prices, from which moving averages, RSI, MACD and Bollinger Bands are computed.
- **no-overshoot consolidation filter.** An FDRL rule permitting trading only once a set number of consecutive DC trends have occurred with no overshoot move, used to restrict the agent to the low-volatility periods it was found to trade profitably.

## Method

Each framework is trained per rolling window, per currency pair, per DC threshold using the Stable Baselines 3 library with a PyTorch backend inside a custom Gym trading environment; the agent chooses between discrete buy/sell actions (FDRL, PADRL) or buy/sell/hold actions (SADRL) and is rewarded with realised trade profit. FDRL uses PPO with a two-hidden-layer (64, 64) ReLU policy/value network over a 150-dimensional state (30 DC indicators across a 5-step lag), trained for 200,000 timesteps with a batch size of 65,536 and 10 epochs, and is restricted to trade only after 5 consecutive no-overshoot DC trends. PADRL removes this filter, adds 4 positional features for a 34-dimensional state with no lag, trains for 3,000,000 timesteps with the same batch/epoch settings, fixes position size at 10% of balance, and selects the best checkpoint via a validation callback every 50,000 steps. SADRL replaces the DC indicators with fixed-interval-style technical indicators computed at DC confirmation points plus 2 candlestick features (a 27-dimensional state including 4 positional features), differences all features for stationarity (verified with Augmented Dickey-Fuller and KPSS tests across 112 pair-threshold combinations, 14 pairs x 8 thresholds), and compares four DRL algorithms (DQN, A2C, PPO, TRPO).

Performance is judged with Total Return, Maximum Drawdown, and the Calmar ratio (return divided by maximum drawdown), computed on a held-out test window after retraining on the combined training and validation data. Statistical comparisons across strategies use the non-parametric Friedman test with Conover post-hoc pairwise comparisons at the 0.05 significance level. FDRL and PADRL are tested under fixed transaction costs (0.025% and 0.035% of position size respectively, approximating commission plus spread), while SADRL is tested using the actual historical bid-ask spread as the transaction cost; slippage and the agent's own market impact are assumed negligible throughout. Benchmarks include Buy and Hold, Moving Average Crossover, RSI, a rule-only 'Blind Low Volatility' DC strategy in the FDRL chapter, and, in the SADRL chapter, Mean Reversion, MACD+RSI, Bollinger Bands and a fixed-interval DRL control (TADRL).

## Results

- Under a fixed 0.035% transaction cost, PADRL outperformed FDRL with an average Calmar-ratio rank of 1.37 versus FDRL's 1.80 (p = 4.139e-3).
- Once real bid-ask spreads replaced fixed transaction costs, both FDRL and PADRL deteriorated sharply, with FDRL's losses exceeding 99% on many pair-threshold combinations.
- Retrained and tested under bid-ask spreads, SADRL (using TRPO) achieved the best average Calmar-ratio rank (1.69) versus 3.93 for PADRL and 4.35 for FDRL (p = 1.42e-44 and 9.05e-60 respectively), and the best maximum-drawdown rank (1.57) versus 3.57 for PADRL and 4.43 for FDRL.
- SADRL outperformed the Mean Reversion, MACD+RSI and Bollinger Bands technical-analysis benchmarks on Calmar ratio, and outperformed the fixed-interval DRL control TADRL, which had the worst average Calmar rank (4.44) among the SADRL-chapter strategies.
- SADRL was not significantly beaten by Bollinger Bands on total return despite Bollinger Bands having a slightly better average rank (1.85 versus 2.20, p = 0.221).
- Across the four DRL algorithms trained inside the SADRL framework, PPO or TRPO produced the best total return in 73% (82/112) of pair-threshold combinations.
- FDRL performed best at higher DC thresholds (0.025%-0.029%) on EUR/CHF, EUR/GBP and EUR/JPY, where some pair-threshold combinations had Calmar ratios exceeding 1,000, but the author describes this as a narrow operating envelope.
- SADRL generalised more broadly than FDRL and PADRL, reaching Calmar ratios of 14.80 (CAD/JPY), 22.71 (CHF/JPY), 21.82 (USD/CHF) and 28.46 (EUR/USD) on pairs that were weak or negative for FDRL and PADRL once bid-ask spreads were applied.

## Limitations

- FDRL's very high headline returns depend on a fixed transaction-cost assumption (0.025%) that the thesis itself shows underestimates the real, spread-widening cost during the low-volatility periods FDRL trades; the author states this makes FDRL's results 'somewhat unattainable in a real market environment.'
- The no-overshoot trading filter used by FDRL is described by the author as making the strategy only partially autonomous and as interrupting the agent's own implicit planning.
- SADRL's learned strategy is trend-following and is reported to struggle when a trend reverses, and to sometimes hold profitable positions too long before exiting.
- Reader note: results are historical backtests on TrueFX tick data for 14 FX pairs over 2022-2023; no live or paper-trading validation, market-impact modelling from the agent's own trading, or execution-latency test is reported.
- The thesis explicitly flags that slippage and the agent's own price impact are assumed negligible throughout all three frameworks, and lists modelling these as future work.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/directional-change|Directional Change]]

## Citation

George Rayment (2025). Deep Reinforcement Learning for Trading Strategy Development on High-Frequency Currency Data Using Directional Changes Sampling. University of Essex (PhD thesis, School of Computer Science and Electronic Engineering).

DOI: 10.5526/err-00042298

Text ingested: `markdown_output/george-2025-deep-reinforcement-learning-trading-strategy-development.md`, converted from `raw/ofi-event-clock/george-2025-deep-reinforcement-learning-trading-strategy-development.pdf`.

Coverage of this summary: Read the abstract, full introduction and motivation, the background chapter's sections on financial forecasting concepts and DC sampling (including the DC sampling algorithm), and for each contribution chapter (FDRL, Chapter 4; PADRL, Chapter 5; SADRL, Chapter 6) the motivation, methodology, data and experimental setup, the prose results and interpretation sections, and the full conclusion chapter including the cross-framework comparison and future-research sections. Chapter 3's machine-learning background/literature-review chapter, the technical-analysis equations in Chapter 2, and most entries in the large per-pair-per-threshold result tables were not read in full detail; headline figures were drawn from the surrounding prose instead.

Known problems with the input: The thesis title as rendered in the converted markdown's title block has its words in a garbled order ('...for on Trading Strategy Development High-Frequency...'); the title recorded here follows the corrected word order given in the job's title_hint rather than the literal broken layout, since that is almost certainly a PDF-to-text line-reordering artifact rather than the actual printed title; This is a long (about 190-page) PhD thesis; per the extraction instructions for long documents, only the sections listed under coverage were read, not the full text or every entry of every results table; Chapter 4's results table and its surrounding prose give conflicting average Friedman ranks for the Buy-and-Hold benchmark (the table states 2.81, a nearby sentence states 1.53); this extraction did not attempt to resolve that inconsistency and avoided citing either figure.
<!-- AUTHORED REGION END -->