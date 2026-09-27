---
authors:
- Martin Magris
- Mostafa Shabani
- Alexandros Iosifidis
content_hash: sha256:86aaa81ae556ce7996ff008cd65384b3d8828ff8511133270434fdbed002b714
created: 2026-09-27 01:47:00+00:00
page_id: sources/magris-2023-bayesian-bilinear-neural-network-predicting-midprice
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
- concepts/market-microstructure
- entities/martin-magris
- entities/mostafa-shabani
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:9130061568f137a2bdf187625a05085ee0c4611be3ffddda2c57e7da6e0483fb
source_path: markdown_output/magris-2023-bayesian-bilinear-neural-network-predicting-midprice.md
source_type: paper
tags:
- bayesian-deep-learning
- limit-order-book
- mid-price-prediction
- variational-inference
- uncertainty-quantification
- tabl-architecture
- fi-2010-dataset
- clock-event
- asset-equity
- harvest-relevant
title: Bayesian Bilinear Neural Network for Predicting the Mid-price Dynamics in Limit-Order
  Book Markets
updated: '2026-09-27T01:47:00Z'
uuid: f0b40922-da4e-53b8-ba05-a703287fda01
year: 2023
---

<!-- AUTHORED REGION START -->
# Bayesian Bilinear Neural Network for Predicting the Mid-price Dynamics in Limit-Order Book Markets

## Summary

The paper asks whether Bayesian deep learning is practical for a real econometric forecasting task, namely classifying whether the mid-price in a limit order book will rise, fall, or stay flat at a future point. It argues that standard neural networks give point forecasts without any sense of confidence, which is a problem for financial decision-making, while Bayesian neural networks (BNNs) place a learned distribution over the network's weights and so yield a predictive distribution over outcomes.

The approach takes an existing lightweight architecture, the Temporal Attention-augmented Bilinear network (TABL), and gives it a Bayesian treatment (B-TABL) by placing a Gaussian mean-field variational posterior over its weights, trained with a natural-gradient variational-inference optimizer called Variational Online Gauss-Newton (VOGN). This is compared against the same TABL layer trained by ADAM, by plain stochastic gradient descent (SGD), and by ADAM combined with Monte Carlo dropout (MCD) as an approximate-Bayesian alternative. The task and data are the FI-2010 benchmark: tick-by-tick limit order book snapshots for five NASDAQ Nordic stocks.

The main finding is that VOGN's Bayesian training is feasible at this scale and gives classification performance that is close to, and on several metrics slightly better than, ADAM, while MCD and SGD are clearly weaker. What is new is not the predictive accuracy itself but the fact that the Bayesian model produces a predictive distribution over class probabilities that can be inspected sample by sample: the paper shows in detail how averaging over posterior draws reveals genuine uncertainty that a single point forecast (as from ADAM) would hide, including cases where the model's top predicted class only reflects a modest true probability.

The authors read this as evidence that Bayesian deep learning is a workable bridge between the probabilistic tradition of econometrics and the flexible, non-parametric practice of machine learning, and they flag using these uncertainty estimates to inform actual trading decisions, verified by backtesting, as future work.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are individual limit order book update events from the FI-2010 benchmark (tick-by-tick data); the benchmark's feature vectors are constructed over non-overlapping blocks of ten events. FI-2010 provides mid-price direction labels at five future horizons, 10, 20, 30, 50 and 100 events ahead; this paper uses only the 10-event horizon and frames the task as three-way classification of the mid-price's direction (up, down, or stationary) at that horizon.

## Data

- **Asset class:** Equities
- **Instruments:** Five stocks traded on the NASDAQ Nordic Helsinki exchange, via the public FI-2010 limit-order-book benchmark dataset
- **Venue:** NASDAQ Nordic Helsinki exchange
- **Period:** June 1 to June 14, 2010 (ten trading days)
- **Granularity:** Tick-by-tick limit order book update events; per-event 144-dimensional feature vectors, of which the first 40 (raw prices and quantities) are used as model input, z-score normalized and aggregated over non-overlapping blocks of ten events

## Features and Measures

- **mid-price.** The average of the best bid price and best ask price at a given time, used as the underlying series whose direction the model predicts.
- **raw LOB price/quantity inputs.** The first 40 of the FI-2010 dataset's 144 feature dimensions, giving raw prices and quantities at the top levels of the order book, used directly as the model's input representation instead of hand-built imbalance or flow features.

## Method

The core model is the Temporal Attention-augmented Bilinear network (TABL), a bilinear layer that maps a features-by-time input matrix to an output representation while learning an attention mask over the time dimension, mixed with a plain bilinear branch through a learnable scalar coefficient. The paper's contribution is a Bayesian version, B-TABL, in which the TABL layer's weights are treated as random variables with a Gaussian mean-field variational posterior rather than fixed point estimates. This posterior is trained with Variational Online Gauss-Newton (VOGN), a natural-gradient variational-inference algorithm that updates the posterior mean and variance using gradient and (approximated, non-negative) Hessian information; the final layer uses a log-softmax activation and the loss is the negative log-likelihood over the three mid-price-direction classes.

B-TABL/VOGN is benchmarked against the same TABL layer trained with the ADAM optimizer, with plain SGD, and with ADAM plus Monte Carlo dropout (MCD) at test time as an approximate-Bayesian baseline. For VOGN and MCD, a predictive distribution is built from Ns = 50 forward passes drawing different weight samples (or dropout masks) for each test input, and predictions can be summarized by the mean, median or mode of these draws, or directly from the averaged predictive distribution. Performance is judged on held-out data using micro-, macro- and weighted-macro precision, recall, f1-score and accuracy for the imbalanced three-class task, on a corresponding one-vs-rest single-class breakdown, and via ROC curves, area under the ROC curve, and calibration curves with an expected calibration error and an L2 calibration distance.

## Results

- VOGN converges markedly faster than ADAM in early training (up to about epoch 500), with validation performance for the two optimizers converging by around epoch 800.
- Using the full predictive distribution, VOGN reaches a weighted-macro f1-score of 0.751 versus ADAM's 0.741 on the three-class test task, a 0.9% improvement, while micro accuracy is 0.774 for VOGN versus 0.772 for ADAM.
- Even the worst individual posterior sample from VOGN outperforms ADAM by up to 1.8% on some metrics, while on precision specifically ADAM remains ahead of VOGN.
- Monte Carlo dropout and plain SGD are clearly weaker than either VOGN or ADAM: SGD's weighted-macro f1-score is 0.667 and MCD's predictive-distribution f1-score is 0.634.
- Of VOGN's 50 posterior draws per test input, 96% agree on a single predicted class, and a single random draw matches the modal (most frequent) predicted label about 99.36% of the time on average.
- The mean predictive probability assigned to the top-ranked class is 55% for correctly classified test inputs versus 51% for misclassified ones, indicating that even correct predictions carry substantial residual uncertainty.
- At a 95% true-positive rate, VOGN's macro-averaged false-positive rate is 88% versus ADAM's 90%, and the micro-averaged false-positive rate is 76% for VOGN versus 77% for ADAM.

## Limitations

- The dataset covers only five stocks over ten trading days (the FI-2010 benchmark). Reader note: this is a narrow sample for generalizing conclusions about model performance.
- The three-way label is highly imbalanced, with 67% of test samples in the stationary class, which the authors address only partly through weighted and micro-averaged metrics.
- The authors state that VOGN's test-set performance is comparable to, rather than clearly superior to, ADAM's, describing the comparison as having no strong winner.
- No trading strategy or backtest is built from the model's predictions or predictive uncertainty; the authors identify this as future work.
- Reader note: only the 10-event label horizon is examined, although the FI-2010 dataset also provides 20-, 30-, 50- and 100-event horizons.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/market-microstructure|market microstructure]]
- [[entities/martin-magris|Martin Magris]]
- [[entities/mostafa-shabani|Mostafa Shabani]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Martin Magris, Mostafa Shabani, Alexandros Iosifidis (2023). Bayesian Bilinear Neural Network for Predicting the Mid-price Dynamics in Limit-Order Book Markets.

DOI: 10.1002/for.2955

Text ingested: `markdown_output/magris-2023-bayesian-bilinear-neural-network-predicting-midprice.md`, converted from `raw/ofi-event-clock/magris-2023-bayesian-bilinear-neural-network-predicting-midprice.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction, literature review, the BNN/TABL/B-TABL and VOGN methods sections, the FI-2010 data description and experiment settings, all results subsections (learning curves, posterior, predictive distribution, label forecasts, multi- and single-class performance tables, ROC and calibration curves), the conclusion, and the appendix; skimmed the reference list.

Known problems with the input: No publication year is printed in the paper text; year taken from the job file's year_hint; No venue (journal/conference) name is printed in the paper text, so venue is left empty.
<!-- AUTHORED REGION END -->