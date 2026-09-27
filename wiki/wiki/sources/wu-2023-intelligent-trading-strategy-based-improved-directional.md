---
authors:
- Bing Wu
- Xiangzu Han
content_hash: sha256:7849c9c1e978accce7fe9c77b7d7f7b85a085bbf83f8e2439b6793164a9115f7
created: 2026-09-27 01:47:00+00:00
page_id: sources/wu-2023-intelligent-trading-strategy-based-improved-directional
page_type: source
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:a220b5e0a0f9245c46a2a71950e7956ad29a507c48ca5e66d53ae57dd46971a0
source_path: markdown_output/wu-2023-intelligent-trading-strategy-based-improved-directional.md
source_type: paper
tags:
- directional-change
- hidden-markov-model
- regime-detection
- forex
- tick-data
- bayesian-optimization
- trading-strategy
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Intelligent trading strategy based on improved directional change and regime
  change detection
updated: '2026-09-27T01:47:00Z'
uuid: 6687dca1-b010-5ecc-b041-335c1706f3d0
year: 2023
---

<!-- AUTHORED REGION START -->
# Intelligent trading strategy based on improved directional change and regime change detection

## Summary

The paper asks whether a Directional Change (DC) trading strategy can be made more adaptive by no longer treating upward and downward price trends with the same fixed threshold, and by giving the strategy a way to sit out abnormal market conditions. Traditional DC records a price event only once price has moved by a preset threshold from the last extreme, but earlier work applied one threshold symmetrically to both trend directions and set it manually.

The authors introduce a decay coefficient that rescales the downtrend threshold relative to the uptrend threshold, then use Bayesian Optimization to jointly tune this coefficient and the base threshold from data rather than by hand. On top of this improved DC (IDC), they feed the resulting return indicator into a two-state hidden Markov model (RCD-HMM), trained with the Baum-Welch/EM algorithm and decoded with the Viterbi algorithm, to flag the market as being in a normal or an abnormal regime. A resulting Intelligent Trading Algorithm (ITA) only takes DC-based buy and sell signals while the market is judged normal.

Across eight forex currency pairs and roughly two years of tick data, ITA produced the highest cumulative return and, in most cases, the lowest maximum drawdown among the methods tested, and nonparametric statistical tests ranked it first for both metrics. Ablation comparisons show the Bayesian-optimized decay coefficient (IDC) improves on a single Bayesian-optimized threshold, and that adding the regime filter on top of IDC further speeds up profit accumulation without increasing drawdown.

What is new is treating the uptrend and downtrend DC thresholds asymmetrically via a jointly optimized decay coefficient, and coupling a DC-derived indicator to a hidden Markov regime filter that suspends trading during abnormal periods, rather than only adjusting the threshold itself.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Price movements are sampled with the Directional Change (DC) paradigm: an event is confirmed only when price has moved by a threshold $\theta$ from the last extreme point in the uptrend, or by a rescaled threshold $\alpha \cdot \theta$ (using a decay coefficient $\alpha$) in the downtrend, rather than being sampled at fixed time intervals. The optimal $(\theta, \alpha)$ pair is found on a training window by Bayesian Optimization and then applied to a subsequent testing window in a rolling two-month sliding window with one-month stride. Trading decisions (buy, sell, or suspend) are generated at each DC confirmation point using rules based on how far price has moved from the running trend extreme, gated by whether a hidden Markov model classifies the current regime as normal or abnormal.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** Eight currency pairs: EUR/GBP, EUR/USD, EUR/JPY, CHF/JPY, EUR/CHF, USD/CHF, USD/JPY, USD/CAD
- **Venue:** not stated
- **Period:** January 1, 2019 to October 31, 2020
- **Granularity:** Tick data (average of bid and ask price), processed with a sliding window of two months and a one-month stride, split 1:1 into training and testing within each window.

## Features and Measures

- **Improved Directional Change (IDC).** A version of Directional Change that applies a separate, decay-coefficient-scaled threshold to downtrends and optimizes both the base threshold and the decay coefficient jointly rather than fixing them manually.
- **Decay coefficient (alpha).** A multiplier applied to the uptrend threshold to obtain a distinct downtrend threshold, reflecting that up and down price moves can have different characteristic magnitudes.
- **RDC indicator.** The return measured between two adjacent Directional Change extreme points, computed using the optimized threshold; used as the input sequence to the regime-detection model.
- **RCD-HMM.** A two-hidden-state hidden Markov model, trained on the RDC indicator sequence, that classifies each point in time as belonging to a normal or an abnormal market regime.

## Method

The threshold pair $(\theta, \alpha)$ is optimized on training data using the Bayesian Optimization Algorithm, searching $\theta$ over [0.0003, 0.003] and $\alpha$ over [0.1, 1] for 100 iterations. The resulting RDC return-indicator sequence is used to train a two-hidden-state hidden Markov model via the Baum-Welch (Expectation-Maximization) algorithm, with the Viterbi algorithm used at test time to decode the most likely regime path. The Intelligent Trading Algorithm (ITA) generates buy and sell signals from simple rules comparing the current price to the running trend extreme and the optimized thresholds, but only acts on those signals when the HMM reports a normal regime; capital management is simplified to an all-in, all-out rule with a starting stake of 10,000 euros and no transaction costs. Performance is judged by Cumulative Return Rate (CRR) and Maximum Drawdown (MDD), and ITA is compared against three benchmarks of increasing sophistication: a fixed-threshold strategy (FT) tested at eight preset thresholds, a Bayesian-optimized single-threshold strategy (OPT_T), and IDC alone without the regime filter. Differences across the four methods are tested for significance with the nonparametric Friedman test and Conover post-hoc comparisons.

## Results

- ITA's average return across the eight currency pairs was 58.76%, versus -24.36% for the fixed-threshold benchmark FT, -10.47% for the single-optimized-threshold benchmark OPT_T, and 16.89% for IDC alone.
- ITA's average maximum drawdown was 3.53%, lower than FT's 19.08%, OPT_T's 13.30%, and IDC's 7.93%.
- ITA's maximum drawdown was lower than FT's for every currency pair except EUR/GBP.
- Friedman and Conover nonparametric tests ranked ITA first among the four methods for both return and maximum drawdown at the 0.05 significance level.
- Adding the decay-coefficient and Bayesian optimization (IDC) improved average monthly return over a single optimized threshold (OPT_T) on every currency pair, for example 1.52% versus -0.51% on EUR/GBP.
- IDC's standard deviation of monthly returns exceeded OPT_T's on five of the eight currency pairs, indicating higher volatility alongside higher average returns.
- Adding the RCD-HMM regime filter on top of IDC produced faster cumulative profit growth on every currency pair while keeping or lowering maximum drawdown.
- The optimal (theta, alpha) pair for EUR/GBP varied substantially across months in the sample, for example theta of 0.0003 in April 2019 versus 0.0030 in August 2019.

## Limitations

- Transaction costs were disregarded in all experiments.
- Short selling was not allowed and an all-in, all-out capital allocation rule was assumed, simplifying position sizing relative to a live strategy.
- History is assumed to repeat and market liquidity is assumed sufficient to execute the strategy; both are stated as simplifying assumptions rather than tested.
- Reader note: results are shown only for eight forex pairs over roughly a two-year window, so generalization to other asset classes or longer horizons is not demonstrated.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/backtesting|backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Bing Wu, Xiangzu Han (2023). Intelligent trading strategy based on improved directional change and regime change detection.

DOI: 10.48550/arxiv.2309.15383

Text ingested: `markdown_output/wu-2023-intelligent-trading-strategy-based-improved-directional.md`, converted from `raw/ofi-event-clock/wu-2023-intelligent-trading-strategy-based-improved-directional.pdf`.

Coverage of this summary: Read the full paper end to end, including the abstract, DC background and related-work sections, the methodology, all result tables and figures, the ablation experiments, and the conclusion.

Known problems with the input: The preprint footer reads 'Preprint submitted to Journal of LaTeX Templates', which is a known Elsevier-template placeholder rather than a real venue name; venue is recorded as not stated rather than using that placeholder text; Table 6 in the markdown is rendered as an omitted picture with an OCR-garbled text block; its numeric content was not used.
<!-- AUTHORED REGION END -->