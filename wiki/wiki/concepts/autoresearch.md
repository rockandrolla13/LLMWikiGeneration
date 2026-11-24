---
content_hash: sha256:6af34dbfa46a2369e51b19127138c8491dd532ee3cab1918d5f16718bd71b224
created: '2026-11-24T23:30:14Z'
mind_map_priority: high
page_id: concepts/autoresearch
page_type: concept
related:
- concepts/autonomous-ai-agents
- concepts/automated-alpha-search
- concepts/multiple-testing
- concepts/overfitting-in-alpha-research
- concepts/walk-forward-analysis
- concepts/llm-knowledge-bases
- analyses/autoresearch-for-equity-to-credit-modelling
- sources/karpathy-2026-autoresearch
revision_id: 1
schema_version: 2
sources:
- sources/karpathy-2026-autoresearch
tags:
- ai-agents
- automated-research
- ai-engineering
title: Autoresearch
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 97e09466-423c-554e-a116-46e6bc898e02
---

<!-- AUTHORED REGION START -->
# Autoresearch

## Definition

A research loop run by an AI agent without a human in the loop. The agent changes a model, runs a fixed experiment, measures one trusted metric and keeps the change only if the metric improves. Then it repeats. The human writes the instructions and the evaluation and does not write the experiments. Andrej Karpathy named and published the pattern in March 2026.

## The Loop

1. Start from a baseline and record its score.
2. Change the model code with one idea.
3. Commit, then run the experiment under a fixed budget.
4. Read the score from the log.
5. Keep the commit if the score improved. Otherwise reset to the previous commit.
6. Log the attempt as keep, discard or crash, and go back to step 2.

## What Makes It Work

- **A frozen evaluation** that the agent cannot edit, so it cannot "improve" by changing the test.
- **A fixed budget per experiment**, so every result is comparable and the throughput is known.
- **One editable file**, so the scope stays small and the diffs stay reviewable.
- **A simplicity rule**, so small gains do not buy large complexity.
- **A pool of ideas** in markdown, because agents implement ideas better than they invent them.

## Risks

- Hundreds of experiments against one validation set will find changes that fit noise. This is the [[concepts/multiple-testing|multiple-testing]] problem and the core of [[concepts/overfitting-in-alpha-research|overfitting in alpha research]]. Karpathy's safeguard was a transfer test: changes found on a small model were re-checked on a larger one.
- Agents produce spurious results when the budget is not controlled, for example a bigger model that also trains longer.
- The loop finds tuning improvements far more often than new ideas.

## Related

- [[concepts/autonomous-ai-agents|Autonomous AI Agents]]
- [[concepts/automated-alpha-search|Automated Alpha Search]]
- [[concepts/walk-forward-analysis|Walk-Forward Analysis]]
- [[concepts/llm-knowledge-bases|LLM Knowledge Bases]]
- [[analyses/autoresearch-for-equity-to-credit-modelling|Autoresearch for Equity-to-Credit Modelling]]

## Sources

- [[sources/karpathy-2026-autoresearch|Autoresearch (Karpathy, 2026)]]
<!-- AUTHORED REGION END -->
