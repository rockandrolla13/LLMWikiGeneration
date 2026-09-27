---
authors:
- Mostafa Shabani
- Dat Thanh Tran
- Martin Magris
- Juho Kanniainen
- Alexandros Iosifidis
content_hash: sha256:fec6f9b8686c6cb66b960bfff21c4e711e1cb2b5382e26d3a83e02377ea9682a
created: 2026-09-27 01:47:00+00:00
page_id: sources/shabani-2022-multi-head-temporal-attention-augmented-bilinear
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
- concepts/transformers
- concepts/multi-head-attention
- entities/mostafa-shabani
- entities/dat-thanh-tran
- entities/martin-magris
- entities/juho-kanniainen
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:190da8cc79f2ce490e71847a7b64cf7c25bf1bd36aded203bf0d2841222ce6ba
source_path: markdown_output/shabani-2022-multi-head-temporal-attention-augmented-bilinear.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- attention-mechanism
- bilinear-network
- mid-price-prediction
- financial-time-series
- clock-event
- asset-equity
- harvest-relevant
title: MULTI-HEAD TEMPORAL ATTENTION-AUGMENTED BILINEAR NETWORK FOR FINANCIAL TIME
  SERIES PREDICTION
updated: '2026-09-27T01:47:00Z'
uuid: 77d9fad1-3ffe-575f-8146-a0d1a904950e
year: 2022
---

<!-- AUTHORED REGION START -->
# MULTI-HEAD TEMPORAL ATTENTION-AUGMENTED BILINEAR NETWORK FOR FINANCIAL TIME SERIES PREDICTION

## Summary

The paper asks whether a bilinear neural layer for financial time-series can be improved by letting it attend to several relevant time instances at once instead of just one. It builds on the Temporal Attention-augmented Bilinear (TABL) layer, which projects a multivariate time series and applies a single learned temporal attention mask, and proposes a Multi-head TABL (MTABL) layer that runs several attention heads in parallel on the same intermediate representation and concatenates their outputs before projecting back to the original feature dimension.

The approach is evaluated on the task of forecasting the short-horizon direction of the mid-price using publicly available limit-order-book data, comparing MTABL variants with two to five attention heads against the original single-head TABL baseline across three network topologies that stack different combinations of bilinear and TABL layers.

Across all three topologies, adding more attention heads to the final layer improves classification performance over single-head TABL, measured by accuracy, precision, recall and F1-score, with the size of the improvement depending on how many other bilinear layers precede the attention layer. What is new is the multi-head extension itself: rather than a single attention mask per layer, several independently learned masks are computed in parallel and combined by concatenation, which the authors argue lets the layer capture salient temporal patterns that involve pairs or larger subsets of time instances that a single attention head would miss.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are individual limit-order-book update events; each input is a window of such event-level snapshots described by a 40-dimensional feature vector (top ten bid and ask price and volume levels). The prediction target is the direction of the mid-price a fixed number of order events ahead; the benchmark dataset defines horizons of 10, 20, 30, 50 or 100 order events, and the experiments in this paper train and evaluate on the 10-order-event horizon.

## Data

- **Asset class:** Equities
- **Instruments:** not stated (paper only names the FI-2010 benchmark limit-order-book dataset; it does not identify which instruments the data covers)
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** event-by-event limit order book snapshots, using the top 10 bid and ask price and volume levels (40 feature dimensions) per event

## Features and Measures

- **TABL (Temporal Attention-augmented Bilinear layer).** A neural layer that projects each time slice of a multivariate input through a bilinear mapping and applies a single learned, softmax-normalised temporal attention mask to emphasise informative time instances before producing the output.
- **MTABL (Multi-head Temporal Attention Bilinear layer).** The paper's proposed layer, which runs several independent attention heads in parallel on the same intermediate bilinear features, concatenates the attended features from each head along the feature dimension, and linearly projects the concatenation back to the original feature size.

## Method

The proposed MTABL layer follows the same first projection step as TABL, then splits into K parallel attention heads, each with its own learned weight matrix, producing K softmax-normalised attention masks over the time dimension. Each head combines the original and attention-masked features using a learned scalar shared across heads, the attended outputs of all heads are concatenated along the feature dimension, and a linear layer projects the concatenation back to the original feature width before the final TABL output step.

The method is evaluated on the mid-price movement classification task using the FI-2010 limit-order-book benchmark, following the same experimental protocol and three network topologies (stacks of bilinear and TABL/MTABL layers) used in the original TABL paper, replacing only the final TABL layer with MTABL variants using two to five attention heads and comparing them under a concatenation combination strategy.

Performance is judged by accuracy, precision, recall and F1-score, with F1-score used as the primary metric because the label distribution is skewed toward the stationary class; results are reported as the mean and standard deviation over four independent training runs per configuration.

## Results

- For network topology A (single TABL/MTABL output layer), the best configuration (MTABL with 5 heads) reached 72.57% accuracy and 60.90% F1-score, versus 67.21% accuracy and 54.25% F1-score for single-head TABL.
- For topology B (one BL layer plus a TABL/MTABL output layer), MTABL with 5 heads reached 69.16% F1-score versus 69.10% for TABL, while accuracy fell slightly from 78.56% to 78.22%.
- For topology C (two BL layers plus a TABL/MTABL output layer), MTABL with 4 heads reached 83.71% accuracy and 76.42% F1-score, versus 83.52% accuracy and 76.01% F1-score for TABL.
- The size of the improvement from adding attention heads was largest for the simplest topology (A, a single attention layer) and smaller once additional bilinear layers preceded the attention layer (topologies B and C).
- Improved performance from multi-head attention held across different numbers of heads (2 to 5) and across all three topologies tested, using concatenation to combine head outputs.

## Limitations

- Only the concatenation strategy for combining attention heads is evaluated in the reported results; the paper does not report the alternative (summation) combination scheme's results in this text.
- Only the 10-order-event prediction horizon is used in the experiments, even though the benchmark dataset defines five horizons (10, 20, 30, 50, 100 events).
- Reader note: results are reported on a single public benchmark dataset (FI-2010), so generalisation to other markets or instruments is not demonstrated.
- Reader note: the paper does not report statistical significance tests between MTABL and TABL results beyond mean and standard deviation over four runs.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/transformers|transformers]]
- [[concepts/multi-head-attention|multi head attention]]
- [[entities/mostafa-shabani|Mostafa Shabani]]
- [[entities/dat-thanh-tran|Dat Thanh Tran]]
- [[entities/martin-magris|Martin Magris]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Mostafa Shabani, Dat Thanh Tran, Martin Magris, Juho Kanniainen, Alexandros Iosifidis (2022). MULTI-HEAD TEMPORAL ATTENTION-AUGMENTED BILINEAR NETWORK FOR FINANCIAL TIME SERIES PREDICTION.

DOI: 10.23919/eusipco55093.2022.9909957

Text ingested: `markdown_output/shabani-2022-multi-head-temporal-attention-augmented-bilinear.md`, converted from `raw/ofi-event-clock/shabani-2022-multi-head-temporal-attention-augmented-bilinear.pdf`.

Coverage of this summary: Read the full markdown file (abstract through references); it is a short conference-length paper.

Known problems with the input: year from file metadata (no publication year is printed in the converted text; the job file's year_hint of 2022 was used); venue/publication outlet is not printed in the converted text and is left empty; figures and equations were rendered as omitted-picture placeholders, so exact mathematical formulations could not be verified from this markdown.
<!-- AUTHORED REGION END -->