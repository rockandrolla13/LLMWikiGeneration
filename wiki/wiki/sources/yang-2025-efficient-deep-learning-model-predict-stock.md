---
authors:
- Jiahao Yang
- Ran Fang
- Ming Zhang
- Jun Zhou
content_hash: sha256:0bf95cb9edef4e1e2f475053b062941a881029b3a7a6fa911bc7a31a84d8cb5a
created: 2026-09-27 01:47:00+00:00
page_id: sources/yang-2025-efficient-deep-learning-model-predict-stock
page_type: source
related:
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/lstm-networks
- concepts/transformers
- concepts/multi-head-attention
revision_id: 1
schema_version: 2
source_hash: sha256:e1efc992364a361dd12ecdfcbe5d00174e5853f71bae6314a223eec3368854b7
source_path: markdown_output/yang-2025-efficient-deep-learning-model-predict-stock.md
source_type: paper
tags:
- limit-order-book
- order-flow-imbalance
- siamese-network
- multi-head-attention
- china-a-share-market
- deep-learning
- high-frequency-trading
- clock-calendar
- asset-equity
- harvest-relevant
title: An Efficient deep learning model to Predict Stock Price Movement Based on Limit
  Order Book
updated: '2026-09-27T01:47:00Z'
uuid: 99c1d07c-6493-515b-8fff-d408000783f0
year: 2025
---

<!-- AUTHORED REGION START -->
# An Efficient deep learning model to Predict Stock Price Movement Based on Limit Order Book

## Summary

The paper asks whether a deep learning model for predicting short-horizon limit-order-book price changes can be improved by exploiting the built-in symmetry between the bid and ask sides of the order book, and separately, whether adding multi-head attention to an LSTM helps forecast price changes in the Chinese A-share market, which the authors say has received far less research attention than the US and European markets.

The approach has two parts. First, a Siamese architecture processes the ask-side and bid-side halves of the order book with two encoders that share the same parameters, then a decoder predicts the price change from the difference between the two encoded representations; this is applied on top of several existing baseline encoders (MLP, stacked LSTM, MLP-LSTM, CNN-LSTM). Second, an LSTM-MHA architecture stacks a multi-head attention layer after a stacked LSTM to see whether attention over past time steps improves forecasts. Both the raw limit order book state and order-flow-imbalance (OFI) features derived from it are tested as inputs, using level-II data for 14 A-share defense-industry stocks between 6 January 2021 and 13 May 2021.

The main finding is that the Siamese framework improves forecasting accuracy (measured by MAE, MSE and out-of-sample R2) over the corresponding non-Siamese baseline for almost every architecture, feature and horizon combination tested, and that OFI features outperform raw LOB features for every architecture except MLP. Multi-head attention on top of the LSTM helped most at the shortest forecasting horizon tested.

What is new is the Siamese, parameter-sharing treatment of the bid/ask symmetry in limit order book data, which the authors say has not previously been used for this task, together with an empirical study of multi-head attention and OFI features specifically on the Chinese A-share market rather than the US/European markets that most prior LOB deep-learning work has focused on.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Observations are level-II limit order book snapshots that the exchange publishes at fixed intervals (every three seconds), producing about 4500-5000 such ticks per trading day; the paper treats each snapshot as one tick. Each input sample uses 50 historical ticks (the past 49 ticks plus the current one, about 150 seconds of history) to predict the change in the mid-price over a forecasting horizon of h ticks, with h = 10, 20 or 50 tested, corresponding to roughly 0.5, 1 and 2.5 minutes ahead.

## Data

- **Asset class:** Equities
- **Instruments:** 14 defense-industry-related A-share stocks: 003026.SZ, 300864.SZ, 300870.SZ, 300877.SZ, 300881.SZ, 300886.SZ, 300892.SZ, 300896.SZ, 300898.SZ, 300908.SZ, 300910.SZ, 300919.SZ, 300925.SZ, 300999.SZ
- **Venue:** China A-share market (the paper does not name a specific exchange)
- **Period:** 6 January 2021 to 13 May 2021
- **Granularity:** level-II limit order book data, top 10 bid and ask price/volume tiers, published every three seconds (about 4500-5000 ticks per day)

## Features and Measures

- **Order Flow Imbalance (OFI) features.** Bid order flow (bOF) and ask order flow (aOF) computed from the change in price and volume at each of the top ten order book tiers between two consecutive snapshots, concatenated into a combined order-flow-imbalance state that the paper reports as more stable over time than the raw order book levels.
- **Siamese architecture for the limit order book.** Two identical encoders with shared parameters that separately process the ask-side and bid-side halves of the order book; a decoder then predicts the price change from the difference between the two resulting feature vectors, exploiting the bid/ask symmetry of the data.
- **LSTM-MHA.** The paper's proposed architecture: a stacked LSTM whose final layer is replaced by a multi-head attention layer that recombines the LSTM's cell states across time steps before a linear layer predicts the price change.

## Method

The paper formulates price forecasting as a regression problem: for each stock and trading tick, the target is the change in mid-price over the next h ticks (h = 10, 20 or 50), capped at an absolute value of 1 CNY to limit the influence of rare large jumps, and the previous trading day's closing price is subtracted from the input series to remove overnight jumps before training. Five architectures are compared: a 3-hidden-layer MLP (500, 250 and 64 hidden units, taking a flattened 2000-dimensional LOB input or 1000-dimensional OFI input), a stacked 3-layer LSTM (64 hidden units per layer, concatenated to 192 units before a linear output layer, with input dimension 40 for LOB or 20 for OFI), an MLP-LSTM (a 128-unit MLP layer feeding the stacked LSTM), a CNN-LSTM (an inception-style front end with 1-dimensional convolution kernels of sizes 1, 3, 5 and 7 whose outputs are concatenated to 64 dimensions before the LSTM), and the paper's own LSTM-MHA (two LSTM layers followed by a multi-head attention layer, with model dimension D=64 and K=4 attention heads). Two full Transformer variants (4-layer causal and non-causal, hidden dimension 64) were also tried but performed worse than every other baseline. Each architecture is trained separately on raw LOB features and on OFI features, and its Siamese version halves the per-side input dimension, processing the ask and bid sides through a shared-parameter encoder before a 2-layer MLP decoder predicts the price change from the difference of the two encoded representations.

Models are trained by minimising mean absolute error with the Adam optimiser (beta1=0.9, beta2=0.999, eps=1e-8, initial learning rate 0.0001, weight decay 0.001, batch size 256), with early stopping after 5 consecutive epochs without validation-loss improvement; hyperparameters were selected by grid search over learning rates between 1e-3 and 1e-4, weight decay of 0.01 or 0.001, and batch sizes of 64, 256 or 512. Experiments were run on a server with a Tesla P100 GPU (12GB) and an Intel Xeon CPU (2.40GHz, 128.0GB RAM), using PyTorch.

Evaluation uses a rolling-window split (one week validation, five weeks training, one week out-of-sample testing) across the 14 A-share stocks from 6 January 2021 to 13 May 2021, giving 149 test sets in total (10 or 11 per stock). Performance is judged by mean absolute error (MAE), mean squared error (MSE), and an out-of-sample R2 that compares each model's MSE against the average out-of-sample return as a benchmark; models are also ranked against one another by MSE across all test sets, stocks and horizons.

## Results

- The Siamese framework improved MSE and out-of-sample R2 over the corresponding non-Siamese baseline for nearly every model, feature and horizon combination tested, using either raw LOB or OFI inputs, at the 10, 20 and 50 tick horizons.
- Except for MLP, OFI-based inputs outperformed raw LOB inputs for every architecture tested; for example, at the 10-tick horizon the original-LOB MLP beat the OFI-based MLP on 60 of the test sets while the OFI-based MLP won on 89.
- The MLP baseline performed markedly worse than the other four architectures (stacked LSTM, MLP-LSTM, CNN-LSTM, LSTM-MHA) on the A-share data and is described by the authors as impractical.
- The proposed LSTM-MHA architecture performed worse than the other baselines on raw LOB input but better than the other baselines when given OFI input, and the authors report that multi-head attention helped most at the shortest horizon tested (10 ticks, about 0.5 minutes ahead).
- Two full Transformer variants (a 4-layer causal and a 4-layer non-causal version, hidden dimension 64) were also tried and performed worse than all other baselines.
- Results are based on 14 A-share defense-industry stocks traded between 6 January 2021 and 13 May 2021, each contributing 10 or 11 rolling test sets for a total of 149 test sets used to rank the models.

## Limitations

- The authors state that the validity of the Siamese architecture on the U.S. and European stock markets has not been verified.
- The authors state that the features used are relatively simple and the model's capability on more complex features has not been validated.
- The authors state that they have not developed or tested a practical profit-making trading strategy from the forecasts.
- Reader note: results are reported for a single, narrow universe of 14 A-share defense-industry stocks over about four months, so generalisation to other sectors or longer periods is not demonstrated.
- Reader note: the two Transformer baselines are reported only as underperforming, without their own MAE/R2 figures given alongside the other models in the results tables, limiting direct comparison.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/transformers|transformers]]
- [[concepts/multi-head-attention|multi head attention]]

## Citation

Jiahao Yang, Ran Fang, Ming Zhang, Jun Zhou (2025). An Efficient deep learning model to Predict Stock Price Movement Based on Limit Order Book.

DOI: 10.48550/arxiv.2505.22678

Text ingested: `markdown_output/yang-2025-efficient-deep-learning-model-predict-stock.md`, converted from `raw/ofi-event-clock/yang-2025-efficient-deep-learning-model-predict-stock.pdf`.

Coverage of this summary: Read the full markdown file end to end: abstract, introduction, related work, data/feature/methodology section, experiment results and discussion, conclusion, references, and the appendix listing baseline model details.

Known problems with the input: year from file metadata (no publication year is printed in the converted text, only a 'Springer Nature 2021' LaTeX template marker which is not a publication date; the job file's year_hint of 2025 was used); venue/journal name is not printed in the converted text and is left empty; author-to-affiliation mapping is not given in the converted text; two institutional affiliations are listed for the author group as a whole without indicating which author belongs to which; many equations and all figures were rendered as omitted-picture placeholders or garbled inline math, so exact formulas (e.g. the OFI and R2 definitions) could not be fully verified from this markdown; Tables 2-6 rendered with column/row alignment broken by the PDF-to-markdown conversion, so their individual cell values could not be reliably attributed to specific models/horizons; only unambiguous numbers stated in the prose (e.g. the Table 2 caption example) were used.
<!-- AUTHORED REGION END -->