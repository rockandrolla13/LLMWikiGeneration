"""
Evaluation harness for the LLM Wiki BM25 retrieval system.

Loads or builds the BM25 index, runs 15 questions from questions.jsonl,
computes Recall@5, and saves results to results.jsonl.
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

# Ensure the project src package is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from llm_wiki.retrieval.bm25_index import BM25WikiIndex  # noqa: E402

WIKI_DIR = Path(__file__).parent.parent / "wiki"
INDEX_DIR = Path(__file__).parent.parent / ".index" / "bm25"
QUESTIONS_FILE = Path(__file__).parent / "questions.jsonl"
RESULTS_FILE = Path(__file__).parent / "results.jsonl"


@dataclass
class EvalResult:
    question_id: str
    question: str
    domain: str
    wiki_top_pages: List[str]
    expected_pages: List[str]
    recall_at_5: float
    top_snippet: str


def load_questions(path: Path) -> List[dict]:
    questions = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                questions.append(json.loads(line))
    return questions


def evaluate_wiki_path(
    questions: List[dict],
    index: BM25WikiIndex,
) -> List[EvalResult]:
    results: List[EvalResult] = []
    for q in questions:
        top_k = index.query(q["question"], k=5)

        # Collect unique page_ids from top-5 results
        wiki_top_pages = list(dict.fromkeys(r.page_id for r in top_k))

        expected = q.get("expected_pages", [])

        # Recall@5: fraction of expected pages found in top-5 retrieved pages
        if expected:
            hits = sum(1 for ep in expected if ep in wiki_top_pages)
            recall = hits / len(expected)
        else:
            recall = 0.0

        top_snippet = top_k[0].snippet if top_k else ""

        results.append(
            EvalResult(
                question_id=q["id"],
                question=q["question"],
                domain=q["domain"],
                wiki_top_pages=wiki_top_pages,
                expected_pages=expected,
                recall_at_5=recall,
                top_snippet=top_snippet,
            )
        )
    return results


def main() -> None:
    print(f"Wiki dir  : {WIKI_DIR}")
    print(f"Index dir : {INDEX_DIR}")

    print("Loading or building BM25 index...")
    index = BM25WikiIndex.load_or_build(WIKI_DIR, INDEX_DIR)
    print("Index ready.")

    questions = load_questions(QUESTIONS_FILE)
    print(f"Loaded {len(questions)} questions from {QUESTIONS_FILE.name}")

    results = evaluate_wiki_path(questions, index)

    # Save results
    with open(RESULTS_FILE, "w", encoding="utf-8") as fh:
        for r in results:
            fh.write(json.dumps(asdict(r), ensure_ascii=False) + "\n")
    print(f"Results saved to {RESULTS_FILE}")

    # --- Summary ---
    mean_recall = sum(r.recall_at_5 for r in results) / len(results)
    print(f"\nMean Recall@5 (all): {mean_recall:.3f}  ({len(results)} questions)")

    # By-domain breakdown
    domains: dict[str, list[float]] = {}
    for r in results:
        domains.setdefault(r.domain, []).append(r.recall_at_5)

    print("\nRecall@5 by domain:")
    for domain, recalls in sorted(domains.items()):
        avg = sum(recalls) / len(recalls)
        print(f"  {domain:<30} {avg:.3f}  (n={len(recalls)})")

    # Per-question detail
    print("\nPer-question breakdown:")
    for r in results:
        status = "OK" if r.recall_at_5 >= 0.5 else "MISS"
        print(
            f"  [{status}] {r.question_id} ({r.domain})  recall={r.recall_at_5:.2f}"
        )
        missing = [ep for ep in r.expected_pages if ep not in r.wiki_top_pages]
        if missing:
            print(f"         missed: {missing}")


if __name__ == "__main__":
    main()
