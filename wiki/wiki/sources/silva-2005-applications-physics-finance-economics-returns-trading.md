---
authors:
- A. Christian Silva
content_hash: sha256:d94e20d1370fdc045bba165bef4321771c1ac697b8ac66e15e53c252d1c8dabc
created: 2026-09-27 01:47:00+00:00
page_id: sources/silva-2005-applications-physics-finance-economics-returns-trading
page_type: source
publication_venue: University of Maryland, Department of Physics (PhD dissertation)
related:
- concepts/sampling-clocks
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/realized-variance
- concepts/market-microstructure
- concepts/stochastic-time-change
revision_id: 1
schema_version: 2
source_hash: sha256:4f01c4568211a730511fdd722514b974c494277616ddec02d9be686a21e8aa6f
source_path: markdown_output/silva-2005-applications-physics-finance-economics-returns-trading.md
source_type: paper
tags:
- econophysics
- stylized-facts
- subordination
- heston-model
- intraday-returns
- income-distribution
- trade-count-clock
- tick-data
- clock-compares
- asset-equity
- harvest-relevant
title: 'Applications of Physics to Finance and Economics: Returns, Trading Activity
  and Income'
updated: '2026-09-27T01:47:00Z'
uuid: 6b43a0b1-a4a0-5a6e-ab08-976c15197f76
year: 2005
---

<!-- AUTHORED REGION START -->
# Applications of Physics to Finance and Economics: Returns, Trading Activity and Income

## Summary

This document is a reformatted PhD dissertation, based on three published papers, that applies statistical-physics style methods to two separate empirical questions. The first is what probability distribution best describes stock log-returns over 'mesoscopic' time lags of roughly an hour to a month, and how that distribution connects to the discrete, trade-by-trade time scale beneath it. The second, self-contained part asks how the distribution of personal income in the USA evolved between 1983 and 2001.

For returns, the thesis derives a symmetrized, three-parameter closed-form solution of the Heston stochastic-volatility model and fits it to log-returns of individual large-cap US stocks built from TAQ tick data (aggregated into 5-minute close prices) and Yahoo daily closes. It separately tests the subordination hypothesis that a driftless Brownian motion, run in a random operational time set by the number of trades, can reproduce intraday return distributions; the number-of-trades-based integrated variance is itself modeled with a Cox-Ingersoll-Ross (CIR) process, and the analysis explicitly accounts for the discreteness of tick-by-tick price changes.

The return distribution is found to be exponential over the central part (more than 99% of probability) at mesoscopic lags, crossing over to Gaussian at longer lags, consistent with the fitted Heston-based closed form. Treating the number of trades as a subordinator explains about 85% of the central log-return distribution for lags between roughly an hour and a day, and the CIR-based reconstruction of that subordinator reproduces the return distribution with a similar, roughly 80%-85%, quality, but the framework is explicitly shown not to capture the largest return moves.

The income chapter documents a stable 'two-class' structure in IRS tax data: the great majority of the population follows an exponential ('thermal') income law with a slowly rising average ('temperature'), while a small upper tail follows a time-varying Pareto ('superthermal') law whose size tracks the rise and fall of the stock market; the dissertation ties this to a maximum-entropy argument for why the exponential part represents a form of statistical equilibrium, and derives closed-form Lorenz-curve and Gini-coefficient expressions from the exponential-plus-Pareto mixture.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Returns are sampled in two ways that the thesis explicitly connects: over fixed calendar-time lags t (built from 5-minute close prices, from 5 minutes up to a month) in the mesoscopic-returns study, and over a fixed number of trades N (a trade/tick clock) in the subordination study. It then shows how the two relate by treating the trade-count-derived integrated variance as the random subordinator (operational time) that maps the trade clock onto the distribution of calendar-time log-returns; the prediction/description horizon in each case is the return over that lag t or after that many trades N.

## Data

- **Asset class:** Equities
- **Instruments:** 27 Dow-listed large-cap US stocks analyzed for mesoscopic returns, with detailed results shown for Intel (INTC), Microsoft (MSFT), IBM and Merck (MRK); the intraday subordination study is restricted to Intel (INTC) alone
- **Venue:** NYSE and NASDAQ, via the TAQ tick database; daily closing prices from Yahoo
- **Period:** daily/interday returns 1993 to 1999 for the mesoscopic-returns study; intraday tick data for the full year 1997 for the subordination study; US personal income data 1983 to 2001
- **Granularity:** tick-by-tick TAQ transaction data aggregated into 5-minute close prices, with return lags studied from 5 minutes to 1 month (20 trading days); the subordination study additionally studies returns after N = 1 to 10000 trades

## Features and Measures

- **demeaned log-return.** the logarithm of the ratio of prices at two times separated by a lag, with the drift term removed.
- **Heston/DY closed-form return density.** a three-parameter probability density for log-returns, derived from the Heston stochastic-volatility model, that interpolates from an exponential distribution at short time lags to a Gaussian at long lags.
- **integrated variance / trade-count subordinator.** a variance process built from the cumulative number of trades in an interval, used as the random operational-time clock (subordinator) for a driftless Brownian motion representing log-returns.
- **income temperature (T).** the average income of the exponential ('thermal') part of the personal-income distribution in a given year, analogous to temperature in the Boltzmann-Gibbs distribution.
- **Pareto tail index / income share.** the power-law exponent and total income share of the upper ('superthermal') income class, tracked year by year.

## Method

For returns, the Heston model's stochastic differential equations are solved via a Fokker-Planck equation and Fourier/Laplace transform, then symmetrized under a zero-correlation assumption into a three-parameter closed form; this density is fit to empirical characteristic functions and cumulative distribution functions of log-returns at several lags for each stock, yielding per-stock estimates of a relaxation-time parameter, a variance-rate parameter, a drift, and an effective overnight time gap needed to reconcile intraday and interday variance scaling.

For the subordination hypothesis, the integrated variance built from the number of trades is checked against the moment relations implied by Brownian subordination, a CIR process is fit by least squares to the empirical distribution of that integrated variance, and the resulting reconstructed return distribution (via binning of the trade-count distribution and numerical convolution) is compared to both the directly observed return distribution and to a return distribution fit directly with the Heston model; agreement is judged by how much of the central probability mass is reproduced and by comparing the variance-rate and relaxation parameters obtained from the different fitting routes.

For income, the cumulative income distribution reported annually by the IRS is regressed log-linearly to identify an exponential regime (from which a yearly income temperature is extracted) and log-log to identify a Pareto regime above a crossover income; the resulting parameters are compared over time to inflation, GDP per capita and the S&P 500 index, and used to construct Lorenz curves and Gini coefficients that are checked against a closed-form formula derived from the exponential-plus-Pareto mixture.

## Results

- At mesoscopic time lags, log-returns for individual large-cap US stocks (1993-1999) follow an exponential law over more than 99% of the central distribution, crossing over to a Gaussian at longer lags, matching the fitted Heston/DY closed form.
- An effective overnight time gap of about 2 hours is needed to make the open-to-close and close-to-close return variances scale consistently with the time lag for each stock studied.
- Intel's smallest observed tick size in 1997 was $1/64, even though the exchange-set minimal price increment was $1/8 before June 24 and $1/16 afterward; this discreteness becomes negligible for return lags above about 1 hour.
- Treating the number of trades as a subordinator for a driftless Brownian motion explains about 85% of the central Intel log-return distribution for lags between roughly 1 hour and 1 day; a CIR fit to that trade-count-derived variance reproduces the log-returns with a similar 80%-85% central quality.
- Excluding the 16% most extreme log-returns (8% from each tail) brings the implied variance-rate parameter to about 8.01e-7, consistent with the subordination relation, reconfirming that the trade-count clock does not explain the most extreme return moves.
- US personal income (IRS data, 1983-2001) shows a stable two-class structure: about 97-99% of the population follows an exponential ('thermal') law whose average income rose from about 19 thousand dollars in 1983 to about 40 thousand dollars in 2001, while the top 1-3% follows a time-varying Pareto ('superthermal') tail.
- The Pareto tail's share of total income grew roughly five-fold, from about 4% in 1983 to about 20% in 2000, before falling after the market decline in 2001, tracking a roughly five-fold rise and fall in the S&P 500 over the same period.
- The Gini coefficient for individual income stays close to the value 1/2 implied by a purely exponential distribution, and a simple two-earner family-income model gives a theoretical Gini of 3/8.

## Limitations

- The intraday subordination test is restricted by the authors to a single stock (Intel) and a single year (1997) to limit the effect of non-stationarity in trading activity.
- The authors state they did not verify the subordination result for 2000 and 2001 data because of technical difficulties handling the larger data sets from those years.
- The subordination/CIR framework is explicitly reported as explaining only the central roughly 85% of the return distribution and as unable to explain the largest return moves.
- Reader note: detailed mesoscopic-return fits are shown for only 4 of the 27 companies analyzed (INTC, MSFT, IBM, MRK); the paper does not state whether the other 23 fit comparably well.
- Reader note: the income analysis uses aggregated IRS tax-return bins rather than individual-level microdata, and does not consistently separate personal from household/family income across all comparisons.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]

## Citation

A. Christian Silva (2005). Applications of Physics to Finance and Economics: Returns, Trading Activity and Income. University of Maryland, Department of Physics (PhD dissertation).

Text ingested: `markdown_output/silva-2005-applications-physics-finance-economics-returns-trading.md`, converted from `raw/ofi-event-clock/silva-2005-applications-physics-finance-economics-returns-trading.pdf`.

Coverage of this summary: Read the abstract, the full introduction (stock-returns background and dissertation outline), the general framing of the Heston-model chapter, chapter III (data and methods) in full, chapter IV (mesoscopic returns) including its data-analysis and conclusions subsections, chapter V (number of trades and subordination) in full including all subsections and its conclusion, and chapter VI (income distribution) including its data-analysis subsection and closing discussion. Did not read the detailed stochastic-differential-equation derivations in chapter II in full, nor the reference list.

Known problems with the input: The converted markdown replaces essentially all equations and figures with '[picture omitted]' placeholders, so exact functional forms and many figure-only values could not be verified beyond what is stated in the surrounding prose and surviving tables; No explicit publication year is printed on the document itself (it only references the author's own companion papers, dated 2003-2005); year taken from the job file's year_hint per instructions, since the paper does not state its own year; The extracted markdown for parts of chapter VI (income distribution) contains repeated/garbled text and stray characters from the PDF-to-text conversion, making some passages there hard to parse cleanly; extraction there relied on the clearer surrounding sentences.
<!-- AUTHORED REGION END -->