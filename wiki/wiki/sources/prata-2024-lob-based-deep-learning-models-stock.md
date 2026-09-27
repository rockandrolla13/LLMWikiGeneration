---
authors:
- Matteo Prata
- Giuseppe Masi
- Leonardo Berti
- Viviana Arrigoni
- Andrea Coletta
- Irene Cannistraci
- Svitlana Vyetrenko
- Paola Velardi
- Novella Bartolini
content_hash: sha256:18beeb94d8d6442d74f738619a0d2e2db35350582edb736d4a09afd2b93f4e2e
created: 2026-09-27 01:47:00+00:00
page_id: sources/prata-2024-lob-based-deep-learning-models-stock
page_type: source
publication_venue: Preprint. Under review.
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/transformers
- concepts/order-flow-prediction
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:720ba0a75e53c5fdc0c94c9f8fe47c79e9ff9225979955d3292122cdb518d45d
source_path: markdown_output/prata-2024-lob-based-deep-learning-models-stock.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- benchmark-study
- stock-price-prediction
- reproducibility
- generalizability
- attention-mechanisms
- equities
- clock-event
- asset-equity
- harvest-relevant
title: 'LOB-Based Deep Learning Models for Stock Price Trend Prediction: A Benchmark
  Study'
updated: '2026-09-27T01:47:00Z'
uuid: f20f3100-9aee-5b37-8151-9218c990ce6b
year: 2024
---

<!-- AUTHORED REGION START -->
# LOB-Based Deep Learning Models for Stock Price Trend Prediction: A Benchmark Study

## Summary

The paper studies whether recent deep-learning models for Stock Price Trend Prediction (SPTP) from limit order book (LOB) data can be trusted outside the exact benchmark they were published on. It notes that some prior systems report F1-scores above 88% in simulated settings, but questions whether such numbers hold up in more realistic conditions, framing this as a possible simulation-to-reality gap. The paper's central question is split into two parts: robustness, whether a model's own claimed performance can be reproduced on the same public benchmark, and generalizability, whether that performance survives on new, previously unseen order book data.

To answer this, the authors built LOBCAST, an open-source framework for LOB data preprocessing, model training and tuning, evaluation reporting, and profitability backtesting. They re-implemented and retrained 15 deep-learning models, most drawn from papers published between 2017 and 2022 plus baseline architectures, all predicting a three-way up/down/stable trend label built from smoothed future mid-price averages. Robustness is tested on FI-2010, the public benchmark most of the original papers used. Generalizability is tested on two new datasets built from LOBSTER order-book data for six NASDAQ stocks, one from a calmer period (July 2021) and one from a more volatile period around the war in Ukraine (February 2022). The authors define single robustness and generalizability scores that penalize both the average gap between claimed and measured F1-score and the variability of that gap, and they also test two ensembles of the 15 models and run a trading simulation.

The main finding is that most models' reproduced F1-scores differ substantially from their claimed scores, and performance drops much further on the new LOBSTER-derived data than on FI-2010, consistent with the best FI-2010 performers having overfit that specific benchmark. One model, BINCTABL, stands out as both the top performer and the most robust and most generalizable, and models using attention mechanisms tend to rank highest overall. Combining all 15 models via a majority vote or a learned meta-classifier failed to beat the single best model. What is new here is less a single model than the benchmarking exercise itself: the open LOBCAST framework, the explicit robustness/generalizability scoring method, and two freshly built, unseen LOB datasets spanning different volatility regimes.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The limit order book is not sampled at fixed wall-clock intervals; instead, an observation is taken every 10 order-book events (submissions, cancellations, or executions), following the same procedure used to build the FI-2010 benchmark. The prediction target is a ternary trend label (up, down, stable) computed by comparing the current mid-price to the average of future mid-prices over a horizon of k time units, with k drawn from the set {1, 2, 3, 5, 10}; a threshold on this averaged difference decides which of the three classes applies at each sampled point.

## Data

- **Asset class:** Equities
- **Instruments:** FI-2010: five Finnish stocks (Kesko Oyj, Outokumpu Oyj, Sampo, Rautaruukki, Wartsila Oyj) on NASDAQ Nordic. LOB-2021/LOB-2022: six NASDAQ stocks (SoFi Technologies, Netflix, Cisco Systems, Wing Stop, Shoals Technologies Group, Landstar System), selected via clustering of a 630-stock pool.
- **Venue:** NASDAQ Nordic (FI-2010) and NASDAQ, via the LOBSTER data provider (LOB-2021/LOB-2022)
- **Period:** FI-2010: June 1st to June 14th, 2010 (10 trading days). LOB-2021: July 2021 (10 trading days). LOB-2022: February 2022 (10 trading days).
- **Granularity:** 10 price levels per side of the book; observations sampled every 10 events. FI-2010 holds about 4 million limit order messages totalling 394,337 sampled events; LOB-2021/2022 are built the same way from LOBSTER data and are described as roughly three times larger than FI-2010 for the same length of time.

## Features and Measures

- **mid-price.** The average of the best bid and best ask prices, used as the reference value from which price trend labels are derived even though it is not itself a tradable price.
- **ternary trend label (U/D/S).** A classification target marking a point in time as upward, downward, or stable, based on comparing the current mid-price to the average of future mid-prices over a chosen horizon against a fixed threshold.
- **robustness score.** A score of at most 100 computed as 100 minus the sum of the average gap and its standard deviation between a model's originally claimed F1-score and the F1-score the authors reproduced on the same FI-2010 benchmark.
- **generalizability score.** The same 100-minus-gap-and-variability formula as the robustness score, but comparing a model's claimed F1-score against its F1-score on the new, unseen LOB-2021/LOB-2022 datasets rather than on the original benchmark.

## Method

The authors built LOBCAST, a PyTorch-Lightning-based open-source framework that handles LOB data preprocessing (normalization, splitting, labelling), model training with hyperparameter tuning support, performance reporting (F1-score, accuracy, recall), and profit backtesting via the Backtesting.py library. Within this framework they evaluate 15 deep-learning models in total, most reproduced from papers published between 2017 and 2022 covering CNN, LSTM, bilinear-attention, transformer, and neural-bag-of-features architectures, alongside baseline DL models; the paper's own text is inconsistent about which two architectures serve as the plain baselines (the main text names MLP and CNN, while an appendix names MLP and LSTM). Where an original model used extra engineered inputs beyond the raw order book, the authors reduced its feature set to the same 40 raw price/volume features used by all other models, to keep comparisons consistent.

Robustness is assessed by retraining and testing each model on FI-2010, the shared benchmark most of the original papers used, and comparing the reproduced F1-score to the one the original paper claimed. Generalizability is assessed the same way but on the two newly built LOB-2021 and LOB-2022 datasets. Each model is trained with five random seeds for each of five prediction horizons, and results are summarized as an average F1-score, its standard deviation, and the robustness/generalizability scores described above. Training all models across seeds and horizons took roughly 155 hours for FI-2010 and roughly 258 hours for LOB-2021/2022 combined, run on a cluster of 8 GPUs. Two ensemble predictors, a majority vote weighted by each model's F1-score and a trained meta-classifier over the 15 models' output probabilities, and a trading simulation on LOB-2021, are also evaluated.

## Results

- Averaged over five seeds and all tested horizons, BINCTABL had the highest F1-score on FI-2010, 82.6 (standard deviation 7.0), and also the strongest robustness score of all models at 99.7.
- BINCTABL's average F1-score exceeded the second-best model, DLA, by up to 9.2%, and exceeded the original CTABL model it extends by up to 13%.
- F1-scores on the new LOB-2021/LOB-2022 data were markedly lower than on FI-2010 across all models, ranging from 48-61%; BINCTABL itself dropped by about 19.6% on average, giving it a generalizability score of 73.5.
- When restricted to the 40 raw order-book features instead of its original engineered feature set, CNNLSTM's F1-score improved by 20.9% on average, the largest such gain among the models affected by this change.
- Roughly half of the hyperparameter-search runs across all models diverged, producing an F1-score of 33% or lower.
- The six best-ranked models on FI-2010 remained the six best-ranked models on both LOB-2021 and LOB-2022, even though the exact ranking within that group shifted.
- ATNBoF was the weakest model overall, with a robustness score of 66.1 and an FI-2010 F1-score of 40.9, while TRANSLOB's claimed F1-score of 87.3 fell to a reproduced 59.4, giving it a robustness score of 69.9.
- Combining all 15 models through a weighted majority vote or a trained meta-classifier did not outperform the single best individual model on either FI-2010 or the new LOBSTER-derived datasets.

## Limitations

- The grid hyperparameter search used for models whose original papers did not publish their settings was not exhaustive, so the chosen hyperparameters may understate what those original systems could achieve.
- Compute limits meant models could only be trained on LOBSTER data spanning 10-trading-day windows rather than the years of history that might give a more reliable generalizability estimate.
- FI-2010 is already normalized, filtered, and labelled, so its underlying raw order book cannot be reconstructed, and its labelling method is described by prior work the authors cite as prone to instability.
- The single labelling threshold used for FI-2010 was tuned to balance classes only at horizon k=5, leaving classes unevenly balanced at the other tested horizons (k=1,2,3,10).
- Reader note: training, validation, and test data for each stock and time window come from different historical sub-periods, so distribution shift between splits could itself lower generalizability scores independent of model quality.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/transformers|transformers]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Matteo Prata, Giuseppe Masi, Leonardo Berti, Viviana Arrigoni, Andrea Coletta, Irene Cannistraci, Svitlana Vyetrenko, Paola Velardi, Novella Bartolini (2024). LOB-Based Deep Learning Models for Stock Price Trend Prediction: A Benchmark Study. Preprint. Under review..

DOI: 10.1007/s10462-024-10715-4

Text ingested: `markdown_output/prata-2024-lob-based-deep-learning-models-stock.md`, converted from `raw/ofi-event-clock/prata-2024-lob-based-deep-learning-models-stock.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, related work, the SPTP/LOB problem definition (Section 3), the full experiments section (Section 4: datasets, models, LOBCAST framework, robustness and generalizability results and Table 2), the discussion and stated limitations (Section 5), the disclaimer/acknowledgements, and the appendices covering market observation format, per-model descriptions, ensemble methods, stock selection, and dataset construction (Appendices A-D).

Known problems with the input: The paper does not print a publication year in the body text I read (it is marked 'Preprint. Under review.'); used the job file's year_hint of 2024; The paper's own text is inconsistent about the two non-SOTA baseline models: Section 4.2 names Multilayer Perceptron and Convolutional Neural Network, while Appendix B names Multilayer Perceptron and LSTM as the two added baselines; both are noted rather than resolved; Several table and equation entries in the converted markdown are rendered with underscores and split digits (e.g. '82_._6') or as picture placeholders; numeric values were reconstructed from these split forms per the digit-provenance rule, and some picture-only equations (e.g. the trend-labelling formulas) could not be verified in exact symbolic form.
<!-- AUTHORED REGION END -->