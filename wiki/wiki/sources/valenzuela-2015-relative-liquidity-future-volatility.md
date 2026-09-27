---
authors:
- Marcela Valenzuela
- Ilknur Zer
- Piotr Fryzlewicz
- Thorsten Rheinlander
content_hash: sha256:d60e41009f87991c4c04f66f1994c8cda9a55ad3c7468e229517ca48423b4b7a
created: 2026-09-27 01:47:00+00:00
page_id: sources/valenzuela-2015-relative-liquidity-future-volatility
page_type: source
publication_venue: Journal of Financial Markets
related:
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/market-microstructure-noise
- concepts/realized-variance
- concepts/amihud-illiquidity
- concepts/bid-ask-spread
- concepts/high-frequency-data
- concepts/fill-probability
revision_id: 1
schema_version: 2
source_hash: sha256:0f300cbfbbb9b0aa7c0c3549f058137f6a62180e5908df9e9b45559741e5e9d0
source_path: markdown_output/valenzuela-2015-relative-liquidity-future-volatility.md
source_type: paper
tags:
- limit-order-book
- volatility-prediction
- principal-component-analysis
- market-microstructure
- order-book-depth
- istanbul-stock-exchange
- out-of-sample-forecasting
- liquidity
- clock-calendar
- asset-equity
- harvest-relevant
title: Relative liquidity and future volatility
updated: '2026-09-27T01:47:00Z'
uuid: 9d52ff77-0caf-5cf7-a4f9-e4ab60315948
year: 2015
---

<!-- AUTHORED REGION START -->
# Relative liquidity and future volatility

## Summary

The paper asks whether the way orders are spread across a limit order book, rather than just how much volume sits at the best quotes, carries information about where prices are heading. It is motivated by a theoretical prediction that when resting orders pile up far from the best quotes rather than close to them, that pattern signals disagreement among traders about the correct price, and disagreement should be followed by larger price moves.

To test this, the authors build a new measure, relative liquidity (RLIQ). For each stock they compute the empirical distribution of resting order volume across price distances from the best quote, average this distribution across stocks to get a market-wide shape, and then take the first principal component of that shape (separately for the buy and sell sides) as a single summary number. The weighting this produces is not chosen by hand; it comes directly from the principal component analysis, and it loads positively on volume near the top of the book and negatively on volume farther away. RLIQ is then used as a predictor of intraday market volatility, measured with a two-scale realized volatility estimator designed to be robust to microstructure noise, in standard predictive regressions that include lagged volatility and intraday time-of-day dummies.

Using reconstructed order and trade books for the largest stocks on the Istanbul Stock Exchange, the paper finds a strong, negative, and statistically robust relationship: when liquidity provision shifts toward the top of the book (higher RLIQ) subsequent volatility falls, and when it accumulates further away, volatility rises. The relationship survives the inclusion of alternative liquidity measures such as the spread, book slope, and standard depth at each quote, and it also shows up out-of-sample, with the predictive power decaying gradually as the forecast horizon extends.

What is new relative to prior liquidity-based volatility studies is the focus on the relative, rather than absolute, concentration of the book, and the fact that the relationship is checked at the level of the whole market rather than one stock at a time; the authors show it holds for most individual names too, not just an average across a few large or unusual stocks.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The reconstructed limit order book is sampled at fixed wall-clock points, every 15 minutes across the trading day (a 30-minute version is also tested), giving 21 trading intervals per day. The dependent variable is the volatility realized over the following interval, and the analysis is extended to look at horizons of several intervals ahead, up to 165 minutes.

## Data

- **Asset class:** Equities
- **Instruments:** the 30 largest constituent stocks of the Istanbul Stock Exchange ISE-30 index
- **Venue:** Istanbul Stock Exchange (ISE), a fully centralized, purely order-driven exchange
- **Period:** June and July 2008
- **Granularity:** order and trade books time-stamped to the second, used to reconstruct the full limit order book at any point in time; the reconstructed book is then sampled at 15-minute (and, as a check, 30-minute) intervals

## Features and Measures

- **RLIQ (relative liquidity).** The first principal component of the aggregate limit order book probability density function, separately for the buy and sell sides, summarizing whether resting volume is concentrated near the best quotes or spread further away.
- **Limit order book distribution (indPDF / avgPDF).** The share of a stock's total resting order volume found at each tick distance from the best quote, and the cross-sectional average of this share across all sample stocks.
- **SLOPE.** The slope of the limit order book, describing how sensitive the quantity supplied at different quotes is to price.
- **relSPR (relative spread).** The bid-ask spread divided by the mid-quote price.
- **DEPTH_i.** The total volume of buy or sell orders waiting at the i-th best bid or ask price level.
- **logQS (log quote slope).** A measure of how steeply the best bid and ask quotes are set relative to each other; a lower value indicates a flatter, more liquid market.
- **AMR (Amihud illiquidity ratio).** The absolute stock return divided by turnover, used as a standard illiquidity proxy.
- **DHW illiquidity measure.** The estimated cost of simultaneously buying and selling a fixed quantity of shares, based on the accumulated volume in the book.

## Method

The core test is a predictive regression of next-interval market (and, separately, individual-stock) volatility on RLIQ, lagged volatility, and intraday dummy variables, with explanatory variables standardized so coefficients are comparable. Volatility is measured with the two-scale realized volatility estimator, chosen because it corrects for the bias that microstructure noise introduces into simple realized-variance estimates; jump-robust and alternative estimators are also used as checks. Significance is assessed with Newey-West standard errors to allow for autocorrelation.

The authors extend the baseline regression by adding standard liquidity controls (spread, book slope, depth at each of the first five quotes, Amihud ratio, log quote slope, and the Domowitz-Hansch-Wang cost measure), by extending the prediction horizon out to eleven future intervals, and by running the same regression separately for each stock with stock fixed effects. Out-of-sample performance is evaluated with a recursive estimation scheme over two training-window lengths, comparing squared forecast errors against a benchmark that forecasts with the historical sample mean, and testing the difference with the Diebold-Mariano test and an out-of-sample R-squared measure. Robustness checks vary the number of price levels considered, the sampling frequency, the cross-sectional weighting scheme used to aggregate across stocks, and the functional form of the regression, and also compare the first principal component against using more principal components or a LASSO-selected set of price-level variables directly.

## Results

- A one standard deviation increase in RLIQ on the buy side lowers 15-minutes-ahead market volatility by 4.4 bps, against a mean volatility level of 19 bps.
- RLIQ alone (both sides) explains about 16% of the variation in one-period-ahead volatility; adding lagged volatility and intraday dummies raises the adjusted R-squared to over 25%, and to 29.53% once all liquidity and trading-activity controls are added.
- Out-of-sample, RLIQ on the buy side achieves a 12.9% out-of-sample R-squared for one-period-ahead volatility, with predictive power decaying but remaining significant up to 75 minutes ahead.
- Combining RLIQ with the relative spread or the log quote slope raises the out-of-sample R-squared above 24% for the nearest forecast horizon.
- Adding standard depth measures at the best five quotes alongside RLIQ raises adjusted R-squared only to 26.11%, and RLIQ remains the strongest predictor.
- At the individual-stock level, RLIQ on the buy side is a significant negative predictor of volatility for 87% of stocks, compared with 37% of stocks on the sell side.
- The buy side of the book is consistently more informative about future volatility than the sell side, both in the market-level and individual-stock regressions.
- The negative relationship between RLIQ and future volatility holds up when using 20 or 30 price levels instead of 10, 30-minute instead of 15-minute sampling, value- and trade-weighted aggregation, and jump-robust or log-transformed volatility measures.

## Limitations

- The sample covers a single exchange (the Istanbul Stock Exchange) over two months, June and July 2008.
- The chosen volatility estimator (TSRV) corrects for microstructure noise but is not itself robust to jumps, though the authors separately check jump-robust estimators.
- The analysis is confined to equities on a purely order-driven market with no market makers; the authors do not test other asset classes or hybrid dealer markets.
- Reader note: the sample window is short (two months) and pre-dates more recent high-frequency trading conditions, which may limit how far the magnitudes generalize.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/amihud-illiquidity|amihud illiquidity]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/fill-probability|fill probability]]

## Citation

Marcela Valenzuela, Ilknur Zer, Piotr Fryzlewicz, Thorsten Rheinlander (2015). Relative liquidity and future volatility. Journal of Financial Markets.

DOI: 10.1016/j.finmar.2015.03.001

Text ingested: `markdown_output/valenzuela-2015-relative-liquidity-future-volatility.md`, converted from `raw/ofi-event-clock/valenzuela-2015-relative-liquidity-future-volatility.pdf`.

Coverage of this summary: Read the entire markdown file, including the abstract, introduction, data and market description, the RLIQ construction section, the predictive methodology, all empirical and robustness subsections, the conclusion, and the appendix worked example.

Known problems with the input: The PDF-to-markdown conversion replaced all equations and figures with 'picture omitted' placeholders, so exact formula notation (e.g. for TSRV or the out-of-sample R-squared) is described only in the surrounding prose, not reproduced from the original equations.
<!-- AUTHORED REGION END -->