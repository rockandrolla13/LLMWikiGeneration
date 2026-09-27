---
authors:
- Elias Wurzer BSc
content_hash: sha256:8a2d3d27163d2cb8472ec462672c8fd2bda3a3421a4ebb74407cf4a483d9d7fd
created: 2026-09-27 01:47:00+00:00
page_id: sources/wurzer-2026-execution-alpha-intraday-liquidity-provision-versus
page_type: source
publication_venue: University of Innsbruck
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/fill-probability
- concepts/adverse-selection
- concepts/optimal-execution
- concepts/limit-order-book
- concepts/price-impact
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:95f574939e4bdd892f78ffb6e0accc1108adfd05c6fec4881fc35ba998ae29f0
source_path: markdown_output/wurzer-2026-execution-alpha-intraday-liquidity-provision-versus.md
source_type: paper
tags:
- execution-alpha
- closing-auction
- market-on-close
- order-flow-imbalance
- passive-liquidity-provision
- fill-modeling
- equity-microstructure
- risk-adjusted-performance
- clock-calendar
- asset-equity
- harvest-relevant
title: Execution Alpha of Intraday Liquidity Provision versus Market-on-Close in the
  S&P 500
updated: '2026-09-27T01:47:00Z'
uuid: 78e4d968-db91-5ae5-8caa-36a7b24d271f
year: 2026
---

<!-- AUTHORED REGION START -->
# Execution Alpha of Intraday Liquidity Provision versus Market-on-Close in the S&P 500

## Summary

This master's thesis asks whether a benchmark-sensitive trader can improve on Market-on-Close (MOC) execution by supplying liquidity with passive limit orders in the continuous book during the run-up to the close, routing any unfilled residual to MOC. It replays millisecond DTAQ trade-and-quote data for point-in-time S&P 500 constituents over 2018-2019, defining a side-signed 'net execution alpha' in basis points relative to the official closing print, decomposed into half-spread capture, an adverse-selection markout, and residual benchmark drift, net of maker rebates, fees, and a self-impact term. Four nested strategy families are compared at a 'small-parent' size of one percent of expected closing-auction volume: a static passive baseline (S1), a time/volatility-adaptive version (S2), signal-conditioned variants (S3) that add an order-flow-imbalance (OFI) signal and/or a public closing-imbalance proxy (IMB), and a learned time-of-day quantity schedule (S4).

The headline finding is that the most informationally rich strategy (S3-full) does not deliver a robust positive net alpha over MOC: the queue-aware replay simulation gives a small negative differential that is not statistically distinguishable from zero, and neither the OFI signal nor the IMB proxy adds pooled value once strategies are compared at matched realized fill rates. Risk-adjusted rankings (an information ratio and a risk-aversion-parametrized RAEAR statistic that price the strategy's tracking-error variance against the benchmark) do not overturn this conclusion, and performance deteriorates sharply once parent order size grows beyond the small-parent regime studied.

The thesis shows that this headline conclusion is highly sensitive to the assumed fill rule: a conservative 'strictly-through' tape-replay rule makes the strategy significantly negative versus MOC, an optimistic 'at-or-through' rule makes it significantly positive, and model-based survival specifications (Cox proportional hazards, XGBoost, Kaplan-Meier) produce much larger positive estimates because they lack the realized post-fill adverse-selection cost embedded in tape replay. Reading the realistic queue-aware rule as the reference case, the thesis concludes that public-data passive liquidity supply does not robustly beat MOC at this scale, though it need not reliably underperform either. Its methodological contributions are a transparent net-alpha decomposition framework, a nested-strategy design that isolates the marginal value of two public microstructure signal layers under matched fill rates, and the RAEAR statistic for ranking execution strategies once tracking-error risk aversion is priced in.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Placement decisions are refreshed on a fixed wall-clock cadence within a fixed pre-close calendar window (the primary Window B runs from 15:30 ET to the 15:50 ET MOC submission cutoff, with Windows A at 15:00 ET and C at 15:45 ET reported as robustness alternatives); the order-flow-imbalance and closing-imbalance-proxy signals are aggregated over trailing wall-clock windows refreshed at that same cadence. The evaluation horizon is not a fixed forward return but the distance to a fixed calendar event, the closing-auction print at time T_t: every strategy's net execution alpha, and any unfilled residual quantity, is measured and settled against that print.

## Data

- **Asset class:** Equities
- **Instruments:** Point-in-time S&P 500 constituent common stocks (large-cap, high-liquidity US equities), including documented index additions/removals and ticker-continuity cases.
- **Venue:** Consolidated US tape (NYSE/Nasdaq primary-listing closing auctions and consolidated NBBO)
- **Period:** Evaluation sample 2018-07-02 to 2019-12-31 (371 trading days, 187,309 symbol-days), with the first half of 2018 used as a separate, non-overlapping calibration sample.
- **Granularity:** Millisecond-timestamped consolidated Daily Trade and Quote (DTAQ) trade and NBBO records; simulated strategy decisions and signal updates are refreshed at a fixed short cadence within each execution window.

## Features and Measures

- **Net execution alpha.** A side-signed, basis-point gap between a strategy's quantity-weighted average execution price and the official closing print, decomposed into half-spread capture, an adverse-selection markout, and residual benchmark drift, net of maker rebates, fees, and a self-impact penalty.
- **Order-flow imbalance (OFI).** A rolling, causally standardized measure of net bid- versus ask-side quantity changes at the NBBO touch, following Cont et al. (2014), used to condition passive order placement on transient one-sided pressure.
- **Closing-imbalance proxy (IMB).** A public, pre-cutoff estimate of closing-auction order-flow pressure built from rolling order flow and the change in displayed best-depth imbalance, scaled by expected closing-auction volume, constructed as a substitute for the official (non-public) exchange auction-imbalance feed.
- **Queue-aware fill probability.** The realized or model-based probability that a resting passive limit order fills, generated either by replaying the trade tape and requiring at-limit prints to exhaust the displayed same-side queue, or, for robustness, by Cox proportional-hazards, XGBoost survival, and Kaplan-Meier models of the state vector (depth, spread, OFI, volatility, time-of-day).
- **Tracking-error variance and RAEAR.** The cross symbol-day variance of a strategy's net alpha, combined with its mean alpha into an information ratio and a risk-aversion-parametrized risk-adjusted execution alpha return (RAEAR), used to rank execution strategies once benchmark-tracking risk is priced.

## Method

The thesis formalizes execution performance in an implementation-shortfall style (following Perold, 1988), defining gross and net execution alpha relative to the official closing print and decomposing gross alpha into half-spread capture, a per-fill adverse-selection markout (following the spread-decomposition tradition of Glosten and Harris, 1988, and Huang and Stoll, 1997), and residual benchmark drift, with maker rebates, commissions, and a stylized Almgren-Chriss-style self-impact term layered on top. Fill probability is additionally modeled as a reduced-form Cox proportional-hazards specification, with an XGBoost-based survival specification and a Kaplan-Meier baseline as alternatives, calibrated on a held-out first-half-2018 pre-sample; the headline results, however, use a queue-aware replay of the realized DTAQ trade tape rather than the fitted model.

Seven placement-rule variants are compared: the MOC benchmark (S0), a static tier-based passive offset (S1), a time/volatility-adaptive offset (S2), three signal-conditioned S3 variants that add the OFI signal, the IMB proxy, or both to the S2 offset, and a learned time-of-day posting-quantity schedule (S4-TOD). Three pre-registered hypotheses are tested: H1 (net alpha gap of S3-full versus MOC), H2a/H2b (marginal contribution of OFI and IMB, tested via a matched-realized-fill-rate design against S2), and H3 (whether the strategy ranking survives tracking-error-variance penalization). Inference uses two-way (symbol-by-date) clustered standard errors, one-sided directional tests with Holm and false-discovery-rate multiplicity correction across the pooled H2 signal family, wild-cluster bootstrap p-values, and design-based minimum-detectable-effect diagnostics.

Robustness is assessed through a fill-specification bracket (strictly-through and at-or-through tape-replay bounds plus Cox, XGBoost, and Kaplan-Meier model-based fill probabilities, each checked for out-of-sample calibration via Brier score, ROC-AUC, and calibration error), a parent-order-size grid (0.5 to 10.0 percent of expected closing-auction volume), three arrival windows, an adverse-selection markout horizon grid, a buy/sell side-split check, and a rolling six-month within-sample stability diagnostic.

## Results

- The headline signal-conditioned strategy (S3-full) underperforms MOC by 0.117 basis points on average (t = 1.50, two-sided p = 0.135, one-sided p = 0.933), so the predicted positive execution-alpha gap over MOC is not supported by the queue-aware headline simulation.
- Neither the order-flow-imbalance signal nor the closing-imbalance proxy adds pooled positive alpha once compared at matched realized S2 fill rates; all pooled signal-family rows fail to reject after one-sided Holm adjustment.
- Risk-adjusted rankings do not overturn the mean-alpha conclusion: S3-full has a negative information ratio versus MOC, and the strategies' complete risk-adjusted ranking is preserved in only 46.9 percent of date-block-bootstrap replications.
- The sign of the headline result depends on the assumed fill rule: a conservative strictly-through replay gives -0.51 basis points (t = 6.18), the realistic queue-aware replay gives -0.12 basis points, and an optimistic at-or-through replay gives +0.18 basis points (t = 2.29), so the fill-rule bracket spans zero.
- Model-based survival fill specifications (Cox, Kaplan-Meier, XGBoost) give much larger positive net-alpha estimates (+2.74, +2.62, and +2.57 basis points respectively) but have near-zero realized adverse-selection markouts, marking them as optimistic bounds rather than tape-feasible estimates.
- Performance deteriorates sharply as parent order size grows past the headline scale: net alpha versus MOC is about flat at 0.5 and 1.0 percent of expected closing-auction volume, then falls to -1.28 basis points at 2.0 percent, -2.05 basis points at 5.0 percent, and -2.84 basis points at 10.0 percent.
- The widest-spread liquidity tier shows an individually significant negative gap versus MOC (-0.24 basis points, t = 2.33, p = 0.020) before multiplicity correction, but it survives only at the ten-percent level after Holm adjustment (p = 0.060).
- The closing auction accounted for about 10.1 percent of consolidated dollar volume (volume-weighted) over the sample, rising by roughly 1.51 percentage points per year, while the final pre-close half hour carried about 15.3 percent of daily dollar volume versus roughly 5.3 percent per mid-day half hour.

## Limitations

- Anchored to a small-parent regime (1.0 percent of expected closing-auction volume); a validated transition threshold into a large-parent regime is not estimated, only a diagnostic size grid.
- DTAQ NBBO data capture only the top of book, not full depth, hidden liquidity, or exact queue position, so the fill simulation relies on a modeled queue-priority assumption bracketed by strictly-through and at-or-through replay rules.
- The closing-imbalance proxy is built from public continuous-tape data rather than the official (non-public) exchange auction-imbalance feed, so it may understate the alpha available to a feed-connected trader.
- Point-in-time index membership relies on a single commercial vendor (Refinitiv) rather than a cross-validated source such as CRSP or official S&P records.
- The sample window (2018-2019) is a historically low-volatility period with a secular rise in closing-auction share; generalizability to higher-volatility regimes (e.g., the 2020 COVID shock) is not directly tested.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/fill-probability|fill probability]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/price-impact|price impact]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Elias Wurzer BSc (2026). Execution Alpha of Intraday Liquidity Provision versus Market-on-Close in the S&P 500. University of Innsbruck.

Text ingested: `markdown_output/wurzer-2026-execution-alpha-intraday-liquidity-provision-versus.md`, converted from `raw/ofi-event-clock/wurzer-2026-execution-alpha-intraday-liquidity-provision-versus.pdf`.

Coverage of this summary: Read the title/abstract page, Chapter 1 (introduction, scope, research question, contribution, structure), the full Chapter 3 theoretical framework (alpha decomposition, fill probability and state vector, adverse selection, OFI/IMB signal construction, strategy heuristics, tracking-error variance/RAEAR, inference), Chapter 4 hypothesis development, Chapter 5 data, Chapter 6 empirical methodology, the full Chapter 7 empirical results (H1, H2, H3, and all robustness subsections), and Chapter 8 conclusion including limitations and future work. Did not read Chapter 2's literature review in full, the references list, or the appendix in detail.
<!-- AUTHORED REGION END -->