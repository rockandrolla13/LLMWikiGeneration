---
authors:
- Paul Bilokon
- Yitao Qiu
content_hash: sha256:b67a8518cd91f9da87ef21fea541a941e684020bb1e26102d21d7d9e9bf86dcc
created: 2026-09-27 01:47:00+00:00
page_id: sources/bilokon-2023-transformers-versus-lstms-electronic-trading
page_type: source
publication_venue: Preprint
related:
- concepts/trade-clock
- concepts/limit-order-book
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/transformers
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/backtesting
- concepts/market-microstructure
- concepts/mid-price-prediction
- concepts/micro-price
revision_id: 1
schema_version: 2
source_hash: sha256:a6cf6cc4e6fd798bcbeda0cab442abd71abc50aaf681b5e29f5af15b6b8a15d7
source_path: markdown_output/bilokon-2023-transformers-versus-lstms-electronic-trading.md
source_type: paper
tags:
- transformers
- lstm
- limit-order-book
- high-frequency-trading
- cryptocurrency
- price-movement-prediction
- deep-learning
- trading-simulation
- clock-trade
- asset-crypto
- harvest-relevant
title: Transformers versus LSTMs for Electronic Trading
updated: '2026-09-27T01:47:00Z'
uuid: 912ed296-5179-52d7-9183-60b771b5d1e5
year: 2023
---

<!-- AUTHORED REGION START -->
# Transformers versus LSTMs for Electronic Trading

## Summary

The paper asks whether Transformer-based sequence models can beat LSTM-based models at financial time series prediction from high-frequency limit order book (LOB) data, given that Transformers had displaced RNNs in NLP but LSTM remained the dominant architecture in finance. It compares a canonical LSTM and three LOB-specific LSTM variants (DeepLOB, DeepLOB-Seq2Seq, DeepLOB-Attention) against a vanilla Transformer and four long-sequence Transformer variants (LogTrans, Reformer, Informer, Autoformer, FEDformer) on three tasks built from Binance cryptocurrency order book data: predicting the absolute mid-price, predicting the mid-price difference, and classifying mid-price movement (rise, stationary, fall).

The authors also propose two innovations. First, they adapt the Transformer-based regression models to the movement-classification task by feeding the whole predicted mid-price sequence into a linear and softmax layer, rather than a single next-step value. Second, they introduce DLSTM, a new model that decomposes the input into a trend series and a remainder series (following the decomposition idea in Autoformer and the Dlinear model), passes each through its own LSTM layer, and sums the resulting hidden states before a final classification layer.

On absolute mid-price prediction, FEDformer and Autoformer had lower error (MSE/MAE) than LSTM, but out-of-sample R2 was negative for every model, which the authors interpret as making these absolute-price forecasts useless for trading despite the lower error metrics. On mid-price difference prediction, canonical LSTM was the strongest and most robust model, reaching an out-of-sample R2 of about 11.5%; FEDformer and Autoformer could not be evaluated here because their decomposition architecture is unsuited to the (nearly stationary) difference series. On mid-price movement classification, the new DLSTM model had the best accuracy at every horizon tested, and in a simple trading simulation it kept the highest cumulative return and Sharpe ratio once a hypothetical transaction cost was introduced, while Transformer-based models' simulated profitability fell sharply under that cost.

What is new relative to prior LOB deep-learning work is the systematic three-task comparison of Transformer families (previously tested mainly on non-financial long-sequence forecasting) against established LSTM/CNN-LSTM baselines on the same LOB data, the DLSTM architecture, the adapted Transformer output head for one-step classification, and a trading simulation that reports profitability both with and without transaction costs.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are individual exchange ticks from Binance's limit order book, arriving at irregular intervals (about 0.1 second apart on average in the task 1 dataset) rather than fixed time steps. The prediction horizon k is expressed in numbers of ticks ahead: k in {96, 192, 336, 720} for the mid-price and mid-price-difference prediction tasks, and k in {20, 30, 50, 100} for the mid-price movement classification task, where k is also the window used on each side to smooth the movement label (comparing the average of the previous k mid-prices to the average of the next k mid-prices).

## Data

- **Asset class:** Crypto
- **Instruments:** BTC-USDT (tasks 1 and 2, mid-price and mid-price-difference prediction) and ETH-USDT (task 3, mid-price movement prediction), from Binance Exchange limit order book data with market depth of 10 levels per side
- **Venue:** Binance Exchange, collected via the cryptofeed WebSocket API and stored using kdb+tick
- **Period:** Task 1: one day, 2022.07.15 (863397 ticks). Task 2: 2022.07.03 to 2022.07.06 inclusive, four days (3432211 ticks). Task 3: 2022.07.03 to 2022.07.14 inclusive, twelve days (10255144 ticks); the trading simulation used the final three days of that window, and a longer window from 2022.07.13 to 2022.07.24 was used for the Sharpe ratio experiment under increasing transaction cost.
- **Granularity:** Tick-by-tick limit order book snapshots, irregular in time (about 0.1 second apart on average), with order book depth of 10 levels per side.

## Features and Measures

- **mid-price.** The average of the best bid and best ask price in the limit order book at a given time; used as the primary target for the absolute-price and price-difference prediction tasks.
- **micro-price / order-book imbalance feature (I).** A feature computed per order-book depth level, called the 'imbalance' by the authors, that combines price and volume information following Oomen and Gatheral's micro-price definition; it is produced inside DeepLOB's second convolutional block.
- **mid-price movement label.** A three-class label (rise, stationary, fall) formed by comparing the average of the previous k mid-prices with the average of the next k mid-prices; the percentage change between the two averages is compared against a threshold delta, calibrated per horizon so the three classes are roughly balanced.

## Method

Canonical LSTM (with forget, input and output gates) is compared against three LOB-specific LSTM variants from prior work: DeepLOB (convolutional blocks plus an Inception-style decomposition module feeding a single LSTM layer), DeepLOB-Seq2Seq (adds an encoder-decoder for multi-horizon forecasting) and DeepLOB-Attention (replaces the Seq2Seq context vector with an attention mechanism). On the Transformer side, the vanilla Transformer (multi-head self-attention with a learnable timestamp encoding in place of word embeddings) is compared against four long-sequence variants from prior work - LogTrans, Reformer, Informer, Autoformer and FEDformer - which mainly differ in how they approximate or restructure the self-attention computation to reduce its time and memory cost.

For the mid-price movement classification task, the Transformer-based models are adapted to feed their whole predicted mid-price sequence, rather than a single next-step value, into a linear and softmax layer. The authors also introduce DLSTM, which decomposes the input into a trend series (via average pooling) and a remainder series, passes each through its own LSTM layer, and sums the resulting hidden states before a final linear and softmax layer.

All models were trained with the Adam optimiser and early stopping for 10 epochs (L2 loss for the two regression tasks, cross-entropy loss for the classification task), implemented in PyTorch on a single NVIDIA GPU. Tasks 1 and 2 used a batch size of 32 and an initial learning rate of 1e-4; task 3 used a batch size of 64. Task 1 used a 70%/10%/20% train/validation/test split of its single day of data; task 2 used an 80% training split with the remaining 20% split evenly between validation and test; task 3 used the first six of twelve days for training and the last three for testing, with the remainder for validation. The two regression tasks were judged by MSE, MAE and out-of-sample R2; the classification task by accuracy, precision, recall and F1; and a simple trading simulation (enter a long or short position on the predicted movement class, hold until the opposite signal, with a fixed order-execution delay) was judged by cumulative price return (CPR) and annualised Sharpe ratio, both with and without a hypothetical 0.002% transaction cost.

## Results

- FEDformer had the lowest error on absolute mid-price prediction, giving a 24% MSE reduction versus LSTM at prediction length 96 (0.104 to 0.0793) and a 21% reduction at length 336 (0.771 to 0.608); Autoformer gave an 11% reduction at length 96 (0.104 to 0.0926) and 16% at length 336 (0.771 to 0.643).
- Despite lower MSE/MAE for FEDformer and Autoformer, out-of-sample R2 for mid-price prediction was negative for every model tested, which the authors interpret as making the absolute-price forecasts useless for trading.
- On mid-price difference prediction, canonical LSTM reached the highest out-of-sample R2 of around 11.5%, outperforming the Transformer, Informer and Reformer models tested on that task.
- FEDformer and Autoformer could not be compared on the price-difference task because their time-decomposition architecture is designed for non-stationary series and performs poorly on the (approximately stationary) difference series.
- The new DLSTM model achieved between 63.73% and 73.31% accuracy on mid-price movement classification across the four horizons tested (20, 30, 50, 100 ticks), outperforming all LSTM-based and Transformer-based baselines at every horizon.
- In the trading simulation, LSTM-based models were generally more profitable than Transformer-based models, and under a hypothetical 0.002% transaction cost DLSTM had the highest cumulative price return and annualised Sharpe ratio at every prediction horizon.
- Autoformer's simulated profitability fell the most under the transaction cost, at times underperforming the plain Transformer despite having better classification metrics.
- LSTM-based models had lower inference time and memory consumption than the Transformer variants tested, and training FEDformer or Autoformer took more than 12 hours even on a 24GB NVIDIA RTX 3090 GPU.

## Limitations

- Reader note: all experiments use a single cryptocurrency pair per task (BTC-USDT for tasks 1 and 2, ETH-USDT for task 3) on a single exchange (Binance), so the comparative results may not generalise to other assets or venues.
- The authors themselves note that the mid-price prediction task produces forecasts with negative out-of-sample R2 for every model, meaning low MSE/MAE on this task does not translate into a usable trading signal.
- The authors state the simulated trading experiment assumes no market impact and mid-price execution with a fixed delay, describing these as unrealistic assumptions that produce an enormous annualised Sharpe ratio.
- The authors note FEDformer and Autoformer could not be evaluated on the price-difference task because their built-in time-decomposition architecture is unsuited to an approximately stationary series.
- Reader note: the mid-price prediction task (task 1) uses only one trading day of data (863397 ticks), a short window, even though the authors argue this is sufficient for that specific sub-task based on precedent from non-financial forecasting work.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/transformers|transformers]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/backtesting|backtesting]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[concepts/micro-price|Micro-Price]]

## Citation

Paul Bilokon, Yitao Qiu (2023). Transformers versus LSTMs for Electronic Trading. Preprint.

DOI: 10.2139/ssrn.4577922

Text ingested: `markdown_output/bilokon-2023-transformers-versus-lstms-electronic-trading.md`, converted from `raw/ofi-event-clock/bilokon-2023-transformers-versus-lstms-electronic-trading.pdf`.

Coverage of this summary: Read the full markdown file (abstract, introduction, related work, all three task formulations, methodology sections for LSTM/Transformer/DLSTM, all experiment and results subsections, efficiency comparison, conclusion, and appendix A on labelling thresholds).

Known problems with the input: Several results tables (e.g. Tables 1-8) were flattened into single garbled cells by the PDF-to-markdown conversion, mixing model names, metrics and prediction-horizon columns together; numbers used in this record were only taken from clearly stated running prose (including the abstract), not reconstructed from those ambiguous table cells.
<!-- AUTHORED REGION END -->