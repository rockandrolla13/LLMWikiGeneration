---
authors:
- Guilherme Augusto Bileki
content_hash: sha256:88ea474447e10a8b3053bc86882de2907be8709efcea826340aa1018d0dbfb29
created: 2026-09-27 01:47:00+00:00
page_id: sources/bileki-2021-uma-abordagem-com-modelo-de-aprendizado
page_type: source
publication_venue: Instituto de Ciências Matemáticas e de Computação, Universidade
  de São Paulo (Master's dissertation, Programa de Pós-Graduação em Ciências de Computação
  e Matemática Computacional)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
- concepts/feature-engineering
- concepts/high-frequency-trading
- concepts/lstm-networks
- concepts/market-microstructure
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:bed16a1668c68c5492a20480e51321a190cbb46611d36949e324ec82506770cd
source_path: markdown_output/bileki-2021-uma-abordagem-com-modelo-de-aprendizado.md
source_type: paper
tags:
- limit-order-book
- mid-price-prediction
- cnn
- catboost
- brazilian-market
- b3-exchange
- hybrid-model
- shap-analysis
- clock-event
- asset-multi
- harvest-relevant
title: Uma abordagem com modelo de aprendizado de máquina híbrido para predição de
  movimentos de preço médio de ativos pelo livro de ofertas
updated: '2026-09-27T01:47:00Z'
uuid: 6616e410-5269-5e78-b766-788090860f77
year: 2021
---

<!-- AUTHORED REGION START -->
# Uma abordagem com modelo de aprendizado de máquina híbrido para predição de movimentos de preço médio de ativos pelo livro de ofertas

## Summary

The thesis addresses mid-price movement prediction from limit order book data. Most prior work treats this as a classification problem (up/down/stationary) solved end-to-end by a single neural network, evaluated mainly on the Nasdaq Nordic FI-2010 benchmark. Unlike most exchanges, the order-message feed of the Brazilian exchange (B3) records which brokerage submitted each order, and the thesis asks whether this extra information helps, and whether separating feature extraction (a convolutional network) from final classification (a tree-based model) improves on an end-to-end network.

Two datasets are used: the public FI-2010 benchmark (five Nasdaq Nordic stocks, ten consecutive trading days in June 2010, a 10-price-level order book) and a newly assembled B3-2020 dataset built by extending an existing order-book reconstruction simulator to also output LOBSTER-style order-book and message files from raw B3 exchange feeds, covering five one-day interbank-deposit-rate futures contracts (the BMF set) and five liquid B3 equities (the VISTA set). Labels follow a smoothed mid-price scheme that compares the average mid-price over k order-book events before and after a point against a threshold alpha to classify the move as up, down, or stationary. The model architecture uses a convolutional network (in two published kernel configurations) to extract a fixed-length feature vector from a rolling window of order-book events; this vector is then classified either by an LSTM, an MLP, or, in the proposed hybrid model, by a separately trained CatBoost gradient-boosted-tree classifier, optionally concatenated with message-file fields such as price, volume, event type, and broker identifier. Feature importance is inspected with SHAP.

The CNN feature extractor trained on B3 data behaves similarly to its behavior on FI-2010, suggesting it generalizes across markets. Replacing the LSTM classification head with a plain MLP barely changes accuracy while cutting extractor training time substantially. Adding CatBoost on top of the CNN features raises accuracy further, and adding message-file information (mainly price and volume, less so the broker field) adds a further improvement; combined, this amounts to roughly an 8-percentage-point accuracy gain over a plain end-to-end CNN, though CatBoost inference is markedly slower than the neural network alone. Extractors trained on one instrument set transfer to another instrument set in far less training time than retraining a network from scratch.

The thesis presents this hybrid CNN-plus-tree pipeline with optional broker-identity features as its main contribution, describing it as the first work to combine these two elements, and it also demonstrates cross-instrument and cross-dataset transfer of the CNN extractor between the Nordic benchmark and the newly built Brazilian dataset.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each model input is a rolling window of 100 consecutive order-book update events, represented as 40 columns (10 price levels of bid/ask price and volume). Labels compare the average mid-price of the k order-book events before a point to the average mid-price of the k events after it (k values tested include 10, 20, 50 and 100), classifying the move as up, down, or stationary once the relative change crosses a threshold alpha chosen so about 80% to 90% of labels fall in the stationary class. Both the input window and the prediction horizon are defined in counts of order-book/message events, not in wall-clock time.

## Data

- **Asset class:** Several asset classes
- **Instruments:** FI-2010: 5 stocks from Nasdaq Nordic (the public benchmark of Ntakaris et al., 2018). B3-2020 BMF set: 5 one-day interbank-deposit-rate futures contracts (DI1F20, DI1F21, DI1F23, DI1F25, DI1F27) traded on the futures (BMF) segment of B3. B3-2020 VISTA set: 5 high-liquidity B3 equities (ABEV3, ITUB4, MGLU3, PETR4, VALE3).
- **Venue:** Nasdaq Nordic (for FI-2010) and B3 – Brasil, Bolsa, Balcão, covering both its futures (BMF) and cash equity (VISTA) segments
- **Period:** FI-2010: June 1 to June 14, 2010 (10 consecutive trading days). B3-2020 futures (DI1F20): November 1 to December 20, 2017. B3-2020 equities: August 1 to November 30, 2019.
- **Granularity:** Order-book and message-level (event-by-event) data reconstructed into LOBSTER-style order-book and message files; FI-2010 keeps only 10 price levels (40 columns) per snapshot and its public release is further summarized to one record per 10-event sequence

## Features and Measures

- **10-level order book snapshot.** the ask and bid price and volume at the 10 best price levels on each side of the book at a given event, 40 numbers in total, used as the raw input to the CNN
- **prior-day z-score normalization.** each price or volume column is standardized using the mean and standard deviation computed from the previous trading day, to reduce day-to-day scale differences across instruments
- **k/alpha mid-price labeling.** a 3-class label (up, down, stationary) built by comparing the mean mid-price of the k events before a point to the mean mid-price of the k events after it, classifying the move as up or down only if the relative change exceeds a threshold alpha
- **message-file features.** per-event fields from the B3 order-message feed – the time gap since the previous event, order direction, event type (insertion, modification, cancellation, trade, or expiration), price, volume, and the identifier of the broker that submitted the order – optionally concatenated to the CNN-extracted order-book feature vector
- **CNN feature extractor (two kernel configurations).** a convolutional network, following Zhang, Zohren and Roberts, that reduces a 100-event order-book window to a fixed-length feature vector, in a 'version 1' configuration that looks at the whole current order book and a 'version 2' configuration that first extracts price-volume relations per level, both followed by an Inception-style parallel-kernel block

## Method

The CNN feature extractor is first trained end-to-end with either an LSTM or an MLP classification head, reproducing a published baseline architecture and a simplified variant of it. Once trained, the classification head is discarded and the CNN is used purely as a feature extractor; its output feeds a separately trained CatBoost gradient-boosted-tree classifier (1000 iterations, default library parameters), optionally with message-file features concatenated in, forming the proposed hybrid model. Data are split by trading day, following a 70%/30% train/test split used in prior related work, and models are compared on log-loss, accuracy, precision, recall and F1-score on held-out test days, with CatBoost and CNN inference latency timed separately. A SHAP analysis ranks the contribution of each order-book and message feature to each predicted class. Training ran on a single machine (Intel Core i7-8750H CPU, NVIDIA GeForce GTX 1070 GPU, 32GB RAM) using TensorFlow in Python.

## Results

- On the FI-2010 benchmark, the CNN-MLP-v2 pair reached 0.77 accuracy, 0.76 precision, 0.73 recall and an F1-score of 0.79, matching the CNN-LSTM (DeepLOB) v2 pair's accuracy while cutting extractor training time from 1144s to 181s.
- Replacing the LSTM classifier head with a plain MLP cut CNN extractor training time by 93% for architecture version 1 and 84% for version 2, with only a small change in accuracy.
- On the B3 futures (BMF) set with 25% of filters, adding CatBoost on top of CNN version 2 features raised accuracy from 0.606 (plain MLP, no messages) to 0.652 (CatBoost, no messages) and further to 0.673 (CatBoost, with message features).
- Adding message-file fields to the CatBoost classifier consistently improved accuracy by a further two to three points beyond CatBoost without messages, seen on both the BMF set (0.652 to 0.673) and the VISTA equity set.
- The thesis abstract reports an overall accuracy improvement of about 8% versus a plain end-to-end CNN, made up of about 5 percentage points from the CatBoost classifier and a further 3 percentage points from the message-file features.
- Per-model inference time on FI-2010 was about 2.1ms to 2.4ms for the CNN pairs alone, rising by roughly 1.4ms more when CatBoost was added, an inference-time increase of more than 50%.
- SHAP analysis showed order-book-derived CNN features dominated variable importance for both the BMF and VISTA sets, with message price and volume fields contributing a smaller but consistent effect and the broker-identifier field having only a marginal effect on classification.
- In cross-transfer tests, a CNN extractor trained on the multi-instrument BMF set for 10 days with a CatBoost classifier trained on 32 days of single-instrument DI1F20 data reached an F1-score of 0.73, and a BMF extractor trained on 32 days with a classifier trained on 10 days of DI1F20 data reached an F1-score of 0.75, compared with only 0.37 when both extractor and classifier were confined to a single-instrument DI1F20 set trained at different prediction horizons (k=10 versus k=100).

## Limitations

- FI-2010 is limited to 10 consecutive trading days and 5 Nordic stocks, and its public release contains only one summarized record per 10-event sequence.
- The B3-2020 futures and equity sets are drawn from short, non-overlapping calendar windows (10 to 32 trading days), explicitly chosen to avoid an election period.
- Several model configurations (higher percentages of CNN filters on the B3 sets) overfit, so reported results depend on manually reducing model complexity for each dataset and prediction-horizon combination.
- Reader note: the broker-identity finding rests on a single classifier (CatBoost) and a single k/alpha choice per dataset; alternative classifiers with the broker feature are not tested.
- Reader note: only one pair of B3-2020 subsets (10 versus 32 trading days) is used to study the effect of more training data, and no out-of-sample trading backtest is reported.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]

## Citation

Guilherme Augusto Bileki (2021). Uma abordagem com modelo de aprendizado de máquina híbrido para predição de movimentos de preço médio de ativos pelo livro de ofertas. Instituto de Ciências Matemáticas e de Computação, Universidade de São Paulo (Master's dissertation, Programa de Pós-Graduação em Ciências de Computação e Matemática Computacional).

DOI: 10.11606/d.55.2021.tde-20052021-111418

Text ingested: `markdown_output/bileki-2021-uma-abordagem-com-modelo-de-aprendizado.md`, converted from `raw/ofi-event-clock/bileki-2021-uma-abordagem-com-modelo-de-aprendizado.pdf`.

Coverage of this summary: Read the title/cover pages, both abstracts (Portuguese and English), the full introduction chapter, the materials-and-methods chapter in full (workflow, both datasets, LOB and message preprocessing, labeling, the CNN feature extractor, the hybrid training pipeline, and the six experiment questions), the entire results chapter for FI-2010 and both B3 datasets including the cross-dataset transfer experiments, and the conclusions and future-work chapter. Skimmed the table of contents and reference list of the related-work chapter without reading its body.

Known problems with the input: The document is in Portuguese with an English abstract; the thesis's own equations for transaction time, mid-price, and the k/alpha labeling ratio (Equations 4.1-4.5) are rendered as omitted pictures in the markdown, so only the prose description of these could be used; Some table headers are visually garbled by the PDF conversion (e.g. 'fltros' for 'filtros', 'Acurcia' variants), but the numeric values in the data rows were legible and used as printed.
<!-- AUTHORED REGION END -->