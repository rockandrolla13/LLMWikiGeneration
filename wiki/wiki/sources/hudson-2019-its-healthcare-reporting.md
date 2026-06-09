---
authors:
- Jemma Hudson
- Shona Fielding
- Craig R. Ramsay
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/hudson-2019-its-healthcare-reporting
page_type: source
publication_date: '2019'
publication_venue: BMC Medical Research Methodology
related:
- concepts/autocorrelation-time-series
- concepts/interrupted-time-series-design
- concepts/quasi-experimental-design
- concepts/randomised-controlled-trial
- concepts/segmented-regression
- entities/bmc-medical-research-methodology
- entities/craig-ramsay
- entities/jemma-hudson
- entities/shona-fielding
- entities/university-of-aberdeen
revision_hash: sha256:a7db6fca75002ed6d71dfe3938f0e6f309d2172a75685f6bc4f7197b28b9f596
revision_id: 1
source_hash: sha256:3dc9c95cf4c2104cfe179dfad76877369659e3eafe95bf5c1736690e84e90266
source_path: raw/causality-testing/s12874-019-0777-x.pdf
source_type: paper
sources: []
tags: []
title: Methodology and reporting characteristics of studies using interrupted time
  series design in healthcare
updated: '2026-06-09T12:00:00Z'
updated_by: op_9f6ea86432f6
---

# Methodology and reporting characteristics of studies using interrupted time series design in healthcare

**Authors:** Jemma Hudson, Shona Fielding, Craig R. Ramsay · **Year:** 2019 · **Venue:** BMC Medical Research Methodology · **Type:** paper

## Summary

This methodological study reviews how the interrupted time series (ITS) design is used and reported across healthcare research. ITS is presented as one of the strongest quasi-experimental designs for evaluating the causal effect of an intervention when a randomised controlled trial (RCT) cannot be used (e.g. because it is costly, unethical, or impractical). In an ITS design, equally spaced data points are collected before and after a known intervention time, and the goal is to test whether the post-intervention data pattern differs from the pre-intervention pattern, summarised through effect estimates such as change in level and change in slope. The authors searched MEDLINE for ITS reports published in 2015 (minimum two pre-intervention and one post-intervention data point), excluding RCTs, systematic reviews/meta-analyses, and ITS designs with a control group, yielding 116 included studies.

The results document substantial inconsistency in design, analysis, and reporting. Interventions were mostly programs (35%) and policies (28%), typically at the hospital level (63%) and aimed at health professionals (79%); data were usually collected monthly (64%). Of the 115 studies reporting an analysis, segmented regression was the dominant method (78%), followed by ARIMA (13%) and generalised estimating equations (6%). Only 55% considered autocorrelation, 8% nonstationarity, and 24% seasonality, and just seven studies reported any sample-size description (only one reproducible). Intervention effects were most often reported as change in slope (84%) and change in level (70%), with only 21% reporting longer-term level changes; confidence intervals or standard errors were frequently omitted.

The authors conclude that reporting of ITS design features and results is currently poor and heterogeneous, that study definitions vary widely (only 29 of 116 studies referred to the design as 'ITS'), and that the diversity of effect estimates and statistical methods makes pooling results in meta-analyses difficult. They call for formal reporting guidelines developed through consensus methods (e.g. a Delphi study) and for methodological work comparing ITS analysis approaches.

## Key Claims

1. The interrupted time series (ITS) design is one of the strongest quasi-experimental designs and serves as an alternative for estimating the causal effect of a healthcare intervention when an RCT is costly, unethical, or impractical.
2. Of 116 included ITS studies published in 2015, segmented regression was the most common analysis method (78%), followed by ARIMA models (13%) and generalised estimating equations (6%).
3. Key time-series assumptions were frequently neglected: only 55% of studies considered autocorrelation, 8% nonstationarity, and 24% seasonality.
4. Only seven studies (6%) reported any sample-size description, and only one of these provided a reproducible calculation; none based the sample size on the effect size of interest.
5. Intervention effects were most often reported as change in slope (84%) and change in level (70%), but the diversity of relative versus absolute effect estimates makes meta-analysis difficult.
6. Study definitions were inconsistent, with only 29 of 116 studies explicitly using the term 'ITS', and reporting of design features and results was generally poor.
7. The authors call for formal consensus-based reporting guidelines (e.g. a Delphi study) and methodological research comparing ITS analysis methods.

## Questions Raised

- Which ITS statistical method (segmented regression, ARIMA, GEE, change-point analysis, mixed models) should be preferred, and under what data conditions?
- How should sample size for an ITS study be justified relative to the effect size of interest (e.g. change in slope) rather than differences in proportions?
- What standardised reporting guideline should be adopted for ITS designs, and how should it be developed through consensus?
- Given the variety of relative and absolute effect estimates, how can results across ITS studies be made comparable or poolable in meta-analysis?
- Would searching multiple years or grey literature and additional databases materially change the picture of ITS use and reporting?

## Concepts

- [[concepts/interrupted-time-series-design|Interrupted Time Series Design]]
- [[concepts/quasi-experimental-design|Quasi-Experimental Design]]
- [[concepts/segmented-regression|Segmented Regression]]
- [[concepts/autocorrelation-time-series|Autocorrelation in Time Series]]
- [[concepts/randomised-controlled-trial|Randomised Controlled Trial]]

## Entities

- [[entities/jemma-hudson|Jemma Hudson]]
- [[entities/shona-fielding|Shona Fielding]]
- [[entities/craig-ramsay|Craig R. Ramsay]]
- [[entities/university-of-aberdeen|University of Aberdeen]]
- [[entities/bmc-medical-research-methodology|BMC Medical Research Methodology]]

## Source

- **Path:** `raw/causality-testing/s12874-019-0777-x.pdf`
- **Type:** paper
- **Hash:** `sha256:3dc9c95cf4c2104cf...`