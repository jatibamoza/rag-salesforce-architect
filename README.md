# rag-salesforce-architect

RAG (Retrieval-Augmented Generation) system designed with an **enterprise/architect mindset**
to answer questions about Salesforce technical documentation (Apex, Flows, ADRs, Confluence exports, PDFs).

This project focuses on:

- Grounded answers (no hallucinations)
- Explicit evidence retrieval
- Clean modular architecture
- Local-first design (FAISS)
- API-ready structure (FastAPI)

---

# 🚀 Project Vision

The goal is to design a Retrieval-Augmented Generation system as an AI Architect would:

- Ingest technical documentation
- Chunk and embed documents
- Store vectors in FAISS
- Retrieve relevant evidence
- Generate answers grounded in sources
- Expose as an API service
- Include evaluation to reduce hallucinations

---

# 📁 Project Structure
rag-salesforce-architect/
├─ data/
│ ├─ raw/ # Input documents
│ └─ processed/ # FAISS index (gitignored)
├─ docs/
│ ├─ architecture/
│ └─ runbook/
├─ eval/
├─ src/
│ └─ rag_sf_architect/
│ ├─ ingest/
│ ├─ retrieve/
│ ├─ llm/
│ ├─ api/
│ └─ scripts/
├─ tests/
├─ pyproject.toml
└─ README.md

---

# 🛠 Local Setup

## 1️⃣ Create virtual environment

```bash
python -m venv .venv

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Upgrade pip:

python -m pip install -U pip

Install project in editable mode:

python -m pip install -e .[dev]

📄 Add Documentation

Place your documents inside:
data/raw/

Supported formats:

.txt
.md
.pdf

Example (Windows PowerShell):

"Documento demo: Apex, Flows, Integraciones, Seguridad." | Out-File -Encoding utf8 .\data\raw\demo.txt

🏗 Build Vector Index
Recommended (module execution)

python -m rag_sf_architect.scripts.ingest_local

Alternative (direct file execution)

python .\src\rag_sf_architect\scripts\ingest_local.py

If successful, you should see:

OK - indexed X chunks into: ./data/processed/index


```

🔎 Query the System
Recommended (module execution)

Alternative (direct file execution)

python .\src\rag_sf_architect\scripts\query_local.py "Que temas cubre el documento"


Output includes:

* Question
* Top matching chunks
* Source file
* Page number (if PDF)
* Retrieval score

🧠 Architecture Overview

Current architecture includes:

Document ingestion

Chunking with overlap

Simple baseline embeddings (placeholder)

FAISS vector store

Top-k retrieval

Evidence output

Next iterations:

Replace baseline embeddings with production-grade embeddings

Add LLM integration (Claude / other)

Add grounded answer generation

Add FastAPI endpoints

Add evaluation pipeline

🔐 Design Principles

This project follows enterprise architecture principles:

Modular design

Separation of ingestion / retrieval / generation

Reproducible indexing

Explicit citation of evidence

Local-first (no hidden external dependencies)

Evaluation-driven improvements

🧪 Development

Run tests:

```bash
pytest
```

Lint with Ruff:

```bash
ruff check .
```

🧱 Roadmap
Phase 1 – Retrieval Foundation (current)

Local ingestion

FAISS index

Evidence retrieval

Phase 2 – LLM Integration

Prompt engineering layer

Claude integration

Grounded response formatting

Phase 3 – API Exposure

FastAPI service

/health

/query

/ingest

Phase 4 – Evaluation & Safety

Groundedness tests

Hallucination detection

Regression dataset

📌 Non-Goals (for now)

Multi-tenant authentication

Cloud vector DB

Complex reranking pipelines

Production deployment

🏷 License
MIT
