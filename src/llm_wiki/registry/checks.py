"""Default verification check registry.

This module provides the default registry of verification checks.
Each check implements the VerificationCheck protocol from core.protocols.

Usage:
    from llm_wiki.registry import get_default_checks

    checks = get_default_checks()
    for check in checks.all():
        result = check.execute(wiki)
"""

from typing import TYPE_CHECKING

from ..core.protocols import VerificationRegistry

if TYPE_CHECKING:
    from ..wiki import Wiki
    from ..verify import VerificationResult


class ConfigExistsCheck:
    """Verify schema.yml exists and is valid."""

    @property
    def name(self) -> str:
        return "Config Exists"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult

        if not wiki.config_path.exists():
            return VerificationResult(
                name=self.name,
                passed=False,
                message="schema.yml not found",
            )

        try:
            config = wiki.config
            return VerificationResult(
                name=self.name,
                passed=True,
                message=f"schema.yml valid (wiki: {config.name})",
            )
        except Exception as e:
            return VerificationResult(
                name=self.name,
                passed=False,
                message=f"schema.yml invalid: {e}",
            )


class ManifestExistsCheck:
    """Verify manifest.jsonl exists and is valid."""

    @property
    def name(self) -> str:
        return "Manifest Exists"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult

        if not wiki.manifest_path.exists():
            return VerificationResult(
                name=self.name,
                passed=False,
                message="manifest.jsonl not found",
            )

        try:
            entries = wiki.manifest.read_all()
            return VerificationResult(
                name=self.name,
                passed=True,
                message=f"manifest.jsonl valid ({len(entries)} operations)",
            )
        except Exception as e:
            return VerificationResult(
                name=self.name,
                passed=False,
                message=f"manifest.jsonl invalid: {e}",
            )


class DirectoryStructureCheck:
    """Verify required directories exist."""

    @property
    def name(self) -> str:
        return "Directory Structure"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult

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
                name=self.name,
                passed=False,
                message=f"{len(missing)} required directories missing",
                details=missing,
            )

        return VerificationResult(
            name=self.name,
            passed=True,
            message="All required directories exist",
        )


class PageFrontmatterCheck:
    """Verify all pages have required frontmatter fields."""

    @property
    def name(self) -> str:
        return "Page Frontmatter"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult
        from ..frontmatter import parse_page

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
                name=self.name,
                passed=False,
                message=f"{len(issues)} pages have frontmatter issues",
                details=issues[:10],  # Limit to first 10
            )

        page_count = wiki.count_pages()
        return VerificationResult(
            name=self.name,
            passed=True,
            message=f"All {page_count} pages have valid frontmatter",
        )


class RevisionHashesCheck:
    """Verify revision_hash matches content hash for all pages."""

    @property
    def name(self) -> str:
        return "Revision Hashes"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult
        from ..frontmatter import parse_page, compute_content_hash

        issues = []

        for page_path in wiki.list_pages():
            try:
                metadata, content = parse_page(page_path)
                if "revision_hash" not in metadata:
                    continue  # Skip if no hash stored

                stored_hash = metadata["revision_hash"]
                computed_hash = compute_content_hash(content)

                if stored_hash != computed_hash:
                    issues.append(
                        f"{page_path.name}: hash mismatch "
                        f"(stored={stored_hash[:20]}..., computed={computed_hash[:20]}...)"
                    )
            except Exception as e:
                issues.append(f"{page_path.name}: error - {e}")

        if issues:
            return VerificationResult(
                name=self.name,
                passed=False,
                message=f"{len(issues)} pages have hash mismatches",
                details=issues[:10],
            )

        return VerificationResult(
            name=self.name,
            passed=True,
            message="All revision hashes match content",
        )


class PageIdsCheck:
    """Verify page_id in frontmatter matches file path."""

    @property
    def name(self) -> str:
        return "Page IDs"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult
        from ..frontmatter import parse_page

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
                name=self.name,
                passed=False,
                message=f"{len(issues)} pages have page_id mismatches",
                details=issues[:10],
            )

        return VerificationResult(
            name=self.name,
            passed=True,
            message="All page_ids match file paths",
        )


class WikilinksCheck:
    """Verify wikilinks point to existing pages or are flagged."""

    @property
    def name(self) -> str:
        return "Wikilinks"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult
        from ..frontmatter import parse_page, extract_wikilinks

        broken_links = []

        # Get all page titles for lookup
        page_titles = set()
        for page_path in wiki.list_pages():
            try:
                metadata, _ = parse_page(page_path)
                if "title" in metadata:
                    page_titles.add(metadata["title"])
            except:
                pass

        # Check all wikilinks
        for page_path in wiki.list_pages():
            try:
                _, content = parse_page(page_path)
                links = extract_wikilinks(content)
                for link in links:
                    # Check if link target exists (by title)
                    if link not in page_titles:
                        broken_links.append(f"{page_path.name}: [[{link}]]")
            except:
                pass

        if broken_links:
            return VerificationResult(
                name=self.name,
                passed=False,
                message=f"{len(broken_links)} broken wikilinks found",
                details=broken_links[:10],
            )

        return VerificationResult(
            name=self.name,
            passed=True,
            message="All wikilinks resolve to existing pages",
        )


class ManifestOperationsCheck:
    """Verify manifest operations are consistent."""

    @property
    def name(self) -> str:
        return "Manifest Operations"

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        from ..verify import VerificationResult

        issues = []
        entries = []

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
                if entries[i].timestamp < entries[i - 1].timestamp:
                    issues.append(
                        f"Timestamp regression: {entries[i].op_id} < {entries[i - 1].op_id}"
                    )

        except Exception as e:
            issues.append(f"Manifest read error: {e}")

        if issues:
            return VerificationResult(
                name=self.name,
                passed=False,
                message=f"{len(issues)} manifest issues found",
                details=issues,
            )

        return VerificationResult(
            name=self.name,
            passed=True,
            message=f"Manifest consistent ({len(entries)} operations)",
        )


# Module-level registry instance
# Checks are registered here during module initialization
default_checks: VerificationRegistry = VerificationRegistry()

# Register all built-in checks
default_checks.register("config_exists", ConfigExistsCheck())
default_checks.register("manifest_exists", ManifestExistsCheck())
default_checks.register("directory_structure", DirectoryStructureCheck())
default_checks.register("page_frontmatter", PageFrontmatterCheck())
default_checks.register("revision_hashes", RevisionHashesCheck())
default_checks.register("page_ids", PageIdsCheck())
default_checks.register("wikilinks", WikilinksCheck())
default_checks.register("manifest_operations", ManifestOperationsCheck())


def get_default_checks() -> VerificationRegistry:
    """Get the default verification check registry.

    Returns a registry pre-populated with all built-in verification checks.
    Use this to run the standard verification suite on a wiki.

    Returns:
        VerificationRegistry with default checks registered
    """
    return default_checks
