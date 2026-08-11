"""Operations on a Second Brain: capture, classify, mutate, link.

This is the layer the CLI drives and the layer tests exercise. Nothing here
prints; every function returns data. That separation is what lets a caller other
than the terminal -- an agent processing a transcript, say -- use the same code
paths without parsing formatted output.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from ..clock import utc_now
from .classify import Classification, classify
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
from .store import Store


class NodeNotFoundError(LookupError):
    """Raised when an id or title matches no node."""


def capture(
    store: Store, content: str, source: str = "cli", now: Optional[datetime] = None
) -> Capture:
    """Record raw text in the inbox without classifying it.

    Capture is deliberately cheap. Nothing is decided here -- no type, no
    confidence -- so nothing can slow it down or fail. Classification happens
    later, in :func:`process`.

    Args:
        store: The database to write to.
        content: The text exactly as the user wrote it.
        source: Where it came from -- cli, slack, email, calendar, file.
        now: Creation time, for deterministic tests.

    Returns:
        The stored capture, with its id.

    Raises:
        ValueError: If *content* is empty or only whitespace.
    """
    if not content or not content.strip():
        raise ValueError("capture content is empty")
    item = Capture(content=content.strip(), source=source)
    if now is not None:
        item.created_at = now
    return store.add_capture(item)


def process_one(
    store: Store,
    item: Capture,
    threshold: float,
    now: Optional[datetime] = None,
) -> tuple[Capture, Optional[Node], Classification]:
    """Classify a single capture and file it.

    A capture above the confidence threshold becomes a node and is marked
    ``classified``. Below it, the node is still created -- losing the thought
    would be worse than filing it imperfectly -- but the capture is marked
    ``needs_review`` so it surfaces in the inbox for a human decision.

    Args:
        store: The database.
        item: The capture to classify.
        threshold: Confidence below which the result needs review.
        now: Reference time for relative dates, for deterministic tests.

    Returns:
        A tuple of the updated capture, the node created, and the verdict.
    """
    verdict = classify(item.content, now=now)
    node = Node(
        title=verdict.title,
        node_type=verdict.node_type,
        body=item.content,
        priority=verdict.priority,
        domain=verdict.domain,
        due=verdict.due,
        source=item.source,
        confidence=verdict.confidence,
        capture_id=item.id,
    )
    store.add_node(node)

    item.node_id = node.id
    item.confidence = verdict.confidence
    item.processed_at = now or utc_now()
    item.status = (
        CaptureStatus.NEEDS_REVIEW
        if verdict.confidence < threshold
        else CaptureStatus.CLASSIFIED
    )
    store.update_capture(item)
    store.log_event(
        "capture.classified",
        item.id,
        node_id=node.id,
        node_type=verdict.node_type.value,
        confidence=verdict.confidence,
        status=item.status.value,
    )
    return item, node, verdict


def process(
    store: Store,
    threshold: float,
    capture_id: Optional[str] = None,
    dry_run: bool = False,
    limit: int = 100,
    now: Optional[datetime] = None,
) -> list[tuple[Capture, Optional[Node], Classification]]:
    """Classify pending captures.

    Args:
        store: The database.
        threshold: Confidence below which a result needs review.
        capture_id: Process only this capture, rather than everything pending.
        dry_run: Classify and report, but write nothing.
        limit: Maximum captures to process in one pass.
        now: Reference time, for deterministic tests.

    Returns:
        One result tuple per capture processed. On a dry run the capture and
        classification are real but no node was created, so the node is None.

    Raises:
        NodeNotFoundError: If *capture_id* matches nothing.
    """
    if capture_id:
        found = store.get_capture(capture_id)
        if found is None:
            raise NodeNotFoundError(f"no capture matching {capture_id!r}")
        pending = [found]
    else:
        pending = store.list_captures(status=CaptureStatus.PENDING, limit=limit)

    results = []
    for item in pending:
        if dry_run:
            results.append((item, None, classify(item.content, now=now)))
        else:
            results.append(process_one(store, item, threshold, now=now))
    return results


def resolve_node(store: Store, reference: str) -> Node:
    """Find a node by id prefix or exact title.

    Args:
        store: The database.
        reference: A full id, a unique id prefix, or an exact title.

    Returns:
        The matching node.

    Raises:
        NodeNotFoundError: If nothing matches, or a title matches several nodes.
        AmbiguousIdError: If an id prefix matches several nodes.
    """
    node = store.get_node(reference)
    if node is not None:
        return node
    by_title = store.find_nodes_by_title(reference)
    if len(by_title) == 1:
        return by_title[0]
    if len(by_title) > 1:
        raise NodeNotFoundError(
            f"{reference!r} matches {len(by_title)} nodes by title; use an id"
        )
    raise NodeNotFoundError(f"no node matching {reference!r}")


def complete(store: Store, reference: str, now: Optional[datetime] = None) -> Node:
    """Mark a node completed.

    Args:
        store: The database.
        reference: Id prefix or exact title.
        now: Completion time, for deterministic tests.

    Returns:
        The updated node.
    """
    node = resolve_node(store, reference)
    node.status = NodeStatus.COMPLETED
    node.completed_at = now or utc_now()
    store.update_node(node)
    store.log_event("node.completed", node.id, title=node.title)
    return node


def reopen(store: Store, reference: str) -> Node:
    """Return a completed or archived node to active, clearing its completion time."""
    node = resolve_node(store, reference)
    node.status = NodeStatus.ACTIVE
    node.completed_at = None
    store.update_node(node)
    store.log_event("node.reopened", node.id, title=node.title)
    return node


def archive(store: Store, reference: str) -> Node:
    """Mark a node archived, keeping it in the graph but out of listings."""
    node = resolve_node(store, reference)
    node.status = NodeStatus.ARCHIVED
    store.update_node(node)
    store.log_event("node.archived", node.id, title=node.title)
    return node


def set_priority(store: Store, reference: str, priority: int) -> Node:
    """Set a node's priority level.

    Args:
        store: The database.
        reference: Id prefix or exact title.
        priority: 0 (critical) to 4 (backlog).

    Returns:
        The updated node.

    Raises:
        ValueError: If *priority* is outside 0-4.
    """
    if not 0 <= priority <= 4:
        raise ValueError(f"priority must be 0-4, got {priority}")
    node = resolve_node(store, reference)
    previous = node.priority
    node.priority = priority
    store.update_node(node)
    store.log_event("node.priority", node.id, was=previous, now=priority)
    return node


def set_domain(store: Store, reference: str, domain: Domain) -> Node:
    """Set a node's domain tag."""
    node = resolve_node(store, reference)
    previous = node.domain.value
    node.domain = domain
    store.update_node(node)
    store.log_event("node.domain", node.id, was=previous, now=domain.value)
    return node


def set_type(store: Store, reference: str, node_type: NodeType) -> Node:
    """Reclassify a node by hand.

    This is what resolves a ``needs_review`` item: the classifier's guess stands
    until a human overrides it here.

    Args:
        store: The database.
        reference: Id prefix or exact title.
        node_type: The corrected type.

    Returns:
        The updated node.
    """
    node = resolve_node(store, reference)
    previous = node.node_type.value
    node.node_type = node_type
    store.update_node(node)
    store.log_event("node.retyped", node.id, was=previous, now=node_type.value)

    # The capture that produced this node is no longer awaiting a decision.
    if node.capture_id:
        item = store.get_capture(node.capture_id)
        if item is not None and item.status is CaptureStatus.NEEDS_REVIEW:
            item.status = CaptureStatus.CLASSIFIED
            store.update_capture(item)
    return node


def link(store: Store, src_ref: str, dst_ref: str, rel: EdgeType) -> Edge:
    """Create a typed edge between two nodes.

    Args:
        store: The database.
        src_ref: Id prefix or title of the node the edge points from.
        dst_ref: Id prefix or title of the node the edge points to.
        rel: The relationship type.

    Returns:
        The edge that was created.

    Raises:
        ValueError: If both references resolve to the same node.
    """
    src = resolve_node(store, src_ref)
    dst = resolve_node(store, dst_ref)
    if src.id == dst.id:
        raise ValueError("cannot link a node to itself")
    edge = Edge(src=src.id, dst=dst.id, rel=rel)
    store.add_edge(edge)
    return edge
