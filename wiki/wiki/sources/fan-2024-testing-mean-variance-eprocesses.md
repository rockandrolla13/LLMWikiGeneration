---
title: Testing the mean and variance by e-processes
page_id: sources/fan-2024-testing-mean-variance-eprocesses
page_type: source
source_path: markdown_output/fan-2024-testing-mean-variance-eprocesses.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Yixuan Fan
- Zhanyi Jiao
- Ruodu Wang
year: 2024
venue: Biometrika (2024)
tags:
- e-process
- anytime-valid
- variance-testing
- nonparametric
- risk-management
sources: []
related:
- concepts/e-process
- concepts/anytime-valid-inference
- concepts/testing-by-betting
- entities/ruodu-wang
mind_map_priority: high
schema_version: 2
uuid: 042b4ce4-5d0f-52f4-8436-942550d1916d
content_hash: sha256:22bcccb04723db3c1e248652ce285ea4b49c2c2c13f3fda753b9fe07589494bc
---

<!-- AUTHORED REGION START -->
# Testing the Mean and Variance by E-processes

**Authors:** Yixuan Fan, Zhanyi Jiao, [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2024 · **Venue:** Biometrika

## Summary

Test, for sequentially arriving and possibly dependent data, whether the conditional mean stays below $\mu$ **and** the conditional variance below $\sigma^2$. No parametric model, no fixed sample size, and valid at any stopping time.

## Why the variance is the hard half

The paper is explicit that the two halves are not symmetric. Testing whether a mean is at least $\mu$ mirrors testing whether it is at most $\mu$; no such mirror exists for the variance.

Shape assumptions also help the two unequally. Relative to the baseline hypothesis, symmetry improves the e-variable by a factor of 2, while unimodality buys it **nothing at all** — even though unimodality does improve the corresponding p-variable. Knowing the variance exactly, rather than as an upper bound, yields no more powerful one-sided statistic either.

## Construction

With $E_0=(X-\mu)_+^2/\sigma^2$, the precise per-observation e-variables are $E_0$ for the baseline hypothesis, $2E_0$ under symmetry, $E_0$ again under unimodality, and $2E_0$ under both. These compound into the e-process
\[
M_t=\prod_{i=1}^{t}\bigl(1-\lambda_i+\lambda_i E_i\bigr),
\]
with each stake $\lambda_i$ chosen from the past. Ville's inequality gives $\mathbb{P}(\sup_t M_t\ge 1/\alpha)\le\alpha$, so you reject the first time the wealth crosses the threshold. Two stake rules are studied: an e-mixture averaging constant stakes, and e-GREE, which adapts from the realised e-values.

## Results

Against p-value combinations, the e-process methods dominate whenever the alternative departs in **variance** rather than mean, and they are the only ones valid under optional stopping. In one simulation with 100 observations and a threshold of 20, the e-mixture's rejection rate is 0.419 under the baseline hypothesis and 0.998 under symmetry, while Fisher's and Simes's p-value combinations reject essentially never.

The empirical study tests volatility forecasts on 20 S&P 500 stocks plus two real-estate names, estimating on 2001–2006 and testing from 2007. For Simon Property, e-GREE crosses thresholds 2, 5, 10 and 20 after 165, 224, 242 and 254 trading days. Technology, health care, consumer staples and utilities names were never rejected by the end of 2010 — the rejections concentrate in the sectors that actually broke.

## Why It Matters

This is the closest companion to [[sources/wang-2022-e-backtesting|E-backtesting]]: same betting machinery, but aimed at a conditional variance rather than a risk measure. For monitoring a volatility model in production, it is the more directly applicable of the two.

## See Also

[[concepts/e-process|E-process]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/testing-by-betting|Testing by Betting]]

**Not yet written:** `entities/zhanyi-jiao`.
<!-- AUTHORED REGION END -->
