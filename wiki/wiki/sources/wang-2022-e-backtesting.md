---
title: E-backtesting
page_id: sources/wang-2022-e-backtesting
page_type: source
source_path: markdown_output/wang-2022-e-backtesting.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Qiuqi Wang
- Ruodu Wang
- Johanna Ziegel
year: 2022
venue: Management Science (2025); arXiv:2209.00991v6, 16 April 2026
tags:
- e-value
- e-process
- backtesting
- expected-shortfall
- value-at-risk
- risk-management
- basel
- anytime-valid
sources: []
related:
- concepts/e-value
- concepts/e-process
- concepts/anytime-valid-inference
- concepts/testing-by-betting
- concepts/backtesting
- concepts/expected-shortfall
- concepts/value-at-risk
- entities/qiuqi-wang
- entities/ruodu-wang
- entities/johanna-ziegel
mind_map_priority: high
schema_version: 2
uuid: 391d56f4-cd4c-5fb3-96bf-b49fcc51dd91
content_hash: sha256:3b63febea3d64bb01719a1f0a5bb3ab5681edada4d2e7922e3f8f35141f1aa18
---

<!-- AUTHORED REGION START -->
# E-backtesting

**Authors:** [[entities/qiuqi-wang|Qiuqi Wang]], [[entities/ruodu-wang|Ruodu Wang]], [[entities/johanna-ziegel|Johanna Ziegel]]

**Year:** 2022 · **Venue:** Management Science (2025). The version read here is arXiv:2209.00991v6, dated 16 April 2026.

## Summary

Basel replaced Value-at-Risk with [[concepts/expected-shortfall|Expected Shortfall]] as the standard market-risk measure, and ES is much harder to backtest than VaR. This paper builds a backtest that is model-free, valid at any sample size, and valid at any stopping time: a regulator can watch the statistic continuously and act the moment it crosses a threshold, without the usual penalty for looking repeatedly.

The mechanism is betting. Each day the forecast is turned into a bet against the bank's reported risk number. If the forecasts are honest the bet is fair, so wealth cannot systematically grow. Wealth that grows large is evidence against the forecasts, and the wealth level *is* the test statistic.

## Why ES is the hard case

The paper states the problem plainly: ES is not elicitable (Gneiting, 2011), so backtesting it is substantially harder than VaR. Proposition 3 gives the e-value analogue of that obstruction: ES admits **no** backtest e-statistic from ES information alone, because ES is monotone, uncapped and not quasi-convex. The fix is to carry the VaR forecast as auxiliary information, using the fact that the pair (ES, VaR) is jointly elicitable — the Fissler–Ziegel "Bayes pair" — with loss
\[
L(z,x) = z + \frac{(x-z)_+}{1-p}.
\]

## Construction

A **backtest e-statistic** is a function $e(x,r,z)$ whose expectation is at most 1 whenever the reported risk $r$ is at least the true risk, and exceeds 1 when the true risk exceeds the report. For ES at level $p$, with $x$ the realised loss, $r$ the ES forecast and $z$ the VaR forecast,
\[
e^{ES}_p(x,r,z)=\frac{L(z,x)-z}{r-z}=\frac{(x-z)_+/(1-p)}{r-z},
\]
with the conventions $0/0=1$, $1/0=\infty$, and $e=\infty$ if $r<z$. Theorem 1 shows this is *monotone*: over-reporting ES lowers the e-value, so prudence is rewarded and only under-forecasting is punished. The corresponding VaR e-statistic is equation (1) of the paper; the converter dropped it as an image, so it is not restated here.

These are then compounded into a wealth process,
\[
M_0=1,\qquad M_t(\lambda)=\prod_{s\le t}\bigl(1-\lambda_s+\lambda_s X_s\bigr),
\qquad X_s=e(L_s,r_s,z_s),
\]
with $\lambda_s\in[0,1]$ chosen in advance of each period. The paper's own reading: all capital is invested each step, split between a random payoff $X_t$ and a fixed payoff 1, and $\lambda_t<1$ means keeping part of the money in your pocket. Ville's inequality gives the guarantee
\[
\mathbb{P}\Bigl(\sup_t M_t \ge 1/\alpha\Bigr)\le \alpha .
\]
Four betting rules are studied: GRO (an oracle), GREE, GREL, and GREM, the average of GREE and GREL, which is the one used in the empirical work. Theorems 4 and 5 show these e-statistics are essentially the only choices: any one-sided e-statistic for VaR, and any increasing one for the (ES, VaR) pair, is dominated by them.

## What it buys over a classical backtest

- Validity at **any** stopping time, so continuous monitoring is legitimate.
- No parametric assumption, no assumed forecast structure, no fixed sample size, no asymptotics. The paper's Table 1 shows it as the only method with "no" in every one of those columns.
- A multi-zone alert scheme with thresholds 2, 5 and 10, mirroring Basel's three-zone approach.
- One-sided by construction: it punishes under-forecasting only.

The stated cost: against a correctly specified model with a fixed sample size, a model-based test is more powerful.

## Results

**Simulation.** AR(1)–GARCH(1,1) with skewed-$t$ innovations ($\nu=5$, $\gamma=1.5$), 1,000 runs of 500 trading days, rolling window 500, GREM. With ES under-reported by 10% at level 0.975 and threshold 10, detection rates are 98.5% (normal innovations), 77.1% ($t$), 6.2% (skewed-$t$) and 3.6% (true model). For exactly correct forecasts the type-I error at threshold 10 is 0.2%. Early warnings at threshold 2 arrive after roughly a quarter of the sample and decisive ones at threshold 10 after about half; for the normal case, 89, 137 and 176 days for thresholds 2, 5 and 10.

**NASDAQ Composite**, negated percentage log-returns, 16 January 1996 to 31 December 2021, backtest sample 5,536 days, reported over 3 January 2005 to 31 December 2021. Average ES(0.975) forecasts: normal 2.676, $t$ 2.997, skewed-$t$ 3.202, skewed-$t$ plus 10% 3.522, empirical 3.656. Days to detection under GREM at thresholds 2/5/10: normal 540/610/713; $t$ 540/933/1381; skewed-$t$ 540/2639/2889; empirical 756/862/931. The deliberately conservative skewed-$t$ plus 10% forecast is never detected, which is the monotonicity property working as intended. Most detections cluster 500–700 trading days after January 2005, around the financial crisis losses.

**Portfolio.** 22 stocks, 5 January 2001 to 31 December 2021, mean–variance weights with per-stock AR(1)–GARCH(1,1). Average ES(0.975): normal 2.817, $t$ 3.191, skewed-$t$ 3.304.

**Against a parametric monitor.** Compared with Hoga & Demetrescu (2023) for structural change, the parametric method wins; GREE, GREL and GREM detect roughly 0 to 30 days later.

**Gaming.** A bank that over-reports and then under-reports is handled by a rolling window of, for example, 250 or 500 days.

## Why It Matters

This is the paper in this cluster closest to practical risk work. The object being tested is a forecast sequence, not a model, so it applies to any risk forecast however produced. The anytime-valid property is what makes continuous monitoring honest: with a classical test, checking every day and stopping at the first rejection inflates the error rate; here it does not.

## See Also

[[concepts/e-value|E-value]] · [[concepts/e-process|E-process]] · [[concepts/anytime-valid-inference|Anytime-Valid Inference]] · [[concepts/testing-by-betting|Testing by Betting]] · [[concepts/backtesting|Backtesting]] · [[concepts/expected-shortfall|Expected Shortfall]] · [[concepts/value-at-risk|Value-at-Risk]]

**Not yet written:** `concepts/elicitability`, `concepts/ville-inequality`.
<!-- AUTHORED REGION END -->
