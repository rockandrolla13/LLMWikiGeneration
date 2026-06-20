---
title: Conformal Risk Control
page_id: concepts/conformal-risk-control
page_type: concept
revision_id: 2
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- uncertainty-quantification
- risk-control
- loss-functions
sources:
- sources/bates-2021-rcps
- sources/farinhas-2024-non-exchangeable-crc
related:
- concepts/conformal-prediction
- concepts/coverage-guarantee
- concepts/exchangeability
- concepts/distribution-drift
mind_map_priority: high
schema_version: 2
uuid: ff8fc6ce-5e79-55fe-8b24-72918bab8152
content_hash: sha256:4c3899b275c3574795d05279cff0dd8947f50cffd27c9c668da4c14d2dc9e81b
---

<!-- AUTHORED REGION START -->
# Conformal Risk Control

## Primary Source

Primary source: [[sources/bates-2021-rcps|Bates, Angelopoulos, Lei, Malik & Jordan (2021), "Distribution-Free, Risk-Controlling Prediction Sets"]] (JACM). This paper introduces the risk-controlling prediction set (RCPS) framework — the calibration recipe that selects the threshold λ̂ from monotone calibration losses to bound the test-time expected loss — which is the foundation the CRC procedure formalised below generalises.

**Conformal Risk Control (CRC)** extends [[concepts/conformal-prediction|conformal prediction]] from guaranteeing coverage to controlling the expected value of arbitrary monotone loss functions.

## Motivation

Standard conformal prediction provides coverage guarantees:

P(Y_{n+1} ∈ C(X_{n+1})) ≥ 1 - α

However, for many applications, the relevant error is not miscoverage but a task-specific loss:
- **Multilabel classification**: False negative rate
- **Time series**: λ-insensitive absolute error
- **Question answering**: Best F₁-score

CRC generalizes conformal prediction to control these arbitrary losses.

## Framework

### Setup

Given:
- Calibration data {(Xᵢ, Yᵢ)}ⁿᵢ₌₁ and test point (X_{n+1}, Y_{n+1})
- Prediction sets C_λ(·) parameterized by λ, where larger λ yields larger sets
- Loss function ℓ(C_λ(X), Y) that is **monotonically nonincreasing** in λ

### The CRC Procedure (Angelopoulos et al., 2023)

1. Compute calibration losses: Lᵢ(λ) = ℓ(C_λ(Xᵢ), Yᵢ)

2. Find optimal threshold:

   λ̂ = inf{λ : (1/n)∑ᵢ Lᵢ(λ) ≤ α}

3. Guarantee: Under exchangeability,

   E[L(λ̂; (X_{n+1}, Y_{n+1}))] ≤ α

### Key Requirement: Monotone Loss

The loss must decrease as the prediction set grows:

λ ≤ λ' ⟹ C_λ(·) ⊆ C_{λ'}(·) ⟹ ℓ(C_{λ'}(·), ·) ≤ ℓ(C_λ(·), ·)

## Example Loss Functions

### Miscoverage Loss (Standard CP)

ℓ(C(X), Y) = 1{Y ∉ C(X)}

### False Negative Rate

For multilabel classification with true labels Y ⊆ {1,...,M}:

L(λ) = |Y \ C_λ(X)| / |Y|

### λ-Insensitive Absolute Loss

For regression with interval C_λ(X) = [f(X) - λ, f(X) + λ]:

L(λ) = max(0, |Y - f(X)| - λ)

### Best F₁-Score Loss

For question answering:

L(λ) = 1 - max_{ŷ∈C_λ(X), y∈Y} F₁(ŷ, y)

## Non-Exchangeable Extension

[[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] extended CRC to handle **non-exchangeable data**:

### Weighted CRC

With weights w₁,...,wₙ ∈ [0,1]:

λ̂ = inf{λ : ∑ᵢ w̃ᵢ Lᵢ(λ) ≤ (N_w/(N_w+1))(α - A) + A}

where w̃ᵢ = wᵢ/(N_w + 1) and A is a lower bound on the loss.

### Risk Guarantee

E[L(λ̂; (X_{n+1}, Y_{n+1}))] ≤ α + (B-A) ∑ᵢ w̃ᵢ d_TV(Z, Z^i)

The extra term accounts for non-exchangeability through total variation distance.

## Relationship to Standard CP

When ℓ(C(X), Y) = 1{Y ∉ C(X)} and data is exchangeable, CRC reduces to standard conformal prediction:

P(Y_{n+1} ∈ C_λ̂(X_{n+1})) ≥ 1 - α

## Applications

1. **Medical diagnosis**: Control false negative rate (don't miss diseases)
2. **Autonomous systems**: Bound worst-case prediction error
3. **Information retrieval**: Control F₁-score for answer quality
4. **Energy forecasting**: Minimize prediction interval violations

## Key References

- Angelopoulos et al. (2023) - Original CRC framework
- [[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] - Non-exchangeable extension
- Bates et al. (2021) - Distribution-free risk control

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/exchangeability|Exchangeability]]
- [[concepts/distribution-drift|Distribution Drift]]

<!-- AUTHORED REGION END -->
