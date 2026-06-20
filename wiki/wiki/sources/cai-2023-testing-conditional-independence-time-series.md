---
authors:
- Zongwu Cai
- Ying Fang
- Ming Lin
- Shengfang Tang
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/cai-2023-testing-conditional-independence-time-series
page_type: source
publication_date: '2023'
publication_venue: Statistica Neerlandica
related:
- concepts/beta-mixing-processes
- concepts/conditional-independence-test
- concepts/inverse-probability-weighting
- concepts/nonparametric-conditional-moment-test
- concepts/potential-outcomes
- concepts/propensity-score
- concepts/unconfoundedness-assumption
- entities/christina-romer
- entities/christopher-sims
- entities/david-romer
- entities/donald-rubin
- entities/guido-kuersteiner
- entities/joshua-angrist
- entities/ming-lin
- entities/oscar-jorda
- entities/pascal-lavergne
- entities/qi-li
- entities/quang-vuong
- entities/shengfang-tang
- entities/yanqin-fan
- entities/ying-fang
- entities/zongwu-cai
revision_hash: sha256:06ec22bb8dc29c52382fb0f835e12f0f1950d98cbb84f0b38333698d95ebb80f
revision_id: 1
source_hash: sha256:3d07d42abedd8002e795cf719b00e41e963e4b0915c151d003f876622ff41e7c
source_path: raw/causality-testing/Testing_TS.pdf
source_type: paper
sources: []
tags: []
title: Testing Conditional Independence in Causal Inference for Time Series Data
updated: '2026-06-20T01:03:51Z'
updated_by: op_68215fbeeed9
schema_version: 2
uuid: 68b9b547-b689-5ba4-a8e9-c904f6a530c9
content_hash: sha256:70dd6f3e496c41b8483a60d17757d2bcbdf2352a590c75bb080f83968a534368
---

<!-- AUTHORED REGION START -->
# Testing Conditional Independence in Causal Inference for Time Series Data

**Authors:** Zongwu Cai, Ying Fang, Ming Lin, Shengfang Tang · **Year:** 2023 · **Venue:** Statistica Neerlandica · **Type:** paper

## Summary

This paper proposes a new statistical procedure for testing the conditional independence (CI) assumption that underlies causal inference and economic policy evaluation in a time series context. The CI assumption states that, conditional on a set of predetermined controls (possibly including lagged outcomes and past policy choices), the current policy choice is independent of potential outcomes, which permits identification of dynamic treatment effects via inverse probability weighting (IPW) estimators. The authors transform the CI assumption into a nonparametric conditional moment restriction using auxiliary variables, which are allowed to affect policy choice but whose linkage to policy is fully captured by potential outcomes and observed controls (analogous to instrumental variables in linear regression). Under this setup, CI can be tested by checking whether the auxiliary variables are significant for the conditional mean of the policy choice given the controls.

Two kernel-based test statistics are developed. The first statistic (U_N) follows the Fan-Li (1996) and Li (1999) consistent model specification testing framework and is shown to be asymptotically standard normal under the null hypothesis for strictly stationary, absolutely regular (beta-mixing) time series processes. To address the curse of dimensionality when the control vector is high-dimensional and the policy choice is binary, the authors derive a second test statistic (V_N) that conditions only on the scalar policy propensity score (estimated by a logit or probit model via maximum likelihood) rather than the full covariate vector; this statistic is also asymptotically normal. A modified version of the test following Lavergne and Vuong (2000) is proposed to improve finite-sample performance, with bootstrapping suggested as an alternative for approximating the null distribution.

Monte Carlo simulations across varying autocorrelation, bandwidth, and sample-size settings show both tests have good size and power, with power increasing sharply in sample size and the degree of CI violation. The methods are applied to revisit Angrist and Kuersteiner's (2011) study of the causal effects of monetary policy shocks, using Romer and Romer (2004) Federal Reserve Greenbook forecast data on the intended federal funds rate. The test fails to reject CI for all auxiliary-variable choices (p-values 0.62-0.91), supporting the identification assumption in Angrist and Kuersteiner (2011).

## Key Claims

1. The conditional independence (unconfoundedness) assumption underlying time-series policy evaluation can be transformed into a nonparametric conditional moment test using auxiliary variables whose effect on policy choice is fully mediated by potential outcomes and observed controls.
2. Under Assumption 2 (valid auxiliary variables), the CI assumption implies E(B_t | M_t, A_t) = E(B_t | M_t), so CI can be tested by checking whether auxiliary variables A_t are significant for the conditional mean of policy choice B_t given controls M_t.
3. The kernel-based test statistic U_N is asymptotically standard normal under the null for strictly stationary, absolutely regular (beta-mixing) time series with geometric mixing decay, and is consistent against fixed alternatives.
4. When the policy choice is binary, conditioning solely on the scalar policy propensity score p(M_t) removes all bias from observable controls, yielding test statistic V_N that avoids the curse of dimensionality in high-dimensional control settings.
5. This is claimed to be the first test of CI for economic policy evaluation in a time series context; prior CI tests (Donald et al. 2014; Chen et al. 2018) addressed only cross-sectional data.
6. A modified test statistic following Lavergne and Vuong (2000) shares the same asymptotic distribution while improving finite-sample performance over the basic statistic.
7. Monte Carlo studies show both U_N and V_N have good empirical size (near nominal 5%) for N=400 with moderate bandwidth, and power rising with sample size and the magnitude of CI violation.
8. Applying the test to the Angrist and Kuersteiner (2011) monetary-policy example with Romer-Romer (2004) data fails to reject CI for all auxiliary variables (p-values 0.62-0.91), supporting their identification assumption.

## Questions Raised

- How should valid auxiliary variables A_t be selected in practice? The authors note there is no general guideline and selection may need to be done case by case, and the testing power may depend on this choice.
- If practitioners choose auxiliary variables that do not satisfy Assumption 2, the test tends to reject CI even when CI is true; how can the validity of candidate auxiliary variables be assessed?
- How can the dimensionality problem be addressed in the general case where the policy choice is multinomial (not binary)?
- Can alternative test constructions, such as the Durbin-Wu-Hausman type (Donald et al. 2014) or Kolmogorov-Smirnov type (Chen et al. 2018) statistics, be extended to the time series setting?

## Concepts

- [[concepts/conditional-independence-test|Conditional Independence Test]]
- [[concepts/unconfoundedness-assumption|Conditional Unconfoundedness / Conditional Independence Assumption]]
- [[concepts/inverse-probability-weighting|Inverse Probability Weighting]]
- [[concepts/propensity-score|Propensity Score]]
- [[concepts/nonparametric-conditional-moment-test|Nonparametric Conditional Moment Test]]
- [[concepts/potential-outcomes|Potential Outcomes Framework (Rubin Causal Model)]]
- [[concepts/beta-mixing-processes|Absolutely Regular (Beta-Mixing) Processes]]

## Entities

- [[entities/zongwu-cai|Zongwu Cai]]
- [[entities/ying-fang|Ying Fang]]
- [[entities/ming-lin|Ming Lin]]
- [[entities/shengfang-tang|Shengfang Tang]]
- [[entities/joshua-angrist|Joshua D. Angrist]]
- [[entities/guido-kuersteiner|Guido M. Kuersteiner]]
- [[entities/donald-rubin|Donald B. Rubin]]
- [[entities/qi-li|Qi Li]]
- [[entities/yanqin-fan|Yanqin Fan]]
- [[entities/christina-romer|Christina D. Romer]]
- [[entities/david-romer|David H. Romer]]
- [[entities/christopher-sims|Christopher A. Sims]]
- [[entities/pascal-lavergne|Pascal Lavergne]]
- [[entities/quang-vuong|Quang Vuong]]
- [[entities/oscar-jorda|Oscar Jorda]]

## Source

- **Path:** `raw/causality-testing/Testing_TS.pdf`
- **Type:** paper
- **Hash:** `sha256:3d07d42abedd8002e...`
<!-- AUTHORED REGION END -->
