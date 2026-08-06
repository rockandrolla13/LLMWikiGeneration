---
title: Implied Volatility Surface
page_id: concepts/implied-volatility-surface
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- options
- implied-volatility
- factor-models
- credit
sources:
- sources/shi-2022-cds-options-comovement
related:
- concepts/implied-volatility-skew
- concepts/unscented-kalman-filter
- concepts/option-implied-credit-information
mind_map_priority: medium
schema_version: 2
uuid: 46a01872-504e-54aa-89d3-172f4b2098cc
content_hash: sha256:e9bcf1b1a121c6dc9daa921d1eabc250e07249effc62e7cdd595ce56d7d578f9
---

<!-- AUTHORED REGION START -->
# Implied Volatility Surface

Implied volatility plotted across strike (or moneyness) and maturity. It is not flat, and how it is not flat carries information.

## As a Factor Structure

The wiki's substantive treatment comes from [[sources/shi-2022-cds-options-comovement|Shi et al. (2022)]], who fit S&P 500 index options from OptionMetrics on a grid of 5 moneyness levels by 6 maturities, weekly from January 2002 to December 2019 (939 observations).

They parameterize the surface with a Deterministic Linear Function and extract level, slope and curvature factors, exactly as the [[concepts/nelson-siegel-model|Nelson-Siegel]] parameterization does for the CDS curve on the other side of their study. Factors follow a VAR(1); estimation uses the [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] because the measurement equation linking observed prices to latent factors is nonlinear.

## What Moves With It

Their findings, on the co-movement between the CDX curve and the volatility surface:

- CDS level correlates with volatility level — the direct channel, consistent with Carr & Wu's Unit Recovery Claim theory, in which the default arrival rate affects the option discount rate and deep out-of-the-money puts price default probability.
- CDS slope correlates with volatility slope, but **through** the S&P 500 return rather than directly.
- CDS level affects the skewness of the volatility smile.
- Co-movement strengthens after the 2008-09 crisis.
- Controlling for the stock return, the relationship between the two markets becomes insignificant.

That last point is the sharpest one: the equity return mediates the link rather than the two surfaces speaking to each other.

## Elsewhere in the Wiki

[[concepts/implied-volatility-skew|Implied Volatility Skew]] is the cross-strike slice — the gap between equidistant put and call implied vols. [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]] is the broader claim that option prices carry credit-relevant information absent from stock prices. [[concepts/gaussian-processes|Gaussian Processes]] lists volatility surface fitting as an application, and [[concepts/rfq-markets|RFQ Markets]] notes that dealers price FX options off Black-Scholes plus a vol surface, with skew, term structure and hedging cost folded into the spread.

## See Also

[[concepts/implied-volatility-skew|Implied Volatility Skew]] · [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]] · [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]] · [[concepts/gaussian-processes|Gaussian Processes]] · [[concepts/rfq-markets|RFQ Markets]]

[[concepts/credit-default-swaps|Credit Default Swaps]]

**Not yet written:** `concepts/black-scholes`, `concepts/option-pricing`


## Implied Volatility as a Credit Signal

- [[sources/cao-2023-implied-vol-bond-returns|Cao et al. (2023)]] -- IV changes signal firm-risk shocks, not just fundamentals
- [[sources/hong-2025-implied-vol-cds-korea|Hong & Park (2025)]] -- cross-sectional prediction of CDS spread changes

<!-- AUTHORED REGION END -->
