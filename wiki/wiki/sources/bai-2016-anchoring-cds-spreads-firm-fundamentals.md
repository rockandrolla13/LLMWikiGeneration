---
authors:
- Jennie Bai
- Liuren Wu
content_hash: sha256:4c541a338b48b3503e91a4b15255ac8e1a32a339d34d8eb00f219efdf3fece22
created: '2026-10-05T15:52:32Z'
page_id: sources/bai-2016-anchoring-cds-spreads-firm-fundamentals
page_type: source
publication_date: '2016'
publication_venue: Journal of Financial and Quantitative Analysis 51(5), pp. 1521-1543
related:
- concepts/merton-model
- concepts/structural-models
- concepts/credit-default-swap-spread
- concepts/corporate-credit-fundamentals
- concepts/option-implied-credit-information
- concepts/credit-relative-value
- concepts/leverage-ratios
- concepts/local-regression
- concepts/bayesian-updating
- concepts/mean-reversion
- concepts/information-ratio
- concepts/factor-signals-in-credit
- concepts/distance-to-default
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/avramov-2007-changes-corporate-credit-spreads
- sources/cao-2023-implied-vol-bond-returns
- sources/bharath-2008-forecasting-default-merton-distance-to-default
- analyses/capital-structure-arbitrage-literature-review
- entities/jennie-bai
- entities/liuren-wu
revision_id: 1
schema_version: 2
source_hash: sha256:ac2ccc9e1f9ce598bcb4bd129773892c840579838dbcedec93965c673930fe28
source_path: markdown_output/bai-2016-anchoring-cds-spreads-firm-fundamentals.md
source_type: paper
sources: []
tags:
- cds
- firm-fundamentals
- distance-to-default
- merton-model
- cross-sectional-valuation
- bayesian-shrinkage
- relative-value
- mean-reversion
title: Anchoring Credit Default Swap Spreads to Firm Fundamentals
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: dbfc6e4d-1fda-5872-a42b-7aadd067efbd
version_read: 'Published JFQA article (manifest version: ''published, author link'');
  the text read is the pdftotext layer of a JSTOR scan, with OCR noise and some right-margin
  text and equations cut off.'
year: 2016
---

<!-- AUTHORED REGION START -->
# Anchoring Credit Default Swap Spreads to Firm Fundamentals

**Authors:** Jennie Bai, Liuren Wu · **Year:** 2016 · **Venue:** Journal of Financial and Quantitative Analysis 51(5), pp. 1521-1543
**Version read:** Published JFQA article (manifest version: 'published, author link'); the text read is the pdftotext layer of a JSTOR scan, with OCR noise and some right-margin text and equations cut off.

## Summary

The paper asks how much of the cross-firm difference in CDS spreads can be explained by firm fundamentals. The authors argue that structural models are best tested across firms, not over time. Firm leverage and business type are stable, so time-series regressions on monthly changes say little about the link between structure and credit risk.

They build a fundamental CDS value in two steps. First, a Merton distance-to-default is computed from debt-to-market-cap and one-year realised stock volatility. It is turned into a raw spread and mapped to market CDS each week by a cross-sectional local quadratic regression (the MCDS value). Second, nine extra characteristics (alternative leverage, interest coverage, working capital, profitability, retained earnings, size, momentum, and the ratio of put implied to realised volatility) are added through a Bayesian shrinkage and stacking scheme (the WCDS value).

Across 579 US non-financial firms from 2003 to 2009, a plain linear regression on the two Merton inputs explains about half of the cross-section of log CDS. The Merton value explains about two thirds, and the WCDS value about three quarters, with stable fit over time and little loss out of sample. Size, retained earnings and the implied-to-realised vol ratio carry the most extra weight.

The gap between market CDS and the fundamental value is mean-reverting. It is negatively correlated with future CDS changes at one and four weeks. A long-short CDS exercise that buys protection where quotes are below fundamental value and sells where they are above earns high information ratios, though the authors stress this is not a realistic backtest.

## Data

- Universe: 579 US non-financial public firms with Markit 5-year CDS quotes; 351 weekly (Wednesday) dates from 8 Jan 2003 to 30 Sep 2009; 138,200 firm-week observations.
- CDS: Markit 5-year composite spreads; quotes above 10,000 bp dropped.
- Fundamentals: Capital IQ balance sheets, matched to market data with a 45-day reporting lag.
- Equity: CRSP prices; one-year daily return history for realised volatility.
- Options: OptionMetrics one-year 25-delta put implied volatility.
- Characteristics: (current liabilities + half of long-term liabilities)/market cap; total debt/total assets; EBIT/interest expense; working capital/total assets; EBIT/total assets; retained earnings/total assets; ln(market cap); past one-year stock return; ln(implied/realised volatility).

## Method

Merton step: solve for asset value A and asset volatility \sigma_A from
$$E = A\,N(d+\sigma_A\sqrt{T}) - D\,N(d),\qquad \sigma_E = N(d+\sigma_A\sqrt{T})\,\sigma_A A/E,$$
with E = market cap, D = total debt, \sigma_E = one-year realised volatility, r = 0 and T = 10 years; d is the standardised distance to default (log leverage scaled by \sigma_A\sqrt{T}). Convert to a raw spread assuming a flat hazard and 40% recovery:
$$\text{RCDS} = -6000\,\ln N(d)/T \text{ (bp)}.$$
Map to market quotes cross-sectionally each week: \ln \text{CDS}_i = f(\ln \text{RCDS}_i) + R_i (local quadratic), giving MCDS.

WCDS step: (i) orthogonalise each characteristic against ln MCDS by local linear regression; (ii) regress the Merton residual ln(CDS/MCDS) on each orthogonalised characteristic by local linear regression, giving K residual predictions; (iii) stack them and estimate weights by a Bayesian regression that uses the previous week's weights as the prior (smoothing parameter 0.98, equal-weight starting prior); missing predictions are filled by a shrinkage-weighted average of the available ones, with error variance proportional to one minus each regression's R^2; (iv) \ln \text{WCDS} = \ln \text{MCDS} + X_t W_t.

Tests: weekly cross-sectional R^2 of ln CDS on (a) leverage and volatility linearly (BLR), (b) ln MCDS, (c) ln WCDS; random half-sample out-of-sample check; cross-sectional correlation between the deviation ln(CDS/CDS-hat) and future log CDS changes at 1 and 4 weeks (Newey-West t-stats); and a dollar-neutral CDS portfolio with notional proportional to (CDS-hat - CDS), marked to market with a flat-hazard CDS valuation.

## Key Findings

1. Average weekly cross-sectional R^2 for log CDS is 49% for the linear leverage-and-volatility regression, 65% for the Merton-based value and 77% for the Bayesian-shrinkage WCDS value.
2. The WCDS fit is the most stable over time: its R^2 standard deviation is 4% (versus 8% for MCDS and 10% for BLR) and it stays between 67% and 85%.
3. Out of sample (random half of firms), the linear regression collapses from 51% to 25% R^2, while MCDS slips from 65% to 64% and WCDS from 77% to 74%.
4. CDS spreads vary far more across firms than over time: the average cross-sectional standard deviation of CDS is 345.71 bp versus 154.55 bp in the time series and 34.27 bp for weekly changes.
5. Deviations of market CDS from the WCDS value are negatively correlated with future CDS changes: about -7% at one week and -12% at four weeks, the strongest of the three valuations.
6. A dollar-neutral CDS exercise trading toward the WCDS value earns an information ratio of 2.26 with weekly rebalancing (1.50 with monthly) versus 1.51 for MCDS and 0.13 for BLR at one week.

## Limitations

The authors say the investment exercise is not a realistic backtest. Markit quotes are consensus averages, not executable prices, and OTC trading costs vary by institution. The Merton step uses simple choices (r = 0, T = 10 years, total debt as the default point, realised volatility). The sample ends in 2009 and covers only US non-financial firms with CDS. The paper's own text gives a weekly WCDS mean excess return of 21.14% while Table 4 shows 32.14% (32.14/14.22 matches the reported 2.26 ratio), so the in-text figure looks like a typo. Equations (3), (10) and (19) are partly cut off in the scan, so their exact printed form was not verified here.

## Questions Raised

- Does a WCDS-style fundamental anchor work for corporate bond spreads, where maturity and liquidity effects must also be controlled?
- How much of the market-minus-fundamental gap is transitory supply-demand pressure versus missing fundamentals (e.g. recovery or sector effects)?
- Does the reversion signal survive realistic CDS transaction costs and post-2009 standardised contracts?
- Can the fundamental value price names without CDS quotes well enough to mark bonds or illiquid credits?

## Relevance to Bond Signals

This is a template for a cross-sectional 'fair spread' model: a distance-to-default core plus shrinkage-weighted fundamentals, refit each week across issuers. The residual (market spread minus fair spread) is a mean-reversion relative-value signal at one to four weeks, and the same machinery could set bond spreads against fundamentals or fill in fair values for bonds without CDS.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/corporate-credit-fundamentals|Corporate Credit Fundamentals]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/credit-relative-value|Credit Relative Value]]
- [[concepts/leverage-ratios|Leverage Ratios]]
- [[concepts/local-regression|Nonparametric Local Regression]]
- [[concepts/bayesian-updating|Bayesian Updating]]
- [[concepts/mean-reversion|Mean Reversion]]
- [[concepts/information-ratio|Information Ratio]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]
- [[concepts/distance-to-default|Distance to Default]]

## Entities

- [[entities/jennie-bai|Jennie Bai]]
- [[entities/liuren-wu|Liuren Wu]]

## Related Sources

- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/avramov-2007-changes-corporate-credit-spreads|Understanding Changes in Corporate Credit Spreads]]
- [[sources/cao-2023-implied-vol-bond-returns|Implied Volatility Changes and Corporate Bond Returns]]
- [[sources/bharath-2008-forecasting-default-merton-distance-to-default|Forecasting Default with the Merton Distance to Default Model]]
<!-- AUTHORED REGION END -->