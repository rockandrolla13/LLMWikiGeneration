"""Verification for LLM Wiki Tier 1 invariants.

Ensures canonical data (wiki/*.md + manifest.jsonl) is consistent
and satisfies all required invariants.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .wiki import Wiki
from .io import parse_page, extract_wikilinks
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


def verify_wiki(wiki: Wiki) -> VerificationReport:
    """Run all verification checks on a wiki.

    Args:
        wiki: Wiki instance to verify

    Returns:
        VerificationReport with all check results
    """
    results = []

    # Run all checks
    results.append(verify_config_exists(wiki))
    results.append(verify_manifest_exists(wiki))
    results.append(verify_directory_structure(wiki))
    results.append(verify_page_frontmatter(wiki))
    results.append(verify_page_ids(wiki))
    results.append(verify_wikilinks(wiki))
    results.append(verify_manifest_operations(wiki))

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
    required_fields = ["title", "page_id", "page_type"]
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


def resolve_link_targets(wiki: Wiki) -> set[str]:
    """Build the set of strings a wikilink may legitimately point at.

    A wiki page is reachable by any of three names, all of which appear in
    real vaults:

    - its page_id, e.g. ``concepts/carry-trade`` (the dominant convention here)
    - its title, e.g. ``Carry Trade``
    - its bare filename stem, e.g. ``carry-trade`` (how Obsidian resolves
      short links)

    Resolving against titles alone reports nearly every link as broken in a
    page_id-linked wiki.

    Args:
        wiki: Wiki instance

    Returns:
        Set of every accepted link target
    """
    targets: set[str] = set()

    for page_path in wiki.list_pages():
        targets.add(page_path.stem)
        try:
            metadata, _ = parse_page(page_path)
        except Exception:
            continue
        if metadata.get("title"):
            targets.add(metadata["title"])
        if metadata.get("page_id"):
            targets.add(metadata["page_id"])
        # Fall back to the path-derived page_id when frontmatter omits it
        targets.add(str(page_path.relative_to(wiki.wiki_dir).with_suffix("")))

    return targets


def normalize_link_target(link: str) -> str:
    """Reduce a raw wikilink to the page it actually points at.

    Handles two forms that would otherwise be reported as broken:

    - ``[[Page#Section]]`` -- the anchor is dropped; it points at Page.
    - ``[[Page\\|text]]`` -- inside a markdown table the pipe must be escaped,
      so the captured target keeps a trailing backslash. Obsidian treats the
      backslash as the escape character, not part of the page name.

    Display text (``[[Page|text]]``) is already removed by extract_wikilinks.
    """
    target = link.split("#", 1)[0].strip()
    # Trailing backslash is the escape before a table-escaped pipe
    return target.rstrip("\\").strip()


def verify_wikilinks(wiki: Wiki) -> VerificationResult:
    """Verify wikilinks point to existing pages or are flagged."""
    broken_links = []

    targets = resolve_link_targets(wiki)

    # Check all wikilinks
    for page_path in wiki.list_pages():
        try:
            _, content = parse_page(page_path)
        except Exception:
            continue
        for link in extract_wikilinks(content):
            target = normalize_link_target(link)
            # An anchor-only link ([[#Section]]) points within the same page
            if not target:
                continue
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
