---
authors:
- Adamantios Ntakaris
- Gbenga Ibikunle
content_hash: sha256:f231140ab25a0d7331fab07ae765e38eab57c481876329d3fc04fdd738e5ddcc
created: 2026-09-27 01:47:00+00:00
page_id: sources/ntakaris-2024-minimal-batch-adaptive-learning-policy-engine
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/feature-engineering
- concepts/market-microstructure
- entities/adamantios-ntakaris
revision_id: 1
schema_version: 2
source_hash: sha256:d02bbe57627704fb70185d56d9fc62207dfacf07030d9f66c71f0fc8ed408382
source_path: markdown_output/ntakaris-2024-minimal-batch-adaptive-learning-policy-engine.md
source_type: paper
tags:
- reinforcement-learning
- limit-order-book
- mid-price-forecasting
- high-frequency-trading
- event-driven-forecasting
- feature-engineering
- deep-learning
- nasdaq
- clock-event
- asset-equity
- harvest-relevant
title: Minimal Batch Adaptive Learning Policy Engine for Real-Time Mid-Price Forecasting
  in High-Frequency Trading
updated: '2026-09-27T01:47:00Z'
uuid: fc3d31aa-a00d-524a-889d-297f68db85e1
year: 2024
---

<!-- AUTHORED REGION START -->
# Minimal Batch Adaptive Learning Policy Engine for Real-Time Mid-Price Forecasting in High-Frequency Trading

## Summary

This study asks whether a reinforcement-learning agent that adapts continuously, event by event, can forecast the limit order book mid-price better than statistical and standard machine-learning or deep-learning models trained the usual way, on fixed batches of historical data. It builds on the authors' earlier work with a Radial Basis Function Neural Network that used automated feature-importance selection over 20 U.S. stocks, and extends the evaluation to 100 stocks while adding a new reinforcement-learning model.

The proposed agent, called the Adaptive Learning Policy Engine (ALPE), is framed as a model-free, value-based reinforcement-learning problem: the state is a vector of limit order book features (either a simple set built from the best bid/ask price and volume, or an extended set of synthesized and kernel-transformed features), the action is a small continuous adjustment to the predicted mid-price, and the reward penalizes the gap between that adjustment and the true mid-price move, weighted by a term that grows as the agent's exploration rate falls. Exploration follows an epsilon-greedy rule with a decaying exploration probability, and the discount factor is set to zero so the agent optimizes only for the very next event. The policy-value function is approximated by a multi-layer perceptron with several hidden layers and batch normalization, retrained after only a couple of passes at every step, using only the current LOB state (no historical window), which is what makes the model batch-free. ALPE is compared against a naive baseline, ARIMA, MLP, CNN, LSTM, GRU, and the earlier RBFNN model, all of which instead train on a short rolling window of past LOB states, using Level 1 LOB data for 100 S&P 500 stocks traded on NASDAQ over a three-month window. Performance is judged with RMSE and with a new metric the authors call Relative RMSE (RRMSE), which divides each stock's RMSE by its own mid-price so that error comparisons are meaningful across stocks trading at very different price and volume levels.

ALPE comes out with the lowest error across almost every stock and every combination of feature set (simple vs. extended, and raw vs. two feature-weighting schemes). Statistical testing shows its advantage over the naive and ARIMA models, and over MLP and CNN, is highly significant, while the gap to LSTM and to the earlier RBFNN model, though usually still in ALPE's favor, is not always statistically significant. On Amazon, used as a worked example, the extended feature set with one of the feature-weighting schemes gives the agent a large relative improvement over both GRU and MLP.

What is new here relative to the authors' own prior work and to the broader forecasting literature is the batch-free design itself: rather than retraining periodically on a window of past states like every other model tested, ALPE updates continuously from a single current observation, which the authors argue better matches how fast conditions actually change intraday. The RRMSE metric is a secondary contribution, aimed at letting practitioners compare forecast quality across stocks of very different scale rather than relying on raw RMSE alone.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are individual limit-order-book events, each given its own index even when several events share the same timestamp, so there is no time-based sampling. The forecast target is the mid-price at the very next LOB event. ALPE updates using only the current LOB state (an effective look-back window of one), while the batch-based competitor models are instead trained on a rolling window covering the current state plus nine preceding states.

## Data

- **Asset class:** Equities
- **Instruments:** 100 U.S. stocks drawn from the S&P 500 index (listed by ticker, e.g. AMZN, BAC, JPM, MSFT, NVDA, XOM)
- **Venue:** NASDAQ, Level 1 limit order book data supplied by the London Stock Exchange Group (LSEG)
- **Period:** September 1 to November 30, 2022
- **Granularity:** Level 1 limit order book (best bid/ask price and volume only), recorded event by event

## Features and Measures

- **Simple feature set.** The raw Level 1 limit order book snapshot: best bid and ask prices and their corresponding volumes.
- **Basic and synthesized extended features.** Transformations of the best bid/ask prices and volumes, including the mid-price, the bid-ask spread, a sinusoidal transform, and product/quadratic combinations of price and volume meant to capture non-linear price-volume interactions.
- **Kernel-transformed extended features.** Linear, polynomial (degree three), sigmoid, exponential, and radial-basis-function kernel transformations of the best bid/ask prices, used to capture more complex, non-linear relationships in the order book snapshot.
- **MDI feature importance.** A random-forest-based feature-importance score computed as the average reduction in variance-based node impurity attributable to each feature across all trees, reused from the authors' earlier work.
- **GD feature importance.** A gradient-descent-based feature-weighting scheme that iteratively adjusts a weight vector to minimize prediction error, with the resulting weight magnitudes used as feature-importance scores.
- **Relative Root Mean Squared Error (RRMSE).** A normalized version of RMSE obtained by dividing a stock's RMSE score by its mid-price on an event-by-event basis, intended to make error comparisons meaningful across stocks with different price scales.

## Method

The forecasting task is posed as an event-by-event regression problem and, for the new model, as a Markov decision process with states given by the chosen LOB feature vector, a bounded continuous action representing the adjustment to the predicted mid-price, a reward that penalizes the squared deviation from the true mid-price move while up-weighting the penalty as exploration decays, and a discount factor of zero so only the immediate reward matters. Actions are chosen with an epsilon-greedy rule in which the exploration probability decays over time toward a small floor, and the policy value is approximated with a multi-layer perceptron of eight hidden layers of 64 rectified-linear-unit neurons each, with batch normalization after the first hidden layer, trained online with the Adam optimizer using only the current LOB state and a very small number of gradient passes at every step, which is what makes the agent batch-free.

ALPE is benchmarked against a naive regressor, ARIMA, MLP, CNN, LSTM, GRU, and the authors' earlier RBFNN model, all trained in a batch-based rolling-window setting instead of the batch-free setting used for ALPE. Every model and stock combination is run multiple times and the RMSE and RRMSE scores are averaged to reduce the effect of random variation. Differences in RMSE across models are tested for statistical significance using a Friedman test followed by a Conover post-hoc pairwise comparison with a Bonferroni correction for multiple comparisons, applied across the different feature-set and feature-weighting configurations (simple and extended feature sets, each with raw, MDI-weighted, and GD-weighted variants).

## Results

- For Amazon under the simple feature set, ALPE achieved an RMSE of 5.586E-02 and an RRMSE of 4.906E-04, the lowest of any model tested.
- For Amazon under the extended feature set, ALPE's error fell further, to an RMSE of 2.527E-02 and an RRMSE of 2.732E-04, again the lowest among all competitor models.
- In the conclusion's worked example, ALPE on the extended, gradient-descent-weighted dataset for Amazon reached an RRMSE of 2.484E-04, about 79% below GRU's RRMSE of 1.178E-03 and about 73% below MLP's RRMSE of 9.202E-04.
- Pairwise statistical testing (Conover post-hoc test after a significant Friedman test) found ALPE's RMSE advantage over the naive and ARIMA models significant at the 0.001 level, and its advantage over CNN and MLP significant at the 0.01 level.
- ALPE's advantage over LSTM and the earlier RBFNN model was directionally consistent (lower average RMSE and RRMSE) but not statistically significant in every dataset configuration.
- Across the 100 stocks, ALPE's error was generally lowest when paired with the extended, gradient-descent-weighted feature set, suggesting the added non-linear kernel and synthesized features help more than the raw Level 1 snapshot alone.
- RRMSE distinguished forecasting quality more clearly than RMSE for lower-volume stocks, since RMSE alone tends to overstate apparent error differences once price and volume scales diverge across stocks.
- Which input configuration gave ALPE its best RRMSE varied by stock and roughly tracked trading volume: high-volume stocks such as BAC and XOM favored extended feature configurations, while lower-volume stocks such as WBD and IPG did best with the simpler feature set.

## Limitations

- Training-window size for the batch-based competitor models, the number of MDI/GD feature-importance iterations, the epsilon-decay schedule, and the network architecture were all fixed across all 100 stocks rather than tuned per stock, even though the authors note some stocks have fewer trading events than the decay schedule assumes.
- The evaluation uses only Level 1 (best bid/ask) limit order book data from one venue (NASDAQ) over a single three-month window; deeper, Level 2 order book data was not used.
- The discount factor is fixed at zero, so the agent is optimized purely for the very next event and does not model longer-horizon dependencies.
- Reader note: the mid-price is not itself directly tradable, so lower forecast error is a proxy for, rather than direct evidence of, better trading outcomes.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/market-microstructure|market microstructure]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]

## Citation

Adamantios Ntakaris, Gbenga Ibikunle (2024). Minimal Batch Adaptive Learning Policy Engine for Real-Time Mid-Price Forecasting in High-Frequency Trading.

DOI: 10.48550/arxiv.2412.19372

Text ingested: `markdown_output/ntakaris-2024-minimal-batch-adaptive-learning-policy-engine.md`, converted from `raw/ofi-event-clock/ntakaris-2024-minimal-batch-adaptive-learning-policy-engine.pdf`.

Coverage of this summary: Read the abstract, introduction, full literature review, the entire methodology section (data description, feature engineering with MDI and GD, the MDP formulation, network architecture, and training protocol), the results and discussion section, the conclusion, and skimmed the reference list; the per-stock appendix tables (A.1-A.13) were not read in detail beyond the Amazon example already reported in the main text.

Known problems with the input: The paper carries no printed publication date or venue in the converted text; year is taken from the job's year_hint (year from file metadata); Equations throughout the methodology section were replaced by 'picture omitted' placeholders during PDF-to-markdown conversion, so exact formula notation (e.g. the MDP reward, MDI, and GD update equations) is described only from the surrounding prose, not the equations themselves; Appendix tables A.1-A.13, holding the full per-stock results for all 100 stocks, were not read in detail; only the Amazon example (Table 3) and the aggregate discussion in the main text were used.
<!-- AUTHORED REGION END -->