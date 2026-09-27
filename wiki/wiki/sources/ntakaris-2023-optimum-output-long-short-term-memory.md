---
authors:
- Adamantios Ntakaris
- Moncef Gabbouj
- Juho Kanniainen
content_hash: sha256:df8c0a1f4cb38060d9f7cd4db92a23118a11aa8a52135a42664615b53e74840c
created: 2026-09-27 01:47:00+00:00
page_id: sources/ntakaris-2023-optimum-output-long-short-term-memory
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
- concepts/feature-engineering
- entities/adamantios-ntakaris
- entities/moncef-gabbouj
- entities/juho-kanniainen
revision_id: 1
schema_version: 2
source_hash: sha256:9a496458db4ec478c8e39ac8e6dddbb40c8522a1f05c7416c342dcefb8702156
source_path: markdown_output/ntakaris-2023-optimum-output-long-short-term-memory.md
source_type: paper
tags:
- lstm
- limit-order-book
- high-frequency-trading
- mid-price-forecasting
- online-learning
- recurrent-neural-networks
- clock-event
- asset-equity
- harvest-core
title: Optimum Output Long Short-Term Memory Cell for High-Frequency Trading Forecasting
updated: '2026-09-27T01:47:00Z'
uuid: 876bf483-e2a9-5c69-b0f2-86792ceb0d32
year: 2023
---

<!-- AUTHORED REGION START -->
# Optimum Output Long Short-Term Memory Cell for High-Frequency Trading Forecasting

## Summary

The paper addresses online, tick-by-tick forecasting of the next limit order book mid-price in high-frequency trading, where a standard LSTM cell applies a fixed, unchanging order of internal gate and state calculations regardless of what the current data looks like. The authors argue this stale internal structure is a poor fit for a fast-changing, ultra-low-latency setting.

Their proposed OPTM-LSTM cell keeps the same four gates and four states as a standard LSTM but adds an internal, non-forecasting supervised regression that predicts the current, already-known mid-price from a concatenation of the six internal gates and states. This regression is trained online with gradient descent at every step, producing an importance weight for each gate or state; the highest-scoring one replaces the cell's hidden-state output, while the cell state itself is left unchanged. The main forecasting task, predicting the mid-price at the next trading event, sits outside this internal mechanism and uses whichever gate or state was chosen.

Tested on tick data for two high-liquid US stocks (Amazon and Google) and two less-liquid Nordic stocks (Kesko and Wartsila), OPTM-LSTM achieved lower mean squared error than five RNN benchmarks (a prototype LSTM, an LSTM with attention, a bidirectional LSTM, a GRU, and an LSTM-CNN hybrid) and two naive baselines, across progressively larger training sets and under both a Short Training regime (up to 5 epochs) and a Long Training regime (up to 60 epochs), while itself using a shallower topology, a batch size of 1, and a look-back period of 1.

What is new is the idea of treating an LSTM cell's own internal gates and states as candidate outputs to be selected online rather than combined in a fixed, pre-set order; this lets the model discard the batch/mini-batch and long look-back choices that other RNNs need, and process every trading event as an independent update.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Every trading event is treated as an independent tick-by-tick observation rather than sampled on a fixed time grid; the model uses only the current full 10-level limit order book state (a look-back period of 1) to predict the mid-price at the next trading event, so the prediction horizon is exactly one trading event ahead.

## Data

- **Asset class:** Equities
- **Instruments:** Amazon and Google (two high-liquid US stocks); Kesko and Wartsila (two less-liquid Nordic stocks)
- **Venue:** NASDAQ, using the ITCH data protocol
- **Period:** First two trading months of 2015 for Amazon and Google; from 1 June to the end of July 2010 for Kesko and Wartsila
- **Granularity:** Tick-by-tick limit order book data with 10 price levels per side (bid and ask); the full-book feature set has 40 features (price and volume levels), and a second feature set uses only the mid-price

## Features and Measures

- **Mid-price (MP).** The average of the best ask and best bid price at a given trading event; used as the forecasting target and, in lagged/current form, as the label for the cell's internal guarantor mechanism.
- **LSTM gates and states as features.** The forget, input, candidate and output gates plus the cell state and hidden state are treated as six candidate output features rather than being combined in one fixed order.
- **Importance Weights Vector (IWV).** Weights learned by an internal, online gradient-descent regression that ranks the six gates/states by average importance per hidden unit; the top-ranked one replaces the cell's hidden-state output.

## Method

The OPTM-LSTM cell adds, just before a standard LSTM cell would release its output, an internal non-forecasting supervised regression problem: it concatenates the six gates/states into one vector and fits, via online gradient descent, a linear model that predicts the current (already known) mid-price. The resulting weights are averaged per gate/state to rank them, and the top-ranked gate or state becomes the new hidden-state output; the cell state is kept unchanged. This internal step is separate from the backpropagation-through-time training of the LSTM's own weights.

Performance is judged by mean squared error (MSE) on tick-by-tick prediction of the next mid-price, computed under raw data and two normalisations (MinMax and Zscore). Training set sizes are increased progressively, from 1,000 up to 20,000,000 trading events for the two US stocks and up to 5,000,000 for the two Nordic stocks, with testing done on a rolling window of 1,000 trading events. Two training regimes are compared: Short Training (up to 5 epochs) and Long Training (up to 60 epochs, with early stopping). Five competing RNN architectures (prototype LSTM, LSTM with attention, bidirectional LSTM, GRU, an LSTM-CNN hybrid) and two naive baselines (a constant-target regressor and a flat/persistence predictor) are each tuned with a topological and hyperparameter grid search (depth up to four layers, units from 8 to 512, several optimizers, batch sizes from 1 to 64, and look-back periods of 1, 5 or 10), while OPTM-LSTM is limited to at most two layers, a batch size of 1 and a look-back period of 1.

## Results

- OPTM-LSTM achieved lower MSE than the five RNN competitors and the two naive baselines across almost all data-size scenarios for all four stocks, in both the Short and Long training regimes.
- The winning OPTM-LSTM topology used a single hidden layer with a batch size of 1 and a look-back period of 1, versus competitors that used up to four hidden layers, batch sizes up to 64, and look-back periods of 1, 5 or 10.
- Under the Zscore normalisation setting, MSE differences across models narrowed for most models but OPTM-LSTM still performed better; for Google, the internal gradient-descent learning rate was tuned to 0.0001.
- For Google, all models showed higher MSE for the 2,000 to 3,000 sample range; mid-price variance at 3,000 samples was 7.37E+14 for Google versus 5.78E+12 for Amazon, and variance dropped 72% for Google versus 2% for Amazon between the 3,000- and 5,000-sample windows.
- Long Training (up to 60 epochs) produced lower MSE than Short Training (up to 5 epochs) for the same data sizes; the authors estimate about 0.4 seconds per epoch for 15,000 trading events on a single GPU.
- The hybrid LSTM-CNN model occasionally approached OPTM-LSTM's performance for Amazon but oscillated heavily across MSE scores, which the authors attribute to the non-linearity of its convolutional layers.

## Limitations

- Restricted number of stocks and trading horizons (two high-liquid and two less-liquid names); the authors state a wider stock selection would give more insight into the model's behaviour.
- The trading horizon used for each stock was chosen once MSE stopped decreasing rather than by a fixed criterion; the authors note a longer horizon might have produced an even lower MSE.
- The authors state that a more advanced optimisation method than the plain online gradient-descent guarantor could be used.
- Reader note: the forecasting target is only the mid-price for four single-name equities; no cross-asset, portfolio-level, or live-trading validation is reported.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/feature-engineering|feature engineering]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/juho-kanniainen|Juho Kanniainen]]

## Citation

Adamantios Ntakaris, Moncef Gabbouj, Juho Kanniainen (2023). Optimum Output Long Short-Term Memory Cell for High-Frequency Trading Forecasting.

DOI: 10.48550/arxiv.2304.09840

Text ingested: `markdown_output/ntakaris-2023-optimum-output-long-short-term-memory.md`, converted from `raw/ofi-event-clock/ntakaris-2023-optimum-output-long-short-term-memory.pdf`.

Coverage of this summary: Read the full converted markdown: abstract, introduction, related work, the proposed-method section (cell design, complexity, and motivation), the experiments section (protocol, datasets, results including Tables II and III, limitations and future research), and the conclusion; the appendix's backpropagation-through-time derivation and the additional per-stock appendix tables were not read in full since most of their content is rendered as omitted pictures.

Known problems with the input: year from file metadata; Many equations, figures, and the appendix derivation are rendered as '==> picture... intentionally omitted <==' in the markdown conversion, so those details could not be verified and were not used.
<!-- AUTHORED REGION END -->