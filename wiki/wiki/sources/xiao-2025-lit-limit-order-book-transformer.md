---
authors:
- Yue Xiao
- Carmine Ventre
- Yuhan Wang
- Haochen Li
- Yuxi Huan
- Buhong Liu
content_hash: sha256:f76096ecb5e682eaf6d509ce57a01500ad7d887f7e49cc7a9b457d1db64f7f97
created: 2026-09-27 01:47:00+00:00
page_id: sources/xiao-2025-lit-limit-order-book-transformer
page_type: source
publication_venue: Frontiers in Artificial Intelligence
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/transformers
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
revision_id: 1
schema_version: 2
source_hash: sha256:4e51c5bb6f13b21b1ab47295d50961528fc5fef6e304ec621fe98c2758975758
source_path: markdown_output/xiao-2025-lit-limit-order-book-transformer.md
source_type: paper
tags:
- transformers
- limit-order-book
- crypto-markets
- deep-learning
- price-forecasting
- fine-tuning
- patch-embedding
- high-frequency-trading
- clock-event
- asset-crypto
- harvest-relevant
title: 'LiT: limit order book transformer'
updated: '2026-09-27T01:47:00Z'
uuid: b0f75d39-e353-5e68-8ff5-12f183b20e3b
year: 2025
---

<!-- AUTHORED REGION START -->
# LiT: limit order book transformer

## Summary

The paper asks whether a transformer architecture that drops convolutional layers entirely can match or beat CNN-based and classical models at forecasting short-term limit order book price direction, and whether such a model can be kept useful as market conditions drift. It proposes LiT, which turns each order-book snapshot window into structured rectangular patches (one dimension spanning a full side's price levels, the other a short run of timestamps), adds a learned positional embedding encoding side and time, processes the patches with transformer self-attention layers, and then passes the result through LSTM layers before a softmax layer classifies the coming mid-price move as up, stable, or down.

Level-2 order book snapshots were reconstructed from Binance at millisecond granularity using the top price levels on each side, and four datasets were collected covering a full month plus single weeks from three later months. Models were compared across four labeling horizons defined by the average forward mid-price change, with a percentage threshold splitting moves into the three classes, and performance was judged with precision, recall, F1 and accuracy reweighted for class imbalance under time-series cross-validation.

Across all four horizons LiT matched or narrowly beat every baseline tested, including ridge regression, random forest, SVM, MLP, LSTM, a vanilla vision-transformer baseline, and the CNN-based DeepLOB and TransLOB architectures, with the advantage most visible at the medium and longer horizons. A patch-size sweep found that narrower temporal patches combined with deeper (fuller book) patches consistently improved results, and a pretrain/fine-tune experiment showed that a model trained on one month's data degraded noticeably when applied unchanged to later months, but recovered and then exceeded from-scratch performance once its last layers were fine-tuned on a slice of the new month.

What is new is the removal of convolutional feature extraction from an order-book forecasting transformer altogether, replaced by a patching scheme shaped to the book's own structure rather than to image-style square patches, paired with a light fine-tuning recipe as a practical response to distribution shift in fast-moving markets.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Order book snapshots are reconstructed from Binance's Level-2 feed at millisecond resolution and treated as an event-based series following the inflow approach of Ntakaris et al. (2018), with the 64 most recent snapshots used as model input. Labels come from the average mid-price change over a fixed forward window (300-500ms, 300-700ms, 300-1000ms or 500-1000ms), but timestamps where the mid-price does not move are dropped, so the labeled sequence of market movement events is itself unevenly spaced in wall-clock time; moves are classed up, stable, or down using a threshold of 0.000015 times the current mid-price.

## Data

- **Asset class:** Crypto
- **Instruments:** not stated (order book of a single, unnamed instrument on Binance; no ticker is given in the text)
- **Venue:** Binance
- **Period:** September 2024 (full month) plus the second week of October, November and December 2024
- **Granularity:** millisecond-level Level-2 snapshots, top 20 price levels on each side (80 price/volume features per timestamp); over 1,077,057 timestamps in the September dataset alone

## Features and Measures

- **Structured LOB patch.** A rectangular slice of the price/volume grid whose height equals the full depth of one side of the book and whose width is a short run of timestamps, used as the transformer's input token instead of a small square image-style patch.
- **Mid-price.** The average of the best bid and best ask price, used as the proxy for market movement that the model predicts.
- **Threshold-based movement label.** A three-way up/stable/down label formed by comparing the average forward mid-price change over a fixed horizon to a set percentage of the current mid-price.

## Method

LiT is a three-stage network: a linear projection of structured patches concatenated with a learned positional embedding encoding book side and temporal position, self-attention transformer layers over these patch embeddings, and LSTM layers on top to capture longer temporal dependencies, ending in a softmax classifier over the three movement classes. It is benchmarked against ridge regression, random forest and SVM as classical baselines, MLP and LSTM as deep-learning baselines, a vanilla vision-transformer (ViT) baseline, and the CNN-based DeepLOB and TransLOB architectures, all built with a comparable parameter count in Keras/TensorFlow and trained with the RMSProp optimiser for up to 300 epochs, with early stopping after 30 epochs without improvement and a batch size of 128.

Performance is judged with precision, recall, F1 and accuracy, each reweighted by class frequency to correct for the imbalance introduced by the movement threshold, using five-fold time-series cross-validation on a subset of the September data for the main model comparison. A separate ablation varies patch height and width to study how patch shape affects performance. A further experiment tests robustness to distribution shift by comparing a model trained from scratch on each of October, November and December against the same September-pretrained model evaluated with no adaptation (zero-shot), and against that pretrained model fine-tuned by unfreezing only its last two dense layers on a 60/40 train/test split of each month.

## Results

- At the shortest 300-500ms horizon LiT had the best F1 (58.99%) and accuracy (59.03%) among all models, with every model scoring under 60% on every metric.
- At the 300-700ms horizon LiT reached the top F1 (63.65%) and accuracy (64.58%).
- At the 300-1000ms horizon LiT led on all four metrics: precision 66.20%, recall 68.34%, F1 66.40% and accuracy 68.34%.
- At the 500-1000ms horizon LiT had the top recall and accuracy (66.37% each), though DeepLOB slightly edged it out on F1.
- The vanilla vision-transformer (ViT) baseline consistently underperformed the CNN-based and LSTM-based state-of-the-art models across all four horizons.
- Patch configurations combining a narrower temporal width (W=4) with a deeper spatial dimension (H=40) consistently gave the strongest results across all horizons.
- A September-trained model applied without adaptation to later months (zero-shot) lost around 5% in most metrics by November and December, falling below the from-scratch baseline for those months.
- Fine-tuning only the final two layers of the September-pretrained model on each month's own data beat both the zero-shot and from-scratch results, e.g. reaching 65.26% precision and 65.07% accuracy on October versus 62.47% precision from-scratch and 64.20% precision zero-shot.

## Limitations

- Evaluation is limited to Binance cryptocurrency order book data for a single, unnamed instrument; no equity, FX or bond order books are tested.
- The main model comparison uses only a subset of the September dataset because of computational constraints on some baselines, rather than the full collected data.
- Fine-tuning experiments use a simple 60/40 train/test split rather than cross-validation, and cover only three subsequent months.
- Reader note: all reported horizons are extremely short (300ms-1000ms), so conclusions about model ranking may not transfer to longer, more economically meaningful prediction horizons.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/transformers|transformers]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]

## Citation

Yue Xiao, Carmine Ventre, Yuhan Wang, Haochen Li, Yuxi Huan, Buhong Liu (2025). LiT: limit order book transformer. Frontiers in Artificial Intelligence.

DOI: 10.3389/frai.2025.1616485

Text ingested: `markdown_output/xiao-2025-lit-limit-order-book-transformer.md`, converted from `raw/ofi-event-clock/xiao-2025-lit-limit-order-book-transformer.pdf`.

Coverage of this summary: Read the full paper markdown start to end (abstract through references), including all result tables.

Known problems with the input: Markdown conversion garbles several results tables (duplicated header rows, strikethrough formatting, misaligned columns), so table numbers were cross-checked against the surrounding prose before use; Key equations (the LOB definition, attention scores, LSTM update) are rendered as omitted images in the markdown, so their exact mathematical form could not be verified from the text and is not reproduced here.
<!-- AUTHORED REGION END -->