---
authors:
- Junbo Wang
- Chunchi Wu
- Eden S. H. Yu
content_hash: sha256:39581b83aad56f0517398561154d31a3ca96ca26ca6c41846a701099584809e7
created: 2026-09-27 01:47:00+00:00
page_id: sources/wang-2012-order-imbalance-liquidity-returns-us-treasury-market
page_type: source
publication_venue: Review of Pacific Basin Financial Markets and Policies
related:
- concepts/order-imbalance
- concepts/bond-liquidity
- concepts/liquidity-risk
- concepts/bid-ask-spread
- concepts/informed-trading
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:f7463f38bf71895e766ba69594c0405b9c3d84dbd6a33d09f9cd94f2b951876d
source_path: markdown_output/wang-2012-order-imbalance-liquidity-returns-us-treasury-market.md
source_type: paper
tags:
- treasury-bonds
- order-imbalance
- bid-ask-spread
- liquidity
- bond-returns
- volatility
- commonality
- govpx
- clock-calendar
- asset-bonds-rates
- added-by-hand
title: Order Imbalance, Liquidity, and Returns of the U.S. Treasury Market
updated: '2026-09-27T01:47:00Z'
uuid: 055243bc-0bae-5aad-9a11-623770d93cc7
year: 2012
---

<!-- AUTHORED REGION START -->
# Order Imbalance, Liquidity, and Returns of the U.S. Treasury Market

## Summary

Extending Chordia, Roll and Subrahmanyam's (2002) equity-market study to government bonds, the paper asks whether marketwide order imbalance, net buy versus sell pressure aggregated across Treasury securities, affects liquidity, returns and volatility of the Treasury market, and whether this effect differs by bond maturity. It complements Brandt and Kavajecz's (2004) finding that individual-bond order imbalances carry private information about yields by instead isolating the inventory/liquidity dimension of imbalance at the aggregate market level.

Using eleven years of intraday GovPX quote and transaction data for on-the-run Treasuries, the authors build daily marketwide order imbalance measures (in number of trades and in dollar volume), quoted spreads, transaction counts and volume, then run day-of-week, spread, return and volatility regressions, corrected for residual autocorrelation, both for the whole market and for six maturity groups. A further pair of regressions splits each maturity group's order imbalance into a marketwide (systematic) component and an idiosyncratic residual to study commonality.

Order imbalance is found to be persistent, to show day-of-week patterns, and to behave like a contrarian signal, with net buying following market declines and net selling following advances. It widens bid-ask spreads contemporaneously, has an asymmetric effect on volatility in which sell-side imbalance matters far more than buy-side imbalance, and moves Treasury market returns in the expected direction, with a same-day effect that partly reverses the next day. All of these effects are concentrated in shorter- and medium-maturity issues (roughly one to five years) rather than at the very short or very long end of the curve, and there is significant commonality in order imbalance across maturity groups.

What is new relative to prior Treasury microstructure work is the explicit focus on the inventory/liquidity channel of aggregate order imbalance (rather than its information content for individual bond prices), the documentation of a liquidity spillover running from the stock market into Treasuries, and an early measurement of commonality in order imbalances themselves, not just commonality in liquidity, across bonds of different maturities.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

All variables (order imbalance, quoted spread, transaction count, volume, return) are built once per calendar trading day from intraday, second-time-stamped GovPX quotes and trades for each on-the-run Treasury issue, then simple-averaged across securities to form a single daily marketwide series. Regressions relate a day's values to same-day and up-to-five-day lagged values, and a subset of models is used to predict the following trading day's spread, return or volatility.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** On-the-run U.S. Treasury securities grouped into six maturity categories: less than six months, six to twelve months, one to two years, two to five years, five to ten years, and ten to thirty years. Trading in on-the-run issues accounts for about 85% of interdealer market activity, which is why the paper restricts its sample to these issues.
- **Venue:** GovPX interdealer market, which consolidates trading data from five of the six major interdealer brokers.
- **Period:** January 1992 to December 2002.
- **Granularity:** Daily aggregates (2,717 daily observations) built from intraday, second-time-stamped quote and transaction data; the trade side (buyer- or seller-initiated) is reported directly in GovPX rather than inferred algorithmically.

## Features and Measures

- **Order imbalance in number of trades (OIBNUM).** The number of buyer-initiated trades minus the number of seller-initiated trades for a Treasury issue on a given day, averaged across securities to build a daily marketwide series.
- **Order imbalance in dollar volume (OIBDOL).** The buyer-initiated dollar trading volume minus the seller-initiated dollar volume for a Treasury issue on a given day.
- **Quoted bid-ask spread (QSPR).** The average daily quoted bid-ask spread across trades in a security, used throughout the paper as the measure of market liquidity.
- **Box-Cox transformed absolute order imbalance.** A nonlinear (Box-Cox) transform of the day-to-day change in absolute order imbalance, used in the spread regressions so the inventory effect need not be assumed linear.
- **Marketwide vs idiosyncratic order imbalance decomposition.** A regression of each maturity group's order imbalance on the marketwide order imbalance; the fitted (systematic) part and residual (idiosyncratic) part are then used separately to explain that group's bid-ask spreads.

## Method

Most relationships are estimated with time-series regressions on daily data, generally corrected for residual autocorrelation using the Cochrane-Orcutt method. Liquidity (spread) regressions relate the percentage change in quoted spread to a Box-Cox transform of absolute order imbalance, the percentage change in the number of transactions, market returns (Treasury and/or S&P 500) split into up- and down-market components, and a lagged dependent variable. Return regressions relate the Treasury market return to contemporaneous and lagged positive/negative order imbalance and to lagged positive/negative returns; a further regression restricts the sample to the top and bottom quintiles of imbalance and returns to check for block-trade-style reversals. Volatility regressions relate the absolute Treasury return to positive/negative order imbalance, volume, spreads and lagged absolute returns, for the whole market and separately by maturity group.

Commonality is assessed with two linked time-series regressions per maturity group: first, each group's order imbalance is regressed on the marketwide order imbalance to obtain a sensitivity coefficient and an idiosyncratic residual; second, that group's bid-ask spread is regressed on the marketwide order imbalance, the number of transactions, average trade size, and the idiosyncratic order imbalance residual from the first regression, so the relative size of systematic and idiosyncratic order-flow effects on liquidity can be compared.

## Results

- Daily marketwide order imbalance is persistent, showing positive serial correlation over multiple lags, and exhibits day-of-week regularities, being lower on Monday and higher on other days.
- Order imbalance behaves like a contrarian flow: investors buy after the Treasury market falls and sell after it rises, and this pattern holds after controlling for auctions, macroeconomic news and the corporate-Treasury default premium.
- Higher order imbalance, in either direction, contemporaneously widens the quoted bid-ask spread, while higher Treasury and S&P 500 returns are associated with better next-day liquidity, indicating a spillover from the stock market into Treasury market liquidity.
- Contemporaneous order imbalance has a strong, expected-signed effect on Treasury market returns, with buy imbalance raising prices and sell imbalance lowering them, while lagged buy imbalance predicts a reversal in the next day's return.
- Order imbalance affects return volatility even after controlling for volume and spreads, and the effect is asymmetric: sell-side imbalance has a much larger effect on volatility than buy-side imbalance.
- Effects of order imbalance on spreads, returns and volatility are strongest for bonds with maturities of roughly one to five years and weakest at the very short (under six months) and very long (ten to thirty years) ends of the curve.
- There is significant commonality in order imbalance across bonds of different maturities, with sensitivity to the marketwide order imbalance factor highest for one-to-two-year and two-to-five-year maturities.
- The marketwide (systematic) component of order imbalance has a larger average effect on bid-ask spreads than the idiosyncratic, bond-specific component across maturity groups.

## Limitations

- The GovPX sample ends in 2002 because coverage declines sharply afterward as interdealer trading shifted to electronic platforms, so results may not extend to the market structure that followed.
- The analysis is conducted at the daily frequency; although the underlying data are intraday, intraday-frequency order imbalance or spread relationships are not reported.
- Reader note: conclusions rest on time-series regressions with an autocorrelation correction rather than a structural model, so the inventory-versus-information interpretation of the estimated effects is inferred rather than directly tested.
- Reader note: several regression tables in the converted file are visually garbled by the PDF-to-markdown conversion, so individual coefficient values in those tables should be checked against the original PDF before being relied on.

## Related

- [[concepts/order-imbalance|order imbalance]]
- [[concepts/bond-liquidity|bond liquidity]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Junbo Wang, Chunchi Wu, Eden S. H. Yu (2012). Order Imbalance, Liquidity, and Returns of the U.S. Treasury Market. Review of Pacific Basin Financial Markets and Policies.

DOI: 10.1142/s0219091512500105

Text ingested: `markdown_output/wang-2012-order-imbalance-liquidity-returns-us-treasury-market.md`, converted from `raw/ofi-event-clock/wang-2012-order-imbalance-liquidity-returns-us-treasury-market.pdf`.

Coverage of this summary: Read the full converted markdown end to end: introduction, the data section (order imbalance summary statistics and regressions), the liquidity/order-imbalance section, the returns section, the volatility section, the commonality-in-order-imbalances section, the conclusion, and the reference list.

Known problems with the input: The PDF-to-markdown conversion mangles many characters, rendering ligatures as '®' or '¯' (for example 'di®erent' for 'different', '¯rst' for 'first'); this does not change the content but is noted here for provenance checking; Several large regression tables (order-imbalance, spread, return, volatility and commonality regressions) are rendered with broken column alignment and stray symbols in the conversion, so individual coefficient and t-statistic values could not be reliably matched to specific variables; only the patterns described in the paper's own prose are reported here.
<!-- AUTHORED REGION END -->