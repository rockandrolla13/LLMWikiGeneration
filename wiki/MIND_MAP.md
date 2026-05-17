# ML Research Wiki - Mind Map

*A grep-friendly knowledge graph. Each `[N]` is a line-anchored marker. Run `grep "^\[N\]"` to fetch a single node, or `grep "\[N\]"` to find all cross-references to it.*

---

## Routing Hubs (Nodes 1–11)

[1] **Overview** — Top-level routing across eleven themes. This wiki interleaves quantitative finance research (fixed income, credit ETFs, market microstructure, ETF flows, stylized facts, actuarial science) with machine-learning methodology (conformal prediction, causal inference, statistical methods, transformers) and a large applied AI engineering branch (LLMs, RAG, knowledge graphs, prompt engineering, LLM security, ML systems, software architecture). Major hubs: AI Engineering [2], Conformal Prediction & Uncertainty Quantification [3], Causal Inference & Treatment Effects [4], Fixed Income & Corporate Bonds [5], Credit ETF & Credit Risk [6], Market Microstructure & Optimal Execution [7], ETF Flows & Trade Decomposition [8], Stylized Facts & Long Memory [9], Actuarial Science & Mortality [10], Statistical Methods & ML Foundations [11]. Coverage as of 2026-05-17: 105 sources, 165 entities, 287 concepts. The AI Engineering branch [2] is the single largest cluster (18 books, added May 2026); fixed-income clusters [5] and [6] are the deepest legacy clusters combined.

[2] **AI Engineering** — Eighteen books (2020–2025) covering the practitioner stack for building applications on top of foundation models. Anchor sources: Huyen's AI Engineering [56] and Designing ML Systems [55], Raschka's Build LLM from Scratch [87], Alammar & Grootendorst's Hands-On LLMs [14]. Sub-clusters: (a) **LLM internals** — Raschka [87], Alammar [14]; (b) **RAG** — Mendelevitch [69], Bratanic & Hane GraphRAG [30], Anon Vector Databases [15]; (c) **Knowledge graphs** — Barrasa & Webber [20], Bratanic [30]; (d) **Prompt engineering** — Berryman & Ziegler [28], Boonstra [29]; (e) **LLM applications** — Caelen [32], Oshin & Campos LangChain [80]; (f) **AI-assisted programming** — Taulli [97]; (g) **LLM security** — Wilson OWASP [106]; (h) **Software architecture & SWE** — Percival & Gregory [82], Nelson [75], Hermans [52]; (i) **AI strategy / business** — Thomas/Zikopoulos/Soule [99]. Cross-cutting concepts: **RAG** [150] appears in 10 of these books, **prompt engineering** [151] in 6, **chain-of-thought** in 6, **prompt injection** in 4. Most-cited entities: **OpenAI** [144] (9 books), **LangChain** [145] (7), **Hugging Face** [146] (3), **Anthropic** (3), **GitHub Copilot** [147] (3). The branch shares its conceptual root — transformers [149] — with the original Vaswani et al. attention paper [18] in hub [11].

[3] **Conformal Prediction & Uncertainty Quantification** — Distribution-free prediction-set methodology from Vovk's original framework through Candès's adaptive extensions, Romano's CQR, Zaffran's electricity-forecasting PhD, and recent extreme-value, multi-output and time-series work. Anchor sources: Zaffran PhD [113], Zaffran ACI [111], Zaffran CP-with-missing-values [112], Bao review [19], Adams functional anomaly [13], Farinhas non-exchangeable CRC [41], Chernozhukov distributional CP [35], Johnstone multi-output [58], Misiakos DAG-TFRC [70], Pasche extreme CP [81], Xu SPCI [108], Sun copula CPTS [96], Yang multi-distribution robust [109], Lee KOWCPI [64]. Connects to causal inference [4] via Koukorinis DR-ACI [59]. Core concepts: conformal prediction [148], conformalized quantile regression, adaptive conformal inference (ACI) [158], conformal risk control (CRC), mask-conditional validity, coverage guarantee, exchangeability. Researchers: Vovk [129], Candès, Romano, Zaffran [130], Farinhas, Martins, Dieuleveut, Josse.

[4] **Causal Inference & Treatment Effects** — Treatment-effect estimation under temporal dependence and distribution drift, bridging conformal prediction [3] with double machine learning. Anchor source: Koukorinis DR-ACI 2026 [59] — doubly robust adaptive conformal inference with temporal cross-fitting and block bootstrap. Concepts: doubly robust estimation [159], temporal cross-fitting, beta-mixing, double machine learning. Author Andreas Koukorinis [131] (UCL) extends Candès's ACI [158] to causal estimands under dependence. Flexible least squares [71] supplies time-varying parameter machinery; statistical methodology in [11].

[5] **Fixed Income & Corporate Bonds** — Credit-spread term structure, factor models for bond returns, momentum strategies, ML-based valuation and prediction. Anchor sources: Martin credit curve [68], Houweling factor investing [53], Haesen momentum spillover [49], Dickerson bond risk [37], Dickerson pitfalls [38], Huang global credit-spread puzzle [54], Feng ML bond returns [43], Saha BlackRock muni-ML [90], Sehatpour green bonds [91], Rehman green/oil [88], He functional regression [51], Krishnan spread forecast [61], De Moura pairs trading [36], Antonian graph-signal-processing thesis [16], Nunes ML fixed income thesis [77], Kumar liquidity-adjusted AFNS [62], Omrane yield-curve forecasting [78], Technical bond-similarity [98]. Concepts: credit spread curve [156], Z-spread, carry-rolldown, bond CAPM, factor investing [157], factor models, bond momentum, residual momentum, credit spread puzzle, Nelson-Siegel model, green bond spreads, look-ahead bias, TRACE data, market microstructure noise. Key entities: Martin [133], Houweling [134], van Zundert, Dickerson [135], Nikitopoulos.

[6] **Credit ETF & Credit Risk** — The Lehman / UBS Delta methodology lineage: hazard-rate credit curves, base correlation for CDO tranches, CDS-bond basis, LBO scoring, pricing of correlated credit. Anchor sources: Pullirsch credit-spread risk [86], Trinh LEVER framework [101], Lehman QCR Quarterly [65], UBS next-gen credit curves [104], Spec single-name fundamental [94], Fermanian MD2C corporate bonds [44], Gueant particle filtering bond mid-prices [47], Fedenia ML trade classification [42], Shi CDS options comovement [92]. Concepts: hazard rate curve, base correlation, CDS-bond basis, LEVER score, LBO risk, spread per turn of leverage, survival probability. Institutional entities: Lehman Brothers [141], UBS Delta [142]; researchers Pullirsch, Trinh, Bhattacharya, Matthews, Bosatta.

[7] **Market Microstructure & Optimal Execution** — Limit-order-book models, market making, optimal execution, FX dealer/RFQ markets, high-frequency liquidity. Anchor sources: Cartea optimal execution [33], Abergel algorithmic-trading LOB [12], Lu market making collection [66], Xu MLOFI [107], Wang cross-responses [105], Ellersgaard hedge tracking LOB [40], Bergault multi-asset MM [26], Bergault RFQ pricing [27], Barzykin algorithmic FX [21], Barzykin dealer tiers [22], Barzykin multi-currency [23], Barzykin precious metals [24], Barzykin adverse selection [25], Lokin fill probabilities [66_a — see [55_a]], Brigida trade-intensity gas futures [31], Golub multiscale liquidity [45], Gueant particle filtering [47], Fermanian MD2C [44]. Concepts: limit order book [161 → 155], market making [154], optimal execution, Avellaneda-Stoikov model, inventory risk, adverse selection, fill probability, RFQ markets, client tiering, MLOFI, cross-responses. Researchers: Cartea, Gueant [137], Jaimungal, Bergault, Barzykin, Gould [138].

[8] **ETF Flows & Trade Decomposition** — How passive flows distort prices and how constituent trade flows can be decomposed. Anchor sources: Optiver corporate-bond ETF contraflow [79], Petit data-driven flow decomposition [85], Chao Deutsche Bank ETF flows research [34]. Concepts: ETF flows, flow decomposition, index reconstitution, trade classification.

[9] **Stylized Facts & Long Memory** — Empirical regularities of FX, equity and crypto returns at high frequency; multifractal and long-memory analysis. Anchor sources: Guillaume O&A stylized facts FX [48], Gould long memory FX [46], Koukorinis stylised facts thesis [60], Stavroyiannis Bitcoin multifractal [95], Ruan MF-DCCA gold-oil [89], Zachos change-point-detection thesis [110], Aslam COVID MFDFA [17], Murphy transaction-clock critique [73]. Concepts: long memory, MFDFA, Hurst exponent, change-point detection, kernel tests for nonstationary processes.

[10] **Actuarial Science & Mortality** — Stochastic mortality, credibility theory, multi-population longevity with Gaussian processes. Anchor sources: Tsai hierarchical credibility multi-country mortality [103], Huynh MOGP longevity [57], Namora hierarchical credibility [74]. Concepts: Lee-Carter model, credibility theory, Bühlmann-Straub model, hierarchical credibility model, longevity risk, multi-population mortality. Researchers Tsai, Ludkovski, Peters.

[11] **Statistical Methods & ML Foundations** — Gaussian processes, kernel hypothesis testing, change-point detection, state-space models, graph signal processing, copulas, extreme-value theory, transformers (architecture). Anchor sources: Vaswani attention paper [18], Laumann kernel tests [63], Montana flexible least squares [71], Triantafyllopoulos mean-reverting spreads [100], Tsagaris robust adaptive portfolio [102], Nobrega Kalman ML stat-arb [76], Zhang pairs general SSM [115], Peters quantile diffusions [84], Peters asynchronous CIR [83], Dong GSP for ML [39], Shi graph Laplacian learning [93], Yu graph-learning financial [110_a], Zhi GPs on graphs [116], Moura Kalman pairs [72], He HF pairs Chinese futures [50], Sun copula CPTS [96]. Concepts: Gaussian processes, kriging, Kalman filter, unscented Kalman filter, state-space models, graph Laplacian, graph signal processing, spectral graph filters, copulas, probability integral transform, extreme value theory, generalized Pareto distribution, Tukey g-and-h transformation, Gegenbauer processes, mean reversion, statistical arbitrage, structural vector autoregression.

---

## Sources (Nodes 12–116)

### Market Microstructure & LOB sources

[12] **Algorithmic Trading in a Microstructural LOB Model** — Abergel et al. (2017). LOB-model framework for algorithmic execution. Hub [7]. Concepts: limit order book, optimal execution.

### Conformal Prediction sources

[13] **Functional Data Anomaly Detection** — Adams (2025). Conformal anomaly detection for functional data using elastic distances. Hub [3]. Concepts: conformal prediction [148], functional data analysis.

### AI Engineering sources

[14] **Hands-On Large Language Models** — Alammar & Grootendorst (2024, O'Reilly, ~408 pp). Visually-driven practitioner guide; representation-vs-generation as the organising mental model; full RAG pipeline from chunking to grounded generation; modern three-stage training stack (pretraining, SFT, RLHF/DPO) with QLoRA. Hub [2]. Concepts: transformers [149], self-attention, tokenization, dense retrieval, RAG [150], reranking, prompt engineering [151], in-context learning, chain-of-thought, contrastive learning, PEFT, RLHF, multimodal embeddings. Entities: Jay Alammar [143], Maarten Grootendorst, Cohere, Hugging Face [146], Ashish Vaswani [125].

[15] **Utilizing Vector Databases to Enhance RAG Models** — John Anderson (2024, self-published, ~40 pp). Short conceptual survey of vector databases plus RAG for text generation, search and chatbots; no algorithm or vendor names. Hub [2]. Concepts: RAG [150], vector databases, semantic embeddings, vector indexing, similarity search, semantic search, conversational AI, high-dimensional data, multimodal retrieval.

### Fixed Income & ML thesis sources

[16] **Graph Signal Processing for Fixed Income** — Antonian (2024). NatWest MSc thesis using GSP on bond graphs. Hub [5] / [11]. Concepts: graph signal processing, graph Laplacian, spectral graph filters.

### Stylized Facts sources

[17] **COVID-19 Impact on European Stock Market Multifractality** — Aslam et al. (2020). MFDFA on European indices during the pandemic outbreak. Hub [9]. Concepts: MFDFA, long memory, Hurst exponent.

### Transformers (foundational)

[18] **Attention Is All You Need** — Vaswani et al. (2017). The Transformer architecture: stacked multi-head self-attention plus position-wise feed-forward layers. The conceptual root of the AI Engineering branch [2]. Cited from [14], [28], [30], [32], [87], [106]. Hub [11]. Concepts: transformers [149], self-attention, multi-head attention, positional embeddings. Entity: Ashish Vaswani [125].

### Conformal Prediction (continued)

[19] **Review of Conformal Regression Methods** — Bao (2025). Comprehensive benchmark and survey of conformal regression. Hub [3]. Concepts: conformal prediction [148], conformalized quantile regression, split conformal prediction, coverage guarantee.

### Knowledge Graph sources

[20] **Building Knowledge Graphs** — Barrasa & Webber (2023, O'Reilly, ~290 pp). Neo4j-grounded practitioner guide; property-graph model, Cypher, the four-level "organising principles" ladder (graphs → labelled property graphs → taxonomies → ontologies); seven use-case archetypes (integration/search, metadata, identity, pattern detection, dependency, semantic search, conversational); "knowledge lake" as architectural pattern; annotated ontology grounding LLM answers. Hub [2]. Concepts: knowledge graph [152], property graph model, Cypher, RDF, ontology, taxonomy, entity resolution, graph data science, graph-native ML, knowledge lake. Entities: Jesus Barrasa, Jim Webber, Neo4j [148_a → 148].

### Market Microstructure (Barzykin / Bergault / Cartea)

[21] **Algorithmic FX Market Making** — Barzykin et al. (2020). Internalization-externalization decisions for FX dealers under inventory risk. Hub [7]. Concepts: market making [154], internalization-externalization, inventory risk.

[22] **FX Dealer Tiers** — Barzykin et al. (2021). Optimal client tiering and spread differentiation in FX. Hub [7]. Concepts: client tiering, market making [154], adverse selection.

[23] **Multi-Currency Inventory Management** — Barzykin et al. (2022). Cross-currency hedging and inventory in FX market making. Hub [7]. Concepts: inventory risk, market making [154].

[24] **Precious Metals Market Making** — Barzykin et al. (2024). Spot precious-metal dealer optimization. Hub [7]. Concepts: market making [154], inventory risk, fill probability.

[25] **Adverse Selection in FX Market Making** — Barzykin et al. (2025). Quote skewing under informed flow. Hub [7]. Concepts: adverse selection, market making [154].

[26] **Multi-Asset Market Making** — Bergault et al. (2019). Optimal-control extension of Avellaneda-Stoikov to multi-asset inventory. Hub [7]. Concepts: market making [154], inventory risk, optimal execution.

[27] **RFQ Pricing for Corporate Bonds** — Bergault et al. (2023). Stochastic-control pricing in request-for-quote markets. Hub [7]. Concepts: RFQ markets, market making [154], client tiering.

### AI Engineering (continued — Prompt Engineering / RAG / Apps)

[28] **Prompt Engineering for LLMs** — Berryman & Ziegler (2025, O'Reilly, ~270 pp). Two ex-GitHub-Copilot engineers; treats prompts as engineered documents ("Little Red Riding Hood" principle — make the prompt look like the training-data documents the model has already seen); concrete feedforward pipeline (retrieve → snippetize → score → pack → assemble within token budget); reverse-engineers the OpenAI tool-calling wire format (ChatML, TypeScript-style function signatures); offline/online evaluation with LLM-as-judge and acceptance-rate telemetry. Hub [2]. Concepts: prompt engineering [151], few-shot prompting, chain-of-thought, RAG [150], ReAct, tool use, RLHF, LLM evaluation, LLM-as-judge, prompt assembly, context window, transformers [149]. Entities: John Berryman, Albert Ziegler, GitHub Copilot [147], OpenAI [144].

[29] **Prompt Engineering** — Boonstra (2024, Google whitepaper, ~68 pp). Google's Vertex-AI-flavoured prompting guide; canonical ladder zero-shot → few-shot → system / contextual / role → step-back, chain-of-thought, self-consistency, tree-of-thoughts → ReAct for tool-using agents; concrete temperature / top-K / top-P recipes (0.2/0.95/30 for balanced output; 0 for math and CoT); standardised prompt-documentation table. Hub [2]. Concepts: prompt engineering [151], zero-shot, few-shot, chain-of-thought, self-consistency, tree-of-thoughts, ReAct prompting, step-back prompting, role prompting, system prompting, automatic prompt engineering, LLM sampling controls. Entities: Lee Boonstra, Google, Gemini, Vertex AI, LangChain [145].

[30] **Essential GraphRAG** — Bratanic & Hane (2025, Manning, ~180 pp). From-scratch GraphRAG in Neo4j without LangChain or LlamaIndex orchestration; step-back prompting and parent-document retrieval to fix recall and context-loss failures; text-to-Cypher with schema-in-prompt vs fine-tuned specialist; agentic RAG with retriever tools, router and answer critic; reproduction of Microsoft GraphRAG over The Odyssey with hierarchical community detection plus global/local search; LLM-based knowledge-graph construction from CUAD legal contracts via OpenAI Structured Outputs. Hub [2]. Concepts: RAG [150], GraphRAG, knowledge-graph construction, vector similarity search, hybrid search, text-to-Cypher, agentic RAG, community detection, parent document retrieval, step-back prompting, entity resolution, RAG evaluation. Entities: Tomaz Bratanic, Oskar Hane, Neo4j, Microsoft GraphRAG, OpenAI [144].

[31] **Trade Intensity and Liquidity** — Brigida (2019). HFT liquidity provision in natural gas futures. Hub [7]. Concepts: limit order book, market making [154].

[32] **Developing Apps with GPT-4 and ChatGPT** — Caelen & Blete (2023, O'Reilly, ~180 pp). End-to-end developer playbook on the OpenAI API; four worked example apps (news generator, YouTube summarizer, Zelda-domain expert with Redis-backed retrieval, voice assistant with Whisper + Gradio); LangChain walkthrough wiring embeddings, FAISS, RetrievalQA, ConversationChain memory and agents/tools into one retrieval-augmented chatbot; explicit on prompt injection inevitability, API key management, moderation endpoint. Hub [2]. Concepts: OpenAI API, ChatGPT, GPT-4, large language models, tokenization, prompt engineering [151], few-shot learning, chain-of-thought, fine-tuning, function calling, embeddings, RAG [150], vector database, LangChain, GPT plug-ins, RLHF, prompt injection, AI hallucination, transformers [149]. Entities: Olivier Caelen, Marie-Alice Blete, OpenAI [144], LangChain [145], FAISS.

[33] **Optimal Execution** — Cartea, Jaimungal & Penalva (2015). Stochastic-control framework for execution; the canonical reference for hub [7]. Concepts: optimal execution, market making [154], limit order book, Avellaneda-Stoikov model.

[34] **Why Do ETF Flows Move Prices** — Chao et al. (2019, Deutsche Bank). Decomposes ETF flows into informed vs liquidity components. Hub [8]. Concepts: ETF flows, flow decomposition.

[35] **Distributional Conformal Prediction** — Chernozhukov, Wuthrich & Zhu (2021). Conformal intervals via the probability integral transform; distribution-free intervals for arbitrary functionals. Hub [3]. Concepts: distributional conformal prediction, probability integral transform, conformal prediction [148].

### Fixed Income (continued)

[36] **Pairs Trading for Corporate Bonds** — De Moura (2016). Kalman-filter cointegration for corporate-bond pairs. Hub [5]. Concepts: cointegration, Kalman filter, pairs trading, statistical arbitrage.

[37] **Corporate Bond Risk Factor Pricing** — Dickerson (2023). Factor model for corporate-bond returns. Hub [5]. Concepts: bond CAPM, factor models, factor investing [157].

[38] **Common Pitfalls in Corporate Bond Research** — Dickerson (2024). Identifies MMN and look-ahead bias in widely cited bond papers. Hub [5]. Concepts: market microstructure noise, look-ahead bias, TRACE data.

[39] **Graph Signal Processing for ML** — Dong et al. (2020). Foundations of graph signal processing for machine learning. Hub [11]. Concepts: graph signal processing, graph Laplacian, graph Fourier transform, spectral graph filters.

[40] **Optimal Hedge Tracking in LOB** — Ellersgaard (2018). Delta-hedging via mixed limit/market orders solved as an HJB quasi-variational inequality. Hub [7]. Concepts: limit order book, optimal execution, market making [154].

[41] **Non-Exchangeable Conformal Risk Control** — Farinhas, Zerva, Ulmer & Martins (2024). CRC under distribution drift and non-exchangeability. Hub [3]. Concepts: conformal risk control, distribution drift, conformal prediction [148]. Entities: António Farinhas [132], André Martins.

[42] **ML-Based Trade Classification** — Fedenia et al. (2021). Random-forest classifier for TRACE buyer/seller initiation. Hub [6] / [5]. Concepts: trade classification, TRACE data.

[43] **Predicting Corporate Bond Returns with ML** — Feng et al. (2025). Random forest outperforms traditional bond return models. Hub [5]. Concepts: bond momentum, factor investing [157].

[44] **MD2C Platforms for Corporate Bonds** — Fermanian, Gueant & Pu (2017). Multi-dealer-to-client RFQ modelling on electronic corporate-bond platforms. Hub [7] / [6]. Concepts: RFQ markets, market making [154].

[45] **Multi-Scale Representation of HF Market Liquidity** — Golub et al. (2014). Intrinsic-time and directional-change analysis. Hub [7]. Concepts: limit order book, optimal execution.

[46] **Long Memory of Order Flow in FX** — Gould et al. (2016). H≈0.7 long-range dependence in single-day FX order flow. Hub [9]. Concepts: long memory, Hurst exponent, MFDFA. Entity: Martin Gould [138].

[47] **Mid-Price Estimation via Particle Filtering** — Gueant et al. (2019). SMC for corporate-bond mid-prices from RFQ data. Hub [7] / [6]. Concepts: market making [154], RFQ markets, state-space models, Kalman filter. Entity: Olivier Gueant [137].

[48] **Stylized Facts in FX Markets** — Guillaume et al. (1997). Foundational Olsen & Associates paper on empirical FX properties. Hub [9]. Concepts: long memory, Hurst exponent.

[49] **Momentum Spillover from Stocks to Bonds** — Haesen, Houweling & van Zundert (2017). Residual equity-momentum strategy applied to bonds. Hub [5]. Concepts: bond momentum, residual momentum, spillover effect. Entity: Patrick Houweling [134].

[50] **High-Frequency Pairs Trading in Chinese Futures** — He et al. (2023). Cointegration-based HF pairs trading. Hub [11] / [7]. Concepts: pairs trading, cointegration, statistical arbitrage.

[51] **Multi-Factor Function-on-Function Regression** — He et al. (2024). Bond yields regressed on commodity futures curves. Hub [5]. Concepts: functional data analysis, factor models.

### Software Engineering / Code Reading

[52] **Code Reading in Practice** — Hermans (2024, O'Reilly Early Release, ~250 pp). Five-dimension framework — structure, domain, code quality, context, collaboration — for the neglected skill of code reading; cognitive-science grounded (working memory holds 2–6 items so chunking and mental-model construction must be deliberate); structural code smells (Fowler) paired with linguistic code smells (Arnaoudova) turn reading sessions into refactoring conversations; Hedy compiler as running example. Hub [2]. Concepts: code reading, working memory in programming, chunking, mental model of code, code smells, linguistic anti-patterns, program slicing, ubiquitous language, name molds, entry point analysis, eye-tracking in code reading. Entities: Felienne Hermans [143_b], Martin Fowler, Venera Arnaoudova.

### Fixed Income (continued)

[53] **Factor Investing in Corporate Bonds** — Houweling & van Zundert (2017). Size, low-risk, value, momentum factors for corporate bonds. Hub [5]. Concepts: factor investing [157], factor models, bond momentum. Entity: Patrick Houweling [134].

[54] **Global Credit Spread Puzzle** — Huang et al. (2025). Credit-spread puzzle across eight developed economies; Japan as exception. Hub [5]. Concepts: credit spread puzzle, credit spread curve [156].

### AI Engineering (Huyen anchor)

[55] **Designing Machine Learning Systems** — Huyen (2022, O'Reilly, ~386 pp). End-to-end ML lifecycle textbook; case studies from Netflix, Stitch Fix, Booking.com, TikTok, Alibaba; unusually deep post-deployment treatment (data distribution shift detection, monitoring and observability, continual learning, test-in-production via shadow deployments / A/B / canaries / interleaving / bandits); responsible AI framework operationalised through model cards and slice-based evaluation; debunks myths like "one model per system", "static performance", "scale doesn't matter". Hub [2]. Concepts: ML system design, data engineering for ML, feature engineering, data leakage, class imbalance handling, batch-vs-online prediction, model compression, distribution drift, ML monitoring and observability, continual learning, test-in-production, feature store, responsible AI, calibration, look-ahead bias. Entity: Chip Huyen [139].

[56] **AI Engineering** — Huyen (2025, O'Reilly, ~530 pp). Companion to [55]; foundation models flip the workflow from train-then-deploy to adapt-then-deploy; adaptation hierarchy prompting → RAG → finetuning → custom pretraining with explicit escalation criteria; evaluation methodology fusing classical metrics with LLM-as-a-judge and comparative ranking; precise inference-perf vocabulary (TTFT, TPOT, throughput, goodput, MFU, MBU); agent memory taxonomy and four agent failure modes (invalid tool, invalid parameters, goal failure, reflection error); dataset engineering as first-class. Hub [2]. Concepts: foundation models, AI engineering, prompt engineering [151], in-context learning, RAG [150], AI agents, PEFT, RLHF, LLM-as-a-judge, inference optimization, dataset engineering, sampling strategies, transformers [149], self-attention. Entities: Chip Huyen [139], OpenAI, Anthropic, Google, Hugging Face, LangChain, LlamaIndex.

### Actuarial Science sources

[57] **Multi-Output GP for Multi-Population Longevity** — Huynh & Ludkovski (2021). MOGP framework for joint mortality across populations. Hub [10] / [11]. Concepts: Gaussian processes, multi-population mortality, longevity risk.

### Conformal Prediction (continued)

[58] **Multi-Output Conformal Regression** — Johnstone (2025). Exact and approximate methods for multivariate-response CP. Hub [3]. Concepts: conformal prediction [148], prediction intervals, coverage guarantee.

### Causal Inference

[59] **DR-ACI: Doubly Robust Adaptive Conformal Inference (2026)** — Andreas Koukorinis (2026). DR-ACI for treatment effects under temporal dependence; temporal cross-fitting with guard bands; block bootstrap for beta-mixing data. Hub [4]. Concepts: causal inference, doubly robust estimation [159], double machine learning, temporal cross-fitting, beta-mixing, adaptive conformal inference [158], conformal prediction [148]. Entity: Andreas Koukorinis [131].

### Stylized Facts (continued)

[60] **Revisiting Stylised Facts** — Koukorinis (2022). Information clocks, MFDFA and kernel tests applied to high-frequency stylized facts. Hub [9]. Concepts: long memory, MFDFA, Hurst exponent, kernel tests.

### Fixed Income (continued)

[61] **Credit Spread Forecasting** — Krishnan et al. (2007). OLS, Logit and neural-network comparison for spread forecasting. Hub [5]. Concepts: credit spread curve [156].

[62] **Liquidity-Adjusted AFNS** — Kumar (2022). Arbitrage-free Nelson-Siegel model with a liquidity factor. Hub [5]. Concepts: Nelson-Siegel model, yield to maturity.

### Statistical Methods (continued)

[63] **Kernel Tests for Nonstationary Processes** — Laumann (2021). MMD and HSIC adapted for dependent data. Hub [11]. Concepts: kernel tests, distribution drift, beta-mixing.

### Conformal Prediction (continued)

[64] **KOWCPI** — Lee (2024). Conformal prediction with kernel-based observation weighting. Hub [3]. Concepts: conformal prediction [148], kowcpi, distribution drift.

### Credit ETF sources

[65] **QCR Quarterly 2007-Q1** — Lehman Brothers (2007). Base-correlation mapping and event-risk trading. Hub [6]. Concepts: base correlation, CDS-bond basis, LBO risk. Entity: Lehman Brothers [141].

### Market Microstructure (continued)

[66] **Papers in Market Microstructure and Liquidity** — Lu (2018). Collection on market making and microstructure. Hub [7]. Concepts: market making [154], limit order book.

[67] **Fill Probabilities** — Lokin (2024). Estimation of fill probabilities for limit orders. Hub [7]. Concepts: fill probability, market making [154], limit order book.

### Fixed Income (continued)

[68] **The Credit Curve Spread I** — Martin (2024). Credit-spread-curve construction and bond valuation. Hub [5]. Concepts: credit spread curve [156], Z-spread, carry-rolldown, survival probability, yield to maturity. Entity: Richard Martin [133].

### AI Engineering (continued — RAG anchor)

[69] **Hands-On RAG for Production** — Mendelevitch & Bao (2025, O'Reilly Early Release, ~80 pp). Vectara-grounded; two-flow blueprint (ingest: extract / chunk / embed / store; query: retrieve / rerank / generate / guardrail); the POC-to-production gap as the central problem; defense-in-depth security across ingestion / vector store / generation; production KPI table (context precision/recall, hallucination rate, answer relevance, latency mean/median, uptime); explicit case for turnkey RAG platforms (TCO runs 3-5x initial estimates). Hub [2]. Concepts: RAG [150], vector database, embeddings, semantic search, hybrid search, reranking, chunking, LLM hallucination, agentic RAG, GraphRAG, prompt injection, RAG evaluation, multimodal RAG. Entities: Ofer Mendelevitch, Forrest Bao, Vectara.

### Conformal Prediction (continued)

[70] **DAG-TFRC** — Misiakos (2025). Conformal prediction for time series via directed acyclic graphs. Hub [3]. Concepts: conformal prediction [148], conditional validity.

### Statistical Methods (continued)

[71] **Flexible Least Squares** — Montana (2009). Time-varying coefficient regression for non-stationary relationships. Hub [11] / [4]. Concepts: flexible least squares, state-space models.

[72] **Kalman Pairs Trading** — Moura (2016). Kalman-filter cointegration for pairs trading. Hub [11] / [5]. Concepts: Kalman filter, pairs trading, cointegration.

### Stylized Facts (continued)

[73] **Transaction Clock Critique** — Murphy (2006). Monte Carlo critique of the Ané–Geman transaction-clock method. Hub [9]. Concepts: long memory.

### Actuarial (continued)

[74] **Hierarchical Credibility Model** — Namora (2021). Multi-level optimal blending for insurance premium calculation. Hub [10]. Concepts: credibility theory, Bühlmann-Straub model, hierarchical credibility model.

### SWE for Data Scientists

[75] **Software Engineering for Data Scientists** — Nelson (2024, O'Reilly Early Release, ~300 pp). Bridges notebook-style data-science work to maintainable production Python; five attributes of good code (simplicity, modularity, readability, efficiency, robustness); training-serving skew as concrete clash between DRY and ML deployment reality (resolved by serialised preprocessing pipelines); documentation as first-class engineering activity with explicit anti-patterns; experiment tracking (Weights & Biases, sacred, SageMaker Experiments) as structured ML-iteration record. Hub [2]. Concepts: dont-repeat-yourself, modular code design, technical debt, refactoring, software testing, PEP 8, code linting and formatting, docstrings, training-serving skew, error handling and logging, experiment tracking, naming conventions. Entities: Catherine Nelson, John Ousterhout, Weights and Biases.

### Statistical Methods (continued)

[76] **Kalman ML for Statistical Arbitrage** — Nobrega (2014). Kalman-filter cointegration for stat-arb. Hub [11]. Concepts: Kalman filter, statistical arbitrage, cointegration.

### Fixed Income (continued)

[77] **ML for Fixed Income Allocation** — Nunes (2022). MSc thesis: LSTM, RL and regime switching for fixed-income allocation. Hub [5]. Concepts: bond momentum, factor investing [157].

[78] **Yield Curve Forecasting** — Omrane (2017). Forecasting models for the yield curve. Hub [5]. Concepts: Nelson-Siegel model, yield to maturity.

### ETF Flows (continued)

[79] **Corporate Bond ETF Contraflow Strategy** — Optiver (2025). Systematic strategy exploiting passive-flow distortions. Hub [8]. Concepts: ETF flows, flow decomposition.

### AI Engineering (LangChain anchor)

[80] **Learning LangChain** — Oshin & Campos (2025, O'Reilly, ~380 pp). First-party O'Reilly treatment of LangChain (Nuno Campos is a core LangChain maintainer); single arc from one-shot chat → RAG over document loaders / text splitters / embeddings / vector store → conversational memory in LangGraph → cognitive architectures (router, parallelisation, orchestrator/worker, reflection) → ReAct agents → multi-agent supervisor/swarm topologies; production deployment on LangGraph Platform; tracing and evaluation with LangSmith (heuristic / human / LLM-as-a-judge evaluators). Hub [2]. Concepts: LangChain, LangGraph, LangSmith, RAG [150], embeddings, vector store, chain-of-thought, tool calling, ReAct agent, LLM memory, structured output, human-in-the-loop, LLM agent, LLM-as-a-judge. Entities: Mayo Oshin, Nuno Campos, LangChain [145], LangGraph framework, LangSmith platform, Harrison Chase.

### Conformal Prediction (continued)

[81] **Extreme Conformal Prediction** — Pasche & Engelke (2025). Conformal intervals in the tails via extreme-value theory. Hub [3]. Concepts: extreme value theory, generalized Pareto distribution, conformal prediction [148].

### Software Architecture

[82] **Architecture Patterns with Python** — Percival & Gregory (2020, O'Reilly, ~300 pp). Domain-Driven Design and Patterns of Enterprise Application Architecture ported to idiomatic Python (Flask + SQLAlchemy); twelve chapters each adding one pattern — Repository, Service Layer, Unit of Work, Aggregates, Domain Events, Message Bus, CQRS, hexagonal architecture; SQLAlchemy classical mapping so the ORM depends on the domain model rather than the other way round; evolves a Flask monolith into event-driven microservices; "high gear / low gear" testing strategy. Hub [2]. Concepts: domain-driven design, repository pattern, unit of work pattern, hexagonal architecture, dependency inversion principle, test-driven development, service layer pattern, aggregate pattern, domain events, message bus, command-query-responsibility-segregation, event-driven microservices. Entities: Harry Percival, Bob Gregory, Eric Evans, Martin Fowler, Flask, SQLAlchemy.

### Statistical Methods (Peters lineage)

[83] **Asynchronous CIR — Continuous-Time Foundation** — Peters (2026). Continuous-time CIR extension for asynchronous observations. Hub [11]. Concepts: state-space models, Ornstein-Uhlenbeck process.

[84] **Tukey g-h Quantile Diffusions** — Peters (2026). Flexible diffusion process for skewed heavy-tailed distributions; linked to conformal prediction. Hub [11]. Concepts: Tukey g-and-h transformation, quantile regression, conformal prediction [148].

### ETF Flows (continued)

[85] **Data-Driven Trade Flow Decomposition for ETFs** — Petit (2025). ML clustering of ETF-constituent trade flows. Hub [8]. Concepts: ETF flows, flow decomposition.

### Credit ETF (continued)

[86] **Measuring Credit-Spread Risk** — Pullirsch (2006, Bank Austria Creditanstalt). Zero-coupon credit-spread-curve estimation. Hub [6]. Concepts: credit spread curve [156], hazard rate curve. Entity: Rainer Pullirsch.

### AI Engineering (Raschka anchor)

[87] **Build a Large Language Model (From Scratch)** — Raschka (2024, Manning, ~370 pp). Code-first PyTorch reimplementation of GPT-2 with no Hugging Face dependency; three stages — architecture+data (BPE via tiktoken, token + positional embeddings, naive → causal → multi-head self-attention), pretraining with cross-entropy loss and loading public GPT-2 weights, two fine-tuning flavours (classification for spam, instruction for an assistant); from-scratch LoRA in Appendix E; everything laptop-runnable. Hub [2]. Concepts: byte-pair encoding, token embeddings, positional embeddings, self-attention, causal attention, multi-head attention, transformers [149], layer normalization, GELU activation, language-model pretraining, decoding strategies, instruction fine-tuning, classification fine-tuning, low-rank adaptation. Entities: Sebastian Raschka [140], OpenAI, Alec Radford, PyTorch, tiktoken, Lightning AI.

### Fixed Income (continued)

[88] **Green Bonds and Oil Shocks** — Rehman (2024). Wavelet coherence analysis of green-bond spreads vs oil shocks. Hub [5]. Concepts: green bond spreads.

### Stylized Facts (continued)

[89] **MF-DCCA Gold-Oil Analysis** — Ruan (2016). Cross-correlation multifractal analysis between gold and oil. Hub [9]. Concepts: MFDFA, long memory.

### Fixed Income (continued)

[90] **Municipal Bond Valuation with ML** — Saha (2024, BlackRock). CatBoost approach to muni valuation. Hub [5]. Concepts: green bond spreads, bond CAPM.

[91] **Anatomy of Municipal Green Bond Yield Spreads** — Sehatpour (2024). Greenium analysis for muni green bonds. Hub [5]. Concepts: green bond spreads.

### Credit ETF (continued)

[92] **CDS Options Comovement** — Shi (2022). Comovement structure of CDS-options portfolios. Hub [6]. Concepts: CDS-bond basis, base correlation.

### Statistical Methods (continued)

[93] **Graph Laplacian Learning** — Shi (2024). Learning graph structure via Laplacian estimation. Hub [11]. Concepts: graph Laplacian, graph signal processing.

### Credit ETF (continued)

[94] **Single Name Fundamental Analysis Spec** — anonymous (2012). European credit analysis framework. Hub [6]. Concepts: LEVER score, LBO risk, spread per turn of leverage.

### Stylized Facts (continued)

[95] **Bitcoin Multifractal Properties** — Stavroyiannis (2017). WTMM and MFDFA on high-frequency Bitcoin. Hub [9]. Concepts: MFDFA, long memory, Hurst exponent.

### Conformal Prediction (continued)

[96] **Copula CPTS** — Sun (2022). Copula-based conformal prediction for time series. Hub [3]. Concepts: copulas, conformal prediction [148], multi-step conformal prediction.

### AI Engineering (AI-Assisted Programming)

[97] **AI-Assisted Programming** — Taulli (2024, O'Reilly, ~250 pp). Survey + handbook of the AI coding tool landscape (Copilot, Cursor, ChatGPT, Gemini, Claude, CodeWhisperer, Tabnine, Replit, Cody, Warp, Bito, Code Llama, StableCode, AlphaCode, CodeT5, StarCoder); pairs modular programming with prompt engineering as the operating discipline (context windows are finite and hallucinations compound with scope, so decompose, prompt per piece, verify before composing); end-to-end SDLC coverage (planning, coding, debugging, testing, deployment) with concrete case studies (Shopify, Accenture, hardware programming). Hub [2]. Concepts: ai-assisted programming, prompt engineering [151], chain-of-thought, few-shot learning, hallucination, RAG [150], large language model, code completion. Entities: Tom Taulli, GitHub Copilot [147], Cursor, Tabnine, Replit, Amazon CodeWhisperer, Code Llama.

### Fixed Income (continued)

[98] **Bond Similarity Framework** — anonymous technical (2025). ML-based bond similarity measures. Hub [5]. Concepts: factor models, random forest proximity.

### AI Strategy

[99] **AI Value Creators** — Thomas, Zikopoulos & Soule (2025, O'Reilly / IBM, ~300 pp). Corporate-strategic playbook (no code, no ML implementation detail); three-tier consumption taxonomy (AI baked into software / AI by API call / platform-based AI Value Creator); "your AI needs an IA" thesis — a data fabric is prerequisite since average LLM contains roughly 1% of any enterprise's data; AI governance levers (fairness, robustness, explainability, lineage) as future moat once accuracy commoditises; multi-model future thesis ("one model will not rule them all"); "generative computing" proposal where neurons join bits and qubits as first-class compute elements managed by structured runtimes. Hub [2]. Concepts: AI value creator, foundation model, generative AI, agentic AI, RAG [150], PEFT, AI hallucination, AI governance, data fabric, prompt injection, generative computing, quantum-safe cryptography. Entities: Rob Thomas, Paul Zikopoulos, Kate Soule, IBM, InstructLab, Hugging Face, DeepSeek, LangChain, OpenAI, Anthropic.

### Statistical Methods (continued)

[100] **Mean-Reverting Spreads** — Triantafyllopoulos (2011). Bayesian state-space inference for mean-reverting spread processes. Hub [11]. Concepts: mean reversion, Ornstein-Uhlenbeck process, state-space models, pairs trading.

### Credit ETF (continued — LEVER framework)

[101] **Introducing LEVER** — Trinh et al. (2006, Lehman Brothers). LBO/recap risk-scoring framework. Hub [6]. Concepts: LEVER score, LBO risk, spread per turn of leverage. Entities: Minh Trinh, Bodha Bhattacharya, Lehman Brothers [141].

### Statistical Methods (continued)

[102] **Robust Adaptive Portfolio** — Tsagaris (2010). Robust adaptive portfolio allocation. Hub [11]. Concepts: state-space models.

### Actuarial (continued)

[103] **Hierarchical Credibility Theory for Multi-Country Mortality** — Tsai (2020). Credibility-theory approach to joint multi-country mortality. Hub [10]. Concepts: credibility theory, Bühlmann-Straub model, hierarchical credibility model, multi-population mortality, Lee-Carter model.

### Credit ETF (continued — UBS Delta)

[104] **Next-Generation Credit Curves** — UBS (2012). Unified hazard-rate methodology (UBS Delta D-Curves). Hub [6]. Concepts: hazard rate curve, credit spread curve [156], CDS-bond basis. Entities: UBS Delta [142], Lindsey Matthews, Luca Bosatta.

### Market Microstructure (continued)

[105] **Cross-Responses Between Stocks** — Wang (2018). Microscopic price-impact decomposition across instruments. Hub [7]. Concepts: limit order book.

### LLM Security

[106] **The Developer's Playbook for LLM Security** — Wilson (2024, O'Reilly Early Release, ~200 pp). Founder of the OWASP Top 10 for LLM Applications; reframes LLM security as a trust-boundary problem; reference architecture across user-interaction layer / training data (internal vs in-the-wild) / live external data feeds / connected internal services / the model itself; case study of Microsoft Tay; documents the sprint-based eight-week process that produced the OWASP LLM Top 10 as a template for community security standards. Hub [2]. Concepts: OWASP LLM Top 10, prompt injection, data poisoning, trust boundaries, LLM supply chain security, LLM jailbreaking, insecure output handling, LLM sensitive data disclosure, LLM hallucination security, transformer architecture, LLM application architecture, LLM threat modeling. Entities: Steve Wilson, OWASP, Microsoft Tay, Ashish Vaswani [125].

### Market Microstructure (continued)

[107] **Multi-Level Order-Flow Imbalance** — Xu (2020). MLOFI extends order-flow imbalance to multiple LOB price levels. Hub [7]. Concepts: limit order book, market making [154].

### Conformal Prediction (continued)

[108] **SPCI: Sequential Predictive Conformal Inference** — Xu (2022). Online CP for time series with sequential coverage. Hub [3]. Concepts: spci, adaptive conformal inference [158], conformal prediction [148].

[109] **Multi-Distribution Robust Conformal Prediction** — Yang (2026). CP under multiple distribution shifts. Hub [3]. Concepts: multi-distribution-robust-cp, conformal prediction [148], distribution drift, worst-case coverage.

### Statistical Methods (continued)

[110] **Change Point Detection** — Zachos (2018). Dissertation on online change-point-detection methods. Hub [9]. Concepts: long memory.

[111] **Adaptive Conformal Predictions for Time Series** — Zaffran et al. (2022). ACI and AgACI methods. Hub [3]. Concepts: adaptive conformal inference [158], conformal prediction [148]. Entity: Margaux Zaffran [130].

[112] **Conformal Prediction with Missing Values** — Zaffran et al. (2023). CP-MDA framework for mask-conditional validity. Hub [3]. Concepts: conformal prediction [148], mask-conditional validity, missing data imputation. Entities: Margaux Zaffran [130], Julie Josse.

[113] **Zaffran PhD Thesis** — Margaux Zaffran (2024). Post-hoc predictive uncertainty quantification for electricity forecasting; lineage thesis for ACI [111] and CP-MDA [112]. Hub [3]. Concepts: adaptive conformal inference [158], conformal prediction [148], distribution drift. Entity: Margaux Zaffran [130].

### Statistical Methods (continued)

[114] **Graph Learning for Financial Networks** — Yu (2024). Graph-structure learning applied to financial networks. Hub [11]. Concepts: graph signal processing, graph Laplacian.

[115] **Pairs Trading with General SSM** — Zhang (2021). General state-space model for pairs trading. Hub [11]. Concepts: state-space models, pairs trading, cointegration, mean reversion.

[116] **Gaussian Processes on Graphs** — Zhi (2024). GP regression over graph-valued inputs. Hub [11]. Concepts: Gaussian processes, kriging, graph signal processing.

---

## Entities (Nodes 117–147)

[117] **Andreas Koukorinis** — Author of DR-ACI [59] and stylised-facts thesis [60]; UCL. Cluster node for hub [4] and a contributor to hub [9]. See also [131].

[118] **Margaux Zaffran** — PhD on conformal prediction for electricity forecasting [113]; lead author of ACI [111] and CP-MDA [112]; Inria PreMeDICaL. Central conformal-prediction node in hub [3]. See also [130].

[119] **Vladimir Vovk** — Originator of conformal prediction [148]; cited across hub [3]. Royal Holloway, University of London. See also [129].

[120] **Emmanuel Candès** — Contributed adaptive conformal inference [158]; cited across hubs [3] and [4].

[121] **Yaniv Romano** — Originator of conformalized quantile regression; Technion. Cited from [19], [81].

[122] **António Farinhas** — Lead author of non-exchangeable conformal risk control [41]; Instituto de Telecomunicações. See also [132].

[123] **André F.T. Martins** — NLP and uncertainty quantification; co-author of [41]; Instituto Superior Técnico.

[124] **Aymeric Dieuleveut** — Learning theory; EPFL / École Polytechnique. Contributor to hub [3].

[125] **Ashish Vaswani** — First author of the Transformer paper [18]; cited from [14], [28], [30], [32], [87], [106]. The Transformer architecture undergirds everything in hub [2] and the transformers concept node [149].

[126] **Olivier Cartea** — Optimal execution and market making; author of [33] which anchors hub [7].

[127] **Sebastian Jaimungal** — Co-author of [33]; algorithmic trading.

[128] **Philippe Bergault** — Co-author of [26], [27]; multi-asset market making and RFQ pricing.

[129] **Vladimir Vovk** — see [119]. Listed twice intentionally — cluster head for [3].

[130] **Margaux Zaffran** — see [118]. Hub head for [3].

[131] **Andreas Koukorinis** — see [117]. Hub head for [4].

[132] **António Farinhas** — see [122].

[133] **Richard J. Martin** — Author of [68]; Imperial College London. Anchor entity for credit-curve methodology in hub [5].

[134] **Patrick Houweling** — Factor investing for corporate bonds; co-author of [49], [53]; Robeco. Anchor entity for factor investing [157] in hub [5].

[135] **Alexander Dickerson** — Author of [37], [38]; UNSW. Anchor entity for bond pitfalls and factor models in hub [5].

[136] **Christina Nikitopoulos** — Green bonds and sustainable finance; UTS. Contributor to hub [5].

[137] **Olivier Gueant** — Market making and optimal execution theory; co-author of [44], [47]; Paris 1. Anchor entity for hub [7].

[138] **Martin D. Gould** — LOB dynamics and long memory; co-author of [46]; Imperial / Oxford. Bridges hub [7] and hub [9].

[139] **Chip Huyen** — Author of Designing ML Systems [55] and AI Engineering [56]; Stanford CS 329S; Claypot AI. Central entity in hub [2].

[140] **Sebastian Raschka** — Author of Build LLM from Scratch [87]; Lightning AI. Co-anchor with [139] for hub [2].

[141] **Lehman Brothers** — Investment bank (historical); produced LEVER [101] and QCR [65]; lineage anchor for hub [6].

[142] **UBS Delta** — UBS's portfolio analytics system; produced the D-Curves methodology [104]; lineage anchor for hub [6].

[143] **Jay Alammar** — Co-author of [14]; visual-explanation style ("The Illustrated Transformer"). Major contributor to hub [2].

[144] **OpenAI** — Most-cited organisational entity in hub [2] (appears in 9 of 18 AI Engineering books). Produces GPT-4, ChatGPT, the OpenAI API; cited from [14], [28], [30], [32], [56], [80], [87], [99], [106].

[145] **LangChain** — Application framework cited in 7 AI Engineering books; primary book is Oshin & Campos [80]. Cited from [14], [29], [30], [32], [56], [69], [99].

[146] **Hugging Face** — Open-source model and dataset hub; cited from [14], [56], [99].

[147] **GitHub Copilot** — AI coding assistant; central case study in [28] and [97]; cited from [106].

---

## Concepts (Nodes 148–160)

[148] **Conformal Prediction** — Distribution-free prediction intervals with finite-sample coverage guarantees under exchangeability. Vovk-Shafer-Romano framework; the core methodology of hub [3]. Reviewed in [19]; built on by ACI [158] ([111], [113]), CRC [41], distributional CP [35], multi-output CP [58], extreme CP [81], SPCI [108], multi-distribution-robust CP [109], DAG-TFRC [70], KOWCPI [64], copula CPTS [96]. Bridges to causal inference via DR-ACI [59]; intersects extreme-value theory in [81] and quantile diffusions in [84]; tested for anomaly detection on functional data in [13]. Adjacent concepts: conformalized quantile regression, split conformal prediction, exchangeability, coverage guarantee, mask-conditional validity.

[149] **Transformers** — Vaswani et al. (2017) architecture [18]; substrate for everything in hub [2]. Encoder-only variants for representation, decoder-only for generation — Alammar [14] uses the split as the spine of his book. Reimplemented from scratch in PyTorch in Raschka [87]; referenced as architecture background in [28], [32], [56], [106]. Adjacent: self-attention, multi-head attention, causal attention, positional embeddings, layer normalization, GELU activation.

[150] **Retrieval-Augmented Generation (RAG)** — Augments LLMs with real-time retrieval from external corpora to ground outputs and reduce hallucination. Appears in **10 of the 18 AI Engineering books** in hub [2]: Alammar [14], Anon vector-DB [15], Berryman [28], Bratanic GraphRAG [30], Caelen [32], Huyen [56], Mendelevitch [69], Oshin LangChain [80], Taulli [97], Thomas [99]. The full production blueprint with ingest/query flow plus KPI table is [69]; the GraphRAG variant is [30]; vector-database substrate is [15]; LangChain wiring is [80]; security and prompt-injection mitigation is [69] and [106].

[151] **Prompt Engineering** — Designing inputs so the LLM responds reliably. Six AI Engineering books treat it as a primary topic: Berryman [28], Boonstra [29], Caelen [32], Huyen [56], Taulli [97], plus the prompting chapters of Alammar [14]. Berryman frames it as document engineering inside a feedforward retrieve/snippetize/score/pack pipeline; Boonstra catalogues techniques and supplies the Vertex AI sampling-control recipes. Sub-techniques: zero-shot, few-shot, chain-of-thought [152], ReAct, step-back prompting, self-consistency, tree-of-thoughts, role / system prompting, automatic prompt engineering, prompt assembly.

[152] **Chain-of-Thought Prompting** — Eliciting intermediate reasoning steps before the final answer. Covered in [14], [28], [29], [32], [80], [97]. Adjacent to ReAct ([28], [29], [80]), self-consistency [29], tree-of-thoughts [29], step-back prompting ([29], [30]).

[153] **Prompt Injection** — Adversarial input that overrides instructions. Treated in [32] (Caelen — frames it as effectively inevitable), [69] (Mendelevitch — RAG-layer mitigation), [99] (Thomas — enterprise governance angle), [106] (Wilson — OWASP framing). Adjacent concepts: LLM jailbreaking, insecure output handling, trust boundaries, OWASP LLM Top 10 (all in [106]); data poisoning ([99], [106]).

[154] **Market Making** — Liquidity provision under inventory risk. Canonical sources: Cartea [33], Lu [66]; multi-asset extensions in the Bergault series [26], [27]; FX-specific work in the Barzykin series [21]–[25]; RFQ specialisations [44], [47]; fill-probability work [67]; cross-responses [105]; LOB-level extensions [40], [107]. Hub [7]. Adjacent: Avellaneda-Stoikov model, inventory risk, adverse selection, fill probability, client tiering, RFQ markets.

[155] **Limit Order Book** — Microstructure of electronic markets. Modelled in [12], [33], [40], [45], [105], [107]; cross-asset extensions in HFT futures [31], [50]. Hub [7]. Adjacent: optimal execution, MLOFI, market making [154].

[156] **Credit Spread Curve** — Term structure of credit spreads. Constructed via the unified hazard-rate methodology of [104] (UBS Delta) and bootstrapping in [86] (Pullirsch); referenced from valuation in [68] (Martin); global puzzle treatment in [54] (Huang); forecasting in [61] (Krishnan). Anchor concept for hubs [5] and [6]. Adjacent: Z-spread, carry-rolldown, survival probability, hazard rate curve.

[157] **Factor Investing** — Systematic factor strategies for bonds (size, low-risk, value, momentum). Core sources [53] (Houweling), [49] (Haesen — spillover), [37] (Dickerson — bond CAPM), [77] (Nunes — ML-based factor allocation), [43] (Feng — ML); pitfalls in [38] (Dickerson). Hub [5]. Adjacent: factor models, bond momentum, residual momentum, market microstructure noise.

[158] **Adaptive Conformal Inference (ACI)** — Online updating of the nominal coverage level to maintain validity under distribution drift. Introduced in [111] (Zaffran 2022); generalised to AgACI in the same paper; basis for DR-ACI [59] under causal-inference dependence; extended for sequential coverage in SPCI [108]; multi-distribution-robust variant in [109]. Hub [3] / [4]. Adjacent: distribution drift, conformal prediction [148].

[159] **Doubly Robust Estimation** — Treatment-effect estimator consistent if either the propensity-score model or the outcome model is correctly specified. Used in [59] (DR-ACI). Hub [4]. Adjacent: double machine learning, temporal cross-fitting, beta-mixing, causal inference.

[160] **Long Memory & MFDFA** — Slowly decaying autocorrelations (Hurst H>0.5) plus multifractal detrended fluctuation analysis. Foundational in Guillaume O&A [48]; confirmed in FX order flow in Gould [46]; analysed via MFDFA in COVID [17], Koukorinis stylised facts [60], gold-oil [89], Bitcoin [95]; transaction-clock interpretation critiqued in [73]. Hub [9]. Adjacent concepts: Hurst exponent, Gegenbauer processes, change-point detection, kernel tests for nonstationary processes [63].

---

*Last updated: 2026-05-17 | Total nodes: 160 | Coverage: 105 sources, 165 entities, 287 concepts | AI Engineering branch added 2026-05-17*
