"""Manifest schema and append logic for LLM Wiki.

The manifest.jsonl is the operation ledger - an append-only log of all
wiki operations. It's the only non-markdown canonical artifact (Tier 1).

Format: JSON Lines (one JSON object per line)
"""

from .clock import utc_now
import json
import os
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, Iterator


class OperationType(Enum):
    """Types of wiki operations."""
    INIT = "init"
    INGEST = "ingest"
    BATCH_INGEST = "batch_ingest"
    UPDATE = "update"
    DELETE = "delete"
    QUERY = "query"
    LINT = "lint"
    REBUILD = "rebuild"
    VERIFY = "verify"


class OperationStatus(Enum):
    """Status of an operation."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


class Actor(Enum):
    """Who performed the operation."""
    USER = "user"
    LLM = "llm"
    SYSTEM = "system"


@dataclass
class OperationInputs:
    """Inputs to an operation."""
    source_path: Optional[str] = None
    source_hash: Optional[str] = None
    query: Optional[str] = None
    page_ids: list[str] = field(default_factory=list)
    profile: Optional[str] = None
    topic: Optional[str] = None
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary, excluding None values."""
        d = {}
        if self.source_path:
            d["source_path"] = self.source_path
        if self.source_hash:
            d["source_hash"] = self.source_hash
        if self.query:
            d["query"] = self.query
        if self.page_ids:
            d["page_ids"] = self.page_ids
        if self.profile:
            d["profile"] = self.profile
        if self.topic:
            d["topic"] = self.topic
        if self.extra:
            d.update(self.extra)
        return d


@dataclass
class OperationOutputs:
    """Outputs from an operation."""
    created_pages: list[str] = field(default_factory=list)  # page_ids
    updated_pages: list[str] = field(default_factory=list)  # page_ids
    deleted_pages: list[str] = field(default_factory=list)  # page_ids
    page_revisions: dict[str, int] = field(default_factory=dict)  # {page_id: revision_id}
    derived_invalidated: list[str] = field(default_factory=list)  # ["MIND_MAP.md", "index.md", etc]
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary, excluding empty values."""
        d = {}
        if self.created_pages:
            d["created_pages"] = self.created_pages
        if self.updated_pages:
            d["updated_pages"] = self.updated_pages
        if self.deleted_pages:
            d["deleted_pages"] = self.deleted_pages
        if self.page_revisions:
            d["page_revisions"] = self.page_revisions
        if self.derived_invalidated:
            d["derived_invalidated"] = self.derived_invalidated
        if self.extra:
            d.update(self.extra)
        return d


@dataclass
class ManifestEntry:
    """A single entry in the manifest (one operation).

    Each entry records a complete operation with its inputs,
    outputs, and status. This provides full audit trail and
    enables recovery/replay if needed.
    """
    op_id: str
    op_type: OperationType
    timestamp: datetime
    actor: Actor
    inputs: OperationInputs
    outputs: OperationOutputs
    status: OperationStatus
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    parent_op_id: Optional[str] = None  # For nested operations

    @classmethod
    def create(
        cls,
        op_type: OperationType,
        actor: Actor = Actor.LLM,
        inputs: Optional[OperationInputs] = None,
        parent_op_id: Optional[str] = None,
    ) -> "ManifestEntry":
        """Create a new manifest entry with generated op_id and timestamp."""
        return cls(
            op_id=f"op_{uuid.uuid4().hex[:12]}",
            op_type=op_type,
            timestamp=utc_now(),
            actor=actor,
            inputs=inputs or OperationInputs(),
            outputs=OperationOutputs(),
            status=OperationStatus.PENDING,
            parent_op_id=parent_op_id,
        )

    def to_json_line(self) -> str:
        """Serialize to a single JSON line."""
        d = {
            "op_id": self.op_id,
            "op_type": self.op_type.value,
            "timestamp": self.timestamp.isoformat() + "Z",
            "actor": self.actor.value,
            "inputs": self.inputs.to_dict(),
            "outputs": self.outputs.to_dict(),
            "status": self.status.value,
        }
        if self.error_message:
            d["error_message"] = self.error_message
        if self.duration_ms is not None:
            d["duration_ms"] = self.duration_ms
        if self.parent_op_id:
            d["parent_op_id"] = self.parent_op_id
        return json.dumps(d, separators=(",", ":"))

    @classmethod
    def from_json_line(cls, line: str) -> "ManifestEntry":
        """Deserialize from a JSON line.

        Handles two on-disk shapes:

        - Current: has `op_type`, `actor`, `inputs`, `outputs`, `status`.
        - Legacy: hand-written entries with `operation` and `page_id` and no
          actor/status. These predate the current schema and appear in wikis
          whose pages were authored directly rather than through wiki_ingest.
          Raising on them made every manifest-reading command unusable.

        The manifest is append-only, so legacy entries are read in place and
        never rewritten.
        """
        return cls.from_dict(json.loads(line))

    @classmethod
    def from_dict(cls, d: dict) -> "ManifestEntry":
        """Build an entry from an already-decoded manifest object."""
        if "op_type" not in d:
            return cls._from_legacy_dict(d)
        inputs = d.get("inputs") or {}
        outputs = d.get("outputs") or {}
        return cls(
            op_id=d["op_id"],
            op_type=_coerce_op_type(d["op_type"]),
            timestamp=datetime.fromisoformat(d["timestamp"].rstrip("Z")),
            # actor and status are absent on entries written by batch tooling.
            # They are descriptive, not load-bearing, so default rather than
            # make one missing key cost the whole ledger.
            actor=_coerce_enum(Actor, d.get("actor"), Actor.LLM),
            inputs=OperationInputs(
                source_path=inputs.get("source_path"),
                source_hash=inputs.get("source_hash"),
                query=inputs.get("query"),
                page_ids=inputs.get("page_ids", []),
                profile=inputs.get("profile"),
                topic=inputs.get("topic"),
            ),
            outputs=OperationOutputs(
                created_pages=outputs.get("created_pages", []),
                updated_pages=outputs.get("updated_pages", []),
                deleted_pages=outputs.get("deleted_pages", []),
                page_revisions=outputs.get("page_revisions", {}),
                derived_invalidated=outputs.get("derived_invalidated", []),
            ),
            status=_coerce_enum(OperationStatus, d.get("status"), OperationStatus.COMPLETED),
            error_message=d.get("error_message"),
            duration_ms=d.get("duration_ms"),
            parent_op_id=d.get("parent_op_id"),
        )

    @classmethod
    def _from_legacy_dict(cls, d: dict) -> "ManifestEntry":
        """Build an entry from a legacy hand-written manifest line.

        Legacy shape:
            {"op_id", "timestamp", "operation", "page_id", "revision_id", "comment"}

        Legacy entries record completed page authoring, so they are read as
        actor=llm, status=completed. `operation` maps onto the closest
        OperationType; unrecognised values fall back to UPDATE.
        """
        operation = (d.get("operation") or "").lower()
        op_type = _LEGACY_OPERATION_TYPES.get(operation, OperationType.UPDATE)

        page_id = d.get("page_id")
        page_ids = [page_id] if page_id else []
        revision_id = d.get("revision_id")

        outputs = OperationOutputs()
        if op_type is OperationType.DELETE:
            outputs.deleted_pages = page_ids
        elif operation == "create":
            outputs.created_pages = page_ids
        else:
            outputs.updated_pages = page_ids
        if page_id and revision_id is not None:
            outputs.page_revisions = {page_id: revision_id}

        # Preserve the human-written note. It is not an error, so it must not
        # land in error_message.
        comment = d.get("comment")
        if comment:
            outputs.extra = {"comment": comment}

        return cls(
            op_id=d["op_id"],
            op_type=op_type,
            timestamp=datetime.fromisoformat(d["timestamp"].rstrip("Z")),
            actor=Actor(d.get("actor", Actor.LLM.value)),
            inputs=OperationInputs(page_ids=page_ids),
            outputs=outputs,
            status=OperationStatus(d.get("status", OperationStatus.COMPLETED.value)),
        )


# Maps the legacy `operation` field onto the current OperationType enum.
# "create" records page authoring, which ingest is the closest analogue of.
_LEGACY_OPERATION_TYPES = {
    "create": OperationType.INGEST,
    "ingest": OperationType.INGEST,
    "update": OperationType.UPDATE,
    "delete": OperationType.DELETE,
    "init": OperationType.INIT,
}


def _coerce_enum(enum_cls, value, default):
    """Return enum_cls(value), or `default` when value is missing/unrecognised."""
    if value is None:
        return default
    try:
        return enum_cls(value)
    except ValueError:
        return default


def _coerce_op_type(value: str) -> OperationType:
    """Map an on-disk op_type onto the enum without crashing on new values.

    The ledger is append-only and written by several tools over time, so it
    contains operation names the enum does not know. Raising made the whole
    manifest unreadable because of a handful of rows; unknown names degrade to
    UPDATE so the surrounding history stays readable.
    """
    try:
        return OperationType(value)
    except ValueError:
        return OperationType.UPDATE


def _iter_json_objects(line: str) -> Iterator[dict]:
    """Yield every JSON object on a single manifest line.

    The format is one object per line, but a batch append once wrote two
    objects onto the same line with no separator. json.loads rejects the whole
    line ("Extra data"), which made the entire manifest unreadable and took
    wiki_stats and verify_wiki down with it. raw_decode consumes one object at
    a time so a missing newline costs nothing.

    Args:
        line: A stripped line from manifest.jsonl

    Yields:
        Each decoded JSON object found on the line, in order

    Raises:
        json.JSONDecodeError: If the remaining text is not valid JSON
    """
    decoder = json.JSONDecoder()
    idx = 0
    end = len(line)
    while idx < end:
        obj, idx = decoder.raw_decode(line, idx)
        yield obj
        while idx < end and line[idx].isspace():
            idx += 1


class Manifest:
    """Interface for reading and appending to manifest.jsonl.

    The manifest is append-only - entries are never modified or deleted.
    This ensures a complete audit trail of all wiki operations.
    """

    def __init__(self, manifest_path: Path):
        """Initialize manifest at given path.

        Args:
            manifest_path: Path to manifest.jsonl file
        """
        self.path = manifest_path

    def exists(self) -> bool:
        """Check if manifest file exists."""
        return self.path.exists()

    def append(self, entry: ManifestEntry) -> None:
        """Append an entry to the manifest.

        This is an atomic append operation - the entry is written
        with a newline and flushed immediately.

        Args:
            entry: The manifest entry to append
        """
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(entry.to_json_line() + "\n")
            f.flush()
            os.fsync(f.fileno())

    def read_all(self) -> list[ManifestEntry]:
        """Read all entries from the manifest.

        Returns:
            List of all manifest entries in order
        """
        if not self.exists():
            return []
        entries = []
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    entries.extend(
                        ManifestEntry.from_dict(o) for o in _iter_json_objects(line)
                    )
        return entries

    def iter_entries(self) -> Iterator[ManifestEntry]:
        """Iterate over entries without loading all into memory.

        Yields:
            ManifestEntry objects one at a time
        """
        if not self.exists():
            return
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    for obj in _iter_json_objects(line):
                        yield ManifestEntry.from_dict(obj)

    def get_entry(self, op_id: str) -> Optional[ManifestEntry]:
        """Get a specific entry by op_id.

        Args:
            op_id: The operation ID to look up

        Returns:
            The matching entry, or None if not found
        """
        for entry in self.iter_entries():
            if entry.op_id == op_id:
                return entry
        return None

    def get_last_entry(self) -> Optional[ManifestEntry]:
        """Get the most recent entry.

        Returns:
            The last entry, or None if manifest is empty
        """
        last = None
        for entry in self.iter_entries():
            last = entry
        return last

    def count_operations(self, op_type: Optional[OperationType] = None) -> int:
        """Count operations, optionally filtered by type.

        Args:
            op_type: If provided, only count this operation type

        Returns:
            Number of matching operations
        """
        count = 0
        for entry in self.iter_entries():
            if op_type is None or entry.op_type == op_type:
                count += 1
        return count

    def get_page_history(self, page_id: str) -> list[ManifestEntry]:
        """Get all operations that affected a specific page.

        Args:
            page_id: The page ID to look up

        Returns:
            List of operations that created/updated/deleted the page
        """
        history = []
        for entry in self.iter_entries():
            if (
                page_id in entry.outputs.created_pages
                or page_id in entry.outputs.updated_pages
                or page_id in entry.outputs.deleted_pages
            ):
                history.append(entry)
        return history

    def generate_next_op_id(self) -> str:
        """Generate a unique operation ID.

        Returns:
            A new unique op_id string
        """
        return f"op_{uuid.uuid4().hex[:12]}"
