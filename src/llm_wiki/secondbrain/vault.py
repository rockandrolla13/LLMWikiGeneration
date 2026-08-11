"""Markdown export, so the graph is readable in Obsidian.

The database is the source of truth. The vault is a projection of it: every
export overwrites the file for a node from the node's current state. Editing a
vault file by hand therefore does not change the graph, and the change is lost
at the next export. That is a deliberate trade -- one writer, no merge problem.

Files are grouped by node type, one folder each, so the vault is navigable
without a plugin.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, Optional

from .models import Node, short_id
from .store import Store

_UNSAFE = re.compile(r"[^a-z0-9]+")


def slugify(title: str, max_length: int = 60) -> str:
    """Turn a title into a filesystem-safe stem.

    Args:
        title: The node title.
        max_length: Truncate the slug beyond this many characters.

    Returns:
        A lowercase, hyphenated stem. Returns ``"untitled"`` when the title has
        no usable characters, so a file is always writable.
    """
    slug = _UNSAFE.sub("-", title.lower()).strip("-")[:max_length].strip("-")
    return slug or "untitled"


def node_filename(node: Node) -> str:
    """Return the file name for *node*, unique by construction.

    The short id is appended so two nodes with the same title never collide.

    Args:
        node: The node to name a file for.

    Returns:
        A file name ending in ``.md``.
    """
    return f"{slugify(node.title)}-{short_id(node.id)}.md"


def render_node(node: Node, store: Optional[Store] = None) -> str:
    """Render a node as a markdown page with YAML frontmatter.

    Args:
        node: The node to render.
        store: If given, outgoing edges are rendered as wikilinks.

    Returns:
        The full file contents.
    """
    lines = [
        "---",
        f"id: {node.id}",
        f"type: {node.node_type.value}",
        f"status: {node.status.value}",
        f"priority: {node.priority}",
        f"domain: {node.domain.value}",
    ]
    if node.due:
        lines.append(f"due: {node.due}")
    if node.confidence is not None:
        lines.append(f"confidence: {node.confidence}")
    lines.append(f"created: {node.created_at.isoformat()}Z")
    lines.append(f"updated: {node.updated_at.isoformat()}Z")
    if node.completed_at:
        lines.append(f"completed: {node.completed_at.isoformat()}Z")
    lines.append(f"source: {node.source}")
    lines += ["---", "", f"# {node.title}", ""]

    if node.body and node.body.strip() != node.title:
        lines += [node.body.strip(), ""]

    if store is not None:
        edges = store.edges_from(node.id)
        if edges:
            lines.append("## Links")
            lines.append("")
            for edge in edges:
                target = store.get_node(edge.dst)
                if target is not None:
                    stem = node_filename(target)[: -len(".md")]
                    lines.append(f"- {edge.rel.value} :: [[{stem}|{target.title}]]")
            lines.append("")

    return "\n".join(lines)


def write_node(node: Node, vault_path: Path, store: Optional[Store] = None) -> Path:
    """Write one node to the vault, overwriting any previous version.

    Args:
        node: The node to write.
        vault_path: Root of the vault.
        store: If given, outgoing edges are rendered as wikilinks.

    Returns:
        The path written.
    """
    folder = vault_path / f"{node.node_type.value}s"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / node_filename(node)
    path.write_text(render_node(node, store=store), encoding="utf-8")
    return path


def export_all(store: Store, vault_path: Path, limit: int = 10_000) -> list[Path]:
    """Write every node in the graph to the vault.

    Args:
        store: The database.
        vault_path: Root of the vault.
        limit: Safety cap on how many nodes to export.

    Returns:
        The paths written, in export order.
    """
    vault_path.mkdir(parents=True, exist_ok=True)
    return [
        write_node(node, vault_path, store=store)
        for node in store.list_nodes(limit=limit)
    ]
