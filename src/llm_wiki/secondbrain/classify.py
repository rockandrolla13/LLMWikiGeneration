"""Rule-based classification of captures into typed nodes.

The classifier is deliberately deterministic. It reads the same decision tree
documented in ``.claude/skills/second-brain/references/node-types.md`` and turns
it into scored patterns, so the same text always yields the same node type and
the same confidence. That is what makes it testable, free to run, and safe to
call in a loop over a pasted transcript.

It is not as good as an LLM at the ambiguous middle of the distribution. That is
what the confidence threshold is for: anything it is unsure about goes to
``needs_review`` rather than being filed wrongly and silently.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional

from ..clock import utc_now
from .models import DEFAULT_CONFIDENCE_THRESHOLD, Domain, NodeType

# Explicit prefixes win outright -- if the user wrote "Task: ..." there is
# nothing left to infer. The right-hand side maps the word people actually type
# onto the eight node types.
_EXPLICIT = {
    "task": NodeType.TASK,
    "todo": NodeType.TASK,
    "action": NodeType.TASK,
    "idea": NodeType.IDEA,
    "insight": NodeType.IDEA,
    "reference": NodeType.REFERENCE,
    "ref": NodeType.REFERENCE,
    "note": NodeType.REFERENCE,
    "decision": NodeType.REFERENCE,
    "decided": NodeType.REFERENCE,
    "meeting": NodeType.MEETING,
    "goal": NodeType.GOAL,
    "project": NodeType.PROJECT,
    "value": NodeType.VALUE,
    "person": NodeType.PERSON,
}

_EXPLICIT_PREFIX = re.compile(
    r"^\s*(" + "|".join(sorted(_EXPLICIT, key=len, reverse=True)) + r")\s*[:\-]\s*",
    re.IGNORECASE,
)

# Verbs that start an instruction. "Call the dentist" is a task; "Calling the
# dentist went badly" is not, which is why these only count at the start.
_IMPERATIVE_VERBS = (
    "call|review|send|buy|fix|email|schedule|write|book|check|update|ask|finish|"
    "draft|renew|pay|order|cancel|reply|submit|prepare|read|watch|clean|install"
)

_PATTERNS: tuple[tuple[NodeType, float, re.Pattern[str]], ...] = (
    # -- person ---------------------------------------------------------
    # "Sarah Chen - VP Engineering": a capitalised name, a dash, then a role.
    (NodeType.PERSON, 0.85, re.compile(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+\s*[-–—]\s*\S")),
    # -- meeting --------------------------------------------------------
    (
        NodeType.MEETING,
        0.80,
        re.compile(
            r"\b(standup|stand-up|1:1|one-on-one|retro|all-hands|"
            r"(?:kick-?off|planning|design|sprint) meeting)\b",
            re.IGNORECASE,
        ),
    ),
    (
        NodeType.MEETING,
        0.70,
        re.compile(r"\b(meeting|interview|call) with\b", re.IGNORECASE),
    ),
    # -- task -----------------------------------------------------------
    (NodeType.TASK, 0.80, re.compile(rf"^\s*(?:{_IMPERATIVE_VERBS})\b", re.IGNORECASE)),
    (
        NodeType.TASK,
        0.75,
        re.compile(
            r"\b(need to|have to|must|don'?t forget to|remember to|"
            r"i'?ll |we should|i should)\b",
            re.IGNORECASE,
        ),
    ),
    # -- goal -----------------------------------------------------------
    (
        NodeType.GOAL,
        0.75,
        re.compile(
            r"\b(get promoted|by (?:january|february|march|april|may|june|july|"
            r"august|september|october|november|december|q[1-4]|next (?:year|quarter)))\b",
            re.IGNORECASE,
        ),
    ),
    # -- project --------------------------------------------------------
    (
        NodeType.PROJECT,
        0.65,
        re.compile(
            r"\b(renovation|migration|rollout|redesign|rebuild|"
            r"(?:the|a) \w+ project)\b",
            re.IGNORECASE,
        ),
    ),
    # -- value ----------------------------------------------------------
    (
        NodeType.VALUE,
        0.70,
        re.compile(
            r"\b(comes first|always be \w+ing|\w+ beats \w+|i believe in)\b",
            re.IGNORECASE,
        ),
    ),
    # -- idea -----------------------------------------------------------
    (
        NodeType.IDEA,
        0.80,
        re.compile(
            r"\b(what if|i wonder|i noticed|interesting that|it seems like|"
            r"hypothesis|might be worth)\b",
            re.IGNORECASE,
        ),
    ),
    # -- reference ------------------------------------------------------
    (
        NodeType.REFERENCE,
        0.75,
        re.compile(
            r"\b(rate limit|password|api key|port \d+|version \d|"
            r"happens every|is located at|https?://)\b",
            re.IGNORECASE,
        ),
    ),
)

_PRIORITY_SIGNALS: tuple[tuple[int, re.Pattern[str]], ...] = (
    (0, re.compile(r"\b(critical|urgent|asap|emergency|system down|p0)\b", re.I)),
    (1, re.compile(r"\b(high priority|important|by tomorrow|due tomorrow)\b", re.I)),
    (3, re.compile(r"\b(low priority|nice to have|when i get a chance)\b", re.I)),
    (4, re.compile(r"\b(someday|maybe|backlog|one day)\b", re.I)),
)

_WORK_SIGNALS = re.compile(
    r"\b(sprint|standup|stand-up|deploy|pull request|\bPR\b|code review|client|"
    r"stakeholder|roadmap|kpi|quarter|colleague|manager|jira|ticket|release)\b",
    re.IGNORECASE,
)
_PERSONAL_SIGNALS = re.compile(
    r"\b(mum|mom|dad|wife|husband|partner|kids?|dentist|doctor|holiday|vacation|"
    r"birthday|groceries|gym|family|weekend)\b",
    re.IGNORECASE,
)

_ISO_DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
_MONTHS = (
    "january february march april may june july "
    "august september october november december"
).split()
_MONTH_DAY = re.compile(
    r"\b(" + "|".join(_MONTHS) + r")\s+(\d{1,2})(?:st|nd|rd|th)?\b", re.IGNORECASE
)
_DAY_MONTH = re.compile(
    r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(" + "|".join(_MONTHS) + r")\b", re.IGNORECASE
)

#: Confidence assigned when an explicit "Task:"-style prefix is present.
EXPLICIT_CONFIDENCE = 0.95

#: Confidence assigned when nothing matched and REFERENCE is used as the default.
DEFAULT_CONFIDENCE = 0.35

#: Longest title we will generate before truncating.
MAX_TITLE = 100


@dataclass
class Classification:
    """The classifier's verdict on one piece of text.

    Attributes:
        node_type: The type the text was filed as.
        title: A one-line summary suitable for listings.
        confidence: 0.0 to 1.0. Below the threshold means needs_review.
        priority: 0 (critical) to 4 (backlog).
        domain: work, personal or both.
        due: ISO date string if a date was found, else None.
        reasons: Human-readable notes on why this verdict was reached.
    """

    node_type: NodeType
    title: str
    confidence: float
    priority: int = 2
    domain: Domain = Domain.BOTH
    due: Optional[str] = None
    reasons: list[str] = field(default_factory=list)

    @property
    def needs_review(self) -> bool:
        """True when confidence is below the auto-file threshold."""
        return self.confidence < DEFAULT_CONFIDENCE_THRESHOLD


def make_title(text: str, max_length: int = MAX_TITLE) -> str:
    """Reduce captured text to a single line suitable for a listing.

    Args:
        text: The raw capture.
        max_length: Truncate beyond this many characters.

    Returns:
        The first non-empty line, stripped of any explicit type prefix and
        truncated on a word boundary with an ellipsis.
    """
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    first = _EXPLICIT_PREFIX.sub("", first).strip()
    if len(first) <= max_length:
        return first
    cut = first[:max_length].rsplit(" ", 1)[0]
    return cut + "..."


def extract_due(text: str, now: Optional[datetime] = None) -> Optional[str]:
    """Find a due date in *text* and return it as an ISO date string.

    Recognises ISO dates, "March 15", "15 March", "today" and "tomorrow". Bare
    month-and-day is resolved to the next occurrence, so "March 15" captured in
    December means next March, not the one that has passed.

    Args:
        text: The raw capture.
        now: Reference time, for deterministic tests. Defaults to now.

    Returns:
        An ISO date string, or None if no date was found.
    """
    now = now or utc_now()

    iso = _ISO_DATE.search(text)
    if iso:
        return iso.group(1)

    lowered = text.lower()
    if re.search(r"\btomorrow\b", lowered):
        return (now + timedelta(days=1)).date().isoformat()
    if re.search(r"\btoday\b", lowered):
        return now.date().isoformat()

    match = _MONTH_DAY.search(text)
    if match:
        month, day = match.group(1), int(match.group(2))
    else:
        match = _DAY_MONTH.search(text)
        if not match:
            return None
        day, month = int(match.group(1)), match.group(2)

    month_number = _MONTHS.index(month.lower()) + 1
    try:
        candidate = now.replace(
            month=month_number, day=day, hour=0, minute=0, second=0, microsecond=0
        )
    except ValueError:  # e.g. February 30th
        return None
    if candidate.date() < now.date():
        candidate = candidate.replace(year=candidate.year + 1)
    return candidate.date().isoformat()


def detect_priority(text: str) -> tuple[int, Optional[str]]:
    """Infer a priority level from wording.

    Args:
        text: The raw capture.

    Returns:
        A ``(level, reason)`` pair. Level is 2 and reason is None when nothing
        matched.
    """
    for level, pattern in _PRIORITY_SIGNALS:
        found = pattern.search(text)
        if found:
            return level, f"priority {level} from {found.group(0)!r}"
    return 2, None


def detect_domain(text: str) -> tuple[Domain, Optional[str]]:
    """Infer work/personal/both from wording.

    Args:
        text: The raw capture.

    Returns:
        A ``(domain, reason)`` pair. Both signals present means ``BOTH``, and so
        does neither -- the difference is recorded in the reason.
    """
    work = _WORK_SIGNALS.search(text)
    personal = _PERSONAL_SIGNALS.search(text)
    if work and personal:
        return Domain.BOTH, "work and personal signals both present"
    if work:
        return Domain.WORK, f"work signal {work.group(0)!r}"
    if personal:
        return Domain.PERSONAL, f"personal signal {personal.group(0)!r}"
    return Domain.BOTH, None


def classify(text: str, now: Optional[datetime] = None) -> Classification:
    """Decide what a piece of captured text is.

    Args:
        text: The raw capture, exactly as the user wrote it.
        now: Reference time for relative dates, for deterministic tests.

    Returns:
        A :class:`Classification`. When nothing matches, the type is REFERENCE
        with a confidence below the threshold, which routes it to needs_review
        rather than filing it as a confident guess.
    """
    reasons: list[str] = []
    title = make_title(text)

    explicit = _EXPLICIT_PREFIX.match(text.strip())
    if explicit:
        node_type = _EXPLICIT[explicit.group(1).lower()]
        confidence = EXPLICIT_CONFIDENCE
        reasons.append(f"explicit prefix {explicit.group(1).lower()!r}")
    else:
        node_type, confidence = NodeType.REFERENCE, DEFAULT_CONFIDENCE
        for candidate_type, weight, pattern in _PATTERNS:
            found = pattern.search(text)
            if found and weight > confidence:
                node_type, confidence = candidate_type, weight
                reasons = [f"matched {found.group(0)!r} -> {candidate_type.value}"]
        if not reasons:
            reasons.append("nothing matched; defaulted to reference")

    priority, priority_reason = detect_priority(text)
    if priority_reason:
        reasons.append(priority_reason)

    domain, domain_reason = detect_domain(text)
    if domain_reason:
        reasons.append(domain_reason)

    due = extract_due(text, now=now)
    if due:
        reasons.append(f"due {due}")

    # A dated task is a firmer read than an undated one, but never firm enough
    # to reach the certainty of an explicit prefix.
    if due and node_type is NodeType.TASK and confidence < EXPLICIT_CONFIDENCE:
        confidence = min(confidence + 0.05, 0.9)

    return Classification(
        node_type=node_type,
        title=title,
        confidence=round(confidence, 3),
        priority=priority,
        domain=domain,
        due=due,
        reasons=reasons,
    )
