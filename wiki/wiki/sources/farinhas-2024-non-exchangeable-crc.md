---
title: "Non-Exchangeable Conformal Risk Control"
page_id: sources/farinhas-2024-non-exchangeable-crc
page_type: source
revision_id: 1
created: 2026-04-26T12:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [conformal-prediction, risk-control, non-exchangeable-data, distribution-drift, time-series]
authors: [Antonio Farinhas, Chrysoula Zerva, Dennis Ulmer, Andre F.T. Martins]
venue: ICLR 2024
year: 2024
sources: []
related: [concepts/conformal-prediction, concepts/conformal-risk-control, concepts/exchangeability, concepts/coverage-guarantee, concepts/distribution-drift]
mind_map_priority: high
---

# Non-Exchangeable Conformal Risk Control

**Farinhas, A., Zerva, C., Ulmer, D., & Martins, A.F.T. (2024).** Non-Exchangeable Conformal Risk Control. *ICLR 2024*.

## Summary

This paper extends [[concepts/conformal-risk-control|conformal risk control (CRC)]] to handle **non-exchangeable data**, a common challenge in real-world applications where the standard exchangeability assumption is violated (e.g., time series with distribution drift, spatial data with correlations).

The key contribution is **non-exchangeable CRC (non-X CRC)**, which provides guarantees on controlling the expected value of any monotone loss function when the data distribution changes over time.

## Key Contributions

1. **Unified Framework**: Combines two prior lines of work:
   - Non-exchangeable conformal prediction (Barber et al., 2023)
   - Conformal risk control (Angelopoulos et al., 2023)

2. **Theorem 1 (Main Result)**: For bounded, monotonically nonincreasing loss functions L(λ; (x,y)) ∈ [A,B], choosing weights w₁,...,wₙ ∈ [0,1] gives:

   E[L(λ̂; (Xₙ₊₁, Yₙ₊₁))] ≤ α + (B-A) ∑ᵢ w̃ᵢ dTV(Z, Z^i)

   where dTV is the total variation distance and w̃ᵢ are normalized weights.

3. **Weight Selection Strategy**: Maximum entropy principle suggests exponentially decaying weights w̃ᵢ ∝ exp(-β(B-A)dTV(Z, Z^i)) for time series with bounded distribution drift.

## Methodology

### Standard Conformal Risk Control (Background)

Given calibration data {(Xᵢ, Yᵢ)}ⁿᵢ₌₁ and prediction sets Cλ(·) that grow with λ:

- Compute calibration losses Lᵢ(λ) = ℓ(Cλ(Xᵢ), Yᵢ)
- Find λ̂ such that the empirical risk is at most α
- Under exchangeability: E[L(λ̂; (Xₙ₊₁, Yₙ₊₁))] ≤ α

### Non-Exchangeable Extension

The paper modifies the threshold selection to use **weighted empirical risk**:

R̂ₙ(λ) = ∑ᵢ w̃ᵢ Lᵢ(λ)

The optimal λ̂ is chosen such that R̂ₙ(λ̂) ≤ (Nw/(Nw+1)) × (α - A) + A

where Nw = ∑wᵢ.

### Key Insight

When data is exchangeable, dTV(Z, Z^i) = 0 for all i, recovering standard CRC guarantees. By choosing large weights for calibration points with low TV distance to the test point, tighter bounds are achieved.

## Experiments

### 1. Multilabel Classification with Synthetic Time Series

- **False Negative Rate (FNR)** minimization
- Three settings: i.i.d., changepoints, distribution drift
- Non-X CRC achieves target risk level (0.2) whereas standard CRC fails under non-exchangeability

| Setting | CRC (mean/median) | Non-X CRC (mean/median) |
|---------|-------------------|-------------------------|
| i.i.d.  | 0.191 / 0.183     | **0.181 / 0.175**       |
| Changepoints | 0.246 / 0.228 | **0.196 / 0.183**       |
| Drift   | 0.225 / 0.218     | **0.182 / 0.175**       |

### 2. Electricity Usage Monitoring (ELEC2 Dataset)

- **λ-insensitive absolute loss** control
- Weights: wᵢ = 0.99^(n+1-i) (exponential decay)
- Non-X CRC maintains desired risk level during distribution shift periods

### 3. Open-Domain Question Answering (Natural Questions)

- **Best token-level F₁-score** control
- Data-dependent weights based on embedding similarity
- Smaller prediction sets (23.0 vs 24.6) while maintaining same risk level

## Theoretical Foundation

**Lemma 1** (TV Bound Extension): For bounded f: S → [A,B]:

|E_P[f] - E_Q[f]| ≤ (B-A) × dTV(P,Q)

This extends Barber et al.'s result for indicator functions to arbitrary bounded functions.

## Practical Implications

- **Time Series**: Use exponentially decaying weights for recent observations
- **Spatial Data**: Weight by geographic proximity
- **Covariate Shift**: Weight by feature similarity to test point
- **Change Point Detection**: Automatic adaptation after distribution changes

## Code Availability

https://github.com/deep-spin/non-exchangeable-crc

## Key Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/conformal-risk-control|Conformal Risk Control]]
- [[concepts/exchangeability|Exchangeability]]
- [[concepts/distribution-drift|Distribution Drift]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/total-variation-distance|Total Variation Distance]]

## Related Entities

- [[entities/antonio-farinhas|Antonio Farinhas]] (Instituto Superior Técnico, Lisbon)
- [[entities/chrysoula-zerva|Chrysoula Zerva]] (Instituto Superior Técnico, Lisbon)
- [[entities/dennis-ulmer|Dennis Ulmer]] (IT University of Copenhagen)
- [[entities/andre-martins|André F.T. Martins]] (Unbabel, Instituto Superior Técnico)

## Related Papers

- [[sources/zaffran-2022-aci|Zaffran et al. (2022)]] - Adaptive Conformal Inference for Time Series
- Barber et al. (2023) - Conformal Prediction Beyond Exchangeability
- Angelopoulos et al. (2023) - Conformal Risk Control

## See Also

- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]] - Another approach to non-exchangeable data
- [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] - Conformal prediction with missing values
