# ML Research Wiki - Mind Map

*A grep-friendly knowledge graph. Each node is one line with embedded [N] cross-references.*

---

## Routing Hubs (Nodes 1-5)

[1] **Overview** - This wiki covers machine learning research with two major themes: Transformers/attention mechanisms [2] and Conformal Prediction for uncertainty quantification [3]. Key researchers include Vaswani [10], Vovk [11], Zaffran [12], and Candès [13]. The wiki synthesizes knowledge from academic papers and PhD theses to build a connected understanding of modern ML uncertainty methods.

[2] **Transformers** - Neural network architecture research centered on the attention mechanism [6]. The foundational paper "Attention Is All You Need" [14] introduced self-attention [7] and the Transformer architecture, revolutionizing NLP and beyond. Key entity: Ashish Vaswani [10].

[3] **Conformal Prediction** - Distribution-free framework for uncertainty quantification [8] providing prediction intervals [9] with finite-sample coverage guarantees [17]. Core concept pages: conformal prediction [15], split conformal [16], adaptive conformal inference [19]. Founded by Vladimir Vovk [11]. Recent advances by Zaffran [12] extend to time series.

[4] **Sources** - Ingested documents include: Attention paper [14], Zaffran PhD thesis [20], ACI paper [21], multi-output regression [22], review paper [23], functional anomaly detection [24]. Total: 6 source summaries covering transformers and conformal prediction.

[5] **Entities** - Key researchers: Ashish Vaswani [10] (Transformers), Vladimir Vovk [11] (CP founder), Margaux Zaffran [12] (time series CP), Emmanuel Candès [13] (ACI). Total: 4 entity pages.

---

## Concepts (Nodes 6-19)

[6] **Attention Mechanism** - See self-attention [7]. The core innovation enabling Transformers [2] to process sequences by computing relevance scores between all positions simultaneously.

[7] **Self-Attention** - Mechanism allowing each position in a sequence to attend to all other positions, computing weighted combinations based on query-key-value projections. Foundation of Transformers [2]. Introduced in [14].

[8] **Uncertainty Quantification** - The science of quantifying prediction confidence. Methods include Bayesian approaches, ensembles, and conformal prediction [15]. Critical for high-stakes applications: medical diagnosis, autonomous systems, energy forecasting.

[9] **Prediction Intervals** - Ranges containing future observations with specified probability. Constructed via conformal prediction [15] with coverage guarantees [17]. Key for decision-making under uncertainty [8].

[15] **Conformal Prediction (Core)** - Framework providing finite-sample, distribution-free prediction sets. Requires only exchangeability [18]. Variants: split conformal [16], full conformal, cross-conformal. Founded by Vovk [11].

[16] **Split Conformal Prediction** - Efficient variant of [15] splitting data into training and calibration sets. Trades statistical efficiency for computational efficiency. Model-agnostic, finite-sample valid.

[17] **Coverage Guarantee** - Property that prediction sets contain true value with probability ≥ 1-α. Marginal coverage is what conformal prediction [15] provides. Stronger conditional coverage is generally impossible distribution-free.

[18] **Exchangeability** - Probabilistic assumption: joint distribution invariant to permutation. Weaker than i.i.d. Key assumption for conformal prediction [15]. Violated by time series, motivating ACI [19].

[19] **Adaptive Conformal Inference** - Extension of [15] for time series and distribution shift. Adaptively updates miscoverage rate based on recent performance. AgACI [21] eliminates learning rate tuning. Developed by Gibbs & Candès [13], analyzed by Zaffran [12].

---

## Entities (Nodes 10-13)

[10] **Ashish Vaswani** - First author of "Attention Is All You Need" [14]. Introduced Transformer architecture [2] and self-attention mechanism [7] at Google Brain.

[11] **Vladimir Vovk** - Professor at Royal Holloway, founder of conformal prediction [15] with Gammerman and Shafer. Author of "Algorithmic Learning in a Random World."

[12] **Margaux Zaffran** - PhD on uncertainty quantification [8] for electricity forecasting using conformal prediction [15]. Developed AgACI [21], proved CP validity with missing data [20].

[13] **Emmanuel Candès** - Stanford professor. With Gibbs, introduced Adaptive Conformal Inference [19]. Also known for compressed sensing and matrix completion.

---

## Sources (Nodes 14, 20-24)

[14] **Attention Is All You Need** - Vaswani et al. (2017). Introduced Transformers [2] and self-attention [7]. Foundational paper for modern NLP and beyond.

[20] **Zaffran PhD Thesis** - "Post-hoc predictive uncertainty quantification" (2024). Covers ACI [19] for time series, conformal prediction with missing data. Applications to electricity forecasting.

[21] **ACI Paper** - Zaffran et al. (2022). Analyzed Adaptive Conformal Inference [19] for time series. Introduced AgACI (parameter-free aggregation method).

[22] **Multi-Output Regression** - Johnstone & Ndiaye (2025). Exact and approximate conformal inference [15] for multivariate responses. Methods: rootCP, unionCP.

[23] **Review Paper** - Bao et al. (2025). Comprehensive survey of univariate conformal regression methods. Benchmarks 8 methods on 12 datasets.

[24] **Functional Anomaly Detection** - Adams et al. (2025). Conformal anomaly detection for functional data using elastic distance metrics.

---

*Last updated: 2026-04-10 | Total nodes: 24 | Coverage: 6 sources, 4 entities, 10 concepts*
