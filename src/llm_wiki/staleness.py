"""Staleness detection for LLM Wiki (P7).

Identifies pages that have been superseded or are challenged by contradicting
or refuting pages according to the knowledge graph's typed edges.

Usage:
    from pathlib import Path
    from llm_wiki.graph import load_or_build_graph
    from llm_wiki.staleness import detect_stale_pages

    g = load_or_build_graph(Path("wiki"))
    all_ids = [...]  # list of page_id strings
    reports = detect_stale_pages(g, all_ids)
    for r in reports:
        print(r.page_id, r.reason)
"""

from __future__ import annotations

from dataclasses import dataclass, field

from llm_wiki.graph import KnowledgeGraph


@dataclass
class StalenessReport:
    """A staleness finding for a single wiki page."""

    page_id: str
    """Identifier of the page that may be stale."""

    reason: str
    """Human-readable description of why the page is considered stale."""

    superseded_by: list[str] = field(default_factory=list)
    """page_ids of pages that supersede this one (via 'superseded-by' edges)."""

    challenged_by: list[str] = field(default_factory=list)
    """page_ids of pages that challenge (contradict or refute) this one."""


def detect_stale_pages(
    graph: KnowledgeGraph, all_page_ids: list[str]
) -> list[StalenessReport]:
    """Detect pages that appear stale based on graph topology.

    A page is considered stale if:
    - It has one or more incoming 'superseded-by' edges (another page supersedes it), OR
    - It has one or more incoming 'contradicts' or 'refutes' edges (it is challenged).

    Both conditions are checked independently; a page may satisfy both.

    Args:
        graph: The populated KnowledgeGraph instance.
        all_page_ids: Iterable of page identifiers to check.

    Returns:
        List of StalenessReport objects, one per stale page (only stale pages are
        included; pages with no staleness signals are omitted).
    """
    reports: list[StalenessReport] = []

    for pid in all_page_ids:
        # Incoming superseded-by edges: this page was superseded by something else
        superseded_edges = graph.incoming(pid, rel="superseded-by")
        superseded_by = [e.source_id for e in superseded_edges]

        # Incoming contradicts / refutes edges: this page is challenged
        challenge_edges = graph.challenges(pid)
        challenged_by = [e.source_id for e in challenge_edges]

        if not superseded_by and not challenged_by:
            continue

        # Build a concise reason string
        parts: list[str] = []
        if superseded_by:
            parts.append(
                f"superseded by {len(superseded_by)} page(s): "
                + ", ".join(superseded_by)
            )
        if challenged_by:
            parts.append(
                f"challenged by {len(challenged_by)} page(s): "
                + ", ".join(challenged_by)
            )

        reports.append(
            StalenessReport(
                page_id=pid,
                reason="; ".join(parts),
                superseded_by=superseded_by,
                challenged_by=challenged_by,
            )
        )

    return reports
