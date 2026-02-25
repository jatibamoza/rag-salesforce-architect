from rag_sf_architect.config import settings
from rag_sf_architect.ingest.build_index import build_and_save

def main() -> None:
    n = build_and_save(settings.data_dir, settings.index_dir)
    print(f"OK - indexed {n} chunks into: {settings.index_dir}")

if __name__ == "__main__":
    main()