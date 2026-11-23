---
content_hash: sha256:daa98d0964d9e1a3378f0f37ece08764c9bfa7f6a8e6efd601fa4cacc7fb9c9e
created: '2026-11-23T14:43:11Z'
mind_map_priority: high
page_id: concepts/llm-knowledge-bases
page_type: concept
related:
- concepts/file-over-app
- concepts/llm-memory
- concepts/retrieval-augmented-generation
- concepts/knowledge-graph
- entities/obsidian
- entities/andrej-karpathy
- sources/karpathy-2026-llm-knowledge-bases-tweets
revision_id: 1
schema_version: 2
sources:
- sources/karpathy-2026-llm-knowledge-bases-tweets
tags:
- ai-engineering
- personal-knowledge-management
title: LLM Knowledge Bases
updated: '2026-11-23T14:43:11Z'
updated_by: op_5c91b297008c
uuid: 183ecb93-3474-5a2d-bff2-2b8e35dd0b91
---

<!-- AUTHORED REGION START -->
# LLM Knowledge Bases

## Definition

A personal research wiki that an LLM builds and maintains from a folder of source documents. The human collects and curates sources. The LLM writes the markdown pages, links them, answers questions against them and checks them for errors. Andrej Karpathy named and described the pattern in April 2026, and this wiki is built the same way.

## How It Works

1. **Ingest.** Source documents (articles, papers, repos, datasets, images) go into a `raw/` directory. Web pages are clipped to markdown, and images are downloaded locally.
2. **Compile.** An LLM incrementally writes a wiki of `.md` files: summaries of every source, concept articles, and backlinks between them.
3. **View.** A markdown viewer such as Obsidian acts as the front end for the raw data, the wiki and derived visualizations.
4. **Ask.** An LLM agent answers complex questions against the wiki. At small scale it can rely on index files and short summaries instead of a retrieval system.
5. **File back.** Answers, slides and plots are saved into the wiki so that later queries build on earlier ones.
6. **Lint.** LLM "health checks" look for inconsistent or missing data and suggest new articles.

## Design Principles

- `raw/` is authoritative. The wiki is derived and keeps links back to the originals.
- The LLM writes the wiki. The human rarely edits it directly but still reads what is filed.
- Plain files in universal formats, so any tool or any AI can work on them (see [[concepts/file-over-app|File Over App]]).
- The memory is explicit: you can see and correct what the AI knows, unlike implicit personalization.

## Limits

- PDF conversion is unreliable for complex documents.
- Low-quality concept pages can creep in and become harder to spot as the wiki grows.
- Ingest is human-in-the-loop, one source at a time.
- Beyond small scale, retrieval or fine-tuning on the wiki may be needed. That last step is still an idea, not a tested result.

## Related

- [[concepts/llm-memory|LLM Memory]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/knowledge-graph|Knowledge Graph]]
- [[entities/obsidian|Obsidian]]
- [[entities/andrej-karpathy|Andrej Karpathy]]

## Sources

- [[sources/karpathy-2026-llm-knowledge-bases-tweets|Karpathy on Obsidian, Second Brains and LLM Knowledge Bases]]
<!-- AUTHORED REGION END -->
