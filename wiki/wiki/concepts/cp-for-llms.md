---
title: Conformal Prediction for Large Language Models
page_id: concepts/cp-for-llms
page_type: concept
revision_id: 1
created: 2026-05-24 16:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- large-language-models
- generative-ai
- hallucination
- alignment
- rag
sources:
- sources/zhou-2025-cp-data-perspective
related:
- concepts/conformal-prediction
- concepts/large-language-models
- concepts/llm-hallucination
- concepts/retrieval-augmented-generation
- concepts/conformal-risk-control
- concepts/cp-for-nlp
mind_map_priority: high
schema_version: 2
uuid: 1627f045-f11e-5a69-8459-f85183b2b202
content_hash: sha256:71718f084042c2217fe6dd5d497905a26b56395f06025db790ec6a465d97bbe1
---

<!-- AUTHORED REGION START -->
# Conformal Prediction for Large Language Models

**CP for LLMs** applies [[concepts/conformal-prediction|conformal prediction]] to generative language models for [[concepts/llm-hallucination|hallucination]] control, factuality filtering, [[concepts/retrieval-augmented-generation|RAG]] pipelines, and alignment.

## Distinctive Challenges

- **Unbounded output space.** Generation spans vocabularies of 50k+ tokens × arbitrary sequence lengths. Standard CP set construction is infeasible.
- **Non-exchangeable training/test.** Pretrained LLMs have seen most internet text; test queries are not exchangeable with calibration queries from the same distribution in any rigorous sense.
- **Multi-statement outputs.** A single LLM response contains many factual claims, not a single label. Subclaim-level decomposition is needed for granular control.
- **Cost.** Calibration over generative outputs requires expensive inference passes.

## Methods

- **Conformal RAG.** Calibrate the retrieval threshold so the retrieved-document set covers the answer-supporting evidence with guaranteed probability. Wraps any retriever.
- **Factuality subclaim filtering.** Decompose the generated text into atomic claims, calibrate per-claim scores, retain only claims with score above the conformal threshold. Bounded factuality risk per response.
- **Conformal alignment.** [[entities/yu-gui|Yu Gui]] et al. framework: train an alignment predictor (does this output align with the user intent?), apply a conformal threshold for FDR-controlled selection of trustworthy outputs.
- **APS-based next-word prediction.** Per-token CP with [[concepts/adaptive-prediction-sets|APS]] over softmax outputs; useful for generation diversity control.
- **CALM (Confident Adaptive Language Modeling).** Early-exit transformer with conformal-style calibration on per-layer confidence; cuts inference cost while preserving generation quality.
- **MCQA and open-domain QA.** Conformal sets of candidate answers with guaranteed coverage of the ground truth.

## Why This Matters

LLM-era applications need calibrated uncertainty more than ever: hallucinations are existential for medical, legal, and financial deployment. CP is the leading non-Bayesian, non-RLHF route to *guaranteed* properties of LLM outputs. The trick is identifying what's being calibrated — usually a derived score (factuality, alignment, retrieval quality) rather than the raw token-level probability.

## Sources

- [[sources/zhou-2025-cp-data-perspective]] — survey chapter on CP for LLMs and NLG.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/large-language-models]]
- [[concepts/llm-hallucination]]
- [[concepts/retrieval-augmented-generation]]
- [[concepts/conformal-risk-control]]
- [[concepts/cp-for-nlp]]

<!-- AUTHORED REGION END -->
