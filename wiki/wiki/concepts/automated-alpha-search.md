---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:2a014de5309932c6d2cf128fee8b277a91ee66fccd73e2ef6fca7284c9818693
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/automated-alpha-search
page_type: concept
related:
- concepts/algorithmic-trading
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/autoresearch
- sources/karpathy-2026-autoresearch
- analyses/autoresearch-for-equity-to-credit-modelling
revision_id: 2
schema_version: 2
sources:
- sources/tulchinsky-2020-finding-alphas
- sources/karpathy-2026-autoresearch
tags: []
title: Automated Alpha Search
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 3b7eb7ab-f084-5a0b-a9bd-01b6dd400561
---

<!-- AUTHORED REGION START -->
# Automated Alpha Search

## Definition

The industrialized generation of large numbers of candidate alphas via automated search and machine learning, combined with a backtesting platform, to mine ever-weaker predictive signals at scale.

## Sources

- [[sources/tulchinsky-2020-finding-alphas|Finding Alphas: A Quantitative Approach to Building Trading Strategies (Second Edition)]]

## Related Concepts

- [[concepts/algorithmic-trading|algorithmic-trading]]
- [[concepts/deep-learning-for-finance|deep-learning-for-finance]]
- [[concepts/feature-engineering|feature-engineering]]
## Agent-Driven Search

Karpathy's autoresearch turns automated search into an agent loop: the agent edits the model, runs a fixed-budget experiment, and keeps the change only if one frozen metric improves. His first run tried about 700 changes and kept about 20. Applied to alpha research the same loop multiplies the number of tests, so it needs a holdout and a multiple-testing correction. See [[sources/karpathy-2026-autoresearch|Autoresearch (Karpathy, 2026)]] and [[analyses/autoresearch-for-equity-to-credit-modelling|Autoresearch for Equity-to-Credit Modelling]].
<!-- AUTHORED REGION END -->
