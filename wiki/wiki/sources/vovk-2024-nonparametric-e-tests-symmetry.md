---
title: Nonparametric e-tests of symmetry
page_id: sources/vovk-2024-nonparametric-e-tests-symmetry
page_type: source
source_path: markdown_output/vovk-2024-nonparametric-e-tests-symmetry.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2024
venue: New England Journal of Statistics in Data Science (2024)
tags:
- e-value
- nonparametric-tests
- symmetry
- wilcoxon
- efficiency
sources: []
related:
- concepts/e-value
- concepts/multiple-testing
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: f1a35eb5-b1e8-5a51-b21b-849ccf41e06b
content_hash: sha256:1dda3e64e2df5ecb9ead3cf7ddf41c8a6d2a617f991e9bd156d2127353716cca
---

<!-- AUTHORED REGION START -->
# Nonparametric E-tests of Symmetry

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2024 · **Venue:** New England Journal of Statistics in Data Science

## Summary

E-value versions of the classical nonparametric tests of symmetry about zero — the sign test, the Wilcoxon signed-rank test, and a Fisher-type test — plus an e-value analogue of Pitman efficiency for grading them.

**A scope note:** these are fixed-sample conditional e-variables, computed given the observed magnitudes under the sign-flip distribution. They are not e-processes, and the paper makes no optional-stopping claim for them.

## Construction

All three take the exponential-family form
\[
E_\lambda(z_1,\dots,z_n)=\exp\bigl(\lambda S(z_1,\dots,z_n)-C\bigr),
\]
where $S$ is a statistic and $C$ is chosen so the e-variable integrates to exactly 1 under the sign-flip model, which makes it admissible. Three choices of $S$: the sum of the observations (Fisher-type), the number of positive observations (sign test), and the sum of ranks of the positive observations (Wilcoxon). The nuisance parameter $\lambda$ is removed by mixing over a prior, the classical mixture-martingale device.

## Efficiency

The e-version of Pitman asymptotic relative efficiency reproduces the classical values exactly:

| Test | Efficiency |
|---|---|
| Fisher-type | 1 |
| Wilcoxon signed-rank | $3/\pi\approx0.955$ |
| Sign test | $2/\pi\approx0.64$ |

In the paper's phrasing, the sign test "wastes every third observation" while Wilcoxon wastes about one in 22.

## Worked example

On Darwin's maize data, 15 paired differences: Fisher's one-sided p-value is 2.634% and the two-sided 5.267%. The Fisher-type e-test gives 7.651 at a fixed $\lambda=0.5$, and 5.149 after averaging over $\lambda\in[0,1]$; the two-sided version gives 2.633, which falls below the $\sqrt{10}$ threshold. The sign test's one-sided p-value is 0.00369, and its e-values are 19.310 and 38.544 depending on the mixing range.

## Why It Matters

It shows the e-value framework reproduces the classical nonparametric toolkit rather than replacing it, and gives a common currency — expected log value, equal to a Kullback–Leibler divergence at the optimum — for comparing tests.

## See Also

[[concepts/e-value|E-value]] · [[concepts/multiple-testing|Multiple Testing]]
<!-- AUTHORED REGION END -->
