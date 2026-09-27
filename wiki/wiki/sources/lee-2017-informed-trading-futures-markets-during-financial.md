---
authors:
- Yen-Hsien Lee
- Wen-Chien Liu
- Chia-Lin Hsieh
content_hash: sha256:e6926c8b1afa40a591eaf6ecbe8fce80cc812a8d9a384a58c5d08f3cc8b1901b
created: 2026-09-27 01:47:00+00:00
page_id: sources/lee-2017-informed-trading-futures-markets-during-financial
page_type: source
publication_venue: International Journal of Economics and Finance, Vol. 9, No. 9
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/order-imbalance
- concepts/trade-classification
- concepts/high-frequency-data
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:87681a323127680c95e70348b432a2da887d9eaaba19525ac45e0e31a3ef6d34
source_path: markdown_output/lee-2017-informed-trading-futures-markets-during-financial.md
source_type: paper
tags:
- vpin
- informed-trading
- futures
- day-of-week-effect
- garch
- taiwan-futures-exchange
- institutional-investors
- clock-volume
- asset-futures
- harvest-core
title: 'Informed Trading of Futures Markets During the Financial Crisis: Evidence
  from the VPIN'
updated: '2026-09-27T01:47:00Z'
uuid: 333fe41f-e009-5ad8-b1cb-e0400311c717
year: 2017
---

<!-- AUTHORED REGION START -->
# Informed Trading of Futures Markets During the Financial Crisis: Evidence from the VPIN

## Summary

The paper asks whether informed trading, measured by the Volume-Synchronized Probability of Informed Trading (VPIN), affected Taiwan futures returns during the 2008-2009 global financial crisis, and whether this effect differs between domestic and foreign institutional investors or interacts with a day-of-the-week pattern in returns. It uses tick-by-tick Taiwan Futures Exchange (TAIFEX) transaction data from January 2, 2008 to March 18, 2009, which identifies trader type.

VPIN is computed with the tick-rule version (TR-VPIN) separately for all investors, domestic institutional investors, and foreign institutional investors. A series of GARCH(1,1) mean-equation models regress futures returns on lagged returns, the put-call ratio, lagged volume, day-of-week dummies (Monday, Wednesday, Friday), the VPIN measures, and interactions between VPIN and the Wednesday dummy.

The day-of-week effect is found mainly on Wednesdays, which have the highest average return and a statistically significant coefficient in the baseline model. The VPIN of all investors combined, and of domestic institutional investors alone, has no significant effect on futures returns; the VPIN of foreign institutional investors has a significant positive effect on futures returns in the models that separate investor types. When interacted with the Wednesday dummy, the VPIN of all investors and the VPIN of domestic institutional investors both become significantly positive on Wednesdays, while the foreign-investor VPIN's Wednesday interaction is not significant.

What is new relative to prior VPIN work is combining trader-identity data (splitting institutional investors into domestic versus foreign) with day-of-the-week interactions in a futures market during a crisis period, rather than studying VPIN alone or in equity markets; the authors present this as a joint test of informed trading and day-of-week effects using a dataset that can distinguish investor identity.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

VPIN divides each day's trading volume into equal-size volume buckets (rather than equal time intervals) using the tick rule to classify buy/sell volume, giving a daily VPIN value per investor-type series. These daily VPIN values (lagged one day, t-1) are then used as a right-hand-side regressor for daily futures returns at time t in the GARCH(1,1) mean-equation models, so the prediction horizon is one trading day ahead.

## Data

- **Asset class:** Futures
- **Instruments:** Taiwan Futures Exchange (TAIFEX) futures contracts, with trades classified by trader identity into domestic institutional and foreign institutional investors
- **Venue:** Taiwan Futures Exchange (TAIFEX)
- **Period:** January 2, 2008 to March 18, 2009
- **Granularity:** Tick-by-tick transaction data, aggregated to daily VPIN values and daily futures returns

## Features and Measures

- **VPIN (tick-rule version, TR-VPIN).** The Volume-Synchronized Probability of Informed Trading, computed by splitting daily volume into equal-size buckets and measuring the expected imbalance between buy and sell volume within them, here computed separately for all investors, domestic institutional investors, and foreign institutional investors using the tick rule to sign trades.
- **day-of-the-week dummies interacted with VPIN.** Indicator variables for Monday, Wednesday and Friday, entered both on their own and multiplied by the VPIN measures, to test whether informed trading's effect on returns is concentrated on particular weekdays.

## Method

The authors first estimate a GARCH(1,1) mean equation for daily futures returns with lagged returns, the put-call ratio, lagged volume, and Monday/Wednesday/Friday dummies (Model 1), then progressively add the lagged VPIN of all investors (Model 2), the VPIN interacted with the Wednesday dummy (Model 3), separate VPIN series for domestic and foreign institutional investors (Model 4), and those investor-type VPIN series interacted with the Wednesday dummy (Model 5).

Before estimation, all series are checked for stationarity with Augmented Dickey-Fuller and Phillips-Perron unit-root tests. Model fit and residual diagnostics are judged using the sum of squared residuals, log-likelihood, Durbin-Watson statistic, Akaike information criterion, Ljung-Box tests for serial correlation in levels and squares, an ARCH-effect Lagrange multiplier test, and an Engle-Ng joint test for asymmetry in conditional volatility; the model with the best combination of these criteria (Model 5) is used for the paper's main conclusions.

## Results

- Wednesday has the highest mean futures return (0.2561) among weekdays, versus -0.4408 on Tuesday and -0.7192 on Thursday, and the Wednesday dummy is significant at the 5% level in the baseline GARCH(1,1) model (coefficient 0.9192).
- The VPIN of all investors combined has no statistically significant effect on futures returns, either on its own (Model 2) or without the Wednesday interaction in Model 3 (coefficient -20.5303, not significant).
- The VPIN of all investors interacted with the Wednesday dummy is significantly positive at the 5% level in Model 3 (coefficient 13.8527), indicating informed trading affects returns specifically on Wednesdays.
- In Model 4, the VPIN of domestic institutional investors is not significant, but the VPIN of foreign institutional investors is significantly positive at the 5% level (coefficient 7.2557).
- In Model 5 (the authors' preferred specification), the foreign-investor VPIN remains significantly positive (coefficient 10.8144), and the domestic-investor VPIN interacted with the Wednesday dummy becomes significantly positive (coefficient 2.4425), while the foreign-investor VPIN's Wednesday interaction (-2.3743) is not significant.
- Unit-root tests (ADF and PP) reject non-stationarity for all series used, at the 1% significance level.
- Model 5 has the best combination of model-selection statistics (log-likelihood, Durbin-Watson, AIC) among the five models estimated.

## Limitations

- The sample covers a single market (TAIFEX) and a single crisis window (January 2, 2008 to March 18, 2009), so results may not generalize to other markets or calmer periods.
- The authors note that the returns on the instruments studied sit close to Taiwan's daily 7% price-move limit (observed range -7.0000 to 6.9906), which the paper flags as a feature of the data without directly testing its effect on the VPIN results.
- Reader note: the paper does not report an out-of-sample or holdout test of the GARCH regression models; all reported significance is in-sample.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/vpin|VPIN]]

## Citation

Yen-Hsien Lee, Wen-Chien Liu, Chia-Lin Hsieh (2017). Informed Trading of Futures Markets During the Financial Crisis: Evidence from the VPIN. International Journal of Economics and Finance, Vol. 9, No. 9.

DOI: 10.5539/ijef.v9n9p123

Text ingested: `markdown_output/lee-2017-informed-trading-futures-markets-during-financial.md`, converted from `raw/ofi-event-clock/lee-2017-informed-trading-futures-markets-during-financial.pdf`.

Coverage of this summary: Read the whole paper: abstract, introduction, literature review and hypothesis development, data and methodology (VPIN and GARCH model specifications, Models 1-5), the full empirical results section with all five tables, conclusion, references, and notes.

Known problems with the input: The markdown conversion garbles several inline mathematical subscripts and superscripts (e.g., VPIN and coefficient subscripts run together without spacing), so all numeric coefficients and variable definitions were cross-checked directly against the regression tables rather than the surrounding prose; The specific futures contract(s) traded on TAIFEX are not clearly named in the converted text; only generic references to 'futures contract' and 'Taiwan stock index futures' appear.
<!-- AUTHORED REGION END -->