---
title: AgACI (Aggregated Adaptive Conformal Inference)
page_id: concepts/agaci
page_type: concept
revision_id: 1
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- adaptive-methods
- online-learning
- expert-aggregation
sources:
- sources/zaffran-2022-aci
- sources/stocker-2025-conformal-timeseries-intro
related:
- concepts/adaptive-conformal-inference
- concepts/conformal-prediction
- concepts/conformal-pid-control
mind_map_priority: medium
schema_version: 2
uuid: 0676bff7-dbbb-5f31-b93b-61934bc2598c
content_hash: sha256:fb1a6990f238a4fabf8e7286a85592a64c20614e1d37083c25b70f4f5d0567b4
---

<!-- AUTHORED REGION START -->
# AgACI (Aggregated Adaptive Conformal Inference)

**AgACI** (Zaffran et al., [[sources/zaffran-2022-aci|2022]]) is a parameter-free variant of [[concepts/adaptive-conformal-inference|ACI]] that **eliminates the need to tune the learning rate `γ`** by running multiple ACI instances in parallel and aggregating them via online expert algorithms.

## Motivation

Standard ACI updates the miscoverage level via:

```
α_{t+1} = α_t + γ · (α − err_t)
```

Performance is sensitive to `γ`:
- `γ` too small → slow to react to distribution shift.
- `γ` too large → noisy interval widths, instability.

Tuning `γ` requires either a validation split (wasteful) or prior knowledge of shift dynamics (usually unavailable).

## The Aggregation

AgACI runs `K` ACI instances with different `γ_1, ..., γ_K` in parallel. At each time `t`, it combines their prediction intervals using **online expert aggregation** (e.g., exponentially weighted average over coverage performance) to produce a single aggregated interval.

The aggregation algorithm itself has no hyperparameters that depend on shift dynamics — it adapts based on observed miscoverage of each expert.

## Empirical Behaviour

On French day-ahead electricity price forecasting, AgACI matches the best-tuned ACI without requiring `γ`-selection. Featured prominently in [[sources/dieuleveut-zaffran-2025-cp-tutorial]].

## Position in the Family

In [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al.'s]] taxonomy, AgACI sits in the "**adapt α online**" family along with vanilla [[concepts/adaptive-conformal-inference|ACI]], time-varying-γ ACI, and [[concepts/conformal-pid-control|Conformal PID Control]].

## Sources

- [[sources/zaffran-2022-aci]] — original AgACI proposal.
- [[sources/stocker-2025-conformal-timeseries-intro]] — taxonomy placement.
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — pedagogical presentation.

## Related Concepts

- [[concepts/adaptive-conformal-inference]]
- [[concepts/conformal-pid-control]]
- [[concepts/conformal-prediction]]

<!-- AUTHORED REGION END -->
