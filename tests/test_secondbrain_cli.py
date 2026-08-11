"""End-to-end tests for the ``sb`` command line interface."""

import pytest

from llm_wiki.secondbrain.cli import EXIT_CONFIG, EXIT_ERROR, EXIT_OK, main


@pytest.fixture
def root(tmp_path):
    """An initialised Second Brain root."""
    assert main(["--root", str(tmp_path), "init"]) == EXIT_OK
    return str(tmp_path)


def run(root, *args):
    """Invoke the CLI against *root* and return its exit code."""
    return main(["--root", root, *args])


def test_commands_require_init(tmp_path, capsys):
    """Running before init explains itself rather than crashing."""
    assert main(["--root", str(tmp_path), "status"]) == EXIT_CONFIG
    assert "sb init" in capsys.readouterr().err


def test_init_creates_database_and_vault(tmp_path):
    main(["--root", str(tmp_path), "init"])
    assert (tmp_path / ".data" / "secondbrain.db").exists()
    assert (tmp_path / "vault").is_dir()


def test_capture_does_not_claim_a_type(root, capsys):
    """Capture cannot know the type -- classification has not run yet."""
    assert run(root, "capture", "Task: review the PR") == EXIT_OK
    out = capsys.readouterr().out
    assert "Captured" in out
    assert "Not classified yet" in out


def test_full_lifecycle(root, capsys):
    """Capture, classify, list, complete -- the path a real note takes."""
    run(root, "capture", "Task: review the PR from Sarah")
    run(root, "process")
    capsys.readouterr()

    run(root, "list", "task")
    listing = capsys.readouterr().out
    assert "review the PR from Sarah" in listing
    node_id = listing.splitlines()[1].split()[0]

    assert run(root, "done", node_id) == EXIT_OK
    assert "completed" in capsys.readouterr().out


def test_inbox_shows_pending_then_empties(root, capsys):
    run(root, "capture", "Task: something")
    run(root, "inbox")
    assert "something" in capsys.readouterr().out

    run(root, "process")
    capsys.readouterr()
    run(root, "inbox", "--status", "pending")
    assert "empty" in capsys.readouterr().out.lower()


def test_low_confidence_is_marked_in_process_output(root, capsys):
    run(root, "capture", "hmm")
    run(root, "process")
    assert "needs review" in capsys.readouterr().out


def test_dry_run_reports_without_writing(root, capsys):
    run(root, "capture", "Task: something")
    run(root, "process", "--dry-run")
    assert "nothing was written" in capsys.readouterr().out.lower()

    run(root, "inbox", "--status", "pending")
    assert "something" in capsys.readouterr().out


def test_query_states_its_own_limitation(root, capsys):
    """The user must not mistake a substring match for semantic search."""
    run(root, "capture", "Reference: the rate limit is 1000 per minute")
    run(root, "process")
    capsys.readouterr()

    run(root, "query", "rate limit")
    out = capsys.readouterr().out
    assert "rate limit" in out
    assert "not semantic" in out


def test_priority_is_validated_by_the_parser(root):
    with pytest.raises(SystemExit):
        run(root, "priority", "abc", "9")


def test_unknown_reference_is_an_error(root, capsys):
    assert run(root, "done", "nosuchnode") == EXIT_ERROR
    assert "Error" in capsys.readouterr().err


def test_link_and_show(root, capsys):
    run(root, "capture", "Goal: ship the paper by June")
    run(root, "capture", "Task: write section 3")
    run(root, "process")
    capsys.readouterr()

    run(root, "list")
    rows = capsys.readouterr().out.splitlines()[1:]
    ids = [row.split()[0] for row in rows]

    assert run(root, "link", ids[0], ids[1], "supports") == EXIT_OK
    capsys.readouterr()

    run(root, "show", ids[0])
    assert "supports ->" in capsys.readouterr().out


def test_export_writes_markdown(root, tmp_path, capsys):
    run(root, "capture", "Idea: what if we used a compensator clock")
    run(root, "process")
    capsys.readouterr()

    assert run(root, "export") == EXIT_OK
    assert "Exported 1 nodes" in capsys.readouterr().out
    assert list((tmp_path / "vault").rglob("*.md"))


def test_status_reports_counts(root, capsys):
    run(root, "capture", "Task: something")
    capsys.readouterr()
    run(root, "status")
    out = capsys.readouterr().out
    assert "Total captures: 1" in out
    assert "Pending:      1" in out


def test_digest_says_so_when_there_is_nothing(root, capsys):
    run(root, "digest")
    assert "Clear" in capsys.readouterr().out
