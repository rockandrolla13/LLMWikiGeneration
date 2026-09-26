---
title: DTS (Duration Times Spread) - A New Measure of Spread Exposure in Credit Portfolios
page_id: sources/bendor-2007-dts
page_type: source
source_path: markdown_output/ssrn-956825.md
source_type: journal-article
revision_id: 1
created: 2026-09-15 00:00:00+00:00
updated: '2026-09-15T00:00:00Z'
authors:
- Arik Ben Dor
- Lev Dynkin
- Jay Hyman
- Patrick Houweling
- Erik van Leeuwen
- Olaf Penninga
year: 2007
venue: Journal of Portfolio Management 33(2), 77-100 (SSRN 956825 version consulted)
tags:
- duration-times-spread
- spread-volatility
- corporate-bonds
- risk-model
- excess-returns
- relative-spread-change
sources: []
related:
- concepts/duration-times-spread
- concepts/credit-spread-changes
- concepts/factor-models
- concepts/volatility-targeting-position-sizing
- concepts/corporate-bonds
- entities/arik-ben-dor
- entities/lev-dynkin
- entities/jay-hyman
- entities/patrick-houweling
- entities/erik-van-leeuwen
- entities/olaf-penninga
- entities/lehman-brothers
- sources/houweling-2017-factor-investing
mind_map_priority: high
schema_version: 2
uuid: 52c4221c-5f2a-5e96-b4c9-78b5bd3ee3af
content_hash: sha256:70a81b0cb2c3d4773f1870a02105d62d60eb6ac8fe0feb8325fc71c32adad3a9
---

<!-- AUTHORED REGION START -->
# DTS (Duration Times Spread): A New Measure of Spread Exposure in Credit Portfolios

**Authors:** [[entities/arik-ben-dor|Arik Ben Dor]], [[entities/lev-dynkin|Lev Dynkin]], [[entities/jay-hyman|Jay Hyman]] (Lehman Brothers, Quantitative Portfolio Strategy); [[entities/patrick-houweling|Patrick Houweling]], [[entities/erik-van-leeuwen|Erik van Leeuwen]], [[entities/olaf-penninga|Olaf Penninga]] (Robeco Asset Management)

**Year:** 2007 · **Venue:** Journal of Portfolio Management 33(2), 77–100. The consulted text is the SSRN version (abstract 956825); the journal citation is taken from Houweling & van Zundert (2017), whose reference list cites it.

## Summary

Credit spreads do not move in parallel. When a sector widens or tightens, bonds trading at wider spreads move by proportionally more. So spread volatility is proportional to the spread level. That holds for the systematic volatility of a sector and for the idiosyncratic volatility of a single bond or issuer, across sectors, maturities and time periods. It follows that excess-return volatility is proportional to **duration times spread (DTS)**, not to spread duration alone. A volatility forecast built as DTS times the historical volatility of *relative* spread changes is better calibrated, and adjusts immediately when spreads move.

## Data

Monthly data on the Lehman Brothers Credit Index, September 1989 to January 2005 (185 months). Zero-coupon bonds, callable bonds and bonds with non-positive spreads are excluded, leaving 416,783 investment-grade observations. High yield bonds rated Ba and B trading above a price of 80 are added for parts of the study, bringing the total to 565,602. Spread changes above the 99th or below the 1st percentile are dropped. Agency debentures (Lehman Agency Index, Aaa, non-callable, 73,000 observations) are used to study very low spreads.

## The Core Identity

With spread duration *D* and spread *s*, the return from a spread change can be written two equivalent ways. One is spread duration times the absolute spread change. The other is DTS (*D*·*s*) times the *relative* spread change, Δs/s. Spread duration is the sensitivity to an absolute change such as "spreads widen 5 bp". DTS is the sensitivity to a relative change such as "spreads widen 10%". The authors' case for the second form rests entirely on the empirical stability of relative spread volatility.

Excess return is approximately the spread change return plus a carry component.

## Findings

**Spread changes are proportional, not parallel.** Across 1,480 sector-month regressions, a model where spread change is proportional to spread explains 33% of spread variation, against 16.9% for a parallel-shift model, and nearly matches a less restrictive combined model. The proportional slope is significant in 73% of sector-months. Large market moves come with slope moves in the same direction, with a correlation of 80%. In other words, wider-spread bonds widen more in sell-offs and tighten more in rallies.

**Systematic spread volatility is about 9% of spread per month.** Partitioning by sector, duration and spread bucket, systematic spread-change volatility rises linearly with spread level. The slope is 9.1% (9.4% excluding three outliers). A segment at 50 bp should have about 4.5 bp a month of spread volatility, and one at 200 bp about 18 bp. Duration and sector have little effect on the relationship.

**Idiosyncratic spread volatility is also proportional to spread.** The pooled idiosyncratic spread volatility of each cell lines up linearly against the cell's median spread, with a zero intercept and a slope of 11.5%. High yield buckets are noisier but follow the same line.

**The slope is stable over time.** Yearly slope estimates have t-statistics between 15 and 30 and are stable apart from 1998. Explanatory power is higher with high yield included: R² consistently above 70% for systematic and above 60% for idiosyncratic volatility, against lows of 40% and 30% for investment grade alone.

**Excess-return volatility is linear in DTS.** Sorting bonds into DTS quintiles and then spread sub-buckets, excess-return volatility against DTS fits a line through the origin with R² of 98% and a slope of 8.8%. Buckets with very different spreads and durations but the same DTS have the same volatility. In one example, a bucket at 54 bp and spread duration 5.48 and another at 127 bp and spread duration 2.53 have DTS of 299 and 320 and similar volatility.

**DTS gives better-calibrated volatility forecasts.** Each month, the realised excess return of 24 sector-quality buckets (carry stripped out) is divided by a volatility forecast. A well-calibrated forecast should give a standard deviation near 1.
- DTS times historical relative spread volatility: **1.01**.
- Spread duration times absolute spread volatility, full history: 1.14 (volatility underestimated).
- Spread duration times absolute spread volatility, previous 36 months: 0.92 (volatility overestimated).

Returns beyond two standard deviations are 4.03% of observations with the DTS forecast against 7.06% with the absolute one. Both standardised distributions are negatively skewed (−2.67 relative, −1.35 absolute).

The mechanism is that the absolute measure embeds the average spread over the estimation window, while the relative measure multiplies by today's spread. So with relative spread volatility a longer estimation window is always better. With absolute volatility there is no obviously right window.

## Limits of the Relationship

**Near zero spread.** Spread volatility has a constant "structural" component from pricing noise and supply-demand effects, plus a credit component proportional to spread. For agencies below about 20 bp, systematic spread volatility is roughly flat at 2.5–3.0 bp a month, and idiosyncratic volatility sits at 4.0–4.5 bp. Above 20 bp the linear relation returns, with a flatter slope of 5.7%. Agency excess-return volatility against DTS has a slope of 9.8% and a significant intercept of 3 bp.

**Seniority.** Within issuers, senior and subordinated portfolios matched to the same DTS have the same volatility. For notes against senior notes across 353 issuers, the median volatility ratio is 0.94 (interquartile range 0.79–1.08). Spreads appear to price differences in recovery.

**Robustness claims.** The authors state the results hold for weekly returns and for Treasury or Libor spread curves. They also state that European corporates and CDS indices behave the same way, citing their own analysis "to be published at a later date". That evidence is not in this paper.

## Implications Stated by the Authors

- Express sector over- and underweights as contributions to DTS rather than to spread duration.
- Set issuer limits on DTS contribution so riskier credits get smaller positions. They warn this can allow large positions in low-spread issuers exposed to "credit torpedoes", so they suggest combining it with market-weight caps.
- In a long-short pair within an industry, match DTS on both sides rather than dollar duration.
- In risk models, define spread factors as relative spread changes. A quality partition then becomes unnecessary, and each sector can be a single factor.
- DTS-based models are more exposed to pricing noise, so price quality control matters.

## Why It Matters for Signal Construction

This is the empirical basis for scaling bond returns or exposures by DTS instead of by realised volatility. Because both systematic and idiosyncratic spread volatility scale with spread, DTS is a candidate forward-looking denominator for a bond-specific signal as well as a market-wide one. It needs no return history, and it updates as spreads move. The paper does not study return predictability or momentum; it is about risk measurement only. The flattening below about 20 bp matters for any DTS-scaled signal on very tight investment-grade or quasi-sovereign bonds, since dividing by a near-zero DTS would overstate their scores.

## Open Questions

- The paper tests volatility, not whether DTS-scaled returns carry more predictive information than returns scaled by realised volatility. That comparison is untested in this wiki.
- How does the structural noise floor interact with TRACE transaction-price noise, which the authors did not have?

## Related

- [[concepts/duration-times-spread|Duration Times Spread]] · [[concepts/credit-spread-changes|Credit Spread Changes]] · [[concepts/factor-models|Factor Models]] · [[concepts/volatility-targeting-position-sizing|Volatility-Based Position Sizing]]
- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] cite this paper as evidence that DTS predicts corporate bond volatility, and use lowest-DTS bonds as an alternative Low-Risk factor definition (LR3).

## Citation

Ben Dor, A., Dynkin, L., Hyman, J., Houweling, P., van Leeuwen, E., & Penninga, O. (2007). DTS (Duration Times Spread): A New Measure of Spread Exposure in Credit Portfolios. *Journal of Portfolio Management*, 33(2), 77–100. SSRN 956825.
<!-- AUTHORED REGION END -->
