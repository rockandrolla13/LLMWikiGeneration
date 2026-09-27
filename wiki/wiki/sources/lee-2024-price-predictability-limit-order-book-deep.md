---
authors:
- Kyungsub Lee
content_hash: sha256:0c71dfe3865be3258c6e87271b944535e6409c28b04540bdce5961773258006f
created: 2026-09-27 01:47:00+00:00
page_id: sources/lee-2024-price-predictability-limit-order-book-deep
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/high-frequency-data
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/market-microstructure
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:d3493cd3ffca46856f3e39dffb54602b794d2943881169b06fde1571fec77c8e
source_path: markdown_output/lee-2024-price-predictability-limit-order-book-deep.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- price-prediction
- volume-imbalance
- market-microstructure
- interpretability
- high-frequency-data
- clock-event
- asset-equity
- harvest-relevant
title: Price predictability in limit order book with deep learning model
updated: '2026-09-27T01:47:00Z'
uuid: 3ba3a67a-82e5-526d-bc16-3efc6050c9a5
year: 2024
---

<!-- AUTHORED REGION START -->
# Price predictability in limit order book with deep learning model

## Summary

The paper asks what actually drives the strong reported accuracy of deep-learning models on high-frequency limit order book (LOB) mid-price prediction, given that such models are hard to interpret and it is unclear whether their accuracy reflects genuine predictability or an artifact of how the prediction target is defined.

The author splits the usual three-class up/down/stable price-prediction problem into two separate questions: whether a model can tell a stable move from a diverging (up-or-down) move, called volatility prediction, and, conditional on a diverging move, whether it can tell the direction, called directional prediction. Using the DeepLOB convolutional-LSTM architecture on Nasdaq TotalView ITCH order-book data for AAPL in 2022 (with additional checks on AMZN, NVDA and MSFT), the model is retrained daily on the preceding 20 days and evaluated out of sample across the whole year, comparing full order-book input against Level-1-only input and against a naive predictor that reuses a past value.

A commonly used target return that averages prices over a forward window is shown to contain overlapping, look-ahead information, so a naive forecast using only the corresponding past-window value performs almost as well as the deep-learning model. Once the target is redefined to compare a current price against a future average with no look-ahead, overall accuracy drops sharply; using price data alone gives essentially chance-level directional accuracy, though volatility (stable-versus-diverging) prediction from price alone remains clearly above chance.

What is new is the demonstration that adding volume information, and specifically the imbalance between bid-side and ask-side volume, restores most of the lost directional predictability, and that Level-1 (top-of-book) data alone performs nearly as well as the full 10-level order book, meaning most of the useful information sits at the top of book and in volume imbalance rather than in book depth.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Time is indexed by integers marking each moment the limit order book changes, not by wall-clock intervals. The model consumes the previous 100 book-update observations as input. The main prediction target is a modified return comparing an average price over a past window to an average price over a future window of length k' (evaluated at k'=20), and a second target compares the current price to the average price over the next 20 updates to remove look-ahead information.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL (Apple Inc.) as the primary instrument, with the same analysis repeated on AMZN, NVDA and MSFT
- **Venue:** Nasdaq TotalView ITCH
- **Period:** 2022, evaluated daily across all trading days of the year, with each day's model retrained on the preceding 20 days and standardization based on the previous five days of data
- **Granularity:** Event-level order book updates covering the top 10 bid and ask price levels, restricted to standard trading hours 09:30 to 16:00, yielding approximately 3 million observations for AAPL

## Features and Measures

- **Modified return $r_{k,k'}$.** A target variable comparing the average of standardized mid-prices over a past window of length k to the average over a future window of length k', used to define up/down/stable classes.
- **$r_{20}$.** A modified return using overlapping past and future windows of 20 observations; shown to contain look-ahead information, which makes a naive last-value forecast almost as accurate as the deep-learning model.
- **$r_{1,20}$.** A modified return comparing the current price to the average price over the next 20 updates, removing the look-ahead problem present in $r_{20}$.
- **Volume imbalance.** An imbalance measure between resting bid-side and ask-side order volume at the top of book, added as an input feature; identified as the main part of the volume data responsible for improving directional prediction.
- **Volatility/directional accuracy decomposition.** A two-step scoring of the three-class problem: the rate of correctly separating stable from diverging (up-or-down) moves, and, among correctly identified diverging cases, the rate of correctly identifying the direction.

## Method

The paper reuses the DeepLOB architecture (Zhang, Zohren and Roberts, 2019): a stack of Conv2D layers, an inception module, a dropout layer at rate 0.2, an LSTM layer with 64 units, and a 3-unit softmax output, applied to a 100-step window of standardized order book data. Two input configurations are tested: the full order book (a 100x40 input using up to 10 price levels of bids, asks and volumes) and a simplified model using only Level-1 best-bid/best-ask prices and volumes (a 100x4 input). Each configuration is retrained daily using the preceding 20 days of data and evaluated out of sample across all 2022 trading days.

Performance is judged first as overall three-class classification accuracy (precision and recall, averaged daily across the year), then decomposed into volatility accuracy (stable versus diverging) and directional accuracy (up versus down, conditional on a correctly identified diverging case). Results are benchmarked against a naive predictor that reuses the corresponding past-window value, and against chance baselines (50% for a binary directional call, roughly a third for the three-class problem). A further set of Level-1 experiments isolates prices only, volumes only, and prices plus volume imbalance as inputs, to identify which inputs drive directional accuracy, and the full comparison is repeated on AMZN, NVDA and MSFT.

## Results

- Using the full order book to predict the look-ahead-contaminated target r20, DeepLOB reached 65.9% overall accuracy, close to a naive predictor using the corresponding past value, which reached 64.8%.
- Switching to the non-look-ahead target r1,20, full-book DeepLOB accuracy fell to 54.6%, still above the 33.3% random-guess baseline for a three-class problem.
- A simplified model using only Level-1 (best bid/ask) data reached 53.6% accuracy on r1,20, nearly matching the full order-book model.
- Decomposing r1,20 predictions, average directional accuracy (up vs down within correctly identified diverging cases) was 71.1% and average volatility accuracy (stable vs diverging) was 69.4%, both above chance.
- Using Level-1 prices alone, directional accuracy fell to essentially chance level, while volatility accuracy from prices alone remained a high 67.5%.
- By asset, directional accuracy from prices alone was close to 50% in every case (0.503 on AAPL, 0.502 on AMZN, 0.499 on MSFT, 0.501 on NVDA).
- Adding volume imbalance to Level-1 prices raised directional accuracy well above the price-only level (0.705 on AAPL, 0.611 on AMZN, 0.632 on MSFT, 0.615 on NVDA), close to the full price-and-volume figures (0.711, 0.615, 0.636, 0.619 respectively).

## Limitations

- The author notes that a strategy aimed at low-risk profits from the volume-imbalance directional signal faces practical limits, since capturing the favorable side of the order book requires competing with other participants for the same orders.
- Reader note: the headline single-asset results are for AAPL only; the multi-stock robustness check is limited to three additional large-cap technology names (AMZN, NVDA, MSFT) in the same year.
- Reader note: directional accuracy is computed only on cases the model already classified as diverging, so it is conditional and not directly comparable to unconditional three-class accuracy.
- Reader note: all data is from a single year (2022) and a single venue feed (Nasdaq TotalView ITCH), so robustness across market regimes or venues is untested.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]

## Citation

Kyungsub Lee (2024). Price predictability in limit order book with deep learning model.

DOI: 10.1080/13504851.2024.2409330

Text ingested: `markdown_output/lee-2024-price-predictability-limit-order-book-deep.md`, converted from `raw/ofi-event-clock/lee-2024-price-predictability-limit-order-book-deep.pdf`.

Coverage of this summary: Read the entire markdown file: abstract, all methodology sections (2.1 through 2.5), all seven tables and the three figure captions, the conclusion, acknowledgements and references.

Known problems with the input: Several equations (the modified return formula, the r20/r1,20 target definitions, and the accuracy formulas) are rendered as omitted images in the markdown; the paper's surrounding prose was used to describe them qualitatively rather than reproducing an exact formal definition.
<!-- AUTHORED REGION END -->