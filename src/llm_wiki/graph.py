"""Typed knowledge graph for LLM Wiki (P4).

Builds an in-memory directed graph from the `relations:` blocks in wiki page
frontmatter. Inverse edges are computed (not persisted). The graph is cached
at .index/graph_cache.json so repeated calls are fast.

Usage:
    from pathlib import Path
    from llm_wiki.graph import load_or_build_graph

    g = load_or_build_graph(Path("wiki"))
    for edge in g.outgoing("concepts/attention_mechanism"):
        print(edge.rel, "->", edge.target_id)

Design notes (see docs/SECOND_BRAIN_DESIGN.md):
- Pre-P9: relation targets are page_id slugs, not UUIDs.
- P9 migrate.py will rewrite slug targets to UUIDs in one idempotent pass.
- Inverse edges (is_computed=True) are never written to frontmatter.
- Cache is stored in .index/graph_cache.json (gitignored, Tier 2).
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .io.page_io import parse_page
from .schemas_v2 import INVERSE_MAP, EdgeRelType, ForwardRelType


# ---------------------------------------------------------------------------
# Edge dataclass
# ---------------------------------------------------------------------------


@dataclass
class Edge:
    """A directed typed edge in the knowledge graph."""

    source_id: str
    """Source page identifier (slug pre-P9; UUID post-P9)."""

    target_id: str
    """Target page identifier (slug pre-P9; UUID post-P9)."""

    rel: EdgeRelType
    """Relation type (forward or computed inverse)."""

    is_computed: bool = False
    """True if this edge was computed as an inverse; False if authored in frontmatter."""

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "rel": self.rel,
            "is_computed": self.is_computed,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Edge":
        return cls(
            source_id=d["source_id"],
            target_id=d["target_id"],
            rel=d["rel"],
            is_computed=d.get("is_computed", False),
        )


# ---------------------------------------------------------------------------
# KnowledgeGraph dataclass
# ---------------------------------------------------------------------------


@dataclass
class KnowledgeGraph:
    """In-memory directed knowledge graph.

    Stores forward and inverse edges. Inverse edges are flagged with
    is_computed=True and are never written back to frontmatter.
    """

    edges: list[Edge] = field(default_factory=list)

    # Adjacency indexes (populated by add_edge)
    _out: dict[str, list[Edge]] = field(
        default_factory=lambda: defaultdict(list), repr=False
    )
    _in: dict[str, list[Edge]] = field(
        default_factory=lambda: defaultdict(list), repr=False
    )

    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the graph and update adjacency indexes."""
        self.edges.append(edge)
        self._out[edge.source_id].append(edge)
        self._in[edge.target_id].append(edge)

    # ------------------------------------------------------------------
    # Traversal helpers
    # ------------------------------------------------------------------

    def outgoing(
        self, page_id: str, rel: Optional[EdgeRelType] = None
    ) -> list[Edge]:
        """Return all outgoing edges from a page.

        Args:
            page_id: Source page identifier.
            rel: If provided, filter to edges with this relation type.

        Returns:
            List of matching Edge objects.
        """
        edges = self._out.get(page_id, [])
        if rel is not None:
            edges = [e for e in edges if e.rel == rel]
        return list(edges)

    def incoming(
        self, page_id: str, rel: Optional[EdgeRelType] = None
    ) -> list[Edge]:
        """Return all incoming edges to a page.

        Args:
            page_id: Target page identifier.
            rel: If provided, filter to edges with this relation type.

        Returns:
            List of matching Edge objects.
        """
        edges = self._in.get(page_id, [])
        if rel is not None:
            edges = [e for e in edges if e.rel == rel]
        return list(edges)

    def challenges(self, page_id: str) -> list[Edge]:
        """Return all edges that challenge (contradict or refute) a page.

        These are incoming edges with rel == 'contradicts' or 'refutes'.

        Args:
            page_id: Target page identifier.

        Returns:
            List of Edge objects representing challenges to this page.
        """
        return [
            e
            for e in self._in.get(page_id, [])
            if e.rel in ("contradicts", "refutes")
        ]

    def lineage(self, page_id: str) -> list[Edge]:
        """Return edges representing the intellectual lineage of a page.

        Lineage = pages this page extends, specialises, or supersedes
        (outgoing extends/special-case-of/supersedes) plus incoming
        extended-by/generalizes/superseded-by edges.

        Args:
            page_id: Page identifier.

        Returns:
            List of Edge objects forming the lineage subgraph.
        """
        lineage_rels = {
            "extends", "special-case-of", "supersedes",
            "extended-by", "generalizes", "superseded-by",
        }
        result = []
        for e in self._out.get(page_id, []):
            if e.rel in lineage_rels:
                result.append(e)
        for e in self._in.get(page_id, []):
            if e.rel in lineage_rels:
                result.append(e)
        return result

    def assumptions(self, page_id: str) -> list[Edge]:
        """Return the dependencies (assumptions) of a page.

        Assumptions = outgoing 'depends-on' edges from this page, and
        incoming 'required-by' edges (pages that depend on this one).

        Args:
            page_id: Page identifier.

        Returns:
            List of Edge objects.
        """
        assumption_rels = {"depends-on", "required-by"}
        result = []
        for e in self._out.get(page_id, []):
            if e.rel in assumption_rels:
                result.append(e)
        for e in self._in.get(page_id, []):
            if e.rel in assumption_rels:
                result.append(e)
        return result

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """Serialise graph to a JSON-compatible dictionary."""
        return {"edges": [e.to_dict() for e in self.edges]}

    @classmethod
    def from_dict(cls, d: dict) -> "KnowledgeGraph":
        """Deserialise graph from a dictionary (as produced by to_dict())."""
        g = cls()
        for edge_dict in d.get("edges", []):
            g.add_edge(Edge.from_dict(edge_dict))
        return g


# ---------------------------------------------------------------------------
# Graph builder
# ---------------------------------------------------------------------------


def build_graph(wiki_dir: Path) -> KnowledgeGraph:
    """Build a KnowledgeGraph from all wiki pages under wiki_dir.

    Reads every ``*.md`` file under wiki_dir, parses YAML frontmatter,
    and adds:
    - A forward edge for each entry in ``relations:`` blocks.
    - A computed inverse edge using INVERSE_MAP.

    Args:
        wiki_dir: Root directory of the wiki (e.g. Path("wiki")).

    Returns:
        Populated KnowledgeGraph.
    """
    g = KnowledgeGraph()

    for md_path in sorted(wiki_dir.rglob("*.md")):
        try:
            metadata, _ = parse_page(md_path)
        except Exception:
            # Skip files that cannot be parsed (binary fragments, etc.)
            continue

        page_id = metadata.get("page_id")
        if not page_id:
            continue

        relations = metadata.get("relations", [])
        if not isinstance(relations, list):
            continue

        for rel_entry in relations:
            if not isinstance(rel_entry, dict):
                continue
            target = rel_entry.get("target")
            rel = rel_entry.get("rel")
            if not target or not rel:
                continue
            if rel not in INVERSE_MAP:
                # Unknown relation type — skip silently
                continue

            # Forward edge
            forward = Edge(source_id=page_id, target_id=target, rel=rel, is_computed=False)
            g.add_edge(forward)

            # Computed inverse edge
            inverse_rel = INVERSE_MAP[rel]
            # For symmetric rels (contradicts), avoid adding duplicate
            if inverse_rel != rel:
                inverse = Edge(
                    source_id=target,
                    target_id=page_id,
                    rel=inverse_rel,
                    is_computed=True,
                )
                g.add_edge(inverse)

    return g


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------

_CACHE_FILENAME = "graph_cache.json"


def _cache_path(wiki_dir: Path) -> Path:
    """Return the path to the graph cache file."""
    return wiki_dir.parent / ".index" / _CACHE_FILENAME


def load_or_build_graph(wiki_dir: Path) -> KnowledgeGraph:
    """Load the graph from cache if available, otherwise build and cache it.

    Args:
        wiki_dir: Root directory of the wiki.

    Returns:
        KnowledgeGraph (from cache or freshly built).
    """
    cache = _cache_path(wiki_dir)
    if cache.exists():
        try:
            data = json.loads(cache.read_text(encoding="utf-8"))
            return KnowledgeGraph.from_dict(data)
        except Exception:
            # Corrupted cache — rebuild
            pass

    g = build_graph(wiki_dir)
    _write_cache(g, cache)
    return g


def rebuild_graph(wiki_dir: Path) -> KnowledgeGraph:
    """Force a rebuild of the graph, ignoring any existing cache.

    Args:
        wiki_dir: Root directory of the wiki.

    Returns:
        Freshly built KnowledgeGraph (cache is updated).
    """
    g = build_graph(wiki_dir)
    cache = _cache_path(wiki_dir)
    _write_cache(g, cache)
    return g


def _write_cache(g: KnowledgeGraph, cache: Path) -> None:
    """Write graph to cache file, creating parent directory as needed."""
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(g.to_dict(), indent=2), encoding="utf-8")
