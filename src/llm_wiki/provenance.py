"""Numeric provenance: does a source page's arithmetic come from its document?

A wiki page summarising a paper is easy to write and hard to check. The failure
mode that matters is not a wrong link or a missing field -- it is a figure that
looks precise and was invented. Two were caught by hand during the August 2026
ingest: a beta of "-1.51" attributed to Daniel & Moskowitz (2016), whose paper
contains no such number, and factor counts of "8.9" and "7.7" attributed to Li,
Chen & Linton (2023), mixed into a sentence whose other five figures were real.
That mixture is the dangerous shape: genuine numbers lend credibility to the
invented ones sitting beside them.

This module turns that hand check into a repeatable one. For every source page
that records where it came from, every decimal figure in its prose must appear
somewhere in the source document. It is a blunt test and it is meant to be:
cheap, mechanical, and hard to talk your way past.

What it deliberately does NOT do:

- It does not check that a figure means what the page says it means. A number
  can be present in the document and still be misattributed.
- It does not check whole numbers. Years, counts and section numbers collide
  with everything and produce noise.
- It does not check pages with no recorded source. Those are reported
  separately as unverifiable rather than silently passing.
- It does not check pages whose source is a PDF. Comparing prose against
  binary produces confident nonsense; convert the PDF first.

Rejected relaxation: accepting a percent/fraction twin (0.9999 for "99.99%")
was tried and removed. It reads as reasonable, but small values have twins that
occur in almost any document -- 0.2 passes because "20" appears somewhere, 0.5
because "50" does -- and it waved through figures already known to be invented.
A page that paraphrases a quantile as a percentage should say so in the
paper's own notation instead. Precision here is worth more than convenience.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# Decimals only. Integers ("2019", "3 factors", "Section 4") match too much
# text to be evidence of anything.
_DECIMAL = re.compile(r"\d+\.\d+")

# Wikilinks carry page slugs and years that are navigation, not claims.
_WIKILINK = re.compile(r"\[\[[^\]]*\]\]")

# arXiv IDs, DOIs and version strings look like decimals but name a thing rather
# than measure one. DOI prefixes ("10.1214") were flagged as invented figures
# until this covered them.
_IDENTIFIER = re.compile(
    r"(?:arxiv[:\s]*)?\b\d{4}\.\d{4,5}(?:v\d+)?\b"   # arXiv: 1905.02928v1
    r"|\b10\.\d{4,9}(?:[./][\w.()/-]+)*"                # DOI:   10.1214/20-AOS1965
    r"|\bv?\d+\.\d+\.\d+\b",                          # semver: 1.2.3
    re.IGNORECASE,
)

# Only text sources can be compared. A PDF read as text yields garbage.
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".rst"}

# Fenced code and inline code are usually formulae or identifiers.
_CODE_FENCE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`]*`")


@dataclass
class ProvenanceResult:
    """Outcome of checking one page against its source document."""

    page_id: str
    source_path: str | None
    checked: int = 0
    unsupported: list[str] = field(default_factory=list)
    note: str | None = None

    @property
    def verifiable(self) -> bool:
        """Whether the page could be checked at all."""
        return self.note is None

    @property
    def passed(self) -> bool:
        return self.verifiable and not self.unsupported


def extract_numeric_claims(body: str) -> set[str]:
    """Pull the decimal figures a page asserts, ignoring navigation and code.

    Args:
        body: Markdown body of a wiki page

    Returns:
        Set of decimal strings the page states as fact
    """
    text = _CODE_FENCE.sub(" ", body)
    text = _INLINE_CODE.sub(" ", text)
    text = _WIKILINK.sub(" ", text)
    text = _IDENTIFIER.sub(" ", text)
    return set(_DECIMAL.findall(text))


def normalize_document(text: str) -> str:
    """Flatten a document so figures match despite PDF-extraction spacing.

    PDF conversion inserts newlines and thin spaces inside numbers, so "1,234.5"
    can arrive as "1, 234. 5". Stripping whitespace and commas makes the
    comparison robust without making it meaningless.
    """
    return re.sub(r"[,\s]", "", text)


def resolve_source_path(wiki_root: Path, source_path: str) -> Path | None:
    """Find the document a page was written from.

    `source_path` is recorded relative to the wiki root in most pages, but
    absolute and repo-relative forms both exist in this corpus.

    Args:
        wiki_root: The wiki directory (the one holding schema.yml)
        source_path: Value of the page's source_path field

    Returns:
        An existing path, or None if the document cannot be found
    """
    candidates = [
        Path(source_path),
        wiki_root / source_path,
        wiki_root.parent / source_path,
    ]
    for c in candidates:
        if c.exists() and c.is_file():
            return c
    return None


def check_page_provenance(
    wiki_root: Path,
    page_id: str,
    metadata: dict,
    body: str,
) -> ProvenanceResult:
    """Check one page's figures against the document it came from.

    Args:
        wiki_root: The wiki directory
        page_id: Page identifier, for reporting
        metadata: Page frontmatter
        body: Page markdown body

    Returns:
        ProvenanceResult; `note` is set when the page could not be checked
    """
    source_path = metadata.get("source_path")
    if not source_path:
        return ProvenanceResult(page_id, None, note="no source_path recorded")

    resolved = resolve_source_path(wiki_root, str(source_path))
    if resolved is None:
        return ProvenanceResult(
            page_id, str(source_path), note=f"source document not found: {source_path}"
        )

    if resolved.suffix.lower() not in TEXT_SUFFIXES:
        # Comparing prose against PDF bytes flags every real figure as invented.
        return ProvenanceResult(
            page_id,
            str(source_path),
            note=f"source is {resolved.suffix or 'binary'}, not text; convert it first",
        )

    try:
        document = normalize_document(resolved.read_text(encoding="utf-8", errors="ignore"))
    except OSError as e:
        return ProvenanceResult(page_id, str(source_path), note=f"unreadable: {e}")

    claims = extract_numeric_claims(body)
    unsupported = sorted(c for c in claims if c not in document)
    return ProvenanceResult(page_id, str(source_path), len(claims), unsupported)


def check_wiki_provenance(wiki) -> list[ProvenanceResult]:
    """Check every source page in the wiki.

    Args:
        wiki: Wiki instance

    Returns:
        One ProvenanceResult per source page
    """
    from .io import parse_page
    from .schemas import PageType

    results = []
    for path in sorted(wiki.list_pages(PageType.SOURCE)):
        try:
            metadata, body = parse_page(path)
        except Exception as e:
            results.append(
                ProvenanceResult(path.stem, None, note=f"page unreadable: {e}")
            )
            continue
        page_id = metadata.get("page_id") or path.stem
        results.append(check_page_provenance(wiki.root, page_id, metadata, body))
    return results
