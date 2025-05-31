from pathlib import Path

def get_project_root() -> Path:
    """Returns the root directory of the project."""
    return Path(__file__).resolve().parent.parent.parent  # → points to project root

def get_faiss_index_path() -> Path:
    """Returns the path to the FAISS index directory."""
    return get_project_root() / "faiss_index"
