from typing import List, Dict

def chunk_text(text: str, chunk_size: int = 900, overlap: int = 120) -> List[str]:
    text = " ".join(text.split())
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks

def make_chunks(doc_id: str, text: str, source: str, page: int | None = None) -> List[Dict]:
    out = []
    for idx, ch in enumerate(chunk_text(text)):
        out.append(
            {
                "doc_id": doc_id,
                "chunk_id": f"{doc_id}::c{idx}",
                "text": ch,
                "source": source,
                "page": page,
            }
        )
    return out
