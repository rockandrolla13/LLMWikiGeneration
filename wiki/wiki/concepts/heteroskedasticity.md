---
title: "Heteroskedasticity"
page_id: concepts/heteroskedasticity
page_type: concept
created: 2026-08-06T00:00:00Z
updated: 2026-08-06T00:00:00Z
tags: [heteroskedasticity, conformal-prediction, conditional-validity, quantile-regression, missing-data]
sources: [sources/chernozhukov-2021-distributional-cp, sources/zaffran-2023-conformal-missing]
related: [concepts/conformal-prediction, concepts/conditional-validity, concepts/conformalized-quantile-regression, concepts/missing-data-imputation, concepts/coverage-guarantee]
mind_map_priority: medium
---

# Heteroskedasticity

Non-constant error variance: the spread of the outcome around its prediction depends on where you are in the covariate space. In this wiki it matters mainly as the reason **fixed-width prediction intervals fail**.

## Why It Breaks Uncertainty Quantification

A method that produces one interval width everywhere will over-cover in low-variance regions and under-cover in high-variance ones, while still hitting its marginal target. Marginal coverage is preserved; [[concepts/conditional-validity|conditional validity]] is not.

This is the gap between "90% of my intervals contain the truth" and "for any given input, there is a 90% chance my interval contains the truth."

## Two Responses in the Literature Here

**Adapt the interval shape.** [[sources/chernozhukov-2021-distributional-cp|Chernozhukov, Wüthrich & Zhu (2021)]] propose Distributional Conformal Prediction, which uses the probability integral transform and permutes estimated ranks rather than modelling the conditional mean. Intervals adapt to heteroskedasticity without it being modelled explicitly. Their comparison places mean-based conformal prediction as fixed-length and not conditionally valid, [[concepts/conformalized-quantile-regression|CQR]] as approximately valid and heteroskedasticity-handling, and DCP as handling both at higher computational cost.

**Recognise where it comes from.** [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] show that **missing values themselves induce heteroskedasticity**: prediction uncertainty depends strongly on which features happen to be observed. Two points with the same imputed covariates but different missingness masks do not carry the same uncertainty. This motivates mask-conditional validity, which standard impute-then-predict methods fail to achieve. See [[concepts/missing-data-imputation|Missing Data Imputation]].

## The General Lesson

Heteroskedasticity is not only a property of the data-generating process. It can be manufactured by the pipeline — by imputation, by preprocessing, by any step that varies in reliability across inputs. Interval methods must adapt to it rather than assume it away.

## See Also

[[concepts/conformal-prediction|Conformal Prediction]] · [[concepts/conditional-validity|Conditional Validity]] · [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]] · [[concepts/missing-data-imputation|Missing Data Imputation]] · [[concepts/coverage-guarantee|Coverage Guarantee]] · [[entities/margaux-zaffran|Margaux Zaffran]]
