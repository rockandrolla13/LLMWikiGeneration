---
title: Expected Shortfall
page_id: concepts/expected-shortfall
page_type: concept
revision_id: 1
created: 2026-05-21 12:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- risk-management
- tail-risk
- basel-frtb
- coherent-risk-measure
sources:
- sources/barendse-2026-efficient-tail-interquantile
related: []
mind_map_priority: medium
schema_version: 2
uuid: ea0578aa-be46-5efb-aa2e-ed73a3ef73a0
content_hash: sha256:c6a46c85dc1583d9fccccb82e35b6272623e776c34f77f9f4857b70a6654a99f
---

<!-- AUTHORED REGION START -->
# Expected Shortfall

**Expected Shortfall (ES)** is a coherent tail-risk measure equal to the conditional mean of losses beyond a specified quantile (VaR). Required under Basel III FRTB and a focus of joint VaR-ES elicitability research.

## Why ES Is Hard to Backtest

ES is **not elicitable**: there is no loss function it alone minimises. [[sources/wang-2022-e-backtesting|Wang, Wang & Ziegel]] prove the e-value analogue of that obstruction — no backtest e-statistic exists from ES information alone, because ES is monotone, uncapped and not quasi-convex.

The way round it is joint elicitability. ES and [[concepts/value-at-risk|VaR]] form a Bayes pair under the loss $L(z,x)=z+(x-z)_+/(1-p)$, so carrying the VaR forecast as auxiliary information makes a valid backtest possible. The resulting statistic is monotone in the right direction: over-reporting ES lowers the evidence against you, so prudence is rewarded.

## Sources

- [[sources/barendse-2026-efficient-tail-interquantile|Efficiently Weighted Estimation of Tail and Interquantile Expectations (2026)]] — central; left-tail expectation is ES, the canonical case for the proposed efficient weighted estimator
- [[sources/wang-2022-e-backtesting|E-backtesting (2022)]] — anytime-valid backtesting of ES forecasts

## Related Concepts

[[concepts/value-at-risk|Value-at-Risk]] · [[concepts/backtesting|Backtesting]] · [[concepts/e-process|E-process]]

<!-- AUTHORED REGION END -->
