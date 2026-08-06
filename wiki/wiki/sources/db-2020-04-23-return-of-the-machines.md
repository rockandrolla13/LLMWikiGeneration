---
title: The Return of the Machines (Quantcraft, 23 April 2020)
page_id: sources/db-2020-04-23-return-of-the-machines
page_type: source
source_path: markdown_output/2f08da6e_4c53_467d_a155_f0955e99b2a1_604.md
source_type: sell-side-research
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Gianpaolo Tomasi
- Vivek Anand
- Andreas Farmakas
- Jose Gonzalez
- Rong Leng
- Caio Natividade
- Ganchi Zhang
- Blaz Zlicar
year: 2020
venue: Deutsche Bank Research — Quantcraft (Global Quantitative Strategy)
tags:
- machine-learning
- alpha-combination
- stock-selection
- sell-side-research
- deutsche-bank
sources: []
related:
- entities/deutsche-bank
- concepts/factor-investing
- concepts/alpha-signal
- concepts/alpha-correlation-turnover
- concepts/decision-trees
- concepts/overfitting-in-alpha-research
- concepts/backtesting
mind_map_priority: medium
schema_version: 2
uuid: 854e5bba-6dd7-5673-8fa3-85ca2c2196a6
content_hash: sha256:b0e2de91b1081cffe6dc535caf1c747c0b55aadea7f775b5c0d25989afa564b1
---

<!-- AUTHORED REGION START -->
# The Return of the Machines

**Published: 23 April 2020** · Deutsche Bank Research, Global Quantitative
Strategy · *Quantcraft* series, twenty-fifth edition · Deutsche Bank AG/London

**Lead contact:** Gianpaolo Tomasi. Research team: Vivek Anand, Andreas Farmakas,
Jose Gonzalez, Rong Leng, Caio Natividade, Gianpaolo Tomasi, Ganchi Zhang,
Blaz Zlicar.

This is dated house research from a sell-side quantitative strategy desk, not a
peer-reviewed paper. It carries a publication date, a house view, and the
commercial context [[entities/deutsche-bank|Deutsche Bank]] research is produced
in. Treat the backtest numbers as the desk's own, and trace anything
load-bearing to the underlying method rather than resting on the note.

## What It Is

A five-years-later revisit of N-LASR — Non-Linear Adaptive Style Rotation — DB's
Adaboost-inspired algorithm for combining stock-selection alphas, originally
described in Wang et al. (2012, 2013, 2014). The note re-tests it rather than
introducing it.

Universe is the most liquid 80% of MSCI World, roughly 1,200 stocks, with 114
features as inputs. The liquid subset is deliberate: the desk wanted to rule out
the model simply harvesting an illiquidity premium. Backtest runs January 2003
to January 2020, adjusted for transaction costs.

## Findings

N-LASR ranks top among the tested aggregation methods on rank information
coefficient, Sharpe ratio, CAGR and drawdown-by-volatility, at 3.8% daily
turnover (19% weekly).

Two comparisons matter more than the headline. First, naive equal weighting of
the 114 features significantly underperforms everything else — weighting alphas
by historical performance earns its keep. Second, plain non-negative least
squares performs *well*, which the note concedes challenges the case for further
complexity. Across eight regional universes N-LASR beat NNLS on net Sharpe by
only 5–20%.

The conclusion is honest about the margin: performance has decayed slightly since
the last report but remains within backtest projections; the model needs a large
universe to work; and its worst drawdowns arrive when the top historical factors
underperform.

## How to Read It

The publication date is April 2020 — weeks after the COVID crash, and the
backtest stops in January 2020. Any claim about robustness through that episode
is outside the tested window.

## Open Questions

- What did the 5–20% Sharpe margin over least squares look like after 2020?
- The desk lists over-fitting, turnover and opacity as the standard objections
  and addresses them in its own tests; none are independently verified here.

## See Also

[[entities/deutsche-bank|Deutsche Bank]] ·
[[concepts/factor-investing|Factor Investing]] ·
[[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]] ·
[[concepts/overfitting-in-alpha-research|Overfitting in Alpha Research]] ·
[[sources/db-2020-11-05-global-factor-monitor|Global Factor Monitor (Nov 2020)]]
tracks N-LASR's live monthly performance.

**Not yet written:** `n-lasr-model`, `adaboost`, `gradient-boosting`,
`rank-information-coefficient`, `alpha-aggregation`.
<!-- AUTHORED REGION END -->

