---
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: high
page_id: analyses/testing-unconfoundedness-vs-g-methods-identifiability
page_type: analysis
query: How does Cai (2023)'s test of the conditional-independence/unconfoundedness
  assumption relate to the g-methods identifiability conditions, and where do BART,
  OSRCT, and interrupted time series fit?
related:
- concepts/back-door-front-door-adjustment
- concepts/bayesian-additive-regression-trees
- concepts/beta-mixing
- concepts/causal-identifiability-conditions
- concepts/causal-inference
- concepts/conditional-independence-test
- concepts/confounding
- concepts/difference-in-differences
- concepts/do-operator
- concepts/doubly-robust-estimation
- concepts/g-methods-time-varying-treatments
- concepts/heterogeneous-treatment-effects
- concepts/instrumental-variables
- concepts/interrupted-time-series-design
- concepts/inverse-probability-weighting
- concepts/ip-weighting-marginal-structural-models
- concepts/nonparametric-conditional-moment-test
- concepts/observational-sampling-from-rcts
- concepts/potential-outcomes
- concepts/propensity-score
- concepts/regression-discontinuity
- concepts/unconfoundedness-assumption
- sources/angrist-2009-mostly-harmless-econometrics
- sources/cai-2023-testing-conditional-independence-time-series
- sources/gentzel-2021-osrct-evaluation
- sources/hernan-2020-causal-inference-what-if
- sources/hill-2011-bart-causal-inference
- sources/hudson-2019-its-healthcare-reporting
- sources/pearl-2018-book-of-why
revision_hash: sha256:b4cf2cae23c68f3aba46888035d7ee01442afe355bc97dac4157bce555d18f2c
revision_id: 1
sources:
- sources/cai-2023-testing-conditional-independence-time-series
- sources/gentzel-2021-osrct-evaluation
- sources/hill-2011-bart-causal-inference
- sources/hudson-2019-its-healthcare-reporting
- sources/hernan-2020-causal-inference-what-if
- sources/pearl-2018-book-of-why
- sources/angrist-2009-mostly-harmless-econometrics
tags:
- causal-inference
- unconfoundedness
- conditional-independence-test
- identifiability
- time-series
- credit-macro
title: Testing Unconfoundedness vs the g-Methods Identifiability Conditions
updated: '2026-06-09T12:00:00Z'
updated_by: op_b20381baef1d
---

# Testing Unconfoundedness vs the g-Methods Identifiability Conditions

**Query:** How does Cai et al. (2023)'s test of the conditional-independence / unconfoundedness assumption relate to the g-methods identifiability conditions, and where do BART, OSRCT, and interrupted time series fit?

> **Caveat:** the four causality-testing papers are grounded sources; the *lifecycle framing* that organises them below is a synthesis, not a claim from any one paper.

## The assumption, and why it is normally untestable

[[concepts/causal-inference|Causal inference]] from observational data rests on the [[concepts/causal-identifiability-conditions|three identifiability conditions]] ([[sources/hernan-2020-causal-inference-what-if|Hernan & Robins]]): **exchangeability** (no unmeasured [[concepts/confounding|confounding]]), **positivity**, and **consistency**. In a time-series policy-evaluation setting this becomes a **conditional-independence (CI) / [[concepts/unconfoundedness-assumption|unconfoundedness]]** statement — the current policy choice is independent of [[concepts/potential-outcomes|potential outcomes]] given predetermined controls (including lagged outcomes and past policy), which is exactly what licenses the [[concepts/g-methods-time-varying-treatments|g-methods]] / [[concepts/ip-weighting-marginal-structural-models|IPW marginal structural models]] for dynamic treatment effects.

Pearl and Hernan are emphatic that exchangeability is **not testable from data alone** — it is an assumption about the *absence* of something unobserved (the [[concepts/do-operator|do]]-vs-see gap; the open back-door path through an unmeasured common cause). This is the same confounding problem the credit-spread analysis hit ([[analyses/credit-spread-determinants-causal-reading|see that note]]).

## Four papers, four stages of the assumption's lifecycle

**1. TEST it — [[sources/cai-2023-testing-conditional-independence-time-series|Cai et al. (2023)]].** The headline contribution: it makes the CI assumption *partially testable*. The trick is to convert CI into a **nonparametric conditional moment restriction** using **auxiliary variables** that may affect policy but whose link to it should be fully captured by potential outcomes and controls — structurally the **same role an [[concepts/instrumental-variables|instrument]] plays in linear regression**. Two kernel statistics (full-covariate `U_N`; propensity-score-conditioned `V_N` to beat the curse of dimensionality) are asymptotically normal under [[concepts/beta-mixing|beta-mixing]]. Applied to Angrist-Kuersteiner (2011) monetary-policy data, the test *fails to reject* CI (p 0.62-0.91).
   - **Key subtlety:** this does **not** overturn the untestability result. Cai trades the untestable exchangeability assumption for a different *assumed* exclusion restriction on the auxiliary variables, then tests an *implication* of it. It is a conditional, IV-flavoured test — strongest when a credible auxiliary/instrument exists.

**2. ESTIMATE under it — [[sources/hill-2011-bart-causal-inference|Hill (2011), BART]].** Given strong ignorability (unconfoundedness + overlap), flexibly model **only the response surface** `E[Y|Z,X]` with [[concepts/bayesian-additive-regression-trees|Bayesian Additive Regression Trees]] rather than fitting a [[concepts/propensity-score|propensity-score]] model. BART captures [[concepts/heterogeneous-treatment-effects|heterogeneous effects]] and widens its intervals where overlap is poor — a Bayesian complement to [[concepts/inverse-probability-weighting|IPW]] and [[concepts/doubly-robust-estimation|doubly-robust]] estimation.

**3. EVALUATE the estimators — [[sources/gentzel-2021-osrct-evaluation|Gentzel et al. (2021), OSRCT]].** Because the true effect is unknown in real observational data, OSRCT sub-samples an RCT with biasing covariates to *construct* a confounded dataset whose true ATE is still recoverable — a benchmark for methods including BART and doubly-robust estimation ([[concepts/observational-sampling-from-rcts|OSRCT]]). This closes the loop: it lets you check whether estimators recover the effect when unconfoundedness is *deliberately* broken.

**4. SUBSTITUTE for it when it fails — [[sources/hudson-2019-its-healthcare-reporting|Hudson et al. (2019), ITS]].** When no control set makes treatment unconfounded, the [[concepts/interrupted-time-series-design|interrupted time series]] design exploits a *temporal* discontinuity at the intervention instead — a quasi-experimental cousin of [[concepts/regression-discontinuity|regression discontinuity]] and [[concepts/difference-in-differences|difference-in-differences]]. (The paper is a reporting-quality review: segmented regression dominates but autocorrelation/nonstationarity are widely ignored — a methodological caution.)

## Synthesis

The g-methods give the *identification theory* (assume CI, then IPW/g-formula identify dynamic effects). The four papers populate the *practical lifecycle around that assumption*: Cai tests it (via an IV-like auxiliary restriction), Hill estimates flexibly under it, Gentzel evaluates whether estimators work when it is violated, and Hudson shows the design fallback when it is unavailable. The recurring lesson — consistent with [[sources/pearl-2018-book-of-why|Pearl]] and [[sources/angrist-2009-mostly-harmless-econometrics|Angrist-Pischke]] — is that you cannot get unconfoundedness for free: you either assume it, import an instrument/auxiliary to test an implication of it, or exploit a design (RD/ITS/DiD) that manufactures as-good-as-random variation.

## Open questions

- Does Cai's auxiliary-variable test reduce to a conditional moment version of an [[concepts/instrumental-variables|IV]] over-identification test?
- Could OSRCT-style constructed benchmarks be built from financial event studies to validate credit causal estimators?
- For credit/macro policy evaluation, when is ITS/RD (temporal discontinuity) more credible than conditioning-based unconfoundedness?