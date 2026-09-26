---
title: Merging P-values and E-values
page_id: concepts/p-value-merging
page_type: concept
concept_type: technique
abstraction_level: intermediate
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- merging
- p-value
- e-value
- admissibility
- arbitrary-dependence
sources:
- sources/vovk-2021-admissible-merging-pvalues
- sources/wang-2025-admissible-merging-evalues
- sources/gasparin-2025-combining-exchangeable-pvalues
- sources/vovk-2024-merging-sequential-evalues
related:
- concepts/e-value
- concepts/exchangeability
- concepts/multiple-testing
mind_map_priority: high
schema_version: 2
uuid: 9e134f5a-6026-562c-95b3-2d2e54f3aab4
content_hash: sha256:535a6530b7afb7d82e9d687248ac3c9aed87a4318a40ae06963c77a25b46c022
---

<!-- AUTHORED REGION START -->
# Merging P-values and E-values

## The question

You have $K$ pieces of evidence about the same hypothesis — several tests, several datasets, several splits. How do you combine them into one valid statistic, without knowing how they depend on each other?

The answer differs sharply between the two currencies, and that difference is the practical case for [[concepts/e-value|e-values]].

## Merging e-values

| Dependence | What is admissible |
|---|---|
| Arbitrary | A weighted average of the e-values and the constant 1 — and *only* that ([[sources/wang-2025-admissible-merging-evalues|Wang, 2025]]) |
| Sequential | Exactly the betting strategies: game martingales ([[sources/vovk-2024-merging-sequential-evalues|Vovk & Wang, 2024]]) |
| Independent | Betting strategies are valid but do not exhaust the admissible rules; symmetric-polynomial constructions sit outside them ([[sources/ming-2026-demi-supermartingales|Ming et al., 2026]]) |

No constants, no corrections. Under arbitrary dependence the question is closed: averaging is the only admissible answer, so there is nothing better to look for.

## Merging p-values

Far messier. Validity under arbitrary dependence requires multiplicative constants — 2 for the arithmetic mean, $e\approx2.718$ for the geometric mean, roughly $\log K$ for the harmonic mean. [[sources/vovk-2021-admissible-merging-pvalues|Vovk, Wang & Wang (2022)]] show the admissible rules are indexed by calibrators, so p-merging is governed by e-value machinery underneath, and the admissible class is a zoo rather than a single answer.

## When you know a little more

[[concepts/exchangeability|Exchangeability]] — the natural condition for repeated sample splitting — is enough to improve on the arbitrary-dependence rules without touching those constants. [[sources/gasparin-2025-combining-exchangeable-pvalues|Gasparin, Wang & Ramdas (2025)]] show the improvement comes from taking a running minimum over prefixes, which requires processing the p-values in order: any symmetric rule valid for exchangeable inputs is automatically valid under arbitrary dependence, so symmetry must be given up to gain anything.

## Practical guidance

- If the inputs are arbitrarily dependent e-values, average them, with weights if you have a reason.
- If they arrive sequentially, bet, and do not automatically stake everything.
- If they come from repeated splits of the same data, they are exchangeable — use the prefix-minimum rules.
- If they are p-values and you can calibrate them into e-values, doing so usually buys more than a cleverer p-merging rule.

## Related Concepts

[[concepts/e-value|E-value]] · [[concepts/exchangeability|Exchangeability]] · [[concepts/multiple-testing|Multiple Testing]]
<!-- AUTHORED REGION END -->
