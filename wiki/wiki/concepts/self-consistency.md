---
title: Self-Consistency
page_id: concepts/self-consistency
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- chain-of-thought-prompting
sources:
- sources/boonstra-2024-google-prompt-engineering
related:
- concepts/chain-of-thought-prompting
mind_map_priority: medium
revision_hash: sha256:33a04ebe97b657e0
---

# Self-Consistency

## Definition

An ensemble technique that samples multiple chain-of-thought reasoning paths at high temperature and returns the majority-voted final answer, giving a pseudo-probability of correctness at the cost of more inference calls.

## Sources

- [[sources/boonstra-2024-google-prompt-engineering|Prompt Engineering]]

## Related Concepts

- [[concepts/chain-of-thought-prompting]]
