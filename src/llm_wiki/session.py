"""Session context for LLM Wiki (Tier 3 - Ephemeral).

Provides lightweight session tracking for convenience context.
Session data is ephemeral - stored in memory or temp files.
If session data is lost, the wiki is still 100% functional.

Key principle: Session provides navigation assistance, NOT knowledge.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional
import json
import tempfile
import uuid


class SessionStatus(Enum):
    """Session lifecycle states."""
    ACTIVE = "active"
    ENDED = "ended"


class OperationKind(Enum):
    """Types of operations logged in session."""
    PAGE_VIEW = "page_view"
    SEARCH = "search"
    INGEST = "ingest"
    EDIT = "edit"
    REBUILD = "rebuild"
    OTHER = "other"


@dataclass
class NavigationEntry:
    """Record of a page view in the session."""
    page_id: str
    title: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)
    source: str = ""  # How the user arrived (search, link, direct)

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "page_id": self.page_id,
            "title": self.title,
            "timestamp": self.timestamp.isoformat() + "Z",
            "source": self.source,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "NavigationEntry":
        """Create from dictionary."""
        return cls(
            page_id=d["page_id"],
            title=d.get("title"),
            timestamp=datetime.fromisoformat(d["timestamp"].rstrip("Z")),
            source=d.get("source", ""),
        )


@dataclass
class QueryEntry:
    """Record of a search query in the session."""
    query: str
    result_count: int = 0
    top_results: list[str] = field(default_factory=list)  # page_ids
    timestamp: datetime = field(default_factory=datetime.utcnow)
    filters: dict = field(default_factory=dict)  # page_types, tags, etc.

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "query": self.query,
            "result_count": self.result_count,
            "top_results": self.top_results,
            "timestamp": self.timestamp.isoformat() + "Z",
            "filters": self.filters,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "QueryEntry":
        """Create from dictionary."""
        return cls(
            query=d["query"],
            result_count=d.get("result_count", 0),
            top_results=d.get("top_results", []),
            timestamp=datetime.fromisoformat(d["timestamp"].rstrip("Z")),
            filters=d.get("filters", {}),
        )


@dataclass
class OperationEntry:
    """Record of an operation performed in the session."""
    kind: OperationKind
    description: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    op_id: Optional[str] = None  # Reference to manifest entry if applicable
    details: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "kind": self.kind.value,
            "description": self.description,
            "timestamp": self.timestamp.isoformat() + "Z",
            "op_id": self.op_id,
            "details": self.details,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "OperationEntry":
        """Create from dictionary."""
        return cls(
            kind=OperationKind(d["kind"]),
            description=d["description"],
            timestamp=datetime.fromisoformat(d["timestamp"].rstrip("Z")),
            op_id=d.get("op_id"),
            details=d.get("details", {}),
        )


@dataclass
class SessionContext:
    """Ephemeral session state (Tier 3).

    Tracks the current session's navigation, queries, and operations.
    This is convenience context - if lost, the wiki is still functional.

    Key properties:
    - Session-scoped: Data is valid only for this session
    - Ephemeral: Can be stored in memory or temp files
    - Non-canonical: NOT backed up, NOT versioned
    - Loss acceptable: Wiki works fine without session data

    Attributes:
        session_id: Unique identifier for this session
        wiki_root: Path to the wiki root directory
        started_at: When the session began
        ended_at: When the session ended (None if active)
        status: Current session status
        navigation_history: Pages viewed in this session
        query_history: Searches performed in this session
        operations: Operations performed in this session
        working_context: Free-form notes about current work
    """
    session_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    wiki_root: Optional[Path] = None
    started_at: datetime = field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = None
    status: SessionStatus = SessionStatus.ACTIVE

    # History tracking
    navigation_history: list[NavigationEntry] = field(default_factory=list)
    query_history: list[QueryEntry] = field(default_factory=list)
    operations: list[OperationEntry] = field(default_factory=list)

    # Working context
    working_context: str = ""
    focus_pages: list[str] = field(default_factory=list)  # page_ids being actively worked on

    # Statistics (computed)
    @property
    def duration_seconds(self) -> float:
        """Session duration in seconds."""
        end = self.ended_at or datetime.utcnow()
        return (end - self.started_at).total_seconds()

    @property
    def pages_viewed(self) -> int:
        """Number of pages viewed."""
        return len(self.navigation_history)

    @property
    def unique_pages_viewed(self) -> int:
        """Number of unique pages viewed."""
        return len(set(e.page_id for e in self.navigation_history))

    @property
    def queries_run(self) -> int:
        """Number of queries run."""
        return len(self.query_history)

    @property
    def operations_count(self) -> int:
        """Number of operations performed."""
        return len(self.operations)

    @property
    def is_active(self) -> bool:
        """Whether the session is still active."""
        return self.status == SessionStatus.ACTIVE

    def log_navigation(
        self,
        page_id: str,
        title: Optional[str] = None,
        source: str = "direct",
    ) -> NavigationEntry:
        """Log a page view.

        Args:
            page_id: Page that was viewed
            title: Page title (optional)
            source: How user arrived (search, link, direct)

        Returns:
            The created NavigationEntry
        """
        entry = NavigationEntry(
            page_id=page_id,
            title=title,
            source=source,
        )
        self.navigation_history.append(entry)
        return entry

    def log_query(
        self,
        query: str,
        result_count: int = 0,
        top_results: Optional[list[str]] = None,
        filters: Optional[dict] = None,
    ) -> QueryEntry:
        """Log a search query.

        Args:
            query: Search query text
            result_count: Number of results found
            top_results: Page IDs of top results
            filters: Applied filters (page_types, tags)

        Returns:
            The created QueryEntry
        """
        entry = QueryEntry(
            query=query,
            result_count=result_count,
            top_results=top_results or [],
            filters=filters or {},
        )
        self.query_history.append(entry)
        return entry

    def log_operation(
        self,
        kind: OperationKind,
        description: str,
        op_id: Optional[str] = None,
        details: Optional[dict] = None,
    ) -> OperationEntry:
        """Log an operation.

        Args:
            kind: Type of operation
            description: Human-readable description
            op_id: Reference to manifest entry
            details: Additional operation details

        Returns:
            The created OperationEntry
        """
        entry = OperationEntry(
            kind=kind,
            description=description,
            op_id=op_id,
            details=details or {},
        )
        self.operations.append(entry)
        return entry

    def set_focus(self, page_ids: list[str]) -> None:
        """Set the pages being actively worked on.

        Args:
            page_ids: Pages to focus on
        """
        self.focus_pages = page_ids

    def add_focus(self, page_id: str) -> None:
        """Add a page to focus list.

        Args:
            page_id: Page to add to focus
        """
        if page_id not in self.focus_pages:
            self.focus_pages.append(page_id)

    def remove_focus(self, page_id: str) -> None:
        """Remove a page from focus list.

        Args:
            page_id: Page to remove from focus
        """
        if page_id in self.focus_pages:
            self.focus_pages.remove(page_id)

    def set_context(self, context: str) -> None:
        """Set working context notes.

        Args:
            context: Free-form notes about current work
        """
        self.working_context = context

    def get_recent_pages(self, n: int = 5) -> list[str]:
        """Get the most recently viewed page IDs.

        Args:
            n: Number of pages to return

        Returns:
            List of recent page_ids (most recent first)
        """
        seen = []
        for entry in reversed(self.navigation_history):
            if entry.page_id not in seen:
                seen.append(entry.page_id)
                if len(seen) >= n:
                    break
        return seen

    def get_recent_queries(self, n: int = 5) -> list[str]:
        """Get the most recent query strings.

        Args:
            n: Number of queries to return

        Returns:
            List of recent query strings (most recent first)
        """
        return [e.query for e in reversed(self.query_history)][:n]

    def end(self) -> None:
        """End the session."""
        self.status = SessionStatus.ENDED
        self.ended_at = datetime.utcnow()

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "session_id": self.session_id,
            "wiki_root": str(self.wiki_root) if self.wiki_root else None,
            "started_at": self.started_at.isoformat() + "Z",
            "ended_at": self.ended_at.isoformat() + "Z" if self.ended_at else None,
            "status": self.status.value,
            "navigation_history": [e.to_dict() for e in self.navigation_history],
            "query_history": [e.to_dict() for e in self.query_history],
            "operations": [e.to_dict() for e in self.operations],
            "working_context": self.working_context,
            "focus_pages": self.focus_pages,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "SessionContext":
        """Create from dictionary."""
        ctx = cls(
            session_id=d["session_id"],
            wiki_root=Path(d["wiki_root"]) if d.get("wiki_root") else None,
            started_at=datetime.fromisoformat(d["started_at"].rstrip("Z")),
            ended_at=datetime.fromisoformat(d["ended_at"].rstrip("Z")) if d.get("ended_at") else None,
            status=SessionStatus(d["status"]),
            working_context=d.get("working_context", ""),
            focus_pages=d.get("focus_pages", []),
        )
        ctx.navigation_history = [NavigationEntry.from_dict(e) for e in d.get("navigation_history", [])]
        ctx.query_history = [QueryEntry.from_dict(e) for e in d.get("query_history", [])]
        ctx.operations = [OperationEntry.from_dict(e) for e in d.get("operations", [])]
        return ctx

    def summary(self) -> str:
        """Generate a human-readable summary of the session.

        Returns:
            Multi-line summary string
        """
        lines = [
            f"Session {self.session_id} ({self.status.value})",
            f"  Started: {self.started_at.isoformat()}",
        ]

        if self.ended_at:
            lines.append(f"  Ended: {self.ended_at.isoformat()}")

        duration_mins = self.duration_seconds / 60
        lines.append(f"  Duration: {duration_mins:.1f} minutes")
        lines.append(f"  Pages viewed: {self.pages_viewed} ({self.unique_pages_viewed} unique)")
        lines.append(f"  Queries run: {self.queries_run}")
        lines.append(f"  Operations: {self.operations_count}")

        if self.focus_pages:
            lines.append(f"  Focus pages: {', '.join(self.focus_pages)}")

        if self.working_context:
            lines.append(f"  Context: {self.working_context[:100]}...")

        return "\n".join(lines)


# Module-level session storage
_current_session: Optional[SessionContext] = None


def get_current_session() -> Optional[SessionContext]:
    """Get the current active session, if any.

    Returns:
        Current SessionContext or None if no session is active
    """
    global _current_session
    return _current_session


def set_current_session(session: Optional[SessionContext]) -> None:
    """Set the current session.

    Args:
        session: SessionContext to set as current, or None to clear
    """
    global _current_session
    _current_session = session


def create_session(wiki_root: Optional[Path] = None) -> SessionContext:
    """Create a new session.

    Args:
        wiki_root: Path to wiki root directory

    Returns:
        New SessionContext
    """
    return SessionContext(wiki_root=wiki_root)


def save_session_to_temp(session: SessionContext) -> Path:
    """Save session to a temporary file.

    Session data is Tier 3 (ephemeral) and stored in temp directory.

    Args:
        session: Session to save

    Returns:
        Path to the saved temp file
    """
    temp_dir = Path(tempfile.gettempdir()) / "llm_wiki_sessions"
    temp_dir.mkdir(parents=True, exist_ok=True)

    session_file = temp_dir / f"session_{session.session_id}.json"
    with open(session_file, "w") as f:
        json.dump(session.to_dict(), f, indent=2)

    return session_file


def load_session_from_temp(session_id: str) -> Optional[SessionContext]:
    """Load a session from temporary storage.

    Args:
        session_id: Session ID to load

    Returns:
        SessionContext if found, None otherwise
    """
    temp_dir = Path(tempfile.gettempdir()) / "llm_wiki_sessions"
    session_file = temp_dir / f"session_{session_id}.json"

    if not session_file.exists():
        return None

    with open(session_file) as f:
        data = json.load(f)

    return SessionContext.from_dict(data)


def list_temp_sessions() -> list[str]:
    """List session IDs in temporary storage.

    Returns:
        List of session IDs
    """
    temp_dir = Path(tempfile.gettempdir()) / "llm_wiki_sessions"
    if not temp_dir.exists():
        return []

    sessions = []
    for f in temp_dir.glob("session_*.json"):
        session_id = f.stem.replace("session_", "")
        sessions.append(session_id)

    return sessions


def cleanup_temp_sessions() -> int:
    """Remove all temporary session files.

    Returns:
        Number of files removed
    """
    temp_dir = Path(tempfile.gettempdir()) / "llm_wiki_sessions"
    if not temp_dir.exists():
        return 0

    count = 0
    for f in temp_dir.glob("session_*.json"):
        f.unlink()
        count += 1

    return count
