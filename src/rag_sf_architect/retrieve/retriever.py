from __future__ import annotations
from pathlib import Path
from typing import List, Dict, Tuple
import json

import faiss
from rag_sf_architect.ingest.build_index import simple_embed

def load_index(index_dir: str) -> Tuple[faiss.Index, List[Dict]]:
    index = faiss.read_index(str(Path(index_dir) / "docs.faiss"))
    chunks = json.loads((Path(index_dir) / "chunks.json").read_text(encoding="utf-8"))
    return index, chunks

def retrieve(index: faiss.Index, chunks: List[Dict], query: str, top_k: int) -> List[Dict]:
    qv = simple_embed([query])
    scores, ids = index.search(qv.astype("float32"), top_k)
    out = []
    for score, idx in zip(scores[0], ids[0]):
        if idx < 0:
            continue
        c = chunks[int(idx)]
        out.append(
            {
                "score": float(score),
                "text": c["text"],
                "source": c["source"],
                "page": c.get("page"),
                "chunk_id": c["chunk_id"],
            }
        )
    return out
