# rag-salesforce-architect

RAG (Retrieval-Augmented Generation) system designed with an enterprise
/ architect mindset to answer questions about Salesforce technical
documentation (Apex, Flows, ADRs, Confluence exports, PDFs).

------------------------------------------------------------------------

## 🚀 Project Vision

This project aims to build a production-style Retrieval-Augmented
Generation (RAG) system with:

-   Grounded answers (no hallucinations)
-   Explicit evidence retrieval
-   Clean modular architecture
-   Local-first FAISS vector store
-   FastAPI service layer
-   Evaluation-first mindset

------------------------------------------------------------------------

## 📁 Project Structure

    rag-salesforce-architect/
    ├─ data/
    │  ├─ raw/
    │  └─ processed/
    ├─ docs/
    │  ├─ architecture/
    │  └─ runbook/
    ├─ eval/
    ├─ src/
    │  └─ rag_sf_architect/
    │     ├─ ingest/
    │     ├─ retrieve/
    │     ├─ llm/
    │     ├─ api/
    │     └─ scripts/
    ├─ tests/
    ├─ pyproject.toml
    └─ README.md

------------------------------------------------------------------------

## 🛠 Local Setup

### 1. Create virtual environment

``` bash
python -m venv .venv
```

Windows PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

``` bash
python -m pip install -U pip
```

Install project in editable mode:

``` bash
python -m pip install -e .[dev]
```

------------------------------------------------------------------------

## 📄 Add Documentation

Place your documents inside:

    data/raw/

Supported formats:

-   .txt
-   .md
-   .pdf

Example:

``` powershell
"Documento demo: Apex, Flows, Integraciones, Seguridad." | Out-File -Encoding utf8 .\data\raw\demo.txt
```

------------------------------------------------------------------------

## 🏗 Build Vector Index

Recommended:

``` bash
python -m rag_sf_architect.scripts.ingest_local
```

Alternative:

``` bash
python .\src\rag_sf_architect\scripts\ingest_local.py
```

------------------------------------------------------------------------

## 🔎 Query the System

Recommended:

``` bash
python -m rag_sf_architect.scripts.query_local "Que temas cubre el documento"
```

Alternative:

``` bash
python .\src\rag_sf_architect\scripts\query_local.py "Que temas cubre el documento"
```

------------------------------------------------------------------------

## 🧠 Architecture Principles

-   Modular separation: ingest / retrieve / generate
-   Reproducible indexing
-   Explicit citation of evidence
-   Evaluation-driven improvements
-   Enterprise-oriented structure

------------------------------------------------------------------------

## 🧱 Roadmap

### Phase 1 -- Retrieval Foundation

-   Local ingestion
-   FAISS index
-   Evidence retrieval

### Phase 2 -- LLM Integration

-   Claude integration
-   Prompt engineering layer
-   Grounded answer formatting

### Phase 3 -- API Exposure

-   FastAPI endpoints
-   /health
-   /query
-   /ingest

### Phase 4 -- Evaluation & Safety

-   Groundedness tests
-   Hallucination detection
-   Regression dataset

------------------------------------------------------------------------

## 🏷 License

MIT
