from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader

def load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def load_md(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def load_pdf(path: Path) -> List[Dict]:
    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        pages.append({"page": i, "text": text})
    return pages
