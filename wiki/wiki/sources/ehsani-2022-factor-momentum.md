---
title: Factor Momentum and the Momentum Factor
page_id: sources/ehsani-2022-factor-momentum
page_type: source
source_path: markdown_output/The Journal of Finance - 2022 - EHSANI - Factor Momentum and the Momentum Factor.md
source_type: journal-article
revision_id: 1
created: 2026-09-15 00:00:00+00:00
updated: '2026-09-15T00:00:00Z'
authors:
- Sina Ehsani
- Juhani T. Linnainmaa
year: 2022
venue: The Journal of Finance 77(3), 1877-1919
doi: 10.1111/jofi.13131
tags:
- momentum
- factor-momentum
- factor-autocorrelation
- principal-components
- residual-momentum
- investor-sentiment
sources: []
related:
- concepts/factor-momentum
- concepts/cross-sectional-momentum
- concepts/residual-momentum
- concepts/factor-timing
- concepts/principal-components-analysis
- concepts/fama-french-factors
- concepts/risk-vs-mispricing
- contradictions/factor-momentum-transmission
mind_map_priority: high
schema_version: 2
uuid: 25effd8f-a19f-54d4-abc1-dd12ef01ddf6
content_hash: sha256:fb0f2a32d08e599d02b551cf22d632f0d7b20229fe6d0aa3e904b176bcec6c4c
---

<!-- AUTHORED REGION START -->
# Factor Momentum and the Momentum Factor

**Authors:** [[entities/sina-ehsani|Sina Ehsani]], [[entities/juhani-linnainmaa|Juhani T. Linnainmaa]]

**Year:** 2022 · **Venue:** The Journal of Finance 77(3), 1877–1919 · DOI 10.1111/jofi.13131

**Institutions:** Northern Illinois University; Dartmouth College, NBER and Kepos Capital

## Summary

Most equity factors are positively autocorrelated, and that autocorrelation is what individual stock momentum is really trading. A stock that went up over the past year tends to load on factors that went up, so buying winners is an indirect bet that those factors keep going. Trade the factors directly and you span every common version of stock momentum, while none of them spans factor momentum. The authors' conclusion is that momentum is not a distinct risk factor. It is a dynamic portfolio that **times the other factors**.

## Sample

Monthly factor returns from the Kenneth French, AQR and Robert Stambaugh data libraries: 15 US factors from July 1963 (liquidity from January 1968) and seven global developed-ex-US factors from July 1990 (momentum from November 1990), ending December 2019. The 20 non-momentum factors are called "off-the-shelf". A second set of 47 US characteristic factors comes from Kozak, Nagel and Santosh (2020), with the seven momentum-related characteristics removed and microcaps excluded. Principal-component (PC) strategies start in July 1973 because ten years of daily data are needed to estimate the first eigenvectors.

## Signal Construction

The core signal is the **sign of a factor's own past-year return**. Time-series factor momentum is long a factor whose average return from month t−12 to t−1 is positive and short it otherwise. A cross-sectional variant is long factors above the median past return and short those below.

Before signing, factors are rescaled so that each has the same variance as the average factor up to month t. For the PC version, eigenvectors come from the correlation matrix of daily factor returns up to month t. The PC factors are demeaned and levered to that common variance, then signed on their t−11 to t average. Because PC factors have zero in-sample mean, the strategy is a pure bet on autocorrelation. The authors argue this avoids the Goyal–Jegadeesh (2017) objection that time-series strategies profit by being net long positive-premium assets.

The volatility enters only as this equal-variance scaling of the legs. The signal itself is a sign and does not divide by volatility. Of the stock momentum variants the paper tests, only Rachev et al.'s (2007) Sharpe-ratio momentum sorts on volatility-scaled returns.

## Findings

**Factors are autocorrelated.** Pooled across the 20 non-momentum factors, the average factor earns 6 bps a month after a losing year and 51 bps after a winning year; the 45 bp difference has a t-value of 4.22. The time-series strategy earns 3.9% a year (t = 7.01) and the cross-sectional one 2.4% (t = 5.04). The time-series version wins because a high return on one factor usually predicts high returns on the others too, which a cross-sectional bet shorts.

**Momentum concentrates in high-eigenvalue factors.** Momentum in PCs 1–10 of the 47 factors earns 19 bps a month (t = 7.07) with a five-factor alpha t-value of 6.51. Lower-eigenvalue sets earn progressively less. In the second half of the sample (October 1996–December 2019) only the PC 1–10 strategy stays significant, and it subsumes the momentum in all the other PC sets.

**Factor momentum prices momentum portfolios.** Adding PC 1–10 factor momentum to the Fama–French five-factor model leaves the ten portfolios sorted on t−12 to t−2 returns with a GRS p-value of 20.29%, so the test does not reject zero alphas. The Carhart six-factor model, which uses UMD itself, is still rejected. Regressing UMD on the five factors plus PC 1–10 factor momentum leaves UMD with an insignificant alpha (t = −0.59) and an R² of 42.5%.

**Spanning runs one way.** Factor momentum spans standard, industry-adjusted, industry, intermediate and Sharpe-ratio stock momentum. None of those five, even all together, spans factor momentum; its alpha t-values stay at 4.30 (individual factors) and 5.32 (PC factors) with all five on the right-hand side. As more factors are added to the strategy, UMD's alpha t-value falls from 3.60 with one factor to −0.04 with all 20.

**Residual momentum is omitted-factor momentum.** Sorting on CAPM residuals earns 58 bps a month (t = 4.29), more than raw returns at 45 bps. Profits then fall as more factors are stripped out: 44 bps on three-factor residuals and 37 bps on five-factor residuals. Net of factor momentum no residual strategy is significant. Simulations show why. If the investor's model omits autocorrelated factors, the estimated residuals inherit their momentum even when true firm-specific returns are IID. Removing a highly systematic but serially uncorrelated factor, like the market, makes residuals *more* informative about the omitted autocorrelated ones. Residual strategies also carry a hidden bet against beta.

**It is not incidental stock momentum.** The authors build "momentum-neutral" factors: weights are adjusted as little as possible so they are orthogonal to stocks' t−12 to t−2 returns. The adjustment is tiny, with an average correlation of 0.99 with the original weights. Factor momentum in these factors is stronger (alpha t = 7.53, information ratio 1.10 versus 0.96) and subsumes the original version.

**Why momentum looks unrelated to other factors.** UMD's unconditional correlation with the basket of factors is 0.04. Conditioned on the sign of each factor's past-year return, it is 0.45 for past winners and −0.51 for past losers. A five-factor model with each factor split into up-year and down-year parts explains 49% of UMD's variance, against 9% for the standard model. Momentum stocks comove, which answers Cochrane's (2011) question, because winners share exposure to the same recently successful factors.

## Mechanism

The paper extends the Kozak–Nagel–Santosh (2018) sentiment model. Sentiment demand follows an AR(1) process with persistence φ. Factors show momentum when φ lies between 1/R_f and 1, and reversal below that. Arbitrageurs could trade the pattern away, but doing so would expose them to factor risk. The model predicts that momentum concentrates in high-eigenvalue factors, and the data agree. The required threshold is demanding. With the 1965–2018 average monthly risk-free rate of 0.39%, sentiment needs φ above 0.996. The Baker–Wurgler index has a first-order autocorrelation of 0.986 and a unit root cannot be rejected, so the authors call the mechanism plausible rather than established.

## Why It Matters / Caveats

For signal design, this means stock-level momentum is largely a noisy, indirect way of timing factors. Trading the factors directly gives higher Sharpe and information ratios at lower volatility. The authors are careful on three points:

- Their result does **not** prove firm-specific returns lack momentum. Unknown factors, unobserved true factor returns and noisy betas make that impossible to settle without a natural experiment.
- Profits weaken in the second half of the sample, in parallel with UMD (81 bps first half, 38 bps and insignificant second half).
- They note that data-dredged subsets of factors reach higher t-values (8.24 for one 10-factor combination) and deliberately report the all-factor strategy instead.

The transmission channel the paper relies on, cross-sectional dispersion in factor loadings, is the part later work attacks. See [[contradictions/factor-momentum-transmission|the contradiction page]].

## Open Questions

- Would a rational time-varying risk-premium model make predictions about factor momentum that distinguish it from the sentiment account?
- How can true firm-specific returns be identified so the split between factor and firm-specific momentum can be settled?
- The paper's own footnote finds that weighting factors by the dispersion of their betas barely changes the strategy (0.31% versus 0.34% a month, correlation 0.95). How does that square with a mechanism that runs through beta dispersion?

## See Also

[[concepts/factor-momentum|Factor Momentum]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/residual-momentum|Residual Momentum]] · [[concepts/factor-timing|Factor Timing]] · [[concepts/principal-components-analysis|Principal Components Analysis]] · [[concepts/risk-vs-mispricing|Risk-vs-Mispricing Debate]]

[[sources/graef-2025-firm-specific-systematic-momentum|Graef, Hoechle & Schmid (2025)]] test this paper's transmission story directly and reject it. [[sources/li-2025-systematic-momentum|Li, Yuan & Zhou (2025)]] reuse its 15 anomalies and separate their systematic momentum from factor momentum. [[sources/blitz-2011-residual-momentum|Blitz, Huij & Martens (2011)]] is the residual momentum this paper reinterprets as omitted-factor momentum. [[sources/daniel-2016-momentum-crashes|Daniel & Moskowitz (2016)]] documents the same time-varying exposures from the crash side.

**Not yet written:** `entities/serhiy-kozak` (Kozak, Nagel and Santosh supply both the model and the 47-factor data); Arnott, Clements, Kalesnik & Linnainmaa (2021) "Factor momentum" and Ehsani & Linnainmaa (2020) "Time-series efficient factors" are cited but not in the wiki.

<!-- AUTHORED REGION END -->
