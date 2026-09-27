---
authors:
- Zijian Shi
- Yu Chen
- John Cartlidge
content_hash: sha256:8df9310d1a973771d16027e567612921d85e130e43923bbe379cac98d84f0f8c
created: 2026-09-27 01:47:00+00:00
page_id: sources/shi-2021-lob-recreation-model-predicting-limit-order
page_type: source
publication_venue: 35th AAAI Conference on Artificial Intelligence (AAAI-2021)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/recurrent-neural-networks
- concepts/lstm-networks
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:e37c4a7d1facbab21dd30072972162c21fd24669a48bd90f2d31eb6efe9f7f84
source_path: markdown_output/shi-2021-lob-recreation-model-predicting-limit-order.md
source_type: paper
tags:
- limit-order-book
- recurrent-neural-networks
- ode-rnn
- transfer-learning
- market-microstructure
- deep-learning
- clock-event
- asset-equity
- harvest-relevant
title: 'The LOB Recreation Model: Predicting the Limit Order Book from TAQ History
  Using an Ordinary Differential Equation Recurrent Neural Network'
updated: '2026-09-27T01:47:00Z'
uuid: 8d63d471-ace0-5b96-a51f-d4bc0de00396
year: 2021
---

<!-- AUTHORED REGION START -->
# The LOB Recreation Model: Predicting the Limit Order Book from TAQ History Using an Ordinary Differential Equation Recurrent Neural Network

## Summary

The paper asks whether, since full limit order book (LOB) data is expensive and not always available, the deeper levels of the LOB (beyond the best bid/ask) can be reconstructed from just trades-and-quotes (TAQ) data, which is far more widely and cheaply available.

The authors build the LOB Recreation Model (LOBRM) from three components: a GRU-based 'history compiler' that tracks past quote volumes at price levels that were previously visible at the top of book; an ODE-RNN-based 'market events simulator' that treats order arrivals at each depth level as an inhomogeneous Poisson process with a continuously evolving latent state, decoded into arrival rates; and an adaptive weighting scheme that combines the two predictions using a learned reliability weight based on how recent and abundant the quote history is at each level. The model is trained and evaluated on one day of LOBSTER order-book data for two small-tick technology stocks (MSFT and INTC), compared against linear/nonlinear regression baselines and discrete-RNN variants, with an ablation study and a transfer-learning experiment from MSFT to INTC.

The ODE-RNN version of LOBRM beats ridge regression, support vector regression, random forest, a single-layer feedforward network, and discrete GRU/LSTM variants on held-out test loss and R2 for both the bid and ask sides. The market-events simulator component is the single biggest contributor to accuracy in the ablation study, though combining all three components gives the best result. Transferring the MSFT-trained model to INTC using only a fraction of INTC's data reaches accuracy close to a fully trained discrete-RNN model, and using the recreated LOB for a downstream mid-price-direction classifier comes within about 1.5 percentage points of using the real five-level LOB, far ahead of using only the top-of-book quote.

What is new, per the authors, is the first deep-learning attempt to recreate deeper LOB levels from TAQ data alone, and the first use of an ODE-RNN (a continuous-time latent state) for this specific LOB-recreation problem, which they show handles the irregular timing of TAQ arrivals better than standard discrete-time RNNs.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The model consumes a rolling window of the last 100 TAQ time points (trade and top-of-book quote records) ending at a target time, encoded with one-hot positional vectors by price-level distance from the current best bid/ask. It predicts the order volumes at the 2nd-through-5th price levels of the LOB observed at that same target time, i.e. a same-time reconstruction rather than a forward-looking forecast; irregular inter-event gaps are handled by letting the ODE-RNN's latent state evolve continuously between observations.

## Data

- **Asset class:** Equities
- **Instruments:** MSFT and INTC (small-tick technology stocks)
- **Venue:** LOBSTER-reconstructed order book (from NASDAQ TotalView-ITCH)
- **Period:** one full trading day, 12/06/2012
- **Granularity:** full order-book updates and TAQ data at event level; about 1 million LOB updates that day, reduced to about 10K time-series samples after restricting to unique trade timestamps and trimming the first/last half hour

## Features and Measures

- **History Compiler (HC).** A GRU module that compiles past quote volumes at price levels that were previously visible at the top of book, giving a rough historical estimate of current depth.
- **Market Events Simulator (ES).** An ODE-RNN module that treats order arrivals at each depth level as an inhomogeneous Poisson process with a continuously evolving latent state, decoded into arrival rates and accumulated into predicted volumes.
- **Weighting Scheme (WS).** An adaptively learned, GRU-encoded reliability weight, derived from the masking sequence of quote history, that fuses the HC and ES predictions at each price level.
- **One-hot positional encoding.** A sparse representation of TAQ quote/trade records that encodes price level implicitly by vector position and encodes volume/direction explicitly as the vector's value.

## Method

Four baseline regressors (ridge regression, support vector regression, random forest, single-layer feedforward network) and four discrete-RNN LOBRM variants (GRU, GRU with time concatenated, LSTM, LSTM with time concatenated) are compared against the full ODE-RNN LOBRM using L1 loss, L1-loss-as-percentage-of-average-volume, and R2 on held-out test data. An ablation study isolates the contribution of the history compiler, event simulator, and weighting scheme, using Wilcoxon signed-rank tests to check statistical significance between configurations. A transfer-learning experiment trains the full model on MSFT and fine-tunes it on only 30% of INTC's data. A downstream application trains a convolutional-plus-GRU mid-price-direction classifier on the real LOB, the recreated LOB, and quote-only (top-of-book) data, to see how much of the real LOB's predictive value the recreated LOB preserves.

## Results

- The full ODE-RNN LOBRM achieved the lowest test loss and highest R2 of all models compared: test loss of 7.36% (bid) and 6.50% (ask) with R2 of 0.773 (bid) and 0.753 (ask), versus 17.32%/15.22% test loss and R2 of 0.169/0.141 for ridge regression.
- In the ablation study, the event simulator (ES) alone (test loss 7.48%/7.00%, R2 0.769/0.723) greatly outperformed the history compiler (HC) alone (test loss 15.20%/12.57%, R2 0.273/0.291), and combining HC with ES gave a further, statistically significant improvement over ES alone (Wilcoxon p<0.01 on both bid and ask sides).
- Transferring the MSFT-trained model to INTC using only 30% of INTC's data reached a test loss of 9.78% (bid) and 8.95% (ask) with R2 of 0.685 (bid) and 0.649 (ask), roughly matching a fully trained discrete-RNN model's accuracy.
- In the downstream mid-price-direction classification task, the real 5-level LOB gave 81.14% test accuracy, the top-of-book quote alone gave 75.17%, and the recreated LOB gave 79.75% -- about 1.5 percentage points below the real LOB and 4.5 points above quote-only data.
- Averaging LOBRM's volume predictions to roughly five-minute frequency raised R2 to over 0.9, closer to the [0.81, 0.88] daily-average R2 range reported for a comparable statistical LOB-recreation model.
- It took roughly 1000 iterations for the discrete-RNN LOBRM variants to converge versus about 250 iterations for the continuous ODE-RNN version, and the ODE-RNN reached a lower loss after 50 iterations than the discrete RNNs reached after 1000.

## Limitations

- The authors state the study trains and tests on only two intraday datasets (MSFT and INTC, one trading day each), which they call an obvious limitation given the scarce availability of public LOB data.
- Longer-horizon benchmark LOB datasets exist (e.g. FI-2010) but could not be used because they lack the timestamps the model's time-aware components need.
- Reader note: results are limited to small-tick technology stocks, and the paper's own cited finding that the top LOB level already explains about 80% of future price movements may bound how much additional value deeper-level recreation can add for this asset class.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Zijian Shi, Yu Chen, John Cartlidge (2021). The LOB Recreation Model: Predicting the Limit Order Book from TAQ History Using an Ordinary Differential Equation Recurrent Neural Network. 35th AAAI Conference on Artificial Intelligence (AAAI-2021).

DOI: 10.1609/aaai.v35i1.16133

Text ingested: `markdown_output/shi-2021-lob-recreation-model-predicting-limit-order.md`, converted from `raw/ofi-event-clock/shi-2021-lob-recreation-model-predicting-limit-order.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, background/related work, the full model description (problem description, model structure, HC, ES, WS), the empirical analysis (data preprocessing, model comparison, ablation study, transfer learning, application scenario), and the conclusion.
<!-- AUTHORED REGION END -->