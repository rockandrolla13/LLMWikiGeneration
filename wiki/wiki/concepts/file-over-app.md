---
content_hash: sha256:d6e8a291f5b12e013c9d23fac4123a968a1d9d735982e5da06d925090f167ec8
created: '2026-11-23T14:43:11Z'
mind_map_priority: medium
page_id: concepts/file-over-app
page_type: concept
related:
- concepts/llm-knowledge-bases
- entities/obsidian
- sources/karpathy-2026-llm-knowledge-bases-tweets
revision_id: 1
schema_version: 2
sources:
- sources/karpathy-2026-llm-knowledge-bases-tweets
tags:
- personal-knowledge-management
- software-design
title: File Over App
updated: '2026-11-23T14:43:11Z'
updated_by: op_5c91b297008c
uuid: a084ca4c-7d0a-5606-b9c2-7fab74bafffe
---

<!-- AUTHORED REGION START -->
# File Over App

## Definition

The principle that data should live in files you control, in simple universal formats, rather than inside a particular application. Software is ephemeral, and files in open formats outlast it. The phrase is the title of an essay by Obsidian's CEO, @kepano, which Karpathy recommended in February 2024.

## Why It Matters for LLM Tools

Plain files are readable by any program, so LLM agents can read, write and search them directly with ordinary command-line tools. Karpathy uses this as an argument for explicit, file-based memory: a wiki of markdown files can be inspected, moved and used with any AI, while memory held inside one AI provider cannot.

## Related

- [[concepts/llm-knowledge-bases|LLM Knowledge Bases]]
- [[entities/obsidian|Obsidian]]

## Sources

- [[sources/karpathy-2026-llm-knowledge-bases-tweets|Karpathy on Obsidian, Second Brains and LLM Knowledge Bases]]
<!-- AUTHORED REGION END -->
