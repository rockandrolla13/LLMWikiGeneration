# ML Research Wiki - Mind Map

*A grep-friendly knowledge graph. Each `[N]` is a line-anchored marker. Run `grep "^\[N\]"` to fetch a single node, or `grep "\[N\]"` to find all cross-references to it.*

---

## Routing Hubs (Nodes 1–11)

[1] **Overview** — Top-level routing across eleven themes. This wiki interleaves quantitative finance research (fixed income, credit ETFs, market microstructure, ETF flows, stylized facts, actuarial science) with machine-learning methodology (conformal prediction, causal inference, statistical methods, transformers) and a large applied AI engineering branch (LLMs, RAG, knowledge graphs, prompt engineering, LLM security, ML systems, software architecture). Major hubs: AI Engineering [2], Conformal Prediction & Uncertainty Quantification [3], Causal Inference & Treatment Effects [4], Fixed Income & Corporate Bonds [5], Credit ETF & Credit Risk [6], Market Microstructure & Optimal Execution [7], ETF Flows & Trade Decomposition [8], Stylized Facts & Long Memory [9], Actuarial Science & Mortality [10], Statistical Methods & ML Foundations [11]. Coverage as of 2026-05-21: **109 sources, 171 entities, 305 concepts**. The CP cluster [3] just gained the tutorial/review quartet [164]-[167] (added 2026-05-21). The AI Engineering branch [2] is the single largest cluster (18 books, added May 2026); fixed-income clusters [5] and [6] are the deepest legacy clusters combined.

[2] **AI Engineering** — Eighteen books (2020–2025) covering the practitioner stack for building applications on top of foundation models. Anchor sources: Huyen's AI Engineering [56] and Designing ML Systems [55], Raschka's Build LLM from Scratch [87], Alammar & Grootendorst's Hands-On LLMs [14]. Sub-clusters: (a) **LLM internals** — Raschka [87], Alammar [14]; (b) **RAG** — Mendelevitch [69], Bratanic & Hane GraphRAG [30], Anon Vector Databases [15]; (c) **Knowledge graphs** — Barrasa & Webber [20], Bratanic [30]; (d) **Prompt engineering** — Berryman & Ziegler [28], Boonstra [29]; (e) **LLM applications** — Caelen [32], Oshin & Campos LangChain [80]; (f) **AI-assisted programming** — Taulli [97]; (g) **LLM security** — Wilson OWASP [106]; (h) **Software architecture & SWE** — Percival & Gregory [82], Nelson [75], Hermans [52]; (i) **AI strategy / business** — Thomas/Zikopoulos/Soule [99]. Cross-cutting concepts: **RAG** [150] appears in 10 of these books, **prompt engineering** [151] in 6, **chain-of-thought** in 6, **prompt injection** in 4. Most-cited entities: **OpenAI** [144] (9 books), **LangChain** [145] (7), **Hugging Face** [146] (3), **Anthropic** (3), **GitHub Copilot** [147] (3). The branch shares its conceptual root — transformers [149] — with the original Vaswani et al. attention paper [18] in hub [11]. Synthesis: see analysis [161] which articulates AI Engineering as a discipline distinct from ML Engineering and software engineering, anchored on Huyen's 2022→2025 evolution.

[3] **Conformal Prediction & Uncertainty Quantification** — Distribution-free prediction-set methodology from Vovk's original framework through Candès's adaptive extensions, Romano's CQR, Zaffran's electricity-forecasting PhD, and recent extreme-value, multi-output and time-series work. Anchor sources: Zaffran PhD [113], Zaffran ACI [111], Zaffran CP-with-missing-values [112], Bao review [19], Adams functional anomaly [13], Farinhas non-exchangeable CRC [41], Chernozhukov distributional CP [35], Johnstone multi-output [58], Misiakos DAG-TFRC [70], Pasche extreme CP [81], Xu SPCI [108], Sun copula CPTS [96], Yang multi-distribution robust [109], Lee KOWCPI [64]. **Tutorial / review quartet (added 2026-05-21):** Angelopoulos & Bates gentle intro [164], Xu & Xie EnbPI [165], Stocker et al. CP-time-series review [166], Dieuleveut & Zaffran Hi! PARIS slide deck [167]. Connects to causal inference [4] via Koukorinis DR-ACI [59]. Core concepts: conformal prediction [148], conformalized quantile regression, adaptive conformal inference (ACI) [158], conformal risk control (CRC), mask-conditional validity, coverage guarantee, exchangeability, [[concepts/marginal-coverage|marginal coverage]], [[concepts/conditional-coverage|conditional coverage]], [[concepts/nonconformity-score|nonconformity score]], [[concepts/enbpi|EnbPI]], [[concepts/weighted-conformal-prediction|weighted CP]], [[concepts/adaptive-prediction-sets|APS]] / [[concepts/regularized-adaptive-prediction-sets|RAPS]], [[concepts/full-conformal-prediction|full]] / [[concepts/cross-conformal-prediction|cross-conformal]], [[concepts/agaci|AgACI]], [[concepts/conformal-pid-control|Conformal PID]], [[concepts/block-conformal-prediction|BCP]], [[concepts/learn-then-test|Learn Then Test]]. Researchers: Vovk [129], Candès, Romano, Zaffran [130], Farinhas, Martins, Dieuleveut, Josse, Angelopoulos, Bates, Xu, Xie, Stocker, Małgorzewicz, Fontana, Ben Taieb. Synthesis: analysis [162] explores Tukey g-h transformation as a route to skewed/heavy-tailed prediction intervals built on this framework.

[4] **Causal Inference & Treatment Effects** — Treatment-effect estimation under temporal dependence and distribution drift, bridging conformal prediction [3] with double machine learning. Anchor source: Koukorinis DR-ACI 2026 [59] — doubly robust adaptive conformal inference with temporal cross-fitting and block bootstrap. Concepts: doubly robust estimation [159], temporal cross-fitting, beta-mixing, double machine learning. Author Andreas Koukorinis [131] (UCL) extends Candès's ACI [158] to causal estimands under dependence. Flexible least squares [71] supplies time-varying parameter machinery; statistical methodology in [11].

[5] **Fixed Income & Corporate Bonds** — Credit-spread term structure, factor models for bond returns, momentum strategies, ML-based valuation and prediction. Anchor sources: Martin credit curve [68], Houweling factor investing [53], Haesen momentum spillover [49], Dickerson bond risk [37], Dickerson pitfalls [38], Huang global credit-spread puzzle [54], Feng ML bond returns [43], Saha BlackRock muni-ML [90], Sehatpour green bonds [91], Rehman green/oil [88], He functional regression [51], Krishnan spread forecast [61], De Moura pairs trading [36], Antonian graph-signal-processing thesis [16], Nunes ML fixed income thesis [77], Kumar liquidity-adjusted AFNS [62], Omrane yield-curve forecasting [78], Technical bond-similarity [98]. Concepts: credit spread curve [156], Z-spread, carry-rolldown, bond CAPM, factor investing [157], factor models, bond momentum, residual momentum, credit spread puzzle, Nelson-Siegel model, green bond spreads, look-ahead bias, TRACE data, market microstructure noise. Key entities: Martin [133], Houweling [134], van Zundert, Dickerson [135], Nikitopoulos.

[6] **Credit ETF & Credit Risk** — The Lehman / UBS Delta methodology lineage: hazard-rate credit curves, base correlation for CDO tranches, CDS-bond basis, LBO scoring, pricing of correlated credit. Anchor sources: Pullirsch credit-spread risk [86], Trinh LEVER framework [101], Lehman QCR Quarterly [65], UBS next-gen credit curves [104], Spec single-name fundamental [94], Fermanian MD2C corporate bonds [44], Gueant particle filtering bond mid-prices [47], Fedenia ML trade classification [42], Shi CDS options comovement [92]. Concepts: hazard rate curve, base correlation, CDS-bond basis, LEVER score, LBO risk, spread per turn of leverage, survival probability. Institutional entities: Lehman Brothers [141], UBS Delta [142]; researchers Pullirsch, Trinh, Bhattacharya, Matthews, Bosatta.

[7] **Market Microstructure & Optimal Execution** — Limit-order-book models, market making, optimal execution, FX dealer/RFQ markets, high-frequency liquidity. Anchor sources: Cartea optimal execution [33], Abergel algorithmic-trading LOB [12], Lu market making collection [66], Xu MLOFI [107], Wang cross-responses [105], Ellersgaard hedge tracking LOB [40], Bergault multi-asset MM [26], Bergault RFQ pricing [27], Barzykin algorithmic FX [21], Barzykin dealer tiers [22], Barzykin multi-currency [23], Barzykin precious metals [24], Barzykin adverse selection [25], Lokin fill probabilities [66_a — see [55_a]], Brigida trade-intensity gas futures [31], Golub multiscale liquidity [45], Gueant particle filtering [47], Fermanian MD2C [44]. Concepts: limit order book [161 → 155], market making [154], optimal execution, Avellaneda-Stoikov model, inventory risk, adverse selection, fill probability, RFQ markets, client tiering, MLOFI, cross-responses. Researchers: Cartea, Gueant [137], Jaimungal, Bergault, Barzykin, Gould [138].

[8] **ETF Flows & Trade Decomposition** — How passive flows distort prices and how constituent trade flows can be decomposed. Anchor sources: Optiver corporate-bond ETF contraflow [79], Petit data-driven flow decomposition [85], Chao Deutsche Bank ETF flows research [34]. Concepts: ETF flows, flow decomposition, index reconstitution, trade classification. Synthesis: analysis [163] codifies the contraflow trading strategy.

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

## Analyses (Nodes 161-163)

*Cross-source syntheses. These are the highest-leverage routing targets — each draws together 3+ sources to articulate a thesis, decision framework, or comparative position.*

[161] **AI Engineering as a Discipline** — Synthesis across all 18 books of hub [2]. Articulates AI Engineering as the *engineering of adaptation on procured foundation models*, distinct from ML Engineering (anchored on Huyen 2022 [55] → 2025 [56] trajectory comparison) and from software engineering (Percival [82], Nelson [75]). Covers what's new (prompt engineering as program design [151], RAG pipelines [150], agentic patterns, inference-time control, hallucination management), what stays the same (testing, observability, DDD, modular code), three core contradictions (fine-tune vs RAG, build-from-scratch vs build-on-APIs from [87] vs [32]/[80], agentic vs scripted), and gaps the corpus has not yet codified. Includes a decision framework table classifying problems as AI / ML / SWE and a canonical reference-architecture diagram. Hub [2]. Sources: all 18 of the AI Engineering corpus.

[162] **Conformal Prediction with Tukey g-h Transformation** — Active-research synthesis (Zaffran [113], Zaffran ACI [111], Peters quantile diffusions [84], Technical bond-similarity [98]). Explores using Tukey g-and-h transformation to construct skewed/heavy-tailed prediction intervals with conformal coverage guarantees. Hub [3]. Concepts: conformal prediction [148], Tukey g-h transformation, prediction intervals, coverage guarantee.

[163] **ETF Contraflow Strategy for Corporate Bonds** — Trading-strategy synthesis combining Chao Deutsche Bank ETF-flows research [34], Optiver contraflow [79], and Petit data-driven flow decomposition [85]. Codifies the mean-reverting-flow signal: long bonds with ETF outflows, short bonds with ETF inflows, with construction details and evaluation framework. Hub [8]. Concepts: ETF flows, flow decomposition, mean reversion, index reconstitution.

---

## Sources (Nodes 164-179)

*CP tutorial/review sources added 2026-05-21. Together they form a quartet covering the i.i.d. case [164], the time-series case [166], the canonical algorithmic extension [165], and the Dieuleveut-group teaching deck [167]. Nodes [168]-[179] are the JFE/JAE/JFS/SNDE batch added 2026-05-21 — eight Journal of Financial Econometrics papers spanning factor models, jumps, market making, VaR, tail expectations, factor timing, FX panel intensity, and bond spread correlations, plus one paper each from Journal of Accounting and Economics, Journal of Financial Stability, and Studies in Nonlinear Dynamics and Econometrics.*

[164] **A Gentle Introduction to Conformal Prediction (Angelopoulos & Bates 2022)** — The de-facto practitioner reference for [[concepts/conformal-prediction|CP]]. Distils CP into a four-step recipe (heuristic uncertainty → [[concepts/nonconformity-score|score]] → empirical `(n+1)(1−α)/n` quantile → set), proves finite-sample [[concepts/marginal-coverage|marginal coverage]], and catalogues extensions: [[concepts/adaptive-prediction-sets|APS]] / [[concepts/regularized-adaptive-prediction-sets|RAPS]] for classification, CQR for regression, [[concepts/conformal-risk-control|conformal risk control]], [[concepts/learn-then-test|Learn Then Test]] for non-monotone risks, [[concepts/weighted-conformal-prediction|weighted CP]] under covariate shift, [[concepts/full-conformal-prediction|full]] / [[concepts/cross-conformal-prediction|cross-conformal]] / Jackknife+, and [[concepts/conformal-outlier-detection|conformal outlier detection]]. Hub [3]. Concepts: conformal prediction [148], [[concepts/marginal-coverage|marginal coverage]], [[concepts/conditional-coverage|conditional coverage]], [[concepts/nonconformity-score|nonconformity score]]. Entities: Anastasios Angelopoulos, Stephen Bates.

[165] **Conformal prediction for time series / EnbPI (Xu & Xie 2023)** — Introduces [[concepts/enbpi|EnbPI]], a bootstrap-ensemble conformal procedure that wraps a point predictor, avoids data splitting, and avoids retraining at test time. Proves asymptotic [[concepts/conditional-coverage|conditional]] and [[concepts/marginal-coverage|marginal coverage]] under β-mixing dependence — rare for CP-on-time-series. Empirically dominates ARIMA, ICP, J+aB, and AdaptCI on solar/wind, anomaly detection, and air-quality benchmarks. Predecessor to the authors' SPCI [108]. Hub [3]. Concepts: [[concepts/enbpi|EnbPI]], [[concepts/jackknife-plus-after-bootstrap|Jackknife+ after Bootstrap]], β-mixing, prediction intervals. Entities: Chen Xu, Yao Xie.

[166] **A Gentle Introduction to Conformal Time Series Forecasting (Stocker, Małgorzewicz, Fontana, Ben Taieb 2025)** — Time-series companion to [164]. Unifies CP-for-time-series into a **four-family taxonomy**: (i) reweight calibration ([[concepts/weighted-conformal-prediction|WCP]]); (ii) refresh residuals via OOB bootstrap ([[concepts/enbpi|EnbPI]], SPCI [108]); (iii) adapt α online ([[concepts/adaptive-conformal-inference|ACI]] [158], [[concepts/agaci|AgACI]], [[concepts/conformal-pid-control|PID-Conformal]]); (iv) block randomisation ([[concepts/block-conformal-prediction|BCP]]). Theoretical: finite-sample marginal and conditional coverage for SCP under β-mixing. Empirical: under abrupt mean shift, SCP / Block-SCP / WCP-window all *fail* to cover; ACI / EnbPI / WCP-exp / WCP-linear self-correct. Hub [3]. Concepts: [[concepts/weighted-conformal-prediction|WCP]], [[concepts/enbpi|EnbPI]], [[concepts/agaci|AgACI]], [[concepts/conformal-pid-control|Conformal PID]], [[concepts/block-conformal-prediction|BCP]]. Entities: M. Stocker, Wiktoria Małgorzewicz, Matteo Fontana, Souhaib Ben Taieb.

[167] **Conformal Prediction: A Tutorial (Dieuleveut & Zaffran, Hi! PARIS 2025)** — 91-slide tutorial deck (joint UAI/ICML material) covering SCP, CQR, APS, [[concepts/full-conformal-prediction|Full CP]], Jackknife+, [[concepts/adaptive-conformal-inference|ACI]] [158], OSSCP, covariate-shift WCP, [[concepts/conformal-risk-control|risk control]], and CP-with-missing-values (CP-MDA-Nested, Zaffran et al. 2024 [112]). Includes the Vovk impossibility result for [[concepts/conditional-coverage|conditional coverage]] and PAC-style calibration-conditional bounds. Pairs naturally with [[sources/zaffran-phd|Zaffran's PhD]] [113]. Hub [3]. Entities: [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]], [[entities/margaux-zaffran|Margaux Zaffran]].

### JFE / JAE / JFS / SNDE batch (added 2026-05-21)

[168] **Mixed-Frequency Macro-Finance Factor Models (Andreou, Gagliardini, Ghysels, Rubin 2020)** — Asymptotic theory for testing common factors across two large panels of macro and financial variables sampled at different frequencies. Compares aggregation-first vs PCA-first procedures within a [[concepts/group-factor-models|group factor]] framework with [[concepts/midas-regression|MIDAS]] aggregation. Finds no single common macro-finance factor across 1963-2017 but evidence of one in pre- and post-[[concepts/great-moderation|Great Moderation]] subperiods, with predictive power for GDP, VIX, VRP, corporate spreads, and ETF returns. Hub [5] / [11]. Concepts: [[concepts/factor-models|factor models]], [[concepts/mixed-frequency-data|mixed-frequency data]], [[concepts/midas-regression|MIDAS]], [[concepts/principal-components-analysis|PCA]], [[concepts/canonical-correlation-analysis|CCA]], [[concepts/group-factor-models|group factors]], [[concepts/great-moderation|Great Moderation]]. Entities: [[entities/elena-andreou|Elena Andreou]], [[entities/patrick-gagliardini|Patrick Gagliardini]], [[entities/eric-ghysels|Eric Ghysels]], [[entities/mirco-rubin|Mirco Rubin]].

[169] **Jump Clustering, Information Flows, and Stock Price Efficiency (Chen 2024)** — Models stock-return jumps as a bivariate positive/negative self/cross-exciting [[concepts/hawkes-processes|Hawkes process]] inside a [[concepts/stochastic-volatility-with-jumps|stochastic-volatility-with-jumps]] model and proposes a [[concepts/jump-clustering|jump-clustering]] measure of [[concepts/stock-price-efficiency|stock price inefficiency]]. Bayesian MCMC for in-sample; [[concepts/particle-filter|particle filter]] for out-of-sample probabilistic jump forecasts. The jump-clustering measure outperforms Hou-Moskowitz price delay in capturing post-earnings-announcement drift; a long-short signal based on predicted positive-vs-negative jump probabilities yields a Sharpe ratio of 1.62 net of costs. Hub [7] / [11]. Concepts: [[concepts/hawkes-processes|Hawkes processes]], [[concepts/jump-clustering|jump clustering]], [[concepts/particle-filter|particle filter]], [[concepts/stock-price-efficiency|stock price efficiency]]. Entities: [[entities/jian-chen|Jian Chen]].

[170] **Large-Dimensional Portfolio Selection with HF Dynamic Factor Model (Bodilsen 2025)** — Proposes a high-frequency-based dynamic factor model for forecasting large [[concepts/realized-covariance|realized covariance]] matrices of S&P 500 constituents with observable ETF factors and a data-driven block idiosyncratic covariance inferred by [[concepts/hierarchical-clustering|hierarchical clustering]]. OLS-estimable, scales linearly, outperforms HEAVY, HAR-DRD, and DCC benchmarks on out-of-sample [[concepts/minimum-variance-portfolio|minimum-variance]] portfolios. Hub [5] / [7]. Concepts: [[concepts/realized-covariance|realized covariance]], [[concepts/multivariate-realized-kernel|multivariate realized kernel]], [[concepts/hierarchical-clustering|hierarchical clustering]], [[concepts/har-model|HAR]], [[concepts/factor-models|factor models]] (with [168] as macro-finance counterpart). Entities: [[entities/simon-t-bodilsen|Simon T. Bodilsen]].

[171] **Statistical Predictions of Trading Strategies in Electronic Markets (Cartea, Cohen, Graumans, Labyad, Sanchez-Betancourt, van Veldhuijzen 2025)** — Uses Euronext Amsterdam regulatory data with algorithm-level identifiers to predict the direction, price, and volume of incoming [[concepts/limit-order-book|limit orders]]. Logistic regression with algorithm/member IDs achieves ~70% order-weighted directional accuracy (vs ~54% without). [[concepts/trader-clustering|Trader clustering]] reveals only ~1/3 of Liquidity Providers actually behave as [[concepts/market-making|market makers]] — the rest split between directional and opportunistic styles despite a single dealing capacity. Hub [7]. Concepts: [[concepts/algorithmic-trading|algorithmic trading]], [[concepts/order-flow-prediction|order-flow prediction]], [[concepts/agent-based-models|agent-based models]], [[concepts/high-frequency-trading|HFT]]. Entities: [[entities/alvaro-cartea|Cartea]] (also [33]), [[entities/samuel-n-cohen|Cohen]], [[entities/leandro-sanchez-betancourt|Sanchez-Betancourt]], [[entities/robert-graumans|Graumans]], [[entities/saad-labyad|Labyad]], [[entities/leon-van-veldhuijzen|van Veldhuijzen]].

[172] **Loss-Based Bayesian Sequential VaR with RNN-HAR (Peiris, Tran, Wang, Gerlach 2025)** — [[concepts/rnn-har|RNN-HAR]] embeds three RNNs (daily/weekly/monthly) inside the [[concepts/har-model|HAR]] cascade for direct [[concepts/value-at-risk|VaR]] forecasting via [[concepts/asymmetric-laplace-density|asymmetric-Laplace]] [[concepts/quantile-regression|quantile-loss]] [[concepts/generalized-bayesian-inference|generalized Bayes]] with [[concepts/sequential-monte-carlo|Sequential Monte Carlo]]. Across 31 market indices the model consistently outperforms HAR variants on quantile scores. Hub [3] / [11]. Concepts: [[concepts/value-at-risk|VaR]], [[concepts/har-model|HAR]] (shared with [170]), [[concepts/recurrent-neural-networks|RNNs]], [[concepts/generalized-bayesian-inference|generalized Bayes]], [[concepts/realized-variance|realized variance]]. Entities: [[entities/rangika-peiris|Rangika Peiris]], [[entities/minh-ngoc-tran|Minh-Ngoc Tran]], [[entities/chao-wang|Chao Wang]], [[entities/richard-gerlach|Richard Gerlach]], [[entities/fulvio-corsi|Fulvio Corsi]] (cited; HAR originator).

[173] **Efficiently Weighted Estimation of Tail and Interquantile Expectations (Barendse 2026)** — Develops a [[concepts/semiparametric-estimation|semiparametric]] two-stage joint estimator for left- and right-[[concepts/tail-expectation|tail expectations]] together with [[concepts/interquantile-expectation|interquantile expectations]] in nonlinear time-series settings, under [[concepts/fissler-ziegel-loss|Fissler-Ziegel]] joint elicitability for VaR / [[concepts/expected-shortfall|Expected Shortfall]]. Derives efficient weights, locally robust to first-stage [[concepts/quantile-regression|quantile-regression]] nuisance, and asymptotics under β-mixing. Empirically, small-market-equity stocks contribute disproportionately to [[concepts/fama-french-factors|Fama-French]] abnormal returns through tail events. Hub [3] / [11]. Concepts: [[concepts/tail-expectation|tail expectation]], [[concepts/expected-shortfall|Expected Shortfall]], [[concepts/interquantile-expectation|interquantile expectation]], [[concepts/fissler-ziegel-loss|Fissler-Ziegel]]. Entities: [[entities/sander-barendse|Sander Barendse]], [[entities/tobias-fissler|Fissler]] (cited), [[entities/johanna-ziegel|Ziegel]] (cited), [[entities/andrew-patton|Patton]] (cited).

[174] **Multifactor Timing with Deep Learning (Cotturo, Liu, Proner 2026)** — A dynamic multitask (DMT) neural network for [[concepts/factor-timing|multifactor timing]] combining hard-sharing [[concepts/multitask-learning|multitask]] layers with separate macroeconomic and financial [[concepts/lstm-networks|LSTMs]]. Across 1965-2021 DMT outperforms linear, tree, and off-the-shelf neural baselines with 56.4% directional accuracy and a 0.82 net Sharpe. [[concepts/shapley-values|Shapley values]] identify unemployment, leverage, profitability, and money as the most influential macro/financial predictors. Hub [5] / [2]. Concepts: [[concepts/factor-timing|factor timing]], [[concepts/multitask-learning|multitask learning]], [[concepts/lstm-networks|LSTM]], [[concepts/deep-learning-for-finance|deep learning for finance]], [[concepts/factor-investing|factor investing]] (shared with [157]). Entities: [[entities/paul-cotturo|Cotturo]], [[entities/fred-liu|Liu]], [[entities/robert-proner|Proner]], [[entities/bryan-kelly|Kelly]] (cited), [[entities/dacheng-xiu|Xiu]] (cited), [[entities/shihao-gu|Gu]] (cited).

[175] **Trading Dynamics in the FX Market: Latent Factor Panel Intensity (Nolte & Voev 2011)** — Multivariate [[concepts/panel-intensity-models|panel intensity]] model with a time-varying latent factor for trader open/close actions across investors and currency pairs in OANDA FXTrade data. Estimated by [[concepts/simulated-maximum-likelihood|simulated ML]] with [[concepts/efficient-importance-sampling|efficient importance sampling]] in the [[concepts/stochastic-conditional-intensity|Bauwens-Hautsch SCI]] tradition. Documents a portfolio-level [[concepts/disposition-effect|disposition effect]] that varies with investor sophistication, linking [[concepts/behavioral-finance|behavioral finance]] / [[concepts/prospect-theory|prospect theory]] to high-frequency FX dynamics. Hub [7] / [9]. Concepts: [[concepts/panel-intensity-models|panel intensity]], [[concepts/disposition-effect|disposition effect]]. Entities: [[entities/ingmar-nolte|Nolte]], [[entities/valeri-voev|Voev]], [[entities/luc-bauwens|Bauwens]] (cited), [[entities/nikolaus-hautsch|Hautsch]] (cited).

[176] **High- and Low-Frequency Correlations in European Government Bond Spreads (Boffelli, Skintzi, Urga 2017)** — Combines [[concepts/dynamic-equicorrelation|DECO]] and [[concepts/midas-regression|MIDAS]] (shared with [168]) to model 15-minute high-frequency correlations and monthly macro-driven low-frequency correlations of European 10-year [[concepts/government-bond-spreads|government bond spreads]] vs Germany during the 2007-2012 [[concepts/sovereign-debt-crisis|sovereign debt crisis]]. Finds crisis-era correlation increases are driven primarily by market-liquidity dynamics rather than macro fundamentals; [[concepts/garch-midas|GARCH-MIDAS]] and [[concepts/dcc-midas|DCC-MIDAS]] machinery handles the mixed-frequency volatility and correlation jointly. Hub [5] / [11]. Concepts: [[concepts/dcc-midas|DCC-MIDAS]], [[concepts/dynamic-equicorrelation|DECO]], [[concepts/garch-midas|GARCH-MIDAS]]. Entities: [[entities/simona-boffelli|Boffelli]], [[entities/vasiliki-skintzi|Skintzi]], [[entities/giovanni-urga|Urga]] (also in [178]), [[entities/robert-engle|Engle]] (cited).

[177] **Information Flows in Trading Networks (Huber, Watts, Zhu 2026, JAE)** — Regulatory insurance-company transaction data on US [[concepts/corporate-bonds|corporate bonds]] maps insurer-[[concepts/dealer-networks|dealer trading networks]] and shows that insurers with larger dealer networks earn ~7 bps monthly risk-adjusted excess return by trading ahead of downgrades, defaults, and M&A. The performance advantage concentrates in connections to dealers with research / underwriting / M&A involvement — consistent with [[concepts/informed-trading|informed trading]] propagating through [[concepts/social-networks-in-finance|social networks in finance]] and [[concepts/material-non-public-information|MNPI]] leakage across information barriers in [[concepts/otc-markets|OTC markets]]. Quid-pro-quo: insurers reward informative dealers with future order flow. Hub [5] / [6] / [8]. Entities: [[entities/stefan-huber|Stefan J. Huber]], [[entities/edward-watts|Edward M. Watts]], [[entities/christina-zhu|Christina Zhu]].

[178] **Asset Class Liquidity Risk Indicators (Coppola, Urga, Varaldo 2025, J Fin Stability)** — Composite [[concepts/liquidity-risk|liquidity-risk]] indicators for six European and US equity and bond markets (2007-2023), aggregating financial, monetary, and credit variables via [[concepts/ecdf-aggregation|ECDF standardization]]. Endogenous [[concepts/markov-switching-models|Markov-switching]] models identify low/medium/high-risk regimes mapped to [[concepts/bubble-detection|PSY bubble]] episodes (GFC, sovereign crisis, 2015-16 China crash, COVID, 2022 Ukraine). The Brunnermeier-Pedersen [[concepts/funding-liquidity|funding liquidity]] vs market-liquidity ([[concepts/amihud-illiquidity|Amihud]]) split shows credit drivers dominate during the sovereign crisis and monetary drivers during COVID. Hub [5] / [9]. Entities: [[entities/anna-coppola|Coppola]], [[entities/giovanni-urga|Urga]] (also in [176]), [[entities/alessandro-varaldo|Varaldo]], [[entities/markus-brunnermeier|Brunnermeier]] (cited), [[entities/yakov-amihud|Amihud]] (cited).

[179] **Realized Probability Index is a Better Market Timing Indicator (Xie, Wu, Sun, Wang 2026, SNDE)** — Compares three [[concepts/market-timing|market-timing]] indicators (return, binary directional, [[concepts/realized-probability-index|realized probability index]]) and proves the realized probability index — the share of cumulative positive intraday returns in cumulative absolute return — dominates the binary indicator in information content and economic efficiency and is more predictable than the return itself. Pairs naturally with the Christoffersen-Diebold [[concepts/sign-dependence-volatility|sign-dependence-via-volatility]] line on [[concepts/directional-forecasting|directional forecasting]] using [[concepts/high-frequency-data|high-frequency data]]. Hub [7] / [9]. Entities: [[entities/haibin-xie|Xie]], [[entities/boyao-wu|Wu]], [[entities/yuying-sun|Sun]], [[entities/shouyang-wang|Wang]], [[entities/francis-diebold|Diebold]] (cited).

---

## Analyses (continued — Node 180)

[180] **Conformal Prediction for Algorithmic and HFT Traders** — Practitioner-facing synthesis ([[analyses/conformal-prediction-for-hft-traders|page]]). Translates the CP literature ([164] Angelopoulos-Bates, [165] Xu-Xie EnbPI, [166] Stocker et al., [167] Dieuleveut-Zaffran, plus [111] Zaffran ACI, [108] Xu SPCI, [59] Koukorinis DR-ACI) into a usable guide for algo/HFT desks. Three realistic use cases: (i) market-making quote placement under [[concepts/adverse-selection|adverse selection]] with σ̂-scaled residual scores wrapped around an XGBoost mid-price predictor; (ii) pre-trade [[concepts/optimal-execution|slippage estimation]] for parent orders via CQR + EnbPI; (iii) [[concepts/statistical-arbitrage|stat-arb]] signal sizing with conformally-calibrated CDFs for Kelly-style position sizing. Side-by-side [[concepts/quantile-regression|QR]] vs CP comparison; four-family taxonomy ([[concepts/weighted-conformal-prediction|WCP]] / [[concepts/enbpi|EnbPI]] / [[concepts/adaptive-conformal-inference|ACI]] / [[concepts/block-conformal-prediction|BCP]]) recast as a practitioner decision matrix; XGBoost-plus-CP recipes with library pointers (MAPIE, crepes); three concrete simulation specs (coverage-vs-parametric, regime-shift recovery, tree+CP comparison) traders can build today. Plus pitfalls/footguns section. Hub [3]. Concepts: [[concepts/conformal-prediction|conformal prediction]] [148], [[concepts/enbpi|EnbPI]], [[concepts/conformalized-quantile-regression|CQR]], [[concepts/adaptive-conformal-inference|ACI]] [158], [[concepts/nonconformity-score|nonconformity score]], [[concepts/marginal-coverage|marginal coverage]], [[concepts/limit-order-book|LOB]] [155], [[concepts/market-making|market making]] [154].

---

---

## Sources (Nodes 181-185 — CP foundational canon, added 2026-05-24)

*Five foundational / canonical CP sources backfilling the wiki's CP cluster. Together with [164]-[167] this completes coverage from the original Vovk-Gammerman-Shafer machinery to the modern data-modality landscape.*

[181] **Algorithmic Learning in a Random World (Vovk, Gammerman, Shafer 2005)** — The foundational CP monograph. Introduces the conformal predictor framework (any [[concepts/nonconformity-score|nonconformity measure]] yields a valid predictor), [[concepts/split-conformal-prediction|inductive conformal predictors (ICP)]], [[concepts/mondrian-conformal-prediction|Mondrian conformal predictors]], the Ridge Regression Confidence Machine (RRCM), [[concepts/venn-predictors|Venn predictors]] for calibrated probability forecasting, the [[concepts/on-line-compression-models|On-Line Compression Models]] generalisation beyond exchangeability, and exchangeability supermartingales for testing the randomness assumption. 2nd ed. 2022 substantially revised. Hub [3]. Entities: [[entities/vladimir-vovk|Vovk]], [[entities/alexander-gammerman|Gammerman]], [[entities/glenn-shafer|Shafer]] (all NEW or updated to include this).

[182] **A Tutorial on Conformal Prediction (Shafer & Vovk 2007)** — 58-page foundational tutorial (arXiv 0706.3188 / JMLR 2008). Develops CP from first principles in the on-line setting: errors are probabilistically independent ε-rare events, so the law of large numbers applies to accumulating data. Works through Czuber 1900 binomial, iris classification, USPS digits with three nonconformity measures (NN, distance-to-average, SVM), and the [[concepts/on-line-compression-models|on-line Gaussian linear model]] (recovers Fisher's t-interval but with stronger on-line validity). Game-theoretic Backward-Looking Betting Protocol proof. Hub [3]. Entities: [[entities/glenn-shafer|Shafer]], [[entities/vladimir-vovk|Vovk]].

[183] **Cross-conformal predictors (Vovk 2012)** — Original paper introducing [[concepts/cross-conformal-prediction|cross-conformal prediction (CCP)]], a K-fold hybrid of ICP + cross-validation. Shows that averaging per-fold p-values (not Fisher-combining) is the correct merge rule because the per-fold p-values are heavily dependent. Validated empirically on Spambase + MART; lower variance of confidence than ICP. Predecessor of Barber-Candès-Ramdas-Tibshirani [[concepts/jackknife-plus|Jackknife+]] (2021). Hub [3]. Entity: [[entities/vladimir-vovk|Vovk]].

[184] **Conformal prediction: A unified review of theory and new challenges (Fontana, Zeni, Vantini 2023, Bernoulli)** — Theory-focused review of post-2005 CP developments. Unifies notation (α after Lei-Robins-Wasserman, predicting (n+1)-th from previous n), maps the validity hierarchy (marginal → local → [[concepts/mondrian-conformal-prediction|Mondrian]] → impossibility of distribution-free object-conditional → CQR as partial answer), covers the on-line / batch duality, and treats [[concepts/cross-conformal-prediction|cross-conformal]] / [[concepts/jackknife-plus|jackknife+]] / [[concepts/conformalized-quantile-regression|CQR]] / weighted-CP / dependent-data extensions. The canonical theoretical companion to [164]. Hub [3]. Entities: [[entities/matteo-fontana|Fontana]], [[entities/gianluca-zeni|Zeni]], [[entities/simone-vantini|Vantini]].

[185] **Conformal Prediction: A Data Perspective (Zhou, Chen, Gui, Cheng 2025, ACM Computing Surveys)** — Data-modality-organised survey (vs the methodology-organised [164] and [184]). Hierarchical taxonomy: static (structured: flat / hierarchical / matrix-tensor / [[concepts/cp-for-graphs|graph]]; unstructured: [[concepts/cp-for-nlp|text]] / [[concepts/cp-for-vision|image]] / heterogeneous) vs dynamic (1D / multi-dim / streaming). Comprehensive treatment of [[concepts/cp-for-llms|CP for LLMs and NLG]] (conformal RAG, factuality subclaim filtering, conformal alignment, CALM early-exit). Three-lineage taxonomy for 1D spatio-temporal CP (reweighting / score-updating / α-updating) overlapping with Stocker et al.'s [166] four-family cut. Hub [3]. Entities: [[entities/xiaofan-zhou|Zhou]], [[entities/baiting-chen|Chen]], [[entities/yu-gui|Gui]], [[entities/lu-cheng|Cheng]].

---

---

## Sources (Nodes 186-201 — CP primary-source backbone, added 2026-05-24)

*Sixteen CP primary sources backfilling the wiki: five Tibshirani-group papers [186]-[190], the Romano-Candès classification line [191]-[193], the Berkeley risk-control trilogy [193]-[195], the Gibbs-Candès online-CP trilogy [196]-[198], the Kim-Xu-Barber J+aB precursor to EnbPI [199], and two edited volumes [200]-[201]. The Vovk-Shen-Manokhin-Xie 2017 CPD paper was intended to be in this batch but the arXiv ID lookup was wrong; rescheduled.*

[186] **Conformal Prediction Under Covariate Shift (Tibshirani, Barber, Candès, Ramdas 2019, NeurIPS)** — Primary source for [[concepts/weighted-conformal-prediction|WCP]]. Reweights nonconformity scores by likelihood ratio `w(x) = dP̃_X / dP_X` to restore finite-sample 1−α coverage under covariate shift. Introduces the broader **weighted-exchangeability** framework subsuming covariate-shift, latent-variable, and missing-data settings. Hub [3]. Entities: [[entities/ryan-tibshirani|Tibshirani]], [[entities/rina-foygel-barber|Barber]], [[entities/emmanuel-candes|Candès]], [[entities/aaditya-ramdas|Ramdas]].

[187] **Predictive Inference with the Jackknife+ (Barber, Candès, Ramdas, Tibshirani 2021, Annals of Statistics)** — Primary source for [[concepts/jackknife-plus|Jackknife+]]. Replaces `μ̂(X_{n+1}) ± R_i^{LOO}` with `μ̂_{−i}(X_{n+1}) ± R_i^{LOO}` and proves distribution-free 1−2α finite-sample coverage via tournament / comparison-matrix argument (Landau 1953). Extends to K-fold CV+ with 1−2α − √(2/n) uniformly in K, closing the gap in Vovk's [[sources/vovk-2012-cross-conformal|cross-conformal]] bound at K=n via a V-statistic variance argument. Defines (ε,ν) stability theory bridging conformal coverage to algorithmic stability. Hub [3]. Direct precursor of [[sources/kim-2020-jackknife-plus-after-bootstrap|J+aB]] and [[sources/barber-2023-beyond-exchangeability|NexCP]].

[188] **Conformal Prediction Beyond Exchangeability (Barber, Candès, Ramdas, Tibshirani 2023, Annals of Statistics)** — Primary source for [[concepts/non-exchangeable-conformal-prediction|NexCP]]. Generalises split / full / [[concepts/jackknife-plus|jackknife+]] CP to non-exchangeable data via **fixed weights** `w_i`. Proves coverage-gap bound `P(miscoverage) ≤ α + Σ w_i d_TV(Z, Z^i) / (1 + Σ w_i)` with no distributional assumption. Provides a strictly stronger residual-level bound and a randomisation technique allowing non-symmetric fitting algorithms. Recovers standard CP coverage exactly when data are exchangeable. Hub [3]. Foundation for [[sources/farinhas-2024-non-exchangeable-crc|Farinhas 2024]] and the "reweight calibration" family of [[sources/stocker-2025-conformal-timeseries-intro|Stocker 2025]].

[189] **Distribution-Free Predictive Inference for Regression (Lei, G'Sell, Rinaldo, Tibshirani, Wasserman 2018, JASA)** — The pre-Angelopoulos canonical reference for CP-in-regression. Establishes [[concepts/split-conformal-prediction|split conformal]] as the practical default. Introduces **locally-weighted (σ-scaled) conformal regression** for heteroskedasticity (predecessor to [[concepts/conformalized-quantile-regression|CQR]]). Proposes **LOCO** model-free variable importance. Companion `conformalInference` R package was the dominant CP-in-R implementation for years. Hub [3]. Entities: [[entities/jing-lei|J. Lei]], [[entities/max-gsell|G'Sell]], [[entities/alessandro-rinaldo|Rinaldo]], [[entities/ryan-tibshirani|Tibshirani]], [[entities/larry-wasserman|Wasserman]].

[190] **Conformal PID Control for Time Series Prediction (Angelopoulos, Candès, Tibshirani 2023, NeurIPS)** — Primary source for [[concepts/conformal-pid-control|Conformal PID Control]]. Recasts online CP as a PID controller (proportional / integral / derivative-via-scorecaster). Proves deterministic long-run coverage `|(1/T) Σ err_t − α| → 0` for **any** sequence (no probabilistic assumptions). Shows ACI is the quantile tracker on a transformed bounded score (Proposition 2), explaining why ACI sometimes returns infinite/null sets while direct quantile tracking doesn't. Hub [3] / [4]. Validated on CDC COVID-19 4-week-ahead forecasting, NSW electricity, AMZN/GOOGL/MSFT stock returns.

[191] **Conformalized Quantile Regression (Romano, Patterson, Candès 2019, NeurIPS)** — Primary source for [[concepts/conformalized-quantile-regression|CQR]]. Combines [[concepts/split-conformal-prediction|split conformal]] with quantile regression to produce distribution-free finite-sample-valid AND heteroskedasticity-adaptive intervals. Symmetric conformity score `E_i = max(q̂_lo − Y_i, Y_i − q̂_hi)`. Algorithm-agnostic — wraps any QR method (quantile random forests, quantile NN, gradient-boosted quantile regressors). Hub [3]. Entities: [[entities/yaniv-romano|Romano]], [[entities/evan-patterson|Patterson]], [[entities/emmanuel-candes|Candès]].

[192] **Classification with Valid and Adaptive Coverage / APS (Romano, Sesia, Candès 2020, NeurIPS)** — Primary source for [[concepts/adaptive-prediction-sets|APS]]. Novel generalized inverse quantile conformity score whose scores are uniform conditional on X under correct base classifier — making scores comparable across inputs unlike earlier adaptive scores. Achieves substantially better worst-slice conditional coverage than homogeneous conformal classification. Direct precursor of [[concepts/regularized-adaptive-prediction-sets|RAPS]]. Hub [3]. Entity: [[entities/matteo-sesia|Sesia]] (NEW).

[193] **Uncertainty Sets for Image Classifiers using Conformal Prediction / RAPS (Angelopoulos, Bates, Malik, Jordan 2021, ICLR)** — Primary source for [[concepts/regularized-adaptive-prediction-sets|RAPS]]. Adds regularisation `λ · (rank(y) − k_reg)_+` to APS, mitigating the permutation problem from miscalibrated softmax tails. On ImageNet ResNeXt-101 at α=0.1: naive top-k undercovers; APS covers with set size ~19; RAPS covers with set size ~2. **Top-k dominance theorem** (Proposition 2). Validated across 9 pretrained classifiers and ImageNet-V2. Hub [3]. Entities: [[entities/jitendra-malik|Malik]], [[entities/michael-i-jordan|Jordan]] (both NEW).

[194] **Distribution-Free Risk-Controlling Prediction Sets / RCPS (Bates, Angelopoulos, Lei, Malik, Jordan 2021, JACM 2024)** — Primary source for [[concepts/risk-controlling-prediction-sets|RCPS]] and foundational for [[concepts/conformal-risk-control|CRC]]. PAC-style (α, δ) high-probability control of expected loss `R(T) ≤ α` for any bounded monotone loss via **UCB calibration** of a nested family `{T_λ}`. Catalogue of concentration bounds: Hoeffding, Bentkus, Hoeffding-Bentkus, Waudby-Smith-Ramdas betting (recommended). Five large-scale demos: cost-sensitive classification, multi-label (MS-COCO), hierarchical (ImageNet), segmentation (Cityscapes/polyps), protein-structure prediction. Hub [3]. Entity: [[entities/lihua-lei|L. Lei]] (NEW; distinct from [[entities/jing-lei|J. Lei]]).

[195] **Learn Then Test / LTT (Angelopoulos, Bates, Candès, Jordan, Lei 2021)** — Primary source for [[concepts/learn-then-test|Learn Then Test]]. Reframes risk control as multiple hypothesis testing over a discretised `λ`-grid, using FWER (Bonferroni / fixed-sequence / sequential graphical testing) with finite-sample-valid p-values (Hoeffding-Bentkus). **Drops the monotonicity assumption** of RCPS, enabling distribution-free control of arbitrary risks: selective classification, F1, AUC, FDR, etc. Multi-risk and multi-dimensional `λ` via `p_j = max_l p_{j,l}`. Hub [3].

[196] **Adaptive Conformal Inference Under Distribution Shift / ACI (Gibbs, Candès 2021, NeurIPS)** — Primary source for [[concepts/adaptive-conformal-inference|ACI]] (the wiki previously anchored ACI via [[sources/zaffran-2022-aci|Zaffran 2022]] instead). Single-parameter online update `α_{t+1} = α_t + γ(α − err_t)`. Distribution-free anytime coverage bound `|empirical miscoverage − α| ≤ O(1/(γT))`. Recommended default `γ = 0.005`. Validated on GARCH(1,1) stock volatility (Nvidia, AMD, BlackBerry, Fannie Mae 2000-2020) and COVID-19. Hub [3]. Entity: [[entities/isaac-gibbs|Gibbs]] (NEW).

[197] **Conformal Inference for Online Prediction with Arbitrary Distribution Shifts / DtACI (Gibbs, Candès 2024, JMLR)** — Extends [196] via [[concepts/dtaci|DtACI]]: removes the user-specified γ by running k parallel ACI experts with geometric step-size grid, aggregating via exponential re-weighting plus uniform mixing. Dynamic-regret bound (Theorem 3.1) translates to local-coverage guarantee without HMM structure. Outperforms AgACI and MVP on jump-shift environments. Hub [3].

[198] **Conformal Prediction with Conditional Guarantees (Gibbs, Cherian, Candès 2023)** — Most direct response to the Lei-Wasserman / Barber et al. impossibility result for distribution-free conditional coverage. Reformulates [[concepts/conditional-coverage|conditional coverage]] as coverage over a class of covariate shifts F; finite-dimensional F gives exact finite-sample coverage simultaneously over all shifts; infinite-dimensional F (RKHS) gives best-effort PAC-style guarantee. Strict improvement over Jung et al. 2023 subgroup-QR. `conditionalconformal` PyPI package. Hub [3]. Entity: [[entities/john-cherian|Cherian]] (NEW).

[199] **Predictive Inference Is Free with the Jackknife+-after-Bootstrap / J+aB (Kim, Xu, Barber 2020, NeurIPS)** — Primary source for [[concepts/jackknife-plus-after-bootstrap|J+aB]]. Turns any bagging/subagging ensemble into a distribution-free predictive-interval method by reusing OOB aggregations as leave-one-out models, at **zero extra fitting cost**. Worst-case 1−2α coverage; empirically near nominal. Direct precursor of [[concepts/enbpi|EnbPI]] which extends to non-exchangeable time series. Hub [3]. Entity: [[entities/byol-kim|Kim]] (NEW).

[200] **The Importance of Being Learnable: Essays Dedicated to Alexander Gammerman (Nguyen, Luo eds. 2026, Springer LNCS 16290)** — Festschrift for [[entities/alexander-gammerman|Gammerman]], 478 pages, Royal Holloway-edited. Volume-level index page; individual chapters promoted to source pages on demand. Hub [3].

[201] **Advanced Analytics and Learning on Temporal Data / AALTD 2024 (Lemaire et al. eds. 2024, Springer LNAI 15433)** — 9th ECML PKDD workshop proceedings, Vilnius. Time-series ML covering classification, forecasting, change-point detection, anomaly detection, increasingly conformal prediction. Volume-level index page. Hub [3] / [11].

---

[202] **Conformal Prediction (Tibshirani 2023, CMU lecture notes)** — Graduate-level lecture notes from *Advanced Topics in Statistical Learning* (Spring 2023). 15 pages. Builds CP from first principles via two organising "key ideas" — rank-based adjusted-level quantiles and symmetric score construction. Distinctive emphasis on calibration-set-conditional Beta coverage and the Lei-Wasserman X-conditional impossibility result; reframes the practical goal as **local adaptivity**. Treats split CP, full CP, [[concepts/conformalized-quantile-regression|CQR]], and classification ([[concepts/adaptive-prediction-sets|APS]] / RAPS). Statistician-style counterpart to the ML-practitioner [[sources/angelopoulos-2022-gentle-intro|Angelopoulos-Bates 2022]] tutorial. Hub [3]. Entity: [[entities/ryan-tibshirani|R. J. Tibshirani]].

---

---

[203] **Credit & Macro branch (creditmacro corpus, 2026-06-09)** — A 46-document branch spanning corporate-credit microstructure, macro/monetary policy, systematic trading, causal inference, and forecasting, ingested from `raw/creditmacro/`. Sub-clusters: structural credit & equity-credit arbitrage [204]; sell-side credit research & the AI-capex financing wave [205]; macro, monetary policy & business cycles [206]; systematic trading, factor investing & alpha research [207]; causal inference & the philosophy of causation [208]; probabilistic forecasting & scoring rules [209]; systems thinking & recursive macro [210]. Routes into existing hubs [2] (sources), [3] (entities), [4] (concepts). Domain-distinct from the ML/conformal core but cross-linked via [[concepts/causal-inference|causal inference]], [[concepts/factor-investing|factor investing]], [[concepts/corporate-bonds|corporate bonds]], and [[concepts/credit-spread-puzzle|the credit-spread puzzle]].

[204] **Structural credit risk & equity-credit arbitrage** — The [[concepts/merton-model|Merton structural model]] (firm value as the driving state; equity as a call, risky debt as a short put) anchors this cluster, shared across [[sources/collin-dufresne-2001-determinants-credit-spread-changes|Collin-Dufresne et al. 2001]] (structural variables explain only ~25% of [[concepts/credit-spread-changes|credit-spread changes]]; a single common factor dominates residuals), [[sources/avino-2024-hedging-credit-equity-options|Avino-Salvador 2024]] (Geske compound-option hedge ratios of spreads to equity puts), and [[sources/kapadia-2012-limited-arbitrage-equity-credit|Kapadia-Pu 2012]] ([[concepts/capital-structure-arbitrage|capital-structure arbitrage]], [[concepts/limits-to-arbitrage|limits to arbitrage]]). Connects to [[concepts/cds-bond-basis|CDS-bond basis]] and [[entities/robert-merton|Robert Merton]]. Hub [4].

[205] **Sell-side credit research & the AI-capex financing wave** — A 2026 cluster of dealer research on [[concepts/ai-capex-funding|AI capex funding]] and [[concepts/private-credit|private credit]]: [[sources/hamid-2026-ai-capex-funding-bond-matrix|J.P. Morgan's hyperscaler-data-center bond matrix]] ([[concepts/high-performance-computing-credit-subsector|HPC credit subsector]], [[concepts/bond-index-inclusion-criteria|144A-for-life index mechanics]]), [[sources/patkar-2026-ms-global-credit-midyear|Morgan Stanley's mid-year outlook]], and [[sources/caprio-2026-steady-but-ai|Deutsche Bank's default study]] ([[concepts/ai-disruption-software-business-models|AI disruption of software]], [[concepts/distressed-exchange|distressed exchanges]]). Tactical/flow notes: [[sources/mercado-2015-taarss-flow-whisperer|Deutsche Bank TAARSS]] ([[concepts/etf-flow-tactical-asset-allocation|ETF-flow allocation]]) and the Citi macro books. Hub [2].

[206] **Macro, monetary policy & business cycles** — Two opposed lenses on post-crisis policy: the ECB-insider account [[sources/rostagno-2021-ecb-monetary-policy-crisis|Rostagno et al. 2021]] ([[concepts/ecb-price-stability-definition|price-stability definition]], [[concepts/outright-monetary-transactions|OMT]], the [[concepts/self-stabilizing-inflation-regime|self-stabilizing inflation regime]]) versus Austrian critiques [[sources/sieron-2021-monetary-policy-after-great-recession|Sieroń 2021]] ([[concepts/zombie-firms|zombie firms]], [[concepts/natural-vs-neutral-interest-rate|natural vs neutral rate]]) and [[sources/huertadesoto-2006-money-bank-credit|Huerta de Soto 2006]] ([[concepts/austrian-business-cycle-theory|ABCT]], [[concepts/fractional-reserve-banking|fractional-reserve banking]]). Crisis-prediction econometrics in [[sources/babecky-2013-leading-indicators-crisis-incidence|Babecky et al. 2013]]/[[sources/babecky-2014-developed-country-crisis-ewi|2014]] ([[concepts/credit-to-gdp-gap|credit-to-GDP gap]], [[concepts/bayesian-model-averaging|BMA]], [[concepts/panel-vector-autoregression|panel VAR]]); the trader-memoir [[sources/lancaster-2021-fed-up|Fed Up]]. Hub [4].

[207] **Systematic trading, factor investing & alpha research** — Ilmanen's risk-premia canon [[sources/ilmanen-2011-expected-returns|Expected Returns]] / [[sources/ilmanen-2022-investing-amid-low-expected-returns|Investing Amid Low Expected Returns]] ([[concepts/risk-premia|risk premia]], [[concepts/style-premia|style premia]], [[concepts/low-expected-returns|the low-return challenge]]); Carver's systematic frameworks [[sources/carver-2015-systematic-trading|Systematic Trading]] / [[sources/carver-2023-advanced-futures-trading-strategies|Advanced Futures]] ([[concepts/volatility-targeting|volatility targeting]], [[concepts/trend-following|trend following]], [[concepts/futures-carry|carry]]); [[sources/pardo-2008-evaluation-optimization-trading-strategies|Pardo's walk-forward analysis]] and [[sources/tulchinsky-2020-finding-alphas|WorldQuant's alpha research]] ([[concepts/the-unrule|the UnRule]], [[concepts/overfitting-in-alpha-research|overfitting]]). The author's own [[sources/koukorinis-2024-xantium-business-plan|Xantium plan]] and [[sources/ahmad-2014-alaph-liquid-macro-credit-fund|Alaph fund]] center [[concepts/etf-creation-redemption-arbitrage|ETF create/redeem arbitrage]] and [[concepts/credit-relative-value|credit relative value]]. Hub [4].

[208] **Causal inference & the philosophy of causation** — A spectrum from applied to metaphysical: [[sources/pearl-2018-book-of-why|Pearl's Book of Why]] ([[concepts/ladder-of-causation|ladder of causation]], [[concepts/do-operator|do-calculus]], [[concepts/causal-diagram|DAGs]]), the [[sources/hernan-2020-causal-inference-what-if|Hernán-Robins]] textbook ([[concepts/potential-outcomes|potential outcomes]], [[concepts/g-methods-time-varying-treatments|g-methods]]), [[sources/angrist-2009-mostly-harmless-econometrics|Angrist-Pischke]] ([[concepts/instrumental-variables|IV]], [[concepts/difference-in-differences|diff-in-diff]], [[concepts/regression-discontinuity|RD]]), [[sources/vanderweele-2015-explanation-causal-inference|VanderWeele]] ([[concepts/mediation-analysis|mediation]]), and the philosophers [[sources/salmon-1998-causality-and-explanation|Salmon]], [[sources/tooley-1997-time-tense-causation|Tooley]], [[sources/schulz-counterfactuals-and-probability|Schulz]]. Extends existing [[concepts/causal-inference|causal inference]] and [[concepts/double-machine-learning|DML]]. Hub [4]. **Assumption-testing sub-cluster** (causality-testing corpus): [[sources/cai-2023-testing-conditional-independence-time-series|Cai 2023]] tests the [[concepts/unconfoundedness-assumption|unconfoundedness]]/[[concepts/conditional-independence-test|CI assumption]] via auxiliary variables; [[sources/hill-2011-bart-causal-inference|Hill 2011]] estimates under it with [[concepts/bayesian-additive-regression-trees|BART]]; [[sources/gentzel-2021-osrct-evaluation|Gentzel 2021]] evaluates estimators via [[concepts/observational-sampling-from-rcts|OSRCT]]; [[sources/hudson-2019-its-healthcare-reporting|Hudson 2019]] substitutes the [[concepts/interrupted-time-series-design|interrupted-time-series]] design. Syntheses: [[analyses/testing-unconfoundedness-vs-g-methods-identifiability]] and [[analyses/credit-spread-determinants-causal-reading]].

[209] **Probabilistic forecasting & scoring rules** — [[sources/gneiting-2007-strictly-proper-scoring-rules|Gneiting-Raftery 2007]] is the anchor: [[concepts/strictly-proper-scoring-rules|strictly proper scoring rules]], the [[concepts/continuous-ranked-probability-score|CRPS]], [[concepts/energy-score|energy score]], [[concepts/logarithmic-score|log score]], [[concepts/tick-loss|pinball loss]], and [[concepts/optimum-score-estimation|optimum-score estimation]]. [[sources/ziel-2019-multivariate-forecasting-evaluation|Ziel-Berk 2019]] extends to the multivariate case ([[concepts/marginal-copula-score|marginal-copula scores]], the [[concepts/diebold-mariano-test|Diebold-Mariano test]]). Bayesian forecasting discipline in [[sources/mauboussin-2026-bayes-base-rates|Mauboussin's base-rates note]] ([[concepts/base-rates-reference-class-forecasting|reference-class forecasting]]). Ties to the conformal-prediction core via [[concepts/calibration|calibration]] and [[concepts/quantile-regression|quantile regression]]. Hub [4].

[210] **Systems thinking & recursive macro** — Meadows' [[sources/meadows-2008-thinking-in-systems|Thinking in Systems]] ([[concepts/systems-thinking|systems thinking]], [[concepts/stocks-and-flows|stocks and flows]], [[concepts/feedback-loops|feedback loops]], [[concepts/leverage-points|leverage points]]) and Dawson's popular companion; the graduate canon in [[sources/ljungqvist-2012-recursive-macroeconomic-theory|Ljungqvist-Sargent]] ([[concepts/recursive-methods-dynamic-programming|recursive methods]], [[concepts/recursive-contracts|recursive contracts]], [[concepts/ramsey-optimal-taxation|Ramsey taxation]]); algorithmic-trading methods in [[sources/halls-moore-advanced-algorithmic-trading|Halls-Moore]] ([[concepts/hidden-markov-models|HMM regime detection]], [[concepts/kalman-filter|Kalman-filter]] pairs trading). Hub [4].

[211] **Morgan Stanley & sell-side credit/macro research archive (2008-2026)** — A 107-note dealer-research archive ingested 2026-06-09, dominated by [[entities/morgan-stanley|Morgan Stanley]] desks (one [[entities/deutsche-bank|Deutsche Bank]] equity-strategy note). Threads: Cross-Asset Strategy playbooks & "Global In the Flow" flow notes (Sheets/Naraparaju/Tang) on [[concepts/cross-asset-rotation|cross-asset rotation]] and [[concepts/global-tactical-asset-allocation|tactical allocation]]; US/European rates strategy (Hornbach) on [[concepts/government-bond-spreads|government bonds]] and [[concepts/term-structure-risk-premium|term premia]]; European credit & bank-capital (Sankaran) introducing [[concepts/corporate-hybrid-bonds|corporate hybrids]], [[concepts/additional-tier-1-capital|AT1]] and [[concepts/bank-capital-structure-seniority|capital-structure seniority]]; EM FX quant (Jaime) with [[concepts/regime-switching-models|regime-switching models]] and [[concepts/volatility-risk-premia|vol risk premia]]; and 2020 COVID-era cross-asset/vol notes. Reuses the existing credit/macro concept graph (only 24 new concepts across 107 notes); routes into hubs [2] and [205]-[206]. Many short dated notes - use `grep "ms-20"` over `wiki/wiki/sources/` to list them.

*Last updated: 2026-06-09 | Total nodes: 211 | Coverage: 300 sources, 531 entities, 668 concepts, 7 analyses | Causality-testing sub-cluster (4 sources) + 3 analyses (credit-spread causal reading, credit-universe topology, unconfoundedness-vs-g-methods) added 2026-06-09; Morgan Stanley archive [211] (107) + Credit & Macro branch [203]-[210] (46) added 2026-06-09; earlier branches see git history*
