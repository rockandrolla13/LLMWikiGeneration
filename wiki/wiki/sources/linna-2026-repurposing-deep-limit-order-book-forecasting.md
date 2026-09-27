---
authors:
- Eljas Linna
- Kestutis Baltakys
- Derrick Manoharan
- Alexandros Iosifidis
- Juho Kanniainen
content_hash: sha256:ebe222e980cf53cef3bc32e948058bdd7774a9d5ce2663c3e25b625b6dede978
created: 2026-09-27 01:47:00+00:00
page_id: sources/linna-2026-repurposing-deep-limit-order-book-forecasting
page_type: source
publication_venue: Association for the Advancement of Artificial Intelligence (AAAI)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow-prediction
- concepts/transformers
- concepts/price-impact
- concepts/market-microstructure
- concepts/deep-learning-for-finance
- entities/alexandros-iosifidis
- entities/juho-kanniainen
revision_id: 1
schema_version: 2
source_hash: sha256:6259fd0b52aefa80c5c9da0e97bf42afad3bf5f719adc58d2a5cf5180f5fc7e2
source_path: markdown_output/linna-2026-repurposing-deep-limit-order-book-forecasting.md
source_type: paper
tags:
- limit-order-book
- market-impact
- transformer-models
- counterfactual-analysis
- deep-learning
- market-microstructure
- clock-event
- asset-equity
- harvest-relevant
title: Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market
  Impact Modeling
updated: '2026-09-27T01:47:00Z'
uuid: e53d61ba-466e-5ee7-8abf-35111c59b3f7
year: 2027
---

<!-- AUTHORED REGION START -->
# Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling

## Summary

The paper asks whether a deep limit order book (LOB) forecaster trained only to predict prices can also be used, without retraining, to estimate how a specific counterfactual order-book message (a new order, cancellation, deletion, or execution) would move the market, and whether that model-implied response lines up with real market behavior.

The authors build a model-agnostic scenario-injection framework: mechanically valid synthetic LOB messages of a chosen type, side, price level, and intensity are appended to the end of a real message sequence, the pretrained Transformer forecaster (LOBERT) is re-run on the extended sequence, and the change in its predicted mid-price distribution is taken as the 'model-implied counterfactual market impact.' This is validated four ways: against paired treated/untreated trajectories from an agent-based LOB simulator; against matched real historical events sharing the scenario's characteristics; against internal microstructure-consistency checks (bid/ask symmetry, depth monotonicity, placebo scenarios); and with a sequence-level regression testing whether the estimated impact adds predictive value for realized returns beyond the scenario type and the pre-event forecast.

The model's scenario rankings correlate strongly with both simulator-implied impact and historical realized outcomes, and it reproduces expected microstructure patterns such as mirror-symmetric bid/ask responses, smaller impact deeper in the book, and a small placebo response; the main exception is full deletion of the best price level, which behaves qualitatively differently. The estimated impact also adds a small but statistically significant amount of predictive information for realized returns beyond the scenario label and the pre-event forecast.

What is new is converting a passive deep LOB forecaster into a scenario-conditioned market-impact estimator through message injection, and validating it jointly against simulation, matched real events, and internal consistency checks, without needing to retrain the model or impose an explicit response/decay function as classical impact models do.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Sequences are built from raw LOBSTER-format message streams (order submissions, cancellations, deletions, executions); the forecaster looks back over a fixed window of 512 messages and predicts, over the next 100 messages, whether the average mid-price will be higher, lower, or about the same as the reference mid-price at the end of the input sequence, using a 1-tick movement threshold. For scenario analysis, synthetic messages are appended after the observed sequence and the prediction horizon begins immediately after the injected messages.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL, AMD, AMZN, ASML, GOOG, MSFT, PLTR
- **Venue:** Nasdaq (L3 message data converted to LOBSTER format)
- **Period:** training: October 1, 2025-January 16, 2026; validation: January 20-30, 2026; held-out test: February 2-13, 2026
- **Granularity:** message-level (L3) LOB events; the training, validation, and test periods contain 795M, 99M, and 156M messages respectively

## Features and Measures

- **Model-implied counterfactual market impact.** The change in a trained forecaster's predicted mid-price distribution or direction after injecting a mechanically valid synthetic message scenario into an otherwise unchanged historical sequence.
- **Directional impact measure.** The change in the forecaster's expected directional score (down/flat/up) between the scenario-conditioned and original predictions, averaged over the sequences eligible for a scenario.
- **Jensen-Shannon divergence impact measure.** A symmetric, sign-free measure of how much a scenario changes the forecaster's entire predicted probability distribution, complementing the directional measure.
- **Scenario families.** Parameterized synthetic interventions (execution, level-1/level-2 deletion, level-1/level-2 new order, new best-price order, level-1/level-2 transient add-then-delete, and a deep placebo order), each run at three volume intensities and on both book sides.

## Method

The base forecaster is LOBERT, a Transformer trained to classify mid-price direction over a 100-message horizon from 512-message input windows. Counterfactual scenarios are injected as mechanically valid synthetic LOBSTER messages appended to real sequences, with the model's context window extended so treated and untreated sequences see equally long history. Validation combines: paired treated/untreated trajectories from an agent-based simulator (500 runs per scenario), scored with Spearman correlation and sign agreement; comparison of average predicted versus realized directionality on matched real historical events; comparison of artificial-injection responses to the model's response around matching natural events; and three nested linear regressions (scenario identity only, plus pre-event forecast, plus estimated directional impact) fitted on a validation period and evaluated out-of-sample on a held-out test period, with asset-day clustered bootstrap confidence intervals throughout. Robustness is checked across 10 independently initialized model instances and via leave-one-asset-out comparisons.

## Results

- Against the controlled agent-based simulator, the model- and simulator-implied impacts had a Spearman correlation of 0.76 and 94.4% sign agreement across 36 non-neutral scenarios.
- Against 9.8M matched historical events across 36 non-neutral scenario groups, predicted and realized directionality had a Spearman correlation of 0.99 and 97.2% sign agreement.
- Artificial-injection responses matched the model's response to corresponding natural events with a Spearman correlation of 0.953, 100% sign agreement across 37 non-neutral groups, and a normalized mean absolute error of 12.4%.
- In an out-of-sample sequence-level regression, adding the estimated directional impact on top of the pre-event forecast changed test MAE by -0.00231 and R2 by 0.000254, and a confirmatory test-period regression gave a positive impact coefficient of 1.796 with a 95% confidence interval of [0.978, 2.613].
- Executions produced the largest average directional impact (about 0.13 at 25% and 50% intensity, falling to about 0.10 when a full level was consumed), consistent with impact not scaling proportionally with order size; full deletion of the best price level was the main exception to otherwise regular intensity patterns, weakening or reversing the directional estimate while its Jensen-Shannon divergence roughly doubled.
- Bid- and ask-side responses were nearly mirror symmetric (Spearman correlation 0.995, normalized asymmetry 0.051, 100% opposite-sign agreement), and impact decreased with book depth in 8 of 9 side-specific comparisons.
- Scenario rankings were stable across a leave-one-asset-out test (median Spearman correlation 0.991, 100% directional agreement) and across 10 independently initialized model instances (median pairwise correlation 0.982, 100% directional agreement).
- The underlying LOBERT forecaster achieved an F1 score of 47.7%, a balanced accuracy of 47.2%, and a negative log-likelihood loss of 1.012 on its base mid-price direction task.

## Limitations

- The authors state the measure is 'model-implied' impact, not an identified causal effect: simulator validation depends on the simulator's realism, and historical events provide no observable untreated counterfactual for the same moment.
- Findings are limited to one studied architecture (LOBERT), one prediction horizon (100 messages), seven Nasdaq equities, and about a five-month period, so absolute impact magnitudes may need recalibration elsewhere.
- The incremental predictive gain from the estimated impact over the pre-event forecast, while statistically significant, is described by the authors as small.
- Reader note: all seven test assets are US large-cap technology-sector equities, so generalization to other sectors, venues, or asset classes is untested here.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/transformers|transformers]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]
- [[entities/juho-kanniainen|Juho Kanniainen]]

## Citation

Eljas Linna, Kestutis Baltakys, Derrick Manoharan, Alexandros Iosifidis, Juho Kanniainen (2027). Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling. Association for the Advancement of Artificial Intelligence (AAAI).

DOI: 10.48550/arxiv.2609.16930

Text ingested: `markdown_output/linna-2026-repurposing-deep-limit-order-book-forecasting.md`, converted from `raw/ofi-event-clock/linna-2026-repurposing-deep-limit-order-book-forecasting.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, background, the full methods section (problem formulation, scenario injection, impact measures), the experimental setup, all results subsections, and the discussion/conclusion.

Known problems with the input: The paper's own copyright line prints the year 2027 (AAAI copyright notice), which is later than the job file's year_hint of 2026; the printed year was used as instructed.
<!-- AUTHORED REGION END -->