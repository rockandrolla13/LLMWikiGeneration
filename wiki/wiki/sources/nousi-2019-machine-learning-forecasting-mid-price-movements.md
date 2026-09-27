---
authors:
- Paraskevi Nousi
- Avraam Tsantekidis
- Nikolaos Passalis
- Adamantios Ntakaris
- Juho Kanniainen
- Anastasios Tefas
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:51c14432a8b4a1a99129f1f1baca567cc6719adaa5012e72394a1a6321453fcb
created: 2026-09-27 01:47:00+00:00
page_id: sources/nousi-2019-machine-learning-forecasting-mid-price-movements
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/feature-engineering
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/market-microstructure-noise
- concepts/order-flow-prediction
- concepts/high-frequency-data
- concepts/mid-price-prediction
- entities/avraam-tsantekidis
- entities/nikolaos-passalis
- entities/adamantios-ntakaris
- entities/juho-kanniainen
- entities/anastasios-tefas
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:705e80a389c0e6e891feccbf86bdd830c347d95c6adca38b0c60e9708f787a52
source_path: markdown_output/nousi-2019-machine-learning-forecasting-mid-price-movements.md
source_type: paper
tags:
- limit-order-book
- machine-learning
- mid-price-prediction
- feature-extraction
- class-imbalance
- high-frequency-trading
- autoencoder
- bag-of-features
- clock-event
- asset-equity
- harvest-relevant
title: Machine Learning for Forecasting Mid Price Movement using Limit Order Book
  Data
updated: '2026-09-27T01:47:00Z'
uuid: 8ad71e72-98f9-565b-b7db-7fc2118d55d7
year: 2019
---

<!-- AUTHORED REGION START -->
# Machine Learning for Forecasting Mid Price Movement using Limit Order Book Data

## Summary

The paper asks how much information the limit order book itself carries about the near-future direction of a stock's mid-price, and whether combining handcrafted microstructure features with features learned by unsupervised methods (autoencoders, Bag-of-Features) improves on handcrafted features alone. It works with five Finnish stocks' full order-book data from Nasdaq Nordic and frames the problem as three-class classification (up, down, no-change) at three prediction horizons.

From the raw order book the authors extract a 144-dimensional handcrafted feature vector per snapshot (prices and volumes at each book level, spreads, mid-price, and average intensities of trades, orders, cancellations and executions), then build four sliding-window variants over a window of 5 consecutive snapshots (the last vector alone, the window mean, and two concatenations), plus two learned, lower-dimensional representations: a 24-dimensional autoencoder bottleneck and a 128-bin Bag-of-Features histogram built by k-means clustering. Three classifiers - a linear SVM trained with SGD, a Single-hidden-Layer Feedforward Network whose hidden layer is fixed by k-means RBF prototypes, and a two-hidden-layer Multilayer Perceptron trained with Adam - are evaluated on eight combinations of these representations, using an anchored walk-forward split and a stock hold-out split, and judged by macro-averaged precision, recall and F-score because the up/down/no-change labels are heavily imbalanced.

The MLP performed best overall, with the SVM close behind and the SLFN clearly weaker in both evaluation setups. Higher-dimensional, temporally-aware representations (concat, last-plus-mean, mean) beat single-snapshot or heavily compressed ones, though pairing a compressed learned representation with a handcrafted one often helped. Both classifiers found it easier to predict the average mid-price move 5 or 10 samples ahead than the move at the very next sample, and the stock hold-out results show that patterns learned from some stocks transfer to an unseen stock, suggesting the classifiers pick up market-wide structure rather than only stock-specific quirks.

The authors present this as a large-scale study (on the order of 4.5 million raw order-book events) that systematically combines handcrafted limit-order-book features with unsupervised feature-learning methods across multiple classifiers, horizons and evaluation protocols, backed by a formal statistical comparison (Friedman and Nemenyi tests) and a run-time complexity analysis aimed at real-time high-frequency trading constraints, positioning the work as strong traditional-ML baselines ahead of more complex deep architectures.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

One feature vector is extracted every 10 limit-order events that change the order book, an event clock rather than calendar time, subsampling about 4.5 million raw events down to 453.975 extracted feature vectors. A 5-sample sliding window over these event-indexed snapshots supplies temporal context to the classifiers. The prediction horizon is defined by comparing a smoothed mid-price (averaged over the past 9 snapshots) to the mean of the smoothed mid-price over the next 1, 5 or 10 snapshots, so the horizon is measured in event-clock samples rather than wall-clock time.

## Data

- **Asset class:** Equities
- **Instruments:** Kesko Oyj, Outokumpu Oyj, Sampo, Rautaruukki and Wartsila Oyj (five Finnish stocks)
- **Venue:** Nasdaq Nordic
- **Period:** 1 June 2010 to 14 June 2010 (business days only)
- **Granularity:** Limit order book snapshots with 10 price levels per side (40 raw values per snapshot), subsampled to one feature vector per 10 order-book events; about 4.5 million raw events over 10 trading days yielding 453.975 extracted feature vectors.

## Features and Measures

- **Handcrafted LOB feature vector (144-dimensional).** A per-snapshot feature set combining raw prices and volumes at each of the 10 order-book levels, time-insensitive features (spread, mid-price, price and volume differences and spreads), and time-sensitive features (average intensities of trades, orders, cancellations, deletions and executions, plus their derivatives).
- **Sliding-window representations (last, mean, last-plus-mean, concat).** Four ways of combining the handcrafted feature vector over a window of 5 consecutive snapshots: the most recent vector alone, the mean of the 5 vectors, the concatenation of the last vector with the window mean, and the concatenation of all 5 vectors.
- **Autoencoder (AE) representation.** A 5-layer autoencoder (144-72-24-72-144 neurons) trained to reconstruct the 144-dimensional last feature vector; the 24-dimensional middle-layer activation is used as a learned, lower-dimensional feature representation.
- **Bag-of-Features (BoF) representation.** A 128-bin histogram built by k-means clustering a sample of feature vectors into codewords, then softly assigning each of the 5 window vectors to those codewords with a fuzziness parameter and averaging the memberships into one histogram per sample.
- **Mid-price movement label.** A three-class label (up, down, no-change) formed by comparing a smoothed mid-price averaged over the past N-beta snapshots to the mean of the smoothed mid-price over the next N-alpha snapshots, with a threshold gamma controlling how large the move must be to count as a change.

## Method

The paper builds four handcrafted representations (last, mean, last-plus-mean, concat) from a 5-sample sliding window over the 144-dimensional per-snapshot feature vector, and separately learns two lower-dimensional representations from the same underlying features: a 24-dimensional autoencoder bottleneck and a 128-bin Bag-of-Features histogram from k-means clustering. All inputs are z-score standardized. Eight combinations of raw and learned representations (including concatenations such as last-plus-BoF and AE-plus-BoF) are then used as inputs to the classifiers.

Three classifiers predict the three-class mid-price movement label at three horizons (Nalpha = 1, 5, 10 samples ahead): a linear SVM trained with SGD and per-class regularization weights inversely proportional to class frequency; a Single-hidden-Layer Feedforward Network (SLFN) whose 1000 hidden-layer weights are fixed by k-means clustering into RBF prototypes and whose output layer is trained with a max-margin objective; and a Multilayer Perceptron with two 512-unit hidden layers trained with the Adam optimizer and a categorical cross-entropy loss. All three use class weights to counter the imbalance toward the no-change label.

Two evaluation protocols are used: an anchored walk-forward setup (train on the first d days, test on day d+1, progressing through all 9 folds) and a stock hold-out setup (train on 4 of the 5 stocks, test on the unseen stock, repeated 5 times). Performance is judged by macro-averaged precision, recall and F-score, since plain accuracy is uninformative under the class imbalance; classifier and representation differences are tested for statistical significance with Friedman's test and the Nemenyi post-hoc test, and a separate run-time analysis measures prediction speed on a GPU.

## Results

- Comparing the three classifiers, Friedman's test rejected equal performance (p = 3.9x10^-26); Nemenyi tests showed the SVM and the MLP were both significantly better than the SLFN, but not significantly different from each other.
- Comparing the eight input representations, Friedman's test again rejected equal performance (p = 5.5x10^-35); the concat, last-plus-mean and mean representations were significantly better than most of the others, and predictive power broadly tracked representation dimensionality.
- Predicting the average mid-price movement 5 or 10 samples ahead was generally easier than predicting the movement at the immediately following 1 sample, especially for the SVM and SLFN classifiers.
- The best MLP result (concat representation, Nalpha = 5, anchored walk-forward setup) reached macro precision 62.71+/-5.80, recall 53.72+/-3.63 and F-score 56.06+/-2.82.
- Per-class scores for the MLP (concat representation, Nalpha = 10) showed higher precision than recall on the up and down classes (49.60+/-9.68 precision / 32.40+/-7.44 recall for up; 52.90+/-11.33 / 27.23+/-8.68 for down), reflecting the imbalance toward the no-change class.
- Combining a compressed learned representation (AE or BoF) with a handcrafted one, such as last-plus-BoF, often improved on using the handcrafted representation alone, particularly for the SVM classifier.
- In the stock hold-out setup the MLP again generalized best to an unseen stock, while the SLFN's F-score varied a great deal across folds, indicating it struggled to transfer information across stocks.
- In the run-time analysis the SVM was fastest (over 14,000 transactions per second on a mid-range GPU) and the MLP slowest but still processed almost 7,000 transactions per second, so all three models met the paper's real-time high-frequency trading benchmark.

## Limitations

- Reader note: the dataset covers only 10 trading days and 5 Finnish stocks from a single venue (Nasdaq Nordic) in June 2010, so the reported accuracy may not generalize to other markets, periods or instrument types.
- Reader note: the three-class labels depend on small, hand-chosen gamma thresholds (0.0001, 0.0002, 0.0003) to define 'no change'; the authors themselves note this is a trade-off between class balance and the meaningfulness of the labels.
- Reader note: the paper benchmarks traditional ML methods (SVM, SLFN, MLP) rather than the deep recurrent or convolutional architectures cited in its own related work, so it does not show whether these simpler baselines are competitive with more complex sequence models on the same data.
- The authors state their computational-complexity analysis covers only prediction time, not training time, reasoning that real-time constraints can be relaxed during training by using a slightly outdated model in production.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[entities/avraam-tsantekidis|Avraam Tsantekidis]]
- [[entities/nikolaos-passalis|Nikolaos Passalis]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/anastasios-tefas|Anastasios Tefas]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Paraskevi Nousi, Avraam Tsantekidis, Nikolaos Passalis, Adamantios Ntakaris, Juho Kanniainen, Anastasios Tefas, Moncef Gabbouj, Alexandros Iosifidis (2019). Machine Learning for Forecasting Mid Price Movement using Limit Order Book Data.

DOI: 10.1109/access.2019.2916793

Text ingested: `markdown_output/nousi-2019-machine-learning-forecasting-mid-price-movements.md`, converted from `raw/ofi-event-clock/nousi-2019-machine-learning-forecasting-mid-price-movements.pdf`.

Coverage of this summary: Read the entire markdown file (abstract, introduction, related work, the LOB data description, the full proposed-methodology section, all of the experimental evaluation and statistical-analysis sections, and the conclusion); the paper is under the full-read threshold.

Known problems with the input: year from file metadata (no publication year is printed on the paper itself in the converted text; year taken from job file year_hint); no journal or conference name is printed anywhere in the converted markdown, so venue is left empty; the count '453.975 extracted feature vectors' is printed with a period where a thousands separator would normally go (i.e. it likely means 453,975); it is reproduced here exactly as printed rather than reinterpreted.
<!-- AUTHORED REGION END -->