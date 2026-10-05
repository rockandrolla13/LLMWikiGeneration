---
title: 'Capital Structure Arbitrage: Literature Review for Bond Signals'
page_id: analyses/capital-structure-arbitrage-literature-review
page_type: analysis
revision_id: 2
created: '2026-10-05T00:00:00Z'
updated: '2026-10-05T12:00:00Z'
updated_by: deep-research-lit-review-2026-10-05
tags:
- capital-structure-arbitrage
- credit-default-swaps
- corporate-bonds
- structural-models
- implied-volatility
- lead-lag
- literature-review
sources:
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/cao-2023-implied-vol-bond-returns
- sources/hong-2025-implied-vol-cds-korea
- sources/amadori-2014-relative-informational-efficiency
- sources/dafonseca-2020-cds-equity-volatility-comovement
- sources/avino-2024-hedging-credit-equity-options
- sources/haesen-2017-momentum-spillover
- sources/bali-2022-bond-ml
- sources/dickerson-2023-bond-risk
- sources/dickerson-2024-bond-pitfalls
- sources/huang-2025-global-credit-spread-puzzle
related:
- concepts/capital-structure-arbitrage
- concepts/merton-model
- concepts/structural-models
- concepts/limits-to-arbitrage
- concepts/credit-spread-puzzle
- concepts/credit-default-swap-spread
- analyses/bond-momentum-signal-design-and-testing
schema_version: 2
---

<!-- AUTHORED REGION START -->
# Capital Structure Arbitrage: Literature Review for Bond Signals

*Prepared 2026-10-05. Lit-review mode: search → verification → synthesis. Written for bond feature and alpha discovery, so it focuses on how signals are built and how strong the evidence is. It does not cover execution or the risk process.*

---

## Bottom line

1. **The classic trade works on paper, but it decays and has crash risk.** Convergence trades between equity and CDS paid in 2001–2006. The edge faded as the CDS market grew. One study finds negative Sharpe ratios for 2005–2009.
2. **The input matters more than the model.** Option-implied volatility beats historical volatility. The choice of structural model (Merton, CreditGrades, etc.) is secondary.
3. **Stocks usually lead credit, in the order stock → CDS → bond.** The lag sits in high-yield and BBB bonds. Investment-grade bonds barely lag.
4. **The best-documented bond signals are cross-asset lead-lag signals, not transplanted equity characteristics.** Examples are residual equity momentum, CDS momentum and implied-volatility change. Most equity anomalies do not pay in bonds after costs.
5. **There is a large caveat on all pre-2023 bond-return evidence.** A 2019 JFE bond paper was retracted over a data timing error. A 2026 audit finds most of 108 bond factor signals lose significant alpha once price errors and asymmetric filtering are fixed. Every bond signal below must be re-tested on corrected data.
6. **Second pass (§11): the classic trade has a modern, top-journal successor.** The debt-equity spread, actual minus equity-implied credit spread, predicts stock and bond returns in opposite directions (Chen, Chen & Li, 2026, *Journal of Finance*). Post-2010 tests of the classic trade exist too, mostly in field journals and theses, and they confirm the option-implied-volatility finding.

---

## 1. The trade and its models

Capital structure arbitrage bets that a firm's equity and its credit will realign after they disagree. The disagreement is measured against a **[[concepts/structural-models|structural model]]**, which treats equity as a call option on the firm's assets ([[concepts/merton-model|Merton, 1974]]). The model turns share price, equity volatility and debt into a "fair" credit spread. The trader compares that with the market spread.

The industry standard is **CreditGrades** (Finger et al., 2002). It is a first-passage model: default happens when asset value hits a barrier. The barrier is uncertain because recovery is uncertain, which gives the model realistic short-term spreads. Inputs are share price, equity volatility, debt per share and bond recovery.

Three findings shape how much to trust the model's output:

- **Levels are wrong, sensitivities are right.** Structural models misprice bonds, but the equity hedge ratios they imply match the data (Schaefer & Strebulaev, 2008). Eom, Helwege & Huang (2004) test five models and find them inaccurate. That verdict is the commonly cited reading; the abstract could not be fetched.
- **Most investment-grade spread is not credit risk.** Credit risk explains only a small part of investment-grade spreads, less at short maturities and much more for high yield (Huang & Huang, 2012). So a gap between model and market levels in investment grade mostly reflects liquidity and other non-credit premia.
- **Volatility is the parameter that matters.** Option-implied volatility substantially improves capital structure arbitrage returns, and model choice is secondary (Bajlum & Larsen, working paper; finding seen via a search snippet only). Model and market spreads diverge most when equity volatility is high (Bedendo, Cathcart & El-Jahel, 2011). A Merton calibration on deep out-of-the-money implied volatility finds volatility dominates by orders of magnitude, and the paper argues the true exposure is vega, not delta (Zeitsch, 2017; lower-weight journal).

**Implication for signals:** use changes or cross-sectional ranks, not raw level gaps. Put effort into the volatility input, not the model. Bai & Wu (2016) do exactly this. They combine distance-to-default (how many standard deviations asset value sits above the default point) with many fundamentals via Bayesian shrinkage. The resulting "fair" CDS spread explains 77% of the cross-section on average. The gap between market and fair value predicts future spread moves.

## 2. Does the trade pay?

| Study | Sample | Result |
|---|---|---|
| Yu (2006), FAJ | 261 North American names, 2001–2004 | Portfolio Sharpe similar to fixed-income arbitrage benchmarks; single trades can lose heavily when a shorted CDS blows out |
| Imbierowicz & Cserna (2008), WP | 808 firms, 2002–2006 | Positive after costs, higher in high yield; edge fades by 2004/05 (figures from search snippets) |
| Duarte, Longstaff & Yu (2007), RFS | Several fixed-income arbitrage strategies | "Intellectual capital" strategies earn significant alpha; returns often positively skewed |
| Kapadia & Pu (2012), JFE | 2001–2009 | Convergence trades earn about 6% a year |
| Avino & Lazar (2020), JAI | 2005–2009 | Classic trade has negative Sharpe; conditioning on price-discovery leadership and cointegration helps |
| Wojtowicz (2014), WP | Later sample | 24.35% a year on invested capital; common factors explain at most 15% |

Yu's rule is the reference design. Calibrate CreditGrades on the first 10 daily CDS points with 1,000-day historical volatility. Enter when the market spread exceeds (1+α) times the model spread, or the reverse, with α from 0.5 to 2. Hedge with equity at entry. Exit on convergence or after 30 or 180 days. The Sharpe figures (0.35–0.80 investment grade, about 0.75 high yield, 180-day hold) are from the 2005 working paper, not the journal version.

**What is consistent:** returns are higher for lower-rated names. They are also higher where arbitrage is harder: illiquid CDS and high idiosyncratic risk (Kapadia & Pu). Wojtowicz is the exception: he finds more liquid CDS earn more.

**What is not:** whether the trade still pays. The positive results are mostly pre-2007. No peer-reviewed study tests the classic trade on post-2015 data (see §7).

## 3. Who leads: equity or credit?

**The default answer is stock → CDS → bond.**
- Stocks lead CDS and bonds; CDS leads bonds (Norden & Weber, 2009; Forte & Peña, 2009).
- Hourly TRACE data: stocks lead junk and BBB bonds, and convertibles in every rating class (Downing, Underwood & Xing, 2009).
- Daily stock returns lead high-yield but not investment-grade bonds (Tolikas, 2018).
- Equity leads CDS, not the reverse (Hilscher, Pollet & Wilson, 2015, "Are CDS a sideshow?").

**Credit leads in specific situations:**
- **Bad credit news.** CDS reveals information ahead of stocks only for negative news, more so for firms with many relationship banks (Acharya & Johnson, 2007).
- **Rating events and private firms.** Around 3,470 rating actions, information flows from CDS to bonds (Lee, Naranjo & Velioglu, 2018).
- **Short-sale bans.** During the 2008 ban, CDS predicted returns of the banned stocks (Ni & Pan, 2024).
- **After 2008.** The flow became two-way; lagged CDS returns now predict equity, more for low-rated firms (Wang, Basu & Clements, 2023). Rubesam & Zimmermann (2025) find credit-to-equity transmission dominates.

**Measurement changes the answer.** Early high-yield transaction data found no stock lead (Hotchkiss & Ronen, 2002). When each firm is represented by its most institutionally traded bond, the stock lead reverses (Ronen & Zhou, 2013). Which bond you pick drives the result.

**Regime dependence.** Equity leads CDS only after aggregate positive news (Marsh & Wagner, 2016). In Europe, the leading market switched between pre-crisis and crisis periods ([[sources/amadori-2014-relative-informational-efficiency|Amadori et al., 2014]]).

## 4. Option-implied signals for credit

**Options carry credit information that stocks do not.**
- Implied volatility (IV) level and skew beat historical volatility in explaining bond spreads (Cremers, Driessen, Maenhout & Weinbaum, 2008).
- Put IV dominates historical volatility for CDS spreads (Cao, Yu & Zhong, 2010, *Journal of Financial Markets*).
- The firm-level variance risk premium (implied minus expected variance) explains CDS spreads beyond standard credit factors (Wang, Zhou & Zhou, 2013).
- Realised-volatility benchmark: volatility alone explains 50% of CDS spread variation, jumps 19%, 77% with controls (Zhang, Zhou & Zhu, 2009).

**The tradeable return forecasts:**
- **IV change → bond returns.** Bonds whose issuer IV rose most underperform those whose IV fell most by 0.6% a month, after controls for size, maturity, rating, liquidity and last month's return ([[sources/cao-2023-implied-vol-bond-returns|Cao, Goyal, Xiao & Zhan, 2023]]). Replicated weakly in 19 Korean firms ([[sources/hong-2025-implied-vol-cds-korea|Hong & Park, 2025]]).
- **Downside variance premium → bond returns**, positive and robust (Huang, Jiang & Li, 2023; figures not seen).
- **IV level and skew → CDS returns.** Protection sellers earn more on high-IV firms, and on steep-skew firms within that group (Duong & Park, 2025; figures not seen).

**No-arbitrage anchor.** A spread of two deep out-of-the-money American puts replicates a pure default payoff, which gives a near model-free default price to compare with CDS (Carr & Wu, 2011). Carr & Wu (2010) give a joint model of the IV surface and CDS.

**Sign trap.** A rising IV predicts *lower* bond returns (slow reaction to news). A high variance premium predicts *higher* bond returns (payment for bearing risk). These are separate signals and their correlation needs checking.

**Aggregate benchmarks (not per-bond signals):** option-based credit spreads from index options (Culp, Nozawa & Veronesi, 2018, AER); synthetic credit-index options from CDX swaptions (Chen, Doshi & Seo, 2023); joint pricing of index options and CDO tranches (Collin-Dufresne, Goldstein & Yang, 2012). Credit-implied volatility from CDS spreads gives the reverse view (Kelly, Manzo & Palhares, FAJ 2025).

## 5. Limits to arbitrage and market integration

- **Structural inputs explain little of spread changes.** A common supply/demand factor dominates ([[sources/collin-dufresne-2001-determinants-credit-spread-changes|Collin-Dufresne, Goldstein & Martin, 2001]]).
- **Integration depends on frictions.** Equity–CDS agreement weakens with low CDS liquidity and high idiosyncratic risk ([[sources/kapadia-2012-limited-arbitrage-equity-credit|Kapadia & Pu, 2012]]). Bond–stock integration is estimated at 50–90% depending on frictions and dealer capacity (Sandulescu, working paper).
- **Characteristic premia do not line up.** For investment and momentum, bond premia are too large relative to equity, more so where noisy demand and short-sale frictions are strong (Choi & Kim, 2018).
- **Bond-implied expected stock returns predict realised stock returns *negatively*,** strongest for risky firms with liquid equity (van Zundert & Driessen, 2022). Clear segmentation.
- **The CDS–bond basis is wider where frictions are higher** (Bai & Collin-Dufresne, 2019). This is the credit-only version of the same problem.

**Reconciliation:** factor models with time-varying loadings find tight integration (Kelly, Palhares & Pruitt, 2023; Dickerson, Julliard & Mueller, forthcoming). Firm-level studies find friction-driven gaps. Both can hold: integration at the factor level, with temporary firm-level gaps where frictions are high. Those gaps are where a signal should look.

## 6. Recent and machine-learning work (2015–2026)

- **Residual equity momentum for bonds.** Sorting bonds on the issuer's firm-specific equity return (not total return) halves default exposure and doubles the Sharpe ratio. It avoids crashes at bear-to-bull turns ([[sources/haesen-2017-momentum-spillover|Haesen, Houweling & van Zundert, 2017]]). It builds on Gebhardt, Hvidkjaer & Swaminathan (2005).
- **CDS momentum spills into bonds.** Past CDS returns give 7.1% a year in CDS, and cross-market alpha of 7.3% a year in bonds and 10.3% in stocks. It is stronger for liquid CDS ahead of slow rating changes (Lee, Naranjo & Sirmans, 2021).
- **Bond book-to-market.** Top-minus-bottom quintile earns 3–4% a year among senior bonds, decaying with implementation delay (Bartram, Grinblatt & Nozawa, 2025).
- **Merton meets ML.** ML on many characteristics plus Merton-model structure beats unstructured models for one-month bond returns ([[sources/bali-2022-bond-ml|Bali et al., working paper]]). It is not established whether it used the data later found flawed.
- **Joint stock–bond–option factor model.** Six IPCA factors explain 31% of total variation across all three (Bali, Beckmeyer & Goyal, 2023, WP).
- **Equity anomalies mostly fail in bonds.** Accruals, earnings surprise and idiosyncratic volatility do not predict bond returns; behavioural signals do not survive costs (Chordia et al., 2017).

**The replication crisis.** [[sources/dickerson-2023-bond-risk|Dickerson, Mueller & Robotti (2023, JFE)]] show that, on corrected data, earlier bond factors add nothing beyond the bond market factor. This led to the retraction of Bai, Bali & Wen (2019, JFE). Dickerson, Robotti & Rossetti (2026) name two biases: price errors entering both signal and return, and asymmetric ex-post filtering that leaks future information. Across 108 signals, most lose significant alpha. Corrected data are public at openbondassetpricing.com.

## 7. Candidate bond signals, ranked by evidence

Ranking weighs replication, top-journal publication and direct bond-return evidence. **None has yet been confirmed on corrected (post-2026-audit) bond data.**

| # | Signal | Construction | Evidence | Main risk |
|---|---|---|---|---|
| 1 | Residual equity momentum | Issuer's firm-specific equity return over past months; sort bonds | GHS 2005, Haesen 2017, Chordia 2017 (equity leads bonds) | Default-beta crashes if not residualised |
| 2 | CDS momentum → bond | Past CDS return of issuer | Lee, Naranjo & Sirmans 2021 | Needs liquid CDS; post-2008 two-way flow |
| 3 | IV change | 1-month change in issuer ATM IV | Cao et al. 2023; weak replication 2025 | Option coverage limits universe |
| 4 | Variance / downside variance premium | Implied minus expected (downside) variance | Wang, Zhou & Zhou 2013; Huang, Jiang & Li 2023 | Opposite sign to #3 — check overlap |
| 5 | Fair-spread gap | Market spread minus shrinkage-fitted DtD + fundamentals spread | Bai & Wu 2016 (CDS) | Not tested on bond returns |
| 6 | Classic CSA gap | Market vs CreditGrades spread, with option IV input | Yu 2006; Bajlum & Larsen; Kapadia & Pu | Decayed after 2004/05; crash risk |
| 7 | IV skew | OTM put IV minus ATM IV | Cremers et al. 2008 (levels); Duong & Park 2025 (CDS returns) | Mostly level evidence, not returns |

**Conditioning variables that recur:** rating (high yield and BBB lag most), CDS and equity liquidity, idiosyncratic volatility, news sign, rating-event windows, crisis regime.

## 8. Contradictions to keep in view

- **Who leads** depends on bond selection (Ronen & Zhou vs Downing et al.), news sign (Marsh & Wagner), period (Wang et al., Amadori et al.) and region (Forte & Lovreta 2019 find CDS-implied volatility leading European equity volatility).
- **Where the edge is:** illiquid names (Kapadia & Pu) vs liquid CDS (Wojtowicz; Lee et al. 2021).
- **Whether the trade still pays:** positive pre-2005 vs negative 2005–2009 (Avino & Lazar) vs 24% (Wojtowicz). Differences are largely sample period and return definition.
- **Skew of returns:** crash risk on single short-CDS trades vs positively skewed portfolio returns (Yu; Duarte et al.).

## 9. Gaps

### 9a. Gaps in the wiki

The wiki holds 10 of the roughly 60 verified papers: Kapadia & Pu 2012, Collin-Dufresne et al. 2001, Cao et al. 2023, Hong & Park 2025, Amadori et al. 2014, Da Fonseca & Gottschalk 2020, Avino & Salvador 2024, Haesen et al. 2017, Bali et al. (Merton meets ML), Dickerson et al. 2023 (plus the related `dickerson-2024-bond-pitfalls`).

Suggested ingest priority, if you want to close the gap:

**Priority 1 — the core of the trade**
- Yu (2006) — reference trade design
- Finger et al. (2002) CreditGrades technical document
- Schaefer & Strebulaev (2008) — hedge ratios
- Bai & Wu (2016) — fair-spread gap
- Lee, Naranjo & Sirmans (2021) — CDS momentum into bonds
- Dickerson, Robotti & Rossetti (2026) — bond factor replication crisis

**Priority 2 — lead-lag and option signals**
- Gebhardt, Hvidkjaer & Swaminathan (2005); Hilscher, Pollet & Wilson (2015); Downing, Underwood & Xing (2009); Lee, Naranjo & Velioglu (2018); Ronen & Zhou (2013)
- Cremers et al. (2008); Cao, Yu & Zhong (2010); Carr & Wu (2011); Huang, Jiang & Li (2023); Duong & Park (2025)

**Priority 3 — integration and context**
- Chordia et al. (2017); Choi & Kim (2018); van Zundert & Driessen (2022); Kelly, Palhares & Pruitt (2023); Huang & Huang (2012); Bajlum & Larsen; Avino & Lazar (2020)

Note: `kelly-2026-ipca` in the wiki is the IPCA method paper, not the 2023 bond-returns paper. `feng-2025-predicting-bond-returns` is a different paper from Feng et al. (2025, JFE) on co-moving bond ratings.

### 9b. Gaps in the literature

*Status after the second pass (§11) in brackets.*

1. **No peer-reviewed test of the classic trade on post-2015 data.** [Largely closed. Chen, Chen & Li (2026, JF) test debt-equity relative mispricing as a cross-sectional signal. Chan et al. (2023, JEF) test CDS-versus-put convergence. Lovreta & Mladenović (2018) cover iTraxx firms to 2017. Several theses cover 2012–2019.]
2. **No test of equity-to-bond signals on corrected bond data.** [Still open. No paper found re-runs the equity-to-bond signals on the 2026 corrected data.]
3. **No published ML study predicting CDS or bond returns from equity-option features.** [Partly closed. Kaufmann, Messow & Vogt (2021, FAJ) boost equity momentum with trees. Equity characteristics enter published and working-paper ML models, but none uses option features as the main input.]
4. **No study combines the signals.** [Partly closed. Henke et al. (2020) and Vladimirova et al. (2022) combine equity-derived signals with bond signals. Dang, Hollstein & Prokopczuk (2023) select equity momentum among a few non-redundant bond factors. Nobody has tested IV change, CDS momentum and the debt-equity spread together.]

## 10. Limits of this review

- Four parallel search agents verified each reference against a journal, SSRN, NBER, RePEc, arXiv or publisher page. Full texts were not read; method notes are at abstract level.
- SSRN and ScienceDirect blocked some direct fetches. Where a figure came from a search summary rather than a fetched abstract, it is flagged above or omitted.
- Some Yu (2006) figures are from the 2005 working paper and may differ in the published version.
- Excluded as unverified in the first pass: Longstaff, Mithal & Neis (2003) lead-lag result; Berndt & Obreja (no option-based paper found); Esquil & Lai (2025). The second pass resolved three others: Kim, Park & Noh (2013, JFM) and Chen, Roussanov, Wang & Zou (NBER, 2026) are now verified (see §11). Longstaff, Mithal & Neis is real as a 2005 *Journal of Finance* paper, but its abstract covers default versus liquidity components, not lead-lag, so the lead-lag claim stays untraced.
- Candidate-list corrections: Cao, Yu & Zhong is in *Journal of Financial Markets*, not *Futures Markets*. "Cserna & Imbierowicz, How profitable is capital structure arbitrage?" conflates two papers; the title is Yu's.

*AI disclosure: search, verification and synthesis were carried out with AI research agents. All references were checked against an online source; claims should be confirmed against full texts before being relied on.*

---

## 11. Second pass: OpenAlex and Semantic Scholar (2026-10-05)

### Method

- **Search.** 21 keyword queries, one set per gap, run on both OpenAlex and Semantic Scholar, limited to 2015–2026.
- **Citation chasing.** Every 2015–2026 paper citing any of 14 seed papers (Yu 2006; Kapadia & Pu 2012; Cao et al. 2023; Haesen et al. 2017; Lee, Naranjo & Sirmans 2021; Culp, Nozawa & Veronesi 2018; Bai & Wu 2016; Schaefer & Strebulaev 2008; Cremers et al. 2008; Gebhardt et al. 2005; Hilscher et al. 2015; Chordia et al. 2017; Dickerson, Mueller & Robotti 2023; Carr & Wu 2011).
- **Screening.** 2,729 unique records. A keyword filter kept 274 that mention both an equity side and a credit side. A second sweep recovered 60 more that cite three or more seeds. AI screeners read each title and abstract against the four gaps. About 90 papers passed.
- **Verification.** Every paper below has a DOI or repository record in OpenAlex or Semantic Scholar, with authors and venue checked against it. Findings come from abstracts only.

### Gap 1 — Modern tests of the trade

**The headline paper.** Chen, Chen & Li (2026, *Journal of Finance*) define the **debt-equity spread (DES)**: a firm's actual credit spread minus the credit spread implied by its equity. DES predicts stock and bond returns in opposite directions. It is distinct from existing mispricing measures and is not explained by risk factors. High-DES firms tend to issue equity, retire debt and see insider selling. The authors read DES as relative mispricing between partially segmented debt and equity markets. This is capital structure arbitrage turned into a cross-sectional bond signal.

**Other post-2010 evidence:**
- **CDS versus deep out-of-the-money puts.** Chan, Kolokolova, Lin & Poon (2023, *Journal of Empirical Finance*) split the gap between CDS-implied and put-implied default rates into a rating-curve part and a friction part. Both shrink over time at different speeds, and trading on the parts beats trading on the raw gap.
- **Long-run linkage.** Lovreta & Mladenović (2018, *European Journal of Finance*) study non-financial iTraxx Europe firms, 2004–2017. Stock and CDS prices are tied in the long run only once structural breaks are allowed for. CDS-equity trades pay only while that tie holds, and CDS illiquidity weakens it.
- **Model-based trades.** Huang & Luo (2016, *JRFM*) report persistent risk-adjusted profits from a capital structure arbitrage built on an improved structural model. Svec (2016, *IJBF*) finds implied-volatility inputs give more profitable crisis-period trades in Australia after costs.
- **Implied volatility as the input (theses).** Mäkilä (2020, Turku) covers 102 European firms, 2012–2019. Calibrating Merton/KMV with implied volatility improves accuracy and profit, and variance swaps can replace the stock hedge. Xiang (2017, Monash) refines the CreditGrades calibration. Both are grey literature.
- **The reverse direction.** Byström (2016, *JFI*) inverts CreditGrades to back out the stock price implied by CDS. Guo (2016, *Journal of Futures Markets*) backs out a CDS-implied stock volatility; a trade on its gap with option-implied volatility earns significant risk-adjusted returns. Shi et al. (2022, *IRFA*) build trading strategies on CDS-implied volatility (abstract not available).
- **Index level.** Collin-Dufresne, Junge & Trolle (2023, *Journal of Finance*) find that a structural model cannot match the relative prices of CDX options and S&P 500 options, which points to incomplete integration. Selling CDX volatility earns more than selling SPX volatility.

### Gap 2 — Equity-to-bond signals

**Slow bond reaction to stock news.**
- Li (2021, *JFE*): bond prices underreact to the issuer's stock returns. Higher-quality bonds underreact more to default news. The lag gives large out-of-sample predictability.
- Lee, Rizova & Wang (2020, SSRN): among issuer variables, only the recent short-term stock return adds information about global bond returns, and it decays fast.

**Equity momentum variants.**
- Bektić (2018, *JFI*): residual equity momentum predicts euro investment-grade bond returns, 2000–2016, better than total equity momentum. This replicates Haesen et al. (2017) outside the US.
- Kaufmann & Messow (2019, SSRN): in European credit, equity momentum predicts bond returns and rating changes, and screens out bonds downgraded within a year.
- Keshavarz & Sirmans (2024, SSRN): the stock's price relative to its 52-week high predicts bond returns. The authors report it as distinct from bond momentum, equity momentum spillover and earnings drift. Chen et al. (2026, *JBF*) study a related 52-week anchor for bonds of past-loser stocks (abstract not available).

**Other equity-derived signals.**
- Volatility: high idiosyncratic stock volatility predicts low bond returns (Chung, Wang & Wu, 2019, *JFE*).
- Beta: European bonds of low equity-beta firms earn higher risk-adjusted returns (Bektić, 2019, *Review of Financial Economics*).
- Earnings: bonds of issuers with positive earnings surprises earn abnormal returns for several months (Ben Dor, Guan & Zeng, 2020, *JFI*).
- Short selling: equity and bond short-selling signals together predict bond returns better than either alone, mainly in high yield (Vladimirova, Markl & Messow, 2022, *JFI*).
- Distance to default: Merton-based quality and value factors add value net of costs (Kang, Parker, Radell & Smith, 2018, *JFI*).

**Do equity factors carry over?** Keshavarz & Sirmans (2024, SSRN) test more than 150 equity signals in bonds and CDS. Factor performance ranks similarly across markets, mainly through credit-risk exposure, and the two decouple in downturns.

**Credit-to-equity decay.** CDS information that stock returns had not yet absorbed used to predict stock returns, but that power fell after the post-2010 trade-reporting and central-clearing reforms (Marra, Yu & Zhu, 2019, *Journal of Financial Stability*). This weakens the case for credit-leads-equity signals in the post-reform period.

### Gap 3 — Machine learning and option features

- **Option IV change replicated.** In a 2017 thesis, selling bonds with the largest IV increases and buying those with the smallest earns 1.03% a month (Navon, 2017, grey literature). This supports Cao et al. (2023).
- **Trees on equity momentum.** Boosted regression trees on past equity returns plus size and liquidity roughly double the alpha and information ratio of plain equity momentum in credit (Kaufmann, Messow & Vogt, 2021, *FAJ*).
- **Deep learning and ML on bonds.** Feng, Jiang & Li (2021, SSRN) build deep-learning bond factors from bond and equity characteristics that beat standard models. Li, Lü, Qi & Zhou (2022, SSRN) find developed-market bonds are more tied to equity and that ML predictability varies over time. A separate Bali, Goyal, Huang, Jiang & Wen working paper (Swiss Finance Institute) finds equity characteristics add nothing significant once bond characteristics are included.
- **Credit and equity risk premia.** High-frequency credit measures with ML forecast both credit and equity risk premia out of sample, and short-horizon equity-credit gaps persist (Kita, 2021, SSRN).
- **Building blocks.** Default probabilities from equity options track CDS-implied ones closely (Conrad, Dittmar & Hameed, 2020, *JFEC*). Combining options with CDS for the left tail improves firm-level risk-neutral distributions (Aramonte, Jahan-Parvar, Rosen & Schindler, 2017, FRB IFDP). Options gained predictive power over CDS after the 2008 crisis (Kim, Park & Noh, 2013, *Journal of Futures Markets*).

### Gap 4 — Combining signals and integration

- **Multi-factor blends.** Value, equity momentum, carry, quality and size have low correlation with each other in USD credit, and blending them gives alpha after costs (Henke, Kaufmann, Messow & Fang-Klingler, 2020, *Journal of Index Investing*).
- **Factor selection.** A Bayesian selection keeps carry, duration, equity momentum and term structure, and finds many other bond factors redundant (Dang, Hollstein & Prokopczuk, 2023, SSRN).
- **Forecast combination.** Stock-market variables matter in an iterated combination of 27 predictors of bond returns (Lin, Wu & Zhou, 2017, *Management Science*).
- **Common factors with segmentation.** Stocks, bonds and options share a strong common factor structure. Pricing errors persist, and factor premia differ enough between markets to show significant segmentation (Chen, Roussanov, Wang & Zou, NBER WP, 2026).
- **When credit leads.** Leverage strengthens the flow of information from stocks to CDS, and CDS leads for the most levered firms (Zimmermann, 2020, *JEDC*). Price discovery shifts toward credit as credit risk rises (Zhou, Bagnarosa & Cummins, 2025, *Accounting & Finance*). Cross-listed firms show tighter CDS-equity integration (Augustin, Jiao, Sarkissian & Schill, 2019, *RFS*).
- **Not fully integrated.** Equity returns in the two days before a credit event predict that day's CDS change, 2010–2013 (Kiesel, Kolaric & Schiereck, 2016, *QREF*).
- **Firms act on the gap.** Firms issue in one market and repurchase in the other based on relative valuations (Ma, 2019, *Journal of Finance*). This is consistent with the DES finding.

### What the second pass changes for signal design

1. **Add the debt-equity spread as the lead candidate.** It is the only top-journal signal built directly on capital structure mispricing with bond-return evidence. Build it as actual spread minus equity-implied spread, then rank cross-sectionally.
2. **Equity momentum for bonds is now replicated in Europe and globally** (Bektić 2018; Kaufmann & Messow 2019; Lee, Rizova & Wang 2020). The residual version stays preferred. Tree-based conditioning improves it (Kaufmann et al. 2021).
3. **The IV-change signal has an independent replication** (Navon 2017, grey literature), still not on corrected data.
4. **Be careful with credit-leads-equity signals in the post-reform period.** Their predictive power fell after CDS market reforms (Marra et al. 2019).
5. **The 52-week-high anchor is a new candidate** (Keshavarz & Sirmans 2024), still a working paper.
6. **Re-testing on corrected bond data is still the main open task.** No paper found does it for these signals.

### Second-pass references (verified via OpenAlex / Semantic Scholar)

- Aramonte, S., Jahan-Parvar, M. R., Rosen, S., & Schindler, J. W. (2017). Firm-specific risk-neutral distributions: The role of CDS spreads. FRB International Finance Discussion Paper. https://doi.org/10.2139/ssrn.2908524
- Augustin, P., Jiao, F., Sarkissian, S., & Schill, M. J. (2019). Cross-listings and the dynamics between credit and equity returns. *RFS*. https://doi.org/10.1093/rfs/hhz052
- Bektić, D. (2018). Residual equity momentum spillover in global corporate bond markets. *Journal of Fixed Income, 28*(3). https://doi.org/10.3905/jfi.2018.28.3.046
- Bektić, D. (2019). The low beta anomaly: A corporate bond investor's perspective. *Review of Financial Economics*. https://doi.org/10.1002/rfe.1022
- Ben Dor, A., Guan, J.-L., & Zeng, X.-M. (2020). How do credit markets react to earnings releases? *Journal of Fixed Income*. https://doi.org/10.3905/jfi.2020.1.101
- Byström, H. (2016). Stock prices and stock return volatilities implied by the credit market. *Journal of Fixed Income*. https://doi.org/10.3905/jfi.2016.2016.1.043
- Chan, K. K., Kolokolova, O., Lin, M.-T., & Poon, S.-H. (2023). Price convergence between credit default swap and put option: New evidence. *Journal of Empirical Finance*. https://doi.org/10.1016/j.jempfin.2023.03.008
- Chen, C., Saha, S., Shafaati, M., Stivers, C., & Sun, L. (2026). Predicting stock returns of past-winner stocks and bond returns of past-loser stocks with a stock's 52-week price anchor. *JBF*. https://doi.org/10.1016/j.jbankfin.2026.107643
- Chen, H., Chen, Z.-Y., & Li, J. E. (2026). The debt-equity spread. *Journal of Finance*. https://doi.org/10.1111/jofi.70060
- Chen, Z., Roussanov, N. L., Wang, X., & Zou, D. (2026). Common risk factors in the returns on stocks, bonds (and options), redux. NBER WP 35579. https://doi.org/10.3386/w35579
- Chung, K. H., Wang, J.-B. L., & Wu, C. (2019). Volatility and the cross-section of corporate bond returns. *JFE*. https://doi.org/10.1016/j.jfineco.2019.02.002
- Collin-Dufresne, P., Junge, B., & Trolle, A. B. (2023). How integrated are credit and equity markets? Evidence from index options. *Journal of Finance*. https://doi.org/10.1111/jofi.13300
- Conrad, J. S., Dittmar, R. F., & Hameed, A. (2020). Implied default probabilities and losses given default from option prices. *Journal of Financial Econometrics*. https://doi.org/10.1093/jjfinec/nbaa017
- Dang, T. D., Hollstein, F., & Prokopczuk, M. (2023). Which factors for corporate bond returns? SSRN. https://doi.org/10.2139/ssrn.4012601
- Feng, G., Jiang, L., & Li, J. (2021). Interpretable and arbitrage-free deep learning for corporate bond pricing. SSRN. https://doi.org/10.2139/ssrn.3971274
- Guo, B. (2016). CDS inferred stock volatility. *Journal of Futures Markets*. https://doi.org/10.1002/fut.21768
- Henke, H., Kaufmann, H., Messow, P., & Fang-Klingler, J. (2020). Factor investing in credit. *Journal of Index Investing*. https://doi.org/10.3905/jii.2020.1.085
- Huang, Z. J., & Luo, Y. (2016). Revisiting structural modeling of credit risk — Evidence from the credit default swap market. *JRFM, 9*(2), 3. https://doi.org/10.3390/jrfm9020003
- Kang, J., Parker, T. B., Radell, S., & Smith, R. (2018). Reach for safety. *Journal of Fixed Income*. https://doi.org/10.3905/jfi.2018.27.4.006
- Kaufmann, H., & Messow, P. (2019). Equity momentum in European credits. SSRN. https://doi.org/10.2139/ssrn.3436776
- Kaufmann, H., Messow, P., & Vogt, J. (2021). Boosting the equity momentum factor in credit. *Financial Analysts Journal*. https://doi.org/10.1080/0015198x.2021.1954377
- Keshavarz, J., & Sirmans, S. (2024a). How similar are the factor structures of equity and credit markets? SSRN. https://doi.org/10.2139/ssrn.4805159
- Keshavarz, J., & Sirmans, S. (2024b). The 52-week high, downside risk, and corporate bond returns. SSRN. https://doi.org/10.2139/ssrn.4826999
- Kiesel, F., Kolaric, S., & Schiereck, D. (2016). Market integration and efficiency of CDS and equity markets. *QREF*. https://doi.org/10.1016/j.qref.2016.02.010
- Kim, T. S., Park, Y. J., & Noh, J. (2013). The linkage between the options and credit default swap markets during the subprime mortgage crisis. *Journal of Futures Markets*. https://doi.org/10.1002/fut.21595
- Kita, A. (2021). Machine learning predictions of credit and equity risk premia. SSRN. https://doi.org/10.2139/ssrn.3800205
- Lee, M. I., Rizova, S., & Wang, S. Y. (2020). The cross-section of global corporate bond returns. SSRN. https://doi.org/10.2139/ssrn.3531279
- Li, D., Lü, L., Qi, Z., & Zhou, G. (2022). International corporate bond returns: Uncovering predictability using machine learning. SSRN. https://doi.org/10.2139/ssrn.4140701
- Li, J. (2021). Endogenous inattention and risk-specific price underreaction in corporate bonds. *JFE*. https://doi.org/10.1016/j.jfineco.2021.09.025
- Lin, H., Wu, C., & Zhou, G. (2017). Forecasting corporate bond returns with a large set of predictors: An iterated combination approach. *Management Science*. https://doi.org/10.1287/mnsc.2017.2734
- Lovreta, L., & Mladenović, Z. (2018). Do the stock and CDS markets price credit risk equally in the long-run? *European Journal of Finance*. https://doi.org/10.1080/1351847x.2018.1501402
- Ma, Y. (2019). Nonfinancial firms as cross-market arbitrageurs. *Journal of Finance*. SSRN: https://doi.org/10.2139/ssrn.2692350
- Mäkilä, V. (2020). On capital structure arbitrage (Master's thesis). University of Turku. https://doi.org/10.13140/rg.2.2.29953.68969
- Marra, M., Yu, F., & Zhu, L. (2019). The impact of trade reporting and central clearing on CDS price informativeness. *Journal of Financial Stability*. https://doi.org/10.1016/j.jfs.2019.07.002
- Navon, Y. (2017). The information content of options (Thesis). Figshare. https://doi.org/10.4225/03/58ae40c9ebb08
- Shi, Y., Chen, D.-R., Guo, B., Xu, Y., & Yan, C. (2022). The information content of CDS implied volatility and associated trading strategies. *IRFA*. https://doi.org/10.1016/j.irfa.2022.102295
- Svec, J. (2016). Impact of financial crisis on the profitability of capital structure arbitrage in Australia. *International Journal of Banking and Finance, 12*(1). https://doi.org/10.32890/ijbf2016.12.1.4
- Vladimirova, D., Markl, T., & Messow, P. (2022). The impact of short selling in the cross-section of corporate bond returns. *Journal of Fixed Income*. https://doi.org/10.3905/jfi.2022.1.147
- Xiang, Y. (2017). The credit risk information dynamics between the CDS and equity markets (Thesis). Monash University. https://doi.org/10.26180/4621849.v1
- Zhou, X.-Q., Bagnarosa, G., & Cummins, M. (2025). How do corporate factors affect price discovery process between equity and credit markets? *Accounting & Finance*. https://doi.org/10.1111/acfi.70116
- Zimmermann, P. A. (2020). The role of the leverage effect in the price discovery process of credit markets. *JEDC*. https://doi.org/10.1016/j.jedc.2020.104033

Screened but not detailed here (lower relevance or no abstract): Procasky (2023); Procasky & Yin (2022); Romanyuk (2026); Mao et al. (2022); Fieberg, Liedtke, Schlag & Zaremba (2025, "Cross-asset trend spillover", no abstract); Keshavarz & Sirmans (2025); Bao & Hou (2017); Huang, Huang & Oxman (2015); Liu, Pu & Zhao (2015); Chau, Han & Shi (2017); Marra (2016); Back & Crotty (2015); Israelov (2019); Xiang, Chng & Fang (2017); Forte & Lovreta (2022). Full screening data: harvest of 2,729 records, session scratchpad (not kept in the repo).

## Related wiki pages

- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]] · [[concepts/merton-model|Merton Model]] · [[concepts/structural-models|Structural Models]] · [[concepts/limits-to-arbitrage|Limits to Arbitrage]] · [[concepts/credit-spread-puzzle|Credit Spread Puzzle]]
- [[sources/avino-2024-hedging-credit-equity-options|Avino & Salvador (2024)]] · [[sources/dafonseca-2020-cds-equity-volatility-comovement|Da Fonseca & Gottschalk (2020)]] · [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. — Common pitfalls in bond strategy evaluation]] · [[sources/huang-2025-global-credit-spread-puzzle|Huang, Nozawa & Shi (2025)]]
- [[analyses/bond-momentum-signal-design-and-testing|Bond Momentum Signal: Findings, Test Plan and Next Steps]]

---

## References (verified)

**Foundations and profitability**
- Avino, D. E., & Lazar, E. (2020). Rethinking capital structure arbitrage: A price discovery perspective. *Journal of Alternative Investments, 22*(4), 75–91.
- Bai, J., & Wu, L. (2016). Anchoring credit default swap spreads to firm fundamentals. *JFQA, 51*(5), 1521–1543. https://doi.org/10.1017/S0022109016000533
- Bajlum, C., & Larsen, P. T. (2007). Capital structure arbitrage: Model choice and volatility calibration. Working paper, SSRN 956839.
- Bedendo, M., Cathcart, L., & El-Jahel, L. (2011). Market and model credit default swap spreads: Mind the gap! *European Financial Management, 17*(4), 655–678. https://doi.org/10.1111/j.1468-036X.2009.00516.x
- Duarte, J., Longstaff, F. A., & Yu, F. (2007). Risk and return in fixed-income arbitrage: Nickels in front of a steamroller? *RFS, 20*(3), 769–811.
- Eom, Y. H., Helwege, J., & Huang, J.-Z. (2004). Structural models of corporate bond pricing: An empirical analysis. *RFS, 17*(2), 499–544.
- Finger, C. C. (Ed.), et al. (2002). *CreditGrades technical document*. RiskMetrics Group.
- Huang, J.-Z., & Huang, M. (2012). How much of the corporate-Treasury yield spread is due to credit risk? *Review of Asset Pricing Studies, 2*(2), 153–202.
- Imbierowicz, B., & Cserna, B. (2008). How efficient are credit default swap markets? Working paper, SSRN 1099456.
- Kapadia, N., & Pu, X. (2012). Limited arbitrage between equity and credit markets. *JFE, 105*(3), 542–564.
- Merton, R. C. (1974). On the pricing of corporate debt. *Journal of Finance, 29*(2), 449–470. https://doi.org/10.1111/j.1540-6261.1974.tb03058.x
- Schaefer, S. M., & Strebulaev, I. A. (2008). Structural models of credit risk are useful. *JFE, 90*(1), 1–19. https://doi.org/10.1016/j.jfineco.2007.10.006
- Wojtowicz, M. (2014). Capital structure arbitrage revisited. Tinbergen Institute DP 14-137/IV/DSF81.
- Yu, F. (2006). How profitable is capital structure arbitrage? *Financial Analysts Journal, 62*(5), 47–62. https://doi.org/10.2469/faj.v62.n5.4282
- Zeitsch, P. J. (2017). Capital structure arbitrage under a risk-neutral calibration. *JRFM, 10*(1), 3.

**Lead-lag and information flow**
- Acharya, V., & Johnson, T. (2007). Insider trading in credit derivatives. *JFE, 84*(1), 110–141. https://doi.org/10.1016/j.jfineco.2006.05.003
- Amadori, M. C., Bekkour, L., & Lehnert, T. (2014). The relative informational efficiency of stocks, options and CDS. *Journal of Risk Finance*.
- Bittlingmayer, G., & Moser, S. (2014). What does the corporate bond market know? *Financial Review, 49*, 1–19.
- Downing, C., Underwood, S., & Xing, Y. (2009). The relative informational efficiency of stocks and bonds. *JFQA, 44*(5), 1081–1102.
- Forte, S., & Peña, J. I. (2009). Credit spreads: An empirical analysis on the informational content of stocks, bonds, and CDS. *JBF, 33*(11), 2013–2025.
- Gebhardt, W., Hvidkjaer, S., & Swaminathan, B. (2005). Stock and bond market interaction: Does momentum spill over? *JFE, 75*(3), 651–690. https://doi.org/10.1016/j.jfineco.2004.03.005
- Han, B., Subrahmanyam, A., & Zhou, Y. (2017). The term structure of credit spreads, firm fundamentals, and expected stock returns. *JFE, 124*(1), 147–171.
- Hilscher, J., Pollet, J., & Wilson, M. (2015). Are credit default swaps a sideshow? *JFQA, 50*(3), 543–567.
- Hotchkiss, E., & Ronen, T. (2002). The informational efficiency of the corporate bond market. *RFS, 15*(5), 1325–1354.
- Kwan, S. H. (1996). Firm-specific information and the correlation between individual stocks and bonds. *JFE, 40*(1), 63–80.
- Lee, J., Naranjo, A., & Sirmans, S. (2021). CDS momentum: Slow-moving credit ratings and cross-market spillovers. *Review of Asset Pricing Studies, 11*(2), 352–401. https://doi.org/10.1093/rapstu/raaa025
- Lee, J., Naranjo, A., & Velioglu, G. (2018). When do CDS spreads lead? *JFE, 130*(3), 556–578.
- Marsh, I., & Wagner, W. (2016). News-specific price discovery in CDS markets. *Financial Management, 45*(2), 315–340. https://doi.org/10.1111/fima.12095
- Ni, S., & Pan, J. (2024). *JBF, 167*, 107243.
- Norden, L., & Weber, M. (2009). The co-movement of credit default swap, bond and stock markets. *European Financial Management, 15*, 529–562.
- Ronen, T., & Zhou, X. (2013). Trade and information in the corporate bond market. *Journal of Financial Markets, 16*(1), 61–103.
- Rubesam, A., & Zimmermann, P. (2025). *Journal of Financial Intermediation, 63*. https://doi.org/10.1016/j.jfi.2025.101151
- Tolikas, K. (2018). The lead-lag relation between the stock and the bond markets. *European Journal of Finance, 24*(10), 849–866.
- Wang, R., Basu, A., & Clements, A. (2023). Are credit default swaps still a sideshow? *Global Finance Journal, 57*.

**Option-implied signals**
- Avino, D. E., & Salvador, E. (2024). Contingent claims and hedging of credit risk with equity options. *Review of Asset Pricing Studies, 14*(2).
- Cao, C., Yu, F., & Zhong, Z. (2010). The information content of option-implied volatility for credit default swap valuation. *Journal of Financial Markets, 13*(3), 321–343.
- Cao, J., Goyal, A., Xiao, X., & Zhan, X. (2023). Implied volatility changes and corporate bond returns. *Management Science, 69*(3), 1375–1397. https://doi.org/10.1287/mnsc.2022.4379
- Carr, P., & Wu, L. (2010). Stock options and credit default swaps. *Journal of Financial Econometrics, 8*(4), 409–449.
- Carr, P., & Wu, L. (2011). A simple robust link between American puts and credit protection. *RFS, 24*(2), 473–505.
- Chen, H., Doshi, H., & Seo, S. B. (2023). Synthetic options and implied volatility for the corporate bond market. *JFQA, 58*(3), 1295–1325.
- Collin-Dufresne, P., Goldstein, R., & Yang, F. (2012). On the relative pricing of long-maturity index options and collateralized debt obligations. *Journal of Finance, 67*(6), 1983–2014.
- Cremers, M., Driessen, J., Maenhout, P., & Weinbaum, D. (2008). Individual stock-option prices and credit spreads. *JBF, 32*(12), 2706–2715. https://doi.org/10.1016/j.jbankfin.2008.07.005
- Culp, C. L., Nozawa, Y., & Veronesi, P. (2018). Option-based credit spreads. *AER, 108*(2), 454–488. https://doi.org/10.1257/aer.20151606
- Duong, H., & Park, J. (2025). Understanding the cross-section of CDS returns using equity options. *Journal of Financial Research, 48*, 982–1012. https://doi.org/10.1111/jfir.12446
- Forte, S., & Lovreta, L. (2019). *Finance Research Letters, 28*, 107–111.
- Hong, C., & Park, Y. J. (2025). Do changes in the implied volatility of stock options predict future changes in CDS spreads? *Journal of Derivatives and Quantitative Studies, 33*(2). https://doi.org/10.1108/jdqs-12-2024-0048
- Huang, Jiang, & Li (2023). Downside variance premium, firm fundamentals, and expected corporate bond returns. *JBF, 154*.
- Kelly, B., Manzo, G., & Palhares, D. (2025). Credit-implied volatility. *Financial Analysts Journal, 81*(2).
- Wang, H., Zhou, H., & Zhou, Y. (2013). Credit default swap spreads and variance risk premia. *JBF, 37*, 3733–3746.
- Zhang, B. Y., Zhou, H., & Zhu, H. (2009). Explaining credit default swap spreads with the equity volatility and jump risks of individual firms. *RFS, 22*.

**Integration, limits to arbitrage, recent and ML**
- Bai, J., & Collin-Dufresne, P. (2019). The CDS-bond basis. *Financial Management, 48*, 417–439. https://doi.org/10.1111/fima.12252
- Bali, T., Beckmeyer, H., & Goyal, A. (2023). A joint factor model for bonds, stocks, and options. Working paper, SSRN 4589282.
- Bali, T., Goyal, A., Huang, D., Jiang, F., & Wen, Q. (2020). Predicting corporate bond returns: Merton meets machine learning. Working paper, SSRN 3686164.
- Bartram, S., Grinblatt, M., & Nozawa, Y. (2025). Book-to-market, mispricing, and the cross-section of corporate bond returns. *JFQA, 60*, 1185–1233.
- Choi, J., & Kim, Y. (2018). Anomalies and market (dis)integration. *Journal of Monetary Economics, 100*, 16–34. https://doi.org/10.1016/j.jmoneco.2018.06.003
- Chordia, T., Goyal, A., Nozawa, Y., Subrahmanyam, A., & Tong, Q. (2017). Are capital market anomalies common to equity and corporate bond markets? *JFQA, 52*(4), 1301–1342.
- Collin-Dufresne, P., Goldstein, R., & Martin, J. S. (2001). The determinants of credit spread changes. *Journal of Finance, 56*(6), 2177–2207. https://doi.org/10.1111/0022-1082.00402
- Dickerson, A., Julliard, C., & Mueller, P. (forthcoming). The co-pricing factor zoo. *JFE*. arXiv 2604.04430.
- Dickerson, A., Mueller, P., & Robotti, C. (2023). Priced risk in corporate bonds. *JFE, 150*(2), 103707.
- Dickerson, A., Robotti, C., & Rossetti, G. (2026). The corporate bond factor replication crisis. arXiv 2604.07880.
- Friewald, N., Wagner, C., & Zechner, J. (2014). The cross-section of credit risk premia and equity returns. *Journal of Finance, 69*(6), 2419–2469. https://doi.org/10.1111/jofi.12143
- Haesen, D., Houweling, P., & van Zundert, J. (2017). Momentum spillover from stocks to corporate bonds. *JBF, 79*, 28–41. https://doi.org/10.1016/j.jbankfin.2017.03.003
- Kelly, B., Palhares, D., & Pruitt, S. (2023). Modeling corporate bond returns. *Journal of Finance, 78*(4), 1967–2008. https://doi.org/10.1111/jofi.13233
- Sandulescu, M. (2020). How integrated are corporate bond and stock markets? Working paper, SSRN 3528252.
- van Zundert, J., & Driessen, J. (2022). Stocks versus corporate bonds: A cross-sectional puzzle. *JBF, 137*, 106447. https://doi.org/10.1016/j.jbankfin.2022.106447

<!-- AUTHORED REGION END -->
