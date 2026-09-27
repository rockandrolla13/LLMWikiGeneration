---
authors:
- Victor Le Coz
- Iacopo Mastromatteo
- Damien Challet
- Michael Benzaquen
content_hash: sha256:21724a067c3ccda39ea8a0c1aea7a7d34e46386dcc9bb3225e433b25262bd351
created: 2026-09-27 01:47:00+00:00
page_id: sources/coz-2024-when-cross-impact-relevant
page_type: source
related:
- concepts/cross-impact
- concepts/price-impact
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/liquidity-risk
- concepts/bond-liquidity
revision_id: 1
schema_version: 2
source_hash: sha256:606a98748caadb7f0c949948578ea5879e5573562cab99bcfc9841b697d4331a
source_path: markdown_output/coz-2024-when-cross-impact-relevant.md
source_type: paper
tags:
- cross-impact
- price-impact
- order-flow
- limit-order-book
- interest-rate-curve
- bond-futures
- liquidity
- high-frequency-data
- clock-calendar
- asset-multi
- harvest-relevant
title: When is cross impact relevant?
updated: '2026-09-27T01:47:00Z'
uuid: dd13b6cd-423e-572d-a0ae-1094f86c67b0
year: 2024
---

<!-- AUTHORED REGION START -->
# When is cross impact relevant?

## Summary

This paper asks under what conditions a linear cross-impact model — one that predicts an asset's price changes from the signed order flow of other, correlated assets — meaningfully outperforms a single-asset (diagonal) model with no cross-asset terms, and what determines the time scale at which cross-impact is best measured.

Using tick-by-tick trades and quotes for 500 US-listed stocks, bonds, bond futures and stock-index futures over 2017-2022 (each year calibrated in-sample on the prior year and tested out-of-sample on the current year), the authors compare a diagonal model, a Maximum Likelihood (ML) cross-impact model, and a no-arbitrage Kyle cross-impact model. Goodness-of-fit is a generalized R² comparing predicted to realized price changes across 20,000 sampled asset pairs per year, chosen for uniform coverage of correlation levels; the paper studies how this fit and its optimal aggregation time scale vary with trading frequency, pairwise correlation, and liquidity (each asset's risk in dollars per time window).

Price formation occurs endogenously in highly liquid, highly traded assets, and their order flow subsequently moves the prices of correlated, less liquid instruments, with transmission speed bounded by the slower asset's trading frequency. A minimum of 10 to 20 trades in both assets is needed before cross-impact becomes reliably measurable, and cross-impact is material mainly between pairs correlated above roughly 50%, with the strongest transmission running from more liquid to less liquid assets. Applied to the US interest-rate curve, this mechanism shows the 10-year Treasury bond future acting as the dominant liquidity reservoir whose trades move the prices of cash bonds and futures across other tenors.

The contribution is a systematic, large-scale characterization of the bin-size, trading-frequency, correlation and liquidity conditions under which cross-impact matters at all, rather than assuming it always does, and a demonstration that this liquid-asset-leads mechanism challenges the standard view that long-term rates simply reflect anticipated future short-term rates.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Trades and mid-prices are binned into fixed time windows of length τ (the paper tests τ from about 1 second to 1 hour); within each window the net signed order flow and the open-to-open price change are computed, and a cross-impact matrix regresses one asset's price change on the same-window order flows of itself and other assets. Prediction is contemporaneous within the bin, and the 'optimal' bin size is chosen per asset or asset pair to maximize out-of-sample goodness-of-fit.

## Data

- **Asset class:** Several asset classes
- **Instruments:** 500 US-listed assets: stocks, sovereign cash bonds, bond futures across tenors (2Y, 5Y, 10Y, 20Y, 30Y), and stock-index futures (e.g. E-mini S&P 500)
- **Venue:** not stated
- **Period:** 2017-2022, with each year's prior year used as in-sample and the current year as out-of-sample; the interest-rate curve application restricts to 2021-2022
- **Granularity:** tick-by-tick trades and quotes, aggregated into bins ranging from about 1 second to 1 hour (5-minute bins for the correlation and liquidity analysis, 30-minute bins for the interest-rate curve application)

## Features and Measures

- **Cross-impact matrix.** A matrix relating the vector of signed order flows across assets in a time window to the vector of price changes in that window, generalizing single-asset price impact to a multi-asset setting.
- **Diagonal model.** The degenerate cross-impact model in which each asset's price change depends only on its own order flow, with no cross-asset terms; used as the no-cross-impact baseline.
- **ML (Maximum Likelihood) cross-impact model.** A cross-impact model estimated to best fit the joint price and order-flow covariance structure without imposing a no-arbitrage constraint, making it more flexible but able to admit arbitrage.
- **Kyle (multidimensional) cross-impact model.** A cross-impact model constructed to satisfy no static and no dynamic arbitrage, built from matrix square roots of the price and order-flow covariance matrices.
- **Generalized R²(M).** A goodness-of-fit score comparing model-predicted to realized price changes, weighted by a chosen positive-definite matrix M so error can be measured per-asset, in typical-deviation units, or in the return covariance matrix's own modes.
- **Liquidity measure (risk per window).** An asset's liquidity, defined as the product of its order-flow volatility and price-change volatility in dollar terms over a fixed time window, used to rank assets from illiquid to highly liquid.

## Method

For each asset pair, and for the full multi-asset system, the authors fit the diagonal, ML and Kyle cross-impact models on one year of tick data (in-sample) and evaluate them on the following year (out-of-sample), building daily estimators of price-change and order-flow volatility and correlation into the covariance and response matrices each model needs.

Model accuracy is judged with a generalized R²(M) comparing predicted to realized price changes under different weightings M (per-asset variance, or the inverse covariance matrix of returns), plus a ΔR²(M) statistic isolating the accuracy gained specifically from other assets' order flow over the single-asset diagonal baseline; pairs are drawn from 20,000 sampled combinations per year, chosen for uniform coverage of correlation levels.

The fitting exercise is repeated across a grid of bin sizes, trading frequencies, correlations and liquidity levels, and the same Kyle-model framework is then applied to a restricted sample of US sovereign cash bonds and bond futures across tenors to study the interest-rate curve specifically.

## Results

- For a single asset, goodness-of-fit R²(Iσi) rises with bin size up to a maximum typically between 10 and 100 seconds, then falls to a negligible level by 1 hour.
- A minimum of about 10 to 20 trades in an asset is required before it reaches its optimal bin size, for both the single-asset and the two-asset cross-impact model.
- Out-of-sample R²*(Iσi) for single assets rises with trading frequency, reaching around 25% at a typical trading frequency near 0.5 trades per second.
- The added accuracy from cross-sectional information rises from 0 to above 5% as pairwise correlation increases; cross-impact is material mainly for pairs correlated above roughly 50%.
- Liquidity improves single-asset goodness-of-fit from below 20% to around 30% across the sample's liquidity range; a typical asset has a liquidity level near 500 USD per 5 minutes and R²*(Iσi) around 25%.
- Average pairwise correlation across the 2017-2022 US sample is about 25%, and at that level pairwise cross-impact explains only a small share of price variance.
- In the interest-rate curve application (2021-2022), the 5-year cash bond's own trades explain 11.8% of its price-variance, rising to 45.2% once all instruments' trades are included.
- Out-of-sample performance of the more flexible ML model exceeds that of the no-arbitrage Kyle model, indicating market frictions such as spreads and fees partially violate the no-arbitrage assumption in practice.

## Limitations

- The linear cross-impact framework is invalidated at large order-flow sizes and long time scales by a genuinely non-linear (sigmoid) price-impact relationship, and by the auto-correlation of signed order flow, per the authors' own appendix tests.
- The main text refers to full coefficient estimates and diagnostics as available only in supplementary materials, so some robustness detail cannot be checked from this file.
- The interest-rate curve application is restricted to US sovereign cash bonds and bond futures for 2021-2022 only.
- Reader note: the study reports only two applied domains (a broad 500-asset cross-section and the interest-rate curve); results for other cross-market pairs (e.g. equities versus their index futures) are not reported.

## Related

- [[concepts/cross-impact|cross impact]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/bond-liquidity|bond liquidity]]

## Citation

Victor Le Coz, Iacopo Mastromatteo, Damien Challet, Michael Benzaquen (2024). When is cross impact relevant?.

DOI: 10.1080/14697688.2024.2302827

Text ingested: `markdown_output/coz-2024-when-cross-impact-relevant.md`, converted from `raw/ofi-event-clock/coz-2024-when-cross-impact-relevant.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, notations, modeling framework, methodology, all results subsections (bin size, trading frequency, correlation, liquidity, discussion), the interest-rate-curve application and Kyle matrix analysis, and the conclusion; the reference list was scanned but not read in detail.

Known problems with the input: Markdown conversion omits all displayed equations (replaced with 'picture omitted' placeholders) and garbles some figure-embedded tables, so exact equation forms and some fine-grained figure values are not verifiable from this file; No journal or preprint venue name is printed in the converted text (only a date), so venue is recorded as not stated.
<!-- AUTHORED REGION END -->