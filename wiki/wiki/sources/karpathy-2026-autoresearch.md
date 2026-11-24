---
authors:
- Andrej Karpathy
content_hash: sha256:267a49ebade424f28ae0645ae3d1e6d8efb59c0cd4d18b510c7efafada395edd
created: '2026-11-24T23:30:14Z'
mind_map_priority: high
page_id: sources/karpathy-2026-autoresearch
page_type: source
publication_date: '2026-03-06'
publication_venue: GitHub (karpathy/autoresearch) and X (@karpathy)
raw_location: raw/karpathy-autoresearch/
related:
- concepts/autoresearch
- concepts/autonomous-ai-agents
- concepts/automated-alpha-search
- concepts/overfitting-in-alpha-research
- concepts/multiple-testing
- entities/andrej-karpathy
- analyses/autoresearch-for-equity-to-credit-modelling
revision_id: 1
schema_version: 2
source_hash: sha256:9ff46d6815ea3c1c3112dadd5d84df7e191ebbc35f98fbe6a53c80a0f7432476
source_path: raw/karpathy-autoresearch/source.md
source_type: notes
source_url: https://github.com/karpathy/autoresearch
sources: []
tags:
- autoresearch
- ai-agents
- automated-research
- nanochat
- andrej-karpathy
title: Autoresearch (Karpathy, 2026)
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 63624b3c-a33f-54ca-b0b6-47c7f3ed73d5
---

<!-- AUTHORED REGION START -->
# Autoresearch (Karpathy, 2026)

**Author:** Andrej Karpathy · **Dates:** repository created 2026-03-06, tweets 2025-06-30 to 2026-03-15 · **Type:** code repository and tweets (notes) · **Original:** [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## Summary

Autoresearch is a minimal recipe for letting an AI coding agent run research on its own. The agent gets a small but real LLM training setup, a single-GPU version of nanochat in about 630 lines. It edits the training script, trains for exactly 5 minutes, checks whether validation bits per byte fell, keeps the change if it did and reverts it if not, then repeats indefinitely. The human does not edit Python. The human edits `program.md`, a markdown instruction file that Karpathy calls a lightweight "skill", and so "programs the research org". In his first two-day run on a depth-12 model the agent worked through about 650 to 700 changes and found about 20 that lowered validation loss. All of them were additive and transferred to a depth-24 model. Stacked together they cut nanochat's "Time to GPT-2" from 2.02 to 1.80 hours, about 11%.

## Key Ideas

1. **Three files, three owners.** `prepare.py` holds the data, tokenizer and evaluation and is never modified. `train.py` is the only file the agent edits. `program.md` is the only file the human edits.
2. **A fixed time budget makes experiments comparable.** Every run trains for 5 minutes of wall clock, whatever the agent changes. That gives about 12 experiments an hour and about 100 overnight. The cost is that results are specific to the hardware.
3. **One objective metric that the agent cannot touch.** The metric is val_bpb, the validation bits per byte. It does not depend on vocabulary size, so architecture changes are compared fairly. The evaluation function is declared ground truth and is read-only.
4. **Keep or discard through git.** Each experiment is a commit on a dedicated branch. If the metric improves, the branch advances. If not, the agent resets. A results table records every attempt as keep, discard or crash.
5. **A simplicity criterion.** A tiny gain that adds ugly complexity is not worth keeping. A change that deletes code and holds the metric is a win.
6. **Never stop.** Once the loop starts the agent must not ask whether to continue. If it runs out of ideas it should re-read the code and papers, combine near-misses or try bolder changes.
7. **Feed it a pool of ideas.** Karpathy exported a blog post to markdown and used it to queue ideas into his loop.
8. **The next step is a research community, not a single researcher**: many agents on many branches sharing findings, SETI@home style. He notes that GitHub's single-master-branch model fits this poorly.

## Notable Claims

- Changes found on the depth-12 model included a missing scale multiplier on the parameter-free QK-norm, no regularization on value embeddings, banded attention that was too conservative, badly set AdamW betas, and untuned weight-decay schedule and initialization (2026-03-09).
- Earlier attempts failed. In February 2026 he wrote that the agents' ideas were "pretty bad out of the box": weak experiment design, no strong baselines or ablations, and no control for runtime or compute. One agent "discovered" that a bigger network lowers validation loss without noticing that it also trained much longer (2026-02-27).
- The agents implement well-specified ideas well but generate creative ones poorly. He describes the current results as closer to hyperparameter tuning than novel research (2026-03-06).
- An earlier version accepted a change only if both loss and training time were better or equal. The 5-minute fixed budget replaced that two-condition rule (2026-03-07, 2026-03-09).
- Any metric that is reasonably cheap to evaluate, or that has a cheap proxy such as a smaller model, can be autoresearched (2026-03-09).
- Practical problems: agents do not want to loop forever, so he uses watcher scripts. An authentication outage wiped out his runs. Codex did not work with the setup at the time (2026-03-09, 2026-03-11).

## Quotes

> any metric you care about that is reasonably efficient to evaluate (or that has more efficient proxy metrics such as training a smaller network) can be autoresearched by an agent swarm.

## How This Wiki Relates

The recipe transfers to any research problem that has a fixed, trusted evaluation and an editable model. [[analyses/autoresearch-for-equity-to-credit-modelling|Autoresearch for Equity-to-Credit Modelling]] sets it up for equity-implied credit spreads. The wiki itself could be a target too: a gold set in the style of the [[sources/anthropic-2026-knowledge-graph-construction-cookbook|Anthropic knowledge-graph cookbook]] would let an agent tune the ingest prompts.

## Concepts

- [[concepts/autoresearch|Autoresearch]]
- [[concepts/autonomous-ai-agents|Autonomous AI Agents]]
- [[concepts/automated-alpha-search|Automated Alpha Search]]
- [[concepts/overfitting-in-alpha-research|Overfitting in Alpha Research]]
- [[concepts/multiple-testing|Multiple Testing]]

## Entities

- [[entities/andrej-karpathy|Andrej Karpathy]]

## Notes on the Source Text

- The raw folder holds the repository `README.md` and `program.md` (commit 228791fb49, 2026-03-26) and 30 of his tweets labelled with the autoresearch theme in the 2026-11-23 tweet corpus.
- The tweets give "~650 experiments" (2026-03-08) and "approx. 700 changes" (2026-03-09) for the same run.
- The training code itself (`train.py`, `prepare.py`) was not fetched.

## Source

`raw/karpathy-autoresearch/source.md`, a bundle of `README.md`, `program.md` and `tweets.md` from the same folder
<!-- AUTHORED REGION END -->
