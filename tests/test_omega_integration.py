"""Tests for OMEGA (omega-memory) integration.

Tests cover:
1. is_omega_available() returns bool
2. All functions work when omega is NOT installed (graceful degradation)
3. All functions work correctly when omega IS available (mocked)
"""

import json
import pytest
from unittest.mock import MagicMock, patch


class TestOmegaNotInstalled:
    """Test graceful degradation when omega-memory is not installed."""

    def test_is_omega_available_returns_bool(self):
        """is_omega_available() should always return a boolean."""
        from llm_wiki.integrations.omega import is_omega_available
        result = is_omega_available()
        assert isinstance(result, bool)

    def test_store_wiki_event_without_omega(self):
        """store_wiki_event should return False when omega unavailable."""
        with patch("llm_wiki.integrations.omega._omega_available", False):
            with patch("llm_wiki.integrations.omega._omega", None):
                from llm_wiki.integrations import omega
                result = omega.store_wiki_event(
                    event_type="decision",
                    content="Test decision",
                    wiki_name="test-wiki",
                    tags=["test"],
                )
                assert result is False

    def test_get_wiki_briefing_without_omega(self):
        """get_wiki_briefing should return empty list when omega unavailable."""
        with patch("llm_wiki.integrations.omega._omega_available", False):
            with patch("llm_wiki.integrations.omega._omega", None):
                from llm_wiki.integrations import omega
                result = omega.get_wiki_briefing("test-wiki", limit=5)
                assert result == []
                assert isinstance(result, list)

    def test_store_lesson_without_omega(self):
        """store_lesson should return False when omega unavailable."""
        with patch("llm_wiki.integrations.omega._omega_available", False):
            with patch("llm_wiki.integrations.omega._omega", None):
                from llm_wiki.integrations import omega
                result = omega.store_lesson(
                    lesson="Test lesson",
                    wiki_name="test-wiki",
                )
                assert result is False

    def test_query_wiki_history_without_omega(self):
        """query_wiki_history should return empty list when omega unavailable."""
        with patch("llm_wiki.integrations.omega._omega_available", False):
            with patch("llm_wiki.integrations.omega._omega", None):
                from llm_wiki.integrations import omega
                result = omega.query_wiki_history(
                    query="test query",
                    wiki_name="test-wiki",
                    limit=10,
                )
                assert result == []
                assert isinstance(result, list)

    def test_checkpoint_task_without_omega(self):
        """checkpoint_task should return False when omega unavailable."""
        with patch("llm_wiki.integrations.omega._omega_available", False):
            with patch("llm_wiki.integrations.omega._omega", None):
                from llm_wiki.integrations import omega
                result = omega.checkpoint_task(
                    task_id="task-123",
                    state={"step": 1, "data": "test"},
                    wiki_name="test-wiki",
                )
                assert result is False

    def test_resume_task_without_omega(self):
        """resume_task should return None when omega unavailable."""
        with patch("llm_wiki.integrations.omega._omega_available", False):
            with patch("llm_wiki.integrations.omega._omega", None):
                from llm_wiki.integrations import omega
                result = omega.resume_task(task_id="task-123")
                assert result is None


class TestOmegaAvailableMocked:
    """Test functions when omega-memory is available (mocked)."""

    @pytest.fixture
    def mock_omega(self):
        """Create a mock omega module."""
        mock = MagicMock()
        mock.store = MagicMock(return_value="mem-123")
        mock.query = MagicMock(return_value="")
        return mock

    def test_store_wiki_event_with_mock_omega(self, mock_omega):
        """store_wiki_event should call omega.store with correct API."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.store_wiki_event(
                    event_type="decision",
                    content="Created entity page for John Doe",
                    wiki_name="my-wiki",
                    tags=["entity", "person"],
                )

                assert result is True
                mock_omega.store.assert_called_once()
                call_kwargs = mock_omega.store.call_args[1]
                assert call_kwargs["content"] == "Created entity page for John Doe"
                assert call_kwargs["event_type"] == "decision"
                assert call_kwargs["project"] == "my-wiki"
                assert "metadata" in call_kwargs
                assert call_kwargs["metadata"]["wiki"] == "my-wiki"

    def test_store_wiki_event_normalizes_invalid_type(self, mock_omega):
        """store_wiki_event should normalize invalid event types to 'memory'."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.store_wiki_event(
                    event_type="invalid_type",
                    content="Test content",
                    wiki_name="my-wiki",
                )

                assert result is True
                mock_omega.store.assert_called_once()
                call_kwargs = mock_omega.store.call_args[1]
                assert call_kwargs["event_type"] == "memory"

    def test_store_wiki_event_handles_exception(self, mock_omega):
        """store_wiki_event should handle exceptions gracefully."""
        mock_omega.store.side_effect = RuntimeError("Connection failed")

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.store_wiki_event(
                    event_type="decision",
                    content="Test content",
                    wiki_name="my-wiki",
                )

                assert result is False

    def test_get_wiki_briefing_with_mock_omega(self, mock_omega):
        """get_wiki_briefing should call query with correct API."""
        mock_omega.query.return_value = "Results: 1\nTest memory content"

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.get_wiki_briefing("my-wiki", limit=5)

                assert len(result) >= 1
                mock_omega.query.assert_called_once()
                call_kwargs = mock_omega.query.call_args[1]
                assert call_kwargs["query_text"] == "my-wiki"
                assert call_kwargs["limit"] == 5
                assert call_kwargs["project"] == "my-wiki"

    def test_get_wiki_briefing_handles_exception(self, mock_omega):
        """get_wiki_briefing should return empty list on exception."""
        mock_omega.query.side_effect = RuntimeError("Query failed")

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.get_wiki_briefing("my-wiki")

                assert result == []

    def test_store_lesson_with_mock_omega(self, mock_omega):
        """store_lesson should store with correct type."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.store_lesson(
                    lesson="Always use ISO dates in wiki pages",
                    wiki_name="my-wiki",
                )

                assert result is True
                mock_omega.store.assert_called_once()
                call_kwargs = mock_omega.store.call_args[1]
                assert call_kwargs["event_type"] == "lesson"
                assert call_kwargs["project"] == "my-wiki"

    def test_query_wiki_history_with_wiki_name(self, mock_omega):
        """query_wiki_history should use project parameter."""
        mock_omega.query.return_value = "Results: 1\nUpdated entity page"

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.query_wiki_history(
                    query="entity page",
                    wiki_name="my-wiki",
                    limit=10,
                )

                assert len(result) >= 1
                mock_omega.query.assert_called_once()
                call_kwargs = mock_omega.query.call_args[1]
                assert call_kwargs["query_text"] == "entity page"
                assert call_kwargs["limit"] == 10
                assert call_kwargs["project"] == "my-wiki"

    def test_query_wiki_history_without_wiki_name(self, mock_omega):
        """query_wiki_history should work without wiki name filter."""
        mock_omega.query.return_value = ""

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.query_wiki_history(
                    query="general search",
                    wiki_name=None,
                    limit=5,
                )

                assert result == []
                mock_omega.query.assert_called_once()
                call_kwargs = mock_omega.query.call_args[1]
                assert call_kwargs["project"] is None

    def test_checkpoint_task_fallback_to_store(self, mock_omega):
        """checkpoint_task should use store() as fallback."""
        # Mock that checkpoint method doesn't exist
        del mock_omega.checkpoint

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.checkpoint_task(
                    task_id="task-123",
                    state={"step": 2, "items": ["a", "b"]},
                    wiki_name="my-wiki",
                )

                assert result is True
                mock_omega.store.assert_called_once()
                call_kwargs = mock_omega.store.call_args[1]
                assert "CHECKPOINT:task-123" in call_kwargs["content"]
                assert call_kwargs["event_type"] == "summary"
                assert call_kwargs["project"] == "my-wiki"

    def test_resume_task_fallback_to_query(self, mock_omega):
        """resume_task should use query() as fallback."""
        # Mock that resume method doesn't exist
        del mock_omega.resume

        # Mock query returning a checkpoint
        checkpoint_data = json.dumps({
            "task_id": "task-123",
            "state": {"step": 2, "items": ["a", "b"]},
            "wiki_name": "my-wiki",
        })
        mock_omega.query.return_value = f"[CHECKPOINT:task-123] {checkpoint_data}"

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.resume_task(task_id="task-123")

                assert result is not None
                assert result["step"] == 2
                assert result["items"] == ["a", "b"]

    def test_checkpoint_handles_exception(self, mock_omega):
        """checkpoint_task should return False on exception."""
        mock_omega.store.side_effect = RuntimeError("Store failed")
        del mock_omega.checkpoint

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.checkpoint_task(
                    task_id="task-123",
                    state={"data": "test"},
                    wiki_name="my-wiki",
                )

                assert result is False

    def test_resume_returns_none_on_no_checkpoint(self, mock_omega):
        """resume_task should return None when no checkpoint found."""
        del mock_omega.resume
        mock_omega.query.return_value = ""

        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                result = omega.resume_task(task_id="nonexistent-task")

                assert result is None


class TestModuleImports:
    """Test that module imports work correctly."""

    def test_integrations_package_imports(self):
        """All omega functions should be importable from integrations package."""
        from llm_wiki.integrations import (
            is_omega_available,
            store_wiki_event,
            get_wiki_briefing,
            store_lesson,
            query_wiki_history,
            checkpoint_task,
            resume_task,
        )

        # Just verify they're callable
        assert callable(is_omega_available)
        assert callable(store_wiki_event)
        assert callable(get_wiki_briefing)
        assert callable(store_lesson)
        assert callable(query_wiki_history)
        assert callable(checkpoint_task)
        assert callable(resume_task)

    def test_top_level_imports(self):
        """Omega functions should be importable from llm_wiki package."""
        from llm_wiki import (
            is_omega_available,
            store_wiki_event,
            get_wiki_briefing,
            store_lesson,
            query_wiki_history,
            checkpoint_task,
            resume_task,
        )

        assert callable(is_omega_available)
        assert callable(store_wiki_event)


class TestEventTypeValidation:
    """Test event type normalization."""

    @pytest.fixture
    def mock_omega(self):
        mock = MagicMock()
        mock.store = MagicMock(return_value="mem-123")
        return mock

    @pytest.mark.parametrize("event_type,expected", [
        ("decision", "decision"),
        ("lesson", "lesson"),
        ("error", "error"),
        ("summary", "summary"),
        ("memory", "memory"),
        ("invalid", "memory"),
        ("DECISION", "memory"),  # Case sensitive
        ("", "memory"),
        ("random_type", "memory"),
    ])
    def test_event_type_normalization(self, mock_omega, event_type, expected):
        """Event types should be normalized correctly."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                omega.store_wiki_event(
                    event_type=event_type,
                    content="Test",
                    wiki_name="my-wiki",
                )

                call_kwargs = mock_omega.store.call_args[1]
                assert call_kwargs["event_type"] == expected


class TestMetadataHandling:
    """Test metadata and tags handling."""

    @pytest.fixture
    def mock_omega(self):
        mock = MagicMock()
        mock.store = MagicMock(return_value="mem-123")
        return mock

    def test_wiki_metadata_always_added(self, mock_omega):
        """Wiki name should always be in metadata."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                omega.store_wiki_event(
                    event_type="decision",
                    content="Test",
                    wiki_name="my-wiki",
                )

                call_kwargs = mock_omega.store.call_args[1]
                assert call_kwargs["metadata"]["wiki"] == "my-wiki"
                assert call_kwargs["project"] == "my-wiki"

    def test_user_tags_in_metadata(self, mock_omega):
        """User tags should be stored in metadata."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                omega.store_wiki_event(
                    event_type="decision",
                    content="Test",
                    wiki_name="my-wiki",
                    tags=["custom1", "custom2"],
                )

                call_kwargs = mock_omega.store.call_args[1]
                assert "tags" in call_kwargs["metadata"]
                tags = call_kwargs["metadata"]["tags"]
                assert "wiki:my-wiki" in tags
                assert "custom1" in tags
                assert "custom2" in tags

    def test_empty_tags_list_handled(self, mock_omega):
        """Empty tags list should still include wiki tag."""
        with patch("llm_wiki.integrations.omega._omega_available", True):
            with patch("llm_wiki.integrations.omega._omega", mock_omega):
                from llm_wiki.integrations import omega
                omega.store_wiki_event(
                    event_type="decision",
                    content="Test",
                    wiki_name="my-wiki",
                    tags=[],
                )

                call_kwargs = mock_omega.store.call_args[1]
                tags = call_kwargs["metadata"]["tags"]
                assert "wiki:my-wiki" in tags
