# Open Questions — Triage Sheet

Harvested from the `## Questions Raised` section of 104 source pages (355 questions, no duplicates).

**How to use this:** tick a box to claim a question, or delete the line to kill it. Clusters are ordered by how paper-shaped I judge them to be, most promising first.

| Cluster                                                      | Count |     |
| ------------------------------------------------------------ | ----- | --- |
| Conformal prediction under dependence and distribution shift | 26    |     |
| Unresolved design and hyperparameter choices in CP           | 18    |     |
| Conditional vs marginal coverage                             | 13    |     |
| Nonconformity score design                                   | 11    |     |
| Extending CP to new data types                               | 20    |     |
| Bound tightness and theory gaps                              | 16    |     |
| Causal identification and untestable assumptions             | 16    |     |
| Evaluating causal methods and study designs                  | 14    |     |
| Credit spreads and equity-credit integration                 | 9     |     |
| Proper scoring rules and forecast evaluation                 | 6     |     |
| Crisis early warning and real-time estimation                | 9     |     |
| Systematic trading: overfitting, costs, capacity             | 34    |     |
| AI / LLM engineering practice                                | 85    |     |
| Monetary policy and macro theory                             | 25    |     |
| AI capex, private credit and the 2026 cycle                  | 13    |     |
| Morgan Stanley / Citi tactical archive                       | 16    |     |
| Philosophy of causation, time and counterfactuals            | 9     |     |
| Statistical and systems reasoning                            | 12    |     |
| Broken extractions — not questions                           | 3     |     |

---

## Conformal prediction under dependence and distribution shift  (26)

**Your home turf, and the densest cluster.** Twelve independent author teams flag the same hole: guarantees assume exchangeability, real data does not supply it. This is where a paper lives.

- [ ] **Q10** How does LTT degrade under distribution shift or non-exchangeable calibration data?  — [[angelopoulos-2021-learn-then-test]]
- [ ] **Q14** How does RAPS interact with distribution shift (e.g., ImageNet → ImageNet-V2 gap) when exchangeability fails?  — [[angelopoulos-2021-raps]]
- [ ] **Q17** How should weights be designed for [[concepts/weighted-conformal-prediction|weighted CP]] under unknown or hard-to-estimate distribution drift, given the variance penalty of small effective sample size?  — [[angelopoulos-2022-gentle-intro]]
- [ ] **Q21** Can a local / windowed integrator avoid late-sequence oscillation when global integrator marginal coverage stays near 1−α despite local drift?  — [[angelopoulos-2023-conformal-pid]]
- [ ] **Q50** How does CV+ behave under non-exchangeable data (distribution shift, time series)? Partially addressed by [[sources/barber-2023-beyond-exchangeability]].  — [[barber-2021-jackknife-plus]]
- [ ] **Q51** How should weights `w_i` be chosen adaptively in practice without violating the fixed-weight assumption?  — [[barber-2023-beyond-exchangeability]]
- [ ] **Q52** Can the residual-level TV bound be estimated empirically to give actionable coverage diagnostics?  — [[barber-2023-beyond-exchangeability]]
- [ ] **Q53** How does NexCP compare to ACI / AgACI / online conformal in finite-sample regimes under abrupt vs gradual drift?  — [[barber-2023-beyond-exchangeability]]
- [ ] **Q54** Can the bound be tightened under specific dependence structures (e.g., β-mixing time series)?  — [[barber-2023-beyond-exchangeability]]
- [ ] **Q62** What happens when exchangeability between calibration and test data fails (covariate shift, label shift, time-series dependence)?  — [[bates-2021-rcps]]
- [ ] **Q115** Under what non-stationarity regimes does ACI outperform OSSCP-horizon, and vice versa?  — [[dieuleveut-zaffran-2025-cp-tutorial]]
- [ ] **Q136** How does ACI behave when the conformity score itself (not just the marginal distribution) drifts?  — [[gibbs-2021-aci]]
- [ ] **Q137** Does combining ACI with feedback-control or PID-style updates yield better finite-sample local coverage? (Answered in the affirmative by [[sources/angelopoulos-2023-conformal-pid|Angelopoulos-Candès-Tibshirani 2023]].)  — [[gibbs-2021-aci]]
- [ ] **Q191** How does J+aB extend to non-exchangeable data? (Addressed by [[sources/xu-2023-enbpi|EnbPI]] and [[sources/xu-2022-spci|SPCI]].)  — [[kim-2020-jackknife-plus-after-bootstrap]]
- [ ] **Q271** How does CQR perform under covariate shift or distribution shift where exchangeability fails?  — [[romano-2019-cqr]]
- [ ] **Q292** How should one diagnose and quantify the practical impact of non-exchangeability before trusting an advertised 1−ε coverage level?  — [[shafer-2007-cp-tutorial]]
- [ ] **Q293** When non-exchangeability is detected, which on-line compression model (Mondrian, exchangeability-within-label, Gaussian linear) is the right relaxation for a given application?  — [[shafer-2007-cp-tutorial]]
- [ ] **Q294** Under what conditions does on-line conformal prediction extend cleanly to dependent / time-series data where neither exchangeability nor a known compression structure holds?  — [[shafer-2007-cp-tutorial]]
- [ ] **Q298** How does empirical performance change when the base forecaster is itself adaptive (re-trained ARIMA, neural sequence models) rather than a frozen AR-LS?  — [[stocker-2025-conformal-timeseries-intro]]
- [ ] **Q300** How do the four families behave under strong seasonality, [[concepts/long-memory|long memory]], locally-stationary, and genuinely non-stationary processes — and under multi-step-ahead horizons?  — [[stocker-2025-conformal-timeseries-intro]]
- [ ] **Q314** How accurately must `w` be estimated for finite-sample coverage to remain near nominal, and what is the price of mis-specified weights?  — [[tibshirani-2019-covariate-shift]]
- [ ] **Q315** Can the weighted-exchangeability framework be extended to label shift, concept drift, or general joint-distribution shift where `Y|X` also changes?  — [[tibshirani-2019-covariate-shift]]
- [ ] **Q336** How do EnbPI's coverage guarantees degrade as the β-mixing rate slows toward [[concepts/long-memory|long-memory]] behaviour?  — [[xu-2023-enbpi]]
- [ ] **Q337** Can EnbPI be combined with online adaptive-α updates ([[concepts/adaptive-conformal-inference|ACI]]) for abrupt-shift robustness without sacrificing interval width?  — [[xu-2023-enbpi]]
- [ ] **Q343** What happens when sources have significant overlap vs. separation?  — [[yang-2026-multi-distribution-robust-cp]]
- [ ] **Q346** How can CP move beyond bounding the coverage gap (as in non-exchangeable CP) to *adaptively minimise* it under heterogeneity and temporal dependence?  — [[zhou-2025-cp-data-perspective]]

## Unresolved design and hyperparameter choices in CP  (18)

Eighteen variants of "how should this constant be chosen?" — gamma, K folds, calibration-set size, window length, |I|=500. Individually each is a footnote. **Collectively they are one paper:** learn the hyperparameters online instead of tuning them ex ante. Nobody in the corpus has done it.

- [ ] **Q8** How should the parameter grid `Λ` be discretised in high dimensions without sacrificing statistical efficiency?  — [[angelopoulos-2021-learn-then-test]]
- [ ] **Q9** How is the fixed-sequence ordering or graph structure for SGT chosen in a data-driven yet valid way when no natural ordering exists?  — [[angelopoulos-2021-learn-then-test]]
- [ ] **Q12** How should `k_reg` and `λ` be chosen adaptively per dataset/classifier beyond the heuristic in Appendix E?  — [[angelopoulos-2021-raps]]
- [ ] **Q15** Can RAPS be combined with calibration alternatives beyond Platt / temperature scaling?  — [[angelopoulos-2021-raps]]
- [ ] **Q19** What is the right computational/statistical trade-off between [[concepts/split-conformal-prediction|split]], [[concepts/cross-conformal-prediction|cross-conformal / CV+ / Jackknife+]], and [[concepts/full-conformal-prediction|full]] CP in modern deep-learning workflows?  — [[angelopoulos-2022-gentle-intro]]
- [ ] **Q20** How should integrator constants (`C_sat`, `K_I`) and learning rates be set principled rather than heuristically?  — [[angelopoulos-2023-conformal-pid]]
- [ ] **Q117** Is pointwise stable selection among conformal sets compatible with online aggregation schemes (Gasparin & Ramdas 2024)?  — [[dieuleveut-zaffran-2025-cp-tutorial]]
- [ ] **Q126** How should a Mondrian taxonomy be chosen? The "problem of the reference class" (categories large enough for stable sample-size estimates vs small enough for informative conditioning) lacks a principled solution.  — [[fontana-2023-cp-unified-review]]
- [ ] **Q127** How should the calibration-set size be chosen in inductive CP? Heuristics suggest 15-33% of the data with at least a few hundred examples; the bias-variance trade-off is unresolved.  — [[fontana-2023-cp-unified-review]]
- [ ] **Q134** How should `γ` be chosen adaptively from data rather than fixed a priori? (Addressed by [[sources/zaffran-2022-aci|AgACI]] and [[sources/gibbs-2024-online-aci|DtACI]].)  — [[gibbs-2021-aci]]
- [ ] **Q138** How should one choose the function class `F` and its regularisation in practice?  — [[gibbs-2023-conditional-guarantees]]
- [ ] **Q142** Sensitivity to the heuristic `|I| = 500` choice across application domains is not characterised.  — [[gibbs-2024-online-aci]]
- [ ] **Q192** What is the optimal choice of `B` and `m` for finite-sample efficiency?  — [[kim-2020-jackknife-plus-after-bootstrap]]
- [ ] **Q274** What is the optimal split ratio between proper training set and calibration set?  — [[romano-2019-cqr]]
- [ ] **Q302** Can hyperparameters (γ for ACI, ρ for WCP, refresh-rate `s` for EnbPI, block size `B` for BCP) be learned online rather than tuned ex ante?  — [[stocker-2025-conformal-timeseries-intro]]
- [ ] **Q328** What is the optimal number of folds K, and how does this depend on the learning curve of the underlying algorithm?  — [[vovk-2012-cross-conformal]]
- [ ] **Q338** How should sliding-window length and bootstrap count `B` be chosen as functions of dependence strength and sample size?  — [[xu-2023-enbpi]]
- [ ] **Q345** Optimal aggregation strategies for expert combination?  — [[zaffran-2022-aci]]

## Conditional vs marginal coverage  (13)

The impossibility frontier. Lei-Wasserman and Barber et al. proved exact conditional coverage is unreachable distribution-free, so every question here is really *what is the best achievable approximation*. Crowded but unresolved.

- [ ] **Q13** Can the regularization idea be extended beyond marginal coverage to class-conditional or group-conditional coverage?  — [[angelopoulos-2021-raps]]
- [ ] **Q16** When exact [[concepts/conditional-coverage|conditional coverage]] is impossible without distributional assumptions, what is the right notion of *approximate* conditional validity (size-stratified, group-balanced, multivalid) for high-stakes deployments?  — [[angelopoulos-2022-gentle-intro]]
- [ ] **Q23** Does the deterministic long-run guarantee extend to conditional-coverage notions without losing the assumption-free property?  — [[angelopoulos-2023-conformal-pid]]
- [ ] **Q105** What is the finite-sample loss in conditional coverage?  — [[chernozhukov-2021-distributional-cp]]
- [ ] **Q128** How can object-conditional validity be achieved in any nontrivial finite-sample sense, given the Lei-Wasserman / Barber et al. impossibility results? CQR and Mondrian predictors are partial answers but not complete ones.  — [[fontana-2023-cp-unified-review]]
- [ ] **Q135** Can the `α_t` recursion be replaced by a multi-parameter or quantile-tracking scheme that achieves conditional rather than marginal coverage?  — [[gibbs-2021-aci]]
- [ ] **Q139** What is the trade-off between richness of `F` (broader coverage guarantees) and the loss of exactness in finite samples?  — [[gibbs-2023-conditional-guarantees]]
- [ ] **Q193** Can J+aB be combined with conditional-coverage methods (CQR, Mondrian) while preserving the cost-free property?  — [[kim-2020-jackknife-plus-after-bootstrap]]
- [ ] **Q203** How tight can conformal intervals be made under conditional (rather than marginal) coverage targets in regression?  — [[lei-2018-distribution-free-regression]]
- [ ] **Q273** How does CQR interact with conditional coverage — does adaptivity translate into approximate conditional validity?  — [[romano-2019-cqr]]
- [ ] **Q278** What is the gap between APS's worst-slice conditional coverage and true conditional coverage as the number of classes `C` grows large?  — [[romano-2020-aps]]
- [ ] **Q339** Does the conditional-coverage guarantee extend uniformly over covariate space, or only on-average within conditioning sets?  — [[xu-2023-enbpi]]
- [ ] **Q347** Can ACI-style adversarial-coverage methods be augmented with light distributional assumptions to recover per-step validity rather than only long-run adversarial guarantees?  — [[zhou-2025-cp-data-perspective]]

## Nonconformity score design  (11)

Scores are still hand-designed. Several authors ask whether they can be learned or made locally adaptive without breaking finite-sample validity. Tractable, and adjacent to CP-TUNE.

- [ ] **Q18** Can [[concepts/nonconformity-score|nonconformity scores]] be *learned* (rather than hand-designed) to optimise adaptivity, set size, or risk-control objectives without sacrificing finite-sample validity?  — [[angelopoulos-2022-gentle-intro]]
- [ ] **Q22** How to design scorecasters that avoid injecting variance on near-i.i.d. score sequences (automatic gating between reactive and forward-looking modes)?  — [[angelopoulos-2023-conformal-pid]]
- [ ] **Q124** Should the i-th example be included in or excluded from the bag against which its nonconformity score is computed, to maximise efficiency? Fontana labels this "an object of further future investigation".  — [[fontana-2023-cp-unified-review]]
- [ ] **Q204** What is the optimal way to estimate the local scale `σ(x)` for locally-adaptive conformal regression?  — [[lei-2018-distribution-free-regression]]
- [ ] **Q272** Can the symmetric two-sided conformity score be replaced with asymmetric per-tail scores for improved efficiency?  — [[romano-2019-cqr]]
- [ ] **Q275** How sensitive is interval efficiency to the quality of the underlying quantile estimator?  — [[romano-2019-cqr]]
- [ ] **Q276** How does APS perform when the base classifier's probability estimates are systematically biased or poorly calibrated (e.g., overconfident deep networks)?  — [[romano-2020-aps]]
- [ ] **Q277** Can the randomized tie-breaking through `Uniform(0, 1)` variables be avoided or derandomized without sacrificing efficiency?  — [[romano-2020-aps]]
- [ ] **Q299** Can sharper, locally-adaptive [[concepts/nonconformity-score|nonconformity scores]] recover asymptotic conditional validity for time series?  — [[stocker-2025-conformal-timeseries-intro]]
- [ ] **Q316** How does the effective-sample-size penalty interact with adaptive nonconformity scores (CQR, locally weighted residuals)?  — [[tibshirani-2019-covariate-shift]]
- [ ] **Q340** Can the bootstrap-LOO trick generalise to non-residual scores (quantile-based, density-ratio-based) while preserving the guarantees?  — [[xu-2023-enbpi]]

## Extending CP to new data types  (20)

Multivariate, functional, graph, multimodal, LLM-scale, continuous treatments. Land-grab territory — cheap to claim, and Q199 is your own open thread.

- [ ] **Q11** What is the right way to extend LTT to online or sequential decision-making settings?  — [[angelopoulos-2021-learn-then-test]]
- [ ] **Q61** Can UCB calibration be extended to non-monotone losses or multi-dimensional risk vectors?  — [[bates-2021-rcps]]
- [ ] **Q64** Can RCPS be combined with online / sequential calibration so that `λ` is updated as new labelled data arrives?  — [[bates-2021-rcps]]
- [ ] **Q103** How does DCP perform with high-dimensional predictors?  — [[chernozhukov-2021-distributional-cp]]
- [ ] **Q104** Can the method be extended to multivariate responses?  — [[chernozhukov-2021-distributional-cp]]
- [ ] **Q116** Can CP-MDA-Nested–style [[concepts/mask-conditional-validity|mask-conditional validity]] be extended beyond MCAR/MAR assumptions?  — [[dieuleveut-zaffran-2025-cp-tutorial]]
- [ ] **Q129** How should CP be extended to functional data so simultaneous bands are both finite-sample valid and tight?  — [[fontana-2023-cp-unified-review]]
- [ ] **Q199** Extension to continuous treatments?  — [[koukorinis-2026-draci]]
- [ ] **Q206** How does LOCO-based variable importance compare to selective-inference and debiased-lasso confidence intervals in practice?  — [[lei-2018-distribution-free-regression]]
- [ ] **Q279** Could the generalized inverse quantile conformity score principle extend beyond classification to structured prediction or multi-label settings?  — [[romano-2020-aps]]
- [ ] **Q301** How should the taxonomy extend to multivariate and functional time series?  — [[stocker-2025-conformal-timeseries-intro]]
- [ ] **Q303** How should conformal forecasting be extended from intervals to full [[concepts/distributional-conformal-prediction|distributional forecasting]]?  — [[stocker-2025-conformal-timeseries-intro]]
- [ ] **Q330** How does CCP behave on regression and multi-class classification, beyond the binary Spambase setting?  — [[vovk-2012-cross-conformal]]
- [ ] **Q342** Can the method handle sources with different feature spaces?  — [[yang-2026-multi-distribution-robust-cp]]
- [ ] **Q344** How to extend to multivariate time series?  — [[zaffran-2022-aci]]
- [ ] **Q348** What is the right framework for CP under block-wise or non-random missingness, beyond MAR assumptions?  — [[zhou-2025-cp-data-perspective]]
- [ ] **Q349** How should multi-modal data (text + image + sensor) be optimally aggregated to enhance CP performance, especially under per-modality covariate shift?  — [[zhou-2025-cp-data-perspective]]
- [ ] **Q350** How can CP for graphs leverage richer structural signals beyond local neighborhoods (similar-degree nodes, shared topological properties, weighted edges)?  — [[zhou-2025-cp-data-perspective]]
- [ ] **Q351** Can CP techniques be made computationally efficient at LLM-scale, particularly with FAISS-style retrieval and unbounded generative output spaces?  — [[zhou-2025-cp-data-perspective]]
- [ ] **Q352** How can CP serve as effective side information for human-in-the-loop decision-making across more domains than medical triage?  — [[zhou-2025-cp-data-perspective]]

## Bound tightness and theory gaps  (16)

Mostly "can the factor of 2 be removed" and "can this bound be sharpened". High skill, narrow payoff, easy to get scooped. Includes two of your own DR-ACI threads (Q197, Q198).

- [ ] **Q48** Can the K-fold CV+ coverage bound be sharpened beyond 1 − 2α − √(2/n)?  — [[barber-2021-jackknife-plus]]
- [ ] **Q49** Can the factor of 2 in the 1−2α bound be removed under intermediate stability assumptions weaker than full in-sample stability?  — [[barber-2021-jackknife-plus]]
- [ ] **Q60** How can the (α, δ) PAC-style guarantee be tightened to a marginal expected-risk guarantee that holds in expectation over the calibration set?  — [[bates-2021-rcps]]
- [ ] **Q63** How tight are the Waudby-Smith-Ramdas bounds in finite samples for very small `α` or very imbalanced losses?  — [[bates-2021-rcps]]
- [ ] **Q114** How tight are PAC-style calibration-conditional bounds in realistic sample sizes?  — [[dieuleveut-zaffran-2025-cp-tutorial]]
- [ ] **Q125** Are transductive (full) conformal predictors systematically more efficient than inductive ones? Linusson et al. (2014b) and Papadopoulos (2008) cast doubt on the conventional wisdom; "still open".  — [[fontana-2023-cp-unified-review]]
- [ ] **Q140** How does computational cost scale with `dim(F)` for the augmented quantile regression?  — [[gibbs-2023-conditional-guarantees]]
- [ ] **Q141** DtACI may produce small bias in long-run coverage with constant `η, σ`. A rigorous bound is not given.  — [[gibbs-2024-online-aci]]
- [ ] **Q190** Can the `1 − 2α` bound be tightened to `1 − α` under mild additional assumptions on the aggregator `φ`?  — [[kim-2020-jackknife-plus-after-bootstrap]]
- [ ] **Q197** Can the switch coefficient bound be tightened? (Empirical coverage exceeds theory at ρ=0.99)  — [[koukorinis-2026-draci]]
- [ ] **Q198** Formal efficiency bounds for VS-DR-ACI?  — [[koukorinis-2026-draci]]
- [ ] **Q205** Can the jackknife approach be salvaged with weaker stability conditions, or is split conformal strictly preferred in high dimensions?  — [[lei-2018-distribution-free-regression]]
- [ ] **Q317** What are the theoretical guarantees when the density-ratio classifier is trained on overlapping data, raising potential leakage concerns?  — [[tibshirani-2019-covariate-shift]]
- [ ] **Q327** Can theoretical validity guarantees (e.g., marginal coverage bounds) be established for cross-conformal predictors, as they are for ICP via Proposition 1? *Vovk's explicit open problem in Section 4.* (Partially addressed by Barber et al. 2021 for the closely-related Jackknife+ / CV+.)  — [[vovk-2012-cross-conformal]]
- [ ] **Q329** Why exactly does p-value averaging yield well-calibrated combined p-values despite the per-fold p-values being dependent — what is the precise dependency structure?  — [[vovk-2012-cross-conformal]]
- [ ] **Q341** How does efficiency scale with the number of sources K?  — [[yang-2026-multi-distribution-robust-cp]]

## Causal identification and untestable assumptions  (16)

One theme repeats: the key assumption (unconfoundedness, consistency, no exposure-induced confounding) cannot be verified from data. Connects directly to your causality-testing sources.

- [ ] **Q24** When is the conditional independence assumption defensible in observational data?  — [[angrist-2009-mostly-harmless-econometrics]]
- [ ] **Q25** How should one interpret and generalize LATE when compliers differ from the population of interest?  — [[angrist-2009-mostly-harmless-econometrics]]
- [ ] **Q26** How can the common-trends assumption underlying differences-in-differences be assessed or relaxed?  — [[angrist-2009-mostly-harmless-econometrics]]
- [ ] **Q88** How should valid auxiliary variables A_t be selected in practice? The authors note there is no general guideline and selection may need to be done case by case, and the testing power may depend on this choice.  — [[cai-2023-testing-conditional-independence-time-series]]
- [ ] **Q89** If practitioners choose auxiliary variables that do not satisfy Assumption 2, the test tends to reject CI even when CI is true; how can the validity of candidate auxiliary variables be assessed?  — [[cai-2023-testing-conditional-independence-time-series]]
- [ ] **Q90** How can the dimensionality problem be addressed in the general case where the policy choice is multinomial (not binary)?  — [[cai-2023-testing-conditional-independence-time-series]]
- [ ] **Q91** Can alternative test constructions, such as the Durbin-Wu-Hausman type (Donald et al. 2014) or Kolmogorov-Smirnov type (Chen et al. 2018) statistics, be extended to the time series setting?  — [[cai-2023-testing-conditional-independence-time-series]]
- [ ] **Q155** How can the no-unmeasured-confounding (exchangeability) assumption be empirically verified rather than assumed?  — [[hernan-2020-causal-inference-what-if]]
- [ ] **Q156** How should the bias-variance trade-off be managed when high-dimensional confounders require flexible models?  — [[hernan-2020-causal-inference-what-if]]
- [ ] **Q157** How can well-defined interventions (consistency) be specified for vague or compound exposures?  — [[hernan-2020-causal-inference-what-if]]
- [ ] **Q258** How can a machine acquire the causal diagram itself, rather than having it supplied by a human modeler?  — [[pearl-2018-book-of-why]]
- [ ] **Q259** When can a causal effect not identifiable by back-door adjustment still be recovered through front-door adjustment or instrumental variables?  — [[pearl-2018-book-of-why]]
- [ ] **Q260** What architecture would let deep-learning systems climb from association to intervention and counterfactual reasoning?  — [[pearl-2018-book-of-why]]
- [ ] **Q324** How can mediation methods be made robust when the no-exposure-induced-confounding assumption is violated?  — [[vanderweele-2015-explanation-causal-inference]]
- [ ] **Q325** How can the counterfactual framework be synthesized with less formal social-science mediation methods?  — [[vanderweele-2015-explanation-causal-inference]]
- [ ] **Q326** What are the limits of inferring biological/mechanistic interaction from observational statistical interaction?  — [[vanderweele-2015-explanation-causal-inference]]

## Evaluating causal methods and study designs  (14)

How do you benchmark a causal estimator when ground truth is unavailable? Plus ITS design and reporting. Methodologically useful, less paper-shaped.

- [ ] **Q130** Would a more complex biasing function using many covariates make RCT-based evaluation results match the high between-method variability seen on synthetic-response data?  — [[gentzel-2021-osrct-evaluation]]
- [ ] **Q131** How representative is method performance on RCT-derived data of performance on the actual observational populations of interest, given that RCTs are conducted in settings where randomization and measurement are feasible?  — [[gentzel-2021-osrct-evaluation]]
- [ ] **Q132** How would individual causal inference methods perform under careful hyperparameter tuning rather than default settings, especially the neural-network method that showed high variability at small sample sizes?  — [[gentzel-2021-osrct-evaluation]]
- [ ] **Q133** Can OSRCT-style evaluation be extended to induce dependence on outcome (not just treatment) or to estimands beyond the single treatment-outcome pair recoverable from an RCT?  — [[gentzel-2021-osrct-evaluation]]
- [ ] **Q158** Bayesian posterior intervals based on a proper prior may not attain desired frequentist coverage, and regularization priors can hurt coverage in regions with limited overlap—how should this trade-off be managed?  — [[hill-2011-bart-causal-inference]]
- [ ] **Q159** As specified, BART may not reliably recover response surfaces with very high-order interactions (tested only through three-way interactions); how does it behave beyond this?  — [[hill-2011-bart-causal-inference]]
- [ ] **Q160** How can regions lacking common support be reliably identified, especially in high-dimensional covariate spaces (taken up in concurrent Hill and Su 2010 work)?  — [[hill-2011-bart-causal-inference]]
- [ ] **Q161** Will BART perform as effectively as a causal inference strategy across a broader range of settings than the few scenarios tested here?  — [[hill-2011-bart-causal-inference]]
- [ ] **Q162** Sample estimands generalize to population estimands only under special conditions (e.g., additive effects); how should population inference with BART be conducted when treatment effects are heterogeneous?  — [[hill-2011-bart-causal-inference]]
- [ ] **Q163** Which ITS statistical method (segmented regression, ARIMA, GEE, change-point analysis, mixed models) should be preferred, and under what data conditions?  — [[hudson-2019-its-healthcare-reporting]]
- [ ] **Q164** How should sample size for an ITS study be justified relative to the effect size of interest (e.g. change in slope) rather than differences in proportions?  — [[hudson-2019-its-healthcare-reporting]]
- [ ] **Q165** What standardised reporting guideline should be adopted for ITS designs, and how should it be developed through consensus?  — [[hudson-2019-its-healthcare-reporting]]
- [ ] **Q166** Given the variety of relative and absolute effect estimates, how can results across ITS studies be made comparable or poolable in meta-analysis?  — [[hudson-2019-its-healthcare-reporting]]
- [ ] **Q167** Would searching multiple years or grey literature and additional databases materially change the picture of ITS use and reporting?  — [[hudson-2019-its-healthcare-reporting]]

## Credit spreads and equity-credit integration  (9)

The classic unexplained-common-factor problem. Collin-Dufresne's residual factor is still unidentified after 25 years — that is a standing invitation.

- [ ] **Q32** How sensitive are the hedge ratios to the maturity mismatch between short-dated puts and 5-year CDS contracts?  — [[avino-2024-hedging-credit-equity-options]]
- [ ] **Q33** How much of the incremental option information is genuinely option-specific versus aggregate credit/equity factors?  — [[avino-2024-hedging-credit-equity-options]]
- [ ] **Q34** How does mark-to-market hedging perform under transaction costs and wider bid-ask spreads?  — [[avino-2024-hedging-credit-equity-options]]
- [ ] **Q108** What is the economic identity of the single common systematic factor driving credit spread changes that structural models cannot capture?  — [[collin-dufresne-2001-determinants-credit-spread-changes]]
- [ ] **Q109** Could a better-measured aggregate bond-market liquidity factor explain the common residual factor?  — [[collin-dufresne-2001-determinants-credit-spread-changes]]
- [ ] **Q110** If stock and bond markets are segmented, why are they segmented?  — [[collin-dufresne-2001-determinants-credit-spread-changes]]
- [ ] **Q187** What determines cross-sectional and time-series variation in the prevalence of pricing discrepancies?  — [[kapadia-2012-limited-arbitrage-equity-credit]]
- [ ] **Q188** What are the relative roles of systematic versus firm-specific impediments to integration?  — [[kapadia-2012-limited-arbitrage-equity-credit]]
- [ ] **Q189** Over what horizons must structural credit-risk models be tested to ensure markets are integrated?  — [[kapadia-2012-limited-arbitrage-equity-credit]]

## Proper scoring rules and forecast evaluation  (6)

Small but sharp, and technically close to conformal work — scoring rules are how you would judge any interval or distributional forecast you produce.

- [ ] **Q143** What is the general form of all proper scoring rules for quantile forecasts?  — [[gneiting-2007-strictly-proper-scoring-rules]]
- [ ] **Q144** Under what conditions is a divergence function a score divergence admitting representation by a proper scoring rule?  — [[gneiting-2007-strictly-proper-scoring-rules]]
- [ ] **Q145** Do asymptotic equivalences linking the logarithmic score to Bayes factors and BIC extend to other proper scores such as the CRPS?  — [[gneiting-2007-strictly-proper-scoring-rules]]
- [ ] **Q353** Can a strict lower bound for the copula energy score be proven?  — [[ziel-2019-multivariate-forecasting-evaluation]]
- [ ] **Q354** Are there better linking functions than the multiplicative structure for combining marginal and copula scores?  — [[ziel-2019-multivariate-forecasting-evaluation]]
- [ ] **Q355** Could Wasserstein- or Hellinger-distance-based scoring rules yield useful proper scores for forecast evaluation?  — [[ziel-2019-multivariate-forecasting-evaluation]]

## Crisis early warning and real-time estimation  (9)

The real-time problem is the live one: credit-to-trend gaps and in-sample variable selection do not survive out-of-sample. Testable.

- [ ] **Q39** How would real-time usefulness differ given the crisis database benefits from hindsight?  — [[babecky-2013-leading-indicators-crisis-incidence]]
- [ ] **Q40** Could excluded indicators (regulatory capital, household credit) add predictive power?  — [[babecky-2013-leading-indicators-crisis-incidence]]
- [ ] **Q41** Does selecting lags via bivariate PVAR rather than jointly within BMA bias the selected horizons?  — [[babecky-2013-leading-indicators-crisis-incidence]]
- [ ] **Q42** How can deviations of domestic private credit from trend be reliably estimated in real time?  — [[babecky-2014-developed-country-crisis-ewi]]
- [ ] **Q43** To what extent do the relationships hold out-of-sample given in-sample variable selection?  — [[babecky-2014-developed-country-crisis-ewi]]
- [ ] **Q44** Why do developed economies show no significant feedback from currency to banking crises?  — [[babecky-2014-developed-country-crisis-ewi]]
- [ ] **Q118** What indicator can reliably forecast the recovery of the real (macro) economy?  — [[duasa-2010-predicting-crisis-recovery]]
- [ ] **Q119** How would adding demand and supply shock controls change the recovery estimates?  — [[duasa-2010-predicting-crisis-recovery]]
- [ ] **Q120** Is assuming 2008 and 1997 environments are similar sufficient to transfer half-life estimates?  — [[duasa-2010-predicting-crisis-recovery]]

## Systematic trading: overfitting, costs, capacity  (34)

Overfitting, transaction costs, crowding and capacity, asked over and over. Practically important for your own strategy work; thin as novel research.

- [ ] **Q1** How robust is the pro-forma Hutchin Hill track record once carved out and fee-adjusted?  — [[ahmad-2014-alaph-liquid-macro-credit-fund]]
- [ ] **Q2** Does the 80%-exit-in-15-20-days liquidity target hold during systemic stress?  — [[ahmad-2014-alaph-liquid-macro-credit-fund]]
- [ ] **Q3** How is theme conviction quantified and converted into the risk-allocation matrix?  — [[ahmad-2014-alaph-liquid-macro-credit-fund]]
- [ ] **Q70** Are correlations during large positive equity moves actually lower than during downturns?  — [[bhansali-2018-right-tail-hedging]]
- [ ] **Q71** How robust is the worked call example given the author acknowledges it is cherry-picked?  — [[bhansali-2018-right-tail-hedging]]
- [ ] **Q72** Can the destabilizing upside hedging feedback loop be empirically distinguished from other drivers of melt-ups?  — [[bhansali-2018-right-tail-hedging]]
- [ ] **Q95** How should forecast weights and instrument weights be chosen when only short or noisy return histories are available?  — [[carver-2015-systematic-trading]]
- [ ] **Q96** When is fully systematic forecasting preferable to a discretionary forecast placed inside the systematic framework?  — [[carver-2015-systematic-trading]]
- [ ] **Q97** How much of the diversification benefit survives realistic time-varying correlations and trading costs?  — [[carver-2015-systematic-trading]]
- [ ] **Q98** Should each asset class be traded with bespoke rules, or do common strategies generalise across all futures markets?  — [[carver-2023-advanced-futures-trading-strategies]]
- [ ] **Q99** When capital is insufficient for the full portfolio, how can dynamic optimisation approximate the diversified target?  — [[carver-2023-advanced-futures-trading-strategies]]
- [ ] **Q100** If earnings growth is essentially unpredictable beyond a year, what justifies the large dispersion in P/E multiples and analyst forecasts?  — [[chan-2001-level-persistence-growth-rates]]
- [ ] **Q101** Are persistent analyst over-optimism and dispersion driven by cognitive biases or brokerage incentives?  — [[chan-2001-level-persistence-growth-rates]]
- [ ] **Q102** How much does survivorship bias inflate measured persistence, especially for volatile glamour stocks?  — [[chan-2001-level-persistence-growth-rates]]
- [ ] **Q146** How robust are the demonstrated backtested strategies once transaction costs and out-of-sample decay are fully accounted for?  — [[halls-moore-advanced-algorithmic-trading]]
- [ ] **Q147** Does the supervised intraday-return prediction approach adequately address class imbalance and lookahead bias?  — [[halls-moore-advanced-algorithmic-trading]]
- [ ] **Q181** For each premium, is the return rational compensation for risk or a behavioral anomaly?  — [[ilmanen-2011-expected-returns]]
- [ ] **Q182** How much of documented return predictability is genuine versus data mining?  — [[ilmanen-2011-expected-returns]]
- [ ] **Q183** How do feedback effects (endogenous risk) alter expected returns once strategies become crowded?  — [[ilmanen-2011-expected-returns]]
- [ ] **Q184** Are the four umbrella style premia sufficient to capture rewarded alternative risk premia?  — [[ilmanen-2022-investing-amid-low-expected-returns]]
- [ ] **Q185** Who takes the other side, and do crowding/capacity concerns threaten persistence?  — [[ilmanen-2022-investing-amid-low-expected-returns]]
- [ ] **Q186** How much should investors rely on tactical timing when valuation-based equity timing has performed poorly?  — [[ilmanen-2022-investing-amid-low-expected-returns]]
- [ ] **Q194** How many components are in the main strategy and which signals/sub-strategies are used?  — [[koukorinis-2024-xantium-business-plan]]
- [ ] **Q195** How are positions and the portfolio constructed and sized?  — [[koukorinis-2024-xantium-business-plan]]
- [ ] **Q196** How is residual curve/basis risk managed over longer holds?  — [[koukorinis-2024-xantium-business-plan]]
- [ ] **Q223** How does TAARSS perform out-of-sample net of transaction costs given the short live track record?  — [[mercado-2015-taarss-flow-whisperer]]
- [ ] **Q224** How are formation and rebalancing frequencies chosen, and how sensitive is performance to window lengths?  — [[mercado-2015-taarss-flow-whisperer]]
- [ ] **Q225** Does ETF flow lead, lag, or merely coincide with the underlying asset price move?  — [[mercado-2015-taarss-flow-whisperer]]
- [ ] **Q251** How should walk-forward window sizes be chosen for a given market and trading frequency?  — [[pardo-2008-evaluation-optimization-trading-strategies]]
- [ ] **Q252** What constitutes a statistically significant and robustly shaped optimization profile rather than a fragile peak?  — [[pardo-2008-evaluation-optimization-trading-strategies]]
- [ ] **Q253** How do shifting market regimes and finite strategy life cycles limit forward validity?  — [[pardo-2008-evaluation-optimization-trading-strategies]]
- [ ] **Q321** How can the predictive power of an individual alpha be assessed before its target strategy is known?  — [[tulchinsky-2020-finding-alphas]]
- [ ] **Q322** How do you distinguish a genuine signal from overfitting when in-sample backtest performance is strong?  — [[tulchinsky-2020-finding-alphas]]
- [ ] **Q323** How should many weak, partially-correlated alphas be combined into a robust portfolio?  — [[tulchinsky-2020-finding-alphas]]

## AI / LLM engineering practice  (85)

Eighty-two questions from eighteen books. Almost all are *industry* questions with a short shelf life ("will this framework survive?"). Two exceptions worth keeping: how to evaluate LLM systems when benchmarks saturate, and how to validate LLM-as-judge against human ground truth.

- [ ] **Q4** How should practitioners decide between fine-tuning an embedding model and using a stronger off-the-shelf one as base models improve quarterly?  — [[alammar-2024-hands-on-llm]]
- [ ] **Q5** What evaluation methodology generalises across RAG systems when retrieval quality, grounding faithfulness, and generation fluency interact non-linearly?  — [[alammar-2024-hands-on-llm]]
- [ ] **Q6** When does parameter-efficient fine-tuning stop being competitive with prompting-plus-retrieval as context windows and instruction-following improve?  — [[alammar-2024-hands-on-llm]]
- [ ] **Q7** How should multimodal embedding models be evaluated beyond CLIP-style image-text retrieval as use cases diversify into video, audio, and structured data?  — [[alammar-2024-hands-on-llm]]
- [ ] **Q27** Which concrete vector indexing algorithms (HNSW, IVF, PQ, ScaNN) and similarity metrics are best suited to which RAG workloads?  — [[anon-2024-vector-databases-rag]]
- [ ] **Q28** How should retrieval quality and end-to-end RAG quality be evaluated quantitatively, beyond qualitative claims of relevance?  — [[anon-2024-vector-databases-rag]]
- [ ] **Q29** What are realistic latency, throughput, and cost trade-offs when scaling vector database integrations in production?  — [[anon-2024-vector-databases-rag]]
- [ ] **Q30** How can privacy-preserving techniques (federated learning, differential privacy) be applied to retrieval indexes without degrading recall?  — [[anon-2024-vector-databases-rag]]
- [ ] **Q31** What guardrails are needed when RAG systems retrieve from untrusted or rapidly changing external corpora?  — [[anon-2024-vector-databases-rag]]
- [ ] **Q55** How should knowledge graphs be governed at enterprise scale to avoid 'recursive knowledge graphs all the way down' once they proliferate?  — [[barrasa-2023-building-knowledge-graphs]]
- [ ] **Q56** Where is the right boundary between ontology-driven reasoning and machine-learning-driven enrichment of a knowledge graph?  — [[barrasa-2023-building-knowledge-graphs]]
- [ ] **Q57** How can in-graph ML pipelines reach the modelling depth of external frameworks (PyTorch, TensorFlow, SageMaker) without losing the round-trip benefits of staying inside the graph?  — [[barrasa-2023-building-knowledge-graphs]]
- [ ] **Q58** How exactly do knowledge graphs 'tame the hallucinatory nature of LLMs' — beyond the prototype shown, what production patterns and evaluation metrics apply?  — [[barrasa-2023-building-knowledge-graphs]]
- [ ] **Q59** When standard ontologies (SNOMED CT, FIBO, schema.org) only partially fit a domain, how should organisations version and evolve hybrid in-house ontologies over time?  — [[barrasa-2023-building-knowledge-graphs]]
- [ ] **Q65** How should prompt-assembly priority tiers and continuous scores be learned automatically rather than hand-tuned?  — [[berryman-2024-prompt-engineering-llms]]
- [ ] **Q66** What evaluation methodology generalises beyond code completion, where surgical delete-and-regenerate gives a near-perfect proxy metric?  — [[berryman-2024-prompt-engineering-llms]]
- [ ] **Q67** When is an open-ended conversational agent strictly preferable to a fixed LLM workflow, and how should one migrate between the two as a product matures?  — [[berryman-2024-prompt-engineering-llms]]
- [ ] **Q68** How portable are the OpenAI-specific tool-calling and ChatML patterns to other frontier models with different internal prompt formats?  — [[berryman-2024-prompt-engineering-llms]]
- [ ] **Q69** How do prompt-engineering practices need to change for multimodal models where 'document-like' training-data analogies are weaker?  — [[berryman-2024-prompt-engineering-llms]]
- [ ] **Q73** How do prompting techniques transfer across model families (Gemini vs GPT vs Claude vs open-source) without re-tuning?  — [[boonstra-2024-google-prompt-engineering]]
- [ ] **Q74** What is the right evaluation metric for non-classification prompts - BLEU/ROUGE are mentioned but acknowledged as weak proxies for LLM quality?  — [[boonstra-2024-google-prompt-engineering]]
- [ ] **Q75** How should prompt versioning integrate with model versioning in production CI/CD pipelines?  — [[boonstra-2024-google-prompt-engineering]]
- [ ] **Q76** When does fine-tuning become preferable to ever-more-elaborate prompting?  — [[boonstra-2024-google-prompt-engineering]]
- [ ] **Q77** How should multimodal prompts (image + text) be designed - the whitepaper flags but does not develop this  — [[boonstra-2024-google-prompt-engineering]]
- [ ] **Q78** How does GraphRAG scale to corpora orders of magnitude larger than The Odyssey, where community summarisation costs dominate?  — [[bratanic-2025-essential-graphrag]]
- [ ] **Q79** When is investing in a maintained knowledge graph cheaper than simply scaling vector retrieval with better chunking and rerankers?  — [[bratanic-2025-essential-graphrag]]
- [ ] **Q80** How should entity resolution be handled when extraction is performed incrementally over a streaming corpus rather than a one-shot batch?  — [[bratanic-2025-essential-graphrag]]
- [ ] **Q81** What is the right division of labour between a finetuned text-to-Cypher model and a general-purpose LLM with schema-in-prompt as schemas grow?  — [[bratanic-2025-essential-graphrag]]
- [ ] **Q82** How do you evaluate agentic GraphRAG end-to-end when answer critics and routers are themselves LLM-driven and non-deterministic?  — [[bratanic-2025-essential-graphrag]]
- [ ] **Q83** How will the OpenAI API surface (function calling, plug-ins, fine-tuning availability for GPT-3.5/GPT-4) evolve past late 2023 and which patterns in the book will be deprecated?  — [[caelen-2023-developing-apps-gpt4]]
- [ ] **Q84** When context windows become large enough to hold whole document corpora, how should retrieval-augmented generation be redesigned -- or skipped -- in production apps?  — [[caelen-2023-developing-apps-gpt4]]
- [ ] **Q85** Given that the authors call prompt injection effectively inevitable, what concrete layered defenses (sandboxing, output filters, capability scoping) belong in a GPT-app reference architecture?  — [[caelen-2023-developing-apps-gpt4]]
- [ ] **Q86** How should fine-tuning costs and synthetic-data quality be evaluated against retrieval-augmented and few-shot approaches for a given domain task?  — [[caelen-2023-developing-apps-gpt4]]
- [ ] **Q87** What is the right operational pattern (caching, batching, model routing between GPT-3.5 and GPT-4) for managing latency and per-token cost in user-facing LLM apps?  — [[caelen-2023-developing-apps-gpt4]]
- [ ] **Q151** How do these reading techniques transfer to multi-language codebases where static analysis tools (find-usages, slicers) fail at language boundaries?  — [[hermans-2024-code-reading-in-practice]]
- [ ] **Q152** Can the dependency-table and name-mold exercises be partially automated without losing the cognitive benefit of manual table-filling?  — [[hermans-2024-code-reading-in-practice]]
- [ ] **Q153** How should code-reading skill be assessed or taught in computer-science curricula, and what is the evidence base for these specific exercises?  — [[hermans-2024-code-reading-in-practice]]
- [ ] **Q154** How do LLM-based code assistants change which reading skills remain essential versus which they automate away?  — [[hermans-2024-code-reading-in-practice]]
- [ ] **Q171** How should organizations choose the optimal retraining cadence for continual learning when label feedback loops are long and imbalanced (e.g., fraud detection requiring two-week A/B windows)?  — [[huyen-2022-designing-ml-systems]]
- [ ] **Q172** What concrete statistical tests reliably detect data distribution shifts on high-dimensional feature spaces and embeddings, where univariate tests are weak?  — [[huyen-2022-designing-ml-systems]]
- [ ] **Q173** How can model iteration (architecture changes) be made compatible with stateful training without falling back to full retraining each time?  — [[huyen-2022-designing-ml-systems]]
- [ ] **Q174** Where should the boundary sit between data scientists owning end-to-end production versus a dedicated ML platform team — and how does this change with company scale?  — [[huyen-2022-designing-ml-systems]]
- [ ] **Q175** How can subject matter experts be meaningfully integrated into ML system development beyond the labeling phase, including no-code/low-code pathways for non-engineers?  — [[huyen-2022-designing-ml-systems]]
- [ ] **Q176** How will preference finetuning evolve as the field debates why RLHF and DPO actually work?  — [[huyen-2025-ai-engineering]]
- [ ] **Q177** Can test-time compute be scaled indefinitely, or do adversarial outputs eventually defeat verifiers as sample counts grow?  — [[huyen-2025-ai-engineering]]
- [ ] **Q178** When closed-model providers restrict logprobs and other model internals, how do practitioners retain the ability to evaluate, debug, and route between models?  — [[huyen-2025-ai-engineering]]
- [ ] **Q179** How should AI engineering teams structure cross-functional collaboration with product, data, and infra as model adaptation replaces model training?  — [[huyen-2025-ai-engineering]]
- [ ] **Q180** What evaluation methodology will survive when benchmarks saturate faster than they can be designed?  — [[huyen-2025-ai-engineering]]
- [ ] **Q218** Which chunking strategies (fixed, semantic, layout-aware, agentic) actually win on which document types, and how should that be benchmarked?  — [[mendelevitch-2025-hands-on-rag]]
- [ ] **Q219** How should hallucination detectors be evaluated and calibrated when ground-truth faithfulness exists on a 'spectrum of factuality' rather than a binary?  — [[mendelevitch-2025-hands-on-rag]]
- [ ] **Q220** What is the right way to combine RBAC metadata filtering with semantic retrieval without leaking information through ranking signals?  — [[mendelevitch-2025-hands-on-rag]]
- [ ] **Q221** When does GraphRAG actually outperform well-tuned hybrid search, and at what data-volume threshold does the knowledge-graph build cost pay off?  — [[mendelevitch-2025-hands-on-rag]]
- [ ] **Q222** How should organizations evaluate the build-vs-buy tradeoff between DIY RAG stacks and turnkey platforms in a way that is not biased by vendor framing?  — [[mendelevitch-2025-hands-on-rag]]
- [ ] **Q242** How should data scientists decide where to draw the boundary between an 'exploratory' notebook that does not need engineering rigour and one that does?  — [[nelson-2024-swe-for-data-scientists]]
- [ ] **Q243** What is the right minimum viable test suite for a notebook-driven analysis that may or may not be productionised?  — [[nelson-2024-swe-for-data-scientists]]
- [ ] **Q244** How should preprocessing be versioned and audited so that training-serving skew does not silently degrade production models?  — [[nelson-2024-swe-for-data-scientists]]
- [ ] **Q245** How do these practices scale to teams where data scientists, ML engineers, and software developers share a single codebase under Agile workflows (deferred to a later chapter that is not in this Early Release)?  — [[nelson-2024-swe-for-data-scientists]]
- [ ] **Q246** Which engineering practices justify the upfront time investment for a solo data scientist whose work is read by no one else?  — [[nelson-2024-swe-for-data-scientists]]
- [ ] **Q247** How will the agency-vs-reliability frontier shift as base models improve, and which of these LangGraph patterns will become obsolete?  — [[oshin-2025-learning-langchain]]
- [ ] **Q248** When is a hand-rolled orchestration layer preferable to LangChain/LangGraph's abstractions, and what is the cost of framework lock-in?  — [[oshin-2025-learning-langchain]]
- [ ] **Q249** How should LLM-as-a-judge evaluators be themselves validated against human ground truth at scale?  — [[oshin-2025-learning-langchain]]
- [ ] **Q250** What are the right UX primitives for LLM-native applications beyond chat, collaborative editing, and autonomous agents?  — [[oshin-2025-learning-langchain]]
- [ ] **Q261** How do you retrofit these patterns into an existing legacy Python codebase (only briefly addressed in the epilogue)?  — [[percival-2020-architecture-patterns-python]]
- [ ] **Q262** When does the operational complexity of an event-driven, message-bus architecture outweigh the design benefits for a small team?  — [[percival-2020-architecture-patterns-python]]
- [ ] **Q263** How should event schemas be versioned and governed once events become an integration contract between independently deployed microservices?  — [[percival-2020-architecture-patterns-python]]
- [ ] **Q264** When (if ever) is full event sourcing worth the additional complexity over the CQRS-with-read-models approach the book demonstrates?  — [[percival-2020-architecture-patterns-python]]
- [ ] **Q267** How do the from-scratch GPT-2 design choices (absolute learned positional embeddings, post-LN ordering, GELU) compare empirically to modern alternatives like RoPE, RMSNorm, and SwiGLU used in Llama-style models?  — [[raschka-2024-build-llm-from-scratch]]
- [ ] **Q268** The book stops at supervised fine-tuning — what would be required to extend the from-scratch approach through RLHF, DPO, or preference optimization?  — [[raschka-2024-build-llm-from-scratch]]
- [ ] **Q269** How does the educational laptop-scale pretraining loss curve behave compared to scaling-law predictions for full-scale GPT-2/3 runs?  — [[raschka-2024-build-llm-from-scratch]]
- [ ] **Q270** At what point does building from scratch stop being a useful exercise and how should readers transition to production frameworks like LitGPT or Hugging Face Transformers?  — [[raschka-2024-build-llm-from-scratch]]
- [ ] **Q304** How does the modular-prompt methodology scale to systems with non-local invariants (distributed consistency, concurrency) where small-unit verification is insufficient?  — [[taulli-2024-ai-assisted-programming]]
- [ ] **Q305** What is the right governance model for IP and licence-contamination risk when AI tools regurgitate training data?  — [[taulli-2024-ai-assisted-programming]]
- [ ] **Q306** How should organisations measure productivity gains from AI coding tools beyond self-reported developer surveys?  — [[taulli-2024-ai-assisted-programming]]
- [ ] **Q307** Will the tool landscape consolidate around a few platforms or remain fragmented as the book suggests?  — [[taulli-2024-ai-assisted-programming]]
- [ ] **Q308** How do autonomous coding agents change accountability when they commit code without human review?  — [[taulli-2024-ai-assisted-programming]]
- [ ] **Q309** How should indemnification, copyright, and 'digital essence' rights be allocated when foundation models are trained on copyrighted or scraped data?  — [[thomas-2025-ai-value-creators]]
- [ ] **Q310** What is the right governance and audit regime for agentic systems whose tool use and control flow are emergent rather than specified?  — [[thomas-2025-ai-value-creators]]
- [ ] **Q311** How quickly will 'generative computing' runtimes mature into something practitioners can adopt, and which framework (LangChain successors, IBM stacks, others) will define that layer?  — [[thomas-2025-ai-value-creators]]
- [ ] **Q312** Where exactly is the line between democratising AI through open source and ceding control of critical infrastructure to actors with different values?  — [[thomas-2025-ai-value-creators]]
- [ ] **Q313** How should enterprises measure the ROI of AI value creation versus the simpler ROI of consuming embedded or hosted AI?  — [[thomas-2025-ai-value-creators]]
- [ ] **Q331** How should organisations reconcile the convenience of public LLM APIs with regulatory and IP-leakage risks demonstrated by the Samsung incident?  — [[wilson-2024-llm-security-playbook]]
- [ ] **Q332** What governance model scales the OWASP LLM Top 10 process to keep pace with rapidly evolving attack techniques such as multimodal and agentic injection?  — [[wilson-2024-llm-security-playbook]]
- [ ] **Q333** How can supply-chain provenance be established for open-weights models when full training-data audits are infeasible?  — [[wilson-2024-llm-security-playbook]]
- [ ] **Q334** Where should liability sit when LLM hallucinations produce harmful or illegal output that is then acted on by downstream systems?  — [[wilson-2024-llm-security-playbook]]
- [ ] **Q335** Can classical input-validation and output-sanitisation primitives be made effective against adversarial prompts, or is a fundamentally new defensive paradigm required?  — [[wilson-2024-llm-security-playbook]]

## Monetary policy and macro theory  (25)

Broad, well-trodden, mostly reading context rather than research targets.

- [ ] **Q45** Would the panel model yield similar rejections in non-US settings?  — [[bams-2003-risk-premia-term-structure-panel]]
- [ ] **Q46** How sensitive are estimated risk premia to the choice of cubic-spline breakpoints in constructing the discount curve?  — [[bams-2003-risk-premia-term-structure-panel]]
- [ ] **Q47** Can the time-variation in risk premia be linked to business-cycle or regime variables?  — [[bams-2003-risk-premia-term-structure-panel]]
- [ ] **Q168** Is a 100-percent reserve requirement enforceable without a central authority that itself distorts the system?  — [[huertadesoto-2006-money-bank-credit]]
- [ ] **Q169** How would a transition to 100-percent reserves be sequenced without triggering deflation/crisis?  — [[huertadesoto-2006-money-bank-credit]]
- [ ] **Q170** Does empirical evidence discriminate the Austrian theory from Monetarist and Keynesian alternatives?  — [[huertadesoto-2006-money-bank-credit]]
- [ ] **Q200** Can the Fed indefinitely backstop asset markets, or does each intervention deepen the underlying fragility?  — [[lancaster-2021-fed-up]]
- [ ] **Q201** Does the dominance of quant strategies and algorithmic trading make crashes more violent?  — [[lancaster-2021-fed-up]]
- [ ] **Q202** Will post-2020 stimulus reignite inflation or merely re-inflate the bubble?  — [[lancaster-2021-fed-up]]
- [ ] **Q207** Under what market-structure and preference modifications can asset-pricing models match Hansen-Jagannathan bounds and resolve the equity premium puzzle?  — [[ljungqvist-2012-recursive-macroeconomic-theory]]
- [ ] **Q208** When do Ricardian-equivalence and Modigliani-Miller policy-irrelevance results fail?  — [[ljungqvist-2012-recursive-macroeconomic-theory]]
- [ ] **Q209** How should optimal taxation and debt be designed when state-contingent government debt is unavailable?  — [[ljungqvist-2012-recursive-macroeconomic-theory]]
- [ ] **Q210** How do closed-form optimization techniques scale to high-dimensional or data-driven economic problems?  — [[lukac-2026-economic-analysis-through-mathematics]]
- [ ] **Q211** Where does deterministic modeling break down relative to stochastic/empirical methods?  — [[lukac-2026-economic-analysis-through-mathematics]]
- [ ] **Q265** How do exchange-rate determination and forecasting frameworks compare to modern empirical FX models?  — [[piros-2013-economics-investment-decision-makers-workbook]]
- [ ] **Q266** How are monetary and fiscal policy interactions framed relative to post-2008 unconventional policy?  — [[piros-2013-economics-investment-decision-makers-workbook]]
- [ ] **Q280** Was the asymmetry of the 'below close to 2%' framework a design flaw contributing to the 2010s disinflation?  — [[rostagno-2021-ecb-monetary-policy-crisis]]
- [ ] **Q281** Did the euro area definitively enter the destabilizing second regime?  — [[rostagno-2021-ecb-monetary-policy-crisis]]
- [ ] **Q282** Was the 2011 rate hike a policy error attributable to the price-stability-ceiling logic?  — [[rostagno-2021-ecb-monetary-policy-crisis]]
- [ ] **Q286** Will the real-economy impact of QT and divergent policy be limited, or trigger a reversal?  — [[schofield-2019-citi-macro-views]]
- [ ] **Q287** Can advanced economies cope with higher rates given elevated debt-service burdens?  — [[schofield-2019-citi-macro-views]]
- [ ] **Q288** Can European politics deliver fiscal reform without serious disruption first?  — [[schofield-2019-citi-macro-views]]
- [ ] **Q295** Why was the post-Great-Recession recovery the weakest post-war US expansion despite aggressive easing?  — [[sieron-2021-monetary-policy-after-great-recession]]
- [ ] **Q296** Can monetary policy stimulate an economy mired in debt overhang and balance-sheet recession?  — [[sieron-2021-monetary-policy-after-great-recession]]
- [ ] **Q297** What are the long-run productivity and allocative costs of keeping zombie firms alive?  — [[sieron-2021-monetary-policy-after-great-recession]]

## AI capex, private credit and the 2026 cycle  (13)

Time-sensitive market calls, not research questions. They expire. Review for trading views, then delete.

- [ ] **Q92** When will AI disruption of software business models translate into weaker fundamentals rather than just lower equity multiples?  — [[caprio-2026-steady-but-ai]]
- [ ] **Q93** Will the Fed begin hiking at YE'26 / early 2027, combining tighter policy with AI-driven software stress?  — [[caprio-2026-steady-but-ai]]
- [ ] **Q94** How large would private-credit loan markdowns be if forced software-loan sales materialize?  — [[caprio-2026-steady-but-ai]]
- [ ] **Q148** How should investors price guarantee/security differences between leasing from a project that issues its own bonds versus a hyperscaler issuing its own?  — [[hamid-2026-ai-capex-funding-bond-matrix]]
- [ ] **Q149** What objective criteria should index providers adopt to handle limited-syndication deals consistently?  — [[hamid-2026-ai-capex-funding-bond-matrix]]
- [ ] **Q150** Can the rapid HPC-driven HY issuance pace and tight spreads persist, or do they signal concentration risk?  — [[hamid-2026-ai-capex-funding-bond-matrix]]
- [ ] **Q212** Will rapid ChatGPT adoption translate into paying customers and revenue?  — [[mauboussin-2026-bayes-base-rates]]
- [ ] **Q213** Can base rates legitimately be revised upward given technology-diffusion speed?  — [[mauboussin-2026-bayes-base-rates]]
- [ ] **Q214** Will the AI infrastructure boom repeat the late-1990s telecom overcapacity pattern?  — [[mauboussin-2026-bayes-base-rates]]
- [ ] **Q254** Will the AI-capex cycle sustain, or concentrate credit risk in data-center debt and software direct lending?  — [[patkar-2026-ms-global-credit-midyear]]
- [ ] **Q255** Is the 8% private-credit default forecast contained to software, with the claimed higher recoveries?  — [[patkar-2026-ms-global-credit-midyear]]
- [ ] **Q256** How systemic is private credit given limited bank disclosure on NDFI sub-components?  — [[patkar-2026-ms-global-credit-midyear]]
- [ ] **Q257** Does current pricing leave credit exposed to a sharp repricing if oil escalates?  — [[patkar-2026-ms-global-credit-midyear]]

## Morgan Stanley / Citi tactical archive  (16)

Dated tactical questions from 2013-2020 notes, already resolved by history. **Strongest delete candidate** — 17 questions, near-zero forward value.

- [ ] **Q226** Will concerns about the sustainability of EM growth relative to DM drive longer-term investors to reduce EM allocations?  — [[ms-2013-11-26-em-strategy-no-rush-for-the-exits]]
- [ ] **Q227** What factors (e.g., reversal in CD-OIS spreads, rising CP issuance, or a credit risk event) could cause FRA-OIS to widen contrary to expectations?  — [[ms-2018-04-05-funding-market-signals]]
- [ ] **Q228** Will the extent of the 2019 growth and earnings slowdown be interpreted by markets as the end of the cycle?  — [[ms-2019-01-25-cause-of-the-pause]]
- [ ] **Q229** How large could a self-reinforcing USD overshoot become if hedging-driven selling accelerates?  — [[ms-2019-02-03-self-catalysing-dollar-weakness]]
- [ ] **Q230** Will high hedging costs actually trigger foreign rebalancing out of US assets?  — [[ms-2019-02-03-self-catalysing-dollar-weakness]]
- [ ] **Q231** How frequently should defensive asset classifications be re-estimated as betas drift?  — [[ms-2019-04-14-low-beta-defensiveness-scorecard]]
- [ ] **Q232** Does a high downside beta in supposedly defensive assets undermine standard hedging assumptions?  — [[ms-2019-04-14-low-beta-defensiveness-scorecard]]
- [ ] **Q233** Why do credit and volatility under-price the risk created by a speculative melt-up?  — [[ms-2019-04-29-melt-up-skepticism]]
- [ ] **Q234** Could overseas growth, particularly in China, catalyze the bull case instead of the US?  — [[ms-2019-04-29-melt-up-skepticism]]
- [ ] **Q235** Why do credit risk premiums lag equity risk premiums in repricing during the selloff?  — [[ms-2020-03-10-cross-asset-moves-context]]
- [ ] **Q236** Will extreme volatility term structure and skew normalize or persist?  — [[ms-2020-03-10-cross-asset-moves-context]]
- [ ] **Q237** Will a persistently less-negative stock-bond correlation trigger further deleveraging?  — [[ms-2020-03-20-risk-parity-deleveraging]]
- [ ] **Q238** How vulnerable are rates to a switch out of bonds into stocks as equity vol eases relative to rates?  — [[ms-2020-03-20-risk-parity-deleveraging]]
- [ ] **Q239** How reliable are historical market lead times over the economy in an unprecedented pandemic recession?  — [[ms-2020-03-27-add-to-credit-markets-lead-economy]]
- [ ] **Q240** Will the US COVID-19 trajectory track worse than the base case and invalidate the upgrade?  — [[ms-2020-03-27-add-to-credit-markets-lead-economy]]
- [ ] **Q241** Can a $2 trillion fiscal package meaningfully flatten the unemployment curve?  — [[ms-2020-03-27-fiscal-package-unemployment]]

## Philosophy of causation, time and counterfactuals  (9)

Genuinely open, centuries deep, and not going to produce a JFEC paper. Keep for thinking, not for output.

- [ ] **Q283** Can the cause-effect connection be grounded in physical processes rather than logical necessity?  — [[salmon-1998-causality-and-explanation]]
- [ ] **Q284** Does causality operate in indeterministic contexts such as quantum mechanics, and what form must explanation take there?  — [[salmon-1998-causality-and-explanation]]
- [ ] **Q285** Can causal and unificationist accounts of explanation be reconciled rather than treated as rivals?  — [[salmon-1998-causality-and-explanation]]
- [ ] **Q289** Do counterfactuals express ordinary propositions with truth conditions, or perform a non-propositional function?  — [[schulz-counterfactuals-and-probability]]
- [ ] **Q290** Does the epsilon-operator semantics introduce an unacceptable indeterminacy in truth conditions?  — [[schulz-counterfactuals-and-probability]]
- [ ] **Q291** Can the view be extended from counterfactuals to indicative conditionals?  — [[schulz-counterfactuals-and-probability]]
- [ ] **Q318** Can a dynamic world with tensed-facts-supervening-on-tenseless-facts be shown coherent and preferable to both standard views?  — [[tooley-1997-time-tense-causation]]
- [ ] **Q319** Can backward causation be proven logically impossible without merely ruling out causal loops?  — [[tooley-1997-time-tense-causation]]
- [ ] **Q320** Does a singularist, realist, probabilistic theory of causation entail a dynamic world and the unreality of the future?  — [[tooley-1997-time-tense-causation]]

## Statistical and systems reasoning  (12)

General thinking tools from four books. Useful mental furniture, not a project.

- [ ] **Q36** How should model complexity be selected to balance bias and variance when no theory specifies the true function?  — [[azzalini-2012-data-analysis-and-data-mining]]
- [ ] **Q37** How can classical inferential guarantees be reinterpreted when data lack a designed sampling scheme?  — [[azzalini-2012-data-analysis-and-data-mining]]
- [ ] **Q38** How do supervised methods perform on rare-event problems such as fraud detection?  — [[azzalini-2012-data-analysis-and-data-mining]]
- [ ] **Q111** How do you reliably identify high-leverage points (deep structure) rather than reacting at the event level?  — [[dawson-2020-systems-mental-models]]
- [ ] **Q112** How can an individual detect and correct their own rigid, faulty mental models given limited self-awareness?  — [[dawson-2020-systems-mental-models]]
- [ ] **Q113** How do system delays and non-linearity limit the predictability of interventions?  — [[dawson-2020-systems-mental-models]]
- [ ] **Q121** When is a detected effect large enough to matter, as opposed to merely statistically detectable?  — [[ellenberg-2014-how-not-to-be-wrong]]
- [ ] **Q122** How should significance testing be reformed or supplemented (e.g. with Bayesian reasoning)?  — [[ellenberg-2014-how-not-to-be-wrong]]
- [ ] **Q123** How do we correct everyday and professional inferences for survivorship and selection effects?  — [[ellenberg-2014-how-not-to-be-wrong]]
- [ ] **Q215** How can leverage points be identified reliably given they are counterintuitive and often pushed the wrong way?  — [[meadows-2008-thinking-in-systems]]
- [ ] **Q216** How do you intervene at the level of paradigm or goal when these are hardest to observe and change?  — [[meadows-2008-thinking-in-systems]]
- [ ] **Q217** Where should system boundaries be drawn, given boundaries are mental constructs?  — [[meadows-2008-thinking-in-systems]]

## Broken extractions — not questions  (3)

These three are conversion failures recorded as questions. Two PDFs need re-converting with OCR; one has no body text at all. Action or delete.

- [ ] **Q35** The document body is absent from this extraction (cover page only); the full PDF must be re-converted to obtain content.  — [[avramov-2007-changes-corporate-credit-spreads]]
- [ ] **Q106** The markdown has no extractable text (all content is omitted images); can the PDF be re-converted with OCR to recover themes and bylines?  — [[citi-global-theme-book]]
- [ ] **Q107** Who are the named Citi analysts and what is the publication date? Not recoverable from this file.  — [[citi-global-theme-book]]

