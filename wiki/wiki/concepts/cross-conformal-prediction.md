---
title: Cross-Conformal Prediction / Jackknife+ / CV+
page_id: concepts/cross-conformal-prediction
page_type: concept
revision_id: 2
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- cross-validation
- jackknife
- ensemble
sources:
- sources/vovk-2012-cross-conformal
- sources/angelopoulos-2022-gentle-intro
- sources/dieuleveut-zaffran-2025-cp-tutorial
- sources/fontana-2023-cp-unified-review
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/full-conformal-prediction
- concepts/jackknife-plus
- concepts/jackknife-plus-after-bootstrap
- concepts/enbpi
mind_map_priority: medium
schema_version: 2
uuid: ecc17433-2996-5725-98d0-82e4203e5ff7
content_hash: sha256:855345b25312798d6954f3624762e9917ce781219e10b73844ef77b0654552d6
---

<!-- AUTHORED REGION START -->
# Cross-Conformal Prediction / Jackknife+ / CV+

A family of computational compromises between [[concepts/split-conformal-prediction|split]] and [[concepts/full-conformal-prediction|full]] CP, using K-fold or leave-one-out refits to use all data for both fitting and calibration with a small number of model fits and **approximate** coverage guarantees.

## The Family

| Method | # Refits | Notes |
|---|---|---|
| **Jackknife** | `n` (leave-one-out) | Pre-CP; uses LOO residuals naively. |
| **Jackknife+** (Barber–Candès–Ramdas–Tibshirani 2021) | `n` | Adds `±` term to interval construction; gives finite-sample 1 − 2α coverage. |
| **CV+** | `K` (K-fold) | K-fold analogue of Jackknife+. |
| **Cross-conformal prediction** (Vovk 2015) | `K` | Pools scores across folds. |
| **[[concepts/jackknife-plus-after-bootstrap\|Jackknife+ after Bootstrap]]** | 1 ensemble fit | Recovers Jackknife+ guarantees from a single bootstrap ensemble — see [[concepts/enbpi\|EnbPI]]. |

## Coverage Guarantees

- Jackknife+ / CV+ achieve **1 − 2α** marginal coverage in finite samples (off by a factor of 2 from split CP's 1 − α).
- In practice, the actual coverage is typically much closer to 1 − α — the 2α bound is loose.
- The looser theoretical guarantee buys back the data lost to splitting.

## When To Use

- **Small `n`** where split CP wastes too much data.
- **Expensive base models** where full CP's `|𝒴| × refit` cost is prohibitive but `n` refits are tolerable.
- **Time-series** where the bootstrap-LOO trick is exploited by [[concepts/enbpi|EnbPI]].

## Sources

- [[sources/vovk-2012-cross-conformal]] — **primary source** for cross-conformal prediction. Establishes the K-fold construction and the empirical case for averaging (rather than Fisher-combining) per-fold p-values.
- [[sources/angelopoulos-2022-gentle-intro]] — family overview, 1 − 2α theorems for Jackknife+ / CV+ (Barber et al. 2021).
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — placement in the "avoid splitting" family.
- [[sources/fontana-2023-cp-unified-review]] — theoretical context within the broader CP literature.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/full-conformal-prediction]]
- [[concepts/jackknife-plus-after-bootstrap]]
- [[concepts/enbpi]]

<!-- AUTHORED REGION END -->
