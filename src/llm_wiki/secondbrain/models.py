"""Domain types for the Second Brain capture system.

A Second Brain holds two kinds of thing. A *capture* is raw text exactly as it
arrived, before anyone decided what it was. A *node* is a classified thing with
a type, a status and a place in the graph. Captures become nodes when
``classify`` runs over them; until then they sit in the inbox.

Keeping them apart is what lets capture stay instant. Nothing is decided at
capture time, so nothing can block it.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from ..clock import utc_now


class NodeType(str, Enum):
    """The eight kinds of thing the graph can hold.

    Definitions and the boundaries between them live in
    ``.claude/skills/second-brain/references/node-types.md``.
    """

    VALUE = "value"
    GOAL = "goal"
    PROJECT = "project"
    TASK = "task"
    PERSON = "person"
    MEETING = "meeting"
    IDEA = "idea"
    REFERENCE = "reference"


class NodeStatus(str, Enum):
    """Lifecycle state of a node."""

    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class Domain(str, Enum):
    """Which part of life a node belongs to."""

    WORK = "work"
    PERSONAL = "personal"
    BOTH = "both"


class CaptureStatus(str, Enum):
    """Where a capture has got to on its way into the graph."""

    PENDING = "pending"
    PROCESSING = "processing"
    CLASSIFIED = "classified"
    FAILED = "failed"
    NEEDS_REVIEW = "needs_review"


class EdgeType(str, Enum):
    """Typed relationships between nodes."""

    SUPPORTS = "supports"
    BLOCKS = "blocks"
    CONTAINS = "contains"
    DERIVED_FROM = "derived_from"
    ASSIGNED_TO = "assigned_to"
    MENTIONED_IN = "mentioned_in"
    RELATED_TO = "related_to"
    CHILD_OF = "child_of"


#: Priority names, indexed by level. Level 2 is the default.
PRIORITY_NAMES: tuple[str, ...] = ("critical", "high", "medium", "low", "backlog")

#: Captures classified below this confidence go to ``needs_review`` instead of
#: being filed automatically.
DEFAULT_CONFIDENCE_THRESHOLD = 0.6


def new_id() -> str:
    """Return a fresh 32-character hex identifier.

    Node identity is random rather than content-derived on purpose. Capturing
    the same sentence twice is a normal thing to do -- two separate reminders to
    call the same person are two tasks, not one -- so identity must not collapse
    them the way :mod:`llm_wiki.identity` collapses duplicate wiki pages.

    Returns:
        A uuid4 as a hex string with no dashes.
    """
    return uuid.uuid4().hex


def short_id(node_id: str) -> str:
    """Return the 8-character display prefix of *node_id*.

    Args:
        node_id: A full 32-character identifier.

    Returns:
        The first 8 characters, which is what the CLI shows and accepts.
    """
    return node_id[:8]


@dataclass
class Capture:
    """Raw text as it arrived, before classification.

    Attributes:
        id: Unique identifier.
        content: The text exactly as captured. Never rewritten.
        source: Where it came from -- cli, slack, email, calendar, file.
        status: Progress through classification.
        created_at: When it was captured.
        processed_at: When classification ran, if it has.
        node_id: The node it became, if it became one.
        confidence: Classifier confidence, once known.
        error: Failure detail when status is ``failed``.
    """

    content: str
    source: str = "cli"
    id: str = field(default_factory=new_id)
    status: CaptureStatus = CaptureStatus.PENDING
    created_at: datetime = field(default_factory=utc_now)
    processed_at: Optional[datetime] = None
    node_id: Optional[str] = None
    confidence: Optional[float] = None
    error: Optional[str] = None


@dataclass
class Node:
    """A classified thing in the graph.

    Attributes:
        id: Unique identifier.
        node_type: Which of the eight kinds this is.
        title: One-line summary, used everywhere the node is listed.
        body: Full text, usually the original capture.
        status: Lifecycle state.
        priority: 0 (critical) to 4 (backlog); 2 is the default.
        domain: work, personal or both.
        due: Due date as an ISO date string, if one was found.
        created_at: When the node was created.
        updated_at: When it last changed.
        completed_at: When it was completed, if it has been.
        source: Where the originating capture came from.
        confidence: Classifier confidence that produced this node.
        capture_id: The capture this node came from, if any.
    """

    title: str
    node_type: NodeType = NodeType.REFERENCE
    body: str = ""
    id: str = field(default_factory=new_id)
    status: NodeStatus = NodeStatus.ACTIVE
    priority: int = 2
    domain: Domain = Domain.BOTH
    due: Optional[str] = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)
    completed_at: Optional[datetime] = None
    source: str = "cli"
    confidence: Optional[float] = None
    capture_id: Optional[str] = None

    @property
    def priority_name(self) -> str:
        """Return the human-readable name of this node's priority level."""
        if 0 <= self.priority < len(PRIORITY_NAMES):
            return PRIORITY_NAMES[self.priority]
        return str(self.priority)


@dataclass
class Edge:
    """A typed relationship between two nodes.

    Attributes:
        src: Identifier of the node the edge points from.
        dst: Identifier of the node the edge points to.
        rel: The relationship type.
        created_at: When the edge was created.
    """

    src: str
    dst: str
    rel: EdgeType
    created_at: datetime = field(default_factory=utc_now)
