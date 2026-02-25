import sys
from rag_sf_architect.config import settings
from rag_sf_architect.retrieve.retriever import load_index, retrieve

def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python -m rag_sf_architect.scripts.query_local "your question"')
        raise SystemExit(2)

    q = sys.argv[1]
    index, chunks = load_index(settings.index_dir)
    hits = retrieve(index, chunks, q, settings.top_k)

    print("\nQUESTION:")
    print(q)
    print("\nTOP EVIDENCE:")
    for i, h in enumerate(hits, start=1):
        where = h["source"]
        if h.get("page"):
            where += f" (page {h['page']})"
        print(f"\n[{i}] score={h['score']:.4f} | {where} | {h['chunk_id']}")
        print(h["text"][:500] + ("..." if len(h["text"]) > 500 else ""))

if __name__ == "__main__":
    main()