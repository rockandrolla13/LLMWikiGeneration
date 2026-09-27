---
authors:
- Sukhman Balagan
content_hash: sha256:471bb39ce4627c91ac4a2bf26e4d88c5f18be7183aa485d20f2c0192ba90f26c
created: 2026-09-27 01:47:00+00:00
page_id: sources/balagan-2026-learning-polymarket-taker-trade-direction-chain
page_type: source
related:
- concepts/trade-clock
- concepts/order-flow-imbalance
- concepts/trade-classification
- concepts/informed-trading
- concepts/feature-engineering
- concepts/order-flow-prediction
- concepts/deep-learning-for-finance
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:5f85eb29cced88b8559c188a1c6354f3d3afc103b3994986c2cb0c5adc55a578
source_path: markdown_output/balagan-2026-learning-polymarket-taker-trade-direction-chain.md
source_type: paper
tags:
- trade-direction-classification
- prediction-markets
- polymarket
- gradient-boosted-trees
- order-flow-imbalance
- on-chain-data
- tick-rule
- clock-trade
- asset-crypto
- harvest-relevant
title: Learning Polymarket Taker Trade Direction from the On-Chain Tape
updated: '2026-09-27T01:47:00Z'
uuid: b1f7c1b9-6249-5953-a04c-c8ece4b2b1a7
year: 2026
---

<!-- AUTHORED REGION START -->
# Learning Polymarket Taker Trade Direction from the On-Chain Tape

## Summary

Classical trade-direction rules (the tick rule, bulk-volume classification) are known to perform near randomly on Polymarket, a decentralized on-chain prediction market, because its order flow shows positive direction autocorrelation and long same-price runs that violate the mean-reversion logic those rules assume; prior work (Qin and Yang, 2026) documents this failure and releases on-chain ground-truth direction labels but does not build a predictive model. This paper asks whether a learned classifier can recover taker trade direction from the trade tape alone, using the on-chain ground truth only for validation, and whether better-classified directions repair the downstream order-flow measures the classical rules distort.

On a single representative liquid month (June 2025), the author builds a fully causal, leakage-audited feature set from the trade tape (recent price level and price change, run-length/same-price structure, trade size, inter-trade timing, and maker concentration) and trains a gradient-boosted-tree (GBT) classifier and a 1D convolutional sequence model over trailing trade windows, comparing both against a price-bin-corrected tick rule baseline fit on the training period.

Both learned models substantially outperform the corrected tick rule, and the improvement holds across all price levels where the classical rule is price-dependent. A feature-subset ablation shows the gain comes from the recent magnitude and short-window trajectory of price changes, not from maker identity (which alone predicts at chance) or explicit run-length features. Substituting the classifiers' predicted directions into standard Order Flow Imbalance (OFI) and VPIN calculations recovers the ground-truth values markedly better than the classical rule does, and both classifiers are well calibrated. The author is explicit that these are single-month, relative findings, not a general full-panel accuracy claim.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Each observation is a single on-chain trade; the target is that trade's own true taker direction (buy/sell of event probability), and every predictor is computed causally, using only information available strictly at or before that trade (per-market series, in reconstructed chronological order), so the current trade's true direction is never an input. Rolling features summarize the 3, 5 and 10 most recent trades' price changes, and the CNN uses a trailing 32-trade window; the temporal train/test split is a single within-month global-timestamp cut at the earliest 70% of trades by block timestamp, so all training trades strictly precede all test trades and there is no fixed forward-looking prediction horizon beyond the current trade.

## Data

- **Asset class:** Crypto
- **Instruments:** Polymarket Standard Binary prediction-market contracts (excluding neg_risk and Up-Down markets and the two taker router/relayer addresses); 2,867 markets in training and 1,774 markets in the test period
- **Venue:** Polymarket, an on-chain (blockchain) decentralized prediction market; data from the public Polymarket-v1 Database (Qin and Yang, 2026, CC-BY-4.0)
- **Period:** single held-out month, June 2025, with an earliest-70%/latest-30% within-month split by block timestamp into training and test periods
- **Granularity:** individual on-chain trade records: 1,781,009 training trades and 763,287 test trades

## Features and Measures

- **Price level and recent price change.** The current normalized event-probability price and its recent change, plus rolling changes over the last 3, 5 and 10 trades (p_event, dp_event, roll_dp_3/5/10).
- **Run structure.** Features counting how long the price has stayed flat or moved in one direction (zero_tick_run, signed_dp_run, trades_since_price_change).
- **Trade size.** The trade's own dollar (USDC) size and rolling aggregates of recent trade sizes.
- **Inter-trade timing.** The time since the previous trade and a rolling mean of recent inter-trade times (dt_seconds, roll_mean_dt_5).
- **Maker concentration.** Features summarizing how concentrated recent trades are among a small set of makers (maker_cum_share, maker_is_top), included specifically to test for label leakage via counterparty identity.
- **Price-bin-corrected tick rule.** The classical tick rule (sign of the most recent price change), with its per-price-bin sign corrected using a flip map fit on the training period and held fixed on the test period; used as the paper's primary baseline.

## Method

Two classifiers are trained on the same causal, leakage-audited feature set: a gradient-boosted-tree model (LightGBM, 300 trees, learning rate 0.05, 63 leaves, seed 17) and a 1D convolutional sequence model over a 32-trade trailing window (two Conv1d layers, 48 channels, kernel size 5, masked pooling, seed 17). Both are compared against the price-bin-corrected tick rule on the same single within-month train/test split. All standard errors are computed by a market-clustered block bootstrap (resampling condition_id markets with replacement, 1,000 resamples, trade-weighted accuracy, seed 17), since trades within a market are not independent. A feature-subset ablation drops maker-concentration and run-structure features to test whether the classifier's accuracy is a proxy for maker identity. Predicted directions from each source are substituted into standard Order Flow Imbalance and VPIN (volume-bucketed, 1,000 USDC per bucket) calculations and compared, market by market, against the ground-truth versions of those metrics via Pearson and Spearman correlation, mean absolute error and signed bias. Classifier calibration is assessed via 12-bin reliability diagrams, expected calibration error (ECE) and Brier score.

## Results

- Overall test accuracy: corrected tick rule 0.6536, GBT 0.8175 (about 16.4 points higher), CNN 0.7941 (about 14.1 points higher), with market-clustered standard errors around 0.004.
- The GBT's accuracy advantage holds across all ten price deciles, ranging 0.75-0.86 versus 0.63-0.70 for the corrected tick rule in every decile.
- Maker-concentration features alone predict at essentially chance level (0.5052 accuracy); dropping maker features from the full model leaves accuracy essentially unchanged (0.8175 to 0.8179), as does dropping run-structure features (0.8175 to 0.8178).
- The GBT's highest-gain-importance features are the rolling and instantaneous price-change features (roll_dp_3, roll_dp_5, dp_event, p_event, roll_dp_10), ranked above size, timing, maker and category features.
- For downstream Order Flow Imbalance recovery, the GBT-based directions achieve a Pearson correlation of 0.684 with ground-truth OFI (versus 0.270 for the corrected tick rule) and near-zero bias (+0.003).
- For downstream VPIN recovery, the CNN-based directions achieve a Pearson correlation of 0.783 with ground-truth VPIN (versus 0.674 for the corrected tick rule).
- Both classifiers are well calibrated: the CNN has the lower expected calibration error (0.0161 versus 0.0260 for the GBT) while the GBT has the lower Brier score (0.1288 versus 0.1448 for the CNN).
- In this particular test month the price-bin correction fired on zero bins, so the corrected tick rule coincides with the raw (uncorrected) tick rule.

## Limitations

- Single-month scope: all results are from one liquid month (June 2025), and the roughly 0.82 GBT accuracy is month-specific, not a general accuracy figure.
- No full-panel absolute-accuracy claim is made: the paper does not reproduce the full roughly 202-million-trade Standard-Binary panel, and cites the near-random performance of classical rules on that full panel from Qin and Yang (2026) rather than reproducing it here.
- Within-second trade ordering on-chain is reconstructed using a deterministic tiebreaker, since the true intra-block (sub-second) sequence is not recoverable from the blockchain record.
- Calibration statistics (ECE, Brier score) are trade-level descriptive summaries only; since trades within a market are not independent, no per-trade IID standard error is attached to them.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/vpin|VPIN]]

## Citation

Sukhman Balagan (2026). Learning Polymarket Taker Trade Direction from the On-Chain Tape.

DOI: 10.5281/zenodo.21039811

Text ingested: `markdown_output/balagan-2026-learning-polymarket-taker-trade-direction-chain.md`, converted from `raw/ofi-event-clock/balagan-2026-learning-polymarket-taker-trade-direction-chain.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction, related work, data and filtering section, method (causal features, baseline, classifiers, temporal split, clustered evaluation), all results subsections (classification accuracy, leakage ablation, downstream OFI/VPIN recovery, calibration), limitations and conclusion.
<!-- AUTHORED REGION END -->