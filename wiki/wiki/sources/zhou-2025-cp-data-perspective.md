---
title: "Conformal Prediction: A Data Perspective"
page_id: sources/zhou-2025-cp-data-perspective
page_type: source
source_type: survey
revision_id: 1
created: 2026-05-24T16:00:00Z
updated: 2026-05-24T16:00:00Z
authors: ["Xiaofan Zhou", "Baiting Chen", "Yu Gui", "Lu Cheng"]
year: 2025
venue: "ACM Computing Surveys 58(2), Article 49 (DOI 10.1145/3736575)"
tags: [conformal-prediction, survey, uncertainty-quantification, data-centric, nlp, computer-vision, graphs, llms, streaming-data]
related: [
  concepts/conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/full-conformal-prediction,
  concepts/cross-conformal-prediction,
  concepts/jackknife-plus,
  concepts/weighted-conformal-prediction,
  concepts/conformal-risk-control,
  concepts/conformalized-quantile-regression,
  concepts/adaptive-prediction-sets,
  concepts/regularized-adaptive-prediction-sets,
  concepts/adaptive-conformal-inference,
  concepts/agaci,
  concepts/spci,
  concepts/enbpi,
  concepts/conformal-pid-control,
  concepts/block-conformal-prediction,
  concepts/distributional-conformal-prediction,
  concepts/cp-for-nlp,
  concepts/cp-for-vision,
  concepts/cp-for-graphs,
  concepts/cp-for-llms,
  entities/xiaofan-zhou,
  entities/baiting-chen,
  entities/yu-gui,
  entities/lu-cheng,
  sources/angelopoulos-2022-gentle-intro,
  sources/fontana-2023-cp-unified-review,
  sources/stocker-2025-conformal-timeseries-intro,
  sources/vovk-2005-algorithmic-learning
]
mind_map_priority: high
---

# Conformal Prediction: A Data Perspective

**Authors:** [[entities/xiaofan-zhou|Xiaofan Zhou]], [[entities/baiting-chen|Baiting Chen]], [[entities/yu-gui|Yu Gui]], [[entities/lu-cheng|Lu Cheng]]

**Year:** 2025

**Venue:** *ACM Computing Surveys* 58(2), Article 49 (Sept 2025), 37 pages. DOI 10.1145/3736575.

## Summary

Zhou, Chen, Gui, and Cheng survey [[concepts/conformal-prediction|conformal prediction (CP)]] from an explicitly data-centric perspective, in contrast to the methodology-organised reviews of [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates (2022)]] and [[sources/fontana-2023-cp-unified-review|Fontana, Zeni & Vantini (2023)]]. The organising device is a hierarchical taxonomy that splits CP applications first by collection process (static vs dynamic data), then by internal structure. Static data subdivides into structured (flat/tabular, hierarchical, matrix/tensor, graph/tree) and unstructured (text, image, heterogeneous/multi-modal). Dynamic data centres on spatio-temporal and further splits into one-dimensional, multi-dimensional, and streaming. The survey treats data modality, not algorithmic family, as the primary axis of comparison — arguing that emerging modalities (LLM-scale generative text, computer vision, graphs, multi-modal sensors, streaming feeds) introduce fundamentally new exchangeability violations and computational constraints that traditional CP variants were not designed to handle.

After a compact background section (full CP, [[concepts/split-conformal-prediction|split CP]], [[concepts/jackknife-plus|jackknife+]] / CV+, [[concepts/weighted-conformal-prediction|weighted CP]], [[concepts/conformal-risk-control|conformal risk control]], and metrics including marginal, adversarial, instantaneous, conditional, and hybrid CWC-style coverage), the paper systematically reviews CP techniques per data type:

- **Tabular regression/classification, multivariate and functional response.** Standard ground.
- **Data with noise / missingness / censoring.** Including causal inference and survival analysis.
- **Hierarchical sampling.** Pooled CDF, double conformal, subsampling once, repeated subsampling.
- **Matrix/tensor completion.** Conformal recovery and rank guarantees.
- **Graph data.** Both inductive and transductive regimes; neighborhood adaptive prediction sets, diffused nonconformity scores, conformalized link prediction with FDR control (Benjamini-Hochberg on conformal p-values).
- **Text and NLU.** Text classification, QA, MCQA, machine translation, POS tagging.
- **NLG and LLMs.** Next-word prediction, code generation, [[concepts/cp-for-llms|conformal RAG]], factuality subclaim filtering, conformal alignment for trustworthy outputs, inference-time efficiency via CALM and Pareto Testing.
- **Computer vision.** Image classification, segmentation (Kandinsky calibration), image-to-image regression.
- **One-dimensional spatio-temporal CP.** Three distinct lineages: reweighting (NexCP, HopCPT), updating nonconformity scores ([[concepts/enbpi|EnbPI]], [[concepts/spci|SPCI]]), updating the miscoverage rate ([[concepts/adaptive-conformal-inference|ACI]], [[concepts/agaci|AgACI]], MVP, SAOCP, [[concepts/conformal-pid-control|PID-Conformal]], [[concepts/block-conformal-prediction|BCI]]).
- **Multi-dimensional and streaming CP.** Ellipsoidal CP, cross-sectional / longitudinal coverage (TQA), CP for motion planning and concept drift.

## Key Contributions

1. **Data-centric CP taxonomy.** A hierarchical organisation by data modality rather than algorithm. Complements the methodology-organised Angelopoulos-Bates and Fontana-Zeni-Vantini surveys.
2. **Unified framework for one-dimensional spatio-temporal CP.** Categorises time-series CP into three distinct lineages — reweighting, score-updating, α-updating — and shows how these can be combined. (Stocker et al. 2025's four-family taxonomy reaches a similar end-state via a slightly different cut.)
3. **Comprehensive treatment of CP for graphs.** Inductive vs transductive distinction, neighborhood adaptive prediction sets, diffused nonconformity scores aggregating neighborhood information, conformalized link prediction with Benjamini-Hochberg FDR control, graph-population CP via quotient spaces.
4. **CP for LLMs and NLG.** Synthesises the recent wave: APS-based next-word prediction with non-exchangeable CP, conformal sets for MCQA and open-domain QA, conformal RAG with risk control, factuality filtering via subclaim decomposition, conformal alignment for selecting trustworthy outputs, inference-time efficiency via early-exit CALM and Pareto Testing.
5. **Heterogeneous and multi-modal CP review.** Multi-modal CP, multi-view CP (MVCP via half-plane intersections), shape-template prediction regions over residuals, zero-shot CP via CLIP foundation models, CP under federated learning with ε-approximate β-quantiles.
6. **Forward research agenda.** Six concrete open directions: principled non-exchangeability under light distributional assumptions, robust CP under block-wise / non-random missingness and adversarial attacks, optimal multi-modal aggregation, CP for responsible AI (fairness/privacy/interpretability), CP as cognitive side information in human-in-the-loop decision-making, and modernisation of open-source CP tooling (PUNCC, TorchCP, Fortuna, R-ACI) for unstructured / streaming / LLM-era data.

## Why This Source Matters

This is the **modality-organised** entry point to the CP literature. If you want to know "what's the state of the art for CP on graphs / LLMs / streaming / images", read this. If you want methodology and theory, pair with [[sources/angelopoulos-2022-gentle-intro|Angelopoulos-Bates]] and [[sources/fontana-2023-cp-unified-review|Fontana et al.]]; for time-series specifically, pair with [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al.]].

## Relation to Other Wiki Sources

- [[sources/angelopoulos-2022-gentle-intro]] — methodology-organised practitioner tutorial.
- [[sources/fontana-2023-cp-unified-review]] — theory-organised review.
- [[sources/stocker-2025-conformal-timeseries-intro]] — time-series-specific four-family taxonomy.
- [[sources/vovk-2005-algorithmic-learning]] — foundational book.

## Questions Raised

- How can CP move beyond bounding the coverage gap (as in non-exchangeable CP) to *adaptively minimise* it under heterogeneity and temporal dependence?
- Can ACI-style adversarial-coverage methods be augmented with light distributional assumptions to recover per-step validity rather than only long-run adversarial guarantees?
- What is the right framework for CP under block-wise or non-random missingness, beyond MAR assumptions?
- How should multi-modal data (text + image + sensor) be optimally aggregated to enhance CP performance, especially under per-modality covariate shift?
- How can CP for graphs leverage richer structural signals beyond local neighborhoods (similar-degree nodes, shared topological properties, weighted edges)?
- Can CP techniques be made computationally efficient at LLM-scale, particularly with FAISS-style retrieval and unbounded generative output spaces?
- How can CP serve as effective side information for human-in-the-loop decision-making across more domains than medical triage?

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/cp-for-nlp]], [[concepts/cp-for-vision]], [[concepts/cp-for-graphs]], [[concepts/cp-for-llms]]
- [[entities/xiaofan-zhou]], [[entities/baiting-chen]], [[entities/yu-gui]], [[entities/lu-cheng]]
