"""Daily and weekly summaries of what matters.

A digest is useless if it is long. The word limits are part of the contract, not
decoration: 150 words for a day, 250 for a week. Sections are dropped from the
bottom up when the text would exceed the limit, so the most urgent material
survives truncation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional

from ..clock import utc_now
from .models import CaptureStatus, Node, NodeStatus, NodeType, short_id
from .store import Store

#: Word limits, by digest period.
DAILY_WORD_LIMIT = 150
WEEKLY_WORD_LIMIT = 250


@dataclass
class DigestSection:
    """One labelled block of a digest.

    Attributes:
        heading: Section title as rendered.
        lines: Already-formatted lines, most important first.
    """

    heading: str
    lines: list[str] = field(default_factory=list)

    def render(self) -> str:
        """Return the section as text, or an empty string when it has no lines."""
        if not self.lines:
            return ""
        return "\n".join([self.heading, *self.lines])


def _describe(node: Node, today: str) -> str:
    """Format one node as a digest line, flagging overdue and high priority."""
    flags = []
    if node.due and node.due < today:
        flags.append("OVERDUE")
    elif node.due == today:
        flags.append("DUE TODAY")
    if node.priority <= 1:
        flags.append(node.priority_name.upper())
    prefix = f"[{'/'.join(flags)}] " if flags else ""
    return f"- {prefix}{node.title} ({short_id(node.id)})"


def build_digest(
    store: Store, now: Optional[datetime] = None, days: int = 1
) -> list[DigestSection]:
    """Assemble the digest sections for a period ending now.

    Args:
        store: The database.
        now: Reference time, for deterministic tests.
        days: 1 for the daily digest, 7 for the weekly review.

    Returns:
        Sections in priority order: due work first, then meetings, then items
        needing review, then recent insights.
    """
    now = now or utc_now()
    today = now.date().isoformat()
    horizon = (now.date() + timedelta(days=days - 1)).isoformat()
    since = now - timedelta(days=days)

    due = store.due_nodes(horizon)
    tasks = [n for n in due if n.node_type is not NodeType.MEETING]
    meetings = [n for n in due if n.node_type is NodeType.MEETING]

    high = [
        n
        for n in store.list_nodes(status=NodeStatus.ACTIVE, limit=50)
        if n.priority <= 1 and n not in tasks and n.due is None
    ]

    review = store.list_captures(status=CaptureStatus.NEEDS_REVIEW, limit=10)
    ideas = [
        n
        for n in store.list_nodes(node_type=NodeType.IDEA, limit=20)
        if n.created_at and n.created_at >= since
    ]

    sections = [
        DigestSection(f"Focus ({today}):", [_describe(n, today) for n in tasks[:6]]),
        DigestSection("High priority:", [_describe(n, today) for n in high[:4]]),
        DigestSection("Meetings:", [_describe(n, today) for n in meetings[:4]]),
        DigestSection(
            "Needs review:",
            [f"- {c.content[:60]} ({short_id(c.id)})" for c in review[:4]],
        ),
        DigestSection("Recent insights:", [f"- {n.title}" for n in ideas[:3]]),
    ]
    return [s for s in sections if s.lines]


def render_digest(
    sections: list[DigestSection], word_limit: int = DAILY_WORD_LIMIT
) -> str:
    """Render sections to text, dropping the least important to fit the limit.

    Args:
        sections: Sections in priority order, most important first.
        word_limit: Maximum words in the rendered output.

    Returns:
        The digest as text. Empty when there is nothing to report, in which case
        the caller should say so rather than print a blank.
    """
    kept: list[str] = []
    words = 0
    for section in sections:
        text = section.render()
        cost = len(text.split())
        if words + cost > word_limit:
            break
        kept.append(text)
        words += cost
    return "\n\n".join(kept)
