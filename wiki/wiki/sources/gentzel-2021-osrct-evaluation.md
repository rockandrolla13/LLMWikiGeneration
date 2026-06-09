---
authors:
- Amanda Gentzel
- Purva Pruthi
- David Jensen
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/gentzel-2021-osrct-evaluation
page_type: source
publication_date: '2021'
publication_venue: Proceedings of the 38th International Conference on Machine Learning
  (ICML), PMLR 139
related:
- concepts/average-treatment-effect
- concepts/confounding
- concepts/doubly-robust-estimation
- concepts/empirical-evaluation-causal-inference
- concepts/ip-weighting-marginal-structural-models
- concepts/observational-sampling-from-rcts
- concepts/potential-outcomes
- entities/amanda-gentzel
- entities/david-jensen
- entities/donald-rubin
- entities/jennifer-hill
- entities/judea-pearl
- entities/purva-pruthi
- entities/stefan-wager
- entities/susan-athey
revision_hash: sha256:5f7cb8349d6e8468ecde4605fa3143425c81919b7cc02581450e7ea06f3ede8b
revision_id: 1
source_hash: sha256:b7a009354b909cd222cda85d49f4a7b4282eefa9bfd2ddb764fa57c7d1527003
source_path: raw/causality-testing/2010.03051v2.pdf
source_type: paper
sources: []
tags: []
title: How and Why to Use Experimental Data to Evaluate Methods for Observational
  Causal Inference
updated: '2026-06-09T12:00:00Z'
updated_by: op_117a674dc12f
---

# How and Why to Use Experimental Data to Evaluate Methods for Observational Causal Inference

**Authors:** Amanda Gentzel, Purva Pruthi, David Jensen · **Year:** 2021 · **Venue:** Proceedings of the 38th International Conference on Machine Learning (ICML), PMLR 139 · **Type:** paper

## Summary

This paper addresses the difficulty of empirically evaluating methods for observational causal inference, which stems from the lack of observational data sets for which the true treatment effect is known. The authors describe and analyze Observational Sampling from Randomized Controlled Trials (OSRCT): a procedure that takes data from an RCT (where treatment is randomly assigned and only one potential outcome is observed per unit) and non-randomly sub-samples it using biasing covariates to induce confounding, producing a constructed observational data set whose true average treatment effect is still recoverable from the original RCT. This lets the field exploit the large and growing supply of publicly available RCT data rather than hand-building specialized evaluation data sets.

The core theoretical contribution is to prove that OSRCT is equivalent, in expectation, to sampling from the potential-outcomes data-generating process (OSAPO) that assumes all potential outcomes are observed. Theorem 1 shows the inclusion probability under OSRCT is exactly half that under OSAPO when treatment and control are equally likely; Theorem 2 shows the constructed sample is, in expectation, half the size of the RCT regardless of biasing strength; and Theorem 3 shows the discarded 'complementary sample' can be reweighted (equivalent to inverse propensity weighting) to serve as a held-out test set for evaluating unit-level outcome-under-intervention estimates.

The authors run a large-scale empirical study applying seven causal inference methods (propensity score matching, IPTW, outcome regression, BART, causal forests, doubly-robust estimation, and a neural-network/Dragonnet method) plus a naive baseline to 37 data sets drawn from RCTs, simulators, real-world computational systems (APO), and observational data augmented with synthetic outcomes (ACIC and IBM benchmarks). They find that RCT, APO, and simulator data yield broadly similar relative performance across methods, whereas synthetic-response data shows markedly more between-method variability, indicating that data source materially affects evaluation conclusions and that synthetic-response benchmarks may be unrealistically complex.

## Key Claims

1. OSRCT can sub-sample data from a randomized controlled trial using biasing covariates to create a constructed observational data set that contains synthetic confounding while retaining a recoverable, unbiased ground-truth treatment effect from the original RCT.
2. Theorem 1: for a binary treatment with P(T=1)=P(T=0)=0.5 in the RCT, the OSRCT inclusion probability equals 0.5 times the OSAPO inclusion probability for every unit and treatment value, so OSRCT data is equivalent to a random sub-sample of OSAPO data.
3. Theorem 2: for binary treatment, the expected size of the OSRCT constructed data set is half the size of the original RCT, independent of the strength of the biasing function.
4. Theorem 3: the discarded 'complementary sample' can be reweighted by the induced selection probabilities (equivalent to inverse propensity score weighting) to approximate the training distribution and serve as a held-out test set for outcome-under-intervention estimation.
5. RCT data cannot identify individual treatment effect (ITE) because only one potential outcome is observed per unit, but it can be used to evaluate estimates of unit-level outcome under intervention E[Y|do(T=t)].
6. Across 37 data sets, performance of RCT, computational APO, and simulator data is broadly similar across the seven methods, while synthetic-response (ACIC/IBM) data produces substantially more between-method variability, suggesting that synthetic-response benchmarks may overstate method differences.
7. Propensity score matching consistently shows the highest variability/error, consistent with prior findings (King & Nielsen) that matching on the propensity score can increase imbalance.
8. OSRCT occupies a favorable position on data availability, internal validity, and external validity simultaneously because only the confounding is synthetic while covariate distributions and outcome functions arise naturally from real RCTs.

## Questions Raised

- Would a more complex biasing function using many covariates make RCT-based evaluation results match the high between-method variability seen on synthetic-response data?
- How representative is method performance on RCT-derived data of performance on the actual observational populations of interest, given that RCTs are conducted in settings where randomization and measurement are feasible?
- How would individual causal inference methods perform under careful hyperparameter tuning rather than default settings, especially the neural-network method that showed high variability at small sample sizes?
- Can OSRCT-style evaluation be extended to induce dependence on outcome (not just treatment) or to estimands beyond the single treatment-outcome pair recoverable from an RCT?

## Concepts

- [[concepts/observational-sampling-from-rcts|Observational sampling from randomized controlled trials (OSRCT)]]
- [[concepts/potential-outcomes|Potential outcomes framework]]
- [[concepts/average-treatment-effect|Average treatment effect (ATE)]]
- [[concepts/confounding|Confounding via biasing covariates]]
- [[concepts/ip-weighting-marginal-structural-models|Inverse probability of treatment weighting (IPTW) / propensity score]]
- [[concepts/doubly-robust-estimation|Doubly-robust estimation]]
- [[concepts/empirical-evaluation-causal-inference|Empirical evaluation of causal inference methods]]

## Entities

- [[entities/amanda-gentzel|Amanda Gentzel]]
- [[entities/purva-pruthi|Purva Pruthi]]
- [[entities/david-jensen|David Jensen]]
- [[entities/donald-rubin|Donald B. Rubin]]
- [[entities/jennifer-hill|Jennifer Hill]]
- [[entities/judea-pearl|Judea Pearl]]
- [[entities/susan-athey|Susan Athey]]
- [[entities/stefan-wager|Stefan Wager]]

## Source

- **Path:** `raw/causality-testing/2010.03051v2.pdf`
- **Type:** paper
- **Hash:** `sha256:b7a009354b909cd22...`