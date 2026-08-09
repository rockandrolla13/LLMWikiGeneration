"""Coverage baselines: has a check quietly stopped checking anything?

Three verification checks in this wiki have failed the same way, and the shape
is worth naming because it is the opposite of the failure people expect. A
check normally fails by finding a problem. These failed by finding nothing:

- Numeric provenance classified pages whose source it could not read as
  "unverifiable". A broken symlink dropped 153 pages out of the checked set and
  the report still said all-clear, because unverifiable is not failing.
- Revision hashes skipped every page without a `revision_hash` field. No page
  had one. It compared nothing, 1,595 times, and reported "All revision hashes
  match content".

Absent data read as PASS in both. A check that says how many pages it covered
cannot do that: the number is the evidence, and a fall in it is a symptom.

The baseline lives in manifest.jsonl as a `verify` entry -- the ledger this
wiki already keeps for every operation, and an operation type that had been
declared but never written. No new file and no new format, and the history of
coverage sits beside the ingests that moved it.

When the baseline moves is the design decision that matters:

- Up, on its own. Growth is the normal case and must never need a manual reset.
- Down, only when the ledger shows an operation that could account for the loss.
  A real ingest or deletion must not cry wolf.
- Never on failure. The old baseline stays, so a second run fails again. A guard
  that a re-run silences is not a guard.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

# Key under which a verify entry carries its coverage payload.
COVERAGE_KEY = "coverage"

# Operations that can legitimately change how much a check covers.
# `rebuild` is excluded on purpose: it writes derived artifacts and cannot add
# or remove a wiki page, so it must never excuse a drop.
_PAGE_MUTATING = frozenset({"ingest", "batch_ingest", "update", "delete"})


@dataclass
class Baseline:
    """The last recorded coverage for one check, and where it was recorded."""

    check: str
    covered: int
    detail: dict = field(default_factory=dict)
    op_id: str = ""
    recorded_at: str = ""
    position: int = -1


def read_baseline(wiki, check: str) -> Optional[Baseline]:
    """Find the most recent coverage recorded for `check`.

    Args:
        wiki: Wiki instance
        check: Name of the check, e.g. "numeric_provenance"

    Returns:
        The last recorded baseline, or None if this check has never recorded one
    """
    entries = wiki.manifest.read_all()
    for position in range(len(entries) - 1, -1, -1):
        payload = entries[position].outputs.extra.get(COVERAGE_KEY)
        if not isinstance(payload, dict) or payload.get("check") != check:
            continue
        return Baseline(
            check=check,
            covered=payload.get("covered", 0),
            detail=payload.get("detail") or {},
            op_id=entries[position].op_id,
            recorded_at=entries[position].timestamp.isoformat(),
            position=position,
        )
    return None


def record_baseline(wiki, check: str, covered: int, detail: Optional[dict] = None) -> None:
    """Append this check's current coverage to the manifest as the new baseline.

    Args:
        wiki: Wiki instance
        check: Name of the check
        covered: How many pages the check could actually examine
        detail: Any secondary counts worth keeping beside it
    """
    from .manifest import Actor, ManifestEntry, OperationStatus, OperationType

    entry = ManifestEntry.create(OperationType.VERIFY, actor=Actor.SYSTEM)
    entry.status = OperationStatus.COMPLETED
    entry.outputs.extra = {
        COVERAGE_KEY: {
            "check": check,
            "covered": covered,
            "detail": detail or {},
        }
    }
    wiki.manifest.append(entry)


def check_regression(
    wiki,
    check: str,
    covered: int,
    detail: Optional[dict] = None,
    subject: str = "coverage",
    unit: str = "pages",
    detail_unit: Optional[tuple[str, str]] = None,
    record: bool = True,
) -> Optional[str]:
    """Fail when a check covers less than last time for no recorded reason.

    Args:
        wiki: Wiki instance
        check: Name of the check, used to keep baselines apart
        covered: How many pages this run could examine
        detail: Secondary counts to record alongside
        subject: How the message should name what fell
        unit: What `covered` counts, for the message
        detail_unit: (detail key, label) to name a second count in the message
        record: Whether the baseline may be written (False keeps this read-only)

    Returns:
        A failure message, or None when coverage is acceptable
    """
    detail = detail or {}
    baseline = read_baseline(wiki, check)

    if baseline is None:
        if record:
            record_baseline(wiki, check, covered, detail)
        return None

    dropped = baseline.covered - covered
    if dropped > 0 and not _mutated_since(wiki, baseline.position):
        lost = f"{dropped} {unit if dropped != 1 else unit.rstrip('s')}"
        if detail_unit:
            key, label = detail_unit
            lost += f" and {baseline.detail.get(key, 0) - detail.get(key, 0)} {label}"
        return (
            f"{subject} fell from {baseline.covered} to {covered} {unit} "
            f"({lost} dropped out) with no ingest, edit or deletion recorded "
            f"since {baseline.recorded_at}; nothing in the ledger accounts for it"
        )

    if record and (covered != baseline.covered or detail != baseline.detail):
        record_baseline(wiki, check, covered, detail)
    return None


def _mutated_since(wiki, position: int) -> bool:
    """Whether the ledger records a page-changing operation after `position`."""
    entries = wiki.manifest.read_all()
    return any(e.op_type.value in _PAGE_MUTATING for e in entries[position + 1:])
