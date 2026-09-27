---
authors:
- not stated
content_hash: sha256:05f1b92202f5d7b17b1b516e0a0b6a0254e64134cedd02885f464b0091f661c7
created: 2026-09-27 01:47:00+00:00
page_id: sources/webster-2023-introduction-mathematics-causal-inference
page_type: source
related:
- concepts/overfitting-backtesting
- concepts/causal-inference
revision_id: 1
schema_version: 2
source_hash: sha256:b1fa7fd4fc97a655113a3eb107867394854ddf2e03778e102735ab917f696ed4
source_path: markdown_output/webster-2023-introduction-mathematics-causal-inference.md
source_type: book
tags:
- causal-inference
- do-calculus
- simpsons-paradox
- causal-regularization
- algorithmic-trading
- overfitting
- transaction-cost-analysis
- clock-unstated
- asset-none
- added-by-hand
title: An Introduction to the Mathematics of Causal Inference
updated: '2026-09-27T01:47:00Z'
uuid: 1c880546-0d9a-5c6c-89c1-17a2518a8033
year: 2023
---

<!-- AUTHORED REGION START -->
# An Introduction to the Mathematics of Causal Inference

## Summary

This chapter is a self-contained mathematical primer on causal inference, written for traders and quants who need to draw reliable conclusions from trading data. It opens with a pedagogical example in which the same transaction-cost-analysis table supports opposite conclusions about whether an aggressive or a passive execution algorithm performs better, depending on how order size is treated as a cause versus a consequence of algorithm choice. This motivates the formal machinery that follows: causal structures as directed acyclic graphs, causal models built by attaching functional relationships and a probability measure to a graph, d-separation, and the do() operator that formalizes counterfactual questions such as 'what if I always used algorithm A'.

The chapter's central worked example is Simpson's paradox applied to comparing execution algorithms on arrival slippage: an aggressive algorithm can appear better in aggregate while underperforming a passive algorithm separately for both small and large orders, once order size is a confound. The chapter derives, via the back-door and front-door criteria and the rules of do-calculus (based on Pearl's Causality), which control variables correctly identify the causal effect of algorithm choice on execution performance, and shows that conditioning on the wrong variable (a consequence rather than a cause) can reintroduce rather than remove bias. It applies the same apparatus to a live-trading A/B-testing setting, defining an 'algorithm switch' and an 'algorithm acceleration' counterfactual and showing which variables must be controlled to identify each from observational trading data.

The chapter's other main contribution is causal regularization: a method, attributed to Janzing (2019), that repurposes ordinary predictive regularization (ridge-type penalties, cross-validation) to remove confounding bias rather than finite-sample overfitting bias, by calibrating the regularization strength on a small amount of bias-free interventional (experimental) data while fitting the bulk of the model on abundant but confounded observational data. A worked linear-model example shows that, unlike ordinary finite-data bias, bias from an unobserved confounder does not vanish as the sample size grows, which is why interventional data is needed to correct it.

What is new relative to a standard causal-inference treatment is the explicit mapping onto trading problems: TCA comparisons of execution algorithms, price-impact model fitting, and the trade-off between scarce bias-free A/B-test data and plentiful but confounded historical trading data. The chapter is entirely theoretical and pedagogical: all numerical examples are stylized (hypothetical slippage tables, toy causal graphs), and the chapter ends with reader exercises rather than an empirical study.

## Clock and Sampling

**Not stated in the paper.**

The chapter is a mathematical primer, not an empirical microstructure study, so it does not define a market data clock. Its unit of observation in worked trading examples is an individual completed parent order, scored by its arrival slippage in basis points; no tick, volume, or event-based subsampling scheme is specified. The only 'horizon' concept present is the do()-operator's counterfactual comparison (e.g., 'what if I always used algorithm A'), which is a change of probability measure rather than a forward-return prediction horizon.

## Data

- **Asset class:** No data (theory or survey)
- **Instruments:** not stated
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated

## Features and Measures

- **Arrival slippage.** A basis-point performance metric for a trading order, equal to the gap between the execution price and the arrival price (defined elsewhere in the source book), used as the outcome variable in the chapter's execution-algorithm examples.
- **Causal structure (DAG).** A directed acyclic graph over a set of trading variables (e.g., algorithm choice, order size, trading speed, slippage) whose links encode assumed direct functional/causal relationships, used to reason about which variables confound a comparison.
- **do() operator.** A formal action that replaces the causal model's function for a chosen variable with a constant or independent random value, used to express counterfactual questions such as switching or accelerating an execution algorithm.
- **Causal regularization.** A regularization scheme that fits a model's shape on observational data but calibrates the regularization strength using a small amount of bias-free interventional data, so as to shrink the effect of a confounding variable rather than merely to control finite-sample overfitting.

## Method

The chapter builds up causal inference axiomatically on top of a standard probability space, following Pearl's Causality: causal structures (DAGs), causal models (DAGs plus functional relationships and a probability measure), d-separation, and the do() operator for counterfactuals. It proves (by citing Pearl's theorems) the rules of do-calculus and two practical identification tools, the back-door and front-door criteria, which specify which control variables let a causal effect be estimated with an ordinary (non-causal) Bayesian formula.

These tools are applied throughout to a running trading example: comparing an aggressive and a passive execution algorithm on arrival slippage, first informally via Simpson's paradox, then formally via three alternative causal graphs (a fair coin toss driving algorithm choice; order size driving algorithm choice; algorithm choice driving trading speed) that lead to different correct estimators for the same observed slippage numbers. The same apparatus is extended to a multi-algorithm A/B-testing setting with an 'algorithm switch' and an 'algorithm acceleration' counterfactual, each mapped to a specific back-door (or sequential back-door) control-variable set, and to a discussion of the variance trade-off between using scarce interventional (experimental) data versus abundant observational (historical) data to estimate these effects.

Finally, the chapter presents causal regularization as an extension of standard predictive regularization (ridge/lasso, train/test splitting, rolling cross-validation), citing Janzing (2019) for the formal correspondence between finite-sample overfitting bias and confounding bias, and illustrating with a linear-model example that confounding bias, unlike overfitting bias, does not vanish as sample size grows. No empirical dataset is analyzed; all illustrations use hypothetical numbers or symbolic model parameters, and the chapter ends with reader exercises (including a simulation exercise for causal regularization) rather than reported results.

## Results

- In the worked trading example, the aggressive execution algorithm has 5 bps better overall arrival slippage than the passive algorithm, but underperforms the passive algorithm by 5 bps for small orders and by 15 bps for large orders, illustrating Simpson's paradox.
- Whether the aggregate or the size-conditioned slippage comparison is the correct one depends on the causal graph: if order size causes algorithm assignment, the size-conditioned comparison is correct; if the algorithm itself causes its own order size, the aggregate comparison is correct.
- For the algorithm-switch and algorithm-acceleration counterfactuals in a multi-algorithm trading example, controlling for order size (and, sequentially, trading speed) is shown to correctly identify each counterfactual via the back-door and sequential back-door criteria.
- A worked rule of thumb states that if order size determines algorithm choice 95% of the time, a stated multiple of observational data (relative to interventional data) is needed to estimate an algorithm's advantage with equivalent statistical confidence.
- A linear-model example shows that, in the presence of a confounding variable, the least-squares estimator's bias does not vanish as the sample size grows to infinity, unlike ordinary finite-sample overfitting bias.
- Causal regularization, calibrated on bias-free interventional data, is presented as achieving lower bias than an estimator fit purely on observational data and lower variance than an estimator fit purely on interventional data.

## Limitations

- Reader note: the chapter is entirely theoretical/pedagogical; there is no real trading dataset, backtest, or empirical performance result, only stylized worked examples and end-of-chapter exercises.
- The causal-regularization argument explicitly rests on a stated idealized generating model for the confounding term (cited from Janzing 2019), and the authors of that cited result caution against quoting the claim without its strong assumptions.
- The chapter itself notes that a companion method (Rothenhäusler et al., 2021) is needed for the case where no bias-free interventional data is available at all, a case this chapter does not itself resolve.
- Reader note: no author name, book title, or publication venue appears in the converted excerpt; the markdown begins mid-book at Chapter 5 (page 197) with unresolved cross-references to Chapters 1, 3, 6, and 7 that are not included in this file.

## Related

- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/causal-inference|causal inference]]

## Citation

not stated (2023). An Introduction to the Mathematics of Causal Inference.

DOI: 10.1201/9781003316923-5

Text ingested: `markdown_output/webster-2023-introduction-mathematics-causal-inference.md`, converted from `raw/ofi-event-clock/webster-2023-introduction-mathematics-causal-inference.pdf`.

Coverage of this summary: Read the entire chapter markdown: the introduction and pedagogical example, the technical primer on causal structures and do-calculus, Simpson's paradox applied to a trading example, the identifiability/back-door/front-door section, the A/B-testing and causal-regularization sections, the chapter's own summary of results, and the end-of-chapter exercises.

Known problems with the input: year from file metadata; No author name, book title, or publication venue appears in the converted excerpt; only the chapter text, page numbers, and a DOI (10.1201/9781003316923-5) are present, so authors and venue are marked not stated rather than inferred.
<!-- AUTHORED REGION END -->