---
authors:
- Prakul Sunil Hiremath
- Vruksha Arun Hiremath
content_hash: sha256:e5959c52997702107484c5471339c5cef16278a873fe9f16f5966fe0f7e9ff2a
created: 2026-09-27 01:47:00+00:00
page_id: sources/hiremath-2026-early-detection-latent-microstructure-regimes-limit
page_type: source
related:
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-flow-imbalance
- concepts/bid-ask-spread
- concepts/adverse-selection
- concepts/informed-trading
- concepts/high-frequency-trading
- concepts/liquidity-risk
revision_id: 1
schema_version: 2
source_hash: sha256:7496378b7f251f6c73c34cf47b83bab6362962cb07dcf957d322de29238dfe33
source_path: markdown_output/hiremath-2026-early-detection-latent-microstructure-regimes-limit.md
source_type: paper
tags:
- limit-order-book
- market-microstructure
- change-point-detection
- liquidity-stress
- hidden-markov-model
- early-warning-signal
- cryptocurrency
- order-book-depth
- clock-calendar
- asset-crypto
- harvest-relevant
title: Early Detection of Latent Microstructure Regimes in Limit Order Books
updated: '2026-09-27T01:47:00Z'
uuid: 6c96f705-e095-5638-992b-bdc99e9662a0
year: 2026
---

<!-- AUTHORED REGION START -->
# Early Detection of Latent Microstructure Regimes in Limit Order Books

## Summary

The paper asks whether limit order book stress is truly abrupt or is preceded by a latent deterioration phase that current early-warning signals cannot exploit, since order flow imbalance and short-term volatility only respond once stress is already underway. It builds a three-regime hidden Markov model of the order book (stable, latent build-up, stress) with a causal transition structure, proves that the hidden regime sequence is identifiable from temporal drift, and derives two guarantees relating a drift-to-noise ratio and the build-up duration to expected lead-time and to the probability of detecting before stress onset. A companion proposition also derives a trade-off between how early a detector can fire and what share of stress events it can still cover.

On top of the theory, the authors build a trigger-based detector that combines four channels (HMM regime-posterior entropy, order-book depth erosion, bid-ask spread drift, and order-flow momentum) using a MAX rule rather than a sum, adds a rising-edge condition so the trigger fires at the onset of an increase rather than at its peak, and recalibrates its threshold online from the running distribution of the composite score. It is benchmarked against CUSUM, Bayesian online change-point detection, HMM posterior thresholding, and simple imbalance/volatility threshold rules.

Across 200 simulation runs of the proposed causal data-generating process, the detector achieves a positive mean lead-time with near-perfect precision, while missing about 46% of stress events; the misses are concentrated in short build-up, high-noise conditions exactly where the theory predicts detection should fail. Depth erosion and HMM entropy are the channels that fire first in almost all early detections. A one-week, five-event illustrative application to real BTC/USDT order book data shows the same qualitative pattern: positive lead-time and high precision and coverage for the proposed detector, and negative lead-times for the reactive baselines.

What is new relative to an earlier version of this argument (as the authors describe it) is a complete proof that closes the gap between a concentration bound on a CUSUM partial sum and the actual stopping-time guarantee, via an explicit coupling lemma; a formal lead-time-versus-coverage trade-off bound; and a conditional breakdown showing that the detector's missed-detection rate is a structural consequence of the drift-to-noise regime rather than a tuning failure.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

In the simulation study, observations occur at abstract discrete timesteps (200 independent runs of 3000 timesteps each) with no real-time unit attached. In the real-data application, raw Binance order-book updates (about 100 ms resolution) are aggregated into fixed 1-second bins over one week of BTC/USDT data, with features z-scored on a strictly causal rolling 30-minute window and an intraday seasonality adjustment. The prediction horizon (lead-time) is the number of timesteps, or seconds in the real-data case, between the detector's trigger and the onset of a stress episode, where stress onset in the simulation is the simulated regime label and in real data is the first time the bid-ask spread exceeds three times its rolling 10-minute median for at least 30 seconds.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC/USDT on Binance for the real-data application; a synthetic order-book feature process with three regimes (stable, latent build-up, stress) for the simulation study.
- **Venue:** Binance public order book WebSocket feed (real data); no venue for the simulated data.
- **Period:** One week of BTC/USDT data for the real-data application (specific calendar dates not stated); 200 independent simulation runs of 3000 timesteps each for the simulation study.
- **Granularity:** Real data resampled into 1-second bins from an approximately 100 ms update feed; simulation uses discrete abstract timesteps.

## Features and Measures

- **HMM entropy.** The entropy of the filtered posterior over hidden regimes from a fitted Gaussian hidden Markov model, used to measure ambiguity between the stable and build-up regimes.
- **Depth erosion.** A signal that measures a sustained, monotone decline in total quoted order-book depth relative to a rolling baseline depth over a lookback window.
- **Spread drift.** A signal that measures drift in the bid-ask spread normalised by the rolling standard deviation of spread changes.
- **Order flow momentum.** A signal that measures persistence of signed order flow imbalance over a rolling window.
- **MAX aggregation.** A composite instability score formed by taking the maximum, rather than the sum or a learned weighted combination, of the four channel signals, justified when only a subset of channels carries signal in a given episode and the channels are weakly correlated in the stable regime.
- **Rising-edge trigger.** A trigger condition that requires the composite score to be above an adaptive threshold and still increasing, so that detection occurs at the onset of a score climb rather than at its peak, with a minimum spacing imposed between consecutive triggers.
- **Adaptive threshold.** A detection threshold recalibrated online as a target percentile of the empirical distribution of the composite score, so the detector stays well-calibrated under distributional shift across sessions.

## Method

The authors model the limit order book as driven by a hidden three-state Markov chain (stable, latent build-up, stress) with a causal transition structure that disallows returning directly from stress to build-up, and an observation model in which the build-up regime carries a persistent linear drift on top of Gaussian noise. They prove the hidden regime sequence is identifiable from this temporal drift, then use CUSUM stopping-time theory to derive a sufficient drift-to-noise condition for positive expected lead-time and a closed-form lower bound on the probability of detecting before stress onset, including a coupling lemma that connects a partial-sum concentration bound to the actual stopping-time guarantee, plus a separate bound on the trade-off between lead-time and coverage.

The detector itself fits a Gaussian HMM to filter the regime posterior, builds four channel signals (HMM entropy, depth erosion, spread drift, order-flow momentum), aggregates them with a MAX rule, applies a rising-edge condition with a minimum trigger spacing, and recalibrates its threshold from the running empirical distribution of the composite score.

Performance is judged by mean lead-time (the gap between the detector's trigger and the stress onset), precision (the share of triggers that are early, matched detections), and coverage (the share of stress events detected early), benchmarked against CUSUM, Bayesian online change-point detection, HMM posterior thresholding, and simple imbalance and volatility threshold rules, across 200 simulation runs and, separately, a preliminary evaluation on one week of 1-second BTC/USDT order book data with five labelled stress events defined from a spread-widening rule.

## Results

- Across 200 simulation runs, the adaptive trigger achieves mean lead-time 18.6 timesteps (95% CI width 3.2), precision 1.00, and coverage 0.54, while the imbalance and volatility baselines show negative mean lead-times of 4.2 and 6.8 timesteps respectively.
- CUSUM and BOCPD achieve small positive mean lead-times (2.1 and 1.4 timesteps) but much lower precision (0.43 and 0.39), reflecting frequent false alarms in stable periods.
- The overall 46% missed-detection rate is concentrated in low signal-to-noise, short build-up episodes, where conditional coverage falls as low as 0.03, rising to 0.98 in high signal-to-noise, long build-up episodes.
- Depth erosion is the first-firing channel in 55.5% of early detections and HMM entropy in 44.4%; spread drift and order-flow momentum never fire first, though they are said to add robustness under noise.
- Ablations show removing the rising-edge condition drops precision from 1.00 to 0.71, and replacing the MAX rule with a SUM rule drops coverage from 0.54 to 0.38.
- Across a 9-cell grid of noise level and build-up delay, lead-time is strictly positive in 8 of 9 configurations, with the one exception matching the theoretical condition for a drift-to-noise violation.
- In one week of 1-second BTC/USDT order book data with 5 labelled stress events, the detector achieves mean lead-time 38 seconds (standard deviation 21), precision 1.00, and coverage 0.80, with zero false alarms, while the imbalance and volatility baselines show negative lead-times of 8 and 14 seconds.

## Limitations

- The real-data evaluation covers only 5 labelled stress events over a single week, which the authors say is too small a sample to support reliable statistical conclusions.
- The stress-event label used for real data is a spread-widening proxy and can miss stress episodes that show up only as depth collapse without spread widening.
- The probability bound (Proposition 2) is derived under linear drift and Gaussian noise and may be loose or inaccurate under real market conditions.
- The MAX aggregation is justified under an assumption of weakly correlated channels in the stable regime, which the authors note may not hold in real order books where depth and spread are structurally correlated.
- Reader note: the real-data test uses a single instrument (BTC/USDT) on a single venue over a single week, so how the method generalises to other assets, venues, or longer periods is untested here.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/liquidity-risk|liquidity risk]]

## Citation

Prakul Sunil Hiremath, Vruksha Arun Hiremath (2026). Early Detection of Latent Microstructure Regimes in Limit Order Books.

DOI: 10.48550/arxiv.2604.20949

Text ingested: `markdown_output/hiremath-2026-early-detection-latent-microstructure-regimes-limit.md`, converted from `raw/ofi-event-clock/hiremath-2026-early-detection-latent-microstructure-regimes-limit.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction, related work, the regime model and identifiability section, the trigger-based detection methodology, the baselines, the full empirical results (simulation and BTC/USDT real-data application), the lead-time/coverage trade-off section, the economic interpretation, the conclusion, and the appendix proofs.

Known problems with the input: No journal, conference, or working-paper series is printed on the document; it appears to be a preprint with code and data hosted on GitHub and Zenodo, so venue is recorded as empty; The converted markdown replaces most equations and figures with omitted-picture placeholders and garbled OCR text (e.g. broken LaTeX symbols), so some formal statements were read from the surrounding prose description rather than the equation itself.
<!-- AUTHORED REGION END -->