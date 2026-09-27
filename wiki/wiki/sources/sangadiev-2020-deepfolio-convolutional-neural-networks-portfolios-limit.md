---
authors:
- Aiusha Sangadiev
- Rodrigo Rivera-Castro
- Kirill Stepanov
- Andrey Poddubny
- Kirill Bubenchikov
- Nikita Bekezin
- Polina Pilyugina
- Evgeny Burnaev
content_hash: sha256:c1f48ef91c2d24d5f29eb98ed77fd5d96664d6a230774d53a38f7ae58b1d77b4
created: 2026-09-27 01:47:00+00:00
page_id: sources/sangadiev-2020-deepfolio-convolutional-neural-networks-portfolios-limit
page_type: source
related:
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:0427d06d3b0fad00e9605525d8d593265fd722424fb5e747e898bedaeb4c3ede
source_path: markdown_output/sangadiev-2020-deepfolio-convolutional-neural-networks-portfolios-limit.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- portfolio-allocation
- cryptoassets
- cnn-gru
- transfer-learning
- clock-calendar
- asset-multi
- harvest-relevant
title: 'DeepFolio: Convolutional Neural Networks for Portfolios with Limit Order Book
  Data'
updated: '2026-09-27T01:47:00Z'
uuid: 1705cd08-52d1-5795-be3f-25333c85a268
year: 2020
---

<!-- AUTHORED REGION START -->
# DeepFolio: Convolutional Neural Networks for Portfolios with Limit Order Book Data

## Summary

The paper asks whether a redesigned deep-learning architecture can predict short-term price trends from limit order book (LOB) data more reliably than the existing DeepLOB model, and whether such predictions can then drive automatic crypto-asset portfolio construction. It builds on the DeepLOB approach (a CNN plus LSTM) but reports that DeepLOB is very sensitive to its initial weight setup, trains slowly on smaller datasets, and scales poorly as more depth is added.

To address these issues, the authors replace DeepLOB's convolution-recurrent block with a "ResCNN+GRU" module: stacked residual convolutional blocks (borrowing residual connections and an inception-v2-style block from computer vision) feeding a GRU instead of an LSTM, with Glorot-uniform weight initialization and no batch normalization inside the residual blocks. The resulting three-way (down/flat/up) price-trend classifier is tested on the FI-2010 Nordic-stock benchmark and on a year of Binance crypto-asset order-book data (BTC, LTC and ETH, with XRP held out for transfer-learning tests). The same trend predictions are then fed into an LSTM-plus-softmax layer that produces rebalancing weights for a small crypto-asset portfolio, trained with either a Sharpe-ratio-maximizing or a volatility-minimizing loss.

DeepFolio outperforms CNN and LSTM baselines and edges out DeepLOB on both datasets, with the advantage over DeepLOB growing at longer prediction horizons; it also starts training faster and is far less sensitive to weight initialization than DeepLOB on the crypto data. In transfer-learning tests on the unseen XRP asset, DeepFolio again beats DeepLOB, suggesting it learns patterns that generalize across order books rather than memorizing one asset. In the portfolio backtest, the DeepFolio strategy trained with the Sharpe-ratio loss produced the best risk-adjusted returns among all the reallocation strategies compared, including Markowitz mean-variance portfolios and a naive equal-weight portfolio, over a test window that happened to include the COVID-19 market shock in early 2020.

The novelty claimed is twofold: an architecture that removes DeepLOB's initialization sensitivity and slow-training problems through residual connections and GRUs, and the idea of driving portfolio rebalancing directly from predicted price-trend labels rather than from historical price or return series.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

For FI-2010 the paper reuses the benchmark's own indexing: prediction horizon k counts steps ahead in the pre-built dataset (k = 1, 5 and 10 are compared) rather than defining a new time clock. For the crypto-asset data the authors build fixed-interval bars themselves: order book information is aggregated to a five-minute interval within an hourly-resolution feed, and the portfolio-rebalancing model re-weights the portfolio on a fixed 50-minute clock regardless of price activity.

## Data

- **Asset class:** Several asset classes
- **Instruments:** FI-2010: five stocks on Nasdaq Nordic; crypto-asset dataset: BTC, LTC and ETH (trained and tested), with XRP held out entirely for transfer-learning tests; the portfolio experiment builds a portfolio of 4 crypto-assets
- **Venue:** Nasdaq Nordic stock market (FI-2010 source); Binance exchange (crypto order book data, via its public API)
- **Period:** FI-2010: ten consecutive trading days; crypto dataset: one year starting February 27, 2019, at hourly resolution; the portfolio backtest test window begins around February 2020
- **Granularity:** FI-2010: per-event LOB snapshots, sliding window of length 100; crypto: the ten best bid and ask levels aggregated into five-minute intervals within an hourly feed, sliding window of length 60, with portfolio rebalancing every 50 minutes

## Features and Measures

- **Mid-price.** The average of the best ask price and best bid price at each point in the data, used as the reference price for computing trend labels.
- **Smoothed price-trend label (l_t).** A three-way label (increase, decrease, or hold) built from the average of the k previous and k following mid-prices, with a threshold alpha = 0.001 marking whether the relative change is large enough to count as a move.
- **Sharpe-ratio loss.** A training objective for the portfolio-weighting network that directly maximizes an estimate of the Sharpe ratio of the resulting portfolio's returns.
- **Minimum-volatility loss.** An alternative training objective that instead minimizes the standard deviation (volatility) of portfolio returns.

## Method

DeepFolio's price-trend module (ResCNN+GRU) is trained with the Adam optimizer at a learning rate of 0.01, with early stopping and checkpointing triggered after 20 epochs without validation improvement, and L2-normalization to control overfitting. Performance on FI-2010 is judged by accuracy, precision, recall and F1; on the crypto data, where classes are unbalanced, the authors emphasize weighted F1. Results are compared against CNN and LSTM baselines and against DeepLOB, run under a matching setup.

For the portfolio stage, the price-trend labels produced every 50 minutes feed an LSTM with 64 units followed by a softmax layer that outputs portfolio weights; this stage is trained with Adam at a learning rate of 0.001 and a batch size of 64, using either the Sharpe-ratio loss or the minimum-volatility loss. The resulting portfolio strategies are evaluated by cumulative log-returns, expected and mean return, return standard deviation, Sharpe ratio, and the ratio of positive to negative return periods, against a Markowitz mean-variance portfolio (under both Sharpe-ratio and minimum-volatility criteria) and a naive equal-weighted (1/n) portfolio, with no transaction costs included.

## Results

- On FI-2010, DeepFolio and DeepLOB both clearly beat the CNN and LSTM baselines across accuracy, precision, recall and F1, and DeepFolio edges out DeepLOB on every metric, with the gap between them widening as the prediction horizon k grows.
- On the Bitcoin order-book data, DeepLOB needs more than 30 epochs before its training loss starts to drop, while DeepFolio's ResCNN+GRU module starts dropping around epoch 8-9.
- DeepFolio is far less sensitive than DeepLOB to the choice of initial weights: DeepLOB's training loss on the crypto data depends heavily on whether default or Glorot-style initialization is used, while DeepFolio trains well under either.
- Keeping batch normalization in the residual blocks gives a higher (worse) validation loss than leaving it out, so the authors drop batch normalization from DeepFolio's residual blocks.
- In the multi-asset generalization tests (train on BTC, LTC and ETH, test on the held-out XRP asset), DeepFolio outperforms DeepLOB in most cases, with average gaps of about 2-3%.
- In the portfolio backtest, DeepFolio trained with the Sharpe-ratio loss achieves the highest expected return (1.467931) and Sharpe ratio (0.053069) of all the strategies tested, versus a Sharpe ratio of 0.040234 for the naive 1/n portfolio and 0.025998 for the Markowitz Sharpe-ratio portfolio.
- The crypto-asset dataset has less than 6% missing values, handled mainly by carrying forward the last valid value rather than interpolating.

## Limitations

- The crypto-asset portfolio backtest ignores transaction costs.
- The crypto dataset is described as more scarce than FI-2010, which the authors say favors smaller models and may limit performance on less liquid assets.
- Reader note: the FI-2010 benchmark covers only five stocks over ten trading days, a narrow equity sample.
- Reader note: the crypto-asset test period overlaps the onset of the COVID-19 market shock, an unusual regime that may not generalize to calmer markets.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Aiusha Sangadiev, Rodrigo Rivera-Castro, Kirill Stepanov, Andrey Poddubny, Kirill Bubenchikov, Nikita Bekezin, Polina Pilyugina, Evgeny Burnaev (2020). DeepFolio: Convolutional Neural Networks for Portfolios with Limit Order Book Data.

DOI: 10.48550/arxiv.2008.12152

Text ingested: `markdown_output/sangadiev-2020-deepfolio-convolutional-neural-networks-portfolios-limit.md`, converted from `raw/ofi-event-clock/sangadiev-2020-deepfolio-convolutional-neural-networks-portfolios-limit.pdf`.

Coverage of this summary: Read the full converted markdown text: introduction, related work, data sections (FI-2010 and crypto-asset datasets), model architecture, the portfolio optimization model, the experiments section and both results tables' surrounding prose, and the conclusion.

Known problems with the input: year from file metadata; Several equations and figures are omitted as images ('picture... intentionally omitted'), so exact loss-function and label-smoothing formulas could not be verified beyond the prose description; Tables I-III (the FI-2010 and first crypto-dataset results) have OCR-scrambled rows and columns; exact per-model accuracy figures could not be reliably attributed to the right model, so they are omitted from results and only Table IV (which reads cleanly) is used for numeric claims; No venue (journal or conference) name is printed in the extracted text.
<!-- AUTHORED REGION END -->