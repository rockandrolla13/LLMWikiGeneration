---
title: Worst-Case Coverage
page_id: concepts/worst-case-coverage
page_type: concept
revision_id: 1
created: 2026-04-26T12:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [conformal-prediction, robustness, coverage-guarantee, fairness]
sources: [sources/yang-2026-multi-distribution-robust-cp]
related: [concepts/multi-distribution-robust-cp, concepts/coverage-guarantee, concepts/conditional-validity, concepts/distributionally-robust-optimization]
mind_map_priority: medium
---

# Worst-Case Coverage

**Worst-case coverage** refers to the minimum coverage probability of a prediction set across a family of distributions or subgroups. It is the key objective in distributionally robust uncertainty quantification.

## Formal Definition

Given prediction set Ĉ(X) and a family of distributions {P^(k)}_{k=1}^K:

> Worst-case coverage = min_k P_{P^(k)}(Y ∈ Ĉ(X))

A prediction set achieves **uniform validity** at level 1-α if:

> min_k P_{P^(k)}(Y ∈ Ĉ(X)) ≥ 1 - α

## Contrast with Marginal Coverage

Standard [[concepts/conformal-prediction|conformal prediction]] guarantees marginal coverage:

> P_{P_train}(Y ∈ Ĉ(X)) ≥ 1 - α

This allows:
- 99% coverage for one subgroup
- 50% coverage for another
- 90% coverage on average

Worst-case coverage prevents such disparities.

## Why Worst-Case Matters

### Fairness
When subgroups represent protected attributes (race, gender, age):
- Marginal coverage may hide discriminatory gaps
- Worst-case coverage ensures equitable reliability

### Safety-Critical Systems
In medical, autonomous vehicle, or financial applications:
- Failures are concentrated in specific scenarios
- Worst-case protection prevents catastrophic errors

### Distribution Shift
When test distribution differs from training:
- Marginal validity under training mixture is insufficient
- Worst-case validity protects against arbitrary shifts within the family

## Achieving Worst-Case Coverage

### Max-p Aggregation
[[concepts/max-p-aggregation|Max-p aggregation]] achieves finite-sample worst-case coverage:
- Compute per-source p-values
- Take maximum
- Invert to get prediction set

### Tightness Property
Optimal methods achieve **exact** worst-case coverage:
- At least one source has coverage = 1-α (not over-conservative)
- Proved for [[concepts/multi-distribution-robust-cp|MDCP]] with optimal scores

## Trade-offs

| Coverage Type | Guarantee | Efficiency | Conservatism |
|--------------|-----------|------------|--------------|
| Marginal | Training mixture | Best | None |
| Per-group | Each group | Good | Per-group |
| **Worst-case** | Min over all | Moderate | Controlled |

Worst-case coverage may require larger prediction sets than marginal methods, but MDCP's score learning minimizes this gap.

## Mathematical Formulation

The optimization problem for worst-case coverage:

**Minimize**: Expected set size E[|Ĉ(X)|]

**Subject to**: min_k P_{P^(k)}(Y ∈ Ĉ(X)) ≥ 1 - α

This is related to [[concepts/distributionally-robust-optimization|distributionally robust optimization]] where the uncertainty set is the family of source distributions.

## Connection to Group Fairness

Worst-case coverage is closely related to **equalized coverage** in algorithmic fairness:
- Ensures no group is systematically underserved
- Can be achieved without observing group membership at test time
- Provides stronger guarantees than post-hoc calibration

## See Also

- [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/max-p-aggregation|Max-p Aggregation]]
- [[concepts/distributionally-robust-optimization|Distributionally Robust Optimization]]
- [[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin (2026)]]
