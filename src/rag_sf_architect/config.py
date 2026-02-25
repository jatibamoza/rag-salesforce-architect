from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    data_dir: str = os.getenv("RAG_DATA_DIR", "./data/raw")
    index_dir: str = os.getenv("RAG_INDEX_DIR", "./data/processed/index")
    top_k: int = int(os.getenv("RAG_TOP_K", "5"))

settings = Settings()
