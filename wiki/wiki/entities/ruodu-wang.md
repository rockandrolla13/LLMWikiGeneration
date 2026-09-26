---
title: Ruodu Wang
page_id: entities/ruodu-wang
page_type: entity
entity_type: person
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
affiliations:
- University of Waterloo, Department of Statistics and Actuarial Science
tags:
- researcher
- e-values
- risk-measures
- multiple-testing
- statistics
sources:
- sources/vovk-2020-evalues-calibration-combination
- sources/wang-2021-fdr-control-evalues
- sources/wang-2025-admissible-merging-evalues
- sources/wang-2022-e-backtesting
- sources/wang-2023-p-star-values
related:
- entities/vladimir-vovk
- entities/aaditya-ramdas
- entities/johanna-ziegel
- concepts/e-value
- concepts/e-process
- concepts/p-value-merging
mind_map_priority: high
schema_version: 2
uuid: 16519a48-bb19-5c3e-b044-a09ab68f9dd4
content_hash: sha256:c05d5b5bdfe16f545f456f6328c83f2a37b5a4285c3caf72451636c9fc61ed5a
---

<!-- AUTHORED REGION START -->
# Ruodu Wang

**Ruodu Wang** is a professor in the Department of Statistics and Actuarial Science at the University of Waterloo, and the central figure in the e-value literature. He works at the junction of risk measures and hypothesis testing, which is why this cluster reaches both [[concepts/expected-shortfall|risk management]] and [[concepts/multiple-testing|multiple testing]].

## The through-line

An e-value is the payoff of a bet against a null hypothesis at fair odds. That single idea produces:

- **Merging without assumptions** — a weighted average of e-values is valid under arbitrary dependence, and [[sources/wang-2025-admissible-merging-evalues|it is the only admissible way]].
- **False discovery rate control without corrections** — [[sources/wang-2021-fdr-control-evalues|e-BH]] with Ramdas, which pays nothing for dependence where Benjamini–Yekutieli pays a factor of about $\log K$.
- **Anytime-valid risk backtesting** — [[sources/wang-2022-e-backtesting|E-backtesting]] with Qiuqi Wang and Johanna Ziegel, which monitors Expected Shortfall forecasts continuously.

## Collaborators in This Wiki

- [[entities/vladimir-vovk|Vladimir Vovk]] — the foundational e-value papers and the sequential merging theory.
- [[entities/aaditya-ramdas|Aaditya Ramdas]] — FDR control, compound e-values, post-selection inference.
- [[entities/johanna-ziegel|Johanna Ziegel]] and [[entities/qiuqi-wang|Qiuqi Wang]] — E-backtesting.
- [[entities/ziyu-xu|Ziyu Xu]] — bandit multiple testing and e-value confidence intervals.

## Publications in This Wiki

The wiki holds 25 papers from his working paper series, spanning foundations, p-value merging, multiple testing, sequential e-processes and applications. Start with [[sources/vovk-2020-evalues-calibration-combination|E-values: calibration, combination and applications]] for the framework, [[sources/wang-2021-fdr-control-evalues|e-BH]] for multiple testing, and [[sources/wang-2022-e-backtesting|E-backtesting]] for the risk-management application.

## See Also

[[concepts/e-value|E-value]] · [[concepts/e-process|E-process]] · [[concepts/p-value-merging|Merging P-values and E-values]]
<!-- AUTHORED REGION END -->
