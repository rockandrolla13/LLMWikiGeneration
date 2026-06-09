---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/association-rule-learning
page_type: concept
related:
- concepts/cluster-analysis-and-association-rules
- concepts/green-bond-spreads
- concepts/yield-to-maturity
revision_id: 2
sources:
- sources/sehatpour-2024-green-bonds
tags:
- machine-learning
- data-mining
- pattern-discovery
- market-basket
title: Association Rule Learning
updated: '2026-06-09T12:00:00Z'
---

# Association Rule Learning

Association rule learning discovers interesting relationships between variables in large datasets, originally developed for market basket analysis.

## Core Concepts

### Association Rule
An implication of the form: $X \Rightarrow Y$

"If X is present, then Y tends to be present"

### Key Metrics

| Metric | Definition | Interpretation |
|--------|------------|----------------|
| **Support** | $P(X \cap Y)$ | How often rule applies |
| **Confidence** | $P(Y|X)$ | Reliability of rule |
| **Lift** | $P(Y|X)/P(Y)$ | Improvement over baseline |

## Apriori Algorithm

Classic approach for mining frequent itemsets:

1. Generate candidate itemsets of size k
2. Prune candidates with support below threshold
3. Generate rules from frequent itemsets
4. Filter by confidence/lift thresholds

**Apriori property**: If an itemset is infrequent, all its supersets are infrequent.

## Application to Green Bonds

Sehatpour et al. (2024) use association rules to:
- Discover patterns in green bond pricing
- Identify factor combinations associated with greenium
- Reveal non-linear relationships between bond characteristics
- Example rule: {Certified, Municipal, Long-term} → {Negative Spread}

## Beyond Market Baskets

| Domain | Application |
|--------|-------------|
| Finance | Trading pattern discovery |
| Healthcare | Symptom-disease associations |
| Web analytics | Page visit sequences |
| Manufacturing | Defect pattern analysis |

## Modern Extensions

- **Sequential pattern mining**: Ordered transactions
- **Temporal association rules**: Time-dependent patterns
- **Quantitative rules**: Numeric attributes
- **Multi-level rules**: Concept hierarchies

## See Also

- [[concepts/green-bond-spreads|Green Bond Spreads]]
- [[concepts/yield-to-maturity|Yield to Maturity]]
- [[sources/sehatpour-2024-green-bonds|Anatomy of Municipal Green Bond Yield Spreads (2024)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/cluster-analysis-and-association-rules|cluster-analysis-and-association-rules]]