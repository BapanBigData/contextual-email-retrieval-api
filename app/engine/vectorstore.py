from langchain_community.vectorstores import FAISS
from app.engine.embedding_func import OllamaEmbeddingFunction
from app.config.path_utils import get_faiss_index_path

def load_faiss_index():
    embedding_func = OllamaEmbeddingFunction()
    return FAISS.load_local(
        folder_path=str(get_faiss_index_path()),
        embeddings=embedding_func,
        allow_dangerous_deserialization=True  # safe if trusted
    )
