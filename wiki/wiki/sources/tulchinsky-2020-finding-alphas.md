---
authors:
- Igor Tulchinsky
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/tulchinsky-2020-finding-alphas
page_type: source
publication_date: '2020'
publication_venue: John Wiley & Sons
related:
- concepts/alpha-correlation-turnover
- concepts/alpha-signal
- concepts/automated-alpha-search
- concepts/information-ratio
- concepts/look-ahead-bias-data-mining
- concepts/overfitting-in-alpha-research
- concepts/the-unrule
- entities/campbell-harvey
- entities/igor-tulchinsky
- entities/john-wiley-sons
- entities/marcos-lopez-de-prado
- entities/worldquant
revision_hash: sha256:24c01b780bcd47fa9ebd61d169deab117602cec843d499e69be7c48484d4a8a9
revision_id: 1
source_hash: sha256:75fc2cc0ecbaf3328895280cbb6bcda3461439bc9347969da1ce0533bce7df71
source_path: raw/creditmacro/Finding Alphas (A Quantitative Approach to Building Trading
  Strategies)  (Tulchinsky, Igor) (z-library.sk, 1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- quantitative-finance
- alpha-research
- algorithmic-trading
- systematic-trading
- backtesting
- overfitting
title: 'Finding Alphas: A Quantitative Approach to Building Trading Strategies (Second
  Edition)'
updated: '2026-06-20T01:03:51Z'
updated_by: op_5e2408512522
schema_version: 2
uuid: 2b0ce35f-5d9b-56cc-b2df-eed39cb8404f
content_hash: sha256:108c95966af0d7207eb310b34fc4033f9f010b37c09cd4c8092d4226e4b0a95f
---

<!-- AUTHORED REGION START -->
# Finding Alphas: A Quantitative Approach to Building Trading Strategies (Second Edition)

**Authors:** Igor Tulchinsky · **Year:** 2020 · **Venue:** John Wiley & Sons · **Type:** book

## Summary

An edited volume by Igor Tulchinsky and WorldQuant staff on the industrial process of discovering, designing, evaluating, and deploying 'alphas' - individual automated predictive trading signals expressed as mathematical expressions, code, and parameters. The thesis is that an alpha is an idea about how the market works that captures a (often weak) predictive signal; rather than seeking a few strong strategies, WorldQuant industrializes the search across millions of weak signals and combines many low-correlation alphas. A governing principle is the 'UnRule' - no rule ever works perfectly - motivating disciplined loss-cutting. The book heavily warns about overfitting, look-ahead bias, and data mining as dominant failure modes, and evaluates alphas via information ratio, margin, turnover, and correlation.

## Key Claims

1. An alpha is an automated predictive model encoding a hypothesis about market behavior, mapping input data to positions or trades.
2. Quality alphas are simple, have a good information ratio, are robust to small data/parameter changes, and generalize across universes and regions.
3. The information ratio measures signal strength and steadiness; a unique, lightly-fitted alpha might show an annualized IR around 1.0.
4. Low correlation to existing alphas is highly desirable because portfolio value comes from combining many uncorrelated weak signals.
5. The 'UnRule' - no rule ever works perfectly - implies disciplined cutting of losses once alphas stop working.
6. Overfitting is the central risk of backtesting; mitigations include minimizing parameters, regularization, cross-validation, out-of-sample testing, and economic justification.
7. Look-ahead bias and data mining are the two main systematic biases; data should be dual-timestamped and ML tuned only on backward-looking data.

## Questions Raised

- How can the predictive power of an individual alpha be assessed before its target strategy is known?
- How do you distinguish a genuine signal from overfitting when in-sample backtest performance is strong?
- How should many weak, partially-correlated alphas be combined into a robust portfolio?

## Concepts

- [[concepts/alpha-signal|Alpha (Predictive Trading Signal)]]
- [[concepts/information-ratio|Information Ratio]]
- [[concepts/the-unrule|The UnRule (Cutting Losses)]]
- [[concepts/overfitting-in-alpha-research|Overfitting in Alpha Research]]
- [[concepts/look-ahead-bias-data-mining|Look-Ahead Bias and Data Mining]]
- [[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]]
- [[concepts/automated-alpha-search|Automated Alpha Search]]

## Entities

- [[entities/igor-tulchinsky|Igor Tulchinsky]]
- [[entities/worldquant|WorldQuant]]
- [[entities/marcos-lopez-de-prado|Marcos Lopez de Prado]]
- [[entities/campbell-harvey|Campbell Harvey]]
- [[entities/john-wiley-sons|John Wiley & Sons]]

## Source

- **Path:** `raw/creditmacro/Finding Alphas (A Quantitative Approach to Building Trading Strategies)  (Tulchinsky, Igor) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:75fc2cc0ecbaf3328...`
<!-- AUTHORED REGION END -->
