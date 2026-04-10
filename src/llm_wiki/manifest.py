"""Manifest schema and append logic for LLM Wiki.

The manifest.jsonl is the operation ledger - an append-only log of all
wiki operations. It's the only non-markdown canonical artifact (Tier 1).

Format: JSON Lines (one JSON object per line)
"""

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
            timestamp=datetime.utcnow(),
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
        """Deserialize from a JSON line."""
        d = json.loads(line)
        return cls(
            op_id=d["op_id"],
            op_type=OperationType(d["op_type"]),
            timestamp=datetime.fromisoformat(d["timestamp"].rstrip("Z")),
            actor=Actor(d["actor"]),
            inputs=OperationInputs(
                source_path=d.get("inputs", {}).get("source_path"),
                source_hash=d.get("inputs", {}).get("source_hash"),
                query=d.get("inputs", {}).get("query"),
                page_ids=d.get("inputs", {}).get("page_ids", []),
                profile=d.get("inputs", {}).get("profile"),
                topic=d.get("inputs", {}).get("topic"),
            ),
            outputs=OperationOutputs(
                created_pages=d.get("outputs", {}).get("created_pages", []),
                updated_pages=d.get("outputs", {}).get("updated_pages", []),
                deleted_pages=d.get("outputs", {}).get("deleted_pages", []),
                page_revisions=d.get("outputs", {}).get("page_revisions", {}),
                derived_invalidated=d.get("outputs", {}).get("derived_invalidated", []),
            ),
            status=OperationStatus(d["status"]),
            error_message=d.get("error_message"),
            duration_ms=d.get("duration_ms"),
            parent_op_id=d.get("parent_op_id"),
        )


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
                    entries.append(ManifestEntry.from_json_line(line))
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
                    yield ManifestEntry.from_json_line(line)

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
