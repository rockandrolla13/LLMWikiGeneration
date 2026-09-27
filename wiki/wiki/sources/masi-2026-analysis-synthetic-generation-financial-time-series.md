---
authors:
- Giuseppe Masi
content_hash: sha256:fe89108a1f07809c002ccb16885eea0d22dbf5df968cb528f4368fd5c5fc4d39
created: 2026-09-27 01:47:00+00:00
page_id: sources/masi-2026-analysis-synthetic-generation-financial-time-series
page_type: source
publication_venue: Sapienza University of Rome, Computer Science Department — PhD
  Thesis in Computer Science (Academic Year 2025-2026, XXXVIII cycle)
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/order-flow-prediction
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/transformers
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:b282829c03f3b6a2dc8a67dff6dcc41399cfbddc5a78ae7178bf8817a4ab7cf1
source_path: markdown_output/masi-2026-analysis-synthetic-generation-financial-time-series.md
source_type: paper
tags:
- limit-order-book
- deep-learning-benchmark
- synthetic-data-generation
- gan
- diffusion-models
- causal-discovery
- stock-shocks
- power-law-spectra
- clock-compares
- asset-multi
- harvest-relevant
title: Analysis and Synthetic Generation of Financial Time-Series
updated: '2026-09-27T01:47:00Z'
uuid: 85329cb6-8066-5c23-ac0b-69ee0b522a3a
year: 2026
---

<!-- AUTHORED REGION START -->
# Analysis and Synthetic Generation of Financial Time-Series

## Summary

This PhD thesis asks how data-driven methods can better model, predict, and simulate financial time series that are volatile, heavy-tailed, non-stationary, and cross-dependent across assets, with a particular focus on limit-order-book (LOB) data. It is organized as five largely self-contained research chapters (each already published, or under review, as a separate paper) plus an introduction and a concluding chapter, addressing three broad questions: how to detect and forecast abrupt price shocks, how reliable deep-learning LOB trend predictors really are outside their original test sets, and how to generate realistic synthetic multi-asset time series that preserve correlation and causal structure, plus a further study of causal-discovery robustness under power-law noise.

The shock-forecasting chapter defines a stock "shock" formally as a return falling in the tail of a fitted Levy-stable distribution over a sliding window, then predicts these events ahead of time from LOB-derived features (Levy-stable parameters, order-book depth, moments, resiliency, cumulative volume) using a Random Forest tuned by hierarchical-clustering feature selection and Bayesian hyperparameter search. The benchmarking chapter instead re-implements and stress-tests 15 published deep-learning LOB trend predictors (plus two ensembles) inside an open-source framework (LOBCAST), separating "robustness" (replicating a model's own claimed FI-2010 result) from "generalizability" (performance on newly built LOBSTER-derived NASDAQ data, LOB-2021/2022), and adds non-DL baselines and a profit-based backtest. The two generative chapters build synthetic multivariate financial series: CoMeTS-GAN is a conditional Wasserstein GAN that generates correlated mid-price/volume series autoregressively while explicitly scoring cross-asset correlation realism, and DiffCATS is a diffusion model that jointly generates a multivariate time series and a per-sample causal graph via generated VAR coefficients, avoiding both a stationarity assumption and the need for post-hoc causal-explanation tools. The final chapter, PLaCy, is a causal-discovery method that performs Granger-style tests on the evolving power-law spectral exponent and amplitude of each series rather than on the raw signal, aiming for robustness to non-stationary and heavy-tailed real-world noise.

Across chapters, the LOB-based Random Forest shock predictor reaches useful precision at the cost of modest recall; the DL benchmark finds that most surveyed SPTP models do not reproduce their published FI-2010 scores and, more importantly, all models' F1-scores fall sharply when moved to new LOBSTER data, with attention-based architectures (especially BINCTABL) faring best on both counts; CoMeTS-GAN matches or beats prior GAN and autoregressive baselines (TimeGAN, RCGAN, C-RNN-GAN, WaveNet/WaveGAN) on a discriminative-score test while training far faster and preserving measured stylized facts and cross-correlation; DiffCATS achieves strong discriminative scores and the best causal-graph fidelity among compared time-series-plus-causal-graph generators (CausalTime, CR-VAE) across three datasets; and PLaCy outperforms Granger causality, PCMCI(+/Omega), CCM-filtering, RCV-VarLiNGAM, DYNOTEARS, Rhino and several frequency-domain baselines on synthetic Ornstein-Uhlenbeck benchmarks and on two real datasets (river discharge, air quality) with known causal structure, particularly under non-stationary, multiplicative noise.

The thesis's stated contribution is a coherent set of tools spanning detection, prediction-robustness auditing, and controllable generation for financial time series: a first formal, statistically grounded shock definition tied to a machine-learning predictor; a systematic robustness/generalizability benchmark of LOB deep-learning trend models with an open-source framework (LOBCAST); a GAN presented as the first to generate arbitrarily long multi-stock series while explicitly modeling correlation dynamics; a diffusion model presented as the first to generate a time series and its own per-sample causal graph jointly without a stationarity assumption; and a causal-discovery method that exploits ubiquitous power-law spectral structure for added robustness to real-world noise.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Different chapters use different clocks rather than one shared design. Chapter 2 aggregates order-book messages into 30-second bars and predicts a shock 150 seconds ahead. Chapter 3 samples LOB snapshots every 10 events and labels the trend over a horizon expressed as a fixed number of future events, with horizons k in {1, 2, 3, 5, 10}. Chapter 4 generates mid-prices and volumes on a minute-level calendar clock. Chapters 5 and 6 operate on generic multivariate time steps (daily river discharge, hourly air-quality readings, or simulated process steps) rather than a financial trading clock, since their generation/causal-discovery methods are presented as domain-agnostic.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Chapter 2: GME (GameStop) order-book data, with smaller supplementary tests on KO and AAPL. Chapter 3: the FI-2010 benchmark (five Finnish NASDAQ Nordic stocks: Kesko Oyj, Outokumpu Oyj, Sampo, Rautaruukki, Wartsila Oyj) plus a newly built LOB-2021/2022 dataset from six NASDAQ stocks (SOFI, NFLX, CSCO, WING, SHLS, LSTR). Chapter 4: Coca-Cola (KO), PepsiCo (PEP), Nvidia (NVDA) and Kansas City Southern (KSU) mid-prices/volumes, plus a 30-stock DJIA scalability test. Chapters 5-6 use non-equity series to test generation/causal-discovery methods in a domain-agnostic way: German river discharge (Iller, Danube, Isar), a Chinese air-quality (PM2.5) sensor network, synthetic Henon chaotic maps, and synthetic Ornstein-Uhlenbeck processes.
- **Venue:** NASDAQ order-book data via the LOBSTER data provider and the FI-2010 benchmark (NASDAQ Nordic); non-financial real-world datasets from a Bavarian river-gauge network and a Chinese air-quality monitoring network for the causal-discovery chapters.
- **Period:** Chapter 2: GME data from November 1, 2021 to April 29, 2022 (first 70% train, remaining 30% test). Chapter 3: FI-2010 spans June 1 to June 14, 2010 (10 trading days); the newly built LOB-2021 dataset spans 2021-07-01 to 2021-07-15 (10 trading days) and LOB-2022 spans 2022-02-01 to 2022-02-15 (10 trading days). Chapter 4: KO/PEP/NVDA/KSU data spans 2018-02-02 to 2018-10-11 (training) and 2018-10-12 to 2018-11-14 (validation); the 30-stock DJIA scalability test spans 2017-02-02 to 2017-10-11 (training) and 2017-10-12 to 2017-11-14 (validation). Chapters 5-6: the real-world Rivers dataset covers 2017 to 2019; the AirQuality dataset covers one year of hourly readings; synthetic Ornstein-Uhlenbeck experiments simulate series of length 5000 time-steps.
- **Granularity:** Order-book message data aggregated to 30-second bars (Ch.2) or sampled every 10 events (Ch.3); minute-level mid-price/volume bars (Ch.4); daily river-discharge and hourly air-quality readings, and discrete simulation steps (Ch.5-6).

## Features and Measures

- **Levy-stable distribution parameters.** The four parameters (stability, skewness, scale, shift) of a Levy-stable distribution fitted to log-returns in a rolling window, used both to define a shock statistically and as predictive inputs to the shock classifier.
- **order-book resiliency.** The trade volume needed to move the best sell price by five or ten LOB levels, used as a measure of the order book's robustness to one-sided, high-volume orders.
- **order-book volume cumulative sum.** The running sum of buy-side or sell-side volume across order-book levels over a look-behind window, used as an order-flow-imbalance style predictor of shocks.
- **order-book moments.** The mean, standard deviation, skewness and kurtosis of prices and volumes across the ten LOB levels at a given time, summarizing the shape of the book just before a candidate shock.
- **cross-correlation distance.** A GAN training and evaluation metric equal to the mean squared error between the real and generated Pearson correlation coefficients for every pair of jointly modeled assets.
- **VAR causal/coefficient matrices.** Time-varying vector-autoregressive coefficient matrices output by a diffusion model's denoising network, used both to reconstruct the synthetic time series and, after thresholding, to define its per-sample causal graph.
- **power-law spectral exponent and amplitude.** A rolling-window log-log linear fit of a series' Fourier amplitude spectrum, yielding a time-varying exponent and amplitude pair that is Granger-tested in place of the raw signal to detect causal relationships robustly.

## Method

Chapter 2 fits Levy-stable distributions to rolling log-return windows to define and label shocks, then trains and compares Random Forest, HDBSCAN and MLP classifiers on hand-built LOB features, selecting features via Spearman-correlation hierarchical clustering and tuning hyperparameters with Bayesian optimization; evaluation is precision/recall/F1 on a chronological train/test split. Chapter 3 reimplements 15 published SPTP deep networks (CNN, LSTM, attention/transformer and bilinear-normalization architectures) plus two ensembles inside an open-source PyTorch-Lightning framework (LOBCAST), training each with grid-search-tuned hyperparameters over five seeds and five labeling horizons, and separately measures "robustness" (the gap to a model's own published FI-2010 F1) versus "generalizability" (F1 on newly built LOBSTER data), plus a backtested trading simulation.

Chapter 4's CoMeTS-GAN is a conditional Wasserstein GAN with a temporal-convolutional generator and critic; the critic score is a weighted sum of a standard realness term and a second term scoring the realism of the pairwise Pearson cross-correlations among the generated series, trained with spectral normalization and evaluated via a discriminative-score classifier, stylized-fact checks, the cross-correlation-distance metric, and a manual perturbation/reactivity test. Chapter 5's DiffCATS is a diffusion model whose denoising network outputs both an initial window of the multivariate series and time-varying VAR coefficient matrices; the remaining series is reconstructed autoregressively from those coefficients, which are thresholded by quantile to produce a per-sample causal graph, and the model is evaluated with discriminative/predictive/authenticity/MMD/cross-correlation scores for the series and false-positive-rate/F1 metrics for the recovered graphs, plus downstream causal-discovery-algorithm benchmarking, causal-conditioned prediction, and causal classification tasks.

Chapter 6's PLaCy method segments each series into overlapping windows, fits a power-law (log-log linear) model to each window's Fourier amplitude spectrum to obtain a time-varying exponent and amplitude pair, and runs a standard multivariate Granger-causality test on these derived spectral series rather than on the raw signal; a theorem argues this spectral transformation preserves the ground-truth linear causal graph under stated assumptions. It is evaluated by F1-score and true-negative rate against Granger causality, PCMCI/PCMCI-Omega, CCM-filtering, RCV-VarLiNGAM, DYNOTEARS, Rhino and three frequency-domain baselines (BCGeweke, DTF, GewekeNP), on simulated Ornstein-Uhlenbeck systems with tunable noise and non-stationarity and on two real datasets with known ground-truth causal graphs.

## Results

- The optimized Random Forest shock predictor (feature selection plus Bayesian-tuned hyperparameters) reaches a precision of 0.80 and recall of 0.37 for shocks on 30-second GME data, versus 0.75 precision and 0.15 recall for the untuned default Random Forest baseline.
- Across 15 benchmarked deep-learning trend predictors, the best model on FI-2010 (BINCTABL) scores an average F1 of 82.6% there but falls to a generalizability score of 73.5% on new LOBSTER data, an average F1 decline of about 19.6%.
- About half of the hyperparameter-search runs across the 15 benchmarked deep-learning models diverged, scoring F1 <= 33%, indicating high sensitivity to hyperparameters and weight initialization.
- Every benchmarked deep-learning model's F1-score on the newly built LOB-2021/2022 NASDAQ data falls in a narrow 48-61% range, well below its FI-2010 performance.
- CoMeTS-GAN trains in about 4 hours and 20 minutes versus 39 hours for TimeGAN, while matching or beating TimeGAN and other GAN/autoregressive baselines on discriminative score across the tested benchmark scenarios.
- DiffCATS attains the best or joint-best time-series discriminative score on two of the three test datasets and the best causal-graph false-positive-rate fidelity on all three (Henon, Rivers, AQI) among methods that generate both a time series and a causal graph.
- PLaCy's F1-score reaches 0.80 on the hardest synthetic Ornstein-Uhlenbeck scenario tested (multiplicative, non-stationary noise), versus at most about 0.63 for plain Granger causality and 0.60 for PCMCI in the same family of scenarios.
- On real-world data, PLaCy attains the best F1 (0.51) and best true-negative rate (0.75) on the Rivers dataset, and the best F1 (0.45) on the AirQuality dataset, where PCMCI instead reaches the highest true-negative rate (0.95) but the lowest F1 (0.25).

## Limitations

- The shock-forecasting chapter is tuned and tested mainly on one heavily-traded, high-volatility stock (GME), with only limited single-day cross-checks on KO and AAPL, and its shock threshold/window parameters are set by hand rather than derived from a stated economic criterion.
- The LOB benchmarking chapter acknowledges its hyperparameter search was not exhaustive for models whose original settings were undisclosed, and computational limits meant models were trained only on data spanning weeks rather than multiple years.
- The GAN chapter does not incorporate order-book-level data or agent-level market impact, and the profit/backtesting evaluations used across the thesis ignore transaction costs, position sizing and market impact. Reader note: this likely overstates the achievable trading performance of any of the described models.
- DiffCATS only encodes linear causal relationships through its VAR coefficients, its expressivity is capped by a fixed maximum lag, and its per-sample causal-graph output makes it slower at inference than time-series-only or fixed-graph competitors.
- PLaCy cannot assess causality when a series' spectrum varies too slowly, and it is not well suited to very short time series because it needs enough length to estimate stable local spectral features.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/transformers|transformers]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]

## Citation

Giuseppe Masi (2026). Analysis and Synthetic Generation of Financial Time-Series. Sapienza University of Rome, Computer Science Department — PhD Thesis in Computer Science (Academic Year 2025-2026, XXXVIII cycle).

Text ingested: `markdown_output/masi-2026-analysis-synthetic-generation-financial-time-series.md`, converted from `raw/ofi-event-clock/masi-2026-analysis-synthetic-generation-financial-time-series.pdf`.

Coverage of this summary: Read the abstract, table of contents, and introduction in full; Chapter 2 (Stock Shocks modeling and Forecasting) in full; Chapter 3 (LOB-Based Deep Learning Models for SPTP) in full including its appendix model descriptions and additional experimental-results appendix (excluding image-only figures); Chapter 4 (CoMeTS-GAN) in full; Chapter 5 (DiffCATS) through its conclusions and limitations, plus the opening of its theory appendix (the deeper appendix implementation-detail and additional-results subsections were not read in full); Chapter 6 (PLaCy / Robust Causal Discovery with Power-Laws) in full through its conclusions, plus the start of its theoretical-analysis appendix; and the thesis-wide Chapter 7 conclusion. Appendix A ('Additional Research Contributions': FANETs patrolling and geo-distributed AI inference) was not read in depth, as the author states it falls outside the thesis's financial-time-series scope.

Known problems with the input: This is a PhD thesis compiling five largely independent published or submitted papers (Chapters 2-6) plus introduction and conclusion chapters; the extraction above compiles across all of them into one record rather than treating each as a separate study, so per-chapter nuance is compressed; The thesis title page prints an academic-year range ('Academic Year 2025-2026') rather than a single publication year; year from file metadata (year_hint 2026) was used for the year field; Nearly all displayed equations and several complex multi-row tables (e.g., Table 3.6, Table 3.7, Table 6.1, Table 6.2) were converted to garbled inline symbol strings or '==> picture omitted <==' placeholders in the markdown; some multi-row tables required manual realignment of jumbled cells to attribute numbers to the correct method, which carries some residual risk of misattribution despite careful cross-checking against the surrounding prose; Appendix A of the thesis (two additional research contributions on aerial-network patrolling and geo-distributed AI inference) was not reviewed in depth, since the author explicitly describes it as work outside the thesis's financial-time-series scope.
<!-- AUTHORED REGION END -->