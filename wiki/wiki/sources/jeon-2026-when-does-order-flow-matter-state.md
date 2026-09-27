---
authors:
- Joohyoung Jeon
content_hash: sha256:e980312b1bec6214ef479e2c92062a5b775c83525ead1e00dd11b197fad627b4
created: 2026-09-27 01:47:00+00:00
page_id: sources/jeon-2026-when-does-order-flow-matter-state
page_type: source
related:
- concepts/order-flow
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/bid-ask-spread
- concepts/order-flow-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:45cc094c6275d4a9b780f6b3ba0e201a4f08596584bf26494169c8209b02220d
source_path: markdown_output/jeon-2026-when-does-order-flow-matter-state.md
source_type: paper
tags:
- crypto-futures
- limit-order-book
- order-flow
- liquidity-regime
- macro-events
- out-of-sample-validation
- gradient-boosting
- clock-calendar
- asset-crypto
- harvest-relevant
title: When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions
  in Crypto Futures
updated: '2026-09-27T01:47:00Z'
uuid: 821dea4f-e0a9-5e64-8d08-4578c20b0036
year: 2026
---

<!-- AUTHORED REGION START -->
# When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures

## Summary

The paper asks, within windows around scheduled macroeconomic announcements, whether the persistent pre-event limit-order-book liquidity state, richer continuous order-book features, nonlinear book shape, or local order flow is the first-order predictor of the discrete post-event liquidity regime (calm, mixed, or stressed) -- as distinct from predicting price direction or detecting a latent regime.

Using top-20-level order book snapshots sampled once per minute and pre-event trade-flow summaries for Binance BTCUSDT and ETHUSDT futures, matched to a calendar of scheduled macro announcements, the authors define a discrete liquidity state from relative spread, depth and imbalance and pose a supervised one-step transition task from the pre-event to the post-event state. They compare a fixed staged sequence of models -- a marginal baseline, a coarse pre-event-state Markov baseline, linear (multinomial and ordered) logits over continuous L2 features, a shallow nonlinear gradient-boosted model over L2 shape, and that model augmented with order flow -- under rolling-month out-of-sample folds, event-clustered bootstrap uncertainty, and permutation-test controls, admitting each layer only if it improves on the layer below it.

The coarse pre-event liquidity state is a strong first-order predictor of the post-event regime, and a linear model over the same continuous features fails to improve on it, while a shallow nonlinear model over L2 shape adds a further gain of comparable size. Local order flow adds a further, smaller gain only when layered on the nonlinear L2 model, and this order-flow contribution is not uniform: it is present across all liquidity regimes for ETH and grows with pre-event stress, but is not established for BTC in either regime-conditional or pooled tests.

What is new is treating the pre-event liquidity state, rather than the event label itself, as the object to beat, and building a staged, layer-by-layer evaluation protocol -- with event-clustered resampling and feature-shuffle permutation nulls -- that credits an added feature only with what it contributes beyond the layer below it; the authors propose this protocol as a baseline that future reinforcement-learning, execution-policy, or language-model context layers should be required to exceed.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The order book is sampled once per minute (top-20 levels per side); each scheduled macro-announcement time t defines a pre-event window from 5 minutes before t up to t, and a post-event window from t up to a horizon h of 1 minute or 5 minutes later, with same-country releases within 60 seconds merged into a single window. The prediction target is the post-event liquidity-state label (calm, mixed or stressed), built from spread, depth and imbalance aggregated over the post-event window, predicted only from features aggregated over the pre-event window.

## Data

- **Asset class:** Crypto
- **Instruments:** BTCUSDT and ETHUSDT perpetual futures on Binance (47,513 evaluation windows per horizon: 18,631 event windows [BTC 9,330, ETH 9,301] and 28,882 matched non-event windows, drawn from 9,773 scheduled macro events across 40 monthly folds)
- **Venue:** Binance
- **Period:** January 2023 through mid-2026, with scored event windows spanning February 2023 to May 2026
- **Granularity:** Top-20-level order book snapshots sampled once per minute, plus aggregated pre-event trade-flow summaries, evaluated over rolling monthly out-of-sample folds

## Features and Measures

- **L2 liquidity state (calm/mixed/stressed).** A discrete three-level regime label built from relative bid-ask spread, total top-20 depth (negated so a thinner book counts as less liquid) and top-20 order-book imbalance, each converted to a training-fold-only tercile and combined by counting how many of the three fall in their worst tercile, capped at two.
- **Coarse pre-event state baseline.** An empirical conditional Markov transition model that predicts the post-event liquidity state from only the symbol, horizon, and pre-event calm/mixed/stressed state, so it already carries pre-event-state persistence.
- **Nonlinear L2-shape model.** A shallow, depth-capped gradient-boosted classifier (maximum depth three, sixty boosting rounds, learning rate 0.05, L2 regularization 1.0) over multi-scale summary descriptors of spread, depth, imbalance and mid-price dynamics from the pre-event book.
- **Order-flow overlay.** Pre-event trade-flow features -- signed taker volume and imbalance, trade counts, quantity, VWAP and returns -- added on top of the L2-shape model to test whether local order flow adds incremental predictive value.

## Method

Five models are compared in a fixed staged sequence on the same held-out panel: a marginal class-frequency baseline, a coarse pre-event-state Markov baseline, a multinomial logit (and an ordered-logit variant) over continuous L2 features, a shallow gradient-boosted nonlinear model over L2-shape descriptors, and that nonlinear model further augmented with order-flow features. Evaluation uses rolling whole-month out-of-sample folds, training on earlier months and scoring a held-out later month, with all thresholds, including the liquidity-state terciles, fit on training folds only. Models are scored by the joint average of the improvement in negative log-likelihood and Brier score over the layer below, with uncertainty from a cluster bootstrap that resamples whole scheduled events rather than individual minutes. A permutation test shuffles only the features under examination within month, symbol and pre-event-state blocks (with a variant that also blocks on UTC hour, to rule out an hour-of-day proxy) to check that an improvement is not an artifact of a flexible model fitting noise, and a Benjamini-Hochberg correction is applied across symbol-horizon-regime cells at q=0.05 for the regime-conditional order-flow tests.

## Results

- The coarse pre-event calm/mixed/stressed state improves on the marginal baseline by 0.034 at the one-minute horizon and 0.045 at five minutes, beating the marginal model on about two-thirds of held-out rows.
- Replacing the coarse state with a multinomial logit over the same continuous L2 features performs worse, not better: -0.048 at one minute and -0.034 at five minutes (ordered logit: -0.052 and -0.047), with confidence intervals entirely below zero.
- A shallow nonlinear gradient-boosted model over L2-shape descriptors improves on the coarse-state baseline by 0.044 at one minute and 0.060 at five minutes, with the gain present separately for BTC (0.037 and 0.052) and ETH (0.052 and 0.067) at the two horizons.
- The nonlinear L2-shape model classifies the three-class post-event regime with accuracy 0.586 at one minute and 0.554 at five minutes, against majority base rates of 0.571 and 0.532.
- Adding order-flow features to the L2-shape model gives a pooled improvement of 0.010 at both horizons, above the flow-shuffle null's 95th percentile of 0.004 (one minute) and 0.003 (five minutes).
- The order-flow gain is ETH-dominant: for ETH it is 0.020 (one minute) and 0.016 (five minutes), both clearing their null, while for BTC it is 0.001 and 0.003, at or below the corresponding null, so no order-flow contribution is established for BTC.
- For ETH the order-flow increment over the L2-only model rises with pre-event stress, from 0.004 (calm) to 0.020 (mixed) to 0.038 (stressed) at one minute, and 0.004, 0.015 and 0.030 at five minutes.
- The coarse pre-event-state baseline already carries a stressed-to-stressed persistence probability of up to 0.456, which underlies its predictive strength.

## Limitations

- The study covers only two assets (BTCUSDT and ETHUSDT), so the BTC/ETH order-flow asymmetry is a two-point observation rather than a population finding.
- The one-minute snapshot cadence cannot recover queue position, own-order fill probability, sub-second market-order impact, or a replay-grade execution simulator.
- The paper reports no trading, execution, or profit result; it is a prediction study of liquidity-state transitions only.
- Order-flow features are local trade-flow summaries rather than a full order-by-order reconstruction, so the BTC non-result concerns these specific tests rather than proving BTC order flow is uninformative.

## Related

- [[concepts/order-flow|order flow]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-flow-prediction|order flow prediction]]

## Citation

Joohyoung Jeon (2026). When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures.

DOI: 10.48550/arxiv.2607.09230

Text ingested: `markdown_output/jeon-2026-when-does-order-flow-matter-state.md`, converted from `raw/ofi-event-clock/jeon-2026-when-does-order-flow-matter-state.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, related work, data and prediction task, evaluation protocol, all results subsections, and discussion/conclusion.

Known problems with the input: No explicit publication year is printed on the paper itself; year taken from the job file's year_hint (2026), consistent with the paper's own 2023-2026 sample window and cited 2026 references; year from file metadata.
<!-- AUTHORED REGION END -->