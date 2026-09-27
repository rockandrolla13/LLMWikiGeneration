---
authors:
- Shengxiong Wu
content_hash: sha256:ef1994127c9442109ce69cfc5c84e694c3e28e8041e767521f75bc903b03cf63
created: 2026-09-27 01:47:00+00:00
page_id: sources/wu-2012-information-content-euro-bund-futures-options
page_type: source
publication_venue: Kent State University Graduate School of Management
related:
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/price-impact
- concepts/informed-trading
- concepts/bid-ask-spread
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:f413f7170ff9ac3465fc67f2074a972986e695b70c1b61632f0873fe21efe9a3
source_path: markdown_output/wu-2012-information-content-euro-bund-futures-options.md
source_type: paper
tags:
- euro-bund
- futures-options
- book-imbalance
- price-discovery
- eurex
- interest-rate-futures
- principal-component-analysis
- clock-calendar
- asset-bonds-rates
- harvest-relevant
title: The Information Content of the Euro-Bund Futures Option Markets
updated: '2026-09-27T01:47:00Z'
uuid: 69c9d0b5-7af4-5852-b086-44ce5c4c48d7
year: 2012
---

<!-- AUTHORED REGION START -->
# The Information Content of the Euro-Bund Futures Option Markets

## Summary

Prior empirical work on price discovery between a security and its derivatives mostly looks at option trading volume; this dissertation instead asks whether the order book of an interest-rate futures options market carries information about the price of the underlying futures contract, a question the author states had not been directly tested for interest-rate derivatives before.

The analysis uses Eurex's historical order book for Euro-Bund futures and futures options from January 02, 2007 to June 30, 2007, rebuilt from order and trade records logged at 10-millisecond resolution and then sampled at one-minute intervals. Principal component analysis reduces the cumulative bid and ask quote sizes at up to 10 price steps on each side of the book to a single common factor, and next-minute futures returns are regressed on this factor together with net trade (order) flow in the futures, call and put markets, separately for the full sample and for out-of-the-money, at-the-money and in-the-money option subsamples.

The best-level book imbalance in Euro-Bund futures at-the-money (ATM) options is significantly related to next-minute futures returns, but book imbalance for out-of-the-money and in-the-money options is not, and imbalance from price steps beyond the best level adds nothing further. The ATM effect holds only when the futures-option bid-ask spread is low and disappears when trading cost is high, and it is the ATM put side rather than the call side that carries the signal, a pattern that becomes especially strong in the second half of the sample, a period of rising interest rates and more negative news surprises about rate risk.

The main contributions the author claims are: this is presented as the first look at order-book-level (rather than volume-based) information content in an interest-rate futures options market; trade direction is identified directly from Eurex's own buy/sell and aggressive/passive flags rather than inferred with algorithms such as Lee and Ready; and the results tie price discovery to the joint role of option leverage (via moneyness) and relative trading cost between the futures and its options.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Book imbalance and net trade flow are computed at the end of each one-minute interval on a calendar clock running from 9:00 to 18:00 CET, using order book and trade records reconstructed at 10-millisecond resolution. The predicted outcome is the one-minute-ahead log return of the Euro-Bund futures mid-quote price; a five-minute version of the same design is run as a robustness check.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** Euro-Bund futures and American-style Euro-Bund futures options (calls and puts) traded on Eurex
- **Venue:** Eurex
- **Period:** January 02, 2007 to June 30, 2007 (101 front-month trading days)
- **Granularity:** Order book and trade records at 10-millisecond resolution, aggregated into one-minute (and, for robustness, five-minute) intervals

## Features and Measures

- **Step-wise quote imbalance (OI).** At a given price step of the order book, the scaled difference between the ask size and the bid size at that step, normalized by their sum; a positive value means more supply than demand at that step.
- **PCA common factor for book imbalance.** A single factor extracted by principal component analysis from the cumulative bid and ask quote sizes across several price steps, used as one aggregate measure of order book imbalance instead of tracking each step separately.
- **Net trade volume (order flow).** Buyer-initiated trade volume minus seller-initiated trade volume within a one-minute interval, with buy/sell direction identified directly from Eurex's own buying/selling and aggressive/passive trade flags.
- **Price-impact-based imbalance.** A book imbalance measure built from the price impact of a hypothetical market order of a given size on the bid and ask sides, defined from the gap between the volume-weighted execution price and the mid-quote.
- **Moneyness classification (OTM/ATM/ITM).** Options grouped into out-of-the-money, at-the-money, and in-the-money buckets by the ratio of the underlying mid-quote futures price to the option's exercise price, used as a proxy for the leverage the option offers.

## Method

The paper first strips expected components out of one-minute Euro-Bund futures returns using an autoregressive filter that includes hourly dummies and a lag length chosen by the Akaike Information Criterion. It then applies principal component analysis to the logarithm of cumulative bid and ask quote sizes at up to 10 price steps, selecting the common factor (the second principal component) and the price-step depth (the best 5 steps) that give the strongest regression fit against step-wise quote imbalances and the strongest explanatory power for next-minute futures returns. The core test regresses the one-minute-ahead futures return on lagged net trade volume in futures, calls and puts, and on lagged book-imbalance factors for calls and puts at the best price level, estimated separately for the full sample and for out-of-the-money, at-the-money and in-the-money subsamples, with the significance of the option book-imbalance terms assessed by a joint F-test.

Robustness checks re-run the same regression after splitting the at-the-money sample by bid-ask spread and by calendar period, after substituting alternative book-imbalance measures built from step-wise quote imbalance and from price impact, and after moving to five-minute sampling. A Breusch-Godfrey test is used to check that the regression residuals are free of autocorrelation.

## Results

- Book imbalance at the best bid/ask level of the Euro-Bund futures ATM option order book is jointly significant for next-minute futures returns (p=0.041), while OTM and ITM option book imbalances are not (p=0.958 and p=0.34).
- Adding book imbalance from price steps beyond the best level does not improve the fit; the best-level imbalance already captures the information content.
- When the ATM option bid-ask spread is low, book imbalance stays jointly significant (p=0.047); when the spread widens, it loses significance (p=0.349).
- ATM put option book imbalance is the more informative side: its coefficient is statistically significant while the ATM call coefficient is not, in the main specification and most robustness checks.
- The ATM put imbalance effect concentrates in the second half of the sample (after 03/10/2007), a period of rising interest rates and more negative rate-risk news, with the joint test significant at p=0.032 versus p=0.381 in the earlier period.
- Findings are qualitatively unchanged when book imbalance is instead measured by step-wise quote imbalance or by price-impact-based imbalance, and when the sampling interval is widened to five minutes.
- A worked example shows the predicted direction from a negative book-imbalance signal matching a subsequent 7-tick (EUR 70) futures move, a size large enough to cover the bid-ask spread and commission.

## Limitations

- The author states there is no data on trader identity and no full detail on OTC block trades, so the mechanism behind the book-imbalance effect cannot be tested directly.
- The author notes the results are specific to this six-month sample period and market environment, so extrapolation to other periods is only conjectural.
- Reader note: the study covers a single underlying (Euro-Bund futures) over one six-month window in 2007, so generalization to other bond futures contracts or other periods is untested within the paper.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/price-impact|price impact]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Shengxiong Wu (2012). The Information Content of the Euro-Bund Futures Option Markets. Kent State University Graduate School of Management.

Text ingested: `markdown_output/wu-2012-information-content-euro-bund-futures-options.md`, converted from `raw/ofi-event-clock/wu-2012-information-content-euro-bund-futures-options.pdf`.

Coverage of this summary: Read the entire converted dissertation text from the title page through the conclusion and bibliography, including the literature review, data description, methodology, and all empirical results tables and their surrounding discussion.

Known problems with the input: Front matter shows two different years for the document: the title page states 'December 2011' while the author's own degree line states 'Ph.D., Kent State University, 2012'; the year field uses 2012 to match the degree-conferral year and the job's year hint; Several regression equations and figures are rendered in the converted markdown as 'picture... intentionally omitted' placeholders, so exact equation forms are not reproduced verbatim; findings here are drawn from the surrounding prose and tables instead.
<!-- AUTHORED REGION END -->