"""Tests for rule-based capture classification."""

from datetime import datetime

import pytest

from llm_wiki.secondbrain import classify, extract_due, make_title
from llm_wiki.secondbrain.models import DEFAULT_CONFIDENCE_THRESHOLD, Domain, NodeType

NOW = datetime(2026, 3, 1, 12, 0, 0)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Task: review the PR", NodeType.TASK),
        ("TODO: renew the domain", NodeType.TASK),
        ("Idea: what about a compensator clock", NodeType.IDEA),
        ("Decision: use Postgres", NodeType.REFERENCE),
        ("Meeting: Q1 planning", NodeType.MEETING),
        ("Goal: ship by June", NodeType.GOAL),
        ("Person: Sarah", NodeType.PERSON),
        ("Value: shipping beats perfection", NodeType.VALUE),
    ],
)
def test_explicit_prefix_wins(text, expected):
    """An explicit prefix is obeyed and reported with high confidence."""
    result = classify(text, now=NOW)
    assert result.node_type is expected
    assert result.confidence >= 0.9
    assert not result.needs_review


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Call the dentist to reschedule", NodeType.TASK),
        ("I need to review the PR from Sarah", NodeType.TASK),
        ("What if we used a Hawkes compensator here", NodeType.IDEA),
        ("I noticed the spread widens before the print", NodeType.IDEA),
        ("The API rate limit is 1000 requests/minute", NodeType.REFERENCE),
        ("Sarah Chen - VP Engineering at Acme", NodeType.PERSON),
        ("Standup at 10am", NodeType.MEETING),
    ],
)
def test_inferred_types(text, expected):
    """Common phrasings are classified without an explicit prefix."""
    assert classify(text, now=NOW).node_type is expected


def test_unrecognised_text_goes_to_review():
    """When nothing matches, confidence stays below the auto-file threshold."""
    result = classify("hmm", now=NOW)
    assert result.node_type is NodeType.REFERENCE
    assert result.confidence < DEFAULT_CONFIDENCE_THRESHOLD
    assert result.needs_review
    assert "nothing matched" in " ".join(result.reasons)


def test_classification_is_deterministic():
    """The same text always yields the same verdict."""
    text = "I need to send the quarterly report by 2026-04-01"
    first, second = classify(text, now=NOW), classify(text, now=NOW)
    assert first == second


class TestPriority:
    """Priority inference from wording."""

    def test_default_is_medium(self):
        assert classify("Call the dentist", now=NOW).priority == 2

    def test_urgent_becomes_critical(self):
        assert classify("Fix this ASAP, system down", now=NOW).priority == 0

    def test_someday_becomes_backlog(self):
        assert classify("Read that paper someday", now=NOW).priority == 4


class TestDomain:
    """Domain inference from wording."""

    def test_work_signal(self):
        assert classify("Review the pull request", now=NOW).domain is Domain.WORK

    def test_personal_signal(self):
        assert classify("Call the dentist", now=NOW).domain is Domain.PERSONAL

    def test_both_signals_present(self):
        result = classify("Ask my manager about the family holiday", now=NOW)
        assert result.domain is Domain.BOTH

    def test_no_signal_defaults_to_both(self):
        assert classify("The limit is 40", now=NOW).domain is Domain.BOTH


class TestDueDates:
    """Date extraction."""

    def test_iso_date(self):
        assert extract_due("due 2026-04-15", now=NOW) == "2026-04-15"

    def test_tomorrow_is_relative_to_now(self):
        assert extract_due("do it tomorrow", now=NOW) == "2026-03-02"

    def test_month_and_day(self):
        assert extract_due("deadline is March 15th", now=NOW) == "2026-03-15"

    def test_day_and_month(self):
        assert extract_due("deadline is 15 March", now=NOW) == "2026-03-15"

    def test_past_month_rolls_to_next_year(self):
        """A month already gone this year means next year, not the past."""
        assert extract_due("due February 10", now=NOW) == "2027-02-10"

    def test_impossible_date_is_ignored(self):
        assert extract_due("February 30th", now=NOW) is None

    def test_no_date(self):
        assert extract_due("no date here", now=NOW) is None


class TestTitles:
    """Title generation."""

    def test_strips_explicit_prefix(self):
        assert make_title("Task: review the PR") == "review the PR"

    def test_takes_first_non_empty_line(self):
        assert make_title("\n\nfirst line\nsecond line") == "first line"

    def test_truncates_on_a_word_boundary(self):
        title = make_title("word " * 60)
        assert title.endswith("...")
        assert len(title) <= 103

    def test_empty_text_yields_empty_title(self):
        assert make_title("   ") == ""
