---
authors:
- Alexander Dickerson
- Cesare Robotti
- Giulio Rossetti
content_hash: sha256:2f9f98ba2c2c2c8e786222c4425d35e9dc3769196a87fd6385772b0a20cd2cc7
created: '2026-10-05T15:52:32Z'
page_id: sources/dickerson-2026-corporate-bond-factor-replication-crisis
page_type: source
publication_date: '2026'
publication_venue: arXiv 2604.07880 [q-fin.PR]
related:
- concepts/corporate-bonds
- concepts/trace-data
- concepts/look-ahead-bias
- concepts/factor-models
- concepts/factor-signals-in-credit
- concepts/bond-capm
- concepts/bond-momentum
- concepts/false-discovery-rate
- concepts/multiple-testing
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/bid-ask-spread
- concepts/bond-liquidity
- concepts/value-premium
- concepts/latent-implementation-bias
- sources/dickerson-2024-bond-pitfalls
- sources/dickerson-2023-bond-risk
- sources/bali-2022-bond-ml
- sources/houweling-2017-factor-investing
- sources/haesen-2017-momentum-spillover
- sources/kelly-2026-ipca
- analyses/capital-structure-arbitrage-literature-review
- entities/alexander-dickerson
- entities/cesare-robotti
- entities/giulio-rossetti
revision_id: 1
schema_version: 2
source_hash: sha256:d481c99e38fbb012a87f33ecedbcba6614a35e0c28555e39ad459246edf42b58
source_path: markdown_output/dickerson-2026-corporate-bond-factor-replication-crisis.md
source_type: paper
sources: []
tags:
- corporate-bond-factors
- factor-zoo
- replication
- measurement-error
- look-ahead-bias
- non-standard-errors
- trace
- bond-capm
title: The Corporate Bond Factor Replication Crisis
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: f264b84d-98f1-5f0a-bf42-212c8f7ff4ef
version_read: arXiv v1 (stamp 9 Apr 2026); earlier circulated as 'Common pitfalls
  in the evaluation of corporate bond strategies'
year: 2026
---

<!-- AUTHORED REGION START -->
# The Corporate Bond Factor Replication Crisis

**Authors:** Alexander Dickerson, Cesare Robotti, Giulio Rossetti · **Year:** 2026 · **Venue:** arXiv 2604.07880 [q-fin.PR]
**Version read:** arXiv v1 (stamp 9 Apr 2026); earlier circulated as 'Common pitfalls in the evaluation of corporate bond strategies'

## Summary

The paper argues that much of the corporate bond factor literature does not survive careful re-testing. The authors build a 'factor zoo' of 108 bond signals in nine clusters on cleaned TRACE data. After two bias corrections, most factors earn no significant alpha against the bond market factor. The survivors are mostly credit-spread-based value signals.

The first bias is Latent Implementation Bias (LIB). The same noisy month-end transaction price feeds both the sorting signal and the return denominator. A bond whose price is recorded too high is sorted to the short leg and also shows a return that is too low, and vice versa. This creates a fake premium. The month-end price is also not a price anyone could trade at. The fix is a gap: take the signal from an earlier price, or start the return at the first price of the next month.

The second bias is Look-Ahead Bias (LAB). Many studies winsorize or trim returns using thresholds computed on the full sample. That uses future information and helps one leg more than the other. Momentum, idiosyncratic volatility, downside-risk and macro-uncertainty factors depend on this. The fix is to set thresholds only from data available at formation.

Third, even bias-free results move a lot with ordinary data-filter and portfolio-construction choices. This spread (the non-standard error) is as large as, or larger than, the sampling standard error. The authors release cleaned data, the factors and the PyBondLab software at Open Bond Asset Pricing.

## Data

- US corporate bonds, TRACE Enhanced plus Rule 144A trades (144A from June 2014), merged with Mergent FISD.
- Universe: USD, fixed-rate, non-convertible, non-asset-backed bonds, $1,000 par, original maturity at least one year; bonds are tracked through and after default.
- Sample August 2002 to December 2024 (269 months); 52,656 unique bonds; average 6,790 bond-month observations per month.
- Cleaning: Dick-Nielsen filters, plus a decimal-shift corrector, a bounce-back filter and four daily filters for distressed-bond prices; daily VWAP prices; QuantLib for yields, duration and spreads.
- Monthly frequency. Month-end and month-begin returns, duration-adjusted excess returns; excess over the Fama-French one-month T-bill.
- Benchmark: single-factor bond CAPM (CAPMB) using MKTB, the value-weighted bond market excess return.
- 108 signals in nine clusters (Spreads/Yields/Size; Value; Momentum & Reversal; Illiquidity; Volatility & Risk; Market Risk; Credit & Default Betas; Volatility & Liquidity Betas; Macro & Other Betas).

## Method

Measurement model (after Blume and Stambaugh 1983): observed price $\hat P_{i,t}=(1+\delta_{i,t})P_{i,t}$, observed signal $\hat s_{i,t}=s_{i,t}+\eta_{i,t}$. The return error is roughly $\epsilon_{i,t}\approx\delta_{i,t+1}-\delta_{i,t}$. Because $\delta_{i,t}$ enters both signal and return, the errors are correlated (CEIV, after Duarte, Jones and Wang 2024) and do not cancel in long-short portfolios.

Returns: month-end $r^{End}_{i,t+1}=\frac{P^{end}_{i,t+1}+AI^{end}_{i,t+1}+C_{i,t+1}}{P^{end}_{i,t}+AI^{end}_{i,t}}-1$ and month-begin $r^{Bgn}_{i,t+1}=\frac{P^{end}_{i,t+1}+AI^{end}_{i,t+1}+C_{i,t+1}}{P^{bgn}_{i,t+1}+AI^{bgn}_{i,t+1}}-1$, with $P^{end}$ from the last 5 and $P^{bgn}$ from the first 5 business days. Decomposition: $r^{End}_{i,t+1}\approx\underbrace{(P^{bgn}_{i,t+1}/P^{end}_{i,t}-1)}_{LIB_{i,t+1}}+r^{Bgn}_{i,t+1}$.

Three approaches: (1) unadjusted; (2) adjusted signal, taken 1 to 10 business days before month-end; (3) adjusted return, from month-begin. Bias estimates: $Bias_{1-2}=(\omega_t-\omega^a_t)\times r^{End}_{t+1}$ and $Bias_{1-3}=\omega_t\times(r^{End}_{t+1}-r^{Bgn}_{t+1})$.

Look-ahead bias: winsorized return $\tilde r_{i,t+1}=\max(\tau_L,\min(r_{i,t+1},\tau_U))$, adjustment $\Delta_{i,t+1}=\tilde r_{i,t+1}-r_{i,t+1}$, and $LAB_{t+1}=\tilde r^{LS}_{t+1}-r^{LS}_{t+1}=\frac{1}{N^L_t}\sum_{i\in Long}\Delta_{i,t+1}-\frac{1}{N^S_t}\sum_{i\in Short}\Delta_{i,t+1}$. Ex-post thresholds use the full sample; ex-ante thresholds use $\{r_{i,s}\}_{s=1}^{t}$ only.

Non-standard error: $NSE^v=Q_{0.75}(\hat\mu^v)-Q_{0.25}(\hat\mu^v)$ across estimation paths, compared with sampling error via the ratio of the cross-path standard deviation to the average Newey-West SE. Data uncertainty: 108 ex-ante filter paths (return trimming, price range, bid-ask bounce) x EW/VW x full/IG/NIG = 648 paths per signal. Methodological uncertainty: 168 admissible constructions per signal (granularity, breakpoints, weighting, rating subsample, maturity bucket). Inference uses Newey-West t-statistics with lags floor(T^0.25), plus a Benjamini-Hochberg FDR check across 432 factor-specification combinations.

## Key Findings

1. Short-term reversal is mostly an artefact of shared-price noise. Its single-sort premium falls from -0.99% to -0.09% per month once the signal is gapped (t from -4.46 to -0.51). The bias is 90 bp, or 91% of the measured premium.
2. Value factors keep about half their premium. For val_ipr the premium falls from 0.96% to 0.51% per month; the 45 bp bias is 47% of the measured premium. Spread-based factors (ytm, cs, bbtm) show smaller biases of 15-18 bp per month. Across price-based factors, LIB inflates premia by 15 to 90 bp per month.
3. Bond momentum depends on ex-post right-tail winsorization. Six-month momentum's 0.30% monthly premium falls to 0.00% without it; twelve-month momentum goes from 0.26% winsorized to -0.13% unwinsorized.
4. Idiosyncratic-volatility and downside-risk factors depend on left-tail winsorization. For ivol_bbw the CAPMB alpha drops from 0.53% (t=2.58) to 0.18% (t=0.72); the bias is 66% of the alpha. Across such factors, 57-78% of the alpha comes from ex-post filtering, and the bias spikes in crises and rises with the VIX.
5. After correction, only 26 of 432 factor-specification alphas (6.0%) survive a Benjamini-Hochberg FDR adjustment. Of 119 nominally significant premia, 22 survive. The survivors are concentrated in credit-spread-based value factors.
6. Researcher choices matter as much as sampling noise. Across 648 ex-ante data-filter paths per signal, the average NSE of premia is 0.35% per month, against an average premium of 0.33% (NSE/SE 1.15). Across 168 portfolio constructions the NSE/SE ratio is 1.45, and 94% of variations do not improve the CAPMB alpha. 12 of the 36 top factors produce both positive and negative premia depending on construction.
7. Illiquidity factors are at best marginal. CAPMB alphas for the five illiquidity factors range from 0.10% to 0.20% per month with |t| below 1.65, and within-firm alphas are indistinguishable from zero.

## Limitations

The gap fix assumes price errors are serially uncorrelated; with stale prices in illiquid bonds some bias may remain (the paper says so in a footnote). The bond CAPM is used as a benchmark only, not as the true model; multi-factor alphas are mentioned only as unreported results. The BH FDR adjustment is presented as illustrative and does not allow for general dependence across strategies. Trading costs are not deducted; the authors flag cost-adjusted profitability as the next step. Filter categories are tested one at a time, not jointly. Several Internet Appendix results (definitions, FDR tables, leg decompositions) were not in the file read.

## Questions Raised

- Do the surviving credit-spread value factors stay profitable after realistic OTC execution costs?
- How much residual LIB remains for very illiquid bonds where price errors are autocorrelated?
- Would quote-based data (e.g. dealer index quotes) remove LIB, or swap it for staleness bias?
- Which pre-registered, economically motivated specification should be the default for a new bond signal?

## Relevance to Bond Signals

Any price-based bond signal (spread, yield, value, reversal) must use a signal-return gap or month-begin execution, or the backtest will be inflated by the same noise twice. Return filters must be ex-ante only. Signals should be reported across many construction choices rather than one favourable path.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/corporate-bonds|Corporate Bonds]]
- [[concepts/trace-data|TRACE Data]]
- [[concepts/look-ahead-bias|Look-ahead Bias]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]
- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/false-discovery-rate|False Discovery Rate]]
- [[concepts/multiple-testing|Multiple Testing]]
- [[concepts/backtesting|Backtesting]]
- [[concepts/overfitting-backtesting|Over-fitting in Back-testing]]
- [[concepts/bid-ask-spread|Bid-Ask Spread]]
- [[concepts/bond-liquidity|Bond Liquidity]]
- [[concepts/value-premium|Value Premium]]
- [[concepts/latent-implementation-bias|Latent Implementation Bias]]

## Entities

- [[entities/alexander-dickerson|Alexander Dickerson]]
- [[entities/cesare-robotti|Cesare Robotti]]
- [[entities/giulio-rossetti|Giulio Rossetti]]

## Related Sources

- [[sources/dickerson-2024-bond-pitfalls|Common Pitfalls in the Evaluation of Corporate Bond Strategies]]
- [[sources/dickerson-2023-bond-risk|Priced risk in corporate bonds]]
- [[sources/bali-2022-bond-ml|Predicting Corporate Bond Returns: Merton Meets Machine Learning]]
- [[sources/houweling-2017-factor-investing|Factor Investing in the Corporate Bond Market]]
- [[sources/haesen-2017-momentum-spillover|Momentum Spillover from Stocks to Corporate Bonds]]
- [[sources/kelly-2026-ipca|Instrumented Principal Component Analysis]]
<!-- AUTHORED REGION END -->