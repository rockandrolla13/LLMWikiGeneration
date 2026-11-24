---
content_hash: sha256:c3ae93910d4dc6e7755b3a63e29dd987167c5d297c55479cefc550ab76e624af
created: '2026-11-24T23:30:14Z'
mind_map_priority: high
page_id: analyses/autoresearch-for-equity-to-credit-modelling
page_type: analysis
related:
- concepts/autoresearch
- analyses/capital-structure-arbitrage-literature-review
- concepts/merton-model
- concepts/creditgrades-model
- concepts/distance-to-default
- concepts/default-model-implied-spread-value-signal
- concepts/cds-implied-volatility
- concepts/look-ahead-bias
- concepts/data-leakage
- concepts/multiple-testing
- concepts/false-discovery-rate
- concepts/overfitting-in-alpha-research
revision_id: 1
schema_version: 2
sources:
- sources/karpathy-2026-autoresearch
- sources/anthropic-2026-knowledge-graph-construction-cookbook
tags:
- autoresearch
- capital-structure-arbitrage
- structural-models
- bond-signals
- design
title: Autoresearch for Equity-to-Credit Modelling
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 880430cc-999a-56bc-a318-a75a0d7b8678
---

<!-- AUTHORED REGION START -->
# Autoresearch for Equity-to-Credit Modelling

*Prepared 2026-11-24. A design for applying Karpathy's autoresearch loop to an equity-implied credit spread model. It is a plan, not code: the files below are to be written in the research repository. Numbers marked "choose" are design choices to set, not findings.*

## Bottom line

1. **Autoresearch works when the evaluation is fixed and trusted.** In credit the danger is not the agent writing bad code. The danger is the agent finding a model that fits the validation period by chance. So most of this design is about the evaluation, not the agent.
2. **The target is a cross-sectional signal, not a price level.** The literature review in this wiki says structural models get spread levels wrong but sensitivities right, so score the model on ranks and changes ([[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage review]], §1).
3. **Keep a holdout the agent never sees**, and re-test anything it finds on a different slice (another rating band, region or period). This is the credit version of Karpathy's small-model-to-large-model transfer check.

## 1. How the recipe maps

| Autoresearch | Equity-to-credit version |
|---|---|
| `prepare.py`: data, tokenizer, `evaluate_bpb`. Read-only. | `prepare.py`: point-in-time panel, train/validation/holdout split, `evaluate()`. Read-only. |
| `train.py`: model and optimizer. Agent edits. | `model.py`: maps equity inputs to a fair spread. Agent edits. |
| `program.md`: instructions. Human edits. | `program.md`: instructions. Human edits. |
| 5-minute training budget | A fixed compute budget per run (choose, for example 5 minutes) |
| val_bpb, lower is better | Validation rank IC, higher is better (defined below) |
| `results.tsv` | `results.tsv` with the same five columns |
| Transfer test, depth 12 to depth 24 | Transfer test to another rating band, region or period, then the holdout |

## 2. The fixed part: `prepare.py`

**Data.** A monthly, point-in-time panel per issuer: share price, equity volatility (historical and option-implied, with skew where available), debt per share, rating, and the market credit spread (CDS or a representative bond). Every input must be lagged to the date it was known. That is the [[concepts/look-ahead-bias|look-ahead]] and [[concepts/data-leakage|leakage]] guard, and it lives here so the agent cannot weaken it. Use corrected bond data, because the review records a retraction and a 2026 audit of bond-factor results (§ Bottom line, point 5).

**Splits (choose the dates).**
- *Calibration:* the period `model.py` may fit parameters on.
- *Validation:* the period the loop scores on. The agent sees this score.
- *Holdout:* the last years of the sample. The agent never runs on it. Only the human runs it, at the end of a round.

**Metric.** Each month, rank issuers by the gap between the market spread and the model's fair spread. Score the Spearman correlation of that gap with the next month's spread change: issuers whose market spread sits above fair value should tighten. Average over the validation months. Higher is better. Report the t-statistic alongside it, so a change that adds noise is visible.

**Why this metric.** It follows the evidence already in the wiki. Bai & Wu find that the gap between the market CDS spread and a fair spread predicts future spread moves (review, §1). Correia, Richardson and Tuna show that a related signal, the log ratio of the actual spread to a default-model-implied spread, mean-reverts and predicts one-to-three-month credit returns ([[concepts/default-model-implied-spread-value-signal|Default-Model-Implied Spread Value Signal]]). The review advises ranks and changes over level gaps.

## 3. The editable part: `model.py`

The baseline is a plain [[concepts/merton-model|Merton]] fair spread from share price, historical equity volatility and debt per share. Everything else is open to the agent, within the rules in `program.md`. A seed pool of ideas, taken from this wiki, goes into `ideas.md`:

1. Replace historical with option-implied volatility. The review reports this as the change that matters most ([[concepts/cds-implied-volatility|CDS Implied Volatility]]).
2. Switch to a first-passage model with an uncertain barrier ([[concepts/creditgrades-model|CreditGrades]]).
3. Add implied-volatility skew as an input.
4. Combine [[concepts/distance-to-default|distance-to-default]] with fundamentals through shrinkage, in the style of Bai & Wu.
5. Condition on rating band and liquidity, because the lag from equity to credit sits mainly in high yield and BBB (§3 of the review).

## 4. The instructions: `program.md`

Adapted from Karpathy's file. Copy and fill in the bracketed parts.

```markdown
# autoresearch: equity-implied credit spreads

## Setup
1. Agree a run tag, e.g. `nov24`. Create branch `autoresearch/<tag>`.
2. Read README.md, prepare.py, model.py and ideas.md.
3. Check the data panel exists at [path]. If not, stop and tell the human.
4. Create results.tsv with the header row. Run the baseline first.

## Rules
- You may edit model.py only.
- Do not edit prepare.py, the splits or evaluate(). evaluate() is ground truth.
- Never read or run the holdout period.
- Do not add packages beyond pyproject.toml.
- Every input must come from the point-in-time panel. No new data sources.
- Each run must finish within [5] minutes. Kill and discard anything over [10].

## Goal
Raise validation rank IC. Report the t-statistic with it.
Keep a change only if rank IC rises by more than [threshold] AND the
t-statistic does not fall.
Simplicity: a gain under [threshold] that adds complexity is a discard.
A change that removes code and holds rank IC is a keep.

## Loop (never stop to ask)
1. Pick an idea from ideas.md or from earlier results.
2. Edit model.py, then git commit.
3. Run: `uv run run.py > run.log 2>&1`
4. Read: `grep "^rank_ic:\|^t_stat:" run.log`. Empty means a crash:
   read `tail -n 50 run.log`, fix simple bugs, otherwise log "crash".
5. Log commit, rank_ic, t_stat, status, description to results.tsv.
6. Keep: advance the branch. Otherwise: git reset to the last keep.
```

## 5. What the human does

1. Write `prepare.py`, the metric and the splits, and freeze them before the first run.
2. Write `program.md` and `ideas.md`.
3. Let a round run (about 100 runs overnight at 5 minutes each).
4. Read `results.tsv` and the kept commits. Throw out anything that has no economic reason ([[concepts/overfitting-in-alpha-research|overfitting]]).
5. Run the transfer test on a different slice, then the holdout, once. Treat the number of runs as the number of tests: hundreds of tries against one validation set will produce chance winners ([[concepts/multiple-testing|Multiple Testing]], [[concepts/false-discovery-rate|False Discovery Rate]]).
6. Rewrite `program.md` with what you learned and start the next round.

## 6. Limits to expect

- Karpathy's loop found tuning improvements, not new theory. Expect better volatility inputs and calibration choices, not a new structural model.
- His early runs failed because the agents designed experiments badly. The fixed budget, the frozen metric and the transfer test are the defences.
- A financial panel is much smaller and noisier than a language-model validation set. A gain that would be real for val_bpb can be noise here. That is why the t-statistic, the threshold and the holdout are part of the rules.

## A second target: this wiki

The same loop could tune this wiki's ingest prompts. Hand-label the entities and concepts for a few sources, as the [[sources/anthropic-2026-knowledge-graph-construction-cookbook|Anthropic knowledge-graph cookbook]] does with its gold set. Then score precision and recall, and let the agent edit only the extraction prompt.

## Sources

- [[sources/karpathy-2026-autoresearch|Autoresearch (Karpathy, 2026)]]
- [[sources/anthropic-2026-knowledge-graph-construction-cookbook|Knowledge Graph Construction with Claude (Anthropic Cookbook)]]
- [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]]
<!-- AUTHORED REGION END -->
