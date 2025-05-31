import requests

class OllamaEmbeddingFunction:
    def __call__(self, text: str) -> list[float]:
        response = requests.post(
            "http://localhost:11434/api/embeddings",
            json={"model": "mxbai-embed-large", "prompt": text}
        )
        return response.json()["embedding"]
