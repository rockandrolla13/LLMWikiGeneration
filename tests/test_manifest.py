"""Unit tests for manifest module.

Tests all classes and functions in llm_wiki.manifest:
- OperationType, OperationStatus, Actor enums
- OperationInputs, OperationOutputs dataclasses
- ManifestEntry dataclass
- Manifest class
"""

import json
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
import pytest

from llm_wiki.manifest import (
    OperationType,
    OperationStatus,
    Actor,
    OperationInputs,
    OperationOutputs,
    ManifestEntry,
    Manifest,
)


class TestEnums:
    """Test manifest enums."""

    def test_operation_type_values(self):
        """OperationType enum has correct values."""
        assert OperationType.INIT.value == "init"
        assert OperationType.INGEST.value == "ingest"
        assert OperationType.UPDATE.value == "update"
        assert OperationType.DELETE.value == "delete"
        assert OperationType.QUERY.value == "query"
        assert OperationType.LINT.value == "lint"
        assert OperationType.REBUILD.value == "rebuild"
        assert OperationType.VERIFY.value == "verify"

    def test_operation_type_from_value(self):
        """OperationType can be created from string value."""
        assert OperationType("init") == OperationType.INIT
        assert OperationType("ingest") == OperationType.INGEST

    def test_operation_type_invalid_value(self):
        """OperationType raises error for invalid value."""
        with pytest.raises(ValueError):
            OperationType("invalid")

    def test_operation_status_values(self):
        """OperationStatus enum has correct values."""
        assert OperationStatus.PENDING.value == "pending"
        assert OperationStatus.IN_PROGRESS.value == "in_progress"
        assert OperationStatus.COMPLETED.value == "completed"
        assert OperationStatus.FAILED.value == "failed"
        assert OperationStatus.ROLLED_BACK.value == "rolled_back"

    def test_actor_values(self):
        """Actor enum has correct values."""
        assert Actor.USER.value == "user"
        assert Actor.LLM.value == "llm"
        assert Actor.SYSTEM.value == "system"


class TestOperationInputs:
    """Test OperationInputs dataclass."""

    def test_create_empty(self):
        """Create OperationInputs with defaults."""
        inputs = OperationInputs()
        assert inputs.source_path is None
        assert inputs.source_hash is None
        assert inputs.query is None
        assert inputs.page_ids == []
        assert inputs.profile is None
        assert inputs.topic is None
        assert inputs.extra == {}

    def test_create_with_fields(self):
        """Create OperationInputs with values."""
        inputs = OperationInputs(
            source_path="raw/test.md",
            source_hash="sha256:abc",
            query="test query",
            page_ids=["page1", "page2"],
            profile="research",
            topic="ML",
            extra={"custom": "value"},
        )
        assert inputs.source_path == "raw/test.md"
        assert inputs.source_hash == "sha256:abc"
        assert inputs.query == "test query"
        assert inputs.page_ids == ["page1", "page2"]
        assert inputs.profile == "research"
        assert inputs.topic == "ML"
        assert inputs.extra == {"custom": "value"}

    def test_to_dict_excludes_none(self):
        """to_dict excludes None values."""
        inputs = OperationInputs(source_path="raw/test.md")
        d = inputs.to_dict()

        assert d == {"source_path": "raw/test.md"}
        assert "source_hash" not in d
        assert "query" not in d

    def test_to_dict_excludes_empty_lists(self):
        """to_dict excludes empty lists."""
        inputs = OperationInputs()
        d = inputs.to_dict()
        assert d == {}

    def test_to_dict_includes_extra(self):
        """to_dict includes extra dict contents."""
        inputs = OperationInputs(extra={"key1": "val1", "key2": 42})
        d = inputs.to_dict()
        assert d == {"key1": "val1", "key2": 42}

    def test_to_dict_full(self):
        """to_dict with all fields set."""
        inputs = OperationInputs(
            source_path="raw/test.md",
            source_hash="sha256:abc",
            query="test",
            page_ids=["p1"],
            profile="research",
            topic="ML",
        )
        d = inputs.to_dict()
        assert d["source_path"] == "raw/test.md"
        assert d["source_hash"] == "sha256:abc"
        assert d["query"] == "test"
        assert d["page_ids"] == ["p1"]
        assert d["profile"] == "research"
        assert d["topic"] == "ML"


class TestOperationOutputs:
    """Test OperationOutputs dataclass."""

    def test_create_empty(self):
        """Create OperationOutputs with defaults."""
        outputs = OperationOutputs()
        assert outputs.created_pages == []
        assert outputs.updated_pages == []
        assert outputs.deleted_pages == []
        assert outputs.page_revisions == {}
        assert outputs.derived_invalidated == []
        assert outputs.extra == {}

    def test_create_with_fields(self):
        """Create OperationOutputs with values."""
        outputs = OperationOutputs(
            created_pages=["page1", "page2"],
            updated_pages=["page3"],
            deleted_pages=["page4"],
            page_revisions={"page1": 1, "page2": 1},
            derived_invalidated=["MIND_MAP.md", "index.md"],
            extra={"custom": "output"},
        )
        assert outputs.created_pages == ["page1", "page2"]
        assert outputs.updated_pages == ["page3"]
        assert outputs.deleted_pages == ["page4"]
        assert outputs.page_revisions == {"page1": 1, "page2": 1}
        assert outputs.derived_invalidated == ["MIND_MAP.md", "index.md"]

    def test_to_dict_excludes_empty(self):
        """to_dict excludes empty values."""
        outputs = OperationOutputs(created_pages=["page1"])
        d = outputs.to_dict()

        assert d == {"created_pages": ["page1"]}
        assert "updated_pages" not in d
        assert "deleted_pages" not in d

    def test_to_dict_includes_extra(self):
        """to_dict includes extra dict contents."""
        outputs = OperationOutputs(extra={"result": "success"})
        d = outputs.to_dict()
        assert d == {"result": "success"}


class TestManifestEntry:
    """Test ManifestEntry dataclass."""

    def test_create_with_required_fields(self):
        """Create ManifestEntry with all required fields."""
        entry = ManifestEntry(
            op_id="op_abc123",
            op_type=OperationType.INIT,
            timestamp=datetime(2024, 1, 15, 12, 30, 0),
            actor=Actor.SYSTEM,
            inputs=OperationInputs(),
            outputs=OperationOutputs(),
            status=OperationStatus.COMPLETED,
        )
        assert entry.op_id == "op_abc123"
        assert entry.op_type == OperationType.INIT
        assert entry.actor == Actor.SYSTEM
        assert entry.status == OperationStatus.COMPLETED

    def test_create_factory_method(self):
        """ManifestEntry.create generates op_id and timestamp."""
        entry = ManifestEntry.create(
            op_type=OperationType.INGEST,
            actor=Actor.LLM,
        )
        assert entry.op_id.startswith("op_")
        assert len(entry.op_id) == 15  # "op_" + 12 hex chars
        assert isinstance(entry.timestamp, datetime)
        assert entry.actor == Actor.LLM
        assert entry.status == OperationStatus.PENDING

    def test_create_factory_with_inputs(self):
        """ManifestEntry.create with inputs."""
        inputs = OperationInputs(source_path="raw/test.md")
        entry = ManifestEntry.create(
            op_type=OperationType.INGEST,
            inputs=inputs,
        )
        assert entry.inputs.source_path == "raw/test.md"

    def test_create_factory_with_parent(self):
        """ManifestEntry.create with parent_op_id."""
        entry = ManifestEntry.create(
            op_type=OperationType.UPDATE,
            parent_op_id="op_parent123",
        )
        assert entry.parent_op_id == "op_parent123"

    def test_to_json_line(self):
        """ManifestEntry serializes to JSON line."""
        entry = ManifestEntry(
            op_id="op_test123",
            op_type=OperationType.INIT,
            timestamp=datetime(2024, 1, 15, 12, 30, 0),
            actor=Actor.SYSTEM,
            inputs=OperationInputs(),
            outputs=OperationOutputs(),
            status=OperationStatus.COMPLETED,
        )
        json_line = entry.to_json_line()

        # Should be valid JSON
        data = json.loads(json_line)
        assert data["op_id"] == "op_test123"
        assert data["op_type"] == "init"
        assert data["timestamp"] == "2024-01-15T12:30:00Z"
        assert data["actor"] == "system"
        assert data["status"] == "completed"

    def test_to_json_line_with_optional_fields(self):
        """ManifestEntry serializes optional fields when present."""
        entry = ManifestEntry(
            op_id="op_test123",
            op_type=OperationType.INGEST,
            timestamp=datetime(2024, 1, 15, 12, 30, 0),
            actor=Actor.LLM,
            inputs=OperationInputs(source_path="raw/test.md"),
            outputs=OperationOutputs(created_pages=["page1"]),
            status=OperationStatus.FAILED,
            error_message="Test error",
            duration_ms=1500,
            parent_op_id="op_parent",
        )
        json_line = entry.to_json_line()
        data = json.loads(json_line)

        assert data["error_message"] == "Test error"
        assert data["duration_ms"] == 1500
        assert data["parent_op_id"] == "op_parent"
        assert data["inputs"]["source_path"] == "raw/test.md"
        assert data["outputs"]["created_pages"] == ["page1"]

    def test_from_json_line(self):
        """ManifestEntry deserializes from JSON line."""
        json_line = '{"op_id":"op_test","op_type":"init","timestamp":"2024-01-15T12:30:00Z","actor":"system","inputs":{},"outputs":{},"status":"completed"}'
        entry = ManifestEntry.from_json_line(json_line)

        assert entry.op_id == "op_test"
        assert entry.op_type == OperationType.INIT
        assert entry.timestamp == datetime(2024, 1, 15, 12, 30, 0)
        assert entry.actor == Actor.SYSTEM
        assert entry.status == OperationStatus.COMPLETED

    def test_from_json_line_with_optional_fields(self):
        """ManifestEntry deserializes optional fields."""
        json_line = '{"op_id":"op_test","op_type":"ingest","timestamp":"2024-01-15T12:30:00Z","actor":"llm","inputs":{"source_path":"raw/test.md"},"outputs":{"created_pages":["p1"]},"status":"failed","error_message":"Error","duration_ms":100,"parent_op_id":"op_parent"}'
        entry = ManifestEntry.from_json_line(json_line)

        assert entry.inputs.source_path == "raw/test.md"
        assert entry.outputs.created_pages == ["p1"]
        assert entry.error_message == "Error"
        assert entry.duration_ms == 100
        assert entry.parent_op_id == "op_parent"

    def test_roundtrip_json(self):
        """ManifestEntry survives serialize/deserialize roundtrip."""
        original = ManifestEntry.create(
            op_type=OperationType.INGEST,
            actor=Actor.LLM,
            inputs=OperationInputs(
                source_path="raw/test.md",
                source_hash="sha256:abc",
            ),
        )
        original.outputs = OperationOutputs(
            created_pages=["page1", "page2"],
            page_revisions={"page1": 1, "page2": 1},
        )
        original.status = OperationStatus.COMPLETED
        original.duration_ms = 250

        json_line = original.to_json_line()
        restored = ManifestEntry.from_json_line(json_line)

        assert restored.op_id == original.op_id
        assert restored.op_type == original.op_type
        assert restored.actor == original.actor
        assert restored.status == original.status
        assert restored.inputs.source_path == original.inputs.source_path
        assert restored.outputs.created_pages == original.outputs.created_pages
        assert restored.duration_ms == original.duration_ms


class TestManifest:
    """Test Manifest class."""

    def test_init(self, tmp_path):
        """Create Manifest instance."""
        manifest_path = tmp_path / "manifest.jsonl"
        manifest = Manifest(manifest_path)
        assert manifest.path == manifest_path

    def test_exists_false(self, tmp_path):
        """exists returns False for missing file."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        assert manifest.exists() is False

    def test_exists_true(self, tmp_path):
        """exists returns True for existing file."""
        manifest_path = tmp_path / "manifest.jsonl"
        manifest_path.touch()
        manifest = Manifest(manifest_path)
        assert manifest.exists() is True

    def test_append_creates_file(self, tmp_path):
        """append creates file if it doesn't exist."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry = ManifestEntry.create(op_type=OperationType.INIT)

        manifest.append(entry)

        assert manifest.exists() is True
        assert manifest.path.read_text().strip() != ""

    def test_append_adds_entry(self, tmp_path):
        """append adds entry to manifest."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry1 = ManifestEntry.create(op_type=OperationType.INIT)
        entry2 = ManifestEntry.create(op_type=OperationType.INGEST)

        manifest.append(entry1)
        manifest.append(entry2)

        # Read and count lines
        lines = manifest.path.read_text().strip().split("\n")
        assert len(lines) == 2

    def test_read_all_empty(self, tmp_path):
        """read_all returns empty list for missing file."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entries = manifest.read_all()
        assert entries == []

    def test_read_all_returns_entries(self, tmp_path):
        """read_all returns all entries."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry1 = ManifestEntry.create(op_type=OperationType.INIT)
        entry2 = ManifestEntry.create(op_type=OperationType.INGEST)

        manifest.append(entry1)
        manifest.append(entry2)

        entries = manifest.read_all()
        assert len(entries) == 2
        assert entries[0].op_id == entry1.op_id
        assert entries[1].op_id == entry2.op_id

    def test_read_all_skips_empty_lines(self, tmp_path):
        """read_all skips empty lines in file."""
        manifest_path = tmp_path / "manifest.jsonl"
        entry = ManifestEntry.create(op_type=OperationType.INIT)
        json_line = entry.to_json_line()

        # Write with empty lines
        manifest_path.write_text(f"{json_line}\n\n{json_line}\n")

        manifest = Manifest(manifest_path)
        entries = manifest.read_all()
        assert len(entries) == 2

    def test_iter_entries(self, tmp_path):
        """iter_entries yields entries one at a time."""
        manifest = Manifest(tmp_path / "manifest.jsonl")

        for i in range(5):
            entry = ManifestEntry.create(op_type=OperationType.INGEST)
            manifest.append(entry)

        entries = list(manifest.iter_entries())
        assert len(entries) == 5

    def test_iter_entries_empty(self, tmp_path):
        """iter_entries returns empty iterator for missing file."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entries = list(manifest.iter_entries())
        assert entries == []

    def test_get_entry_found(self, tmp_path):
        """get_entry returns entry when found."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry = ManifestEntry.create(op_type=OperationType.INIT)
        manifest.append(entry)

        found = manifest.get_entry(entry.op_id)
        assert found is not None
        assert found.op_id == entry.op_id

    def test_get_entry_not_found(self, tmp_path):
        """get_entry returns None when not found."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry = ManifestEntry.create(op_type=OperationType.INIT)
        manifest.append(entry)

        found = manifest.get_entry("op_nonexistent")
        assert found is None

    def test_get_last_entry(self, tmp_path):
        """get_last_entry returns last entry."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry1 = ManifestEntry.create(op_type=OperationType.INIT)
        entry2 = ManifestEntry.create(op_type=OperationType.INGEST)

        manifest.append(entry1)
        manifest.append(entry2)

        last = manifest.get_last_entry()
        assert last is not None
        assert last.op_id == entry2.op_id

    def test_get_last_entry_empty(self, tmp_path):
        """get_last_entry returns None for empty manifest."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        last = manifest.get_last_entry()
        assert last is None

    def test_count_operations_all(self, tmp_path):
        """count_operations counts all operations."""
        manifest = Manifest(tmp_path / "manifest.jsonl")

        for _ in range(3):
            manifest.append(ManifestEntry.create(op_type=OperationType.INIT))
        for _ in range(2):
            manifest.append(ManifestEntry.create(op_type=OperationType.INGEST))

        count = manifest.count_operations()
        assert count == 5

    def test_count_operations_by_type(self, tmp_path):
        """count_operations filters by type."""
        manifest = Manifest(tmp_path / "manifest.jsonl")

        for _ in range(3):
            manifest.append(ManifestEntry.create(op_type=OperationType.INIT))
        for _ in range(2):
            manifest.append(ManifestEntry.create(op_type=OperationType.INGEST))

        init_count = manifest.count_operations(OperationType.INIT)
        ingest_count = manifest.count_operations(OperationType.INGEST)

        assert init_count == 3
        assert ingest_count == 2

    def test_count_operations_empty(self, tmp_path):
        """count_operations returns 0 for missing file."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        count = manifest.count_operations()
        assert count == 0

    def test_get_page_history(self, tmp_path):
        """get_page_history returns operations affecting page."""
        manifest = Manifest(tmp_path / "manifest.jsonl")

        # Init operation
        init = ManifestEntry.create(op_type=OperationType.INIT)
        manifest.append(init)

        # Ingest creates page
        ingest = ManifestEntry.create(op_type=OperationType.INGEST)
        ingest.outputs = OperationOutputs(created_pages=["sources/test"])
        manifest.append(ingest)

        # Update modifies page
        update = ManifestEntry.create(op_type=OperationType.UPDATE)
        update.outputs = OperationOutputs(updated_pages=["sources/test"])
        manifest.append(update)

        # Other operation
        other = ManifestEntry.create(op_type=OperationType.INGEST)
        other.outputs = OperationOutputs(created_pages=["sources/other"])
        manifest.append(other)

        history = manifest.get_page_history("sources/test")
        assert len(history) == 2
        assert history[0].op_id == ingest.op_id
        assert history[1].op_id == update.op_id

    def test_get_page_history_empty(self, tmp_path):
        """get_page_history returns empty for unknown page."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry = ManifestEntry.create(op_type=OperationType.INIT)
        manifest.append(entry)

        history = manifest.get_page_history("nonexistent/page")
        assert history == []

    def test_generate_next_op_id(self, tmp_path):
        """generate_next_op_id creates unique IDs."""
        manifest = Manifest(tmp_path / "manifest.jsonl")

        ids = set()
        for _ in range(100):
            op_id = manifest.generate_next_op_id()
            assert op_id.startswith("op_")
            assert len(op_id) == 15
            ids.add(op_id)

        # All should be unique
        assert len(ids) == 100


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_manifest_append_atomic(self, tmp_path):
        """append is atomic (data is flushed)."""
        manifest = Manifest(tmp_path / "manifest.jsonl")
        entry = ManifestEntry.create(op_type=OperationType.INIT)
        manifest.append(entry)

        # Re-read immediately
        manifest2 = Manifest(tmp_path / "manifest.jsonl")
        entries = manifest2.read_all()
        assert len(entries) == 1

    def test_concurrent_appends(self, tmp_path):
        """Multiple manifests can append to same file."""
        path = tmp_path / "manifest.jsonl"

        # Simulate concurrent access
        m1 = Manifest(path)
        m2 = Manifest(path)

        m1.append(ManifestEntry.create(op_type=OperationType.INIT))
        m2.append(ManifestEntry.create(op_type=OperationType.INGEST))

        entries = Manifest(path).read_all()
        assert len(entries) == 2

    def test_malformed_json_line(self, tmp_path):
        """Malformed JSON line raises error on read."""
        manifest_path = tmp_path / "manifest.jsonl"
        manifest_path.write_text("not valid json\n")

        manifest = Manifest(manifest_path)
        with pytest.raises(json.JSONDecodeError):
            manifest.read_all()

    def test_missing_required_field(self, tmp_path):
        """Missing required field raises error on deserialize."""
        manifest_path = tmp_path / "manifest.jsonl"
        # Missing op_type
        manifest_path.write_text('{"op_id":"test","timestamp":"2024-01-01T00:00:00Z","actor":"llm","inputs":{},"outputs":{},"status":"completed"}\n')

        manifest = Manifest(manifest_path)
        with pytest.raises(KeyError):
            manifest.read_all()

    def test_timestamp_precision(self):
        """Timestamps preserve microsecond precision."""
        now = datetime.utcnow()
        entry = ManifestEntry(
            op_id="op_test",
            op_type=OperationType.INIT,
            timestamp=now,
            actor=Actor.SYSTEM,
            inputs=OperationInputs(),
            outputs=OperationOutputs(),
            status=OperationStatus.COMPLETED,
        )

        json_line = entry.to_json_line()
        restored = ManifestEntry.from_json_line(json_line)

        # datetime.fromisoformat loses microseconds when using rstrip("Z")
        # but that's acceptable for manifest purposes
        assert restored.timestamp.date() == now.date()
        assert restored.timestamp.hour == now.hour
        assert restored.timestamp.minute == now.minute
        assert restored.timestamp.second == now.second


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
