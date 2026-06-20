---
title: Conformal PID Control
page_id: concepts/conformal-pid-control
page_type: concept
revision_id: 2
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- time-series
- control-theory
- adaptive-methods
- online-learning
sources:
- sources/angelopoulos-2023-conformal-pid
- sources/stocker-2025-conformal-timeseries-intro
related:
- concepts/adaptive-conformal-inference
- concepts/agaci
- concepts/conformal-prediction
mind_map_priority: medium
schema_version: 2
uuid: cdfd7e20-2b3d-5c6e-a3c5-cc933a13520d
content_hash: sha256:79dd70695a3b852e1be7cfd30df91ffe14f2ffca6a2e6be46c57af3f63c34068
---

<!-- AUTHORED REGION START -->
# Conformal PID Control

## Primary Source

Primary source: [[sources/angelopoulos-2023-conformal-pid|Angelopoulos, Candès & Tibshirani (2023), "Conformal PID Control for Time Series Prediction"]]. This NeurIPS paper recasts the ACI miscoverage-tracking update as a classical PID controller, adding integral and derivative terms to the proportional ACI update — the construction formalised below — to eliminate steady-state error and dampen oscillation under drift.

**Conformal PID Control** (Angelopoulos, Candès, Tibshirani, 2023) extends [[concepts/adaptive-conformal-inference|ACI]] by viewing the miscoverage-tracking problem through **classical control theory**.

## The Idea

Vanilla ACI uses pure proportional feedback:

```
α_{t+1} = α_t + γ · (α − err_t)         (P-controller)
```

PID-Conformal adds integral and derivative terms:

```
α_{t+1} = α_t + K_P · e_t + K_I · Σ e_τ + K_D · (e_t − e_{t-1})
```

where `e_t = α − err_t` is the coverage error.

- **Integral term** drives steady-state error to zero — eliminates persistent over/under-coverage that plagues vanilla ACI under slow drift.
- **Derivative term** adds anticipation — reacts to *rate* of coverage change, useful when shift accelerates.

## Why This Matters

In [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al.'s]] benchmarks, vanilla ACI shows characteristic oscillation around the target after abrupt shifts. PID controllers from classical engineering practice (and online-learning theory) are well-understood tools to dampen this oscillation while retaining responsiveness.

## Position in the Family

In the four-family taxonomy of CP-for-time-series, Conformal PID Control sits in the "**adapt α online**" family along with [[concepts/adaptive-conformal-inference|ACI]] and [[concepts/agaci|AgACI]].

## Sources

- [[sources/stocker-2025-conformal-timeseries-intro]] — reviews PID-Conformal as state-of-the-art adapter.

## Related Concepts

- [[concepts/adaptive-conformal-inference]]
- [[concepts/agaci]]
- [[concepts/conformal-prediction]]

<!-- AUTHORED REGION END -->
