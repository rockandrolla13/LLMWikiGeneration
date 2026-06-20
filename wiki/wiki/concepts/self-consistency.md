---
title: Self-Consistency
page_id: concepts/self-consistency
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
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
schema_version: 2
uuid: fe06d4f0-3a58-5eb8-a110-51a159a2c804
content_hash: sha256:762b3fd93e3e1116682f61b0c4523207f25c32995cff85b0811796dddeaf16f5
---

<!-- AUTHORED REGION START -->
# Self-Consistency

## Definition

An ensemble technique that samples multiple chain-of-thought reasoning paths at high temperature and returns the majority-voted final answer, giving a pseudo-probability of correctness at the cost of more inference calls.

## Sources

- [[sources/boonstra-2024-google-prompt-engineering|Prompt Engineering]]

## Related Concepts

- [[concepts/chain-of-thought-prompting]]

<!-- AUTHORED REGION END -->
