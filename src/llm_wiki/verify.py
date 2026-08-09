"""Verification for LLM Wiki Tier 1 invariants.

Ensures canonical data (wiki/*.md + manifest.jsonl) is consistent
and satisfies all required invariants.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .wiki import Wiki
from .frontmatter import parse_page, compute_content_hash, extract_wikilinks
from .io.wikilinks import normalize_link_target
from .schemas import PageType


@dataclass
class VerificationResult:
    """Result of a single verification check."""
    name: str
    passed: bool
    message: str
    details: list[str] = field(default_factory=list)


@dataclass
class VerificationReport:
    """Complete verification report."""
    wiki_name: str
    total_checks: int
    passed: int
    failed: int
    results: list[VerificationResult] = field(default_factory=list)

    @property
    def all_passed(self) -> bool:
        return self.failed == 0

    def to_markdown(self) -> str:
        """Generate markdown report."""
        status = "✓ PASSED" if self.all_passed else "✗ FAILED"
        lines = [
            f"# Verification Report: {self.wiki_name}",
            "",
            f"**Status:** {status}",
            f"**Checks:** {self.passed}/{self.total_checks} passed",
            "",
            "## Results",
            "",
        ]

        for result in self.results:
            icon = "✓" if result.passed else "✗"
            lines.append(f"### {icon} {result.name}")
            lines.append("")
            lines.append(result.message)
            if result.details:
                lines.append("")
                for detail in result.details:
                    lines.append(f"- {detail}")
            lines.append("")

        return "\n".join(lines)


def verify_wiki(wiki: Wiki, record_baseline: bool = True) -> VerificationReport:
    """Run all verification checks on a wiki.

    Args:
        wiki: Wiki instance to verify
        record_baseline: Whether coverage baselines may be written to the
            manifest. False makes verification read-only, at the cost of
            leaving the coverage-regression guards unarmed.

    Returns:
        VerificationReport with all check results
    """
    results = []

    # Run all checks
    results.append(verify_config_exists(wiki))
    results.append(verify_manifest_exists(wiki))
    results.append(verify_directory_structure(wiki))
    results.append(verify_page_frontmatter(wiki))
    results.append(verify_revision_hashes(wiki, record_baseline=record_baseline))
    results.append(verify_page_ids(wiki))
    results.append(verify_wikilinks(wiki))
    results.append(verify_manifest_operations(wiki))
    results.append(verify_numeric_provenance(wiki, record_baseline=record_baseline))

    passed = sum(1 for r in results if r.passed)
    failed = len(results) - passed

    return VerificationReport(
        wiki_name=wiki.config.name if wiki.exists() else "Unknown",
        total_checks=len(results),
        passed=passed,
        failed=failed,
        results=results,
    )


def verify_config_exists(wiki: Wiki) -> VerificationResult:
    """Verify schema.yml exists and is valid."""
    if not wiki.config_path.exists():
        return VerificationResult(
            name="Config Exists",
            passed=False,
            message="schema.yml not found",
        )

    try:
        config = wiki.config
        return VerificationResult(
            name="Config Exists",
            passed=True,
            message=f"schema.yml valid (wiki: {config.name})",
        )
    except Exception as e:
        return VerificationResult(
            name="Config Exists",
            passed=False,
            message=f"schema.yml invalid: {e}",
        )


def verify_manifest_exists(wiki: Wiki) -> VerificationResult:
    """Verify manifest.jsonl exists and is valid."""
    if not wiki.manifest_path.exists():
        return VerificationResult(
            name="Manifest Exists",
            passed=False,
            message="manifest.jsonl not found",
        )

    try:
        entries = wiki.manifest.read_all()
        return VerificationResult(
            name="Manifest Exists",
            passed=True,
            message=f"manifest.jsonl valid ({len(entries)} operations)",
        )
    except Exception as e:
        return VerificationResult(
            name="Manifest Exists",
            passed=False,
            message=f"manifest.jsonl invalid: {e}",
        )


def verify_directory_structure(wiki: Wiki) -> VerificationResult:
    """Verify required directories exist."""
    required_dirs = [
        wiki.raw_dir,
        wiki.wiki_dir,
        wiki.wiki_dir / "sources",
        wiki.wiki_dir / "entities",
        wiki.wiki_dir / "concepts",
        wiki.wiki_dir / "analyses",
        wiki.wiki_dir / "contradictions",
    ]

    missing = [str(d) for d in required_dirs if not d.exists()]

    if missing:
        return VerificationResult(
            name="Directory Structure",
            passed=False,
            message=f"{len(missing)} required directories missing",
            details=missing,
        )

    return VerificationResult(
        name="Directory Structure",
        passed=True,
        message="All required directories exist",
    )


def verify_page_frontmatter(wiki: Wiki) -> VerificationResult:
    """Verify all pages have required frontmatter fields."""
    required_fields = ["title", "page_id", "page_type", "revision_id"]
    issues = []

    for page_path in wiki.list_pages():
        try:
            metadata, _ = parse_page(page_path)
            missing = [f for f in required_fields if f not in metadata]
            if missing:
                issues.append(f"{page_path.name}: missing {', '.join(missing)}")
        except Exception as e:
            issues.append(f"{page_path.name}: parse error - {e}")

    if issues:
        return VerificationResult(
            name="Page Frontmatter",
            passed=False,
            message=f"{len(issues)} pages have frontmatter issues",
            details=issues[:10],  # Limit to first 10
        )

    page_count = wiki.count_pages()
    return VerificationResult(
        name="Page Frontmatter",
        passed=True,
        message=f"All {page_count} pages have valid frontmatter",
    )


def verify_revision_hashes(
    wiki: Wiki, record_baseline: bool = True
) -> VerificationResult:
    """Verify revision_hash matches content hash for the pages that store one.

    Pages without a `revision_hash` field cannot be compared. That is a gap to
    backfill rather than a mismatch to fail on, so it does not fail the check --
    but it is stated in the message, because the alternative is what this check
    used to do. Every page in this wiki lacks the field, every page was skipped,
    and it reported "All revision hashes match content" while comparing nothing.
    Editing a page body by hand did not disturb it.

    What does fail is a real mismatch, or a fall in how many pages carry a hash
    with nothing in the manifest to explain it. Coverage that only ever grows is
    the property worth guarding: hashes should not evaporate.

    Args:
        wiki: Wiki instance to verify
        record_baseline: Whether coverage may be written to the manifest.
            False makes this read-only, at the cost of not arming the guard.
    """
    from .coverage import check_regression

    issues = []
    total = 0
    hashed = 0

    for page_path in wiki.list_pages():
        total += 1
        try:
            metadata, content = parse_page(page_path)
            if "revision_hash" not in metadata:
                continue

            hashed += 1
            stored_hash = metadata["revision_hash"]
            computed_hash = compute_content_hash(content)

            if stored_hash != computed_hash:
                issues.append(
                    f"{page_path.name}: hash mismatch "
                    f"(stored={stored_hash[:20]}..., computed={computed_hash[:20]}...)"
                )
        except Exception as e:
            issues.append(f"{page_path.name}: error - {e}")

    regression = check_regression(
        wiki,
        "revision_hashes",
        covered=hashed,
        subject="revision-hash coverage",
        record=record_baseline,
    )

    if issues or regression:
        problems = []
        if issues:
            problems.append(
                f"{len(issues)} {'page' if len(issues) == 1 else 'pages'} "
                f"{'has' if len(issues) == 1 else 'have'} hash mismatches"
            )
        if regression:
            problems.append(regression)
        return VerificationResult(
            name="Revision Hashes",
            passed=False,
            message="; ".join(problems),
            details=issues[:10],
        )

    if hashed == 0:
        return VerificationResult(
            name="Revision Hashes",
            passed=True,
            message=(
                f"0 of {total} pages carry a revision_hash, so this check "
                f"verifies nothing until they do"
            ),
        )

    return VerificationResult(
        name="Revision Hashes",
        passed=True,
        message=(
            f"{hashed} of {total} pages carry a revision_hash and all match "
            f"their content"
        ),
    )


def verify_page_ids(wiki: Wiki) -> VerificationResult:
    """Verify page_id in frontmatter matches file path."""
    issues = []

    for page_path in wiki.list_pages():
        try:
            metadata, _ = parse_page(page_path)
            if "page_id" not in metadata:
                continue

            stored_id = metadata["page_id"]
            # Compute expected page_id from path
            rel_path = page_path.relative_to(wiki.wiki_dir)
            expected_id = str(rel_path.with_suffix(""))

            if stored_id != expected_id:
                issues.append(
                    f"{page_path.name}: page_id mismatch "
                    f"(stored={stored_id}, expected={expected_id})"
                )
        except Exception as e:
            issues.append(f"{page_path.name}: error - {e}")

    if issues:
        return VerificationResult(
            name="Page IDs",
            passed=False,
            message=f"{len(issues)} pages have page_id mismatches",
            details=issues[:10],
        )

    return VerificationResult(
        name="Page IDs",
        passed=True,
        message="All page_ids match file paths",
    )


def verify_wikilinks(wiki: Wiki) -> VerificationResult:
    """Verify wikilinks point to existing pages or are flagged."""
    broken_links = []

    # A page is legitimately reachable by page_id, by title, or by bare
    # filename stem, and this corpus uses all three. Resolving against titles
    # alone reported ~9000 live links as broken.
    targets = set()
    for page_path in wiki.list_pages():
        targets.add(page_path.stem)
        targets.add(str(page_path.relative_to(wiki.wiki_dir).with_suffix("")))
        try:
            metadata, _ = parse_page(page_path)
        except Exception:
            continue
        if metadata.get("title"):
            targets.add(metadata["title"])
        if metadata.get("page_id"):
            targets.add(metadata["page_id"])

    # Check all wikilinks
    for page_path in wiki.list_pages():
        try:
            _, content = parse_page(page_path)
        except Exception:
            continue
        for link in extract_wikilinks(content):
            target = normalize_link_target(link)
            if not target:
                continue  # anchor-only link refers to this page
            if target not in targets:
                broken_links.append(f"{page_path.name}: [[{link}]]")

    if broken_links:
        return VerificationResult(
            name="Wikilinks",
            passed=False,
            message=f"{len(broken_links)} broken wikilinks found",
            details=broken_links[:10],
        )

    return VerificationResult(
        name="Wikilinks",
        passed=True,
        message="All wikilinks resolve to existing pages",
    )


def verify_manifest_operations(wiki: Wiki) -> VerificationResult:
    """Verify manifest operations are consistent."""
    issues = []

    try:
        entries = wiki.manifest.read_all()

        # Check for required init operation
        has_init = any(e.op_type.value == "init" for e in entries)
        if not has_init:
            issues.append("No init operation in manifest")

        # Check operation IDs are unique
        op_ids = [e.op_id for e in entries]
        if len(op_ids) != len(set(op_ids)):
            issues.append("Duplicate operation IDs found")

        # Check timestamps are monotonically increasing
        for i in range(1, len(entries)):
            if entries[i].timestamp < entries[i-1].timestamp:
                issues.append(
                    f"Timestamp regression: {entries[i].op_id} < {entries[i-1].op_id}"
                )

    except Exception as e:
        issues.append(f"Manifest read error: {e}")

    if issues:
        return VerificationResult(
            name="Manifest Operations",
            passed=False,
            message=f"{len(issues)} manifest issues found",
            details=issues,
        )

    return VerificationResult(
        name="Manifest Operations",
        passed=True,
        message=f"Manifest consistent ({len(entries)} operations)",
    )


def verify_numeric_provenance(
    wiki: Wiki, record_baseline: bool = True
) -> VerificationResult:
    """Verify that figures on source pages appear in the documents they cite.

    A summary page is easy to write and hard to check, and the failure that
    matters is an invented statistic that reads as precise. This compares every
    decimal figure on each source page against the text of the document that
    page records as its origin.

    Pages that could not be checked are reported by reason rather than as one
    lump, because the reasons mean different things. A page recording no source
    never had an origin written down; a page whose recorded source is not on
    disk makes a claim about its origin that cannot be located. The second is
    worth investigating and is not, on this corpus, evidence that the document
    once existed.

    The check also fails when fewer pages are checkable than the last recorded
    baseline and nothing in the manifest accounts for the loss. Without that,
    losing access to the source documents makes this check quieter instead of
    louder -- which is exactly how a broken symlink dropped 153 pages out of the
    checked set while the report still read "all pass".

    Args:
        wiki: Wiki instance to verify
        record_baseline: Whether coverage may be written back to the manifest.
            False makes this read-only, at the cost of not arming the guard.
    """
    from .coverage import check_regression
    from .provenance import Unverifiable, check_wiki_provenance, summarize_coverage

    results = check_wiki_provenance(wiki)
    verifiable = [r for r in results if r.verifiable]
    failing = [r for r in verifiable if r.unsupported]
    coverage = summarize_coverage(results)
    regression = check_regression(
        wiki,
        "numeric_provenance",
        covered=coverage.verified_pages,
        detail={"verified_figures": coverage.verified_figures},
        subject="verified provenance coverage",
        detail_unit=("verified_figures", "figures"),
        record=record_baseline,
    )

    unchecked = (
        f"{coverage.source_missing} record a source not found on disk, "
        f"{coverage.no_source} record no source at all, "
        f"{coverage.not_text} cite a PDF"
    )
    traced = (
        f"{coverage.verified_figures} figures across {coverage.verified_pages} "
        f"pages trace to their source"
    )

    if failing or regression:
        problems = []
        details = []
        if failing:
            problems.append(
                f"{sum(len(r.unsupported) for r in failing)} figures on "
                f"{len(failing)} pages do not appear in their source document"
            )
            details.extend(
                f"{r.page_id}: {', '.join(r.unsupported)} not found in "
                f"{Path(r.source_path).name}"
                for r in failing[:10]
            )
        if regression:
            problems.append(regression)
            details.extend(
                f"{r.page_id}: {r.note}"
                for r in results
                if r.reason is Unverifiable.SOURCE_MISSING
            )
        return VerificationResult(
            name="Numeric Provenance",
            passed=False,
            message="; ".join(problems),
            details=details[:20],
        )

    return VerificationResult(
        name="Numeric Provenance",
        passed=True,
        message=f"{traced} ({len(results) - len(verifiable)} unverifiable: {unchecked})",
    )
