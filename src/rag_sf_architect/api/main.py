from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

from rag_sf_architect.config import settings
from rag_sf_architect.ingest.build_index import build_and_save
from rag_sf_architect.retrieve.retriever import load_index, retrieve

app = FastAPI(
    title="rag-salesforce-architect",
    version="0.1.0",
    description="Local RAG retrieval API (FAISS) with evidence output.",
)


class Evidence(BaseModel):
    score: float
    text: str
    source: str
    page: Optional[int] = None
    chunk_id: str


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User question")
    top_k: Optional[int] = Field(None, ge=1, le=20, description="Override default top_k (1..20)")


class QueryResponse(BaseModel):
    question: str
    top_k: int
    evidence: List[Evidence]


class IngestResponse(BaseModel):
    chunks_indexed: int
    index_dir: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/ingest", response_model=IngestResponse)
def ingest() -> IngestResponse:
    try:
        n = build_and_save(settings.data_dir, settings.index_dir)
        return IngestResponse(chunks_indexed=n, index_dir=settings.index_dir)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest) -> QueryResponse:
    top_k = req.top_k if req.top_k is not None else settings.top_k

    try:
        index, chunks = load_index(settings.index_dir)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=f"Index not found or unreadable. Run /ingest first. Expected in: {settings.index_dir}",
        )

    hits = retrieve(index, chunks, req.question, top_k)
    evidence = [Evidence(**h) for h in hits]
    return QueryResponse(question=req.question, top_k=top_k, evidence=evidence)