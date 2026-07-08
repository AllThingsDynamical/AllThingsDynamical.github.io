"""
Convert a PDF into a draft Quarto blog post.

Usage:
    python scripts/pdf_to_post.py path/to/file.pdf --title "My Post Title"

Notes:
    This extracts text. It does not perfectly preserve mathematical layout.
    For serious math posts, prefer TeX/Markdown/Quarto as the source.
"""
from pathlib import Path
import argparse
import re
import sys
from datetime import date

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "pdf-post"

def extract_text(pdf_path: Path) -> str:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        raise SystemExit("Install PyMuPDF first: pip install pymupdf")
    doc = fitz.open(pdf_path)
    parts = []
    for i, page in enumerate(doc, start=1):
        parts.append(f"\\n\\n## Page {i}\\n\\n")
        parts.append(page.get_text("text"))
    return "\\n".join(parts).strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--title", default=None)
    parser.add_argument("--categories", default="pdf,draft")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f"File not found: {pdf_path}")

    title = args.title or pdf_path.stem.replace("_", " ").replace("-", " ").title()
    slug = slugify(title)
    out_dir = Path("posts") / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    text = extract_text(pdf_path)
    pdf_copy = out_dir / pdf_path.name
    pdf_copy.write_bytes(pdf_path.read_bytes())

    cats = ", ".join([c.strip() for c in args.categories.split(",") if c.strip()])
    qmd = f"""---
title: "{title}"
date: {date.today().isoformat()}
categories: [{cats}]
draft: true
---

[Download original PDF]({pdf_path.name})

> This post was imported from a PDF and needs manual cleanup.

{text}
"""
    (out_dir / "index.qmd").write_text(qmd, encoding="utf-8")
    print(f"Created draft: {out_dir / 'index.qmd'}")

if __name__ == "__main__":
    main()