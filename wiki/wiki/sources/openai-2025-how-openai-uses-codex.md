---
title: How OpenAI Uses Codex
page_id: sources/openai-2025-how-openai-uses-codex
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2_2026_06_19
tags:
- codex
- openai
- agentic-coding
- software-engineering
- llm-applications
- developer-tools
- code-generation
- refactoring
- test-automation
- prompt-engineering
- internal-workflow
- research-preview
- 2025
sources:
- sources/openai-2025-how-openai-uses-codex
related: []
mind_map_priority: medium
authors:
- OpenAI
year: 2025
source_type: article
schema_version: 2
uuid: fe57be07-d054-5e98-a7a2-668a0cb50797
content_hash: sha256:61fe71d20ce24519292f460d0a21627ec1b5777fa9212365c14228e3ebd9fcef
---

<!-- AUTHORED REGION START -->
# How OpenAI Uses Codex

**Authors:** OpenAI  
**Year:** 2025  
**Type:** article  
**Markdown source:** `markdown_output/openai-2025-how-openai-uses-codex.md`

## Summary

A 12-page internal guide published by OpenAI in 2025 describing how OpenAI's own engineering teams use Codex — their agentic AI coding assistant — in day-to-day software development. Drawing from engineer interviews and internal usage data, the document catalogs seven use cases (code understanding, refactoring/migrations, performance optimization, test coverage, development velocity, staying in flow, and exploration/ideation) alongside six best practices, with concrete example prompts for each use case. The "Looking Ahead" section notes Codex is still in research preview and signals further workflow integration as models improve.

## Key Claims

- Codex is used daily across Security, Product Engineering, Frontend, API, Infrastructure, and Performance Engineering teams at OpenAI.
- Codex helps engineers ramp into unfamiliar codebases faster during onboarding, debugging, and incident response by mapping service relationships and tracing data flow.
- For refactoring, Codex can apply consistent changes across dozens of files and open PRs automatically — tasks reported to take minutes instead of hours.
- Codex is used to identify performance bottlenecks (hot paths, expensive DB calls, redundant operations) and suggest optimized alternatives.
- Test coverage is improved by having Codex generate unit/integration tests overnight on low-coverage modules and produce runnable PRs.
- Codex is used as a lightweight async backlog: engineers fire off tasks in the background and review resulting PRs when free, enabling 4 merged PRs in a single meeting-heavy day (per one anecdote).
- Best practices include: starting with Ask Mode for planning before Code Mode, maintaining an AGENTS.md file for persistent repo context, structuring prompts like GitHub Issues, using Best-of-N output sampling, and iteratively improving Codex's dev environment (startup script, env vars, internet access).
- Codex works best with well-scoped tasks equivalent to roughly one hour of human work or a few hundred lines of code.
- Codex is in research preview as of publication; OpenAI states model improvements will expand the scope of tasks it can handle.

## Main Concepts

- [[concepts/agentic-coding-assistant|Agentic coding assistant]]
- [[concepts/code-understanding-and-codebase-navigation|Code understanding and codebase navigation]]
- [[concepts/refactoring-and-large-scale-migrations|Refactoring and large-scale migrations]]
- [[concepts/performance-optimization-and-bottleneck-detection|Performance optimization and bottleneck detection]]
- [[concepts/automated-test-generation-and-coverage-improvement|Automated test generation and coverage improvement]]
- [[concepts/development-velocity-and-async-task-delegation|Development velocity and async task delegation]]
- [[concepts/flow-state-preservation-and-context-handoff|Flow state preservation and context handoff]]
- [[concepts/exploration-and-ideation-alternative-design-evaluation-|Exploration and ideation (alternative design evaluation)]]
- [[concepts/ask-mode-vs-code-mode-two-step-prompting-pattern-|Ask Mode vs Code Mode (two-step prompting pattern)]]
- [[concepts/agents-md-persistent-context-file|AGENTS.md persistent context file]]
- [[concepts/best-of-n-output-sampling|Best-of-N output sampling]]
- [[concepts/task-queue-as-lightweight-backlog|Task queue as lightweight backlog]]
- [[concepts/prompt-engineering-for-code-agents-github-issue-style-|Prompt engineering for code agents (GitHub Issue style)]]

## Key Entities

- [[entities/openai-organization-author-and-subject-|OpenAI (organization — author and subject)]]
- [[entities/codex-openai-s-agentic-ai-coding-assistant-|Codex (OpenAI's agentic AI coding assistant)]]
- [[entities/chatgpt-web-internal-team-product-|ChatGPT Web (internal team/product)]]
- [[entities/chatgpt-enterprise-internal-team-product-|ChatGPT Enterprise (internal team/product)]]
- [[entities/chatgpt-desktop-internal-team-product-|ChatGPT Desktop (internal team/product)]]
- [[entities/chatgpt-api-internal-team-|ChatGPT API (internal team)]]
- [[entities/api-platform-internal-team-|API Platform (internal team)]]
- [[entities/infrastructure-services-internal-team-|Infrastructure Services (internal team)]]
- [[entities/api-reliability-internal-team-|API Reliability (internal team)]]
- [[entities/model-serving-internal-team-|Model Serving (internal team)]]
- [[entities/payments-and-billing-internal-team-|Payments and Billing (internal team)]]
- [[entities/internal-tools-internal-team-|Internal Tools (internal team)]]
- [[entities/infrastructure-observability-internal-team-|Infrastructure Observability (internal team)]]
- [[entities/retrieval-systems-internal-team-performance-engineering-|Retrieval Systems (internal team — Performance Engineering)]]
- [[entities/datadog-third-party-observability-tool-referenced-in-engineer-anecdote-|Datadog (third-party observability tool referenced in engineer anecdote)]]
- [[entities/terraform-infrastructure-as-code-tool-referenced-in-engineer-anecdote-|Terraform (infrastructure-as-code tool referenced in engineer anecdote)]]
- [[entities/github-pr-issue-workflow-referenced-in-best-practices-|GitHub (PR/Issue workflow referenced in best practices)]]

## Questions Raised

- What specific model underlies Codex in 2025, and how does it differ from the original 2021 OpenAI Codex (GPT-based code model)?
- What is the exact structure and recommended content of an AGENTS.md file beyond what is described here?
- How does Codex's 'Ask Mode' vs 'Code Mode' distinction map to the broader agentic tool-use architecture (e.g., does it correspond to planning vs execution steps in an agent loop)?
- What are the quantitative productivity metrics (beyond anecdotes) from internal usage data referenced in the introduction?
- How does Codex handle security and secret management when given internet access and environment variable configuration?
- What is the 'Best-of-N' feature's computational cost and how is the tradeoff managed at scale?
- How does this 2025 Codex relate to OpenAI's broader agentic product roadmap (e.g., operator/tool-use APIs)?

<!-- AUTHORED REGION END -->
