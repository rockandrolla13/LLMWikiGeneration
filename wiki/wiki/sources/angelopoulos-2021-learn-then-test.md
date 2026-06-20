---
title: 'Learn Then Test: Calibrating Predictive Algorithms to Achieve Risk Control'
page_id: sources/angelopoulos-2021-learn-then-test
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Anastasios N. Angelopoulos
- Stephen Bates
- Emmanuel J. Candès
- Michael I. Jordan
- Lihua Lei
year: 2021
venue: arXiv:2110.01052
tags:
- conformal-prediction
- risk-control
- multiple-hypothesis-testing
- fwer
- calibration
- distribution-free
- fdr-control
- selective-classification
related:
- concepts/learn-then-test
- concepts/conformal-risk-control
- concepts/risk-controlling-prediction-sets
- concepts/conformal-prediction
- entities/anastasios-angelopoulos
- entities/stephen-bates
- entities/emmanuel-candes
- entities/michael-i-jordan
- entities/lihua-lei
- sources/bates-2021-rcps
- sources/angelopoulos-2021-raps
- sources/angelopoulos-2022-gentle-intro
- sources/farinhas-2024-non-exchangeable-crc
mind_map_priority: high
schema_version: 2
uuid: cc98e547-9e13-579c-9cb6-ad2cf93ce060
content_hash: sha256:316ef1d85b4f1acf956f89019d5316c89f287b5a2c45840db63dcb478f48e283
---

<!-- AUTHORED REGION START -->
# Learn Then Test (LTT)

**Authors:** [[entities/anastasios-angelopoulos|Anastasios N. Angelopoulos]], [[entities/stephen-bates|Stephen Bates]], [[entities/emmanuel-candes|Emmanuel J. Candès]], [[entities/michael-i-jordan|Michael I. Jordan]], [[entities/lihua-lei|Lihua Lei]]

**Year:** 2021

**Venue:** arXiv:2110.01052. Code: `github.com/aangelopoulos/ltt`.

## Summary

**Primary source** for the wiki concept [[concepts/learn-then-test|Learn Then Test]]. Reframes the problem of calibrating a pretrained ML model to satisfy a user-specified risk bound as a **multiple hypothesis testing problem**, generalising [[sources/bates-2021-rcps|RCPS]] beyond monotone risks to arbitrary (possibly non-monotone, multi-dimensional) losses.

For a low-dimensional post-processing parameter `λ` indexing predictions `T_λ`, each candidate `λ_j` is assigned a null hypothesis `H_j : R(λ_j) > α`. A finite-sample valid p-value is computed via concentration inequalities (e.g., Hoeffding-Bentkus) on the empirical risk over the calibration set. A family-wise error rate (FWER)-controlling procedure (Bonferroni, fixed sequence testing, or sequential graphical testing) returns a set of admissible `λ` values. Any `λ` chosen from this set yields an (α, δ)-risk-controlling prediction.

## Why It Matters

The key step is **dropping monotonicity**. [[concepts/conformal-risk-control|Conformal risk control]] (RCPS / Angelopoulos et al. 2024) handles bounded monotone losses; LTT extends to arbitrary risks via multiple-testing machinery. This enables risk-controlled deployment of selective classification, F1, AUC, FDR, and other risks that aren't monotone in any single parameter.

## Key Contributions

1. **Risk control as multiple hypothesis testing.** Reduces arbitrary (non-monotone, multi-dimensional) risk control to FWER control over a discretised parameter grid.
2. **Theorem 1 (LTT validity).** Given finite-sample valid p-values and any FWER-controlling algorithm at level `δ`, every `λ` in the returned rejection set is an (α, δ)-risk-controlling prediction.
3. **Hoeffding-Bentkus hybrid p-values.** Tight finite-sample p-values for bounded losses; CLT-based p-values cover the unbounded case asymptotically.
4. **FWER procedure catalogue.** Fixed sequence testing exhausts the full `δ` budget asymptotically; Bonferroni is conservative; sequential graphical testing generalises both with structural priors.
5. **Multi-risk and multi-dimensional `λ` (Proposition 6).** Handled by taking `p_j = max_l p_{j,l}` and applying the same FWER framework.

## Empirical Demonstrations

- FDR-controlled multi-label classification.
- Selective classification and regression.
- OOD detection.
- Instance segmentation with simultaneous IoU / recall / coverage guarantees.

## Relation to Other Wiki Sources

- [[sources/bates-2021-rcps]] — RCPS is the monotone-loss precursor that LTT generalises.
- [[sources/angelopoulos-2021-raps]] — companion paper from the same Berkeley group.
- [[sources/farinhas-2024-non-exchangeable-crc]] — risk-control extension under non-exchangeable data.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner exposition.

## Questions Raised

- How should the parameter grid `Λ` be discretised in high dimensions without sacrificing statistical efficiency?
- How is the fixed-sequence ordering or graph structure for SGT chosen in a data-driven yet valid way when no natural ordering exists?
- How does LTT degrade under distribution shift or non-exchangeable calibration data?
- What is the right way to extend LTT to online or sequential decision-making settings?

## See Also

- [[concepts/learn-then-test]]
- [[concepts/conformal-risk-control]]
- [[concepts/risk-controlling-prediction-sets]]
- [[entities/lihua-lei]]

<!-- AUTHORED REGION END -->
