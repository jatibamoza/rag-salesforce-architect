from __future__ import annotations
from pathlib import Path
from typing import List, Dict, Tuple
import os
import json

import numpy as np
import faiss

from .loaders import load_txt, load_md, load_pdf
from .chunking import make_chunks

def simple_embed(texts: List[str]) -> np.ndarray:
    """
    Baseline embeddings (no external model): hashed bag-of-words style.
    We replace this with real embeddings later.
    """
    dim = 384
    vecs = np.zeros((len(texts), dim), dtype="float32")
    for i, t in enumerate(texts):
        for token in t.lower().split():
            h = hash(token) % dim
            vecs[i, h] += 1.0
        norm = np.linalg.norm(vecs[i]) + 1e-9
        vecs[i] /= norm
    return vecs

def ingest_dir(data_dir: str) -> List[Dict]:
    p = Path(data_dir)
    chunks: List[Dict] = []
    if not p.exists():
        return chunks

    for path in sorted(p.glob("*")):
        suf = path.suffix.lower()
        if suf == ".txt":
            text = load_txt(path)
            chunks.extend(make_chunks(path.stem, text, source=str(path)))
        elif suf == ".md":
            text = load_md(path)
            chunks.extend(make_chunks(path.stem, text, source=str(path)))
        elif suf == ".pdf":
            pages = load_pdf(path)
            for pg in pages:
                chunks.extend(make_chunks(path.stem, pg["text"], source=str(path), page=pg["page"]))
    return chunks

def build_faiss(chunks: List[Dict]) -> Tuple[faiss.IndexFlatIP, List[Dict]]:
    texts = [c["text"] for c in chunks]
    emb = simple_embed(texts)
    index = faiss.IndexFlatIP(emb.shape[1])
    index.add(emb)
    return index, chunks

def save_index(index_dir: str, index: faiss.IndexFlatIP, chunks: List[Dict]) -> None:
    os.makedirs(index_dir, exist_ok=True)
    faiss.write_index(index, str(Path(index_dir) / "docs.faiss"))
    (Path(index_dir) / "chunks.json").write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

def build_and_save(data_dir: str, index_dir: str) -> int:
    chunks = ingest_dir(data_dir)
    if not chunks:
        raise ValueError(f"No documents found in {data_dir}. Add files to data/raw first.")
    index, chunks = build_faiss(chunks)
    save_index(index_dir, index, chunks)
    return len(chunks)
