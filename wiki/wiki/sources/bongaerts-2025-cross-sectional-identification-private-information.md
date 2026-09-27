---
authors:
- Dion Bongaerts
- Dominik Rösch
- Mathijs van Dijk
content_hash: sha256:dc3c8b6193c809ccfd136e6062fafb04cfce94db9f781ddb238a5f3667b22980
created: 2026-09-27 01:47:00+00:00
page_id: sources/bongaerts-2025-cross-sectional-identification-private-information
page_type: source
publication_venue: Review of Asset Pricing Studies
related:
- concepts/informed-trading
- concepts/price-impact
- concepts/order-imbalance
- concepts/market-microstructure
- concepts/adverse-selection
- concepts/trade-classification
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:36467e146281af5bf531739f79b3ec34cdbc40482ffcfa1007e30e8c8094c902
source_path: markdown_output/bongaerts-2025-cross-sectional-identification-private-information.md
source_type: paper
tags:
- private-information
- informed-trading
- price-impact
- order-imbalance
- market-microstructure
- event-study
- return-reversal
- equities
- clock-calendar
- asset-equity
- harvest-relevant
title: Cross-sectional identification of private information
updated: '2026-09-27T01:47:00Z'
uuid: 07811f34-d832-56d7-852b-8016c9ae1543
year: 2026
---

<!-- AUTHORED REGION START -->
# Cross-sectional identification of private information

## Summary

The paper asks how to recover a security's private information shock -- the information driving informed trading -- from ordinary market data, rather than relying on Kyle's (1985) lambda alone (which only measures expected asymmetric information, not realized, signed trading) or on PIN-style probability models (which need many days of data and lose directional and timely signal). It builds a multi-security trade-optimization model in which strategic investors, hit by liquidity and private-information shocks, spread their uninformed trading across securities inversely to price impact, which lets the paper separate uninformed from informed order flow using one benchmark security assumed free of private information.

The main theoretical result is that a security's private information shock can be recovered from its price impact (lambda) times its order imbalance (OIB), net of a correction term from the benchmark security; in cross-sectional applications over the same period the correction term is common to all securities and drops out, giving the simple measure lambda times OIB. The paper estimates this measure daily for NYSE stocks from 2001 to 2014 using intraday quote and trade data.

Empirically, lambda times OIB behaves as a private-information proxy should: it is larger in magnitude for smaller, more dispersed-analyst-forecast stocks; it peaks cleanly around insider Form-4 filings without the false positives shown by OIB, lambda, PIN, or a machine-learning informed-trading measure; it is positively related to same-day returns; it predicts weaker return reversals and higher future volatility; and it rises before M&A announcements and after an exogenous loss of analyst coverage.

What is new is a theory-grounded, cross-sectional, high-frequency, and directional (signed) private information measure that needs no long time-series per security and requires only price impact and order imbalance -- both straightforward to estimate -- rather than a structural likelihood model.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Analysis is at the daily-stock level: each stock-day's order imbalance (OIB) is the dollar volume of Lee-Ready buyer-initiated minus seller-initiated trades over the trading day, and its expected price impact (lambda) is a 20-day trailing moving average of daily lambda estimates from a regression of five-minute mid-quote returns on signed dollar volume in the same five-minute interval. The private information measure lambda times OIB is then formed at the daily frequency. Prediction and event horizons vary by test: same-day returns, next-day return and volatility regressions, and multi-day event windows around Form-4 filings, M&A announcements, and analyst-coverage terminations.

## Data

- **Asset class:** Equities
- **Instruments:** 1,388 NYSE-listed common stocks (CRSP share codes 10 and 11)
- **Venue:** NYSE and other US exchanges (consolidated NBBO quotes and trades from Thomson Reuters Tick History)
- **Period:** February 1, 2001 to end of 2014
- **Granularity:** Intraday quotes and trades aggregated to five-minute bins for lambda estimation and to daily stock-day observations for OIB and lambda times OIB; final panel averages 1,992 daily observations per stock, built from 18,626,168,999 signed trades

## Features and Measures

- **Order imbalance (OIB).** The dollar volume of buyer-initiated minus seller-initiated trades for a stock over a trading day, with trades signed using the Lee and Ready (1991) algorithm.
- **Price impact (lambda).** A stock's expected transaction-cost sensitivity, estimated from a regression of five-minute mid-quote log-returns on signed dollar trading volume in the same interval, averaged over the trailing 20 trading days.
- **lambda x OIB (private information measure).** The product of a stock's price impact and its order imbalance; theoretically shown to rank securities by their private information shock once uninformed order flow is purged using an information-free benchmark security.
- **lambda x |OIB| (absolute private information measure).** The absolute-value version of lambda times OIB, used to measure the magnitude rather than the direction of private information in tests such as return reversals and volatility prediction.

## Method

The paper first builds a one-period model in which many risk-neutral investors face investor-specific liquidity shocks and private-information shocks and choose trades across securities to maximize speculative profit net of quadratic transaction costs (linear price impact), subject to a budget constraint. Solving the model shows that both liquidity-motivated and funding (financing) trades are spread across securities in inverse proportion to each security's price impact, so all uninformed order flow can be summarized by one implicit market-wide liquidity shock. Assuming one benchmark security carries no private information shock, the model yields a closed-form expression for every other security's private information shock as price impact times aggregate order flow, net of a correction term equal to the benchmark's price impact times its own order flow; in cross-sectional comparisons over the same period this correction term drops out, leaving the simplified measure lambda times OIB.

Empirically, daily lambda and OIB are estimated for NYSE stocks from intraday quotes and trades, and the resulting lambda times OIB (or its absolute value) is validated in six ways: quintile sorts of stock characteristics; regressions of the measure and of comparison measures (OIB, lambda, PIN, ITI) on indicators for Form-4 insider-trade filings; Fama-MacBeth regressions of daily returns and of future return volatility on the measure and controls; double-sorted portfolio tests of return-reversal strategies across asset-pricing factor models (CAPM, Fama-French three-factor, Carhart four-factor, and a five-factor model adding short-term reversal); event-study regressions of cumulative abnormal returns around M&A announcements; and a difference-in-differences design around an exogenous loss of analyst coverage.

## Results

- Stocks in the top quintile of absolute private information (lambda x |OIB|) have median return volatility of 4.50% versus 1.76% for the bottom quintile, and roughly double the analyst dispersion (0.04 vs 0.02).
- In Fama-MacBeth regressions of daily returns, lambda x OIB has a positive, significant coefficient beyond lambda and OIB individually; a one-standard-deviation increase in lambda x OIB is associated with a 0.19 standard-deviation increase in same-day returns.
- Return reversals are much weaker after large absolute lambda x OIB days: a five-factor reversal-strategy alpha of about 7-8 basis points per day (around 18% per annum, t-stats greater than 4) for low-|lambda x OIB| stocks falls to about 0.7 basis point per day (t-stat 0.34, statistically indistinguishable from zero) for high-|lambda x OIB| stocks; the difference is 6.3 basis points per day (t-stat 3.59).
- Lagged lambda x |OIB| positively predicts next-day return volatility even after controlling for lagged returns, lagged volatility, lambda, and |OIB| separately.
- lambda x OIB peaks about two days before Form-4 insider-trade filings and shows no spurious peaks on placebo days, unlike OIB, lambda alone, PIN, or the ITI machine-learning measure, which all show weaker precision or the wrong sign.
- Around 350 M&A target-firm events (174 with a significant pre-event run-up used in the main analysis), lambda falls from about 80 basis points per $1 million traded before the announcement to about 15 basis points per $1 million after it, while lambda x OIB is strongly positive pre-announcement (OIB around $2 million per day) and close to zero afterward; cumulative lambda x OIB over the pre-event window explains 5% to 20% of cross-sectional variation in the target's price run-up (which averages about 25% over the full [-10,+10] event window, with an 8% pre-event run-up).
- After the exogenous closure of 43 U.S. brokerage research departments (2000-2008) that ended analyst coverage for some stocks, a difference-in-differences test finds lambda x |OIB| rose for affected stocks by about 3% of its pre-event average, significant in the 180-day event window (out of 90-, 180-, and 360-day windows tested).

## Limitations

- The identification requires one 'benchmark' security assumed free of private information; if none exists, only the rank ordering of lambda x OIB (not the exact private information shock) is preserved.
- The baseline model assumes homogeneous, rational investors and exogenous (partial-equilibrium) price impact; a full equilibrium with endogenous, cross-sectionally linear price impact only exists under restrictive conditions, addressed separately in the Internet Appendix.
- The simplified cross-sectional measure lambda x OIB omits a correction term for uninformed order flow, so its sign and magnitude (though not its cross-sectional ranking) can be an imperfect proxy for private information on days when that correction term is large.
- The sample is limited to NYSE-listed common stocks over 2001-2014; results may not generalize to other venues, asset classes, or time periods.
- Reader note: because lambda is estimated with a 20-day trailing moving average, the measure reacts slowly to abrupt shifts in price impact -- the paper itself switches to same-day lambda around M&A announcements for this reason.

## Related

- [[concepts/informed-trading|informed trading]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/vpin|VPIN]]

## Citation

Dion Bongaerts, Dominik Rösch, Mathijs van Dijk (2026). Cross-sectional identification of private information. Review of Asset Pricing Studies.

DOI: 10.1093/rapstu/raaf009

Text ingested: `markdown_output/bongaerts-2025-cross-sectional-identification-private-information.md`, converted from `raw/ofi-event-clock/bongaerts-2025-cross-sectional-identification-private-information.pdf`.

Coverage of this summary: Read the full converted markdown: cover/citation page, abstract, introduction, full model section (Sections 2.1-2.3), data and variable construction (Section 3), all seven empirical results subsections (Section 4.1-4.7), limitations and extensions (Section 5), and the conclusion (Section 6); skimmed only the appendix proofs and reference list.

Known problems with the input: Document mixes an EUR institutional-repository cover page (citing a 2026 published version in Review of Asset Pricing Studies) with a paper body dated May 5, 2025; used 2026 as the year since that matches the formal published citation, but this is not certain -- verify against the actual publication; Sample size for NYSE stocks is stated inconsistently in the source: 1,338 in the introduction versus 1,388 in the data and summary-statistics sections; used 1,388, the value used consistently in Sections 3-4; Most equations and several tables are rendered as omitted pictures or reflowed table markup in the markdown conversion; extraction relies on the surrounding prose description of results rather than the raw table cells.
<!-- AUTHORED REGION END -->