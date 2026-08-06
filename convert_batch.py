#!/usr/bin/env python3
"""Convert PDFs to markdown for wiki ingestion.

Takes a folder, a single PDF, or several of either. Output goes to
markdown_output/ as one .md per PDF, which is the staging area the wiki
ingest step reads from.

Run inside the llm-wiki environment, which is where pymupdf4llm lives:

    conda run -n llm-wiki python convert_batch.py "/path/to/folder"
    conda run -n llm-wiki python convert_batch.py paper1.pdf paper2.pdf
    conda run -n llm-wiki python convert_batch.py --recursive "/path/to/folder"
    conda run -n llm-wiki python convert_batch.py --dry-run "/path/to/folder"

Conversion is the easy half. Turning the markdown into concept and entity
pages is a reading job, not a scripted one -- and doing it unattended is how
this wiki ended up with 569 links to pages that were never written. Convert in
bulk; ingest in small batches you actually look at.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "markdown_output"


def collect_pdfs(inputs: list[str], recursive: bool) -> list[Path]:
    """Expand the given files and folders into a sorted list of PDFs.

    Args:
        inputs: Paths to PDF files or folders containing them
        recursive: Whether to descend into subfolders

    Returns:
        Sorted, de-duplicated list of PDF paths
    """
    found: list[Path] = []
    for raw in inputs:
        path = Path(raw).expanduser()
        if not path.exists():
            print(f"  ! not found, skipping: {path}")
            continue
        if path.is_file():
            if path.suffix.lower() == ".pdf":
                found.append(path)
            else:
                print(f"  ! not a PDF, skipping: {path.name}")
        else:
            found.extend(path.rglob("*.pdf") if recursive else path.glob("*.pdf"))

    # Duplicate downloads land as "name (1).pdf"; they convert to the same stem.
    found = [p for p in found if "(1)" not in p.name]
    return sorted(set(found))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert PDFs to markdown in markdown_output/.",
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="PDF files and/or folders containing PDFs",
    )
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Descend into subfolders",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Reconvert even if the .md already exists (default: skip)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List what would be converted and stop",
    )
    args = parser.parse_args()

    pdfs = collect_pdfs(args.inputs, args.recursive)
    if not pdfs:
        print("No PDFs found.")
        return 1

    OUTPUT_DIR.mkdir(exist_ok=True)

    pending, skipped = [], []
    for pdf in pdfs:
        out = OUTPUT_DIR / f"{pdf.stem}.md"
        (skipped if out.exists() and not args.force else pending).append(pdf)

    print(f"Found {len(pdfs)} PDF(s): {len(pending)} to convert, "
          f"{len(skipped)} already converted.")
    if skipped and not args.force:
        print("  (pass --force to reconvert those)")

    if args.dry_run:
        for pdf in pending:
            print(f"  would convert: {pdf.name}")
        return 0

    # Imported here so --dry-run and --help work outside the llm-wiki env.
    try:
        import pymupdf4llm
    except ImportError:
        print("\npymupdf4llm is not available in this interpreter.")
        print("Run inside the wiki environment:")
        print('  conda run -n llm-wiki python convert_batch.py "<path>"')
        return 1

    ok = failed = 0
    for i, pdf in enumerate(pending, 1):
        out = OUTPUT_DIR / f"{pdf.stem}.md"
        print(f"[{i}/{len(pending)}] {pdf.name}", flush=True)
        try:
            text = pymupdf4llm.to_markdown(str(pdf))
            out.write_text(text, encoding="utf-8")
            print(f"    ok  {out.name} ({len(text):,} chars)")
            ok += 1
        except Exception as e:
            print(f"    FAILED  {type(e).__name__}: {e}")
            failed += 1

    print(f"\nConverted {ok}, failed {failed}, skipped {len(skipped)}.")
    print(f"Markdown is in {OUTPUT_DIR}/")
    print("Next: ask Claude to ingest those files, in small batches you can check.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
