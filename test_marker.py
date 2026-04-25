#!/usr/bin/env python
"""
Test script for PDF to Markdown conversion using pymupdf4llm.

This script demonstrates how to use pymupdf4llm to convert PDF documents
to markdown with extracted images. This is a lightweight alternative to
marker-pdf that doesn't require GPU/ML models.

Installation:
    pip install pymupdf4llm
"""

import os
import sys
from pathlib import Path

# Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def convert_pdf_to_markdown(pdf_path: str, output_dir: str = "./markdown_output") -> dict:
    """
    Convert a PDF file to markdown using pymupdf4llm.

    Args:
        pdf_path: Path to the PDF file to convert
        output_dir: Directory to save output markdown and images

    Returns:
        dict with keys: 'markdown', 'markdown_path', 'images', 'images_dir', 'metadata'
    """
    try:
        import pymupdf4llm
        import pymupdf
    except ImportError:
        raise ImportError(
            "pymupdf4llm is not installed. Install it with:\n"
            "    pip install pymupdf4llm"
        )

    # Validate input
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    # Create output directories
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create image output directory based on PDF filename
    pdf_stem = pdf_path.stem
    images_dir = output_dir / f"{pdf_stem}_images"
    images_dir.mkdir(parents=True, exist_ok=True)

    print(f"Converting PDF using pymupdf4llm (lightweight, no ML models needed)...")

    # Convert PDF to markdown with image extraction
    # pymupdf4llm.to_markdown returns markdown text directly
    # Use write_images=True to extract images
    markdown_text = pymupdf4llm.to_markdown(
        str(pdf_path),
        write_images=True,
        image_path=str(images_dir),
        image_format="png",
        dpi=150,  # Image resolution
    )

    # Save markdown to file
    output_md_path = output_dir / f"{pdf_stem}.md"
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)
    print(f"Markdown saved to: {output_md_path}")

    # Find saved images in the images directory
    saved_images = []
    if images_dir.exists():
        for img_file in images_dir.iterdir():
            if img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
                saved_images.append(str(img_file))
                print(f"Image saved to: {img_file}")

    if not saved_images:
        print("No images extracted from PDF")

    # Extract metadata using pymupdf directly
    metadata = {}
    try:
        doc = pymupdf.open(str(pdf_path))
        metadata = {
            'title': doc.metadata.get('title', ''),
            'author': doc.metadata.get('author', ''),
            'subject': doc.metadata.get('subject', ''),
            'keywords': doc.metadata.get('keywords', ''),
            'creator': doc.metadata.get('creator', ''),
            'producer': doc.metadata.get('producer', ''),
            'creationDate': doc.metadata.get('creationDate', ''),
            'modDate': doc.metadata.get('modDate', ''),
            'page_count': len(doc),
        }
        doc.close()
    except Exception as e:
        print(f"Warning: Could not extract metadata: {e}")

    print(f"\nConversion complete!")
    print(f"  Markdown file: {output_md_path}")
    print(f"  Images directory: {images_dir}")
    print(f"  Total images: {len(saved_images)}")

    return {
        'markdown': markdown_text,
        'markdown_path': str(output_md_path),
        'images': saved_images,
        'images_dir': str(images_dir),
        'metadata': metadata
    }


def main():
    """Main entry point for the test script."""
    # Default test PDF path
    default_pdf = "/home/ak/Documents/Conformal Prediction/johnstone25a.pdf"

    # Allow override from command line
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = default_pdf

    # Output directory
    output_dir = Path(__file__).parent / "markdown_output"

    print(f"PDF to Markdown Converter Test")
    print(f"=" * 50)
    print(f"Input PDF: {pdf_path}")
    print(f"Output dir: {output_dir}")
    print(f"=" * 50)
    print()

    try:
        result = convert_pdf_to_markdown(pdf_path, str(output_dir))

        # Print a preview of the markdown
        print(f"\n{'=' * 50}")
        print("MARKDOWN PREVIEW (first 2000 characters):")
        print(f"{'=' * 50}")
        print(result['markdown'][:2000])
        if len(result['markdown']) > 2000:
            print(f"\n... (truncated, total length: {len(result['markdown'])} characters)")

        return 0

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1
    except ImportError as e:
        print(f"ERROR: {e}")
        return 1
    except Exception as e:
        print(f"ERROR during conversion: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
