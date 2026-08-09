---
title: Instrumented Principal Component Analysis
page_id: sources/kelly-2026-ipca
page_type: source
source_type: working-paper
revision_id: 1
source_path: markdown_output/kelly-2026-ipca.md
created: 2026-08-07 00:00:00+00:00
updated: '2026-08-07T11:38:46Z'
authors:
- Bryan Kelly
- Sofonias A. Korsaye
- Seth Pruitt
- Yinan Su
year: 2026
venue: Working paper (SSRN 2983919), April 2026
tags:
- ipca
- latent-factors
- factor-loadings
- panel-data
- asset-pricing
sources: []
related:
- concepts/factor-models
- concepts/principal-components-analysis
mind_map_priority: high
schema_version: 2
uuid: bdeb0554-4324-58b2-ba5f-f3a87832f779
content_hash: sha256:cb35dfe444283200318aa1dc3b5d8303d6c18d3cf4690a4fbe6f5c4437a9cab8
---

<!-- AUTHORED REGION START -->
# Instrumented Principal Component Analysis

**Authors:** Bryan Kelly (Yale, AQR, NBER), Sofonias A. Korsaye (Johns Hopkins), Seth Pruitt (Arizona State), Yinan Su (Johns Hopkins)

**Version here:** working paper, April 2026

> **Naming note.** Pages in this wiki previously linked to `kelly-2023-ipca`, described as
> "IPCA factors". That link came from the bibliography of [[sources/feng-2025-predicting-bond-returns|Feng et al. (2025)]],
> which cites Kelly, Palhares & Pruitt (2023), *Modeling Corporate Bond Returns*,
> J. Finance 78, 1967–2008 — a different paper. This page is the IPCA **method**
> paper. The bond paper is still not in this wiki.

## What IPCA Is

A latent factor method that, alongside the main panel of interest, brings in additional information as **instruments**.

The move: instead of estimating a static loading for each individual, it estimates a **structural link between time-varying instruments and dynamic factor loadings**. The loadings are then a function of observable characteristics rather than free parameters per unit.

## Why That Helps

- It improves factor model estimation especially where **loadings are dynamic and cross-sections are large** — precisely the setting where per-individual static loadings are worst.
- It makes the economic relationships between factors and individuals interpretable, because they run through observable instruments.
- It is fast to compute and handles **unbalanced panels**, which matters for real asset data where coverage starts and stops.

The paper establishes **consistency and asymptotic normality under general conditions**, and demonstrates the method on simulated data and in applications to equity asset pricing and international macroeconomics.

## Why It Is Worth Having Here

Several pages in this wiki concern factor estimation from high-frequency or large panels — see [[sources/aitsahalia-2017-pca-hf-factor-model|PCA for high-dimensional factor models]] and [[sources/pelger-2019-large-dimensional-hf-factor-model|Pelger]]. IPCA is the alternative that refuses to treat loadings as static, which is the assumption those methods lean on hardest.

## Open Questions

- The applications shown are equities and macro. How does IPCA behave on corporate bonds, where panels are more unbalanced still?
- Instruments must be chosen. How sensitive are the factors to that choice?

## See Also

[[concepts/factor-models|Factor Models]] · [[concepts/principal-components-analysis|Principal Components Analysis]] · [[sources/aitsahalia-2017-pca-hf-factor-model|PCA for High-Dimensional Factor Models]] · [[sources/pelger-2019-large-dimensional-hf-factor-model|Pelger (2019)]] · [[sources/aleti-2022-high-frequency-factor-zoo|Aleti, High-Frequency Factor Zoo]]

**Not yet written:** `concepts/latent-factors`, `concepts/instrumented-pca`
<!-- AUTHORED REGION END -->

