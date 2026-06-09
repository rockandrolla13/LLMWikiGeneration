---
authors:
- Judea Pearl
- Dana Mackenzie
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/pearl-2018-book-of-why
page_type: source
publication_date: '2018'
publication_venue: Basic Books (Hachette Book Group)
related:
- concepts/back-door-front-door-adjustment
- concepts/causal-diagram
- concepts/confounding
- concepts/counterfactuals
- concepts/do-operator
- concepts/instrumental-variables
- concepts/ladder-of-causation
- concepts/mediation-analysis
- entities/dana-mackenzie
- entities/david-hume
- entities/francis-galton
- entities/judea-pearl
- entities/karl-pearson
- entities/sewall-wright
revision_hash: sha256:90d4aad76f9ed71f3e505d547cf84bb5da420d22a588786327e4a5587464e4eb
revision_id: 1
source_hash: sha256:e067ef7bbe43b52c6d8bbde1f7a7e7fd554ee4dccc07a9ea609e98aed457f757
source_path: raw/creditmacro/The Book of Why (Judea Pearl) (z-library.sk, 1lib.sk,
  z-lib.sk).md
source_type: book
sources: []
tags:
- causal-inference
- causality
- directed-acyclic-graphs
- do-calculus
- counterfactuals
- artificial-intelligence
title: 'The Book of Why: The New Science of Cause and Effect'
updated: '2026-06-09T12:00:00Z'
updated_by: op_9fa651e5a47d
---

# The Book of Why: The New Science of Cause and Effect

**Authors:** Judea Pearl, Dana Mackenzie · **Year:** 2018 · **Venue:** Basic Books (Hachette Book Group) · **Type:** book

## Summary

The Book of Why is Judea Pearl's popular-science account of the 'Causal Revolution': the development of a mathematical language for cause and effect that statistics had long avoided. Pearl argues that classical statistics deliberately suppressed causal vocabulary after Galton and Pearson, leaving science able only to summarize data ('correlation is not causation') without a means to express what causation actually is. The book's central organizing metaphor is the Ladder of Causation, a three-rung hierarchy: association/seeing (P(Y|X)), intervention/doing (the do-operator, P(Y|do(X))), and counterfactuals/imagining. Machine learning and Big Data, Pearl contends, operate only on the bottom rung; genuine intelligence and scientific understanding require climbing higher. The calculus of causation rests on causal diagrams (DAGs) and a symbolic do-calculus, resolving problems such as confounding via back-door and front-door adjustment and instrumental variables.

## Key Claims

1. Causation can be mathematized: the Causal Revolution gives causal relationships a formal language, ending the era in which statistics could say only that variables are 'associated'.
2. The Ladder of Causation has three rungs - association (seeing), intervention (doing), and counterfactuals (imagining) - and higher-rung questions cannot be answered with only lower-rung tools and data.
3. The do-operator P(Y|do(X)) is fundamentally different from the conditional probability P(Y|X); seeing is not doing.
4. Data alone are 'profoundly dumb': they cannot answer causal or counterfactual questions without an external causal model.
5. Confounding from lurking variables can be solved by tracing paths in a causal diagram, generalizing what the randomized controlled trial achieves.
6. Effects of interventions and counterfactual queries can in many cases be computed from observational data using back-door adjustment, front-door adjustment, and instrumental variables.
7. Causal reasoning is essential to strong AI: machines need causal models to explain, generalize, and reason about responsibility.

## Questions Raised

- How can a machine acquire the causal diagram itself, rather than having it supplied by a human modeler?
- When can a causal effect not identifiable by back-door adjustment still be recovered through front-door adjustment or instrumental variables?
- What architecture would let deep-learning systems climb from association to intervention and counterfactual reasoning?

## Concepts

- [[concepts/ladder-of-causation|Ladder of Causation]]
- [[concepts/causal-diagram|Causal Diagram (DAG)]]
- [[concepts/do-operator|do-operator and do-calculus]]
- [[concepts/confounding|Confounding]]
- [[concepts/back-door-front-door-adjustment|Back-door and Front-door Adjustment]]
- [[concepts/instrumental-variables|Instrumental Variables]]
- [[concepts/counterfactuals|Counterfactuals]]
- [[concepts/mediation-analysis|Mediation Analysis]]

## Entities

- [[entities/judea-pearl|Judea Pearl]]
- [[entities/dana-mackenzie|Dana Mackenzie]]
- [[entities/sewall-wright|Sewall Wright]]
- [[entities/francis-galton|Francis Galton]]
- [[entities/karl-pearson|Karl Pearson]]
- [[entities/david-hume|David Hume]]

## Source

- **Path:** `raw/creditmacro/The Book of Why (Judea Pearl) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:e067ef7bbe43b52c6...`