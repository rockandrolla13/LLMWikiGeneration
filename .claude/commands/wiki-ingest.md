Ingest a source document into the wiki. $ARGUMENTS

## PDF Handling - MANDATORY

**If the source is a PDF file (.pdf), you MUST convert it first:**
1. Run `/wiki-convert <pdf_path>` to convert PDF to markdown
2. Then ingest the resulting markdown file from `markdown_output/`

**DO NOT attempt to read or ingest PDF files directly.** The wiki ingests markdown only.

## Duplicate Detection (SHA-256 Idempotency)

Duplicates are automatically detected via SHA-256 content hashing:
- **Exact duplicate**: Same content hash as existing source → SKIP (safe re-run)
- **Content update**: Same slug but different hash → UPDATE existing page
- **New source**: No match → CREATE new page

The `content_hash` field is stored in source page frontmatter for tracking.

## Process

If no source path is provided, list files in raw/ and ask which to ingest.

Before ingesting, read the source and discuss with user:
1. What is the main thesis or contribution?
2. What entities (people, orgs, places) are mentioned?
3. What concepts does this relate to?
4. Does this contradict anything already in the wiki?
5. What should be emphasized?

Then execute:

```python
from pathlib import Path
from llm_wiki import (
    Wiki, wiki_ingest, is_omega_available, store_wiki_event,
    check_duplicate, format_duplicate_result
)

wiki = Wiki(Path("."))
source_path = Path("<source_path>")

# Check for duplicates first
source_content = source_path.read_text()
slug = source_path.stem  # or compute from title
wiki_sources = wiki.root / "wiki" / "sources"

dup_result = check_duplicate(wiki_sources, source_content, slug)
if dup_result.is_duplicate:
    print(f"SKIP: Duplicate of {dup_result.existing_path}")
else:
    result = wiki_ingest(
        wiki,
        source_path=source_path,
        title="<title>",
        source_type="<type>",  # article, paper, book, video, podcast, note
        authors=["<author1>", "<author2>"],
        content_hash=dup_result.new_hash,  # Include hash in metadata
    )

    if result["success"]:
        print(f"Ingested: {result['source_page']}")
        print(f"Created pages: {result.get('created_pages', [])}")

        # Store in OMEGA
        if is_omega_available():
            store_wiki_event(
                "decision",
                f"Ingested '{result['title']}' - created {len(result.get('created_pages', []))} pages",
                wiki_name=wiki.config.name,
            )
    else:
        print(f"Error: {result['error']}")
```

After ingestion:
1. Show the source summary page created
2. List entity and concept pages created/updated
3. Show updated links in index.md
4. Suggest next sources to add or questions to explore
