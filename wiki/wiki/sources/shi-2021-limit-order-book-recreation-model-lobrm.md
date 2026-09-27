---
authors:
- Zijian Shi
- John Cartlidge
content_hash: sha256:fbe599d8d465c473e16a6ed34b57905478aad802a4b4f1e3798adc205eecbc00
created: 2026-09-27 01:47:00+00:00
page_id: sources/shi-2021-limit-order-book-recreation-model-lobrm
page_type: source
publication_venue: ECML-PKDD 2021
related:
- concepts/trade-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/recurrent-neural-networks
- concepts/stylized-facts
revision_id: 1
schema_version: 2
source_hash: sha256:1da54cba61c974158e19309be72c8c788034a21774c65307e988795b4a6b0bd7
source_path: markdown_output/shi-2021-limit-order-book-recreation-model-lobrm.md
source_type: paper
tags:
- limit-order-book
- taq-data
- recurrent-neural-networks
- lookahead-bias
- chronological-evaluation
- equities
- deep-learning
- clock-trade
- asset-equity
- harvest-relevant
title: 'The Limit Order Book Recreation Model (LOBRM): An Extended Analysis'
updated: '2026-09-27T01:47:00Z'
uuid: 3ff13729-ba16-5fc9-8eda-57e2d3a675ac
year: 2021
---

<!-- AUTHORED REGION START -->
# The Limit Order Book Recreation Model (LOBRM): An Extended Analysis

## Summary

The paper asks whether the original Limit Order Book Recreation Model (LOBRM), a deep learning system that predicts resting order volumes in a limit order book (LOB) from trades-and-quotes (TAQ) data, still performs well when tested realistically: on multiple stocks, over several trading days, and using a strictly chronological train/test split rather than the original one-day, shuffled-sample setup that risked lookahead bias.

The authors keep the original LOBRM architecture of three neural modules, a Market Event Simulator, a History Compiler, and a Weighting Scheme, but replace its ordinary-differential-equation (ODE) kernel with a computationally cheaper exponential decay kernel, and add a time-weighted z-score standardization for LOB volumes. They test the revised model on an extended LOBSTER dataset covering five trading days for three small-tick US stocks (Microsoft, Intel, JPMorgan), using the first three days for training, the fourth for validation, and the fifth for chronological out-of-sample testing.

LOBRM with the decay kernel outperforms linear and non-linear regression baselines, and ensembling the Market Event Simulator and History Compiler modules improves results further. Chronological, lookahead-free testing produces noticeably higher error than the original non-chronological setup, confirming that earlier results were partly inflated by lookahead bias. Prediction error is negatively correlated with the volatility of resting order volumes, and adding more historical training days lowers test error, suggesting stochastic drift can be partly offset with more data.

New contributions include a sparse one-hot positional encoding for TAQ data that outperforms an explicit encoding on both LOB-volume prediction and stock price-trend prediction, and a demonstration that the purpose-built decay kernel avoids the overfitting shown by the original's fully flexible ODE kernel under chronological evaluation.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

The LOB is sampled only at trade-event times, not on every book update, producing an irregularly-spaced time series per stock; a rolling window of the previous 100 TAQ observations forms the model input, and the prediction target is the LOB order volume at the deeper price levels at the very next trade-event timestep, a next-event prediction rather than a fixed calendar horizon.

## Data

- **Asset class:** Equities
- **Instruments:** Microsoft (MSFT), Intel (INTC), JPMorgan (JPM); three small-tick US stocks
- **Venue:** not stated
- **Period:** Five consecutive trading days per stock: the first three for training, the fourth for validation, the fifth for testing; specific calendar dates are not stated.
- **Granularity:** Trade-event-time snapshots of the top five price levels on each side of the book, using a rolling window of 100 time steps.

## Features and Measures

- **Time-weighted z-score standardization.** A standardization of LOB order volumes that weights each observation by the time it persisted before the next update, computed separately for the top price level and for deeper levels because their volume statistics differ.
- **Sparse one-hot TAQ encoding.** An encoding of historical quotes and trades where only volume is represented numerically and price is implied by the position of the non-zero element in a one-hot vector, keeping only the nearest relative price ticks.
- **Market Event Simulator (ES) module.** A recurrent module that treats net order arrivals as an inhomogeneous Poisson process and decodes its latent state, via an exponential-decay or ODE kernel, into predicted order-arrival rates at each price level.
- **History Compiler (HC) module.** A module that looks back over historical quotes at the specific price levels being predicted to supply a volume estimate that supplements the Market Event Simulator's prediction.
- **Weighting Scheme (WS) module.** A module that combines the ES and HC module predictions using a learned, data-dependent weight based on how abundant and recent the relevant historical quotes are.

## Method

LOBRM is an ensemble of three GRU-based modules, ES, HC, and WS, that take sparsely encoded TAQ history as input and output predicted LOB order volumes at deeper price levels, separately for the bid and ask sides. In this extended study, the original ODE-RNN kernel inside the ES module is replaced with a pre-defined exponential decay kernel to reduce computation and overfitting, and time-weighted z-score standardization is applied to LOB volumes before training.

Training uses L1 loss over a fixed number of iterations with a small learning rate, with model selection by lowest validation loss; the ES, HC, and WS modules each consist of a GRU followed by a multi-layer perceptron decoder with a module-specific activation and latent state size.

Performance is judged with L1 test loss, in standard-deviation units, and R-squared computed against ground truth, benchmarked against linear support vector regression, ridge regression, a single-layer feedforward network, and XGBoost regression; an ablation study isolates the contribution of the HC, ES, and WS modules, and a separate experiment compares sparse versus explicit TAQ encodings on both LOB-volume prediction and a three-class price-trend prediction task.

## Results

- LOBRM with the decay kernel achieved the lowest average test loss and highest average R-squared among all models compared, with L1 test losses ranging from 0.332 to 0.628 across the six bid/ask stock experiments.
- Hourly L1 test loss correlated with the standard deviation of resting order volume with a correlation coefficient of 0.48 (p < 0.01), supporting a negative relationship between prediction accuracy and volume volatility.
- Chronological, lookahead-free evaluation gave a mean transformed test loss of 18.9% of average volume, versus 6.9% for the original non-chronological interpolation-style evaluation, showing the earlier results benefited from lookahead bias.
- When averaged to hourly frequency, R-squared across the experiments ranged from 0.48 to 0.88 with an average of 0.71, comparable to the 0.81 to 0.88 range reported for daily-average volume prediction in prior statistical-model work.
- The full HC+ES+WS ensemble and the HC+ES combination tied for the best average ablation test loss of 5.49, both beating HC alone at 6.09 and ES alone at 5.72.
- Sparse encoding lowered average LOB-volume test loss by 17.9% relative to explicit encoding, and it also gave higher price-trend prediction accuracy, 60.2% validation and 57.4% test with z-score standardization, than convolution-based encoding.
- Adding more historical training days reduced average test loss from 6.03 with one day of training to 5.48 with three days of training.

## Limitations

- The dataset covers only three small-tick stocks and five trading days each; the authors note this remains a small sample relative to the one-month and seventeen-month datasets used in other cited LOB studies.
- The model only predicts order volumes at the moment of each trade, ignoring order submissions and cancellations and all LOB states between trades.
- Stocks and sample period were fixed by the data provider rather than chosen by the authors, and specific calendar dates are not given in the paper.
- Reader note: only one stock and a simplified model were used for the price-trend prediction comparison, so that result generalizes less than the main LOB-volume findings.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/stylized-facts|stylized facts]]

## Citation

Zijian Shi, John Cartlidge (2021). The Limit Order Book Recreation Model (LOBRM): An Extended Analysis. ECML-PKDD 2021.

DOI: 10.1007/978-3-030-86514-6_13

Text ingested: `markdown_output/shi-2021-limit-order-book-recreation-model-lobrm.md`, converted from `raw/ofi-event-clock/shi-2021-limit-order-book-recreation-model-lobrm.pdf`.

Coverage of this summary: Read the full markdown paper, including abstract, introduction, background and related work, model formulation (data standardization, sparse encoding, ES/HC/WS modules), experiment and empirical analysis, ablation study, sparse-encoding comparison, training-size analysis, and conclusion.

Known problems with the input: Several equations (LOB standardization formulas, ODE and decay-kernel updates, sparse-encoding formulas) are rendered as 'picture... omitted' placeholders in the converted markdown and could not be transcribed.
<!-- AUTHORED REGION END -->