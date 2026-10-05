---
abstraction_level: intermediate
concept_type: framework
content_hash: sha256:8e951b86effb51dbc0eb01a3f7554351cf5baaf8be578b19bead0b81053cda13
created: 2026-09-16 00:00:00+00:00
mind_map_priority: high
page_id: concepts/multiple-testing
page_type: concept
related:
- concepts/false-discovery-rate
- concepts/e-value
- concepts/p-value-merging
- concepts/null-hypothesis-significance-testing
revision_id: 2
schema_version: 2
sources:
- sources/wang-2021-fdr-control-evalues
- sources/ignatiadis-2023-evalues-unnormalized-weights
- sources/vovk-2019-confidence-discoveries-evalues
- sources/xu-2021-bandit-multiple-testing
- sources/dickerson-2026-co-pricing-factor-zoo
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
tags:
- multiple-testing
- false-discovery-rate
- e-value
- dependence
title: Multiple Testing
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 0248b831-f205-5bf4-81f2-04d666ca7a19
---

<!-- AUTHORED REGION START -->
# Multiple Testing

## The problem

Test one hypothesis and a 5% error rate is a 5% error rate. Test a thousand and you expect fifty false rejections from noise alone. Multiple testing is the machinery for saying something meaningful about a batch of tests at once.

Two targets dominate: the family-wise error rate, the probability of *any* false rejection, which is strict; and the [[concepts/false-discovery-rate|false discovery rate]], the expected share of rejections that are false, which is the workable choice when screening many candidates.

## What dependence does

Every guarantee is really a statement about dependence between the tests. The classical procedures are indexed by what they assume:

| Assumption | Typical cost |
|---|---|
| Independence | none |
| Positive regression dependence | none for BH |
| Negative dependence | previously unstudied; now a bounded constant ([[sources/chi-2024-multiple-testing-negative-dependence|Chi et al.]]) |
| Arbitrary dependence | a factor $\approx\log K$ for p-values; **nothing** for [[concepts/e-value|e-values]] ([[sources/wang-2021-fdr-control-evalues|e-BH]]) |

In practice the dependence between tests is rarely known, which is the strongest argument for procedures whose validity does not hinge on it.

## Beyond a rejection list

- **Weighting.** [[sources/ignatiadis-2023-evalues-unnormalized-weights|E-values act as unnormalized weights]] on p-values, so side information adds power without a fixed weight budget.
- **Counting true discoveries.** [[sources/vovk-2019-confidence-discoveries-evalues|Discovery matrices]] give confidence bounds on how many of your top $r$ hits are real, rather than an average error rate.
- **Selection and reporting.** [[sources/xu-2024-post-selection-evalue-ci|e-BY]] keeps interval coverage valid after you choose which results to report.
- **Adaptive collection.** [[sources/xu-2021-bandit-multiple-testing|Bandit multiple testing]] keeps FDR control when the sampling rule and stopping time respond to the data.

## Existence

Before constructing a procedure it is worth knowing whether a powerful statistic exists at all. [[sources/zhang-2024-powerful-p-e-composite|Zhang, Ramdas & Wang (2024)]] give a convex-geometry criterion for composite nulls and alternatives, and show that coarsening the filtration can make an untestable hypothesis testable.

## Related Concepts

[[concepts/false-discovery-rate|False Discovery Rate]] · [[concepts/e-value|E-value]] · [[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/null-hypothesis-significance-testing|Null Hypothesis Significance Testing]]

## Sources

- [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|The Corporate Bond Factor Replication Crisis]]
- [[sources/dickerson-2026-co-pricing-factor-zoo|The Co-Pricing Factor Zoo]]
<!-- AUTHORED REGION END -->