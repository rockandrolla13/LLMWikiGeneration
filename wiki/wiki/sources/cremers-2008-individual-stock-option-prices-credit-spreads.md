---
authors:
- Martijn Cremers
- Joost Driessen
- Pascal Maenhout
- David Weinbaum
content_hash: sha256:2d22a3a247b9c24ab5eb480a2c22425d38726393b143ffb927647d855f1b7b12
created: '2026-10-05T15:52:32Z'
page_id: sources/cremers-2008-individual-stock-option-prices-credit-spreads
page_type: source
publication_date: '2008'
publication_venue: Journal of Banking and Finance 32(12)
related:
- concepts/implied-volatility-skew
- concepts/volatility-smirk
- concepts/option-implied-credit-information
- concepts/structural-models
- concepts/merton-model
- concepts/jump-diffusion-option-pricing
- concepts/credit-spread-changes
- concepts/credit-spread-puzzle
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/cao-2023-implied-vol-bond-returns
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/avino-2024-hedging-credit-equity-options
- sources/hong-2025-implied-vol-cds-korea
- sources/dafonseca-2020-cds-equity-volatility-comovement
- analyses/capital-structure-arbitrage-literature-review
- entities/martijn-cremers
- entities/joost-driessen
- entities/pascal-maenhout
- entities/david-weinbaum
revision_id: 1
schema_version: 2
source_hash: sha256:51f4cf86c45a23eb0f92d9118b55b47440c8f95488e0e2e28359977c1fd86e5f
source_path: markdown_output/cremers-2008-individual-stock-option-prices-credit-spreads.md
source_type: paper
sources: []
tags:
- implied-volatility
- implied-volatility-skew
- credit-spreads
- corporate-bonds
- jump-risk
- structural-models
- credit-ratings
- equity-credit-linkage
title: Individual Stock-Option Prices and Credit Spreads
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 9795b3a5-2125-5a9a-b770-6cdf574c3aec
version_read: Yale ICF Working Paper No. 04-14, dated December 2004. The published
  JBF 2008 version may differ in sample, tables and numbers; all figures here come
  from the 2004 draft.
year: 2008
---

<!-- AUTHORED REGION START -->
# Individual Stock-Option Prices and Credit Spreads

**Authors:** Martijn Cremers, Joost Driessen, Pascal Maenhout, David Weinbaum · **Year:** 2008 · **Venue:** Journal of Banking and Finance 32(12)
**Version read:** Yale ICF Working Paper No. 04-14, dated December 2004. The published JBF 2008 version may differ in sample, tables and numbers; all figures here come from the 2004 draft.

## Summary

The paper asks whether prices of options on a firm's own stock help explain the credit spreads on its bonds. It uses two option measures. At-the-money implied volatility stands in for the volatility of firm value. The slope of the put smirk stands in for the risk of a sudden downward jump.

Both measures matter, across firms and over time. On their own they explain about 14% of the variation in short-maturity spreads and 32% for long maturities in a pooled panel. That beats credit ratings alone by 5 to 15 percentage points. Firm implied volatility stays the strongest firm-level variable after controls for stock returns, rates, the BAA yield, liquidity proxies, year dummies and firm fixed effects. Index option measures and historical volatility are much less robust.

Sensitivity rises as ratings fall, which a structural model predicts. A calibrated jump-diffusion firm-value model gives coefficients broadly in line with the estimates. Option bid-ask spreads also widen short-maturity spreads, a liquidity spillover. Implied volatility rises in the weeks before downgrades.

The authors also revisit Collin-Dufresne, Goldstein and Martin (2001). Once the option measures and controls are in, principal components of spreads explain almost none of what is left. So they argue there is no large unexplained common factor in spread levels. The cross-section of spreads remains harder to explain than the time series.

## Data

- 69 US firms with both bond and option data (a subset of Duffee 1999 firms), 524 straight fixed-coupon corporate bonds, weekly, January 1996 to September 2002 (351 weeks).
- Bond mid-quotes, ratings and terms from the Bloomberg Corporate Bonds Database; bonds with under one year to maturity dropped; short (1-5y) and long (7y+) maturities analysed separately.
- Treasury curve fitted weekly with an extended Nelson-Siegel model to get matched-maturity default-free yields; spreads are yield minus matched Treasury yield.
- Option quotes and implied volatilities from OptionMetrics, using the expiry in the month after the current one.
- Controls: 180-day firm and S&P returns (CRSP), 2- and 10-year Treasury yields, BAA yield, 10-year swap rate, 30-day Eurodollar minus Treasury (Datastream).
- S&P ratings grouped into 5 buckets (AAA, AA, A, BBB, BB and below), and into 3 buckets for interactions (AAA to A-, BBB+ to BBB-, BB+ and below).

## Method

Measures. Implied volatility is the at-the-money implied volatility of the firm's near-month stock options. The skew is the left slope of the smirk: the implied volatility of a put with strike-to-spot of 0.92 (or nearest) minus the at-the-money put implied volatility, divided by the gap in strike-to-spot ratios, i.e.
$$\text{Skew}_{i,t}=\frac{IV^{put}_{i,t}(K/S\approx0.92)-IV^{put}_{i,t}(ATM)}{1-0.92}$$
(the paper states the definition in words; Table 1 fixes the sign: the mean individual skew is 0.314, positive, so the denominator is 1 − 0.92). Historical volatility uses the past 180 daily returns, rescaled to the same time-series standard deviation as implied volatility so coefficients are comparable.

Regressions. Pooled OLS of weekly spread levels (not changes) on the option measures, index option measures, historical volatilities and controls, with one coefficient set for all bonds. Standard errors allow for heteroskedasticity, AR(1) errors per bond and full cross-bond correlation. Extensions add year dummies, firm fixed effects, option bid-ask spreads (ATM and OTM), rating dummies, and rating-bucket interactions with implied volatility, skew and historical volatility.

Theory check. A Huang-Huang (2003) style jump-diffusion firm-value model with a continuous default boundary at 100% of debt (Longstaff-Schwartz type), rates 8% and payout 6%, downward exponential jumps (benchmark intensity 0.4 a year, mean jump 20%; alternatives 0.8/10% and 1.6/5%, plus a default-at-maturity case). Model partial derivatives of a 10-year par spread with respect to implied volatility and skew are compared with the regression coefficients.

Other. Event plots of implied volatility over 32 weeks around rating changes versus non-migrating controls. Principal components of spread levels (EM algorithm for missing data) used to test how much systematic variation remains in regression residuals.

## Key Findings

1. Firm implied volatility and skew alone give an R-squared of 14% for short-maturity and 32% for long-maturity spreads; rating dummies alone give 9% and 17%.
2. A one-standard-deviation weekly move in implied volatility (0.046) widens spreads by almost 12 bp (short) and 20 bp (long); a similar skew shock adds slightly under 10 bp.
3. With macro and liquidity controls, firm implied volatility remains the single most significant variable for long-maturity spreads, with a coefficient of 2.38 and a t-statistic of 21.
4. Sensitivity rises as ratings fall. For long bonds, the implied-volatility coefficient is 3.47 for A- or better and 4.72 for BBB; the skew coefficient is 0.117 for the top bucket and 0.463 for junk, so a one-standard-deviation skew shock moves spreads 4, 13 and 17 bp across the three buckets.
5. Option bid-ask spreads matter for short-maturity bond spreads but not long ones; the OTM option spread is the most precise (t = 9.21), consistent with a liquidity spillover.
6. Five principal components explain 94% of spread variation bond by bond, but only 5.58% (short) and 6.97% (long) of residual variation after the volatility and skew measures, and almost none after full controls.
7. Implied volatility of downgraded firms rises ahead of the event and peaks 2 to 3 weeks before the announcement; the sample has 34 upgrades and 73 downgrades, and upgrades show little pattern.

## Limitations

- Read from the 2004 working paper; the published JBF 2008 version may differ.
- Small sample: 69 large firms, mostly investment grade, 1996-2002.
- Bond prices are Bloomberg mid-quotes, not trades; no bond bid-ask spreads, so option liquidity cannot be tied directly to bond liquidity.
- All regressions are contemporaneous; the paper explains spread levels, it does not forecast spread changes or returns.
- The skew is measured with a single near-month OTM put and is noisy; the authors suggest this may explain why model skew coefficients are larger than the estimates.
- The structural-model check uses constant volatility and jump intensity, so it is a comparative-statics check, not a fitted model.
- Rating-migration evidence is informal and based on few events.

## Questions Raised

- Do changes in firm implied volatility and skew predict future bond excess returns, not just explain contemporaneous spread levels?
- Does the stronger skew sensitivity for low-rated issuers survive in a larger, post-2002 high-yield sample?
- Is the option-liquidity effect on short-maturity spreads a true liquidity spillover or a proxy for informed hedging demand?
- Does a levels-based, PCA residual test overturn the Collin-Dufresne et al. common-factor finding when applied to spread changes?

## Relevance to Bond Signals

Firm-level ATM implied volatility and put skew are strong, timely proxies for issuer volatility and jump risk that rating buckets miss, with larger loadings for BBB and high-yield names. For bond signals they can serve as fair-value inputs (spread versus option-implied risk) and as early-warning features for downgrades, interacted with rating.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/implied-volatility-skew|Implied Volatility Skew]]
- [[concepts/volatility-smirk|Volatility Smirk as Informed-Trading Signal]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/jump-diffusion-option-pricing|Jump-Diffusion Option Pricing]]
- [[concepts/credit-spread-changes|Credit Spread Changes]]
- [[concepts/credit-spread-puzzle|Credit Spread Puzzle]]

## Entities

- [[entities/martijn-cremers|Martijn Cremers]]
- [[entities/joost-driessen|Joost Driessen]]
- [[entities/pascal-maenhout|Pascal Maenhout]]
- [[entities/david-weinbaum|David Weinbaum]]

## Related Sources

- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/cao-2023-implied-vol-bond-returns|Implied Volatility Changes and Corporate Bond Returns]]
- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/avino-2024-hedging-credit-equity-options|Contingent Claims and Hedging of Credit Risk with Equity Options]]
- [[sources/hong-2025-implied-vol-cds-korea|Do Changes in the Implied Volatility of Stock Options Predict Future Changes in CDS Spreads?]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
<!-- AUTHORED REGION END -->