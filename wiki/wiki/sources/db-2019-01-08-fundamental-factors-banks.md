---
title: Building Fundamental Factors for Banks (Signal Processing, 8 January 2019)
page_id: sources/db-2019-01-08-fundamental-factors-banks
page_type: source
source_type: sell-side-research
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Paul Ward
- Ronnie Shah
- Aris Tentes
- Kinner Lakhani
- David Lock
- Amandeep Singh
- Spyros Mesomeris
year: 2019
venue: Deutsche Bank Research — Signal Processing (Global Quantitative Strategy)
tags:
- bank-equities
- fundamental-factors
- stock-selection
- sell-side-research
- deutsche-bank
sources: []
related:
- entities/deutsche-bank
- concepts/factor-investing
- concepts/factor-models
- concepts/fama-french-factors
- concepts/risk-parity
- concepts/alpha-signal
- concepts/backtesting
mind_map_priority: medium
schema_version: 2
uuid: ba2257b1-a5ce-55cc-b5f8-40713521bd4e
content_hash: sha256:2814648f13ca2723bab857805acdd645f6ab69ee2f2173d4aad960f4f1885fda
---

<!-- AUTHORED REGION START -->
# Building Fundamental Factors for Banks

*Introducing Industry-specific Banking Insights*

**Published: 8 January 2019** · Deutsche Bank Research, Global Quantitative
Strategy · *Signal Processing* series · Deutsche Bank AG/London

**Authors:** Paul Ward, Ronnie Shah, Aris Tentes (quantitative strategy);
Kinner Lakhani, David Lock, Amandeep Singh (European banks research);
Spyros Mesomeris. The note credits Andreas Farmakas for contributions.

House research produced in a commercial context, with a publication date that
matters as much as the content. It is a different evidentiary standing from a
peer-reviewed paper — see [[entities/deutsche-bank|Deutsche Bank]] for how this
archive is framed. Backtest statistics below are the desk's own.

## The Problem It Addresses

Banks get dropped from quantitative equity models. The metrics that discriminate
among ordinary corporates do not transfer — debt-to-EBITDA is meaningless for an
institution whose core business is intermediating money — and the note observes
that academic work including
[[concepts/fama-french-factors|Fama and French (1993)]] excludes financials for
this reason. That exclusion leaves a sector uncovered rather than solved.

## What They Do

They mine the S&P Global Market Intelligence SNL Bank fundamentals database for
industry-specific signals across four themes: valuation, asset quality, balance
sheet strength, and profitability. The stated aim is not novel metrics but
insights into earnings quality, asset growth, profitability and valuation that
standard financial-statement data cannot reach for a bank.

Signals are evaluated by rank information coefficient and Sharpe ratio, then
combined using the portfolio construction approach of Osiol et al. (2017).
Sample period is January 2000 to August 2018, covering US and European banks.

## Findings

The exercise yields 11–12 signals. Individually they support portfolios with
Sharpe ratios of 0.3–1.0 in the US and 0.5–1.2 in Europe. Because the signals are
weakly correlated with one another, simple combination lifts that to 1.5 in the
US and 1.3 in Europe, and a [[concepts/risk-parity|risk parity]] construction
reaches 1.64 in the US over the sample.

The desk also claims the composite is additive to non-fundamental signals such
as momentum and analyst revisions, and diversifies a traditional stock-picking
strategy.

## Caveats

The headline 1.64 Sharpe is an in-sample backtest over a period that begins with
the run-up to, and includes, the global financial crisis — a regime in which bank
balance-sheet and asset-quality signals would be expected to work unusually well.
The note does not report an out-of-sample split, and 2018 is where it stops.

## Open Questions

- Does the US-versus-Europe Sharpe gap reflect signal quality or the different
  regulatory and recapitalisation paths of the two banking systems?
- How much of the combined 1.5 comes from the crisis years alone?

## See Also

[[entities/deutsche-bank|Deutsche Bank]] ·
[[concepts/factor-investing|Factor Investing]] ·
[[concepts/factor-models|Factor Models]] ·
[[concepts/leverage-ratios|Leverage Ratios]] ·
[[concepts/alpha-signal|Alpha Signal]]

**Not yet written:** `bank-asset-quality-metrics`, `snl-bank-fundamentals`,
`rank-information-coefficient`, `earnings-quality`, `industry-specific-factors`.
<!-- AUTHORED REGION END -->

