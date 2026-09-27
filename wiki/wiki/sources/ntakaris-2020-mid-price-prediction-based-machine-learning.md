---
authors:
- Adamantios Ntakaris
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:afdca08661d4feba75e4cfb80f4a638702a4b6eb010bc0b5740226a6909e849d
created: 2026-09-27 01:47:00+00:00
page_id: sources/ntakaris-2020-mid-price-prediction-based-machine-learning
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/order-imbalance
- concepts/order-flow
- concepts/high-frequency-data
- concepts/mid-price-prediction
- entities/adamantios-ntakaris
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:1b61a2a0abf54100c381c8cb8bb8d73a125894984e590a3c5cc693d34ac1afac
source_path: markdown_output/ntakaris-2020-mid-price-prediction-based-machine-learning.md
source_type: paper
tags:
- mid-price-prediction
- feature-selection
- limit-order-book
- technical-indicators
- nasdaq-nordic
- wrapper-method
- high-frequency-trading
- clock-event
- asset-equity
- harvest-relevant
title: Mid-price Prediction Based on Machine Learning Methods with Technical and Quantitative
  Indicators
updated: '2026-09-27T01:47:00Z'
uuid: 7ba515ab-0939-5efc-9c57-7f2e76433f0b
year: 2020
---

<!-- AUTHORED REGION START -->
# Mid-price Prediction Based on Machine Learning Methods with Technical and Quantitative Indicators

## Summary

The paper asks which of the many features used in high-frequency trading actually help predict the short-term direction of a stock's mid-price, arguing that prior studies typically use a narrow, unmotivated set of indicators. The authors assemble 273 hand-crafted features across three groups: raw and derived limit-order-book statistics, classical technical-analysis indicators, and quantitative/time-series indicators, and add a new feature of their own, an online (adaptive, Hessian-based) logistic regression fit over order-book volumes at the best levels.

To find the most informative subset, the paper converts entropy, least-mean-squares, and linear discriminant analysis into five feature-ranking criteria, each combined with one of three classifiers (LMS, LDA, and a radial-basis-function network), giving twelve sorting-and-classification pipelines. Under an anchored, walk-forward cross-validation scheme, features are added incrementally in ranked order and macro-F1 is tracked to see how few features are needed to reach peak performance. The prediction target is the direction of the mid-price (up, down, stationary) some events ahead, with the label built from the percentage change of a smoothed mid-price against a fixed threshold.

The main finding is that a handful of top-ranked features reach performance close to using the entire 273-feature pool, so most of the pool is redundant for this task. The new adaptive logistic regression feature is ranked first by most of the five sorting criteria, ahead of both classic technical indicators and other quantitative measures, and mixing technical- and quantitative-analysis features outperforms using either family alone.

What is new is the scale of the comparison: the authors describe this as the first wrapper-based comparison of technical, quantitative and LOB-derived features of this size in the high-frequency trading literature, together with the new online logistic-regression feature itself.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are built from blocks of 10 consecutive limit-order-book message events (submissions, cancellations, executions); each 10-message block is treated as one pseudo trading day for computing technical and quantitative features. Prediction horizons are defined at the 10th, 20th and 30th subsequent message-book event (one, two or three blocks ahead), with labels built from the percentage change of a smoothed mid-price against a fixed threshold, using rolling z-score normalization to avoid look-ahead bias.

## Data

- **Asset class:** Equities
- **Instruments:** Five stocks from the FI-2010 benchmark limit order book dataset (Nasdaq Nordic), built from ITCH feed order-book and message data.
- **Venue:** Nasdaq Nordic (ITCH feed)
- **Period:** not stated in the paper's text beyond an example message-list/order-book excerpt dated 01 June 2010 for Wartsila Oyj; the overall sample period for the five-stock dataset is not given.
- **Granularity:** Millisecond-resolution ITCH message and order-book data, aggregated into blocks of 10 message-book events. The full dataset contains 4,581,250 events across five stocks, giving a feature tensor of 273 features by several hundred thousand samples.

## Features and Measures

- **Adaptive logistic regression feature.** An online logistic regression over order-book volumes at the first several LOB levels, updated with an adaptive Hessian-based Newton learning rate every 10-message block; reported as the top-ranked feature under most feature-selection criteria.
- **Basic / time-insensitive / time-sensitive LOB features.** Raw and derived limit-order-book statistics such as spread, mid-price, price and volume differences and means, price/volume derivatives, and average or relative order-arrival intensities computed per 10-message block.
- **Technical-analysis indicators.** A broad set of classical technical indicators (e.g. Bollinger Bands, MACD, RSI, Aroon, ADX, Ichimoku, Donchian channels, moving averages) recomputed on 10-message blocks treated as pseudo trading days.
- **Quantitative / time-series indicators.** Statistical measures including autocorrelation, partial autocorrelation, Engle-Granger cointegration test statistics and p-values, and order book imbalance.

## Method

The experimental protocol follows an anchored (expanding-window) cross-validation over the five-stock dataset: the first day trains and the second tests in the first fold, and each later fold adds the prior training-and-testing period to the training set. Feature relevance is scored with five sorting criteria - sample entropy, two least-mean-squares-based criteria, and two linear-discriminant-analysis-based criteria - each of which ranks the full 273-feature pool. Classification performance for each ranked list is then measured incrementally, adding one feature at a time, using three classifiers: least-mean-squares, linear discriminant analysis, and a radial-basis-function network trained via k-means-initialized extreme-learning-machine-style weights. Accuracy, precision, recall and F1 (with F1 emphasized because of class imbalance) are reported for predicting the mid-price direction at the 10th, 20th and 30th subsequent event.

## Results

- Under entropy sorting, the top 20 ranked features were almost entirely technical indicators (19 of 20), while the top 100 places split into 36 quantitative, 48 technical, and 16 basic-group features.
- Under one LMS-based sorting criterion, the top 20 places were dominated by quantitative features (11 of 20, versus 7 basic-group and 2 technical), and the new adaptive logistic regression feature ranked first; the top 100 places had 25 quantitative, 18 technical, and 57 basic-group features.
- With only 5 top-ranked features, macro-F1 across the twelve sorting-classifier combinations already reached values from about 0.316 up to about 0.421, close to the level obtained using the full 273-feature pool (up to about 0.442).
- The best single-model accuracy reported for a 10-event-ahead horizon was about 0.616 (LDA-based sorting classified with LDA).
- Several sorting-classifier pairs (including the two criteria based on within/between-class scatter ratios) reached their peak F1 with roughly 5 features and then plateaued or declined as more, less-informative features were added.
- The adaptive logistic regression feature placed first in the top-10 ranked list for most of the five sorting criteria, ahead of long-established technical and quantitative indicators.
- The full dataset used contained 4,581,250 message-book events across the five stocks.

## Limitations

- Evaluated on only five stocks from a single exchange group (Nasdaq Nordic); the authors state they intend to test the protocol on a longer trading period in future work.
- The authors suggest the same style of analysis could apply to exchange rates and Bitcoin time series but do not test this themselves.
- The authors note classification performance could likely be improved with more advanced classifiers such as convolutional or recurrent neural networks, but state this comparison is outside the scope of the present evaluation.
- Reader note: prediction horizons are defined in message-block counts (10/20/30 events) rather than calendar time, so results may not translate directly to a fixed-time trading horizon.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Adamantios Ntakaris, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2020). Mid-price Prediction Based on Machine Learning Methods with Technical and Quantitative Indicators.

DOI: 10.1371/journal.pone.0234107

Text ingested: `markdown_output/ntakaris-2020-mid-price-prediction-based-machine-learning.md`, converted from `raw/ofi-event-clock/ntakaris-2020-mid-price-prediction-based-machine-learning.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, related literature, problem statement, feature pool description (main text; Appendix A's per-indicator formulas were skimmed rather than read in full detail), the wrapper feature-selection method, all results tables and discussion, the conclusion, and the reference list.

Known problems with the input: year not printed on this version; year_hint 2020 used; no journal or venue name is given anywhere in the converted markdown; some tables (message list, order book example) show garbled or duplicated cell formatting from the PDF conversion; only the surrounding definitional text was used for factual claims.
<!-- AUTHORED REGION END -->