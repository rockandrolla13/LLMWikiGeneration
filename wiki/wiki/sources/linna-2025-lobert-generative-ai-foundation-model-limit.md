---
authors:
- Eljas Linna
- Kestutis Baltakys
- Alexandros Iosifidis
- Juho Kanniainen
content_hash: sha256:32ac875ac1546ef54d2b873da6cbb980bd048b76c9f7b3dcfabc71ac998847b5
created: 2026-09-27 01:47:00+00:00
page_id: sources/linna-2025-lobert-generative-ai-foundation-model-limit
page_type: source
publication_venue: NeurIPS Conference
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/transformers
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
- concepts/order-flow-prediction
- concepts/market-microstructure
- concepts/order-flow
- entities/alexandros-iosifidis
- entities/juho-kanniainen
revision_id: 1
schema_version: 2
source_hash: sha256:7e88a5bc980017f037b81775d7a07f5a5cea2b3461864dc1062f743a9e1aef41
source_path: markdown_output/linna-2025-lobert-generative-ai-foundation-model-limit.md
source_type: paper
tags:
- limit-order-book
- transformer
- foundation-model
- tokenization
- mid-price-prediction
- bert
- high-frequency-trading
- clock-event
- asset-equity
- harvest-core
title: 'LOBERT: Generative AI Foundation Model for Limit Order Book Messages'
updated: '2026-09-27T01:47:00Z'
uuid: 652bac48-86b3-5982-b89a-6d63f0931c61
year: 2025
---

<!-- AUTHORED REGION START -->
# LOBERT: Generative AI Foundation Model for Limit Order Book Messages

## Summary

The paper asks whether a transformer built directly on the stream of individual limit order book messages, rather than on snapshot-style Level II features, can learn a reusable representation of market microstructure. The authors adapt BERT's encoder-only, masked-reconstruction training scheme to this message stream, building LOBERT: a model that turns each incoming order book message (side, type, price and volume) into a single token, augmented with continuous representations of price, volume and time so that rare precise values are not lost to coarse binning.

LOBERT combines a discrete vocabulary of common message shapes with three parallel regression heads for price, volume and time difference, and a rotary attention mechanism adapted to run on cumulative elapsed time rather than sequence position, so irregular gaps between messages are represented directly. Training proceeds in two stages: a masked-message-modeling pretraining phase that also masks the accompanying order book snapshots to stop the model reading the answer off nearby context, followed by task-specific fine-tuning for next-message prediction and for classifying the direction of future mid-price moves.

On Nasdaq ITCH message data for four large-cap stocks, LOBERT predicts the discrete components of the next message substantially more accurately than a reconstructed prior autoregressive model, and its combined discrete-plus-continuous inference scheme reproduces the true distribution of price, volume and time changes more closely than using either channel alone. For mid-price direction, LOBERT matches or beats a retrained DeepLOB baseline across three message-based horizons, and its accuracy on the predictions it is confident enough to make rises sharply as the confidence threshold is tightened.

The main novelty the authors claim is treating a whole message as one token instead of splitting it into many sub-tokens, which shortens the sequence a model must process and speeds up training relative to prior generative order-flow models, at the cost of somewhat slower inference than a smaller convolutional baseline.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are individual limit order book messages (new orders, edits, deletions, executions, hidden orders), each turned into one token with an accompanying order book snapshot taken immediately after the message. For next-message prediction the model reconstructs the single next message in sequence. For mid-price prediction the target is the direction of the average tick-normalized mid-price over a forward window of 10, 50 or 100 messages, so the prediction horizon is defined in message counts rather than clock time.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL, INTC, MSFT and FB (Nasdaq-listed stocks)
- **Venue:** Nasdaq ITCH feed
- **Period:** 2015.05.11 to 2015.09.30, comprising 80 training days ending 2015.09.01, 10 validation days from 2015.09.02 to 2015.09.16, and 10 test days from 2015.09.17 to 2015.09.30
- **Granularity:** Message level (Level III order flow); about 470M messages split into 919k non-overlapping sequences of 512 messages each; message-arrival time differences are only available at millisecond resolution in these experiments

## Features and Measures

- **one-token-per-message tokenizer.** Packs each order book message's side, type, and coarsely quantized price and volume into a single discrete token, instead of the many sub-tokens per message used by earlier generative order-flow models.
- **Piecewise Linear-Geometric Scaling (PLGS).** A continuous value transform that grows linearly for small, common values and compresses large, rare ones geometrically toward a bound, applied to price differences, volumes and inter-message time gaps alongside their discrete tokens.
- **continuous-time rotary attention.** A version of rotary position embeddings driven by cumulative elapsed time instead of token position, letting self-attention reflect the true irregular spacing between messages.
- **Masked Message Modeling (MMM).** A pretraining objective, adapted from masked language modeling, that hides random messages and their surrounding order book snapshots and trains the encoder to reconstruct them.
- **Combined discrete-continuous inference.** An inference scheme that uses the predicted message token's quantization bin to bound the corresponding continuous regression output, blending categorical and continuous predictions for price, volume and time.

## Method

LOBERT is an encoder-only transformer whose embedding layer merges four inputs: discrete message tokens, continuous price-difference values, continuous volume values, and an optional gated representation of the order book snapshot after the message. Learned positional embeddings are combined with the continuous rotary attention described above. Output heads consist of a token-classification head trained with cross-entropy loss and three regression heads (price, volume, time difference) trained with weighted mean-squared-error losses, with the regression heads also taking the token head's logits as input so continuous predictions can draw on the discrete prediction.

Training first pretrains the encoder bidirectionally with Masked Message Modeling, then fine-tunes it, using a causal (triangular) attention mask, on two downstream tasks: predicting the next message and classifying the direction of the future mid-price. Optimization uses AdamW with cosine-annealing-with-warm-restarts scheduling.

Next-message prediction is judged by per-component and full-message token accuracy against a reconstructed prior state-space model (referred to as S5) trained on the same data, and by comparing the marginal distributions of predicted versus true price, volume and time values using Wasserstein-1 distance, Jensen-Shannon divergence and total variation distance. Mid-price prediction is judged with macro-F1 under selective prediction, where a prediction is only issued once the model's maximum softmax probability clears a confidence threshold, against a retrained DeepLOB baseline.

## Results

- LOBERT predicts the full next message correctly 26.4% of the time (27.8% with the order book snapshot module), versus 6.1% for the reconstructed S5 baseline.
- Per-component next-message accuracy for LOBERT is higher than S5 across the board: message type 60.6% vs 50.8%, side/direction 65.1% vs 52.2%, quantized price 51.8% vs 18.6%, and quantized volume 72.1% vs 32.1%.
- LOBERT's predicted value distributions correlate with the true test-set distributions with Pearson correlations of 0.55 for price, 0.37 for volume and 0.52 for time difference.
- Combining the token head and the continuous regressors at inference (the Combined mode) gives the lowest distributional discrepancy to ground truth for price, volume and time difference, for example a price Wasserstein-1 distance of 10.04 versus 15.44 for token-only and 10.85 for regressor-only decoding.
- For mid-price direction at a 100-message horizon, LOBERT's macro-F1 on the predictions it is confident enough to make rises from 0.55 to 0.88 as the confidence threshold is raised from 0.3 to 0.9, while the share of cases it is willing to predict on falls from 1.00 to 0.10.
- LOBERT matches or outperforms a retrained DeepLOB baseline across the tested horizons and confidence thresholds for mid-price direction.
- On a single V100 GPU, LOBERT runs at 281.87 predictions per second, 47% of DeepLOB's throughput, i.e. about 53% slower than DeepLOB at batch size 1.

## Limitations

- The authors state the current experiments do not establish whether LOBERT can generate realistic long sequences of future messages.
- The authors state they have not yet completed a broader study of the range of downstream tasks LOBERT can be fine-tuned for.
- The authors note LOBERT does not model individual order identities, so it may struggle to track a specific resting order's size and position as prices move, and that the transformer architecture's computational cost and inference latency are non-trivial, currently slower than the DeepLOB baseline.
- Reader note: time differences in these experiments are only available at millisecond rather than nanosecond resolution, so timing precision is coarser than the underlying exchange feed.
- Reader note: results are reported on four large-cap Nasdaq stocks over a few months of 2015, so generalization to other periods, venues or asset classes is untested.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/transformers|transformers]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow|order flow]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]
- [[entities/juho-kanniainen|Juho Kanniainen]]

## Citation

Eljas Linna, Kestutis Baltakys, Alexandros Iosifidis, Juho Kanniainen (2025). LOBERT: Generative AI Foundation Model for Limit Order Book Messages. NeurIPS Conference.

DOI: 10.48550/arxiv.2511.12563

Text ingested: `markdown_output/linna-2025-lobert-generative-ai-foundation-model-limit.md`, converted from `raw/ofi-event-clock/linna-2025-lobert-generative-ai-foundation-model-limit.pdf`.

Coverage of this summary: Read the full markdown file, including abstract, introduction, methodology (sections 2.1-2.4), experiments and results (sections 3.1-3.3), discussion/conclusion, and appendices A-F.

Known problems with the input: No publication year is printed in the body; year taken from the job file's year_hint of 2025; The venue field reproduces the literal text 'NeurIPS Conference' that appears in the page footer; it is unclear whether this confirms an actual accepted venue or is a template artifact, so treat it as unconfirmed; The markdown replaces several equations and figures with picture placeholders (e.g. PLGS formulas, mid-price label definition, RoPE-related figures), so those exact mathematical forms could not be extracted from text.
<!-- AUTHORED REGION END -->