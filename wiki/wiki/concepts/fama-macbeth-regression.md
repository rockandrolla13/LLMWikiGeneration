---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:6f46a58844eaf7096afc494c990eb8b1252ea429c4f0138747c935aa94204204
created: '2026-10-22T21:10:31Z'
page_id: concepts/fama-macbeth-regression
page_type: concept
related:
- concepts/factor-models
- concepts/fama-french-factors
revision_id: 1
schema_version: 2
sources:
- sources/israel-2017-common-factors-corporate-bond-returns
tags: []
title: Fama-MacBeth Regression
updated: '2026-10-22T21:10:31Z'
updated_by: op_0cdb8cc1f169
uuid: 644e978c-b371-5bf5-990c-067f813ac042
---

<!-- AUTHORED REGION START -->
# Fama-MacBeth Regression

## Definition

A two-pass method that runs a cross-sectional regression of returns on lagged characteristics each period, then averages the coefficients over time and tests them with their time-series t-statistics. Israel, Palhares and Richardson use rank-normalised characteristics so each coefficient reads as the next-month return per one standard deviation of rank.

## Sources

- [[sources/israel-2017-common-factors-corporate-bond-returns|Common Factors in Corporate Bond Returns]] (2017)

## Related Concepts

- [[concepts/factor-models|Factor Models]]
- [[concepts/fama-french-factors|Fama-French Factors]]
<!-- AUTHORED REGION END -->