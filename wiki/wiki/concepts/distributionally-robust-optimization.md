---
title: Distributionally Robust Optimization
page_id: concepts/distributionally-robust-optimization
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T17:35:34Z'
tags:
- distributionally-robust-optimization
- robustness
- conformal-prediction
- fairness
- distribution-shift
sources:
- sources/yang-2026-multi-distribution-robust-cp
related:
- concepts/worst-case-coverage
- concepts/multi-distribution-robust-cp
- concepts/conformal-prediction
- concepts/max-p-aggregation
- concepts/conditional-validity
mind_map_priority: medium
schema_version: 2
uuid: cd5a10e6-8b88-55d7-a165-57b7ab531308
content_hash: sha256:c68b703f5b06b0b129e6b4f6653a320f6bbe004b4e631ec0bdae6f36501c4ea8
---

<!-- AUTHORED REGION START -->
# Distributionally Robust Optimization

Optimising against the **worst case over a family of distributions** rather than against a single nominal distribution. Instead of minimising expected loss under one assumed P, you minimise the maximum expected loss over a set of candidate distributions.

In this wiki the term appears as the theoretical frame for robust conformal prediction, via [[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin (2026)]].

## The Connection to Coverage

Standard [[concepts/conformal-prediction|conformal prediction]] guarantees coverage **marginally**, under the training mixture. That permits 99% coverage on one subgroup and 50% on another while averaging to 90%.

The distributionally robust objective replaces the average with the minimum. Given K source distributions, require

> min_k P_{P^(k)}(Y ∈ Ĉ(X)) ≥ 1 − α

This is [[concepts/worst-case-coverage|worst-case coverage]], and it is what [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust Conformal Prediction]] targets.

## How It Is Achieved Here

[[sources/yang-2026-multi-distribution-robust-cp|Yang & Jin (2026)]] use [[concepts/max-p-aggregation|max-p aggregation]]: compute a conformal p-value per source, take the maximum, and keep labels whose aggregated p-value exceeds α. The resulting set is the union of the per-source sets. They prove finite-sample uniform validity, and that the scheme is optimal and tight when paired with properly learned conformity scores — the score is learned by dual optimisation, which is where the DRO machinery enters.

## Why It Matters

- **Fairness.** When sources correspond to protected subgroups, marginal coverage can hide systematic under-coverage of one of them.
- **Distribution shift.** Coverage holds whichever source the test point came from, without knowing which.
- **Cost.** Robustness is not free: worst-case guarantees generally produce larger prediction sets than marginal ones.

## Open Questions

- How is the source family chosen in practice? The guarantee is only as meaningful as the set it ranges over.
- How much set-size inflation is incurred relative to marginal conformal prediction on real data?

## See Also

[[concepts/worst-case-coverage|Worst-Case Coverage]] · [[concepts/multi-distribution-robust-cp|Multi-Distribution Robust CP]] · [[concepts/conformal-prediction|Conformal Prediction]] · [[concepts/max-p-aggregation|Max-p Aggregation]] · [[concepts/conditional-validity|Conditional Validity]] · [[concepts/coverage-guarantee|Coverage Guarantee]]

<!-- AUTHORED REGION END -->
