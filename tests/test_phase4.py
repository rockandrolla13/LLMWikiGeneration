"""Tests for Phase 4: Session Context (Tier 3 - Ephemeral).

Tests the session context functionality:
- SessionContext dataclass
- Session start/end tracking
- Navigation history
- Query history
- Operations log
- Temp file storage

Key principle: If session data is lost, the wiki is still 100% functional.
"""

from datetime import datetime
from pathlib import Path
import pytest
import time

from llm_wiki import (
    Wiki,
    wiki_init,
    wiki_ingest,
    wiki_query,
    # Session commands
    wiki_session_start,
    wiki_session_end,
    wiki_session_status,
    wiki_session_log_navigation,
    wiki_session_log_query,
    wiki_session_set_context,
    # Session classes
    SessionContext,
    SessionStatus,
    NavigationEntry,
    QueryEntry,
    OperationEntry,
    OperationKind,
    get_current_session,
    set_current_session,
    create_session,
    save_session_to_temp,
    load_session_from_temp,
    list_temp_sessions,
    cleanup_temp_sessions,
)


class TestSessionContext:
    """Test the SessionContext dataclass."""

    def test_create_session(self):
        """Session can be created with default values."""
        session = SessionContext()

        assert session.session_id  # Has an ID
        assert len(session.session_id) == 8  # 8 char ID
        assert session.status == SessionStatus.ACTIVE
        assert session.is_active is True
        assert session.started_at is not None
        assert session.ended_at is None
        assert session.pages_viewed == 0
        assert session.queries_run == 0
        assert session.operations_count == 0

    def test_create_session_with_wiki_root(self, tmp_path):
        """Session can be created with wiki root."""
        session = SessionContext(wiki_root=tmp_path)

        assert session.wiki_root == tmp_path

    def test_session_log_navigation(self):
        """Session can log page views."""
        session = SessionContext()

        entry = session.log_navigation("concepts/ml", title="Machine Learning", source="search")

        assert entry.page_id == "concepts/ml"
        assert entry.title == "Machine Learning"
        assert entry.source == "search"
        assert session.pages_viewed == 1
        assert session.unique_pages_viewed == 1

        # Log same page again
        session.log_navigation("concepts/ml")
        assert session.pages_viewed == 2
        assert session.unique_pages_viewed == 1  # Still 1 unique

        # Log different page
        session.log_navigation("entities/john")
        assert session.pages_viewed == 3
        assert session.unique_pages_viewed == 2

    def test_session_log_query(self):
        """Session can log search queries."""
        session = SessionContext()

        entry = session.log_query(
            "machine learning",
            result_count=5,
            top_results=["concepts/ml", "sources/paper1"],
            filters={"page_types": ["concept"]},
        )

        assert entry.query == "machine learning"
        assert entry.result_count == 5
        assert len(entry.top_results) == 2
        assert session.queries_run == 1

    def test_session_log_operation(self):
        """Session can log operations."""
        session = SessionContext()

        entry = session.log_operation(
            kind=OperationKind.INGEST,
            description="Ingested paper.pdf",
            op_id="op_123",
            details={"source": "raw/paper.pdf"},
        )

        assert entry.kind == OperationKind.INGEST
        assert entry.description == "Ingested paper.pdf"
        assert entry.op_id == "op_123"
        assert session.operations_count == 1

    def test_session_focus_pages(self):
        """Session can track focus pages."""
        session = SessionContext()

        session.set_focus(["concepts/ml", "concepts/nn"])
        assert session.focus_pages == ["concepts/ml", "concepts/nn"]

        session.add_focus("concepts/dl")
        assert "concepts/dl" in session.focus_pages

        session.remove_focus("concepts/ml")
        assert "concepts/ml" not in session.focus_pages

    def test_session_working_context(self):
        """Session can store working context."""
        session = SessionContext()

        session.set_context("Working on ML chapter")
        assert session.working_context == "Working on ML chapter"

    def test_session_end(self):
        """Session can be ended."""
        session = SessionContext()
        assert session.is_active is True

        session.end()

        assert session.is_active is False
        assert session.status == SessionStatus.ENDED
        assert session.ended_at is not None
        assert session.duration_seconds >= 0

    def test_session_duration(self):
        """Session tracks duration."""
        session = SessionContext()

        time.sleep(0.1)  # Wait a bit
        duration = session.duration_seconds

        assert duration >= 0.1

    def test_session_get_recent_pages(self):
        """Session returns recent unique pages."""
        session = SessionContext()

        session.log_navigation("page1")
        session.log_navigation("page2")
        session.log_navigation("page1")  # Revisit
        session.log_navigation("page3")
        session.log_navigation("page4")
        session.log_navigation("page5")
        session.log_navigation("page6")

        recent = session.get_recent_pages(3)
        assert len(recent) == 3
        assert recent[0] == "page6"  # Most recent first
        assert recent[1] == "page5"
        assert recent[2] == "page4"

    def test_session_get_recent_queries(self):
        """Session returns recent queries."""
        session = SessionContext()

        session.log_query("query1")
        session.log_query("query2")
        session.log_query("query3")

        recent = session.get_recent_queries(2)
        assert len(recent) == 2
        assert recent[0] == "query3"  # Most recent first
        assert recent[1] == "query2"


class TestSessionSerialization:
    """Test session serialization/deserialization."""

    def test_session_to_dict(self):
        """Session can be converted to dict."""
        session = SessionContext()
        session.log_navigation("page1")
        session.log_query("test query")

        d = session.to_dict()

        assert d["session_id"] == session.session_id
        assert d["status"] == "active"
        assert len(d["navigation_history"]) == 1
        assert len(d["query_history"]) == 1

    def test_session_from_dict(self):
        """Session can be restored from dict."""
        original = SessionContext()
        original.log_navigation("page1", title="Page One")
        original.log_query("test query", result_count=5)
        original.set_context("Working on tests")

        d = original.to_dict()
        restored = SessionContext.from_dict(d)

        assert restored.session_id == original.session_id
        assert restored.pages_viewed == 1
        assert restored.queries_run == 1
        assert restored.working_context == "Working on tests"

    def test_navigation_entry_serialization(self):
        """NavigationEntry can be serialized/deserialized."""
        entry = NavigationEntry(
            page_id="concepts/ml",
            title="Machine Learning",
            source="search",
        )

        d = entry.to_dict()
        restored = NavigationEntry.from_dict(d)

        assert restored.page_id == entry.page_id
        assert restored.title == entry.title
        assert restored.source == entry.source

    def test_query_entry_serialization(self):
        """QueryEntry can be serialized/deserialized."""
        entry = QueryEntry(
            query="machine learning",
            result_count=5,
            top_results=["page1", "page2"],
            filters={"page_types": ["concept"]},
        )

        d = entry.to_dict()
        restored = QueryEntry.from_dict(d)

        assert restored.query == entry.query
        assert restored.result_count == entry.result_count
        assert restored.top_results == entry.top_results

    def test_operation_entry_serialization(self):
        """OperationEntry can be serialized/deserialized."""
        entry = OperationEntry(
            kind=OperationKind.INGEST,
            description="Ingested paper",
            op_id="op_123",
            details={"source": "raw/paper.pdf"},
        )

        d = entry.to_dict()
        restored = OperationEntry.from_dict(d)

        assert restored.kind == entry.kind
        assert restored.description == entry.description
        assert restored.op_id == entry.op_id


class TestTempStorage:
    """Test temporary file storage for sessions."""

    def test_save_session_to_temp(self):
        """Session can be saved to temp file."""
        session = SessionContext()
        session.log_navigation("page1")

        temp_path = save_session_to_temp(session)

        assert temp_path.exists()
        assert temp_path.suffix == ".json"
        assert session.session_id in temp_path.name

    def test_load_session_from_temp(self):
        """Session can be loaded from temp file."""
        original = SessionContext()
        original.log_navigation("page1", title="Page One")
        original.log_query("test query")

        save_session_to_temp(original)
        loaded = load_session_from_temp(original.session_id)

        assert loaded is not None
        assert loaded.session_id == original.session_id
        assert loaded.pages_viewed == 1
        assert loaded.queries_run == 1

    def test_load_nonexistent_session(self):
        """Loading nonexistent session returns None."""
        loaded = load_session_from_temp("nonexistent_id")
        assert loaded is None

    def test_list_temp_sessions(self):
        """Can list sessions in temp storage."""
        # Clean up first
        cleanup_temp_sessions()

        # Create some sessions
        s1 = SessionContext()
        s2 = SessionContext()
        save_session_to_temp(s1)
        save_session_to_temp(s2)

        sessions = list_temp_sessions()
        assert s1.session_id in sessions
        assert s2.session_id in sessions

    def test_cleanup_temp_sessions(self):
        """Can clean up temp session files."""
        # Create a session
        session = SessionContext()
        save_session_to_temp(session)

        # Cleanup
        count = cleanup_temp_sessions()
        assert count >= 1

        # Should be empty now
        sessions = list_temp_sessions()
        assert session.session_id not in sessions


class TestModuleLevelSession:
    """Test module-level session management."""

    def setup_method(self):
        """Clear any existing session before each test."""
        set_current_session(None)

    def teardown_method(self):
        """Clean up after each test."""
        set_current_session(None)

    def test_no_session_initially(self):
        """No session exists initially."""
        session = get_current_session()
        assert session is None

    def test_create_and_set_session(self):
        """Can create and set a session."""
        session = create_session()
        set_current_session(session)

        current = get_current_session()
        assert current is not None
        assert current.session_id == session.session_id

    def test_clear_session(self):
        """Can clear the current session."""
        session = create_session()
        set_current_session(session)
        set_current_session(None)

        current = get_current_session()
        assert current is None


class TestWikiSessionCommands:
    """Test wiki_session_* commands."""

    def setup_method(self):
        """Clear any existing session before each test."""
        set_current_session(None)

    def teardown_method(self):
        """Clean up after each test."""
        set_current_session(None)

    def test_wiki_session_start(self, tmp_path):
        """wiki_session_start creates a new session."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_session_start(wiki)

        assert result["success"] is True
        assert "session_id" in result
        assert result["wiki_root"] == str(tmp_path)

        # Session should be active
        session = get_current_session()
        assert session is not None
        assert session.is_active is True

    def test_wiki_session_start_without_wiki(self):
        """wiki_session_start works without a wiki."""
        result = wiki_session_start()

        assert result["success"] is True
        assert result["wiki_root"] is None

    def test_wiki_session_start_already_active(self, tmp_path):
        """wiki_session_start fails if session already active."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)
        result = wiki_session_start(wiki)  # Try to start another

        assert result["success"] is False
        assert "already active" in result["error"].lower()

    def test_wiki_session_end(self, tmp_path):
        """wiki_session_end ends the active session."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)
        session_id = get_current_session().session_id

        result = wiki_session_end()

        assert result["success"] is True
        assert result["session_id"] == session_id
        assert "duration_seconds" in result

        # Session should be cleared
        assert get_current_session() is None

    def test_wiki_session_end_no_session(self):
        """wiki_session_end fails if no session active."""
        result = wiki_session_end()

        assert result["success"] is False
        assert "no active session" in result["error"].lower()

    def test_wiki_session_end_save_to_temp(self, tmp_path):
        """wiki_session_end can save to temp file."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)
        session_id = get_current_session().session_id

        result = wiki_session_end(save_to_temp=True)

        assert result["success"] is True
        assert "saved_to" in result
        assert Path(result["saved_to"]).exists()

        # Can reload the session
        loaded = load_session_from_temp(session_id)
        assert loaded is not None
        assert loaded.status == SessionStatus.ENDED

    def test_wiki_session_status_no_session(self):
        """wiki_session_status reports no session."""
        result = wiki_session_status()

        assert result["success"] is True
        assert result["has_session"] is False

    def test_wiki_session_status_active_session(self, tmp_path):
        """wiki_session_status reports active session."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)

        result = wiki_session_status()

        assert result["success"] is True
        assert result["has_session"] is True
        assert result["status"] == "active"
        assert "statistics" in result

    def test_wiki_session_log_navigation(self, tmp_path):
        """wiki_session_log_navigation logs page views."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)

        result = wiki_session_log_navigation(
            "concepts/ml",
            title="Machine Learning",
            source="search",
        )

        assert result["success"] is True
        assert result["page_id"] == "concepts/ml"
        assert result["session_pages_viewed"] == 1

        # Verify in session
        session = get_current_session()
        assert session.pages_viewed == 1
        assert session.navigation_history[0].title == "Machine Learning"

    def test_wiki_session_log_navigation_no_session(self):
        """wiki_session_log_navigation fails without session."""
        result = wiki_session_log_navigation("page1")

        assert result["success"] is False
        assert "no active session" in result["error"].lower()

    def test_wiki_session_log_query(self, tmp_path):
        """wiki_session_log_query logs search queries."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)

        result = wiki_session_log_query(
            "machine learning",
            result_count=5,
            top_results=["concepts/ml"],
        )

        assert result["success"] is True
        assert result["query"] == "machine learning"
        assert result["result_count"] == 5
        assert result["session_queries_run"] == 1

    def test_wiki_session_log_query_no_session(self):
        """wiki_session_log_query fails without session."""
        result = wiki_session_log_query("test")

        assert result["success"] is False
        assert "no active session" in result["error"].lower()

    def test_wiki_session_set_context(self, tmp_path):
        """wiki_session_set_context updates session context."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_session_start(wiki)

        result = wiki_session_set_context(
            context="Working on ML chapter",
            focus_pages=["concepts/ml", "concepts/nn"],
        )

        assert result["success"] is True
        assert result["working_context"] == "Working on ML chapter"
        assert result["focus_pages"] == ["concepts/ml", "concepts/nn"]

    def test_wiki_session_set_context_no_session(self):
        """wiki_session_set_context fails without session."""
        result = wiki_session_set_context(context="test")

        assert result["success"] is False
        assert "no active session" in result["error"].lower()


class TestTier3Ephemerality:
    """Test that session data is truly ephemeral (Tier 3).

    Key invariant: Wiki is 100% functional without session data.
    """

    def setup_method(self):
        """Clear any existing session before each test."""
        set_current_session(None)

    def teardown_method(self):
        """Clean up after each test."""
        set_current_session(None)

    def test_wiki_works_without_session(self, tmp_path):
        """Wiki operations work without any session."""
        # Initialize wiki
        result = wiki_init(tmp_path, name="Test Wiki")
        assert result["success"] is True

        # Create source
        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test Article\n\nContent here.")

        # Ingest without session
        wiki = Wiki(tmp_path)
        result = wiki_ingest(wiki, Path("raw/test.md"), title="Test Article")
        assert result["success"] is True

        # Query without session
        result = wiki_query(wiki, "test")
        assert result["success"] is True

    def test_session_loss_doesnt_affect_wiki(self, tmp_path):
        """Losing session data doesn't affect wiki functionality."""
        # Initialize wiki with session
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)
        wiki_session_start(wiki)

        # Do some work
        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test Article\n\nContent here.")
        wiki_ingest(wiki, Path("raw/test.md"), title="Test Article")

        # Log navigation and queries
        wiki_session_log_navigation("sources/test")
        wiki_session_log_query("test", result_count=1)

        # "Lose" the session (simulate crash)
        set_current_session(None)

        # Wiki should still work
        fresh_wiki = Wiki(tmp_path)

        # Can still query
        result = wiki_query(fresh_wiki, "test")
        assert result["success"] is True

        # Can still get stats
        from llm_wiki import wiki_stats
        stats = wiki_stats(fresh_wiki)
        assert stats["total_pages"] >= 1

    def test_session_data_not_in_wiki_directory(self, tmp_path):
        """Session data is not stored in wiki/ directory."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)
        wiki_session_start(wiki)

        # Log some data
        wiki_session_log_navigation("page1")
        wiki_session_log_query("test")

        # End and save to temp
        wiki_session_end(save_to_temp=True)

        # Check wiki directory
        wiki_dir = tmp_path / "wiki"
        session_files = list(wiki_dir.rglob("*session*"))
        assert len(session_files) == 0, "Session files found in wiki directory"

    def test_session_summary(self):
        """Session produces readable summary."""
        session = SessionContext()
        session.log_navigation("page1")
        session.log_navigation("page2")
        session.log_query("test query")
        session.set_context("Working on tests")

        summary = session.summary()

        assert session.session_id in summary
        assert "active" in summary.lower()
        assert "Pages viewed: 2" in summary
        assert "Queries run: 1" in summary


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
