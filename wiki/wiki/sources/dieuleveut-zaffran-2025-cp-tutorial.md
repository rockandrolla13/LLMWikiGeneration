---
title: "Conformal Prediction: A Tutorial (Hi! PARIS Summer School)"
page_id: sources/dieuleveut-zaffran-2025-cp-tutorial
page_type: source
source_type: tutorial-slides
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
authors: ["Aymeric Dieuleveut", "Margaux Zaffran"]
year: 2025
venue: "Hi! PARIS Summer School, July 8, 2025 (based on Dieuleveut–Zaffran UAI/ICML tutorial)"
tags: [conformal-prediction, tutorial, slides, split-conformal-prediction, cqr, adaptive-conformal-inference, time-series, covariate-shift, missing-values, full-conformal, jackknife-plus, uncertainty-quantification]
related: [
  concepts/conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/conformalized-quantile-regression,
  concepts/adaptive-conformal-inference,
  concepts/exchangeability,
  concepts/marginal-coverage,
  concepts/conditional-coverage,
  concepts/full-conformal-prediction,
  concepts/nonconformity-score,
  concepts/adaptive-prediction-sets,
  concepts/mask-conditional-validity,
  concepts/uncertainty-quantification,
  entities/aymeric-dieuleveut,
  entities/margaux-zaffran,
  sources/zaffran-2022-aci,
  sources/angelopoulos-2022-gentle-intro,
  sources/zaffran-phd,
  sources/zaffran-2023-conformal-missing
]
mind_map_priority: medium
---

# Conformal Prediction: A Tutorial (Hi! PARIS Summer School)

**Authors / Presenters:** [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]] (delivering), [[entities/margaux-zaffran|Margaux Zaffran]] (co-developer)

**Year:** 2025

**Venue:** Hi! PARIS Summer School, École Polytechnique, July 8, 2025. Based on the joint Dieuleveut–Zaffran tutorial previously given at UAI and ICML.

**Format:** 91-slide deck (PDF with animations; some slide frames repeat after pymupdf extraction due to rasterised animations).

## Summary

A structured introduction to [[concepts/conformal-prediction|conformal prediction]] as a model-agnostic, distribution-free framework for finite-sample-valid predictive set construction. The deck opens with motivation (uncertainty quantification, miscoverage level α, marginal coverage guarantee), then builds up from [[concepts/split-conformal-prediction|Split Conformal Prediction (SCP)]] in regression and classification through [[concepts/conformalized-quantile-regression|CQR]] and [[concepts/adaptive-prediction-sets|Adaptive Prediction Sets (APS)]], with explicit treatment of [[concepts/exchangeability|exchangeability]], the quantile lemma, and the standard SCP proof architecture.

The second half covers more advanced material: [[concepts/conditional-coverage|conditional coverage]] and its impossibility result, PAC-style calibration-conditional bounds (Vovk 2012; Bian–Barber 2023), [[concepts/full-conformal-prediction|Full Conformal Prediction]], Jackknife / Jackknife+ (Barber et al. 2021), and methods for **breaking exchangeability** — covariate shift (Tibshirani et al. 2019), online/time-series settings via OSSCP (Zaffran et al. 2022; Dutot et al. 2024) and [[concepts/adaptive-conformal-inference|ACI]] (Gibbs & Candès 2021). Applied case studies include image-to-image regression with distribution-free UQ (Angelopoulos et al. 2022) and French day-ahead electricity spot price forecasting. Methodological advances featured: CP with missing values ([[sources/zaffran-2023-conformal-missing|Zaffran, Josse, Romano, Dieuleveut 2024]]) and Valid Selection among Conformal Sets (Hegazy, Aolaritei, Jordan, Dieuleveut 2025).

## Key Topics Covered

1. **Foundations.** SCP marginal validity via the quantile lemma and exchangeability.
2. **Score design.** [[concepts/nonconformity-score|Nonconformity scores]] for regression, classification (APS), and [[concepts/conformalized-quantile-regression|CQR]].
3. **Coverage notions.** Marginal vs. (X-)conditional vs. calibration-conditional; Vovk impossibility / PAC bounds.
4. **Avoiding the split.** [[concepts/full-conformal-prediction|Full CP]], Jackknife, and Jackknife+ as the "no split" family.
5. **Beyond exchangeability.** Covariate shift via weighted CP (Tibshirani 2019); time-series CP via OSSCP and [[concepts/adaptive-conformal-inference|ACI]] with online gradient updates.
6. **Applied case studies.** Healthcare image-to-image regression (Angelopoulos et al. 2022); French day-ahead electricity prices.
7. **Recent Dieuleveut-group results.** CP under missing values (CP-MDA-Nested); Valid Selection among Conformal Sets.
8. **Outlook.** Selective inference / FDR, beyond-indicator-loss [[concepts/conformal-risk-control|risk control]], aggregation of predictive sets.

## Pedagogical Notes

- The deck is **the cleanest entry-point** to the Zaffran/Dieuleveut research line. For published companions, see [[sources/zaffran-2022-aci]] (ACI for time series) and [[sources/zaffran-2023-conformal-missing]] (CP with missing values).
- Math notation lightly mangled in pymupdf extraction (PDF italics encoding) but readable. Cover-slide identification of presenter, venue, and date is unambiguous.
- Animated/duplicated slide frames inflate the markdown — many `## **Section**` headers repeat 5–10× because animations were rasterised as separate pages.

## Relation to Other Wiki Sources

- [[sources/zaffran-phd]] — Zaffran's PhD thesis (June 2024), the long-form companion to this tutorial.
- [[sources/zaffran-2022-aci]] — featured ACI paper.
- [[sources/zaffran-2023-conformal-missing]] — featured CP-with-missing-values paper.
- [[sources/angelopoulos-2022-gentle-intro]] — recommended as the i.i.d. companion text.

## Questions Raised

- How tight are PAC-style calibration-conditional bounds in realistic sample sizes?
- Under what non-stationarity regimes does ACI outperform OSSCP-horizon, and vice versa?
- Can CP-MDA-Nested–style [[concepts/mask-conditional-validity|mask-conditional validity]] be extended beyond MCAR/MAR assumptions?
- Is pointwise stable selection among conformal sets compatible with online aggregation schemes (Gasparin & Ramdas 2024)?

## See Also

- [[entities/aymeric-dieuleveut]], [[entities/margaux-zaffran]]
- [[concepts/conformal-prediction]]
- [[concepts/adaptive-conformal-inference]]
