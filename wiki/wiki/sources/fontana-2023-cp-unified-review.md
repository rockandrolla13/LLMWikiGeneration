---
title: "Conformal prediction: A unified review of theory and new challenges"
page_id: sources/fontana-2023-cp-unified-review
page_type: source
source_type: review-paper
revision_id: 1
created: 2026-05-24T16:00:00Z
updated: 2026-05-24T16:00:00Z
authors: ["Matteo Fontana", "Gianluca Zeni", "Simone Vantini"]
year: 2023
venue: "Bernoulli 29(1), 1-23 (DOI 10.3150/21-BEJ1447)"
tags: [conformal-prediction, review, theory, nonparametric-statistics, prediction-intervals, exchangeability]
related: [
  concepts/conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/full-conformal-prediction,
  concepts/cross-conformal-prediction,
  concepts/conformalized-quantile-regression,
  concepts/conditional-validity,
  concepts/exchangeability,
  concepts/nonconformity-score,
  concepts/mondrian-conformal-prediction,
  concepts/jackknife-plus,
  concepts/venn-predictors,
  concepts/coverage-guarantee,
  concepts/prediction-intervals,
  entities/matteo-fontana,
  entities/gianluca-zeni,
  entities/simone-vantini,
  sources/vovk-2005-algorithmic-learning,
  sources/shafer-2007-cp-tutorial,
  sources/vovk-2012-cross-conformal,
  sources/angelopoulos-2022-gentle-intro,
  sources/stocker-2025-conformal-timeseries-intro
]
mind_map_priority: high
---

# Conformal prediction: A unified review of theory and new challenges

**Authors:** [[entities/matteo-fontana|Matteo Fontana]], [[entities/gianluca-zeni|Gianluca Zeni]], [[entities/simone-vantini|Simone Vantini]]

**Year:** 2023

**Venue:** *Bernoulli* 29(1), 1-23. DOI 10.3150/21-BEJ1447.

## Summary

Fontana, Zeni and Vantini provide a theory-first unified review of [[concepts/conformal-prediction|Conformal Prediction]], the distribution-free, finite-sample valid framework that emerged from [[entities/vladimir-vovk|Vovk]], [[entities/alexander-gammerman|Gammerman]] and [[entities/glenn-shafer|Shafer]]'s work beginning in the late 1990s. The paper is positioned to fill a gap left by the two canonical book-length treatments — [[sources/vovk-2005-algorithmic-learning|Vovk-Gammerman-Shafer (2005)]] and Balasubramanian-Ho-Vovk (2014). It captures roughly fifteen years of post-2005 theoretical development and imposes a consistent notation (using α for the significance level after Lei-Robins-Wasserman, rather than the Vovk-school ε).

Part 2 lays the foundations: examples, bags, [[concepts/nonconformity-score|nonconformity measures]], p-values, smoothed conformal predictors, validity vs efficiency, the i.i.d./[[concepts/exchangeability|exchangeability]]/randomness distinction, classification and regression nonconformity measures including the Ridge Regression Confidence Machine (RRCM), and the online framework where successive conformal errors are shown (Vovk 2002) to be independent Bernoulli trials.

Part 3 reviews recent advances: different notions of validity (the impossibility of distribution-free object-conditional validity per Lei-Wasserman 2014 and Barber et al. 2021), local validity, [[concepts/mondrian-conformal-prediction|Mondrian conformal predictors]], [[concepts/conformalized-quantile-regression|CQR]]; inductive / [[concepts/split-conformal-prediction|split conformal predictors]]; [[concepts/cross-conformal-prediction|cross-conformal prediction]] and jackknife / [[concepts/jackknife-plus|jackknife+]] procedures; normalised (locally-weighted) nonconformity scores for heteroskedastic data; and functional prediction bands.

## What's Unique to Fontana's Framing

Compared to [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates 2022]] (practitioner-facing recipes with code), [[sources/zhou-2025-cp-data-perspective|Zhou et al. 2025]] (data-modality-organised), and [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]] (time-series-specific):

- Deliberate emphasis on the mathematical scaffolding: measurability, bags as multisets, n-taxonomies, on-line compression models, the de Finetti reduction of randomness to exchangeability over Borel spaces.
- Terminological and notational unification across a literature the authors describe as inconsistent.
- Retains the original transductive formalism rather than collapsing to split-CP recipes.
- Treats the on-line setting as a first-class object, not an afterthought.
- Substantial attention to the conditional-validity impossibility results and partial workarounds (Mondrian taxonomies, local validity, CQR) as a coherent theoretical thread.

This is the canonical theoretical companion to Angelopoulos-Bates and the entry point for researchers wanting to *extend* CP rather than *apply* it.

## Key Contributions

1. Unified notation across the CP literature: α (after Lei-Robins-Wasserman) for the significance level, and predicting the (n+1)-th example from the previous n rather than Vovk's n-th-from-(n−1) convention.
2. First comprehensive theory-focused review of post-2005 developments. Deliberately complements rather than duplicates the [[sources/vovk-2005-algorithmic-learning|2005 textbook]] and the application-focused Balasubramanian-Ho-Vovk (2014) edited volume.
3. Systematic treatment of validity notions as a coherent hierarchy: marginal → local (Lei-Wasserman 2014) → Mondrian / category-conditional → the impossibility of distribution-free object-conditional validity (Barber et al. 2021) → [[concepts/conformalized-quantile-regression|CQR]] (Romano-Patterson-Candès 2019) as a practical partial answer.
4. Integration of the on-line framework (where successive errors are i.i.d. Bernoulli per Vovk 2002) with the batch framework on equal footing, including the de Finetti argument that randomness and exchangeability coincide in the infinite-horizon Borel-space case.
5. Map of post-exchangeability extensions: on-line compression models, random effects (Dunn-Wasserman 2018), weighted exchangeable data / covariate shift (Barber et al. 2019b), and dependent / time-series data via blocking (Chernozhukov-Wuthrich-Zhu 2018).
6. Survey of efficiency / computation trade-offs across transductive (full), inductive (split), [[concepts/cross-conformal-prediction|cross-conformal]], jackknife and [[concepts/jackknife-plus|jackknife+]] procedures. Includes the open question of whether transductive predictors are systematically more efficient than inductive ones (Linusson et al. 2014b).
7. Section on functional prediction bands tying CP to Functional Data Analysis, including the authors' own work (Diquigiovanni-Fontana-Vantini 2021) on closed-form finite-sample valid bands for functional data, multivariate functional data, and functional time series.

## Relation to Other Wiki Sources

- [[sources/vovk-2005-algorithmic-learning]] — the textbook this paper extends.
- [[sources/shafer-2007-cp-tutorial]] — the foundational tutorial.
- [[sources/vovk-2012-cross-conformal]] — primary source for one of the methods reviewed.
- [[sources/angelopoulos-2022-gentle-intro]] — the practitioner counterpart.
- [[sources/zhou-2025-cp-data-perspective]] — the data-centric companion.
- [[sources/stocker-2025-conformal-timeseries-intro]] — the time-series companion.

## Questions Raised

- Should the i-th example be included in or excluded from the bag against which its nonconformity score is computed, to maximise efficiency? Fontana labels this "an object of further future investigation".
- Are transductive (full) conformal predictors systematically more efficient than inductive ones? Linusson et al. (2014b) and Papadopoulos (2008) cast doubt on the conventional wisdom; "still open".
- How should a Mondrian taxonomy be chosen? The "problem of the reference class" (categories large enough for stable sample-size estimates vs small enough for informative conditioning) lacks a principled solution.
- How should the calibration-set size be chosen in inductive CP? Heuristics suggest 15-33% of the data with at least a few hundred examples; the bias-variance trade-off is unresolved.
- How can object-conditional validity be achieved in any nontrivial finite-sample sense, given the Lei-Wasserman / Barber et al. impossibility results? CQR and Mondrian predictors are partial answers but not complete ones.
- How should CP be extended to functional data so simultaneous bands are both finite-sample valid and tight?

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/mondrian-conformal-prediction]]
- [[concepts/conditional-validity]]
- [[entities/matteo-fontana]], [[entities/gianluca-zeni]], [[entities/simone-vantini]]
