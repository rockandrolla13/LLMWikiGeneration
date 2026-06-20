---
title: Risk-Controlling Prediction Sets (RCPS)
page_id: concepts/risk-controlling-prediction-sets
page_type: concept
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- risk-control
- distribution-free
- pac
- tolerance-regions
sources:
- sources/bates-2021-rcps
- sources/angelopoulos-2021-learn-then-test
- sources/angelopoulos-2022-gentle-intro
related:
- concepts/conformal-risk-control
- concepts/learn-then-test
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/marginal-coverage
- concepts/coverage-guarantee
mind_map_priority: medium
schema_version: 2
uuid: 0c57bc2a-8730-5607-92f0-07b537a8cdbc
content_hash: sha256:e13149e4b2a906da8ac826c2738eb720b5ede11cbcb397f185015a3315b490e7
---

<!-- AUTHORED REGION START -->
# Risk-Controlling Prediction Sets (RCPS)

**RCPS** (Bates, Angelopoulos, Lei, Malik, Jordan, [[sources/bates-2021-rcps|2021]]) is the PAC-style distribution-free framework for controlling **expected loss** (not just miscoverage) of set-valued predictors.

## The Guarantee

A random set predictor `T` is an **(α, δ)-RCPS** if:

```
P(R(T) ≤ α) ≥ 1 − δ
```

where `R(T) = E[L(Y, T(X))]` for any bounded-from-below **monotone** loss `L` on prediction sets. The probability is over the i.i.d. calibration set.

This is **PAC-style**: with high probability `(1 − δ)`, the test-time risk is at most `α`. Contrast with [[concepts/conformal-risk-control|Conformal Risk Control]] (CRC) which gives a marginal expected-risk guarantee `E[R(T)] ≤ α` over both calibration and test randomness.

## How It Works: UCB Calibration

Given a nested family `{T_λ}` and a monotone loss:

1. Compute a pointwise `(1 − δ)` upper confidence bound `R̂^+(λ)` for the risk at each `λ`.
2. Choose `λ̂ = inf{λ : R̂^+(λ') ≤ α for all λ' ≥ λ}`.
3. Return `T_{λ̂}`.

Theorem 1 of [[sources/bates-2021-rcps|Bates et al. 2021]] proves this yields an (α, δ)-RCPS. Monotonicity of `R(λ)` turns a pointwise concentration result into a uniform high-probability guarantee.

## Concentration Bounds

- **Hoeffding**: closed-form, looser.
- **Bentkus**: binomial-worst-case, tighter for proportions.
- **Hoeffding-Bentkus hybrid (HB)**: closed-form, near-tight.
- **Waudby-Smith-Ramdas betting bound**: variance-adaptive, recommended default.
- **CLT-based**: for unbounded losses, asymptotic.

## Why It Matters

RCPS is the **distribution-free analogue of tolerance regions** generalised from coverage to arbitrary monotone losses. The framework decouples model fitting (possibly on a shifted distribution) from calibration (which must use exchangeable data). It strictly generalises split conformal: `L(y, S) = 1{y ∉ S}` recovers tolerance-region coverage.

## RCPS vs CRC vs LTT

- **RCPS** (Bates et al. 2021): (α, δ) PAC guarantee; monotone losses only.
- **[[concepts/conformal-risk-control|CRC]]** (Angelopoulos et al. 2024): `E[R(T)] ≤ α` marginal expected-risk; monotone losses only.
- **[[concepts/learn-then-test|LTT]]** (Angelopoulos et al. 2021): generalises RCPS to **arbitrary** (possibly non-monotone, multi-dimensional) losses via FWER control.

## Sources

- [[sources/bates-2021-rcps]] — primary source for RCPS.
- [[sources/angelopoulos-2021-learn-then-test]] — Learn Then Test generalises beyond monotonicity.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner exposition.

## Related Concepts

- [[concepts/conformal-risk-control]]
- [[concepts/learn-then-test]]
- [[concepts/conformal-prediction]]
- [[concepts/coverage-guarantee]]

<!-- AUTHORED REGION END -->
