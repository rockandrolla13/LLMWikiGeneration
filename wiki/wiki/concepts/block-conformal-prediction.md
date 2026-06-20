---
title: Block Conformal Prediction (BCP)
page_id: concepts/block-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- block-methods
- weak-dependence
sources:
- sources/stocker-2025-conformal-timeseries-intro
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/exchangeability
- concepts/beta-mixing
mind_map_priority: medium
schema_version: 2
uuid: 4c32e18b-0e98-5755-ac55-bcf71e4a3a73
content_hash: sha256:83819ea0c323b9eb34674662686d2e1349e2451396564aecab374c1d30ea94a4
---

<!-- AUTHORED REGION START -->
# Block Conformal Prediction (BCP)

**Block Conformal Prediction** (Chernozhukov, Wüthrich, Zhu, 2018; Oliveira et al., 2024) handles temporal dependence by performing the conformal construction on **blocks** of consecutive observations rather than on individual points, exploiting the weak dependence between distant blocks.

## Variants

- **Transductive Block CP.** Refits the model on each augmented block, à la full CP.
- **Split Block CP (Block-SCP).** Partitions the calibration set into blocks of size `B`; computes block-level scores (e.g., max residual within block); takes the empirical quantile of block scores.

## Theoretical Motivation

If the time series is [[concepts/beta-mixing|β-mixing]] with rate `β(k)`, blocks of size `B` separated by gaps of size `B` are approximately independent for `B` larger than the mixing horizon. CP applied at block level then enjoys (approximate) [[concepts/exchangeability|exchangeability]] of blocks.

## Empirical Pitfall

[[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. (2025)]] find that **Block-SCP undercovers even on stationary β-mixing data** — a non-obvious failure mode. Possible reasons:
- Block size `B` mis-specified relative to actual mixing rate.
- Within-block aggregation (e.g., max) loses information.
- The block-quantile approximation introduces non-vanishing bias for finite `B`.

This makes BCP **less robust than its theory suggests**; the other families (WCP, ACI, EnbPI) are usually preferred in practice.

## Sources

- [[sources/stocker-2025-conformal-timeseries-intro]] — taxonomy and empirical evaluation.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/exchangeability]]
- [[concepts/beta-mixing]]

<!-- AUTHORED REGION END -->
