---
authors:
- Jiwon Jung
- Kiseop Lee
content_hash: sha256:a80081c0733970ef44793a1be992049893f7e78fe3446c269cc0188caa5bc19a
created: 2026-09-27 01:47:00+00:00
page_id: sources/jung-2025-attention-based-reading-highlighting-forecasting-limit
page_type: source
related:
- concepts/limit-order-book
- concepts/transformers
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
- concepts/lstm-networks
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:6d66c109041d67b7a91c7eb9ff122fdca47b6d59912359b6b75a5ea2644e2568
source_path: markdown_output/jung-2025-attention-based-reading-highlighting-forecasting-limit.md
source_type: paper
tags:
- limit-order-book
- attention-mechanism
- multi-level-forecasting
- transformers
- high-frequency-data
- sequence-to-sequence
- clock-calendar
- asset-equity
- harvest-relevant
title: Attention-Based Reading, Highlighting, and Forecasting of the Limit Order Book
updated: '2026-09-27T01:47:00Z'
uuid: 55f962a5-07f4-5167-85a6-a7ffa37b9e14
year: 2024
---

<!-- AUTHORED REGION START -->
# Attention-Based Reading, Highlighting, and Forecasting of the Limit Order Book

## Summary

The paper asks whether an attention-based model can forecast the whole multi-level limit order book (prices and volumes at every depth level), rather than just the mid-price, arguing that the mid-price alone hides differences in depth and spread that matter for execution.

Its approach is a Spacetimeformer-based encoder-decoder in which a new compound multivariate embedding gives separate learned embeddings to order side, price level, feature type (price or volume), and stock, then combines them, alongside Time2Vec time features. To fight non-stationarity in multi-level prices within a trading day, inputs are transformed with a percent-change step followed by variable-wise min-max scaling, and an ordinal structural regularizer penalizes any predicted violation of bid/ask price ordering across levels.

Using LOBSTER level-5 order book data for five technology stocks resampled to a 5-second calendar grid, the compound-embedding model is compared against a linear model, an LSTM, an Informer-style temporal-attention model, and the original spacetimeformer. The compound model achieves the lowest mid-price and structural-violation error of the group, and combining the percent-change and min-max transforms cuts error far more than either alone.

What is new is extending attention-based LOB forecasting beyond the mid-price to the full depth of prices and volumes while keeping the predicted book internally ordered, via the compound embedding and the ordinal regularizer.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

LOB snapshots are resampled onto a fixed 5-second calendar grid (about 4,680 bars over the trading day) rather than kept in native millisecond event time; the model consumes a 120-step (10-minute) context window and predicts the following 24 steps (2 minutes) at every level of the book.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL, GOOG, INTC, MSFT, AMZN (five LOBSTER Nasdaq-listed technology stocks, concatenated into one 100-dimensional dataset)
- **Venue:** not stated
- **Period:** single trading day, June 21, 2012, 9:30am-4:00pm
- **Granularity:** Level-5 bid/ask price-volume snapshots resampled to 5-second bars

## Features and Measures

- **Compound multivariate embedding.** A learned embedding scheme that gives each attribute of a LOB observation (order side, price level, price-vs-volume, and stock) its own embedding layer, then combines and scales them, instead of assigning one embedding per raw variable as in the original spacetimeformer.
- **Percent-change transformation.** Converts each price series to period-over-period percentage changes before feeding the model, to reduce the non-stationarity of raw multi-level prices within a trading day.
- **Min-max scaling.** Rescales price and volume series variable-by-variable so that high-variance volume series do not dominate the loss relative to price series.
- **Structural (ordinal) regularizer.** An added penalty term based on a ReLU function that discourages the model from predicting a lower level's ask price below a higher level's ask price (or a lower level's bid above a higher level's bid), keeping predicted books internally consistent.

## Method

The model is an attention-based encoder-decoder built on the spacetimeformer architecture, using self-attention in the encoder and masked attention in the decoder, with the Performer approximation used to keep attention cost roughly linear in sequence length. Inputs are embedded via Time2Vec time features plus the compound multivariate embedding, and a binary flag marks whether a token belongs to the context or the target window. Training minimizes mean squared error on level-5 bid/ask prices and volumes plus a weighted ordinal structural-regularizer term ($w_o=0.01$), with mean absolute error tracked for reference only. Optimization uses a learning-rate decay factor of 0.8 with 1000 warm-up steps, three attention heads, early stopping after 10 epochs without validation improvement, and training on a single A100 GPU. Performance is judged against a linear autoregressive baseline, an LSTM, an Informer-style temporal-attention model, and the original spacetimeformer, each scored by MSE and MAE on mid-price, multi-level price, and multi-level volume forecasts, plus structural-loss and total-loss metrics.

## Results

- Combining percent-change and min-max input transforms gave the lowest error of any transform choice, MSE 0.0464 and MAE 0.1260, versus MSE 4.5447/MAE 1.3225 for percent-change alone and MSE 0.0660/MAE 0.1469 for min-max alone.
- The compound multivariate embedding model had the lowest mid-price error of the five models tested (MSE 0.0120, MAE 0.1388), ahead of the plain spacetimeformer (MSE 0.0122, MAE 0.1425) and the temporal-attention model (MSE 0.0124, MAE 0.1520).
- For multi-level price forecasts the compound model and the spacetimeformer tied on MSE (0.0025 each) while the compound model had the lower MAE (0.0288 vs 0.0293).
- For multi-level volume forecasts the spacetimeformer had a marginally lower MSE (0.0105) than the compound model (0.0106), but the compound model had the lowest MAE (0.0504).
- The compound model's structure loss (0.1480) was far below the spacetimeformer's (0.5774) and the temporal model's (0.8836), and it also had the lowest total loss (0.0080 vs 0.0123 and 0.0157), showing it best preserved correct level ordering.
- On held-out AMZN test windows, the compound embedding tracked the actual downward price trend and preserved level ordering more closely than the temporal-attention baseline, which broke the ordinal structure between levels.

## Limitations

- The model cannot attribute predicted changes to specific causes such as new orders, cancellations, or executions, since it only sees aggregated price and volume levels.
- Experiments were restricted to the top five levels of the book because of computational resource limits.
- Reader note: all results come from a single trading day (June 21, 2012) and five large technology stocks, so generalization to other days, regimes, or asset types is untested.
- Reader note: the compound model's advantage was not uniform across every metric (the spacetimeformer had a marginally lower multi-level volume MSE), so gains are strongest for price and structure but mixed for volume.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/transformers|transformers]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Jiwon Jung, Kiseop Lee (2024). Attention-Based Reading, Highlighting, and Forecasting of the Limit Order Book.

DOI: 10.1080/14697688.2025.2522914

Text ingested: `markdown_output/jung-2025-attention-based-reading-highlighting-forecasting-limit.md`, converted from `raw/ofi-event-clock/jung-2025-attention-based-reading-highlighting-forecasting-limit.pdf`.

Coverage of this summary: Read the full markdown file: introduction, data, method, results, discussion, conclusion, and the supplementary figure captions.

Known problems with the input: The paper's running header prints the date 'November 5, 2024' throughout, but the job file's year_hint is 2025; used 2024 (the printed date) as year and flag the discrepancy here; No venue name is printed in the visible text; the running-header code 'ws-ijtaf' suggests the International Journal of Theoretical and Applied Finance but this is not confirmed in the text, so venue is left not stated.
<!-- AUTHORED REGION END -->