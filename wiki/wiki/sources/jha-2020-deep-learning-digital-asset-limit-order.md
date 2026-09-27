---
authors:
- Rakshit Jha
- Mattijs De Paepe
- Samuel Holt
- James West
- Shaun Ng
content_hash: sha256:9d6549e23591dfee0ce7c63b6899b2660ca4db8c815aa39556214de310bc6a81
created: 2026-09-27 01:47:00+00:00
page_id: sources/jha-2020-deep-learning-digital-asset-limit-order
page_type: source
related:
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/high-frequency-trading
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:e3d3909c4a2c82024be49fb425e7692929f1ade547bca76dcddad02d71a96fea
source_path: markdown_output/jha-2020-deep-learning-digital-asset-limit-order.md
source_type: paper
tags:
- cryptocurrency
- limit-order-book
- temporal-convolutional-network
- midprice-prediction
- walk-forward-validation
- high-frequency-data
- clock-calendar
- asset-crypto
- harvest-relevant
title: Deep Learning for Digital Asset Limit Order Books
updated: '2026-09-27T01:47:00Z'
uuid: a9f9d600-551d-5e31-88c3-186f7706e748
year: 2020
---

<!-- AUTHORED REGION START -->
# Deep Learning for Digital Asset Limit Order Books

## Summary

The paper asks whether a temporal convolutional network (TCN) can predict short-horizon bitcoin midprice movements from limit order book snapshots on a cryptocurrency exchange, and whether such a model is cheap enough to train and deploy in colocation on commodity hardware.

Using 100ms-resolution Coinbase BTCUSD order-book snapshots spanning 9 consecutive days (12 to 20 June 2019) with 50 levels of bid/ask depth, the authors label each timestep by the signed change between k-averaged midprices before and after time t (k=20, movement threshold alpha=0.002), downsample to balance the resulting Down/Stable/Up classes, and train a TCN (kernel size 2, dilation 6) with causal convolutions to classify the next label. The model is validated with a walk-forward scheme that varies the training window (1 to 7 days) against a fixed 1-day test period, and the authors also vary order-book depth and prediction horizon to study where predictive signal lives.

The best walk-forward configuration (7-day training, 1-day test) reached 71% walk-forward accuracy at a 2-second horizon, with recall of 61% on downward moves and 66% on upward moves. Predictive signal was concentrated in the top 10 bid/ask levels, persisted for up to about a minute, and model accuracy improved with longer training windows rather than degrading, in contrast to the frequent intraday retraining used for equities and futures models.

The contribution is mainly empirical: showing that a TCN trained in under a day on commodity GPUs can predict cryptocurrency limit-order-book midprice direction, and drawing out several 'stylized facts' about cryptocurrency order-book regimes, including a shallower depth of predictive signal than in equities, longer useful training windows, hours-to-days regime durations, and roughly 10-second order-book memory.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The order book is snapshotted at fixed 100ms calendar intervals (near-continuous, not event-driven) across 9 consecutive days of Coinbase BTCUSD data. Each timestep's label compares a k-averaged midprice (k=20) over the preceding window to the k-averaged midprice over the following window, applying a movement threshold alpha=0.002 to separate Stable from Up/Down. Horizons from a few seconds up to about a minute are examined, with the headline result reported at a 2-second horizon.

## Data

- **Asset class:** Crypto
- **Instruments:** Bitcoin/US dollar (BTCUSD) spot limit order book
- **Venue:** Coinbase
- **Period:** 12 to 20 June 2019 (9 consecutive days)
- **Granularity:** 100ms snapshots, 50 levels of bid and ask depth per snapshot (200 raw features); most predictive signal found within the top 10 levels.

## Features and Measures

- **k-averaged midprice movement label.** The signed difference between the average midprice over the k=20 steps up to and including time t and the average midprice over the following k=20 steps, thresholded at alpha=0.002 to produce a Down/Stable/Up label.
- **Order-book depth features.** Price and volume at up to 50 bid and ask levels (200 raw features per snapshot), standardized using the previous day's mean and standard deviation before being fed to the network.

## Method

The model is a temporal convolutional network (TCN) with causal, dilated convolutions (kernel size 2, dilation 6) trained to classify each snapshot's Down/Stable/Up label by minimising categorical cross-entropy with the ADAM optimiser (learning rate 0.01), a batch size of 128, early stopping after 4 epochs without validation improvement, and a learning-rate reduction (factor 0.5) after 2 epochs without improvement; the reported run trained for 57 epochs. Because Stable events dominate the raw label distribution, the majority class is randomly downsampled before training. Evaluation uses a walk-forward design: models are trained on windows of 1 to 7 days and tested on the following, non-overlapping single day, with performance reported via a confusion matrix, recall/precision/F1 by class and overall accuracy, plus sensitivity studies over order-book depth, training-window length, and prediction horizon.

## Results

- The headline configuration (7-day training, 1-day test) reached 71% walk-forward accuracy at a 2-second prediction horizon.
- Recall was 61% for downward midprice moves and 66% for upward moves at the 2-second horizon.
- Predictive performance did not decline through the trading day, suggesting the market does not quickly arbitrage away the signal within a session.
- Accuracy improved with longer training windows, up to the 7-day maximum tested, rather than requiring frequent intraday retraining.
- Predictive signal was concentrated in the top 10 bid/ask levels, with no further gain and some decline beyond that depth.
- Predictability of midprice direction persisted for up to about a minute on Coinbase.
- Downsampling reduced the labelled sample from 4,219,932 to 1,681,407 observations to correct for class imbalance toward the Stable label.

## Limitations

- The dataset covers only 9 consecutive days of a single instrument (BTCUSD) on a single exchange (Coinbase), which the authors themselves describe as limited.
- The authors state they do not explicitly validate, for cryptocurrency order books, the claim (established elsewhere for traditional assets) that deep learning gives more accurate forecasts than other machine-learning techniques.
- Reader note: the paper contains two different confusion-matrix/classification-report tables that appear to describe the same three-class prediction task but show inconsistent precision/recall/F1 values, without reconciling them.
- Reader note: beyond a general acknowledgement of support from Globe Research, the paper gives no per-author or per-institution breakdown of contribution or funding.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]

## Citation

Rakshit Jha, Mattijs De Paepe, Samuel Holt, James West, Shaun Ng (2020). Deep Learning for Digital Asset Limit Order Books.

DOI: 10.2139/ssrn.3704098

Text ingested: `markdown_output/jha-2020-deep-learning-digital-asset-limit-order.md`, converted from `raw/ofi-event-clock/jha-2020-deep-learning-digital-asset-limit-order.pdf`.

Coverage of this summary: Read the entire markdown file (short paper, single read): abstract, introduction, methodology (data, model architecture, evaluation), results (Sections 3.1 and 3.2), conclusion, and Appendices A/B as far as the picture-omitted figures allow.

Known problems with the input: Author affiliations could not be reliably mapped to individual authors because the PDF-to-markdown conversion interleaves two affiliation blocks (University of Cambridge, Globe Research) with the five author names in a way that does not clearly indicate who belongs to which; affiliations are therefore recorded as not stated for all five authors; The paper's confusion-matrix table in Section 3.1 (Figure 2) and the classification-report table in Appendix B (Table 1) give different precision/recall/F1 numbers for what appears to be the same three-class task, and the source markdown's table extraction is visibly garbled (merged cells), so those secondary numbers were not relied on in the results field.
<!-- AUTHORED REGION END -->