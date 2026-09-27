---
authors:
- Antonio Briola
- Silvia Bartolucci
- Tomaso Aste
content_hash: sha256:f963db8e2d540ccc490f2c7d353cfc405c0533a4d7e002e5416935b25f0de008
created: 2026-09-27 01:47:00+00:00
page_id: sources/briola-2024-hlobinformation-persistence-structure-limit-order-books
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
- concepts/stylized-facts
- concepts/lstm-networks
- entities/antonio-briola
- entities/tomaso-aste
revision_id: 1
schema_version: 2
source_hash: sha256:8dac309929ef87ebe22951b46b87faf349533e153532fb18d8759f5a08185c4c
source_path: markdown_output/briola-2024-hlobinformation-persistence-structure-limit-order-books.md
source_type: paper
tags:
- hlob
- limit-order-book
- deep-learning
- tmfg
- information-filtering-networks
- tick-size
- mid-price-prediction
- nasdaq
- clock-event
- asset-equity
- harvest-relevant
title: HLOB – Information Persistence and Structure in Limit Order Books
updated: '2026-09-27T01:47:00Z'
uuid: 418cc40f-7acc-5ca0-8ed7-0805d05c704c
year: 2024
---

<!-- AUTHORED REGION START -->
# HLOB – Information Persistence and Structure in Limit Order Books

## Summary

The paper asks whether modeling higher-order, non-adjacent dependencies among a limit order book's volume levels — rather than only dependencies between consecutive levels, as in prior CNN-LSTM models — improves forecasts of the direction of mid-price changes at high frequency. It builds on the authors' earlier finding that stocks' microstructural tick-size class (small, medium, or large tick) governs how sparse or compact the LOB's structure is, and therefore how learnable it is.

The method, HLOB, first strips price information from each LOB snapshot, bins the remaining volumes, and computes a pairwise mutual-information matrix between volume levels for each stock, averaged over the training days. A Triangulated Maximally Filtered Graph (TMFG) is built from this matrix, and the tetrahedra, triangles and edges (cliques of size 4, 3 and 2) it contains are extracted as three separate input views, each re-combined with the corresponding price levels and a 100-step history window. Each view is passed through its own 3-layer convolutional head (styled after a Homological Convolutional Neural Network), the three heads are concatenated, and an LSTM plus a linear layer produce the final 3-class direction forecast.

HLOB is benchmarked against 9 other deep learning models (CNN1, CNN2, DLA, Transformer, iTransformer, LobTransformer, BinBTabl, BinCTabl, DeepLOB) on 15 NASDAQ stocks split into small-, medium- and large-tick groups, across three prediction horizons and three calendar years, using F1, MCC and a round-trip-transaction probability metric. HLOB is the best or tied-best model in most short-horizon cases and for large-tick stocks generally, but loses its edge over the dual-attention BinBTabl/BinCTabl models at longer horizons, especially for small- and medium-tick stocks.

What is new is the direct link the authors draw between a stock's tick-size class, the spatial concentration of mutual information across its LOB levels, and how quickly a spatially-informed model's edge decays as the prediction horizon lengthens: large-tick stocks show a compact, hierarchical MI structure that stays informative at longer horizons, while small- and medium-tick stocks show sparser, drift-prone structure that HLOB can only exploit at short horizons.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are consecutive LOB snapshots recorded after each order-book update (tick-by-tick, unevenly spaced in physical time). Prediction horizons of 10, 50 and 100 LOB updates are used, defined purely as a count of updates ahead, never as elapsed wall-clock time; a move only counts as up/down if the simple mid-price difference over that many updates is at least one tick.

## Data

- **Asset class:** Equities
- **Instruments:** 15 NASDAQ-listed stocks split into small-tick (CHTR, GOOG, GS, IBM, MCD, NVDA), medium-tick (AAPL, ABBV, PM) and large-tick (BAC, CSCO, KO, ORCL, PFE, VZ) groups
- **Venue:** NASDAQ
- **Period:** January 2017 to December 2019 (three separate one-year windows: 2017, 2018, 2019)
- **Granularity:** Tick-by-tick limit order book data from the LOBSTER provider, 10 price/volume levels per side

## Features and Measures

- **Triangulated Maximally Filtered Graph (TMFG) similarity structure.** A planar, chordal graph built by iteratively joining the LOB's volume levels that share the highest pairwise mutual information, used to encode which volume levels are structurally dependent on each other.
- **HLOB architecture (Homological Convolutional Neural Network + LSTM).** A three-headed convolutional architecture whose filter structure mirrors the tetrahedra, triangles and edges extracted from the TMFG, followed by an LSTM to add temporal memory, used to forecast the direction of mid-price changes.
- **Actual LOB depth (Ξ).** A measure of how many nominal price levels are needed to span a fixed distance in the book on the bid or ask side, used to explain when the LOB's spatial structure is stable enough for mutual-information-based modeling to remain reliable.
- **Probability of correct round-trip transaction (p_T).** The share of simulated round-trip trades, triggered by the model's prediction, that would have been profitable; used alongside F1 and MCC to judge trading practicability.

## Method

For each stock, LOB snapshots are reduced to volume-only data, binned, and used to compute a pairwise mutual-information (MI) matrix between the 20 volume levels (10 per side), averaged across the training days of that year. A TMFG is built from this averaged MI matrix, and its maximal cliques of size 4, 3 and 2 (tetrahedra, triangles, edges) are isolated. For every timestamp in a 100-step history window, each clique set is flattened and the corresponding price levels are re-inserted, producing three separate input tensors that are fed to three parallel convolutional heads; each head applies three convolutional layers whose filter sizes and strides are set deterministically by the clique structure. The three heads' outputs are concatenated, passed through an LSTM and a linear output layer, and trained with categorical cross-entropy via AdamW.

HLOB is compared against 9 benchmark deep learning models spanning CNN, attention and transformer families, all run inside the same 'LOBFrame' pipeline for reproducibility. Models are trained per stock and year with balanced mini-batch sampling, evaluated on F1 score, Matthews Correlation Coefficient, and the probability of a correctly executed round-trip transaction, with results averaged within each tick-size group and across the three prediction horizons.

## Results

- HLOB outperformed the 9 benchmark models (by summed F1+MCC+p_T) in 73.3% of stock cases at horizon 10, in 60% of cases at horizon 50, and in 33% of cases at horizon 100.
- At horizon 10, HLOB's average F1 was 0.42 for small-tick stocks, 0.41 for medium-tick stocks, and 0.48 for large-tick stocks.
- At horizon 100, HLOB's average F1 fell to 0.32 (small-tick) and 0.35 (medium-tick), while rising to 0.52 for large-tick stocks.
- HLOB consistently outperformed DeepLOB, its closest structure-agnostic architectural relative, at all three horizons and across all tick-size groups.
- BinBTabl and BinCTabl, which apply a dual attention mechanism over both spatial and temporal dimensions, overtook HLOB at horizons 50 and 100, particularly for small- and medium-tick stocks.
- Large-tick stocks showed the highest and most hierarchically organized mutual information (e.g., not-normalized average MI of 1.18 for BAC, 1.00 for CSCO), and the 'actual LOB depth' Ξ for these stocks stayed close to 9.00, indicating a stable spatial structure.
- Small-tick stocks such as CHTR and GOOG showed much higher and unstable actual LOB depth (mean Ξ around 50-70), which the authors link to faster degradation of HLOB's forecasting edge at longer horizons.
- Across the full study, 1350 experiments were run (15 stocks × 3 years × 10 models × 3 horizons), consuming a cumulative 7192 hours of GPU runtime.

## Limitations

- The TMFG/mutual-information structure is computed once as a training-set average and stays fixed; the authors flag temporally-evolving IFNs as future work.
- HLOB's advantage over dual-attention competitors (BinBTabl, BinCTabl) disappears at longer horizons (50, 100 updates), especially for small- and medium-tick stocks.
- Reader note: the study covers only 15 large-to-mega-cap NASDAQ stocks over 2017-2019; generalization to other markets, smaller-cap names, or more recent periods is untested.
- The dual-attention models that beat HLOB at longer horizons are less interpretable, so the authors note a trade-off between HLOB's interpretability and the competitors' longer-horizon accuracy.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/lstm-networks|lstm networks]]
- [[entities/antonio-briola|Antonio Briola]]
- [[entities/tomaso-aste|Tomaso Aste]]

## Citation

Antonio Briola, Silvia Bartolucci, Tomaso Aste (2024). HLOB – Information Persistence and Structure in Limit Order Books.

DOI: 10.1016/j.eswa.2024.126078

Text ingested: `markdown_output/briola-2024-hlobinformation-persistence-structure-limit-order-books.md`, converted from `raw/ofi-event-clock/briola-2024-hlobinformation-persistence-structure-limit-order-books.pdf`.

Coverage of this summary: Read the full paper end-to-end (introduction, related work, data, methods, all results subsections and the conclusion); skipped only the reference list.

Known problems with the input: No explicit publication year is printed in the body text of this arXiv-style paper; used the year_hint (2024) from the job file; No venue (journal/conference) is stated anywhere in the text read; left venue empty.
<!-- AUTHORED REGION END -->