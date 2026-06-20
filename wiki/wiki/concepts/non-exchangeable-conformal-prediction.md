---
title: Non-Exchangeable Conformal Prediction (NexCP)
page_id: concepts/non-exchangeable-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- non-exchangeable
- distribution-drift
- weighted-quantiles
- total-variation
sources:
- sources/barber-2023-beyond-exchangeability
- sources/stocker-2025-conformal-timeseries-intro
- sources/farinhas-2024-non-exchangeable-crc
related:
- concepts/conformal-prediction
- concepts/exchangeability
- concepts/weighted-conformal-prediction
- concepts/distribution-drift
- concepts/online-conformal-prediction
mind_map_priority: high
schema_version: 2
uuid: 6fea407c-0e8a-5bdd-aaf4-893f75e95ddd
content_hash: sha256:06a9eadaaff37ec9b2fda2110f66b86f4a9811d3f5ac0dd3d15c14886d2a8045
---

<!-- AUTHORED REGION START -->
# Non-Exchangeable Conformal Prediction (NexCP)

**NexCP** (Barber, Candès, Ramdas, Tibshirani, [[sources/barber-2023-beyond-exchangeability|2023]]) is the family of [[concepts/conformal-prediction|CP]] methods that uses **fixed weights** `w_i ∈ [0, 1]` on training data to handle non-exchangeable settings without requiring knowledge of the shift mechanism.

## How It Differs From WCP

[[concepts/weighted-conformal-prediction|Weighted Conformal Prediction]] (Tibshirani et al. 2019) requires **knowing the likelihood ratio** `w(x) = dP̃_X / dP_X`, and loses validity under exchangeability if weights are misspecified.

**NexCP** uses fixed (data-independent) weights without knowing the shift, and **recovers standard CP coverage exactly when data are exchangeable** regardless of the weight choice. There's no penalty for using NexCP weights on exchangeable data.

## The Coverage-Gap Bound

```
P(miscoverage) ≤ α + Σ_i w_i · d_TV(Z, Z^i) / (1 + Σ_i w_i)
```

where `Z^i` is the data sequence with the test point swapped with training point `i`, and `d_TV` is total variation distance. The bound holds **with no assumption** on the joint distribution of the `n+1` points.

A strictly stronger **residual-level** bound is also available, computing `d_TV` on residual vectors `R(Z)` vs `R(Z^i)` — much tighter in high dimensions.

For independent data, Lemma 1 gives `d_TV(Z, Z^i) ≤ d_TV(Z_i, Z_{n+1})`, connecting the bound to pairwise marginal drift.

## Variants

- **NexCP-split**: split-conformal version.
- **NexCP-full**: full / transductive version.
- **NexCP-jackknife+**: the [[concepts/jackknife-plus|Jackknife+]] version.

A randomisation technique allows the underlying fit `A` to be **non-symmetric** (e.g., recency-weighted models) without breaking the guarantee.

## Practical Weight Choices

- **Exponential decay** in time-series settings: `w_i = ρ^{n−i}` for some `ρ ∈ (0, 1)`. Recency weighting.
- **Linear decay**: `w_i = (n − i + 1)/n` or similar.
- **Hard window**: `w_i = 1{i ≥ n − W}`. Equivalent to a sliding window of the most recent `W` points.

[[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]] benchmark these in the WCP / NexCP family and find exponential and linear self-correct under abrupt mean shift while hard-window fails.

## Sources

- [[sources/barber-2023-beyond-exchangeability]] — original NexCP paper.
- [[sources/stocker-2025-conformal-timeseries-intro]] — places NexCP in the "reweight calibration" family of the four-family taxonomy.
- [[sources/farinhas-2024-non-exchangeable-crc]] — risk-control extension under non-exchangeability.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/weighted-conformal-prediction]]
- [[concepts/exchangeability]]
- [[concepts/distribution-drift]]
- [[concepts/online-conformal-prediction]]

<!-- AUTHORED REGION END -->
