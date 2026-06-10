import pymupdf4llm
import pathlib
import sys

pdf_dir = pathlib.Path("/home/ak/Documents/Momentum For Corporate Bonds")
output_dir = pathlib.Path("markdown_output")
output_dir.mkdir(exist_ok=True)

pdfs = sorted([p for p in pdf_dir.glob("*.pdf") if "(1)" not in p.name])
total = len(pdfs)

for i, pdf in enumerate(pdfs, 1):
    out_file = output_dir / f"{pdf.stem}.md"
    print(f"[{i}/{total}] Converting: {pdf.name}...", flush=True)
    try:
        md_text = pymupdf4llm.to_markdown(str(pdf))
        out_file.write_text(md_text)
        print(f"    ✓ {out_file.name} ({len(md_text)} chars)")
    except Exception as e:
        print(f"    ✗ Error: {e}")

print(f"\nDone! Converted {total} PDFs.")
