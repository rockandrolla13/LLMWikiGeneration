---
title: Learn Then Test
page_id: concepts/learn-then-test
page_type: concept
revision_id: 2
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-risk-control
- multiple-testing
- calibration
- fwer
sources:
- sources/angelopoulos-2021-learn-then-test
- sources/angelopoulos-2022-gentle-intro
related:
- concepts/conformal-risk-control
- concepts/conformal-prediction
mind_map_priority: medium
schema_version: 2
uuid: 5058d85d-1382-557a-b724-92f351bb29da
content_hash: sha256:b57423cbb7f5d5f36d48d820b400e0d45dca4771886c76e6de50caffb9db02a0
---

<!-- AUTHORED REGION START -->
# Learn Then Test

## Primary Source

Primary source: [[sources/angelopoulos-2021-learn-then-test|Angelopoulos, Bates, Candès, Jordan & Lei (2021), "Learn Then Test: Calibrating Predictive Algorithms to Achieve Risk Control"]]. This paper introduces the LTT recipe — converting calibration into a family of per-λ p-values and applying any FWER procedure — which provides finite-sample, distribution-free control of arbitrary (possibly non-monotone) risks and is the construction this page formalises.

**Learn Then Test (LTT)** (Angelopoulos, Bates, Candès, Jordan, Lei, 2021) is a multiple-hypothesis-testing framework for distribution-free control of **arbitrary**, possibly non-monotone risks.

## The Problem

[[concepts/conformal-risk-control|Conformal risk control]] (Bates et al. 2021) handles bounded, **monotone** losses — losses that increase monotonically as a tuning parameter `λ` shrinks the prediction set. Many practical risks are non-monotone:

- **Selective classification.** Risk = error rate on kept predictions; non-monotone in the abstention threshold (raising the threshold abstains on hard cases — usually reduces risk, but can increase it if the threshold also abstains on easy correct cases).
- **F1 score, AUC** — generally non-monotone in any single parameter.

## The Solution

LTT converts calibration into a **family of p-values**, one per candidate `λ`:

```
p_λ = P-value for the null H_λ : R(λ) > α
```

Then applies any familywise-error-rate (FWER) procedure (Bonferroni, fixed-sequence, Holm) to select a safe set `Λ̂` such that:

```
P(any λ ∈ Λ̂ has R(λ) > α) ≤ δ
```

This delivers finite-sample, distribution-free control of arbitrary risk functions at the cost of multiple-testing correction.

## Use Cases

- Selective classification with a guaranteed selective-accuracy bound.
- Hyperparameter tuning under risk constraints.
- Any setting where the risk surface is not amenable to monotone conformal risk control.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — chapter on Learn Then Test.

## Related Concepts

- [[concepts/conformal-risk-control]]
- [[concepts/conformal-prediction]]

<!-- AUTHORED REGION END -->
