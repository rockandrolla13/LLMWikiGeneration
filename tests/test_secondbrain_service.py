"""Tests for the Second Brain store, service layer, digest and vault export."""

from datetime import datetime, timedelta

import pytest

from llm_wiki.secondbrain import (
    AmbiguousIdError,
    EdgeType,
    Node,
    NodeNotFoundError,
    NodeStatus,
    NodeType,
    SecondBrainConfig,
    Store,
    archive,
    build_digest,
    capture,
    complete,
    export_all,
    link,
    process,
    render_digest,
    render_node,
    reopen,
    set_priority,
    set_type,
)
from llm_wiki.secondbrain.models import CaptureStatus, Domain
from llm_wiki.secondbrain.vault import node_filename, slugify

NOW = datetime(2026, 3, 1, 12, 0, 0)
THRESHOLD = 0.6


@pytest.fixture
def store(tmp_path):
    """An empty Second Brain database in a temporary directory."""
    with Store(tmp_path / "sb.db") as s:
        yield s


class TestCapture:
    """Capturing raw text."""

    def test_capture_is_pending_and_unclassified(self, store):
        item = capture(store, "Task: review the PR")
        assert item.status is CaptureStatus.PENDING
        assert item.node_id is None
        assert item.confidence is None

    def test_capture_creates_no_node(self, store):
        capture(store, "Task: review the PR")
        assert store.counts()["nodes"] == 0

    def test_content_is_stored_verbatim(self, store):
        item = capture(store, "  spacing   preserved inside  ")
        assert store.get_capture(item.id).content == "spacing   preserved inside"

    def test_empty_capture_is_rejected(self, store):
        with pytest.raises(ValueError):
            capture(store, "   ")


class TestProcess:
    """Classification of pending captures."""

    def test_confident_capture_is_classified(self, store):
        capture(store, "Task: review the PR")
        (item, node, verdict) = process(store, THRESHOLD, now=NOW)[0]
        assert item.status is CaptureStatus.CLASSIFIED
        assert node.node_type is NodeType.TASK
        assert node.capture_id == item.id

    def test_unclear_capture_needs_review_but_still_becomes_a_node(self, store):
        """Losing the thought would be worse than filing it imperfectly."""
        capture(store, "hmm")
        (item, node, verdict) = process(store, THRESHOLD, now=NOW)[0]
        assert item.status is CaptureStatus.NEEDS_REVIEW
        assert node is not None
        assert verdict.confidence < THRESHOLD

    def test_dry_run_writes_nothing(self, store):
        capture(store, "Task: review the PR")
        results = process(store, THRESHOLD, dry_run=True, now=NOW)
        assert results[0][1] is None
        assert store.counts()["nodes"] == 0
        assert store.list_captures(status=CaptureStatus.PENDING)

    def test_processing_is_not_repeated(self, store):
        capture(store, "Task: review the PR")
        process(store, THRESHOLD, now=NOW)
        assert process(store, THRESHOLD, now=NOW) == []

    def test_unknown_capture_id_raises(self, store):
        with pytest.raises(NodeNotFoundError):
            process(store, THRESHOLD, capture_id="nosuchid", now=NOW)


class TestMutations:
    """The operations that change an existing node."""

    @pytest.fixture
    def node(self, store):
        capture(store, "Task: review the PR")
        return process(store, THRESHOLD, now=NOW)[0][1]

    def test_complete_sets_status_and_timestamp(self, store, node):
        done = complete(store, node.id, now=NOW)
        assert done.status is NodeStatus.COMPLETED
        assert done.completed_at == NOW

    def test_reopen_clears_completion(self, store, node):
        complete(store, node.id, now=NOW)
        again = reopen(store, node.id)
        assert again.status is NodeStatus.ACTIVE
        assert again.completed_at is None

    def test_archive(self, store, node):
        assert archive(store, node.id).status is NodeStatus.ARCHIVED

    def test_priority_is_bounded(self, store, node):
        assert set_priority(store, node.id, 0).priority == 0
        with pytest.raises(ValueError):
            set_priority(store, node.id, 9)

    def test_retype_resolves_the_review_flag(self, store):
        """Correcting the type is what closes a needs_review capture."""
        item = capture(store, "hmm")
        process(store, THRESHOLD, now=NOW)
        node = store.list_nodes()[0]
        assert store.get_capture(item.id).status is CaptureStatus.NEEDS_REVIEW

        set_type(store, node.id, NodeType.IDEA)
        assert store.get_capture(item.id).status is CaptureStatus.CLASSIFIED

    def test_mutations_are_logged(self, store, node):
        before = store.counts()["events"]
        complete(store, node.id, now=NOW)
        assert store.counts()["events"] > before

    def test_lookup_by_short_prefix(self, store, node):
        assert complete(store, node.id[:8], now=NOW).id == node.id

    def test_lookup_by_title(self, store, node):
        assert complete(store, "review the PR", now=NOW).id == node.id

    def test_missing_node_raises(self, store):
        with pytest.raises(NodeNotFoundError):
            complete(store, "nothinghere")


class TestAmbiguity:
    """Short id prefixes must not silently pick a winner."""

    def test_ambiguous_prefix_raises(self, store):
        store.add_node(Node(title="one", id="abcd" + "0" * 28))
        store.add_node(Node(title="two", id="abcd" + "1" * 28))
        with pytest.raises(AmbiguousIdError):
            store.get_node("abcd")

    def test_exact_id_still_resolves_when_a_prefix_is_shared(self, store):
        first = store.add_node(Node(title="one", id="abcd" + "0" * 28))
        store.add_node(Node(title="two", id="abcd" + "1" * 28))
        assert store.get_node(first.id).title == "one"


class TestEdges:
    """Typed relationships."""

    @pytest.fixture
    def pair(self, store):
        goal = store.add_node(Node(title="Ship the paper", node_type=NodeType.GOAL))
        task = store.add_node(Node(title="Write section 3", node_type=NodeType.TASK))
        return goal, task

    def test_link_and_traverse(self, store, pair):
        goal, task = pair
        link(store, task.id, goal.id, EdgeType.SUPPORTS)
        assert [n.id for n in store.neighbours(task.id)] == [goal.id]

    def test_filter_by_relation(self, store, pair):
        goal, task = pair
        link(store, task.id, goal.id, EdgeType.SUPPORTS)
        assert store.neighbours(task.id, rel=EdgeType.BLOCKS) == []

    def test_duplicate_edges_collapse(self, store, pair):
        goal, task = pair
        link(store, task.id, goal.id, EdgeType.SUPPORTS)
        link(store, task.id, goal.id, EdgeType.SUPPORTS)
        assert store.counts()["edges"] == 1

    def test_self_link_is_rejected(self, store, pair):
        goal, _ = pair
        with pytest.raises(ValueError):
            link(store, goal.id, goal.id, EdgeType.RELATED_TO)


class TestListing:
    """Filters on the node listing."""

    @pytest.fixture
    def populated(self, store):
        store.add_node(Node(title="a task", node_type=NodeType.TASK, domain=Domain.WORK))
        store.add_node(Node(title="an idea", node_type=NodeType.IDEA))
        store.add_node(
            Node(title="archived", node_type=NodeType.TASK, status=NodeStatus.ARCHIVED)
        )
        return store

    def test_filter_by_type(self, populated):
        assert len(populated.list_nodes(node_type=NodeType.TASK)) == 2

    def test_filter_by_status(self, populated):
        assert len(populated.list_nodes(status=NodeStatus.ARCHIVED)) == 1

    def test_filter_by_domain(self, populated):
        assert len(populated.list_nodes(domain=Domain.WORK)) == 1

    def test_substring_search(self, populated):
        assert len(populated.search_nodes("IDEA")) == 1


class TestDigest:
    """Digest assembly and its word limit."""

    def test_empty_digest_has_no_sections(self, store):
        assert build_digest(store, now=NOW) == []

    def test_overdue_task_is_flagged(self, store):
        store.add_node(
            Node(title="late thing", node_type=NodeType.TASK, due="2026-02-01")
        )
        text = render_digest(build_digest(store, now=NOW))
        assert "OVERDUE" in text

    def test_due_today_is_flagged(self, store):
        store.add_node(
            Node(title="today thing", node_type=NodeType.TASK, due="2026-03-01")
        )
        assert "DUE TODAY" in render_digest(build_digest(store, now=NOW))

    def test_completed_work_is_excluded(self, store):
        node = store.add_node(
            Node(title="done thing", node_type=NodeType.TASK, due="2026-02-01")
        )
        complete(store, node.id, now=NOW)
        assert build_digest(store, now=NOW) == []

    def test_word_limit_is_respected(self, store):
        for index in range(40):
            store.add_node(
                Node(
                    title=f"task number {index} with a deliberately long title",
                    node_type=NodeType.TASK,
                    due="2026-02-01",
                )
            )
        text = render_digest(build_digest(store, now=NOW), word_limit=50)
        assert len(text.split()) <= 50


class TestVault:
    """Markdown export."""

    def test_slug_is_filesystem_safe(self):
        assert slugify("Review PR #1234 (urgent!)") == "review-pr-1234-urgent"

    def test_slug_never_empty(self):
        assert slugify("###") == "untitled"

    def test_filename_disambiguates_identical_titles(self):
        first = Node(title="same title")
        second = Node(title="same title")
        assert node_filename(first) != node_filename(second)

    def test_rendered_page_has_frontmatter(self, store):
        node = store.add_node(Node(title="a thing", node_type=NodeType.IDEA))
        text = render_node(node)
        assert text.startswith("---\n")
        assert "type: idea" in text
        assert "# a thing" in text

    def test_links_render_as_wikilinks(self, store):
        goal = store.add_node(Node(title="Ship it", node_type=NodeType.GOAL))
        task = store.add_node(Node(title="Do the work", node_type=NodeType.TASK))
        link(store, task.id, goal.id, EdgeType.SUPPORTS)
        assert "[[ship-it-" in render_node(store.get_node(task.id), store=store)

    def test_export_groups_by_type(self, store, tmp_path):
        store.add_node(Node(title="a task", node_type=NodeType.TASK))
        store.add_node(Node(title="an idea", node_type=NodeType.IDEA))
        paths = export_all(store, tmp_path / "vault")
        folders = {p.parent.name for p in paths}
        assert folders == {"tasks", "ideas"}

    def test_export_is_idempotent(self, store, tmp_path):
        store.add_node(Node(title="a task", node_type=NodeType.TASK))
        vault = tmp_path / "vault"
        first = export_all(store, vault)
        second = export_all(store, vault)
        assert first == second
        assert len(list(vault.rglob("*.md"))) == 1


class TestConfig:
    """Path resolution."""

    def test_explicit_root_wins(self, tmp_path):
        config = SecondBrainConfig.resolve(tmp_path)
        assert config.db_path.is_relative_to(tmp_path)
        assert config.vault_path.is_relative_to(tmp_path)

    def test_database_is_hidden_from_obsidian(self, tmp_path):
        """Obsidian ignores dot directories, so the db must live in one."""
        config = SecondBrainConfig.resolve(tmp_path)
        assert ".data" in config.db_path.parts

    def test_environment_overrides(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SECONDBRAIN_ROOT", str(tmp_path / "elsewhere"))
        assert SecondBrainConfig.resolve().root == tmp_path / "elsewhere"

    def test_ensure_dirs_creates_both(self, tmp_path):
        config = SecondBrainConfig.resolve(tmp_path / "fresh")
        config.ensure_dirs()
        assert config.db_path.parent.is_dir()
        assert config.vault_path.is_dir()
