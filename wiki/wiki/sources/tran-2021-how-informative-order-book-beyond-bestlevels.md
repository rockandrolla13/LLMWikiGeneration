---
authors:
- Dat Thanh Tran
- Juho Kanniainen
content_hash: sha256:cbdcf1857886d145584e99f2929867e42f54cf447d4441ba50ba712593688b1a
created: 2026-09-27 01:47:00+00:00
page_id: sources/tran-2021-how-informative-order-book-beyond-bestlevels
page_type: source
publication_venue: NeurIPS 2021 Workshop on Machine Learning Meets Econometrics (MLECON)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/high-frequency-data
- concepts/mid-price-prediction
- entities/dat-thanh-tran
- entities/juho-kanniainen
revision_id: 1
schema_version: 2
source_hash: sha256:0ae3495bc23f89beb1147cca60a5a4bb43139d576aeefcd34fd5d9541c3766e2
source_path: markdown_output/tran-2021-how-informative-order-book-beyond-bestlevels.md
source_type: paper
tags:
- limit-order-book
- feature-selection
- mid-price-prediction
- deep-learning
- order-book-levels
- machine-learning-finance
- clock-event
- asset-equity
- harvest-relevant
title: How informative is the Order Book Beyond the Best Levels? Machine Learning
  Perspective
updated: '2026-09-27T01:47:00Z'
uuid: fc94b7a0-696f-52c7-83da-fa21a284a418
year: 2021
---

<!-- AUTHORED REGION START -->
# How informative is the Order Book Beyond the Best Levels? Machine Learning Perspective

## Summary

The paper asks whether excluding order-book quotes beyond the best bid/ask level (Level-I data) degrades the predictive performance of models forecasting mid-price movement, and whether using all available price levels maximises predictive power, given that much existing research relies on Level-I data alone for tractability while a linear-model literature has only partly addressed the question.

The authors apply two feature-selection methods, Backward Elimination (BE) and Binary Particle Swarm Optimization (BPSO), to two state-of-the-art nonlinear LOB neural networks, DeepLOB and TABL, using order-book data from two markets (five Helsinki Stock Exchange-listed Nordic stocks, and Amazon and Google in the US) collected over ten trading days via the TotalView-ITCH feed. Models are trained to classify the future mid-price direction (up, down or stationary) at three prediction horizons (10, 20 and 50 order-book events ahead), giving 24 configurations each repeated 20 times.

Across both feature-selection methods, both network architectures and both markets, Level 1 (the best bid/ask) is by far the most frequently retained level: it is the sole surviving level in 100% of US configurations under BE, and is chosen far more often than any other level in the final BPSO solutions. The top three levels also rank in the same order as their execution priority in the book. However, restricting the model to only the most informative level(s) selected by BE or BPSO costs on average 2 to 4 percentage points of F1 score compared with using all ten levels, showing that deeper levels still carry complementary information.

The contribution is the first data-driven test of order-book informativeness that allows nonlinear interactions between levels (via deep neural networks) rather than assuming a linear relationship, and that requires consensus across two feature-selection methods, two network architectures and two markets before drawing conclusions.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Model inputs are the ten most recent order-book events (top ten bid and ask prices and volumes) at each time index, so observations are sampled per order-book event rather than by wall-clock time. The prediction target is the future mid-price movement (up, down or stationary) evaluated at horizons of H = 10, 20 and 50 order-book events ahead.

## Data

- **Asset class:** Equities
- **Instruments:** Five Nordic stocks listed on the Helsinki Stock Exchange (Kesko, Outokumpu, Rautaruukki, Sampo, Wartsila) and two US stocks (Amazon and Google)
- **Venue:** Helsinki Stock Exchange (Nordic data); US market via the TotalView-ITCH feed (US data)
- **Period:** 22 September 2015 to 5 October 2015 (ten working days); the first seven days used for training and validation, the last three days held out as the test set
- **Granularity:** Full order-book event data across ten levels per side; approximately 13 million events for the US dataset and 4 million events for the Nordic dataset

## Features and Measures

- **Backward Elimination (BE).** A feature-selection procedure that starts from all ten order-book levels and repeatedly retrains the network with one level removed at a time, discarding whichever level's removal costs the least prediction performance, until a single level remains.
- **Binary Particle Swarm Optimization (BPSO).** A swarm-based binary optimiser that searches over a mask of order-book levels to include or exclude, guided by a fitness function based on the network's F1 score, without a predefined subset size.
- **DeepLOB.** A deep convolutional neural network architecture that takes raw multi-level order-book snapshots as input to classify future mid-price direction.
- **TABL.** The Temporal Attention-augmented Bilinear Layer network, a neural architecture for classifying LOB-derived multivariate time series.

## Method

For each combination of two networks (DeepLOB, TABL), two feature-selection methods (BE, BPSO), two datasets (US, Nordic) and three prediction horizons (10, 20, 50 events), the experiment is repeated 20 times, giving 24 configurations in total. BE is run by training a separate network for each candidate elimination and removing the level whose omission least hurts test performance, continuing until one level remains; BPSO instead optimises a binary mask over the ten levels to maximise the F1 score of a jointly trained network, using particle velocity and position update rules from swarm optimisation. Mean and standard deviation of the held-out test F1 score are reported for each configuration, and results are compared against a baseline model trained on all ten levels.

## Results

- Backward Elimination selected Level 1 as the single surviving level in 100% of US configurations across both networks and all three horizons.
- For Nordic data, Level 1 was the sole surviving level in at least 90% of runs for most configurations, the only exception being TABL at horizon 10.
- In the average two-element subset chosen by BE, Level 1 appeared 98.33% of the time and Level 2 was the next most frequent, at 25.42%.
- Restricting the model to the BE-selected most informative level(s) instead of all ten levels reduced F1 score by an average of 3.76% for US stocks and 3.58% for Nordic stocks.
- Restricting the model to the BPSO-selected subset instead of all ten levels reduced F1 score by an average of 2.43% for US stocks and 3.10% for Nordic stocks.
- Baseline (all-levels) F1 scores across the two networks, two markets and three horizons ranged from about 64.31% to 71.89%.
- The top three order-book levels were ranked in the same order by both BE and BPSO, matching their execution priority in the book.
- Overall, including all levels rather than only the single most informative one improved performance by around 3.5%, and informativeness decreases from the first to the fourth level before levelling off.

## Limitations

- Reader note: only two markets and seven stocks in total (two US, five Nordic) over a ten-trading-day window were used, so results may not generalise to other markets or periods.
- The authors note the performance gain from using all levels versus only the best level is a few percentage points, and whether that gain outweighs the added computational cost depends on the application.
- Feature-selection outcomes vary across runs because both BE and BPSO rely on stochastic-gradient-descent-trained networks, so the selected subsets are not perfectly reproducible run to run.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[entities/dat-thanh-tran|Dat Thanh Tran]]
- [[entities/juho-kanniainen|Juho Kanniainen]]

## Citation

Dat Thanh Tran, Juho Kanniainen (2021). How informative is the Order Book Beyond the Best Levels? Machine Learning Perspective. NeurIPS 2021 Workshop on Machine Learning Meets Econometrics (MLECON).

DOI: 10.2139/ssrn.3920827

Text ingested: `markdown_output/tran-2021-how-informative-order-book-beyond-bestlevels.md`, converted from `raw/ofi-event-clock/tran-2021-how-informative-order-book-beyond-bestlevels.pdf`.

Coverage of this summary: Read the full workshop paper: abstract, introduction, the feature-selection method section, and the empirical results and conclusion sections.

Known problems with the input: The byline lists a third affiliation (Department of Engineering, Aarhus University, Aarhus, Denmark, email ai@ece.au.dk) with no accompanying name visible in the converted text, so only two named authors are listed here; the third author's name did not survive PDF-to-markdown conversion.
<!-- AUTHORED REGION END -->