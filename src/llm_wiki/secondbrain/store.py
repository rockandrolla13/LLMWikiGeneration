"""SQLite persistence for the Second Brain graph.

One file holds everything: captures, nodes, typed edges, and an append-only
event log. The event log is what makes the system auditable -- every mutation
writes a row, so "when did this task get archived, and by what" is answerable
after the fact.

All timestamps are stored as ISO strings produced by :func:`llm_wiki.clock.utc_now`,
matching the convention used by the wiki itself.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Optional

from ..clock import utc_now
from .models import (
    Capture,
    CaptureStatus,
    Domain,
    Edge,
    EdgeType,
    Node,
    NodeStatus,
    NodeType,
)

SCHEMA_VERSION = 1

_SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS captures (
    id           TEXT PRIMARY KEY,
    content      TEXT NOT NULL,
    source       TEXT NOT NULL DEFAULT 'cli',
    status       TEXT NOT NULL DEFAULT 'pending',
    created_at   TEXT NOT NULL,
    processed_at TEXT,
    node_id      TEXT,
    confidence   REAL,
    error        TEXT
);

CREATE TABLE IF NOT EXISTS nodes (
    id           TEXT PRIMARY KEY,
    node_type    TEXT NOT NULL,
    title        TEXT NOT NULL,
    body         TEXT NOT NULL DEFAULT '',
    status       TEXT NOT NULL DEFAULT 'active',
    priority     INTEGER NOT NULL DEFAULT 2,
    domain       TEXT NOT NULL DEFAULT 'both',
    due          TEXT,
    created_at   TEXT NOT NULL,
    updated_at   TEXT NOT NULL,
    completed_at TEXT,
    source       TEXT NOT NULL DEFAULT 'cli',
    confidence   REAL,
    capture_id   TEXT
);

CREATE TABLE IF NOT EXISTS edges (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    src        TEXT NOT NULL,
    dst        TEXT NOT NULL,
    rel        TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE (src, dst, rel)
);

CREATE TABLE IF NOT EXISTS events (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    ts         TEXT NOT NULL,
    event_type TEXT NOT NULL,
    entity_id  TEXT,
    detail     TEXT
);

CREATE INDEX IF NOT EXISTS idx_captures_status ON captures (status);
CREATE INDEX IF NOT EXISTS idx_nodes_type      ON nodes (node_type);
CREATE INDEX IF NOT EXISTS idx_nodes_status    ON nodes (status);
CREATE INDEX IF NOT EXISTS idx_nodes_due       ON nodes (due);
CREATE INDEX IF NOT EXISTS idx_edges_src       ON edges (src);
CREATE INDEX IF NOT EXISTS idx_edges_dst       ON edges (dst);
"""


def _iso(value: Optional[datetime]) -> Optional[str]:
    """Serialise a datetime the way the rest of the codebase does."""
    return None if value is None else value.isoformat() + "Z"


def _parse(value: Optional[str]) -> Optional[datetime]:
    """Reverse :func:`_iso`, tolerating a missing trailing Z."""
    if not value:
        return None
    return datetime.fromisoformat(value.rstrip("Z"))


class AmbiguousIdError(LookupError):
    """Raised when a short id prefix matches more than one node."""


class Store:
    """A Second Brain database.

    Args:
        path: Location of the SQLite file. Parent directories are created.
    """

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._init_schema()

    def _init_schema(self) -> None:
        with self._conn:
            self._conn.executescript(_SCHEMA)
            self._conn.execute(
                "INSERT OR IGNORE INTO meta (key, value) VALUES (?, ?)",
                ("schema_version", str(SCHEMA_VERSION)),
            )

    def close(self) -> None:
        """Close the underlying connection."""
        self._conn.close()

    def __enter__(self) -> "Store":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- events ----------------------------------------------------------

    def log_event(
        self, event_type: str, entity_id: Optional[str] = None, **detail: Any
    ) -> None:
        """Append a row to the audit log.

        Args:
            event_type: Short verb, e.g. ``node.completed``.
            entity_id: The capture or node the event concerns.
            **detail: Anything else worth recording; stored as JSON.
        """
        with self._conn:
            self._conn.execute(
                "INSERT INTO events (ts, event_type, entity_id, detail) VALUES (?, ?, ?, ?)",
                (
                    _iso(utc_now()),
                    event_type,
                    entity_id,
                    json.dumps(detail, default=str) if detail else None,
                ),
            )

    # -- captures --------------------------------------------------------

    def add_capture(self, capture: Capture) -> Capture:
        """Insert a capture and log the event.

        Args:
            capture: The capture to store.

        Returns:
            The same capture, unchanged.
        """
        with self._conn:
            self._conn.execute(
                """INSERT INTO captures
                   (id, content, source, status, created_at, processed_at,
                    node_id, confidence, error)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    capture.id,
                    capture.content,
                    capture.source,
                    capture.status.value,
                    _iso(capture.created_at),
                    _iso(capture.processed_at),
                    capture.node_id,
                    capture.confidence,
                    capture.error,
                ),
            )
        self.log_event("capture.created", capture.id, source=capture.source)
        return capture

    def get_capture(self, capture_id: str) -> Optional[Capture]:
        """Return the capture whose id starts with *capture_id*, or None."""
        row = self._conn.execute(
            "SELECT * FROM captures WHERE id = ? OR id LIKE ? || '%'",
            (capture_id, capture_id),
        ).fetchone()
        return self._row_to_capture(row) if row else None

    def list_captures(
        self, status: Optional[CaptureStatus] = None, limit: int = 20
    ) -> list[Capture]:
        """List captures, newest first.

        Args:
            status: Restrict to one status, or None for all.
            limit: Maximum rows to return.

        Returns:
            Matching captures.
        """
        sql = "SELECT * FROM captures"
        params: list[Any] = []
        if status is not None:
            sql += " WHERE status = ?"
            params.append(status.value)
        sql += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        return [self._row_to_capture(r) for r in self._conn.execute(sql, params)]

    def update_capture(self, capture: Capture) -> None:
        """Write a capture's mutable fields back to the database."""
        with self._conn:
            self._conn.execute(
                """UPDATE captures
                   SET status = ?, processed_at = ?, node_id = ?, confidence = ?, error = ?
                   WHERE id = ?""",
                (
                    capture.status.value,
                    _iso(capture.processed_at),
                    capture.node_id,
                    capture.confidence,
                    capture.error,
                    capture.id,
                ),
            )

    # -- nodes -----------------------------------------------------------

    def add_node(self, node: Node) -> Node:
        """Insert a node and log the event."""
        with self._conn:
            self._conn.execute(
                """INSERT INTO nodes
                   (id, node_type, title, body, status, priority, domain, due,
                    created_at, updated_at, completed_at, source, confidence, capture_id)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    node.id,
                    node.node_type.value,
                    node.title,
                    node.body,
                    node.status.value,
                    node.priority,
                    node.domain.value,
                    node.due,
                    _iso(node.created_at),
                    _iso(node.updated_at),
                    _iso(node.completed_at),
                    node.source,
                    node.confidence,
                    node.capture_id,
                ),
            )
        self.log_event("node.created", node.id, node_type=node.node_type.value)
        return node

    def get_node(self, node_id: str) -> Optional[Node]:
        """Return a node by full id or unique short prefix.

        Args:
            node_id: A full identifier or any unique leading prefix of one.

        Returns:
            The matching node, or None if nothing matched.

        Raises:
            AmbiguousIdError: If the prefix matches more than one node.
        """
        rows = self._conn.execute(
            "SELECT * FROM nodes WHERE id = ? OR id LIKE ? || '%'", (node_id, node_id)
        ).fetchall()
        if not rows:
            return None
        exact = [r for r in rows if r["id"] == node_id]
        if exact:
            return self._row_to_node(exact[0])
        if len(rows) > 1:
            raise AmbiguousIdError(
                f"{node_id!r} matches {len(rows)} nodes; use more characters"
            )
        return self._row_to_node(rows[0])

    def find_nodes_by_title(self, title: str) -> list[Node]:
        """Return every node whose title matches *title* exactly."""
        rows = self._conn.execute("SELECT * FROM nodes WHERE title = ?", (title,))
        return [self._row_to_node(r) for r in rows]

    def list_nodes(
        self,
        node_type: Optional[NodeType] = None,
        status: Optional[NodeStatus] = None,
        domain: Optional[Domain] = None,
        limit: int = 20,
    ) -> list[Node]:
        """List nodes, most recently updated first.

        Args:
            node_type: Restrict to one type.
            status: Restrict to one lifecycle state.
            domain: Restrict to one domain.
            limit: Maximum rows to return.

        Returns:
            Matching nodes.
        """
        sql = "SELECT * FROM nodes WHERE 1 = 1"
        params: list[Any] = []
        if node_type is not None:
            sql += " AND node_type = ?"
            params.append(node_type.value)
        if status is not None:
            sql += " AND status = ?"
            params.append(status.value)
        if domain is not None:
            sql += " AND domain = ?"
            params.append(domain.value)
        sql += " ORDER BY updated_at DESC LIMIT ?"
        params.append(limit)
        return [self._row_to_node(r) for r in self._conn.execute(sql, params)]

    def search_nodes(self, term: str, limit: int = 20) -> list[Node]:
        """Return nodes whose title or body contains *term*, case-insensitively.

        This is a substring match, not a semantic search. It will miss a node
        that means the same thing in different words.

        Args:
            term: The substring to look for.
            limit: Maximum rows to return.

        Returns:
            Matching nodes, most recently updated first.
        """
        pattern = f"%{term.lower()}%"
        rows = self._conn.execute(
            """SELECT * FROM nodes
               WHERE lower(title) LIKE ? OR lower(body) LIKE ?
               ORDER BY updated_at DESC LIMIT ?""",
            (pattern, pattern, limit),
        )
        return [self._row_to_node(r) for r in rows]

    def update_node(self, node: Node) -> Node:
        """Write a node's mutable fields back, stamping ``updated_at``.

        Args:
            node: The node to persist. Its ``updated_at`` is set to now.

        Returns:
            The same node, with ``updated_at`` refreshed.
        """
        node.updated_at = utc_now()
        with self._conn:
            self._conn.execute(
                """UPDATE nodes
                   SET node_type = ?, title = ?, body = ?, status = ?, priority = ?,
                       domain = ?, due = ?, updated_at = ?, completed_at = ?
                   WHERE id = ?""",
                (
                    node.node_type.value,
                    node.title,
                    node.body,
                    node.status.value,
                    node.priority,
                    node.domain.value,
                    node.due,
                    _iso(node.updated_at),
                    _iso(node.completed_at),
                    node.id,
                ),
            )
        return node

    def due_nodes(self, on_or_before: str, limit: int = 50) -> list[Node]:
        """Return active nodes due on or before an ISO date, soonest first."""
        rows = self._conn.execute(
            """SELECT * FROM nodes
               WHERE status = 'active' AND due IS NOT NULL AND due <= ?
               ORDER BY due ASC, priority ASC LIMIT ?""",
            (on_or_before, limit),
        )
        return [self._row_to_node(r) for r in rows]

    # -- edges -----------------------------------------------------------

    def add_edge(self, edge: Edge) -> None:
        """Insert an edge, ignoring exact duplicates."""
        with self._conn:
            self._conn.execute(
                "INSERT OR IGNORE INTO edges (src, dst, rel, created_at) VALUES (?, ?, ?, ?)",
                (edge.src, edge.dst, edge.rel.value, _iso(edge.created_at)),
            )
        self.log_event("edge.created", edge.src, dst=edge.dst, rel=edge.rel.value)

    def edges_from(self, node_id: str) -> list[Edge]:
        """Return every edge leaving *node_id*."""
        rows = self._conn.execute("SELECT * FROM edges WHERE src = ?", (node_id,))
        return [self._row_to_edge(r) for r in rows]

    def edges_to(self, node_id: str) -> list[Edge]:
        """Return every edge arriving at *node_id*."""
        rows = self._conn.execute("SELECT * FROM edges WHERE dst = ?", (node_id,))
        return [self._row_to_edge(r) for r in rows]

    def neighbours(self, node_id: str, rel: Optional[EdgeType] = None) -> list[Node]:
        """Return the nodes *node_id* points at, optionally filtered by relation.

        Args:
            node_id: The node to traverse from.
            rel: Restrict to one relationship type.

        Returns:
            The nodes on the far end of the matching edges.
        """
        sql = "SELECT n.* FROM edges e JOIN nodes n ON n.id = e.dst WHERE e.src = ?"
        params: list[Any] = [node_id]
        if rel is not None:
            sql += " AND e.rel = ?"
            params.append(rel.value)
        return [self._row_to_node(r) for r in self._conn.execute(sql, params)]

    # -- stats -----------------------------------------------------------

    def counts(self) -> dict[str, int]:
        """Return row counts for the status display.

        Returns:
            Counts keyed ``nodes``, ``edges``, ``captures``, ``events``,
            ``pending`` and ``needs_review``.
        """
        one = lambda sql, *p: self._conn.execute(sql, p).fetchone()[0]  # noqa: E731
        return {
            "nodes": one("SELECT count(*) FROM nodes"),
            "edges": one("SELECT count(*) FROM edges"),
            "captures": one("SELECT count(*) FROM captures"),
            "events": one("SELECT count(*) FROM events"),
            "pending": one("SELECT count(*) FROM captures WHERE status = ?", "pending"),
            "needs_review": one(
                "SELECT count(*) FROM captures WHERE status = ?", "needs_review"
            ),
        }

    # -- row mapping -----------------------------------------------------

    @staticmethod
    def _row_to_capture(row: sqlite3.Row) -> Capture:
        return Capture(
            id=row["id"],
            content=row["content"],
            source=row["source"],
            status=CaptureStatus(row["status"]),
            created_at=_parse(row["created_at"]),
            processed_at=_parse(row["processed_at"]),
            node_id=row["node_id"],
            confidence=row["confidence"],
            error=row["error"],
        )

    @staticmethod
    def _row_to_node(row: sqlite3.Row) -> Node:
        return Node(
            id=row["id"],
            node_type=NodeType(row["node_type"]),
            title=row["title"],
            body=row["body"],
            status=NodeStatus(row["status"]),
            priority=row["priority"],
            domain=Domain(row["domain"]),
            due=row["due"],
            created_at=_parse(row["created_at"]),
            updated_at=_parse(row["updated_at"]),
            completed_at=_parse(row["completed_at"]),
            source=row["source"],
            confidence=row["confidence"],
            capture_id=row["capture_id"],
        )

    @staticmethod
    def _row_to_edge(row: sqlite3.Row) -> Edge:
        return Edge(
            src=row["src"],
            dst=row["dst"],
            rel=EdgeType(row["rel"]),
            created_at=_parse(row["created_at"]),
        )
