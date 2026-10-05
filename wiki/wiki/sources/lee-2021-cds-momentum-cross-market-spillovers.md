---
authors:
- Jongsub Lee
- Andy Naranjo
- Stace Sirmans
content_hash: sha256:d45607ac791ea172bf75230e5f8eba22a8fb44defd5a69ddcdfe50e9b31e9879
created: '2026-10-05T15:52:32Z'
page_id: sources/lee-2021-cds-momentum-cross-market-spillovers
page_type: source
publication_date: '2021'
publication_venue: Review of Asset Pricing Studies 11(2)
related:
- concepts/credit-default-swaps
- concepts/credit-default-swap-spread
- concepts/cross-sectional-momentum
- concepts/bond-momentum
- concepts/spillover-effect
- concepts/market-implied-ratings
- concepts/momentum-trend-following
- concepts/capital-structure-arbitrage
- concepts/cds-holding-period-return
- concepts/cds-momentum
- sources/haesen-2017-momentum-spillover
- sources/jostova-2013-momentum
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/daniel-2016-momentum-crashes
- sources/dafonseca-2020-cds-equity-volatility-comovement
- analyses/capital-structure-arbitrage-literature-review
- entities/jongsub-lee
- entities/andy-naranjo
- entities/stace-sirmans
revision_id: 1
schema_version: 2
source_hash: sha256:dd51ff0b3446cdb5d97b31aabe9999d49648cb7d544ca0df1478e058ddeee0fc
source_path: markdown_output/lee-2021-cds-momentum-cross-market-spillovers.md
source_type: paper
sources: []
tags:
- cds-momentum
- credit-default-swaps
- cross-market-spillover
- credit-ratings
- momentum
- equity-credit-linkage
- information-flow
- cds-depth
title: 'CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers'
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 04fec1ed-63a0-5dc9-9456-4be9398512ef
version_read: Working paper dated 28 December 2014 (AEA 2015 conference copy). The
  published RAPS 2021 version may differ in sample, tables and numbers; all figures
  here come from the 2014 draft.
year: 2021
---

<!-- AUTHORED REGION START -->
# CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers

**Authors:** Jongsub Lee, Andy Naranjo, Stace Sirmans · **Year:** 2021 · **Venue:** Review of Asset Pricing Studies 11(2)
**Version read:** Working paper dated 28 December 2014 (AEA 2015 conference copy). The published RAPS 2021 version may differ in sample, tables and numbers; all figures here come from the 2014 draft.

## Summary

The paper asks whether single-name CDS returns show momentum, and whether past CDS returns help predict stock returns. It turns daily Markit CDS spreads into monthly holding-period returns for a protection seller. It then sorts firms on past CDS returns, as in standard stock momentum.

CDS momentum exists. Buying protection on past CDS losers and selling protection on past winners earns about 52 bps a month with a three-month look-back and one-month hold. Profits are larger for junk-rated names, for contracts with many dealer quotes (high Markit depth), and during the 2007-2010 crisis. Bond and equity factors do not explain it.

The main driver is rating changes that the CDS market sees coming. Past CDS winners are upgraded more often over the next six months, and past losers are downgraded more often. When firms with no rating change are removed, momentum profits mostly vanish. This sets CDS momentum apart from corporate bond momentum, which earlier work found unrelated to rating changes.

The signal also spills into stocks. Sorting stocks on past CDS returns earns a positive spread, concentrated in junk and high-depth names. A joint sort that buys stocks that are winners on both stock and CDS returns, and sells double losers, earns about 116 bps a month. Plain stock momentum earns almost nothing in the same sample and crashes in the crisis.

## Data

- 5-year USD single-name CDS on 1,247 US public firms, January 2003 to December 2011, from Markit (composite spreads and 'depth', the number of quote contributors).
- Modified Restructuring contracts before the April 2009 Big Bang, No Restructuring after.
- Equity: CRSP daily returns compounded to the CDS holding window; share codes 10/11; NYSE/AMEX/Nasdaq; price at least $1.
- S&P ratings from Compustat, mapped 1 (AAA) to 22 (D).
- Realised recoveries for 40 credit events from Creditex; USD Libor curve from Datastream fitted with Nelson-Siegel-Svensson for discounting.
- CDS bid-ask spreads from Datastream (2005-2010) for cost checks; bond momentum series from Jostova et al. (2013); Fama-French/Carhart factors.
- Monthly rebalancing on the 19th/20th of each month (weekly returns also computed as a check).

## Method

CDS returns. The authors price a 5-year CDS with the standard ISDA-style model (O'Kane 2008) under a flat hazard rate calibrated to the quoted 5-year spread. The risky annuity over 21 quarterly coupon dates is
$$RPV01(t_0,t_{21})=\sum_{n=1}^{21}\Delta(t_{n-1},t_n)Z(t_0,t_n)Q(t_0,t_n)+\sum_{n=1}^{21}\tfrac12\Delta(t_{n-1},t_n)Z(t_0,t_n)\big(Q(t_0,t_{n-1})-Q(t_0,t_n)\big),$$
with $Q$ the survival probability and $Z$ the discount factor. For a protection seller entering at $t_0$ and unwinding at $t'$ (ignoring coupons and default inside the window), the holding-period excess return is
$$\text{CDS return}(t_0,t')=-\big(S(t')-S(t_0)\big)\,RPV01(t',t_{21}).$$
In implementation they add coupon accrual (post-Big-Bang full-coupon convention, running-spread basis) and set the return to $-(1-\tilde R)$ on a credit event. Trades run from the 20th to the 19th of the next month so the same maturity date is sold and bought back.

Momentum. Each month firms are sorted into quintiles on past $J$-month CDS return; the strategy sells protection on the top quintile (P5) and buys protection on the bottom (P1), equal-weighted, held $K$ months with overlapping portfolios averaged. No skip month is used, because weekly CDS returns show continuation, not reversal.

Tests. Alphas from Newey-West (12 lags) regressions on bond factors (DEFAULT, TERM), Carhart factors and a local stock-momentum factor. Characteristic-adjusted returns on size, rating and depth, plus quintile sorts on each after orthogonalising against the other two. Splits of P1/P5 by rating change (upgrade, downgrade, none) in the following six months. Independent 5x5 sorts on past stock and past CDS returns to isolate incremental information. Cross-market strategy: sort on past CDS return, trade the stock. Joint-market strategy: long stocks in both CDS-winner and stock-winner quintiles, short stocks in both loser quintiles.

## Key Findings

1. A 3-month formation, 1-month holding CDS momentum strategy earns 0.520% a month (6.42% a year), with a t-statistic of 3.87 and a Sharpe ratio of 0.423, over 2003-2011.
2. Momentum is stronger for junk-rated names (0.833% a month) than investment grade (0.268%), but both are significant and have similar Sharpe ratios; the highest-depth quintile earns 0.798% a month and still about 42 bps after costs under a 100% turnover assumption.
3. Profits rise in the crisis: 0.971% a month from July 2007 to April 2010, versus 0.228% pre-crisis and 0.641% post-crisis.
4. Momentum comes from anticipated rating changes. P5 has more upgrades than P1 (10.2% vs 5.00%) and P1 more downgrades (20.6% vs 11.0%). Firms rated in the anticipated direction yield 2.044% a month; firms with no rating change yield an insignificant 0.102%; unanticipated changes show reversal (-0.587%).
5. Upgraded (downgraded) firms already show a six-month cumulative CDS return of 221 bps (-324 bps) before the announcement, then a further 44 bps (-133 bps) in the announcement month.
6. Sorting stocks on past CDS returns earns 0.518% a month across all firms (t = 1.69), 1.365% for junk names and 0.806% for high-depth names, versus -0.0473% for low-depth names.
7. Plain stock momentum earns an insignificant 0.124% a month in this sample, while the joint CDS-plus-stock sort earns 1.160% (a net gain of 1.037%), with 2.647% in the crisis. Joint losers are downgraded 32.4% of the time versus 18.9% for stock-only losers.

## Limitations

- Read from the 2014 working paper; the published RAPS 2021 tables may differ.
- Short sample (2003-2011) dominated by one crisis; much of the joint-strategy gain sits in the crisis window.
- CDS returns rest on a flat hazard rate fitted to the 5-year quote only and on Markit composite mid quotes, not traded prices.
- Transaction-cost evidence is partial: bid-ask data only for 2005-2010 and only checked for the high-depth group.
- The CDS-to-stock cross-market return for all firms is only marginally significant (t = 1.69).
- Sample tilts to very large firms (over half in the top NYSE size decile), so small-issuer behaviour is not covered.
- The rating-change channel is shown with ex-post rating outcomes; it explains returns but is not itself a tradable signal.

## Questions Raised

- Does CDS momentum survive in the post-2012 market of standard 100/500 bp coupons, central clearing and thinner single-name liquidity?
- Does the same CDS-return signal predict corporate bond excess returns, given that bond momentum here lags CDS momentum?
- How much of the anticipated-rating effect is captured by simpler measures, such as spread changes relative to rating-implied spreads?
- Is the joint CDS-plus-stock momentum gain robust outside the 2007-2010 crisis?

## Relevance to Bond Signals

Past 3-month CDS returns are a timely issuer-level credit signal that leads both bond momentum and rating changes, strongest for high-yield names with many dealer quotes. For bond signals this suggests using CDS-return momentum, or spread change scaled by risky duration, as an input that anticipates downgrades and as a confirmation filter alongside equity momentum.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]]
- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/spillover-effect|Momentum Spillover Effect]]
- [[concepts/market-implied-ratings|Market-Implied Ratings]]
- [[concepts/momentum-trend-following|Momentum and Trend Following]]
- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/cds-holding-period-return|CDS Holding-Period Return]]
- [[concepts/cds-momentum|CDS Momentum]]

## Entities

- [[entities/jongsub-lee|Jongsub Lee]]
- [[entities/andy-naranjo|Andy Naranjo]]
- [[entities/stace-sirmans|Stace Sirmans]]

## Related Sources

- [[sources/haesen-2017-momentum-spillover|Momentum Spillover from Stocks to Corporate Bonds]]
- [[sources/jostova-2013-momentum|Momentum in Corporate Bond Returns]]
- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/daniel-2016-momentum-crashes|Momentum crashes]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
<!-- AUTHORED REGION END -->