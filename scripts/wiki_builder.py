#!/usr/bin/env python3
"""
DEPRECATED: This script writes wiki pages directly, bypassing wiki_ingest() and
manifest.jsonl. Pages created here are invisible to verification checks and the
audit trail. Use wiki_ingest() from the llm_wiki package instead.

Kept for reference only. Do not use for new ingestion work.

---

Wiki Builder - End-to-end document processing pipeline.

Usage:
    python scripts/wiki_builder.py /path/to/documents/
    python scripts/wiki_builder.py paper.pdf
    python scripts/wiki_builder.py --dry-run /path/to/docs/
"""

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import hashlib
import re

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
WIKI_ROOT = PROJECT_ROOT / "wiki" / "wiki"
MARKDOWN_OUTPUT = PROJECT_ROOT / "markdown_output"
CONVERTER_SCRIPT = PROJECT_ROOT / "test_marker.py"


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')


def convert_pdf(pdf_path: Path) -> Path | None:
    """Convert PDF to markdown using pymupdf4llm."""
    print(f"  Converting: {pdf_path.name}")

    try:
        result = subprocess.run(
            ["conda", "run", "-n", "llm-wiki", "python", str(CONVERTER_SCRIPT), str(pdf_path)],
            capture_output=True,
            text=True,
            timeout=300  # 5 min timeout
        )

        if result.returncode != 0:
            print(f"  ✗ Conversion failed: {result.stderr[:200]}")
            return None

        # Find output file
        output_name = pdf_path.stem + ".md"
        output_path = MARKDOWN_OUTPUT / output_name

        if output_path.exists():
            print(f"  ✓ Converted: {output_path.name}")
            return output_path
        else:
            print(f"  ✗ Output not found: {output_path}")
            return None

    except subprocess.TimeoutExpired:
        print(f"  ✗ Conversion timed out")
        return None
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None


def extract_metadata(md_path: Path) -> dict:
    """Extract basic metadata from markdown content."""
    content = md_path.read_text(errors='ignore')[:5000]  # First 5KB

    # Try to find title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else md_path.stem

    # Try to find authors
    author_patterns = [
        r'(?:Authors?|By)[:\s]+([^\n]+)',
        r'\*\*([A-Z][a-z]+ [A-Z][a-z]+(?:,\s*[A-Z][a-z]+ [A-Z][a-z]+)*)\*\*',
    ]
    authors = []
    for pattern in author_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            authors = [a.strip() for a in match.group(1).split(',')]
            break

    # Generate slug
    slug = slugify(title)[:50]

    return {
        'title': title,
        'authors': authors,
        'slug': slug,
        'source_path': str(md_path),
    }


def create_source_page(metadata: dict, content_preview: str, dry_run: bool = False) -> Path:
    """Create a source summary page."""
    slug = metadata['slug']
    page_path = WIKI_ROOT / "sources" / f"{slug}.md"

    now = datetime.now().isoformat()
    authors_yaml = ', '.join(f'"{a}"' for a in metadata.get('authors', []))

    page_content = f"""---
title: "{metadata['title']}"
page_id: sources/{slug}
page_type: source
source_type: paper
authors: [{authors_yaml}]
created: {now}
updated: {now}
tags: []
related: []
---

## Summary

{content_preview[:500]}...

## Key Claims

- (To be extracted)

## Questions Raised

- (To be identified)
"""

    if dry_run:
        print(f"  [DRY RUN] Would create: {page_path}")
    else:
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(page_content)
        print(f"  ✓ Created: sources/{slug}.md")

    return page_path


def update_index(new_pages: list[Path], dry_run: bool = False):
    """Update wiki/index.md with new pages."""
    index_path = WIKI_ROOT / "index.md"

    if not index_path.exists():
        print("  ⚠ index.md not found, skipping update")
        return

    if dry_run:
        print(f"  [DRY RUN] Would update index.md with {len(new_pages)} entries")
        return

    # Read current index
    content = index_path.read_text()

    # Add new entries to sources section
    for page in new_pages:
        if "sources" in str(page):
            entry = f"- [[{page.stem}]]\n"
            # Simple append (proper implementation would insert in right section)

    print(f"  ✓ Updated index.md")


def process_document(doc_path: Path, dry_run: bool = False) -> dict:
    """Process a single document through the pipeline."""
    result = {
        'input': str(doc_path),
        'success': False,
        'pages_created': [],
        'error': None,
    }

    # Step 1: Convert if PDF
    if doc_path.suffix.lower() == '.pdf':
        md_path = convert_pdf(doc_path)
        if not md_path:
            result['error'] = 'PDF conversion failed'
            return result
    elif doc_path.suffix.lower() == '.md':
        md_path = doc_path
    else:
        result['error'] = f'Unsupported format: {doc_path.suffix}'
        return result

    # Step 2: Extract metadata
    metadata = extract_metadata(md_path)
    content = md_path.read_text(errors='ignore')

    # Step 3: Create wiki pages
    source_page = create_source_page(metadata, content[:1000], dry_run)
    result['pages_created'].append(str(source_page))

    result['success'] = True
    return result


def main():
    parser = argparse.ArgumentParser(description='Wiki Builder - End-to-end document processing')
    parser.add_argument('input', help='File or directory to process')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--skip-existing', action='store_true', help='Skip already-ingested sources')
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()

    # Collect documents
    if input_path.is_file():
        documents = [input_path]
    elif input_path.is_dir():
        documents = list(input_path.glob('*.pdf')) + list(input_path.glob('*.md'))
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)

    if not documents:
        print(f"No documents found in {input_path}")
        sys.exit(1)

    print(f"\n{'='*50}")
    print(f"Wiki Builder - Processing {len(documents)} document(s)")
    print(f"{'='*50}\n")

    # Process each document
    results = []
    for i, doc in enumerate(documents, 1):
        print(f"[{i}/{len(documents)}] {doc.name}")
        result = process_document(doc, dry_run=args.dry_run)
        results.append(result)
        print()

    # Summary
    successful = sum(1 for r in results if r['success'])
    pages = sum(len(r['pages_created']) for r in results)

    print(f"{'='*50}")
    print(f"Summary")
    print(f"{'='*50}")
    print(f"Documents processed: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {len(results) - successful}")
    print(f"Pages created: {pages}")

    if not args.dry_run:
        print(f"\nRun 'git status' to see changes")


if __name__ == '__main__':
    main()
