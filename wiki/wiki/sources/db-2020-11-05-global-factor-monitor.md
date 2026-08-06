---
title: Global Factor Monitor (Quantitative Musing, 5 November 2020)
page_id: sources/db-2020-11-05-global-factor-monitor
page_type: source
source_path: markdown_output/d3ea8aa0_0a10_11eb_b600_309433ce0310_604.md
source_type: sell-side-research
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Andreas Farmakas
- Vivek Anand
- Jose Gonzalez
- Rong Leng
- Caio Natividade
- Gianpaolo Tomasi
- Ganchi Zhang
- Blaz Zlicar
year: 2020
venue: Deutsche Bank Research — Quantitative Musing (Europe/Global Quantitative Strategy)
tags:
- factor-monitoring
- risk-premia
- factor-valuation
- sell-side-research
- deutsche-bank
sources: []
related:
- entities/deutsche-bank
- concepts/factor-timing
- concepts/style-premia
- concepts/trend-following
- concepts/cross-asset-rotation
- concepts/value-premium
- concepts/risk-premia
mind_map_priority: low
schema_version: 2
uuid: 9de81a76-b3a0-5b0e-a328-f9fa2ab22e28
content_hash: sha256:bd3fb03d8cb3429d09a0a603e85398db4fbfa746724afccbf1e6f0860901469c
---

<!-- AUTHORED REGION START -->
# Global Factor Monitor

**Published: 5 November 2020** · Deutsche Bank Research, Europe and Global
Quantitative Strategy · *Quantitative Musing* series · Deutsche Bank AG/London

**Author:** Andreas Farmakas. Research team: Vivek Anand, Andreas Farmakas,
Jose Gonzalez, Rong Leng, Caio Natividade, Gianpaolo Tomasi, Ganchi Zhang,
Blaz Zlicar.

A monthly performance monitor for the desk's alternative risk premia strategies,
covering October 2020. This is commercial house research with a stated house
view — a different evidentiary standing from a peer-reviewed paper, and a note
whose value is almost entirely tied to its date. See
[[entities/deutsche-bank|Deutsche Bank]] for how the archive is framed here.

## What the Month Looked Like

Cash equity factors underperformed and moved together: they gained in the first
half of October as markets rallied, then gave it all back when sentiment turned.
Value declined separately, since growth outperformed for most of the month.
N-LASR, the desk's machine-learning stock selection model, dropped about 2%, with
balance sheet and efficiency alphas the only positive contributors.

Cross-asset was mixed. Trend rose about 1% — gains in rates and commodities
offsetting losses in equities and FX — while carry fell about 1%. In FX, value
gained 1.1% and momentum 0.6%, while carry lost 0.7%. Ahead of the US
presidential election, MXN was the best and TRY the worst performing currency,
with the dollar declining.

## The Factor Focus: Valuation Spreads

The substantive part of the note. Factor valuation is defined as the spread in
median book-to-price between a strategy's long and short legs, converted to a
60-month rolling z-score to strip out structural bias — value always screens
cheap, quality always expensive. Cheap and expensive regimes are z-scores above
+1.5 and below -1.5.

The finding is a warning about [[concepts/factor-timing|factor timing]]: the
academically supported relationship — cheap value spreads predict value
outperformance — held **pre-2016 and inverted after**. Value spent recent years
screening cheap while underperforming. Momentum and low beta both showed better
risk-adjusted performance when cheap.

## The House View, As Of That Date

DB economists saw a 3.7% US contraction for the year (revised from 4% at the
start of October), an 8% Euro Area contraction, and 2% Chinese growth. Rates
strategists projected 10-year Treasury yields at 0.7 by year end, 0.95 by June
2021 and 1.15 by December 2021, against 0.88 at end-October. These are forecasts
made before the vaccine announcements later that month, and should be read as a
record of what the desk thought, not as evidence about what happened.

## Open Questions

- The post-2016 inversion of the value spread signal is asserted from the desk's
  own subsample split. Has it since reverted?
- Regime definitions at +/-1.5 sd over a 60-month window are choices, not
  results.

## See Also

[[entities/deutsche-bank|Deutsche Bank]] ·
[[concepts/style-premia|Style Premia]] ·
[[concepts/value-premium|Value Premium]] ·
[[concepts/trend-following|Trend Following]] ·
[[sources/db-2020-04-23-return-of-the-machines|Return of the Machines (April 2020)]]
documents the N-LASR model tracked here.

**Not yet written:** `factor-valuation-spreads`, `n-lasr-model`,
`alternative-risk-premia`, `fx-carry`, `book-to-price`.
<!-- AUTHORED REGION END -->

