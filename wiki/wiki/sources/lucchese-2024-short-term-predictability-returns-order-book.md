---
authors:
- Lorenzo Lucchese
- Mikko S. Pakkanen
- Almut E. D. Veraart
content_hash: sha256:25275bdccf011515cd60c170fa96984cec268bebcdb5b69efeda1f2c2991c80d
created: 2026-09-27 01:47:00+00:00
page_id: sources/lucchese-2024-short-term-predictability-returns-order-book
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/high-frequency-trading
- concepts/order-flow-prediction
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:4a651dd0cb01ad53897b5cf28e74938aa50fba82f3d80dc970835a54db4e3a4e
source_path: markdown_output/lucchese-2024-short-term-predictability-returns-order-book.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- order-flow
- high-frequency-trading
- model-confidence-sets
- return-predictability
- nasdaq
- multi-horizon-forecasting
- clock-event
- asset-equity
- harvest-relevant
title: 'The Short-Term Predictability of Returns in Order Book Markets: A Deep Learning
  Perspective'
updated: '2026-09-27T01:47:00Z'
uuid: e351e790-e989-5485-ba6c-ef11f950d304
year: 2023
---

<!-- AUTHORED REGION START -->
# The Short-Term Predictability of Returns in Order Book Markets: A Deep Learning Perspective

## Summary

The paper asks whether high-frequency mid-price returns in limit order book markets are predictable from past order-book data, how far ahead such predictability extends, which way of representing the order book works best for a deep-learning predictor, and whether one model can generalise across forecast horizons and across different stocks.

The authors treat prediction as a three-class problem (mid-price moving down, staying flat, or up) and build on the deepLOB convolutional-LSTM architecture. They compare three input representations: raw price/volume order-book snapshots (deepLOB), order flow, i.e. the net change in volume at each price level (deepOF), and a new representation the authors call deepVOL, which reindexes volume by distance in ticks from the mid-price instead of by book level, arguing this is more robust to small perturbations and better suited to convolutional layers; they also test a version using per-order queue (L3) data. A multi-horizon version adds an LSTM encoder plus a sequence-to-sequence decoder so a single trained model can output predictions for several horizons at once. Data come from LOBSTER-reconstructed 10-level order books for ten Nasdaq stocks over about a year, using an order-book event clock that advances once per order-book action rather than by wall-clock time. Each candidate model's out-of-sample cross-entropy loss is compared against an unpredictive benchmark (the empirical training-set return distribution) using the model confidence set statistical testing procedure, repeated over eleven rolling five-week windows.

The paper reports that order-book-driven predictability is widespread at high frequency, typically holding up to roughly 50 to 300 order-book events ahead depending on the stock. Using the top ten levels of the book (L2) clearly beats using only the best bid/ask (L1); moving to per-order (L3) detail gives little extra benefit for stock-specific models but does help when a single model is trained across a pool of stocks. Order-flow and volume-based inputs consistently outperform the plain level-based order-book representation. Multi-horizon seq2seq models beat their single-horizon counterparts for every input type tested. Models trained jointly on several stocks can still detect predictability in stocks they never trained on, which the authors take as evidence of shared trading patterns across tickers.

What is new here is the volume representation itself as a more robust, permutation-tolerant alternative to level-indexed order-book snapshots, its extension to L3 queue data, the systematic multi-horizon seq2seq treatment of order-flow and volume inputs, and the use of model confidence sets to give a statistically formal answer to all four questions rather than relying on point-estimate comparisons.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Time and the prediction horizon h are measured on a discrete order-book event clock that advances by one each time a limit order, market order, or cancellation occurs in the first 10 levels of the book; horizons tested run from 10 up to 1000 such events. Returns are defined between the mid-price at t and a 5-observation-smoothed mid-price around t+h, then discretized into down/flat/up classes using a stock- and window-specific threshold.

## Data

- **Asset class:** Equities
- **Instruments:** 10 Nasdaq-listed stocks (LILAK, QRTEA, XRAY, CHTR, PCAR, EXC, AAL, WBA, ATVI, AAPL), selected to span a range of liquidity levels
- **Venue:** Nasdaq (LOBSTER-reconstructed order books from the TotalView-ITCH feed)
- **Period:** January 2, 2019 to January 31, 2020, with the model confidence set experiments run over 55 weeks from January 14, 2019 to January 31, 2020
- **Granularity:** Full trading-day (9:30-16:00 EST) order-book data reconstructed to L1/L2 (10 price levels) and, for one model variant, L3 (individual order queues); observations are indexed by order-book event, not wall-clock time

## Features and Measures

- **order flow.** The net change in standing volume at a given bid or ask price level between one order-book event and the next, capturing the instantaneous effect of that event on one side of the book.
- **order flow imbalance.** The difference between ask-side and bid-side order flow at the best level, summarising net buying versus selling pressure implied by order-book events.
- **volume representation (deepVOL).** Bid and ask volumes rebinned by distance in ticks from the mid-price rather than by order-book level, giving a fixed-width array that the authors argue is smoother and more robust to small order placements than a level-indexed snapshot.
- **L3 volume feature.** An extension of the volume representation that keeps individual order sizes within the time-priority queue at each price, cut off at a fixed queue depth with remaining orders aggregated, to make use of per-order (L3) data.

## Method

The core network is the deepLOB convolutional-LSTM architecture (CNN and inception modules extracting spatio-temporal features, followed by an LSTM and a softmax output over three return classes). This backbone is fed three alternative inputs: raw order-book snapshots (deepLOB), order flow (deepOF), or the volume representation (deepVOL) at L2 and L3 granularity. For multi-horizon prediction the LSTM acts as an encoder and a sequence-to-sequence decoder rolls forward class-probability predictions across several horizons from one trained model. All models are trained with the Adam optimizer and a weighted categorical cross-entropy loss, with early stopping, on a fixed set of hyperparameters (no tuning), using rolling four-week train/validation and one-week test splits repeated across eleven windows. Model quality is judged by comparing each model's out-of-sample cross-entropy loss on the test week against an unpredictive benchmark (the empirical training-set label distribution) using the model confidence set procedure of Hansen et al., which yields a p-value per model indicating whether it is statistically excluded from the set of best models.

## Results

- Order-book-driven predictability in mid-price returns was found to persist up to about 50 to 300 order-book events ahead depending on the stock.
- For most stocks, predictability was identified up to 50 order-book events ahead at the 99% confidence level.
- deepOF(L2) was placed in the set of superior models 89% of the time at the stricter confidence level, versus only 11% for plain deepLOB(L2) and 0% for the benchmark.
- deepVOL(L2) and deepVOL(L3) performed similarly (84% and 86%), suggesting L3 (per-order) detail adds little for stock-specific models.
- Adding a sequence-to-sequence multi-horizon decoder improved performance over single-horizon models for every input type tested; deepOF(L2, seq2seq) reached 97%.
- Models trained jointly on a pool of stocks could still detect predictability in stocks excluded from training, consistent with shared trading patterns across tickers.
- For these pooled models, L3 volume data became clearly useful, with deepVOL(L3, universal) in the superior set 100% of the time.
- L1-only models, using just the best bid/ask, were rarely placed among the superior models, showing that book depth beyond the top level matters.

## Limitations

- Results are specific to the ten selected Nasdaq stocks, the January 2019-2020 period, and the model architectures tested; the authors note different setups may give different results.
- The paper predicts mid-to-mid returns, which are not directly tradable, and does not test an executable trading strategy, market impact, or execution latency.
- No hyperparameter tuning was carried out for any model, and the training set was downsampled by a factor of 10 for computational reasons.
- Reader note: horizons are measured in order-book events rather than wall-clock time, so predictable horizons are not directly comparable across stocks in physical time.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Lorenzo Lucchese, Mikko S. Pakkanen, Almut E. D. Veraart (2023). The Short-Term Predictability of Returns in Order Book Markets: A Deep Learning Perspective.

DOI: 10.1016/j.ijforecast.2024.02.001

Text ingested: `markdown_output/lucchese-2024-short-term-predictability-returns-order-book.md`, converted from `raw/ofi-event-clock/lucchese-2024-short-term-predictability-returns-order-book.pdf`.

Coverage of this summary: Read the full paper start to finish: abstract, introduction, model descriptions (deepLOB, deepOF, deepVOL, multi-horizon seq2seq), the LOBSTER data and feature-construction section, all four experiment subsections with their result tables, the conclusion, and skimmed the deep-learning and model-confidence-set technical appendices.

Known problems with the input: The paper's date is printed as October 10, 2023, which differs from the year_hint (2024) provided in the job file; year 2023 was used because it is what the paper itself states; Most inline equations and figures render only as picture-omitted placeholders in the converted markdown, so exact equation forms are not reproduced here.
<!-- AUTHORED REGION END -->