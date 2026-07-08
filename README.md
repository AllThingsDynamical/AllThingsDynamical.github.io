# AllThingsDynamical.github.io

A polished Quarto academic portfolio and math blog template.

## Local preview

```bash
quarto preview
```

## Render

```bash
quarto render
```

## Create a new post

```bash
python scripts/new_post.py "My New Math Note" --categories "math,numerics"
```

## Convert a PDF into a draft post

```bash
pip install pymupdf
python scripts/pdf_to_post.py path/to/file.pdf --title "My Imported Note"
```

## Deploy to GitHub Pages

1. Create the GitHub repository:

```text
AllThingsDynamical.github.io
```

2. Push this folder to `main`.

3. In GitHub:

```text
Settings → Pages → Source → GitHub Actions
```

The site will appear at:

```text
https://allthingsdynamical.github.io
```

## Edit these first

- `_quarto.yml`: email, title, social links.
- `index.qmd`: homepage text.
- `publications.qmd`: real papers.
- `assets/cv/cv.pdf`: your real CV.
- `references.bib`: bibliography.