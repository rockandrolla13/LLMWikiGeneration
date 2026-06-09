
---

## [2026-05-15] ingest | Conformal Prediction with Tukey g-h batch (2 PDFs)

Operation ID: op_conformal_gh_20260515
Status: completed

**Sources Created:**
- sources/peters-2026-quantile-diffusions - Tukey g-h quantile diffusions for dynamic risk modelling (Peters, Macrina, Brannelly 2026)
- sources/peters-2026-asynchronous-cir - Asynchronous regime-switching CIR with Onsager-Machlup THMM (Peters et al. 2026)

**Pages Updated:**
- entities/gareth-peters - Added new sources and research areas
- analyses/conformal-tukey-gh-intervals - Added reference to Peters 2026 quantile diffusions
- concepts/tukey-gh-transformation - Added continuous-time extension section

Summary: Batch ingestion of 2 PDFs from ConformalPrediction_w_GH folder. Key contribution: Peters (2026) provides the continuous-time theoretical foundation for Tukey g-h quantile processes, directly supporting the conformal-tukey-gh-intervals research direction. Random-level and function-valued constructions enable dynamic skewness/kurtosis modulation for VaR/TVaR and insurance applications.

---

## [2026-05-06] ingest | ETF Flows topic batch (3 PDFs)

Operation ID: op_etfflows_20260506
Status: completed

**Sources Created:**
- sources/optiver-2025-corporate-bond-etf-contraflow - Corporate bond ETF contraflow strategy (Optiver 2025)
- sources/petit-2025-data-driven-flow-etf - Data-driven trade flow decomposition (Petit et al. ICAIF 2025)
- sources/chao-2019-etf-flows-prices - Why do ETF flows move prices (Deutsche Bank 2019)

**Concepts Created:**
- concepts/etf-flows - ETF ownership changes and return predictability
- concepts/flow-decomposition - Allocation, index, weight reconstitution decomposition
- concepts/index-reconstitution - Index additions/deletions creating predictable flows

Summary: Batch ingestion of 3 PDFs covering ETF flow analysis, contraflow trading strategies, and flow decomposition methodologies. Key themes: passive investing inefficiencies, mean reversion in ETF-driven flows, and ML-based trade clustering.

---

## [2026-05-05] ingest | creditETF topic batch (5 PDFs)

Operation ID: op_creditetf_20260505
Status: completed

**Sources Created:**
- sources/spec-2012-single-name-fundamental - Single-name credit analysis framework
- sources/pullirsch-2006-credit-spread-risk - Credit-spread curve estimation (Pullirsch 2006)
- sources/trinh-2006-lever-framework - LEVER LBO risk scoring (Lehman 2006)
- sources/lehman-2007-qcr-quarterly - QCR Quarterly with base correlation mapping
- sources/ubs-2012-next-gen-credit-curves - Unified hazard-rate curves (UBS Delta)

**Concepts Created:**
- concepts/lever-score - LBO/recap risk scoring framework
- concepts/hazard-rate-curve - Unified credit curve approach
- concepts/base-correlation - CDO tranche pricing framework
- concepts/cds-bond-basis - Cross-instrument spread differences
- concepts/lbo-risk - Leveraged buyout event risk
- concepts/spread-per-turn-of-leverage - Relative value metric

**Entities Created:**
- entities/lehman-brothers - Investment bank (historical)
- entities/ubs-delta - Portfolio analytics system
- entities/rainer-pullirsch - Credit risk researcher
- entities/minh-trinh - LEVER framework co-author
- entities/bodha-bhattacharya - LEVER framework co-author
- entities/lindsey-matthews - UBS Delta client development
- entities/luca-bosatta - UBS Delta risk modelling

Summary: Batch ingestion of 5 PDFs covering credit curve estimation, LBO event risk, CDO tranche pricing, and unified hazard-rate methodologies. Key themes: relative value analysis, credit-spread risk measurement, and practical quantitative credit research from Lehman Brothers and UBS Delta.

---

## [2026-04-26] ingest | Ingested spci-2022.pdf (SPCI for Time Series)

Operation ID: op_spci_20260426
Status: completed
Created: sources/xu-2022-spci
Entities: entities/chen-xu, entities/yao-xie
Concepts: concepts/spci, concepts/quantile-random-forest

Summary: Sequential Predictive Conformal Inference (SPCI) by Xu & Xie (ICML 2023). Uses quantile random forests on residuals to exploit temporal dependence, achieving narrower prediction intervals than EnbPI and other methods.


---

## [2026-04-26] ingest | Ingested copula-conformal-2022.pdf (CopulaCPTS)

Operation ID: op_copula_20260426
Status: completed
Created: sources/sun-2022-copula-cpts
Entities: entities/sophia-sun, entities/rose-yu
Concepts: concepts/copulas, concepts/multi-step-conformal-prediction

Summary: CopulaCPTS by Sun & Yu (ICLR 2024). Uses copulas to model joint uncertainty across multiple forecast steps, providing full-horizon validity guarantees with 30-50% tighter confidence regions than Bonferroni correction.


---

## [2026-04-25] ingest | Ingested output

Operation ID: op_32a173c93db1
Status: completed
Created: sources/output


---

## [2026-04-25] ingest | Ingested 030011_1_online

Operation ID: op_4671eae9eb2e
Status: completed
Created: sources/030011_1_online


---

## [2026-04-25] ingest | Ingested 1-s2.0-S0167668720300019-main

Operation ID: op_dc2bd8593a40
Status: completed
Created: sources/1_s20_s0167668720300019_main


---

## [2026-04-25] ingest | Ingested 1-s2.0-S0304405X23001393-main

Operation ID: op_5a7e80ae7771
Status: completed
Created: sources/1_s20_s0304405x23001393_main


---

## [2026-04-25] ingest | Ingested 2201.01330v3

Operation ID: op_750cf5d0057c
Status: completed
Created: sources/220101330v3


---

## [2026-04-25] ingest | Ingested 2412.05889v1

Operation ID: op_a9e7ae2667f4
Status: completed
Created: sources/241205889v1


---

## [2026-04-25] ingest | Ingested multi-output-gaussian-processes-for-multi-population-longevity-modelling

Operation ID: op_5bf8569a238f
Status: completed
Created: sources/multi_output_gaussian_processes_for_multi_population_longevity_modelling


---

## [2026-04-25] ingest | Ingested ssrn-5075265

Operation ID: op_f5cafdc45b64
Status: completed
Created: sources/ssrn_5075265

---

## [2026-05-21] batch_ingest | JFE batch ingestion (12 papers)

Operation ID: op_jfe_batch_20260521
Status: completed
Created: 12 sources, 51 entities, 71 concepts
Updated: 7 existing pages (alvaro-cartea, factor-models, limit-order-book, market-making, liquidity-risk, quantile-regression, factor-investing)
Sources added:
- sources/andreou-2020-mixed-frequency-macro-finance
- sources/chen-2024-jump-clustering-information-flows
- sources/bodilsen-2025-hf-dynamic-factor-portfolio
- sources/cartea-2025-statistical-predictions-trading
- sources/peiris-2025-rnn-har-var
- sources/barendse-2026-efficient-tail-interquantile
- sources/cotturo-2026-multifactor-timing-deep-learning
- sources/nolte-2011-fx-latent-factor-panel-intensity
- sources/boffelli-2017-euro-bond-spread-correlations
- sources/huber-2026-information-flows-trading-networks
- sources/coppola-2025-asset-class-liquidity-indicators
- sources/xie-2026-realized-probability-market-timing

Summary: Batch ingestion of 12 papers from Journal of Financial Econometrics (8 papers spanning factor models, jump clustering, HF portfolio selection, electronic-market order-flow prediction, RNN-HAR VaR, tail/interquantile expectations, multifactor timing, FX panel intensity, bond spread correlations), plus one paper each from Journal of Accounting and Economics (Huber et al on dealer networks), Journal of Financial Stability (Coppola/Urga/Varaldo on liquidity-risk regimes), and Studies in Nonlinear Dynamics and Econometrics (Xie et al on realized probability market timing). MIND_MAP nodes [168]-[179] added under hubs [3], [5], [7], [9], [11].


---

## [2026-06-09] ingest | Ingest (credit-macro): The Determinants of Credit Spread Changes

Operation ID: op_8c5d21d8cada
Status: completed
Created: sources/collin-dufresne-2001-determinants-credit-spread-changes


---

## [2026-06-09] ingest | Ingest (credit-macro): Strictly Proper Scoring Rules, Prediction, and Estimation

Operation ID: op_c66282c02cb0
Status: completed
Created: sources/gneiting-2007-strictly-proper-scoring-rules


---

## [2026-06-09] ingest | Ingest (credit-macro): Right Tail Hedging: Managing Risk When Markets Melt Up

Operation ID: op_2aa0f0b54fec
Status: completed
Created: sources/bhansali-2018-right-tail-hedging


---

## [2026-06-09] ingest | Ingest (credit-macro): The Book of Why: The New Science of Cause and Effect

Operation ID: op_9fa651e5a47d
Status: completed
Created: sources/pearl-2018-book-of-why


---

## [2026-06-09] ingest | Ingest (credit-macro): Understanding Changes in Corporate Credit Spreads

Operation ID: op_9032b5354106
Status: completed
Created: sources/avramov-2007-changes-corporate-credit-spreads


---

## [2026-06-09] ingest | Ingest (credit-macro): Contingent Claims and Hedging of Credit Risk with Equity Options

Operation ID: op_32f967511f6a
Status: completed
Created: sources/avino-2024-hedging-credit-equity-options


---

## [2026-06-09] ingest | Ingest (credit-macro): Limited arbitrage between equity and credit markets

Operation ID: op_cbc7ffd3de97
Status: completed
Created: sources/kapadia-2012-limited-arbitrage-equity-credit


---

## [2026-06-09] ingest | Ingest (credit-macro): Leading indicators of crisis incidence: Evidence from developed countries

Operation ID: op_0ea28cacd6be
Status: completed
Created: sources/babecky-2013-leading-indicators-crisis-incidence


---

## [2026-06-09] ingest | Ingest (credit-macro): Risk premia in the term structure of interest rates: a panel data approach

Operation ID: op_2de49c1476ac
Status: completed
Created: sources/bams-2003-risk-premia-term-structure-panel


---

## [2026-06-09] ingest | Ingest (credit-macro): Banking, debt, and currency crises in developed countries: Stylized facts and early warning indicators

Operation ID: op_4b956bf11812
Status: completed
Created: sources/babecky-2014-developed-country-crisis-ewi


---

## [2026-06-09] ingest | Ingest (credit-macro): Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper Scoring Rules

Operation ID: op_b7a89e800e62
Status: completed
Created: sources/ziel-2019-multivariate-forecasting-evaluation


---

## [2026-06-09] ingest | Ingest (credit-macro): The Level and Persistence of Growth Rates

Operation ID: op_b7f0270dc818
Status: completed
Created: sources/chan-2001-level-persistence-growth-rates


---

## [2026-06-09] ingest | Ingest (credit-macro): Predicting the Global Crisis Recovery Period: Lessons from the 1997 Crisis

Operation ID: op_1cb31aa3f9b0
Status: completed
Created: sources/duasa-2010-predicting-crisis-recovery


---

## [2026-06-09] ingest | Ingest (credit-macro): Morgan Stanley Global Credit Webcast - May 2026: Debating the Mid-Year Outlook

Operation ID: op_b373b1b50fd7
Status: completed
Created: sources/patkar-2026-ms-global-credit-midyear


---

## [2026-06-09] ingest | Ingest (credit-macro): AI Capex Funding: Data Center - Hyperscaler Bond Matrix Version 1.0

Operation ID: op_e7bd8d02c4df
Status: completed
Created: sources/hamid-2026-ai-capex-funding-bond-matrix


---

## [2026-06-09] ingest | Ingest (credit-macro): 2026: Steady, but AI & the Hawks are Circling (Software)

Operation ID: op_a772291713fc
Status: completed
Created: sources/caprio-2026-steady-but-ai


---

## [2026-06-09] ingest | Ingest (credit-macro): The Flow Whisperer: TAARSS says prefer a mix of bonds and equities in Q1

Operation ID: op_a565c113018a
Status: completed
Created: sources/mercado-2015-taarss-flow-whisperer


---

## [2026-06-09] ingest | Ingest (credit-macro): Citi Global Theme Book

Operation ID: op_e01d78c0f933
Status: completed
Created: sources/citi-global-theme-book


---

## [2026-06-09] ingest | Ingest (credit-macro): Citi Macro Views: Global Strategy and Macro Theme Book, Q1 2019

Operation ID: op_20932109df67
Status: completed
Created: sources/schofield-2019-citi-macro-views


---

## [2026-06-09] ingest | Ingest (credit-macro): Introduction to the Alaph Capital Liquid Macro Credit Fund

Operation ID: op_d95e21d08a98
Status: completed
Created: sources/ahmad-2014-alaph-liquid-macro-credit-fund


---

## [2026-06-09] ingest | Ingest (credit-macro): Bayes and Base Rates: How History Can Guide Our Assessment of the Future

Operation ID: op_35ca9dd91883
Status: completed
Created: sources/mauboussin-2026-bayes-base-rates


---

## [2026-06-09] ingest | Ingest (credit-macro): Business Plan Details for Xantium: Systematic Spread Fixed Income Trading

Operation ID: op_0d00a43bc19a
Status: completed
Created: sources/koukorinis-2024-xantium-business-plan


---

## [2026-06-09] ingest | Ingest (credit-macro): Advanced Algorithmic Trading

Operation ID: op_b7b9ceb47ac6
Status: completed
Created: sources/halls-moore-advanced-algorithmic-trading


---

## [2026-06-09] ingest | Ingest (credit-macro): Advanced Futures Trading Strategies

Operation ID: op_65664026f29b
Status: completed
Created: sources/carver-2023-advanced-futures-trading-strategies


---

## [2026-06-09] ingest | Ingest (credit-macro): Causal Inference: What If

Operation ID: op_3d8a63fdb139
Status: completed
Created: sources/hernan-2020-causal-inference-what-if


---

## [2026-06-09] ingest | Ingest (credit-macro): Causality and Explanation

Operation ID: op_1ee15510fea6
Status: completed
Created: sources/salmon-1998-causality-and-explanation


---

## [2026-06-09] ingest | Ingest (credit-macro): Counterfactuals and Probability

Operation ID: op_cf8947eec072
Status: completed
Created: sources/schulz-counterfactuals-and-probability


---

## [2026-06-09] ingest | Ingest (credit-macro): Data Analysis and Data Mining: An Introduction

Operation ID: op_517152a99a7e
Status: completed
Created: sources/azzalini-2012-data-analysis-and-data-mining


---

## [2026-06-09] ingest | Ingest (credit-macro): Economic Analysis Through Mathematics: Tools and Techniques for Decision Making

Operation ID: op_eecfdd0ee8cd
Status: completed
Created: sources/lukac-2026-economic-analysis-through-mathematics


---

## [2026-06-09] ingest | Ingest (credit-macro): Economics for Investment Decision Makers Workbook: Micro, Macro, and International Economics

Operation ID: op_ff60dc24238d
Status: completed
Created: sources/piros-2013-economics-investment-decision-makers-workbook


---

## [2026-06-09] ingest | Ingest (credit-macro): The Evaluation and Optimization of Trading Strategies

Operation ID: op_dac7763811d3
Status: completed
Created: sources/pardo-2008-evaluation-optimization-trading-strategies


---

## [2026-06-09] ingest | Ingest (credit-macro): Expected Returns: An Investor's Guide to Harvesting Market Rewards

Operation ID: op_f76556d4f11f
Status: completed
Created: sources/ilmanen-2011-expected-returns


---

## [2026-06-09] ingest | Ingest (credit-macro): Explanation in Causal Inference: Methods for Mediation and Interaction

Operation ID: op_99b4040d069a
Status: completed
Created: sources/vanderweele-2015-explanation-causal-inference


---

## [2026-06-09] ingest | Ingest (credit-macro): Fed Up! Success, Excess and Crisis Through the Eyes of a Hedge Fund Macro Trader

Operation ID: op_73d6730202f6
Status: completed
Created: sources/lancaster-2021-fed-up


---

## [2026-06-09] ingest | Ingest (credit-macro): Finding Alphas: A Quantitative Approach to Building Trading Strategies (Second Edition)

Operation ID: op_5e2408512522
Status: completed
Created: sources/tulchinsky-2020-finding-alphas


---

## [2026-06-09] ingest | Ingest (credit-macro): How Not to Be Wrong: The Power of Mathematical Thinking

Operation ID: op_5e764acf4757
Status: completed
Created: sources/ellenberg-2014-how-not-to-be-wrong


---

## [2026-06-09] ingest | Ingest (credit-macro): Investing Amid Low Expected Returns: Making the Most When Markets Offer the Least

Operation ID: op_2fb5ee9b1941
Status: completed
Created: sources/ilmanen-2022-investing-amid-low-expected-returns


---

## [2026-06-09] ingest | Ingest (credit-macro): Monetary Policy after the Great Recession: The Role of Interest Rates

Operation ID: op_89aace8429f9
Status: completed
Created: sources/sieron-2021-monetary-policy-after-great-recession


---

## [2026-06-09] ingest | Ingest (credit-macro): Monetary Policy in Times of Crisis: A Tale of Two Decades of the European Central Bank

Operation ID: op_bc5afc77bdfe
Status: completed
Created: sources/rostagno-2021-ecb-monetary-policy-crisis


---

## [2026-06-09] ingest | Ingest (credit-macro): Money, Bank Credit, and Economic Cycles

Operation ID: op_68333b9ca48e
Status: completed
Created: sources/huertadesoto-2006-money-bank-credit


---

## [2026-06-09] ingest | Ingest (credit-macro): Mostly Harmless Econometrics: An Empiricist's Companion

Operation ID: op_fa4f0577e2a2
Status: completed
Created: sources/angrist-2009-mostly-harmless-econometrics


---

## [2026-06-09] ingest | Ingest (credit-macro): Recursive Macroeconomic Theory

Operation ID: op_7025e7dec594
Status: completed
Created: sources/ljungqvist-2012-recursive-macroeconomic-theory


---

## [2026-06-09] ingest | Ingest (credit-macro): Systematic Trading: A unique new method for designing trading and investing systems

Operation ID: op_4e728a91977f
Status: completed
Created: sources/carver-2015-systematic-trading


---

## [2026-06-09] ingest | Ingest (credit-macro): Thinking in Systems: A Primer

Operation ID: op_ac2a6777b704
Status: completed
Created: sources/meadows-2008-thinking-in-systems


---

## [2026-06-09] ingest | Ingest (credit-macro): Thinking in Systems and Mental Models: Think Like a Super Thinker

Operation ID: op_65673c42dc71
Status: completed
Created: sources/dawson-2020-systems-mental-models


---

## [2026-06-09] ingest | Ingest (credit-macro): Time, Tense, and Causation

Operation ID: op_c4b5641fe0e6
Status: completed
Created: sources/tooley-1997-time-tense-causation


---

## [2026-06-09] ingest | Analysis: credit-spread determinants + do-calculus reading

Operation ID: op_db16de9c3673
Status: completed
Created: analyses/credit-spread-determinants-causal-reading


---

## [2026-06-09] ingest | Ingest (credit-macro): A Birdie for the Balance Sheet — Duration and Curves

Operation ID: op_7fec3280be2d
Status: completed
Created: sources/ms-2019-01-26-duration-and-curves


---

## [2026-06-09] ingest | Ingest (credit-macro): A High Yield Hedge

Operation ID: op_dc673497112e
Status: completed
Created: sources/ms-2019-03-22-high-yield-hedge


---

## [2026-06-09] ingest | Ingest (credit-macro): Add to Credit – and How Much Do Markets Lead the Economy?

Operation ID: op_db12f9b23eeb
Status: completed
Created: sources/ms-2020-03-27-add-to-credit


---

## [2026-06-09] ingest | Ingest (credit-macro): Assessing Risk Premia in EMFX (Part 1): A Two-Factor Model Approach

Operation ID: op_f76ca169d4c2
Status: completed
Created: sources/ms-2018-06-05-emfx-risk-premia-two-factor


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Playbook – April 2019: Late-Cycle and Weaker Dollar

Operation ID: op_9bce1c594bdd
Status: completed
Created: sources/ms-2019-04-07-cross-asset-playbook-late-cycle-weaker-dollar


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Playbook – February 2019: Fundamental Problems

Operation ID: op_a24c9426f4c5
Status: completed
Created: sources/ms-2019-02-11-cross-asset-playbook-fundamental-problems


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Playbook – February 2019: Fundamental Problems

Operation ID: op_65f5528335bf
Status: completed
Created: sources/ms-2019-02-11-cross-asset-playbook-fundamental-problems-2


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Playbook – January 2019: Turning Points Intact

Operation ID: op_d8a9833a01e6
Status: completed
Created: sources/ms-2019-01-13-cross-asset-playbook-turning-points-intact


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Playbook – March 2019: Overpricing Goldilocks, Underpricing Tails

Operation ID: op_a8f8bedd0578
Status: completed
Created: sources/ms-2019-03-10-cross-asset-playbook-overpricing-goldilocks


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Playbook – March 2020: Brace for Recession

Operation ID: op_8cbca8fb34c9
Status: completed
Created: sources/ms-2020-03-17-cross-asset-playbook-brace-for-recession


---

## [2026-06-09] ingest | Ingest (credit-macro): Global In the Flow: 2018 by the Numbers

Operation ID: op_358cbe1f9288
Status: completed
Created: sources/ms-2019-01-02-global-in-the-flow-2018-by-the-numbers


---

## [2026-06-09] ingest | Ingest (credit-macro): Global In the Flow: February Recap

Operation ID: op_2e8d9f21c33a
Status: completed
Created: sources/ms-2019-03-01-global-in-the-flow-february-recap


---

## [2026-06-09] ingest | Ingest (credit-macro): Global In the Flow: First Quarter Recap

Operation ID: op_e7ca822b13c7
Status: completed
Created: sources/ms-2019-04-01-cross-asset-1q-recap


---

## [2026-06-09] ingest | Ingest (credit-macro): Global In the Flow: October Recap

Operation ID: op_c4876abb602c
Status: completed
Created: sources/ms-2018-11-01-cross-asset-october-recap


---

## [2026-06-09] ingest | Ingest (credit-macro): Corporate Credit Research: The Cause of the Pause

Operation ID: op_d18b379f7e4c
Status: completed
Created: sources/ms-2019-01-25-cause-of-the-pause


---

## [2026-06-09] ingest | Ingest (credit-macro): Corporate Credit Research: Meet in the Middle

Operation ID: op_9db3d21d97a0
Status: completed
Created: sources/ms-2019-04-12-meet-in-the-middle


---

## [2026-06-09] ingest | Ingest (credit-macro): US Interest Rate Strategy: Funding Market Signals (Correction)

Operation ID: op_11494c4ba831
Status: completed
Created: sources/ms-2018-04-05-funding-market-signals


---

## [2026-06-09] ingest | Ingest (credit-macro): Introducing the Credit Bond Market Indicator (credit-BMI)

Operation ID: op_17a7cbea0a0d
Status: completed
Created: sources/ms-2018-03-16-credit-bmi


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Brief: Risk Parity — Worst Behind Us

Operation ID: op_e7184f31a832
Status: completed
Created: sources/ms-2020-03-20-risk-parity-deleveraging


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Brief: Taking Stock — Recent Moves in Context

Operation ID: op_1c318fb3750a
Status: completed
Created: sources/ms-2020-03-10-cross-asset-moves-context


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Dispatches: Add to Credit — and How Much Do Markets Lead the Economy?

Operation ID: op_aec9dbd6f445
Status: completed
Created: sources/ms-2020-03-27-add-to-credit-markets-lead-economy


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Dispatches: Are You Sure That's 'Low Beta'?

Operation ID: op_1d33b7e33fa8
Status: completed
Created: sources/ms-2019-04-14-low-beta-defensiveness-scorecard


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Dispatches: Could Dollar Weakness Be Self-Catalysing?

Operation ID: op_e2dd321a5012
Status: completed
Created: sources/ms-2019-02-03-self-catalysing-dollar-weakness


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Dispatches: Melting Up Is Hard to Do

Operation ID: op_f6df8da495c0
Status: completed
Created: sources/ms-2019-04-29-melt-up-skepticism


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Dispatches: Volatility Peaks Before Markets Trough

Operation ID: op_6c9f9ed49e2c
Status: completed
Created: sources/ms-2020-03-19-volatility-peaks-before-markets-trough


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Dispatches: What Do Recoveries Usually Look Like?

Operation ID: op_8d7302c2955b
Status: completed
Created: sources/ms-2020-04-01-what-do-recoveries-look-like


---

## [2026-06-09] ingest | Ingest (credit-macro): Crossing the Rubicon (Government Bonds)

Operation ID: op_3f734c237057
Status: completed
Created: sources/ms-2019-04-05-crossing-the-rubicon-government-bonds


---

## [2026-06-09] ingest | Ingest (credit-macro): ECB Preview: TLTRO Funding on its Way

Operation ID: op_b995ec803812
Status: completed
Created: sources/ms-2019-02-28-ecb-preview-tltro-funding


---

## [2026-06-09] ingest | Ingest (credit-macro): EM Quant Strategy: EM Risk Indicator - A Regime-Switching Model Approach

Operation ID: op_3fecbbf5f529
Status: completed
Created: sources/ms-2018-07-09-em-risk-indicator-regime-switching


---

## [2026-06-09] ingest | Ingest (credit-macro): EM Quant Strategy: EMFX Quant's Lab - Carry Performs

Operation ID: op_c85cb5443521
Status: completed
Created: sources/ms-2019-06-03-emfx-quants-lab-carry-performs


---

## [2026-06-09] ingest | Ingest (credit-macro): EMFX Quant's Lab: Steady Path

Operation ID: op_98f4e18a4234
Status: completed
Created: sources/ms-2019-02-11-emfx-quants-lab-steady-path


---

## [2026-06-09] ingest | Ingest (credit-macro): Trading Risk Premia in EMFX (Part 2): A mixed strategy using Volatility Risk Premia (VIRP)

Operation ID: op_b42b5e980551
Status: completed
Created: sources/ms-2018-11-05-trading-risk-premia-emfx-virp


---

## [2026-06-09] ingest | Ingest (credit-macro): EM Strategy Update: No Rush for the Exits

Operation ID: op_38f00bc3fa8b
Status: completed
Created: sources/ms-2013-11-26-em-strategy-no-rush-for-the-exits


---

## [2026-06-09] ingest | Ingest (credit-macro): Emerging Markets Quantitative Quarterly: EM Fixed Income and Foreign Exchange Strategy

Operation ID: op_c94b39bde1d2
Status: completed
Created: sources/ms-2010-09-15-em-quantitative-quarterly


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategy: Euro Sovereign Bond Market Indicators (eBMIs)

Operation ID: op_ec5470251428
Status: completed
Created: sources/ms-2016-04-13-euro-sovereign-bond-market-indicators


---

## [2026-06-09] ingest | Ingest (credit-macro): Europe Economics: Recession Returns

Operation ID: op_52b692fb9029
Status: completed
Created: sources/ms-2011-11-28-europe-economics-recession-returns


---

## [2026-06-09] ingest | Ingest (credit-macro): Europe looks set to surprise on the upside

Operation ID: op_a174b4a5a3ac
Status: completed
Created: sources/ms-2019-03-11-europe-surprise-upside


---

## [2026-06-09] ingest | Ingest (credit-macro): European Banks - Equity & Credit: Untested Cycle - watch for corporate risk

Operation ID: op_8466e2a1a292
Status: completed
Created: sources/ms-2019-03-11-untested-cycle-corporate-risk


---

## [2026-06-09] ingest | Ingest (credit-macro): European Banks: Autumn AT1 Primer – Extension and Par Calls

Operation ID: op_fd2742aaaaaf
Status: completed
Created: sources/ms-2018-11-02-at1-primer-extension-par-calls


---

## [2026-06-09] ingest | Ingest (credit-macro): European Banks: CRR2 Agreed; ADI Boost for AT1

Operation ID: op_3cc281df6f28
Status: completed
Created: sources/ms-2019-02-15-crr2-agreed-adi-boost-at1


---

## [2026-06-09] ingest | Ingest (credit-macro): European Banks: Facing the Cycle – Picking Swiss

Operation ID: op_9806b4f81317
Status: completed
Created: sources/ms-2020-03-11-facing-cycle-picking-swiss


---

## [2026-06-09] ingest | Ingest (credit-macro): European Banks: Hunting for Value in Tier 2 and Seniors

Operation ID: op_54b7ac3e8f3d
Status: completed
Created: sources/ms-2019-05-23-value-tier2-seniors


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Playbook: A Reluctant Rally

Operation ID: op_0338b473f157
Status: completed
Created: sources/ms-2019-01-28-european-credit-reluctant-rally


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy: Corporate Hybrids Playbook

Operation ID: op_cfd8484e49f6
Status: completed
Created: sources/ms-2015-11-16-corporate-hybrids-playbook


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy: What We're Watching

Operation ID: op_a8f9206b84a2
Status: completed
Created: sources/ms-2012-03-12-what-were-watching


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy: A Premium for Size

Operation ID: op_aac3dd6351dc
Status: completed
Created: sources/ms-2019-03-04-a-premium-for-size


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy: Corporate Hybrids Playbook — Staying in Short Calls, Revisiting Call Risks

Operation ID: op_a84f7e1dff8a
Status: completed
Created: sources/ms-2019-02-04-corporate-hybrids-playbook


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy: IG Fundamentals — In Good Shape

Operation ID: op_0417ac91e4b8
Status: completed
Created: sources/ms-2017-06-23-ig-fundamentals-in-good-shape


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy — What We're Watching

Operation ID: op_bd71e75d44a8
Status: completed
Created: sources/ms-2017-07-10-european-credit-watch


---

## [2026-06-09] ingest | Ingest (credit-macro): European Credit Strategy — What We're Watching

Operation ID: op_ba1e83b981b6
Status: completed
Created: sources/ms-2019-01-28-european-credit-watch


---

## [2026-06-09] ingest | Ingest (credit-macro): European Economics: A Practitioner's Guide to European Macro Indicators

Operation ID: op_db215fb8d8ca
Status: completed
Created: sources/ms-2010-06-04-european-macro-indicators-guide


---

## [2026-06-09] ingest | Ingest (credit-macro): European Economics Weekly — Bank Funding Focus

Operation ID: op_4571b6988981
Status: completed
Created: sources/ms-2019-03-01-bank-funding-focus


---

## [2026-06-09] ingest | Ingest (credit-macro): European Economics Weekly — Ongoing Weakness

Operation ID: op_1d1064072f9d
Status: completed
Created: sources/ms-2019-02-15-ongoing-weakness


---

## [2026-06-09] ingest | Ingest (credit-macro): European High Yield Strategy Monthly Leveraged Finance Playbook — Performance

Operation ID: op_039523490922
Status: completed
Created: sources/ms-2017-06-23-hy-leveraged-finance-playbook


---

## [2026-06-09] ingest | Ingest (credit-macro): European High Yield Strategy Monthly Leveraged Finance Playbook — Returns

Operation ID: op_250ae2fc3e19
Status: completed
Created: sources/ms-2012-03-09-european-hy-leveraged-finance-playbook


---

## [2026-06-09] ingest | Ingest (credit-macro): FAQs on Hybrids — Hybrids Monitor and Relative Value (Corporate Hybrids Playbook)

Operation ID: op_eb9ee07d5ead
Status: completed
Created: sources/ms-2013-12-04-faqs-on-corporate-hybrids


---

## [2026-06-09] ingest | Ingest (credit-macro): Goldilocks Whiplash (Sunday Start: What's Next in Global Macro)

Operation ID: op_5ae117fe925b
Status: completed
Created: sources/ms-2019-02-17-goldilocks-whiplash


---

## [2026-06-09] ingest | Ingest (credit-macro): An Easing Trio (Sunday Start: What's Next in Global Macro)

Operation ID: op_7e6ee47a9ca8
Status: completed
Created: sources/ms-2019-03-03-an-easing-trio


---

## [2026-06-09] ingest | Ingest (credit-macro): Another Turning Point (Sunday Start: What's Next in Global Macro)

Operation ID: op_8b63f907bde6
Status: completed
Created: sources/ms-2019-02-24-china-current-account-turning-point


---

## [2026-06-09] ingest | Ingest (credit-macro): Weekly Credit Wrap: High Yield — Pricing Tomorrow's Deleveraging Today

Operation ID: op_7c601c38f3b6
Status: completed
Created: sources/ms-2011-04-18-hy-pricing-tomorrows-deleveraging


---

## [2026-06-09] ingest | Ingest (credit-macro): Weekly Credit Wrap: High Grade, Mid-Cycle

Operation ID: op_574a9c114e0f
Status: completed
Created: sources/ms-2011-03-28-high-grade-mid-cycle


---

## [2026-06-09] ingest | Ingest (credit-macro): For Whom the Tariffs Toll

Operation ID: op_f84b30235bea
Status: completed
Created: sources/ms-2019-05-17-tariffs-government-bonds


---

## [2026-06-09] ingest | Ingest (credit-macro): Correction: Global Futures Rolls Report: Eurex Futures Rolls - Mar 19 / Jun 19 Roll

Operation ID: op_29f443fac943
Status: completed
Created: sources/ms-2019-02-13-eurex-futures-rolls


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Insights Day 2019 - Polling Results

Operation ID: op_533f61919f1b
Status: completed
Created: sources/ms-2019-03-01-global-insights-polling


---

## [2026-06-09] ingest | Ingest (credit-macro): Differentiation and Divergence

Operation ID: op_046cb9da4496
Status: completed
Created: sources/ms-2011-05-06-differentiation-divergence


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Volatility Playbook: A Market of Many Extremes

Operation ID: op_79c2f4aec6f9
Status: completed
Created: sources/ms-2020-03-25-global-volatility-playbook


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Volatility Playbook: What's Wrong with FX Volatility

Operation ID: op_690b7614875d
Status: completed
Created: sources/ms-2019-06-28-fx-volatility-playbook


---

## [2026-06-09] ingest | Ingest (credit-macro): The Global Macro Analyst: Japanification or Salvation

Operation ID: op_afec8e8ddfac
Status: completed
Created: sources/ms-2013-10-30-japanification-or-salvation


---

## [2026-06-09] ingest | Ingest (credit-macro): China – Doing whatever it takes

Operation ID: op_e0187f5c3ed7
Status: completed
Created: sources/ms-2019-01-18-china-doing-whatever-it-takes


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Growth Tracker – DMs Underperform More than Expected

Operation ID: op_cc1501d9a148
Status: completed
Created: sources/ms-2019-01-24-global-growth-tracker-dm-underperform


---

## [2026-06-09] ingest | Ingest (credit-macro): Global In the Flow First Quarter Recap: What a Year This Quarter Has Been

Operation ID: op_e7ecf7a8fea1
Status: completed
Created: sources/ms-2020-04-01-in-the-flow-q1-recap


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategist: Trading with Stocks – Duration and Curves

Operation ID: op_0cb3597e9aae
Status: completed
Created: sources/ms-2017-01-28-rates-strategist-duration-and-curves


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategist: Don't Miss the Bull Market

Operation ID: op_6647a5943536
Status: completed
Created: sources/ms-2019-02-09-dont-miss-the-bull-market


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategist: The Bullish 'Bond Cyclone'

Operation ID: op_c73132e97100
Status: completed
Created: sources/ms-2019-03-15-bullish-bond-cyclone


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategist: Toward More Tightening

Operation ID: op_5c4741048a08
Status: completed
Created: sources/ms-2018-03-16-toward-more-tightening


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategy: Introducing BMI(2) and xBMI, Improving BMI(10) and iBMI

Operation ID: op_207f40d5dfd0
Status: completed
Created: sources/ms-2017-06-15-bmi2-xbmi-models


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Interest Rate Strategy: XCCY Basis Primer

Operation ID: op_0e01ecc9062b
Status: completed
Created: sources/ms-2016-03-22-xccy-basis-primer


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Macro Briefing: 1937-38 Redux?

Operation ID: op_50240ee54e18
Status: completed
Created: sources/ms-2016-06-15-1937-38-redux


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Macro Commentary | April 2

Operation ID: op_7a8d4e823ae3
Status: completed
Created: sources/ms-2020-04-03-global-macro-commentary-covid


---

## [2026-06-09] ingest | Ingest (credit-macro): Global Macro Strategist | The End of Trends

Operation ID: op_971e640f8729
Status: completed
Created: sources/ms-2022-11-04-end-of-trends


---

## [2026-06-09] ingest | Ingest (credit-macro): Government Bond Auction Pipeline | The Month Ahead

Operation ID: op_b473f076114a
Status: completed
Created: sources/ms-2019-02-15-govt-bond-auction-pipeline


---

## [2026-06-09] ingest | Ingest (credit-macro): Cross-Asset Strategy: Global In the Flow — Highlights from January

Operation ID: op_3ed0002d58b8
Status: completed
Created: sources/ms-2019-02-01-cross-asset-january-recap


---

## [2026-06-09] ingest | Ingest (credit-macro): Insight into the Balance Sheet

Operation ID: op_a106311f8416
Status: completed
Created: sources/ms-2019-01-11-balance-sheet-normalization


---

## [2026-06-09] ingest | Ingest (credit-macro): 4Q18 US Credit Fundamental Review

Operation ID: op_ce15d65d54a9
Status: completed
Created: sources/ms-2019-03-15-4q18-credit-fundamentals


---

## [2026-06-09] ingest | Ingest (credit-macro): Long-Dated Vol Lines Up

Operation ID: op_cd5c6b007877
Status: completed
Created: sources/ms-2019-04-05-long-dated-equity-vol


---

## [2026-06-09] ingest | Ingest (credit-macro): MODs: Machine Learning on Drivers

Operation ID: op_43b3448a64f7
Status: completed
Created: sources/ms-2017-10-13-machine-learning-loan-mod-redefaults


---

## [2026-06-09] ingest | Ingest (credit-macro): MREL – Raising the Subordination Stakes

Operation ID: op_572ddb1057e7
Status: completed
Created: sources/ms-2019-04-18-mrel-subordination-brrd2


---

## [2026-06-09] ingest | Ingest (credit-macro): US Interest Rate Strategist: Top 10 Surprises for 2014

Operation ID: op_3ed3e9c5ec8b
Status: completed
Created: sources/ms-2013-12-13-top-10-rates-surprises-2014


---

## [2026-06-09] ingest | Ingest (credit-macro): UK Interest Rate Strategist: Gilt Futures: The Return of the Option

Operation ID: op_9a4a9488cabc
Status: completed
Created: sources/ms-2008-08-28-gilt-futures-ctd-option


---

## [2026-06-09] ingest | Ingest (credit-macro): Momentum for Diversification

Operation ID: op_a3d1dcff6f12
Status: completed
Created: sources/ms-2016-09-27-momentum-for-diversification


---

## [2026-06-09] ingest | Ingest (credit-macro): US Interest Rate Strategist: Stay Close to Home

Operation ID: op_cefd641e1a9d
Status: completed
Created: sources/ms-2009-11-12-us-rate-strategist


---

## [2026-06-09] ingest | Ingest (credit-macro): Morgan Stanley FX Positioning Tracker

Operation ID: op_8fd7d4d4318f
Status: completed
Created: sources/ms-2019-02-11-fx-positioning-tracker


---

## [2026-06-09] ingest | Ingest (credit-macro): One Size Doesn't Fit All

Operation ID: op_9d0ac324d82e
Status: completed
Created: sources/ms-2019-02-13-ecb-periphery-one-size


---

## [2026-06-09] ingest | Ingest (credit-macro): Our Bond Market Indicators: A Powerful Systematic Approach

Operation ID: op_5519d02e8a6c
Status: completed
Created: sources/ms-2015-03-06-bond-market-indicators


---

## [2026-06-09] ingest | Ingest (credit-macro): Thoughts on the Market: Can $2 Trillion Flatten the Unemployment Curve?

Operation ID: op_8090aa74c370
Status: completed
Created: sources/ms-2020-03-27-fiscal-package-unemployment


---

## [2026-06-09] ingest | Ingest (credit-macro): Credit Strategy: Corporate Hybrid Primer - 2014 Edition

Operation ID: op_6f0d02ce3ff7
Status: completed
Created: sources/ms-2014-02-21-corporate-hybrid-primer


---

## [2026-06-09] ingest | Ingest (credit-macro): Sovereign Subjects: Europe in the Balance

Operation ID: op_7c35d3a753b9
Status: completed
Created: sources/ms-2011-11-29-europe-in-the-balance


---

## [2026-06-09] ingest | Ingest (credit-macro): Sunday Start | What's Next in Global Macro: A Full-Court Policy Press

Operation ID: op_e4593b743eae
Status: completed
Created: sources/ms-2020-03-29-full-court-policy-press


---

## [2026-06-09] ingest | Ingest (credit-macro): 2019 US Credit Outlook: The Bear Has Begun

Operation ID: op_33a868fd6015
Status: completed
Created: sources/ms-2018-11-25-the-bear-has-begun


---

## [2026-06-09] ingest | Ingest (credit-macro): Treasury Market Commentary, January 25

Operation ID: op_b2f32a9d14ad
Status: completed
Created: sources/ms-2019-01-25-treasury-market-commentary


---

## [2026-06-09] ingest | Ingest (credit-macro): US Corporate Credit Strategy Brief: Selling the Rally

Operation ID: op_656854f2baa7
Status: completed
Created: sources/ms-2019-02-28-selling-the-rally


---

## [2026-06-09] ingest | Ingest (credit-macro): US Corporate Credit Strategy Chartbook

Operation ID: op_7806d4e32a0f
Status: completed
Created: sources/ms-2019-02-01-credit-strategy-chartbook


---

## [2026-06-09] ingest | Ingest (credit-macro): US Corporate Credit Strategy: MS Credit-BMI Updated Reading

Operation ID: op_922fa7be662f
Status: completed
Created: sources/ms-2018-04-16-credit-bmi-update


---

## [2026-06-09] ingest | Ingest (credit-macro): US Economics: Deeper Drop, Slower Climb

Operation ID: op_a5626beb6e4f
Status: completed
Created: sources/ms-2020-04-03-deeper-drop-slower-climb


---

## [2026-06-09] ingest | Ingest (credit-macro): US Interest Rate Strategy: Who Is Going to Buy Treasuries?

Operation ID: op_7fa805404524
Status: completed
Created: sources/ms-2018-02-27-who-buys-treasuries


---

## [2026-06-09] ingest | Ingest (credit-macro): US Interest Rate Strategist: What Also Comes Before Recessions? Rate Cuts

Operation ID: op_e47a18d12743
Status: completed
Created: sources/ms-2019-03-25-rate-cuts-before-recessions


---

## [2026-06-09] ingest | Ingest (credit-macro): European Equity Strategy: Global growth momentum starts to recover: what is priced in?

Operation ID: op_0b4859a1191a
Status: completed
Created: sources/db-2019-03-15-european-equity-strategy-growth-momentum


---

## [2026-06-09] ingest | Analysis: credit-universe representation + topology

Operation ID: op_cf6a7d2ce927
Status: completed
Created: analyses/credit-universe-topology-and-representation


---

## [2026-06-09] ingest | Ingest (credit-macro): How and Why to Use Experimental Data to Evaluate Methods for Observational Causal Inference

Operation ID: op_117a674dc12f
Status: completed
Created: sources/gentzel-2021-osrct-evaluation


---

## [2026-06-09] ingest | Ingest (credit-macro): Bayesian Nonparametric Modeling for Causal Inference

Operation ID: op_02ab320de22d
Status: completed
Created: sources/hill-2011-bart-causal-inference


---

## [2026-06-09] ingest | Ingest (credit-macro): Methodology and reporting characteristics of studies using interrupted time series design in healthcare

Operation ID: op_9f6ea86432f6
Status: completed
Created: sources/hudson-2019-its-healthcare-reporting


---

## [2026-06-09] ingest | Ingest (credit-macro): Testing Conditional Independence in Causal Inference for Time Series Data

Operation ID: op_68215fbeeed9
Status: completed
Created: sources/cai-2023-testing-conditional-independence-time-series


---

## [2026-06-09] ingest | Analysis: testing unconfoundedness vs g-methods identifiability

Operation ID: op_b20381baef1d
Status: completed
Created: analyses/testing-unconfoundedness-vs-g-methods-identifiability
