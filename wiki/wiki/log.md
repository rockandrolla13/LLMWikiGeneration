
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
