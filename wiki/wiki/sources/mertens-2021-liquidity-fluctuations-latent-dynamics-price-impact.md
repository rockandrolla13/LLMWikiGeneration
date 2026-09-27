---
authors:
- Luca Philippe Mertens
- Alberto Ciacci
- Fabrizio Lillo
- Giulia Livieri
content_hash: sha256:8b5b8edea5c13603c35c2e5a09cd27b72d316f32f70d067e9baa20a819c3790e
created: 2026-09-27 01:47:00+00:00
page_id: sources/mertens-2021-liquidity-fluctuations-latent-dynamics-price-impact
page_type: source
publication_venue: Quantitative Finance
related:
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-flow
- concepts/adverse-selection
- concepts/high-frequency-trading
- entities/fabrizio-lillo
revision_id: 1
schema_version: 2
source_hash: sha256:c7344803653f013aed2f18867ac0dc043f1dbeff76b41d8bf4cd4e48164dc5df
source_path: markdown_output/mertens-2021-liquidity-fluctuations-latent-dynamics-price-impact.md
source_type: paper
tags:
- price-impact
- order-flow-imbalance
- kalman-filter
- limit-order-book
- nasdaq
- intraday-liquidity
- state-space-model
- high-frequency
- clock-calendar
- asset-equity
- harvest-relevant
title: Liquidity Fluctuations and the Latent Dynamics of Price Impact
updated: '2026-09-27T01:47:00Z'
uuid: 5167d835-78fa-5c1b-912c-1cabf278b331
year: 2021
---

<!-- AUTHORED REGION START -->
# Liquidity Fluctuations and the Latent Dynamics of Price Impact

## Summary

The paper asks whether the price impact coefficient linking order flow imbalance to price changes, which the widely used Cont, Kukanov and Stoikov (2014) model estimates as fixed within an estimation window, is itself predictable at high frequency, and whether treating it as a hidden, time-varying state can improve real-time liquidity estimates and out-of-sample forecasts.

Working with LOBSTER-reconstructed NASDAQ order-book data for five large-tick stocks, the authors first show that the standard Cont et al. regression loses explanatory power as the sampling interval shortens, then propose a state-space model in which the one-minute price impact coefficient is the product of a daily level, a deterministic diurnal shape, and a latent mean-reverting autoregressive component. The model is estimated jointly by Kalman filtering and maximum likelihood, using a two-stage procedure that first estimates the diurnal pattern and then embeds it in a second filtering pass.

The fitted model explains a large share of price-change variance, recovers an intraday pattern that peaks after the opening auction and fades before the close, and shows that autoregressive persistence, once the diurnal effect is removed, is much shorter than it looks if the diurnal pattern is ignored. Real-time filtering also reduces out-of-sample forecast error relative to both a purely historical/diurnal benchmark and a re-estimated static model, and the resulting dynamic price impact measure is only moderately correlated with the static, depth-based measure, suggesting it captures additional information.

The contribution relative to Cont et al. (2014) is to treat price impact itself as a dynamic, partly unobserved variable rather than a fixed within-window coefficient, and to separate day-level, time-of-day, and short-lived stochastic sources of liquidity variation within one estimable framework, with an explicit link drawn to optimal-execution applications such as Almgren and Chriss (2001).

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Price impact is estimated on one-minute calendar bins: each trading day is split into 390 non-overlapping one-minute windows, with the first and last 30 minutes trimmed to avoid opening and closing auction effects. Mid-price change and order flow imbalance are sampled once per bin, and the price impact coefficient linking them is treated as a latent state that a Kalman filter updates each bin from the current bin's order flow imbalance; the horizon is essentially one bin ahead, and an out-of-sample exercise also uses a prior day's fitted parameters to filter and forecast the next day's bins.

## Data

- **Asset class:** Equities
- **Instruments:** Five large-tick NASDAQ 100 stocks used for the main analysis: Microsoft (MSFT), Comcast (CMCSA), Intel (INTC), Cisco (CSCO) and Apple (AAPL); three additional small-tick stocks, Amgen, Amazon and Alphabet Class C, are analysed separately in an appendix.
- **Venue:** NASDAQ, with order-book data reconstructed via LOBSTER from NASDAQ Historical TotalView-ITCH.
- **Period:** January 4, 2016 to June 30, 2016 (125 trading days), split into a 100-day in-sample/training period and a 25-day out-of-sample test period.
- **Granularity:** One-minute mid-price change and order flow imbalance series built from best-quote limit order, market order and cancellation events.

## Features and Measures

- **Order flow imbalance (OFI).** The sum of signed volume from limit order submissions, cancellations and market order executions at the best bid and ask within a time bin, following Cont et al. (2014); a positive value indicates net buying pressure.
- **Price impact coefficient.** The regression coefficient linking order flow imbalance to the contemporaneous mid-price change in a given bin; the paper treats it as unobserved and time-varying rather than fixed.
- **Diurnal price impact pattern.** A deterministic, day-invariant multiplicative factor capturing how the average level of price impact changes with the time of day.
- **Daily price impact level.** A day-specific multiplicative factor in the price impact model representing that day's average liquidity level.
- **Stochastic autoregressive price impact component.** A latent, mean-reverting autoregressive process multiplying the daily and diurnal components, meant to capture short-lived, unobserved liquidity fluctuations within the day.
- **Market depth.** The size available at the best bid and ask, used to construct a book-reconstructed benchmark measure of price impact equal to one over twice the depth.

## Method

The authors model the one-minute price impact coefficient as the product of a daily average level, a deterministic diurnal pattern, and a latent autoregressive component with Gaussian innovations. This gives a linear Gaussian state-space model estimated with a Kalman filter and maximum likelihood, in two stages: the diurnal pattern is first estimated by running the filter with a flat diurnal factor and averaging the resulting smoothed state across days, and this diurnal estimate is then embedded in a second filtering pass to obtain the final parameter and state estimates. Initial values for the daily level and residual variance come from an ordinary least squares fit of price change on order flow imbalance, and the autoregressive coefficient and its innovation variance are initialised by grid search.

To justify treating order flow imbalance as exogenous at the one-minute frequency, the paper estimates a vector autoregression in the spirit of Hasbrouck (1991) and checks whether lagged order flow has a significant effect on price changes. It also runs classical Kalman filter diagnostics (autocorrelation and normality checks on the standardized one-step-ahead forecast errors) and a Monte Carlo simulation study to check that the two-stage procedure does not introduce material bias. Performance is judged three ways: the share of price-change variance explained by the fitted impact-times-order-flow term, the mean squared error of filtered and smoothed price impact estimates against an ex-post smoothed benchmark in an out-of-sample period, and the correlation between the dynamic (Kalman) and static (Cont et al. 2014) price impact estimates.

## Results

- The dynamic price impact estimates, conditioned on order flow imbalance, explain on average 82% of the variance of real price changes.
- After removing the diurnal pattern, the autoregressive coefficient of the latent price impact component averages around 0.5, implying persistence lasting on the order of one minute rather than tens of minutes.
- Price impact follows a clear intraday shape: it peaks just after the opening auction, holds roughly flat through the middle of the day, and drops again before the close.
- Conditioning on real-time order-book information lowers the mean squared error of price impact estimates, relative to a deterministic diurnal-pattern-only benchmark, by a factor of between 0.22 and 0.83 across the five stocks over 25 out-of-sample days.
- The Kalman-filtered estimates also produce a lower out-of-sample mean squared error than a re-estimated static Cont et al. (2014) model at the same one-minute frequency.
- The correlation between the dynamic (Kalman) and static price impact measures is moderate, around 60%, suggesting the filtered measure captures liquidity information beyond quoted depth alone.
- A Hasbrouck-style vector autoregression finds a significant contemporaneous effect of order flow imbalance on price changes but mostly insignificant lagged effects, supporting the exogeneity assumption for order flow at the one-minute frequency for large-tick stocks.
- Diagnostic checks of the fitted Kalman filter's standardized forecast errors show only weak heteroskedasticity and a close-to-normal distribution, supporting the model's Gaussian assumption as an adequate approximation.

## Limitations

- The model is estimated on only five large-tick NASDAQ stocks over 125 trading days in 2016; the authors show in an appendix that the approach performs notably worse for small-tick stocks.
- The model assumes contemporaneous order flow imbalance is exogenous and does not model commonality in order flow across different assets, which the authors flag as an assumption for future work.
- The Gaussian innovation assumption is a simplification given the discrete nature of price changes at a one-minute horizon, though the authors report only weak deviations from normality in diagnostic tests.
- Reader note: the two-stage estimation procedure (diurnal pattern estimated first, then embedded in a second filtering pass) could in principle let first-stage errors propagate into the second stage, though the authors' own simulation study suggests this effect is small.
- Reader note: the out-of-sample comparison uses only 25 days per stock, a relatively short evaluation window.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow|order flow]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[entities/fabrizio-lillo|Fabrizio Lillo]]

## Citation

Luca Philippe Mertens, Alberto Ciacci, Fabrizio Lillo, Giulia Livieri (2021). Liquidity Fluctuations and the Latent Dynamics of Price Impact. Quantitative Finance.

DOI: 10.1080/14697688.2021.1947511

Text ingested: `markdown_output/mertens-2021-liquidity-fluctuations-latent-dynamics-price-impact.md`, converted from `raw/ofi-event-clock/mertens-2021-liquidity-fluctuations-latent-dynamics-price-impact.pdf`.

Coverage of this summary: Read the full converted markdown end to end, including the introduction, literature review, data description, the review of the Cont et al. (2014) model, the dynamical model and estimation section, econometric diagnostics, empirical results (in-sample, out-of-sample, and price impact versus market depth), the concluding remarks, and the appendices on data construction, estimation details, small-tick stocks, Kalman filter diagnostics and the simulation study.

Known problems with the input: Several inline equations are replaced in the converted markdown with '[picture... intentionally omitted]' placeholders, so the exact functional forms of some equations (for example the full price impact model and the Kalman recursions) are described here only from the surrounding prose, not verified symbol-by-symbol against the original typeset equations; The converter renders many decimals with a split, italic form (for example '0 _._ 5' for 0.5); these are treated here as the printed digit strings with a normal decimal point, per the extraction rules.
<!-- AUTHORED REGION END -->