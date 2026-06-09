---
title: Full (Transductive) Conformal Prediction
page_id: concepts/full-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
tags: [conformal-prediction, transductive, full-cp]
sources: [sources/angelopoulos-2022-gentle-intro, sources/dieuleveut-zaffran-2025-cp-tutorial]
related: [concepts/conformal-prediction, concepts/split-conformal-prediction, concepts/cross-conformal-prediction, concepts/transductive-learning, concepts/exchangeability]
mind_map_priority: medium
---

# Full (Transductive) Conformal Prediction

**Full conformal prediction** is the original Vovk–Gammerman–Shafer construction: for every candidate label `y ∈ 𝒴`, refit a symmetric algorithm on the augmented dataset `(X_1, Y_1), ..., (X_{n+1}, y)` and include `y` in the prediction set if its [[concepts/nonconformity-score|score]] is below the conformal quantile.

## Recipe

For test point `X_{n+1}`:
1. For each candidate `y ∈ 𝒴`:
   - Train algorithm on `D ∪ {(X_{n+1}, y)}` — `n + 1` points total.
   - Compute score `s_y(X_i, Y_i)` for all training points and `s_y(X_{n+1}, y)`.
   - If the test score is among the `⌈(n+1)(1−α)⌉` smallest, include `y`.
2. Return `Ĉ(X_{n+1}) = {y : included}`.

## Trade-offs

| | Full CP | [[concepts/split-conformal-prediction\|Split CP]] | [[concepts/cross-conformal-prediction\|Jackknife+ / CV+]] |
|---|---|---|---|
| **Data efficiency** | Uses all `n` points | Wastes calibration half | Uses all `n` |
| **Computation** | `\|𝒴\| × refit` | One refit total | `K × refit` (K-fold) |
| **Coverage guarantee** | Finite-sample exact | Finite-sample exact | Approximate (small slack) |
| **Practicality** | Heavy; classification only | Standard default | Reasonable middle ground |

## When To Use

- **Small `n`** where splitting wastes too much data.
- **Discrete `𝒴`** (classification) where iteration over candidates is feasible.
- Theoretical analyses where you want the **strongest** finite-sample guarantees.

For continuous regression, full CP requires special structure (e.g., linear regression has closed-form refits) — otherwise [[concepts/split-conformal-prediction|split CP]] or [[concepts/cross-conformal-prediction|J+/CV+]] is the practical choice.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — chapter on full CP and its relationship to split/CV+.
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — full CP in the "avoid splitting" family.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/split-conformal-prediction]]
- [[concepts/cross-conformal-prediction]]
- [[concepts/transductive-learning]]
