---
created: '2026-04-09T17:05:46.767273Z'
page_type: index
title: Wiki Index
updated: '2026-04-25T23:00:00Z'
---

# ML Research Wiki

*Topics: transformers, conformal prediction, uncertainty quantification, fixed income, corporate bonds, factor investing, momentum, actuarial science, mortality modelling, market microstructure, limit order books, stylized facts, creditETF, LBO risk, credit curves*

Master catalog of all pages in this wiki.

## Sources
*Summary pages for ingested source documents.*

### Transformers
- [[sources/attention-paper|Attention Is All You Need]] — Transformer architecture paper by Vaswani et al.

### Conformal Prediction & Causal Inference
- [[sources/koukorinis-2026-draci|Doubly Robust Adaptive Conformal Inference (2026)]] — DR-ACI for treatment effects under temporal dependence
- [[sources/zaffran-phd|Zaffran PhD Thesis (2024)]] — Post-hoc predictive uncertainty quantification for electricity forecasting
- [[sources/zaffran-2022-aci|Adaptive Conformal Predictions for Time Series (2022)]] — ACI and AgACI methods
- [[sources/zaffran-2023-conformal-missing|Conformal Prediction with Missing Values (2023)]] — CP-MDA framework for mask-conditional validity
- [[sources/farinhas-2024-non-exchangeable-crc|Non-Exchangeable Conformal Risk Control (2024)]] — CRC extension for distribution drift
- [[sources/johnstone-2025-multioutput|Multi-Output Conformal Regression (2025)]] — Exact and approximate methods for multivariate responses
- [[sources/bao-2025-review|Review of Conformal Regression Methods (2025)]] — Comprehensive survey and benchmark
- [[sources/adams-2025-functional|Functional Data Anomaly Detection (2025)]] — Conformal methods with elastic distances
- [[sources/angelopoulos-2022-gentle-intro|A Gentle Introduction to Conformal Prediction (2022)]] — Angelopoulos & Bates, canonical practitioner tutorial; APS/RAPS, CQR, CRC, weighted CP, Learn Then Test
- [[sources/xu-2023-enbpi|Conformal prediction for time series / EnbPI (2023)]] — Xu & Xie, bootstrap-ensemble CP without exchangeability; asymptotic conditional coverage under β-mixing
- [[sources/stocker-2025-conformal-timeseries-intro|A Gentle Introduction to Conformal Time Series Forecasting (2025)]] — Stocker et al., four-family taxonomy (WCP / EnbPI / ACI / BCP)
- [[sources/dieuleveut-zaffran-2025-cp-tutorial|Conformal Prediction: A Tutorial (Hi! PARIS 2025)]] — Dieuleveut & Zaffran, 91-slide UAI/ICML tutorial deck
- [[sources/vovk-2005-algorithmic-learning|Algorithmic Learning in a Random World (2005)]] — Vovk, Gammerman, Shafer; foundational CP monograph (Springer; 2nd ed. 2022)
- [[sources/shafer-2007-cp-tutorial|A Tutorial on Conformal Prediction (2007)]] — Shafer & Vovk, 58-page foundational tutorial (arXiv 0706.3188 / JMLR)
- [[sources/vovk-2012-cross-conformal|Cross-conformal predictors (2012)]] — Vovk, primary source for cross-conformal prediction (arXiv 1208.0806)
- [[sources/fontana-2023-cp-unified-review|Conformal prediction: A unified review (2023, Bernoulli)]] — Fontana, Zeni, Vantini; theory-focused review of post-2005 developments
- [[sources/zhou-2025-cp-data-perspective|Conformal Prediction: A Data Perspective (2025, ACM CSUR)]] — Zhou, Chen, Gui, Cheng; data-modality-organised survey (NLP, vision, graphs, LLMs)
- [[sources/tibshirani-2019-covariate-shift|Conformal Prediction Under Covariate Shift (2019, NeurIPS)]] — Tibshirani, Barber, Candès, Ramdas; primary source for weighted CP
- [[sources/barber-2021-jackknife-plus|Predictive Inference with the Jackknife+ (2021, AoS)]] — Barber-Candès-Ramdas-Tibshirani; 1−2α distribution-free LOO coverage
- [[sources/barber-2023-beyond-exchangeability|Conformal Prediction Beyond Exchangeability (2023, AoS)]] — Barber-Candès-Ramdas-Tibshirani; NexCP with fixed weights and TV-bounded coverage gap
- [[sources/lei-2018-distribution-free-regression|Distribution-Free Predictive Inference for Regression (2018, JASA)]] — Lei-G'Sell-Rinaldo-Tibshirani-Wasserman; pre-Angelopoulos canonical CP-regression
- [[sources/angelopoulos-2023-conformal-pid|Conformal PID Control for Time Series Prediction (2023, NeurIPS)]] — Angelopoulos-Candès-Tibshirani; PID controller for online CP
- [[sources/romano-2019-cqr|Conformalized Quantile Regression (2019, NeurIPS)]] — Romano-Patterson-Candès; primary source for CQR
- [[sources/romano-2020-aps|Classification with Valid and Adaptive Coverage / APS (2020, NeurIPS)]] — Romano-Sesia-Candès; primary source for APS
- [[sources/angelopoulos-2021-raps|Uncertainty Sets for Image Classifiers / RAPS (2021, ICLR)]] — Angelopoulos-Bates-Malik-Jordan; primary source for RAPS
- [[sources/bates-2021-rcps|Distribution-Free Risk-Controlling Prediction Sets / RCPS (2021, JACM)]] — Bates-Angelopoulos-Lei-Malik-Jordan; primary source for RCPS and CRC
- [[sources/angelopoulos-2021-learn-then-test|Learn Then Test (2021)]] — Angelopoulos-Bates-Candès-Jordan-Lei; risk control via FWER over discretised λ-grid
- [[sources/gibbs-2021-aci|Adaptive Conformal Inference Under Distribution Shift (2021, NeurIPS)]] — Gibbs-Candès; the original ACI paper
- [[sources/gibbs-2024-online-aci|Conformal Inference for Online Prediction with Arbitrary Distribution Shifts (2024, JMLR)]] — Gibbs-Candès; DtACI with dynamic-regret bounds
- [[sources/gibbs-2023-conditional-guarantees|Conformal Prediction with Conditional Guarantees (2023)]] — Gibbs-Cherian-Candès; PAC-style conditional coverage via shift-class
- [[sources/kim-2020-jackknife-plus-after-bootstrap|Predictive Inference Is Free with J+aB (2020, NeurIPS)]] — Kim-Xu-Barber; J+aB ensemble construction (precursor to EnbPI)
- [[sources/nguyen-2026-gammerman-festschrift|The Importance of Being Learnable (Gammerman Festschrift, 2026)]] — Nguyen & Luo eds.; Springer LNCS 16290, 478 pp
- [[sources/lemaire-2024-aaltd-workshop|Advanced Analytics and Learning on Temporal Data / AALTD 2024]] — Lemaire et al. eds.; ECML PKDD workshop proceedings
- [[sources/tibshirani-2023-cp-lecture-notes|Conformal Prediction (Tibshirani CMU lecture notes, Spring 2023)]] — Graduate statistician-style introduction; two "key ideas", Beta calibration-conditional coverage, Lei-Wasserman impossibility, local adaptivity

### Fixed Income & Credit
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (2024)]] — Credit spread curve construction and bond valuation

### Credit ETF & Credit Risk (creditETF)
- [[sources/spec-2012-single-name-fundamental|Single Name Fundamental Analysis Spec (2012)]] — European credit analysis framework
- [[sources/pullirsch-2006-credit-spread-risk|Measuring Credit-Spread Risk (2006)]] — Zero-coupon credit-spread curve estimation
- [[sources/trinh-2006-lever-framework|Introducing LEVER (2006)]] — LBO/recap risk scoring framework
- [[sources/lehman-2007-qcr-quarterly|QCR Quarterly 2007-Q1]] — Base correlation mapping and event risk trading
- [[sources/ubs-2012-next-gen-credit-curves|Next-Generation Credit Curves (2012)]] — Unified hazard-rate methodology
- [[sources/dickerson-2023-bond-risk|Corporate Bond Risk Factor Pricing (2023)]] — Factor models for corporate bond returns
- [[sources/sehatpour-2024-green-bonds|Anatomy of Municipal Green Bond Yield Spreads (2024)]] — Green bond pricing and greenium analysis
- [[sources/technical-2025-bond-similarity|Bond Similarity Framework (2025)]] — ML-based bond similarity measures
- [[sources/he-2024-functional-regression|Multi-Factor Function-on-Function Regression (2024)]] — Bond yields on commodity futures
- [[sources/huang-2025-global-credit-spread-puzzle|Global Credit Spread Puzzle (2025)]] — CSP across 8 developed economies, Japan exception
- [[sources/dickerson-2024-bond-pitfalls|Common Pitfalls in Corporate Bond Research (2024)]] — MMN and look-ahead bias identification
- [[sources/feng-2025-predicting-bond-returns|Predicting Corporate Bond Returns with ML (2025)]] — RF outperforms traditional models
- [[sources/houweling-2017-factor-investing|Factor Investing in Corporate Bonds (2017)]] — Size, Low-Risk, Value, Momentum factors
- [[sources/haesen-2017-momentum-spillover|Momentum Spillover from Stocks to Bonds (2017)]] — Residual spillover strategy
- [[sources/fedenia-2021-ml-trade-classifier|ML-Based Trade Classification (2021)]] — RF classifier for TRACE data
- [[sources/krishnan-2007-credit-spread-forecast|Credit Spread Forecasting (2007)]] — OLS, Logit, Neural network comparison
- [[sources/saha-2024-muni-bond-ml|Municipal Bond Valuation with ML (2024)]] — BlackRock CatBoost approach
- [[sources/de-moura-2016-pairs-trading|Pairs Trading for Corporate Bonds (2016)]] — Kalman filter cointegration
- [[sources/rehman-2024-green-bonds|Green Bonds and Oil Shocks (2024)]] — Wavelet coherence analysis

### Theses - Fixed Income & ML
- [[sources/antonian-2024-graph-signal-processing|Graph Signal Processing for Fixed Income (2024)]] — NatWest MSc thesis, GSP bonds
- [[sources/nunes-2022-ml-fixed-income|ML for Fixed Income Allocation (2022)]] — LSTM, RL, regime switching thesis

### Actuarial Science & Mortality
- [[sources/tsai-2020-hierarchical-mortality|Hierarchical Credibility Theory for Multi-Country Mortality (2020)]] — Credibility approach to mortality modelling
- [[sources/huynh-2021-mogp-longevity|Multi-output Gaussian Processes for Multi-population Longevity (2021)]] — MOGP framework for mortality
- [[sources/namora-2021-hierarchical|Hierarchical Credibility Model (2021)]] — Insurance premium calculation

### ETF Flows & Trade Decomposition
- [[sources/optiver-2025-corporate-bond-etf-contraflow|Corporate Bond ETF Contraflow Strategy (2025)]] — Systematic strategy exploiting passive flow distortions
- [[sources/petit-2025-data-driven-flow-etf|Data-Driven Trade Flow Decomposition for ETFs (2025)]] — ML clustering of ETF-constituent trade flows
- [[sources/chao-2019-etf-flows-prices|Why Do ETF Flows Move Prices (2019)]] — Deutsche Bank flow decomposition research

### Market Microstructure & Limit Order Books
- [[sources/abergel-2017-algorithmic-trading-lob|Algorithmic Trading in a Microstructural Limit Order Book Model (2017)]] — LOB model from Limit Order Books (Abergel et al.)
- [[sources/golub-2014-multiscale-liquidity|Multi-Scale Representation of High Frequency Market Liquidity (2014)]] — Intrinsic time and directional change analysis
- [[sources/lu-2018-market-making|Papers in Market Microstructure and Liquidity (2018)]] — Market making and microstructure collection
- [[sources/xu-2020-mlofi|Multi-Level Order-Flow Imbalance (2020)]] — MLOFI extends OFI to multiple price levels
- [[sources/ellersgaard-2018-hedge-tracking-lob|Optimal Hedge Tracking in LOB (2018)]] — Delta hedging with limit/market orders via HJB QVI
- [[sources/wang-2018-cross-responses|Cross-Responses Between Stocks (2018)]] — Microscopic price impact decomposition
- [[sources/brigida-2019-trade-intensity-liquidity|Trade Intensity and Liquidity (2019)]] — HFT liquidity provision in natural gas futures
- [[sources/gueant-2019-particle-filtering-bonds|Mid-Price Estimation via Particle Filtering (2019)]] — SMC for corporate bond mid-prices
- [[sources/fermanian-2017-md2c-corporate-bonds|MD2C Platforms for Corporate Bonds (2017)]] — RFQ modeling on electronic platforms

### Stylized Facts & Long Memory
- [[sources/guillaume-1997-stylized-facts-fx|Stylized Facts in FX Markets (1997)]] — Foundational O&A paper on empirical properties
- [[sources/gould-2016-long-memory-fx|Long Memory of Order Flow in FX (2016)]] — H≈0.7 confirmed in single-day FX data
- [[sources/koukorinis-stylized-facts|Revisiting Stylised Facts (2022)]] — Information clocks, MFDFA, kernel tests
- [[sources/stavroyiannis-2017-bitcoin-multifractal|Bitcoin Multifractal Properties (2017)]] — WTMM and MFDFA on high-frequency Bitcoin
- [[sources/ruan-2016-mfdcca-gold|MF-DCCA Gold-Oil Analysis (2016)]] — Cross-correlation multifractal analysis
- [[sources/zachos-2018-change-point-detection|Change Point Detection (2018)]] — Dissertation on online CPD methods
- [[sources/aslam-2020-covid-mfdfa|COVID-19 Impact on European Stock Market Multifractality (2020)]] — MFDFA during pandemic outbreak
- [[sources/murphy-2006-order-flow-critique|Transaction Clock Critique (2006)]] — Monte Carlo analysis of Ané & Geman method

### Statistical Methods
- [[sources/laumann-2021-kernel-tests-nonstationary|Kernel Tests for Nonstationary Processes (2021)]] — MMD and HSIC for dependent data

## Entities
*People, organizations, places.*

### Researchers - Transformers & ML
- [[entities/ashish-vaswani|Ashish Vaswani]] — First author of the Transformer paper
- [[entities/margaux-zaffran|Margaux Zaffran]] — PhD on conformal prediction for electricity forecasting
- [[entities/vladimir-vovk|Vladimir Vovk]] — Founder of conformal prediction
- [[entities/emmanuel-candes|Emmanuel Candès]] — Contributed Adaptive Conformal Inference
- [[entities/yaniv-romano|Yaniv Romano]] — Conformalized Quantile Regression, Technion

### Researchers - Conformal Prediction & Statistics
- [[entities/andreas-koukorinis|Andreas Koukorinis]] — DR-ACI for causal inference under dependence, UCL
- [[entities/antonio-farinhas|António Farinhas]] — Non-exchangeable conformal risk control, Instituto de Telecomunicações
- [[entities/andre-martins|André F.T. Martins]] — NLP, uncertainty quantification, Instituto Superior Técnico
- [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]] — Learning theory, EPFL/École Polytechnique
- [[entities/julie-josse|Julie Josse]] — Missing data, Inria PreMeDICaL
- [[entities/anastasios-angelopoulos|Anastasios N. Angelopoulos]] — Practitioner-facing CP, APS/RAPS, EECS UC Berkeley
- [[entities/stephen-bates|Stephen Bates]] — Conformal risk control, Learn Then Test, MIT
- [[entities/m-stocker|M. Stocker]] — CP for time series, Karlsruhe Institute of Technology
- [[entities/wiktoria-malgorzewicz|Wiktoria Małgorzewicz]] — CP time-series, Royal Holloway University of London
- [[entities/matteo-fontana|Matteo Fontana]] — Functional CP, Royal Holloway University of London
- [[entities/souhaib-ben-taieb|Souhaib Ben Taieb]] — Probabilistic forecasting, MBZUAI / U. of Mons
- [[entities/alexander-gammerman|Alexander Gammerman]] — Co-inventor of CP, head of Computer Learning Research Centre, Royal Holloway
- [[entities/glenn-shafer|Glenn Shafer]] — Co-inventor of CP; coined "conformal predictor"; game-theoretic probability, Rutgers
- [[entities/gianluca-zeni|Gianluca Zeni]] — CP theory, MOX Politecnico di Milano
- [[entities/simone-vantini|Simone Vantini]] — Functional CP, MOX Politecnico di Milano
- [[entities/xiaofan-zhou|Xiaofan Zhou]] — Data-centric CP survey, UIC
- [[entities/baiting-chen|Baiting Chen]] — CP for modern data modalities, UCLA
- [[entities/yu-gui|Yu Gui]] — Conformal alignment for LLMs, University of Chicago
- [[entities/lu-cheng|Lu Cheng]] — Responsible-AI CP, UIC
- [[entities/ryan-tibshirani|Ryan J. Tibshirani]] — Modern CP theory (weighted, jackknife+, beyond-exchangeability, PID), UC Berkeley/CMU. Distinct from Robert Tibshirani (lasso, Stanford)
- [[entities/rina-foygel-barber|Rina Foygel Barber]] — Jackknife+, NexCP, J+aB, University of Chicago
- [[entities/aaditya-ramdas|Aaditya Ramdas]] — Sequential testing, anytime-valid inference, non-exchangeable CP, CMU
- [[entities/jing-lei|Jing Lei]] — CP-regression foundations, CMU. Distinct from Lihua Lei (Stanford GSB)
- [[entities/max-gsell|Max G'Sell]] — JASA 2018 CP-regression co-author, CMU
- [[entities/alessandro-rinaldo|Alessandro Rinaldo]] — High-dimensional inference, CP-regression theory, UT Austin
- [[entities/larry-wasserman|Larry Wasserman]] — Distribution-free inference, conditional-coverage impossibility, CMU
- [[entities/evan-patterson|Evan Patterson]] — CQR co-author, Topos Institute / Stanford
- [[entities/matteo-sesia|Matteo Sesia]] — APS, FDR control, knockoffs, USC Marshall
- [[entities/jitendra-malik|Jitendra Malik]] — RAPS / RCPS co-author; computer vision, UC Berkeley
- [[entities/michael-i-jordan|Michael I. Jordan]] — Senior on Berkeley CP-risk-control line, UC Berkeley
- [[entities/lihua-lei|Lihua Lei]] — RCPS / LTT co-author, Stanford GSB. Distinct from Jing Lei (CMU)
- [[entities/isaac-gibbs|Isaac Gibbs]] — Originator of ACI / DtACI / conditional guarantees, Stanford
- [[entities/byol-kim|Byol Kim]] — J+aB lead author, University of Washington
- [[entities/john-cherian|John J. Cherian]] — Conformal conditional guarantees, Stanford

### Researchers - Fixed Income & Quantitative Finance
- [[entities/richard-martin|Richard J. Martin]] — Credit spreads, Imperial College London
- [[entities/gareth-peters|Gareth W. Peters]] — Statistics, actuarial science, UC Santa Barbara
- [[entities/christina-nikitopoulos|Christina S. Nikitopoulos]] — Green bonds, sustainable finance, UTS
- [[entities/patrick-houweling|Patrick Houweling]] — Factor investing, corporate bonds, Robeco
- [[entities/jeroen-van-zundert|Jeroen van Zundert]] — Momentum strategies, Robeco
- [[entities/alexander-dickerson|Alexander Dickerson]] — Bond market microstructure, UNSW

### Researchers - Market Microstructure
- [[entities/olivier-gueant|Olivier Gueant]] — Market making theory, optimal execution, Paris 1
- [[entities/martin-gould|Martin D. Gould]] — LOB dynamics, long memory, Imperial College/Oxford

### Researchers - Actuarial Science
- [[entities/cary-tsai|Cary Chi-Liang Tsai]] — Credibility theory, mortality modelling, Simon Fraser
- [[entities/mike-ludkovski|Mike Ludkovski]] — Gaussian processes, actuarial science, UC Santa Barbara

### Researchers - Credit Risk (creditETF)
- [[entities/rainer-pullirsch|Rainer Pullirsch]] — Credit-spread curve estimation, Bank Austria Creditanstalt
- [[entities/minh-trinh|Minh Trinh]] — LEVER framework co-author, Lehman Brothers
- [[entities/bodha-bhattacharya|Bodha Bhattacharya]] — LEVER framework co-author, Lehman Brothers
- [[entities/lindsey-matthews|Lindsey Matthews]] — Head of Client Development, UBS Delta
- [[entities/luca-bosatta|Luca Bosatta]] — Head of Risk Modelling, UBS Delta

### Institutions (creditETF)
- [[entities/lehman-brothers|Lehman Brothers]] — Investment bank (historical), LEVER and QCR research
- [[entities/ubs-delta|UBS Delta]] — Portfolio analytics system, D-Curves methodology

## Concepts
*Ideas, themes, topics.*

### Transformers & Attention
- [[concepts/self-attention|Self-Attention]] — Mechanism for computing relationships between sequence positions
- [[concepts/transformers|Transformers]] — Neural network architecture based on self-attention

### Conformal Prediction
- [[concepts/conformal-prediction|Conformal Prediction]] — Framework for distribution-free prediction sets with coverage guarantees
- [[concepts/split-conformal-prediction|Split Conformal Prediction]] — Computationally efficient variant using data splitting
- [[concepts/full-conformal-prediction|Full Conformal Prediction]] — Transductive variant; refits per candidate label
- [[concepts/cross-conformal-prediction|Cross-Conformal / Jackknife+ / CV+]] — Computational compromises between split and full CP
- [[concepts/jackknife-plus-after-bootstrap|Jackknife+ after Bootstrap (J+aB)]] — LOO via bootstrap ensemble, basis for EnbPI
- [[concepts/enbpi|EnbPI (Ensemble batch Prediction Intervals)]] — CP for time series via bootstrap-LOO; non-exchangeable
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]] — Extension for time series and distribution shift
- [[concepts/agaci|AgACI (Aggregated ACI)]] — Parameter-free ACI via online expert aggregation
- [[concepts/conformal-pid-control|Conformal PID Control]] — PID controller for online α-adaptation
- [[concepts/weighted-conformal-prediction|Weighted Conformal Prediction]] — CP under covariate shift via likelihood reweighting
- [[concepts/block-conformal-prediction|Block Conformal Prediction (BCP)]] — Block-level CP for β-mixing time series
- [[concepts/conformal-risk-control|Conformal Risk Control]] — Control expected value of arbitrary monotone loss functions
- [[concepts/learn-then-test|Learn Then Test]] — Distribution-free control of non-monotone risks via FWER
- [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]] — Adaptive prediction intervals with coverage guarantees
- [[concepts/adaptive-prediction-sets|Adaptive Prediction Sets (APS)]] — Classification score that adapts set size to input difficulty
- [[concepts/regularized-adaptive-prediction-sets|Regularized APS (RAPS)]] — APS with low-rank-class penalty for large-class problems
- [[concepts/conformal-outlier-detection|Conformal Outlier Detection]] — Distribution-free type-1 error control
- [[concepts/conformal-predictive-distribution|Conformal Predictive Distribution]] — Full predictive CDF from conformal p-values
- [[concepts/group-balanced-conformal-prediction|Group-Balanced CP]] — Coverage conditional on observed group feature
- [[concepts/class-conditional-conformal-prediction|Class-Conditional CP]] — Per-class coverage for imbalanced classification
- [[concepts/marginal-coverage|Marginal Coverage]] — Coverage averaged over the joint randomness
- [[concepts/conditional-coverage|Conditional Coverage]] — Coverage pointwise in covariates (distribution-free impossible)
- [[concepts/nonconformity-score|Nonconformity Score]] — Function `s(x,y)` measuring deviation from calibration sample
- [[concepts/mask-conditional-validity|Mask-Conditional Validity]] — Coverage conditional on missing value patterns
- [[concepts/distribution-drift|Distribution Drift]] — Covariate, label, and concept drift in non-stationary data
- [[concepts/non-exchangeable-conformal-prediction|Non-Exchangeable Conformal Prediction (NexCP)]] — Fixed-weight CP with TV-bounded coverage gap (Barber et al. 2023)
- [[concepts/online-conformal-prediction|Online Conformal Prediction]] — Umbrella for ACI / AgACI / DtACI / PID / EnbPI / NexCP families
- [[concepts/risk-controlling-prediction-sets|Risk-Controlling Prediction Sets (RCPS)]] — PAC-style (α, δ) high-probability risk control via UCB calibration
- [[concepts/dtaci|DtACI (Dynamically-tuned ACI)]] — Parameter-free ACI via dynamic-regret expert aggregation (Gibbs-Candès 2024)
- [[concepts/missing-data-imputation|Missing Data Imputation]] — Methods for handling missing values in conformal prediction
- [[concepts/jackknife-plus|Jackknife+ Prediction]] — Barber-Candès-Ramdas-Tibshirani LOO variant with 1−2α coverage
- [[concepts/mondrian-conformal-prediction|Mondrian Conformal Prediction]] — Taxonomy-conditional CP (parent of group/class-conditional variants)
- [[concepts/venn-predictors|Venn Predictors]] — Multi-probability distribution-free probabilistic predictors
- [[concepts/on-line-compression-models|On-Line Compression Models (OCM)]] — Vovk's generalisation beyond exchangeability
- [[concepts/cp-for-nlp|CP for NLP]] — Conformal prediction for text classification, QA, NLU
- [[concepts/cp-for-vision|CP for Computer Vision]] — RAPS at ImageNet scale, segmentation, image-to-image
- [[concepts/cp-for-graphs|CP for Graph Data]] — Inductive/transductive, NAPS, conformalized link prediction
- [[concepts/cp-for-llms|CP for Large Language Models]] — Conformal RAG, factuality filtering, conformal alignment

### Causal Inference & Dependence
- [[concepts/causal-inference|Causal Inference]] — Treatment effect estimation from observational data
- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]] — Consistent if either propensity or outcome model correct
- [[concepts/temporal-cross-fitting|Temporal Cross-Fitting]] — Block cross-fitting with guard bands for time series
- [[concepts/beta-mixing|Beta-Mixing]] — Temporal dependence decay measure for time series

### Statistical Foundations
- [[concepts/coverage-guarantee|Coverage Guarantee]] — Statistical validity property of prediction intervals
- [[concepts/exchangeability|Exchangeability]] — Key assumption for conformal prediction
- [[concepts/prediction-intervals|Prediction Intervals]] — Ranges containing future observations with specified probability
- [[concepts/uncertainty-quantification|Uncertainty Quantification]] — Science of quantifying prediction confidence
- [[concepts/calibration|Calibration]] — Agreement between predicted and observed frequencies

### Fixed Income & Credit
- [[concepts/credit-spread-curve|Credit Spread Curve]] — Term structure of credit spreads
- [[concepts/z-spread|Z-Spread]] — Zero-volatility spread over risk-free curve
- [[concepts/carry-rolldown|Carry and Rolldown]] — Bond return components from curve dynamics
- [[concepts/survival-probability|Survival Probability]] — Default-free probability over time
- [[concepts/bond-capm|Bond CAPM]] — Factor models for corporate bond returns
- [[concepts/factor-models|Factor Models]] — Systematic risk decomposition
- [[concepts/liquidity-risk|Liquidity Risk]] — Trading cost and market depth risk
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]] — Parsimonious yield curve fitting
- [[concepts/green-bond-spreads|Green Bond Spreads]] — Greenium and sustainable bond pricing
- [[concepts/yield-to-maturity|Yield to Maturity]] — Internal rate of return for bonds
- [[concepts/credit-spread-puzzle|Credit Spread Puzzle]] — Why structural models underpredict IG spreads
- [[concepts/factor-investing|Factor Investing]] — Systematic factor strategies for bonds

### Credit ETF & Credit Risk (creditETF)
- [[concepts/lever-score|LEVER Score]] — LBO/recap risk scoring framework (Lehman 2006)
- [[concepts/hazard-rate-curve|Hazard Rate Curve]] — Unified credit curve methodology
- [[concepts/base-correlation|Base Correlation]] — CDO tranche pricing framework
- [[concepts/cds-bond-basis|CDS-Bond Basis]] — Cross-instrument spread differences
- [[concepts/lbo-risk|LBO Risk]] — Leveraged buyout event risk for bondholders
- [[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage]] — Credit relative value metric

### Bond Trading & Momentum
- [[concepts/bond-momentum|Bond Momentum]] — Persistence of bond returns
- [[concepts/spillover-effect|Momentum Spillover]] — Equity momentum predicts bond returns
- [[concepts/residual-momentum|Residual Momentum]] — Idiosyncratic return momentum
- [[concepts/trade-classification|Trade Classification]] — Identifying buyer/seller initiated trades
- [[concepts/trace-data|TRACE Data]] — FINRA corporate bond transaction data
- [[concepts/market-microstructure-noise|Market Microstructure Noise]] — Bid-ask bounce and data quality
- [[concepts/look-ahead-bias|Look-ahead Bias]] — Using future information in backtests

### ETF Flows & Passive Investing
- [[concepts/etf-flows|ETF Flows]] — Change in ETF ownership, negatively predicts returns
- [[concepts/flow-decomposition|Flow Decomposition]] — Separating allocation, index, and weight reconstitution flows
- [[concepts/index-reconstitution|Index Reconstitution]] — Additions/deletions from indices creating predictable flows

### Market Microstructure
- [[concepts/limit-order-book|Limit Order Book]] — Order matching mechanism for electronic markets
- [[concepts/market-making|Market Making]] — Liquidity provision via bid-ask quotes
- [[concepts/long-memory|Long Memory]] — Slowly decaying autocorrelations (H > 0.5)
- [[concepts/mfdfa|MFDFA]] — Multifractal detrended fluctuation analysis

### Actuarial Science & Mortality
- [[concepts/lee-carter-model|Lee-Carter Model]] — Foundational stochastic mortality model
- [[concepts/hierarchical-credibility-model|Hierarchical Credibility Model]] — Multi-level optimal blending
- [[concepts/longevity-risk|Longevity Risk]] — Risk of people living longer than expected
- [[concepts/credibility-theory|Credibility Theory]] — Optimal blending of individual and group experience
- [[concepts/buhlmann-straub-model|Bühlmann-Straub Model]] — Credibility with unequal exposures
- [[concepts/multi-population-mortality|Multi-Population Mortality]] — Joint modelling across populations

### Machine Learning & Statistics
- [[concepts/gaussian-processes|Gaussian Processes]] — Non-parametric Bayesian regression
- [[concepts/kriging|Kriging]] — Spatial interpolation (GP equivalent)
- [[concepts/random-forest-proximity|Random Forest Proximity]] — Tree-based similarity measure
- [[concepts/association-rule-learning|Association Rule Learning]] — Pattern discovery in data
- [[concepts/gegenbauer-processes|Gegenbauer Processes]] — Cyclical long-memory processes
- [[concepts/tukey-gh-transformation|Tukey g-and-h Transformation]] — Flexible skewed heavy-tailed distributions

### Time Series & State Space
- [[concepts/functional-data-analysis|Functional Data Analysis]] — Treating curves as observations
- [[concepts/schwartz-smith-model|Schwartz-Smith Model]] — Two-factor commodity pricing
- [[concepts/state-space-models|State-Space Models]] — Latent variable dynamic systems
- [[concepts/kalman-filter|Kalman Filter]] — Optimal linear recursive estimation

## Analyses
*Comparisons, syntheses, query answers.*

- [[analyses/conformal-prediction-for-hft-traders|Conformal Prediction for Algorithmic and HFT Traders]] — Practitioner guide. CP vs QR, σ̂-scaled scores, three trading use cases, tree-model combinations, simulation recipes
- *(See also analyses [161] AI Engineering as a Discipline, [162] CP × Tukey g-h, [163] ETF Contraflow in MIND_MAP.md — not all analyses are listed in this curated index.)*

## Contradictions
*Disagreements between sources.*

(No contradictions yet)

---

**Stats**
- Total sources: 142 (wiki/wiki/sources/)
- Total entities: 245 (wiki/wiki/entities/)
- Total concepts: 388 (wiki/wiki/concepts/)
- Total analyses: 4 (wiki/wiki/analyses/)
- Total pages: ~779
- Last updated: 2026-05-24 (CP primary-source backbone: 14 arXiv papers including the Tibshirani-group quartet + Romano-Candès classification line + Berkeley risk-control trilogy + Gibbs-Candès online-CP trilogy + Kim-Xu-Barber J+aB; plus Gammerman Festschrift and AALTD 2024 workshop)

*Note: This index lists curated highlights, not every page in the wiki. For exhaustive listings, see `find wiki/wiki/<type>/ -name "*.md"` or the MIND_MAP graph.*
