---
title: Online monotone density estimation and log-optimal calibration
page_id: sources/hore-2026-monotone-density-calibration
page_type: source
source_path: markdown_output/hore-2026-monotone-density-calibration.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Rohan Hore
- Ruodu Wang
- Aaditya Ramdas
year: 2026
venue: Working paper, arXiv:2602.08927 (25 May 2026)
tags:
- calibrator
- e-process
- online-learning
- grenander
- changepoint-detection
sources: []
related:
- concepts/e-process
- concepts/e-value
- concepts/anytime-valid-inference
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: b3cf461a-c966-5ea6-b661-5b8b136d7cd6
content_hash: sha256:cc4bbc081857dda5a63c38807d31c971ccf665b1ed0cf340dddad580c218a1e9
---

<!-- AUTHORED REGION START -->
# Online Monotone Density Estimation and Log-optimal Calibration

**Authors:** Rohan Hore, [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2026 · **Venue:** Working paper, arXiv:2602.08927

## Summary

The paper's organising observation: **an admissible p-to-e calibrator is exactly a decreasing density on $[0,1]$**. So choosing the best calibrator online, as p-values stream in, is literally the problem of estimating a monotone density online. Two classical-looking algorithms then solve a testing problem.

## Construction

Given sequential p-values, pick a calibrator $h_t$ from the past and form
\[
M_t=\prod_{s=1}^{t} h_s(P_s),
\]
a nonnegative supermartingale under the null, so Ville's inequality makes thresholding at $1/\alpha$ a valid sequential test whatever the stopping rule.

Two ways to choose $h_t$:
- **Online Grenander**: the constrained maximum-likelihood monotone density fitted to the p-values seen so far.
- **Expert aggregation**: a weighted mixture over a finite set of monotone densities, weights proportional to accumulated likelihood.

The oracle benchmark is the calibrator maximising expected log value, which under an IID alternative is the alternative's own density — hence the equivalence with density estimation.

## Results

Both algorithms have excess Kullback–Leibler risk of order $n^{1/3}$, which is essentially optimal given the $n^{-1/3}$ minimax rate for offline monotone density estimation, and expert aggregation additionally has pathwise regret of order $\sqrt{n\log n}$ that holds distribution-free. Both are asymptotically log-optimal, and when the alternative differs from uniform the wealth diverges almost surely, so the test stops in finite time.

In experiments the two adapt to different situations: after a change point, expert aggregation adapts faster while the Grenander estimator is held back by pre-change data. Against fixed calibrators, which are strongly signal-dependent — one wins for large shifts, another for small ones — both adaptive methods are robust across the range.

## Why It Matters

It removes a tuning decision. Rather than picking a calibrator and hoping it matches the signal strength, you learn it from the data while keeping validity at every stopping time.

## See Also

[[concepts/e-process|E-process]] · [[concepts/e-value|E-value]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]]

Supplies the online Grenander calibrator used by [[sources/su-2026-llm-watermark-eprocesses|the LLM watermark detector]]; cites [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]] for admissible calibrators.

**Not yet written:** `entities/rohan-hore`.
<!-- AUTHORED REGION END -->
