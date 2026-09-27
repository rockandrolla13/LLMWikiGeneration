---
authors:
- Antonio Scalia
content_hash: sha256:6202e6127a2b505051afc4c07197ab7cac8ae39b4e939156155786bab9bccd4d
created: 2026-09-27 01:47:00+00:00
page_id: sources/scalia-1998-information-transmission-causality-italian-treasury-bond-market
page_type: source
publication_venue: Journal of Empirical Finance
related:
- concepts/trade-clock
- concepts/market-microstructure
- concepts/bond-liquidity
- concepts/high-frequency-data
- concepts/informed-trading
- concepts/backtesting
- concepts/trade-classification
revision_id: 1
schema_version: 2
source_hash: sha256:c6e5c2545cd74a239e6e125041a85c73dc4732f516ee4ff0f1c163810cbb0983
source_path: markdown_output/scalia-1998-information-transmission-causality-italian-treasury-bond-market.md
source_type: paper
tags:
- treasury-bonds
- lead-lag
- causality
- market-efficiency
- futures-cash-basis
- intraday-data
- italy
- trading-rule
- clock-trade
- asset-bonds-rates
- added-by-hand
title: Information transmission and causality in the Italian Treasury bond market
updated: '2026-09-27T01:47:00Z'
uuid: a6e061c3-58a6-519f-8779-fcb2a3684a5b
year: 1998
---

<!-- AUTHORED REGION START -->
# Information transmission and causality in the Italian Treasury bond market

## Summary

The paper studies the lead-lag relationship between the Italian Treasury bond (BTP) cash market, traded on the domestic MTS screen network, and the BTP futures contract traded at LIFFE in London. Using intraday, trade-by-trade data from January 1992 through June 1993, it applies a two-sided Sims-style causality test, regressing innovations in one market's price changes on lagged, contemporaneous and leading innovations of the other market, separately for cash sales and cash buys and across three sub-periods.

The cash price series is built in transaction time (trade-to-trade) rather than at fixed calendar intervals, because non-trading frequency in the cash market is too high for short calendar windows; the matching futures regressors are built at 5-minute or 15-minute calendar intervals depending on which direction of causality is being tested. Estimation uses feasible generalised least squares after time-weighting and ARMA filtering to remove heteroskedasticity and residual autocorrelation.

The results show a lead from futures to cash of 15 to 30 minutes, consistent with prior stock-index studies, but also a comparably sized and comparably long lead from cash to futures, which the author presents as the paper's principal new finding. Contemporaneous correlation between the two markets rises steadily across the sample period, and both the contemporaneous correlation and the cash lead strengthen further on days with large adverse price moves.

A simple trading rule that buys or sells the cash bond whenever the futures market moves beyond a threshold is then backtested across many combinations of lookback window and threshold. Average daily profits net of transaction costs are essentially zero or negative in almost every case, which the author interprets as evidence that the futures lead cannot be exploited and that the cash market is weak-form efficient with respect to LIFFE prices.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Cash BTP prices are sampled trade-by-trade (separately for public sales and public buys) in transaction time rather than fixed calendar time, because the frequency of non-trading at 5-minute intervals in the cash market always exceeds 42%. To test cash-leads-futures causality, lagged and leading regressors are built from futures price changes at 5-minute calendar intervals matched around each cash trade; to test futures-leads-cash causality, lagged and leading regressors are built from cash price changes at 15-minute calendar intervals matched around each futures move. Five lagged/leading terms are used in the first regression and three in the second, so the effective prediction horizon studied is up to about 20-30 minutes.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** Buoni del Tesoro Poliennali (BTP) cash bonds deliverable into the LIFFE BTP futures contract, and the LIFFE BTP futures contract itself (notional 12% 10-year BTP, 200 million ITL nominal value per contract).
- **Venue:** Mercato Telematico dei Titoli di Stato (MTS) for cash trades; London International Financial Futures Exchange (LIFFE) for futures.
- **Period:** January 1992 through June 1993, split into three sub-periods: January-May 1992, June-December 1992, and January-June 1993.
- **Granularity:** Intraday, trade-by-trade; each cash trade is marked to the nearest second and flagged as a public sale (bid) or public buy (ask); futures trades are marked to the nearest second from LIFFE Time and Sales files.

## Features and Measures

- **Sims two-sided lead-lag regression.** Regresses innovations of one market's price changes on lagged, contemporaneous and leading innovations of the other market's price changes, so that significant leading coefficients indicate causality running from the regressor market to the dependent market.
- **Cost-of-carry adjusted cash-futures basis.** A no-arbitrage relationship linking the futures (forward) price to the cash price via the financing cost to delivery and a bond-specific conversion factor, used to align cash and futures price changes before the causality regressions.
- **Threshold-triggered intraday trading rule.** A rule that buys or sells the minimum-size cash bond whenever a cumulative or single largest futures price move over the last z minutes exceeds a filter q, then closes the position at the next available opposite-side trade.

## Method

The paper estimates Sims-style two-sided regressions of cash price innovations on lagged, contemporaneous and leading futures innovations, and the mirror-image regression of futures on cash, using feasible generalised least squares. Time-weighting corrects for heteroskedasticity arising from uneven spacing between trades, and an ARMA filter (most often ARMA(2,2)) removes residual autocorrelation. Causality is judged from an F-test on the joint significance of the leading coefficients, with Durbin-Watson and Q-statistics reported as residual diagnostics. A further set of regressions interacts the lagged/leading coefficients with a dummy for bad-news versus good-news days, defined from the top and bottom quintiles of daily cumulative price change. Weak-form efficiency of the cash market is then assessed by backtesting two variants of the trading rule across a grid of lookback windows (z = 1, 3, 5, 10, 15 minutes) and filter thresholds (q = 0.05 to 0.30), reporting the mean and standard deviation of net daily cash-market profit.

## Results

- Contemporaneous correlation between cash and futures price changes rose over the sample, from 0.35 in period 1 to 0.59 in period 3 using sales, and from 0.33 to 0.55 using buys.
- Futures prices lead cash prices by 15 to 30 minutes, with the largest lead coefficient in the first 15 minutes falling in the range 0.20-0.29.
- Cash prices also lead futures prices, with cumulative lead coefficients of 0.21 (period 1), 0.10 (period 2) and 0.11 (period 3), extending up to about 20 minutes; the author describes this cash-to-futures lead as the paper's main new finding.
- On bad-news days the cash lead and the contemporaneous correlation both strengthen: the cash lead reaches 0.14 versus 0.11 on good-news days in period 2, and the contemporaneous correlation rises to 0.60 (cash-on-futures regression) and 0.79 (futures-on-cash regression) in period 3.
- On bad-news days the futures lead shortens instead, with the first lead coefficient ranging from -0.03 to -0.19 across periods.
- A trading rule triggered by futures price moves produced nil or negative average daily profit in almost every filter/window combination; the one positive case (filter 0.20, lookback of 5 minutes, period 2) gave a mean daily profit of 1 million ITL with a standard deviation of 4 million ITL.
- The author concludes that the Italian cash market is weak-form efficient with respect to LIFFE futures prices once transaction costs are accounted for.

## Limitations

- The sample covers a single bond-futures pair (BTP cash versus LIFFE BTP futures) over January 1992-June 1993.
- Non-trading frequency above 42% in the cash market forced the author to abandon fixed 5-minute sampling for cash prices in favour of transaction-time sampling.
- The trading rule implicitly assumes there is a further trade available on the required side to close each position, and halts otherwise.
- Reader note: most results focus on a single cheapest-to-deliver bond per day rather than the full basket of deliverable bonds, though a most-liquid-bond robustness check is mentioned as giving similar results.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bond-liquidity|bond liquidity]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/backtesting|backtesting]]
- [[concepts/trade-classification|trade classification]]

## Citation

Antonio Scalia (1998). Information transmission and causality in the Italian Treasury bond market. Journal of Empirical Finance.

Text ingested: `markdown_output/scalia-1998-information-transmission-causality-italian-treasury-bond-market.md`, converted from `raw/ofi-event-clock/scalia-1998-information-transmission-causality-italian-treasury-bond-market.pdf`.

Coverage of this summary: Read the full markdown file end to end, including the introduction, the no-arbitrage/causality background, the data description and summary statistics, the causality methodology and results, the good-news/bad-news results, the trading-rule efficiency test, and the conclusion.

Known problems with the input: The OCR conversion renders minus signs as the letter 'y' and parentheses/apostrophes as stray characters like 'Ž' and '.' throughout; negative numbers in results (e.g. lead coefficients on bad-news days) are inferred from this consistent pattern; Most equations are shown in the markdown only as 'picture intentionally omitted', so the regression and no-arbitrage equations are described qualitatively rather than reproduced in symbol form.
<!-- AUTHORED REGION END -->