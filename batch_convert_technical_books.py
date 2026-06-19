#!/usr/bin/env python
"""
Batch convert Technical Books PDFs to markdown using pymupdf4llm.
Skips PDFs already converted (checks markdown_output/ for existing files).
"""

import sys
import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

SOURCE_DIR = Path("/media/ak/d1c5342e-77c5-411d-a9ac-03660a90ce7d/home/ak/Technical Books To Ingest")
OUTPUT_DIR = Path("/media/ak/d1c5342e-77c5-411d-a9ac-03660a90ce7d/home/ak/Gitrepos/LLMWikiGeneration/markdown_output")

# Mapping: PDF filename stem → clean output slug
# (Books already in wiki sources are excluded)
PDF_TO_SLUG = {
    "Agentic Coding for beginners (Wasi) (z-library.sk, 1lib.sk, z-lib.sk)": "wasi-2024-agentic-coding-beginners",
    "A practical guide to building agents (OpenAI) (z-library.sk, 1lib.sk, z-lib.sk)": "openai-2025-practical-guide-building-agents",
    "Beyond Vibe Coding From Coder to AI-Era Developer (Addy Osmani) (z-library.sk, 1lib.sk, z-lib.sk)": "osmani-2025-beyond-vibe-coding",
    "Build a DeepSeek Model (From Scratch) (MEAP) (Raj Abhijit Dandekar, Rajat Dandekar etc.) (z-library.sk, 1lib.sk, z-lib.sk)": "dandekar-2025-build-deepseek-model",
    "Building Embodied AI Systems The Agents, the Architecture Principles, Challenges, and Application Domains (Pethuru Raj, Alvaro Rocha etc.) (z-library.sk, 1lib.sk, z-lib.sk)": "raj-2025-building-embodied-ai-systems",
    # Skip the duplicate "(1)" version
    "Building LLMs for Production Enhancing LLM Abilities and Reliability with Prompting, Fine-Tuning, and RAG (Louis-François Bouchard) (z-library.sk, 1lib.sk, z-lib.sk)": "bouchard-2024-building-llms-production",
    "Building Modern Data Applications Using Databricks Lakehouse (Will Girten) (z-library.sk, 1lib.sk, z-lib.sk)": "girten-2024-building-modern-data-databricks",
    "Claude Code The Definitive Guide to Agentic Development (Written by Claude Code etc.) (z-library.sk, 1lib.sk, z-lib.sk) (1)": "anthropic-2025-claude-code-definitive-guide",
    "Coding with AI (MEAP) (Jeremy C. Morgan) (z-library.sk, 1lib.sk, z-lib.sk)": "morgan-2025-coding-with-ai",
    "Databricks Certified Data Engineer Associate Study Guide (for Raymond Rhine) (Derar Alhussein) (z-library.sk, 1lib.sk, z-lib.sk)": "alhussein-2024-databricks-certified-data-engineer",
    "Databricks. Databricks Spark Knowledge Base () (z-library.sk, 1lib.sk, z-lib.sk)": "databricks-spark-knowledge-base",
    "Databricks Spark 知识库 (it-ebooks) (z-library.sk, 1lib.sk, z-lib.sk)": "databricks-spark-knowledge-base-cn",
    "Data Quality Engineering in Financial Services Applying Manufacturing Techniques to Data (Brian Buzzelli) (z-library.sk, 1lib.sk, z-lib.sk)": "buzzelli-2024-data-quality-engineering-financial",
    "Datenverwaltung mit Unity Catalog auf Databricks (Kiran Sreekumar, Karthik Subbarao) (z-library.sk, 1lib.sk, z-lib.sk)": "sreekumar-2024-datenverwaltung-unity-catalog-databricks",
    "Designing Financial Data Architectures (for Duc ka) (Tamer Khraisha) (z-library.sk, 1lib.sk, z-lib.sk)": "khraisha-2024-designing-financial-data-architectures",
    "Financial Data Engineering Design and Build Data-Driven Financial Products (Tamer Khraisha) (z-library.sk, 1lib.sk, z-lib.sk)": "khraisha-2024-financial-data-engineering",
    "Financial Theory with Python A Gentle Introduction (Yves Hilpisch) (z-library.sk, 1lib.sk, z-lib.sk)": "hilpisch-2021-financial-theory-python",
    "Fundamentals of Data Engineering Plan and Build Robust Data Systems (Joe Reis, Matt Housley) (z-library.sk, 1lib.sk, z-lib.sk)": "reis-2022-fundamentals-data-engineering",
    "Graph Neural Networks in Action (Keita Broadwater, Namid Stillman) (z-library.sk, 1lib.sk, z-lib.sk)": "broadwater-2023-graph-neural-networks-action",
    "Hands-On Large Language Models 动手操作大型语言模型 (Jay Alammar) (z-library.sk, 1lib.sk, z-lib.sk)": None,  # Already in wiki
    "Hands-On RAG for Production (for Raymond Rhine) (First Early Release) (Ofer Mendelevitch, Forrest Bao) (z-library.sk, 1lib.sk, z-lib.sk)": None,  # Already in wiki
    "Hands-on Small Language Models (Alexander Thomas) (z-library.sk, 1lib.sk, z-lib.sk)": "thomas-2025-hands-on-small-language-models",
    "How OpenAI uses Codex (OpenAI) (z-library.sk, 1lib.sk, z-lib.sk)": "openai-2025-how-openai-uses-codex",
    "How we built our multi-agent research system (Anthropic) (z-library.sk, 1lib.sk, z-lib.sk)": "anthropic-2025-multi-agent-research-system",
    "Introduction to Agents (Alan Blount, Antonio Gulli, Shubham Saboo etc.) (z-library.sk, 1lib.sk, z-lib.sk)": "blount-2025-introduction-to-agents",
    "Introduction to Machine Learning Systems Principles and Practices of Engineering Artificially Intelligent Systems (Vijay Janapa Reddi) (z-library.sk, 1lib.sk, z-lib.sk)": "reddi-2024-introduction-ml-systems",
    "Learning AutoML (for . .) (Kerem Tomak) (z-library.sk, 1lib.sk, z-lib.sk)": "tomak-2024-learning-automl",
    "Learning LangChain (Mayo Oshin, Nuno Campos) (z-library.sk, 1lib.sk, z-lib.sk)": None,  # Already in wiki
    "Learning Systems Thinking Essential Non-Linear Skills and Practices for Software Professionals (Diana Montalion) (z-library.sk, 1lib.sk, z-lib.sk)": "montalion-2024-learning-systems-thinking",
    "Math and Architectures of Deep Learning (Krishnendu Chaudhury) (z-library.sk, 1lib.sk, z-lib.sk)": "chaudhury-2024-math-architectures-deep-learning",
    "Mathematical Engineering of Deep Learning (Benoit Liquet, Sarat Moka, Yoni Nazarathy) (z-library.sk, 1lib.sk, z-lib.sk)": "liquet-2024-mathematical-engineering-deep-learning",
    "Multi-Agent Coordination A Reinforcement Learning Approach (Arup Kumar Sadhu, Amit Konar) (z-library.sk, 1lib.sk, z-lib.sk)": "sadhu-2024-multi-agent-coordination-rl",
    "Practical MLOps Operationalizing Machine Learning Models (Noah Gift, Alfredo Deza) (z-library.sk, 1lib.sk, z-lib.sk)": "gift-2021-practical-mlops",
    "Prompt Engineering for LLMs (John Berryman , Albert Ziegler) (z-library.sk, 1lib.sk, z-lib.sk)": None,  # Already in wiki
    "Simulation Models for Data Science (Early Release V2) (Dan Sullivan) (z-library.sk, 1lib.sk, z-lib.sk)": "sullivan-2025-simulation-models-data-science",
    "Software Testing with Generative AI (Mark Winteringham) (z-library.sk, 1lib.sk, z-lib.sk)": "winteringham-2025-software-testing-generative-ai",
    "Statistical Rethinking A Bayesian Course with Examples in R and STAN (Chapman  HallCRC Texts in Statistical Science) (Richard Mcelreath) (z-library.sk, 1lib.sk, z-lib.sk)": "mcelreath-2020-statistical-rethinking",
    "The Elements of Statistical Learning Data Mining, Inference, and Prediction, Second Edition (Trevor Hastie, Robert Tibshirani etc.) (z-library.sk, 1lib.sk, z-lib.sk)": "hastie-2009-elements-statistical-learning",
    "Vector Databases A Practical Introduction (Nitin Borwankar) (z-library.sk, 1lib.sk, z-lib.sk)": None,  # Already in wiki
    "Vibe Coding (Gene KimSteve Yegge  Steve Yegge) (z-library.sk, 1lib.sk, z-lib.sk)": "yegge-2025-vibe-coding",
}

# Books to skip (duplicates or already processed)
SKIP_STEMS = {
    "Building Embodied AI Systems The Agents, the Architecture Principles, Challenges, and Application Domains (Pethuru Raj, Alvaro Rocha etc.) (z-library.sk, 1lib.sk, z-lib.sk) (1)",  # duplicate
}


def convert_pdf(pdf_path: Path, output_slug: str) -> dict:
    import pymupdf4llm
    import pymupdf

    output_md = OUTPUT_DIR / f"{output_slug}.md"
    images_dir = OUTPUT_DIR / f"{output_slug}_images"

    if output_md.exists():
        print(f"  [SKIP] Already converted: {output_slug}.md")
        return {"skipped": True, "path": output_md}

    print(f"  Converting: {pdf_path.name[:60]}...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    md_text = pymupdf4llm.to_markdown(
        str(pdf_path),
        write_images=True,
        image_path=str(images_dir),
        image_format="png",
        dpi=150,
    )

    output_md.write_text(md_text, encoding="utf-8")
    print(f"  [OK] → {output_slug}.md ({len(md_text):,} chars)")
    return {"skipped": False, "path": output_md, "chars": len(md_text)}


def main():
    pdfs = list(SOURCE_DIR.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs in source directory\n")

    to_convert = []
    skipped_already_wiki = []
    skipped_duplicate = []

    for pdf in sorted(pdfs):
        stem = pdf.stem
        if stem in SKIP_STEMS:
            skipped_duplicate.append(pdf.name)
            continue
        slug = PDF_TO_SLUG.get(stem)
        if slug is None:
            skipped_already_wiki.append(pdf.name)
            continue
        to_convert.append((pdf, slug))

    print(f"Already in wiki (skip): {len(skipped_already_wiki)}")
    for n in skipped_already_wiki:
        print(f"  - {n[:70]}")

    print(f"\nDuplicates (skip): {len(skipped_duplicate)}")
    for n in skipped_duplicate:
        print(f"  - {n[:70]}")

    print(f"\nTo convert: {len(to_convert)}")
    for pdf, slug in to_convert:
        print(f"  {slug}")

    print("\n--- Starting conversion ---\n")
    results = []
    for i, (pdf, slug) in enumerate(to_convert, 1):
        print(f"[{i}/{len(to_convert)}] {slug}")
        try:
            r = convert_pdf(pdf, slug)
            results.append((slug, r))
        except Exception as e:
            print(f"  [ERROR] {e}")
            results.append((slug, {"error": str(e)}))

    print("\n--- Summary ---")
    converted = [s for s, r in results if not r.get("skipped") and "error" not in r]
    skipped = [s for s, r in results if r.get("skipped")]
    errors = [s for s, r in results if "error" in r]

    print(f"Converted: {len(converted)}")
    print(f"Already existed (skipped): {len(skipped)}")
    print(f"Errors: {len(errors)}")
    if errors:
        for s in errors:
            print(f"  ERROR: {s}")


if __name__ == "__main__":
    main()
