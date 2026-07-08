from pathlib import Path
from datetime import date
import argparse, re

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

parser = argparse.ArgumentParser()
parser.add_argument("title")
parser.add_argument("--categories", default="math")
args = parser.parse_args()

slug = slugify(args.title)
folder = Path("posts") / slug
folder.mkdir(parents=True, exist_ok=True)
(folder / "index.qmd").write_text(f"""---
title: "{args.title}"
date: {date.today().isoformat()}
categories: [{args.categories}]
author: "Rahul Manavalan"
---

## Summary

Write the post here.

""")
print(folder / "index.qmd")