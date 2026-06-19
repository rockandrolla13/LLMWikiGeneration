Convert a PDF to markdown for wiki ingestion. $ARGUMENTS

**IMPORTANT:** This skill MUST be used before ingesting any PDF file. PDFs cannot be ingested directly.

## Usage

```
/wiki-convert path/to/paper.pdf
/wiki-convert raw/conformal-prediction/paper.pdf
```

## Process

1. Validate the PDF exists
2. Run pymupdf4llm conversion
3. Extract images to accompanying directory
4. Report conversion results

## Execution

```bash
# Activate the wiki environment and run converter
conda run -n llm-wiki python "$(git rev-parse --show-toplevel)/test_marker.py" "<pdf_path>"
```

The script outputs:
- Markdown file: `markdown_output/<filename>.md`
- Images directory: `markdown_output/<filename>_images/`

## After Conversion

1. Review the markdown preview shown
2. Check image count and quality
3. Proceed with `/wiki-ingest markdown_output/<filename>.md`

## Troubleshooting

If conversion fails:
- Ensure `llm-wiki` conda environment is active
- Check pymupdf4llm is installed: `pip show pymupdf4llm`
- For scanned PDFs, Tesseract OCR is used automatically

## Tool Chain

For academic papers with complex elements:
1. `/wiki-convert` - Text, images, basic tables (pymupdf4llm)
2. For citations: GROBID client (when server available)
3. For equations: pix2text (if installed)
