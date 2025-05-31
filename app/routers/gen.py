from fastapi import APIRouter
from app.models.schemas import EmailQuery, EmailResponse
from app.engine.vectorstore import load_faiss_index
from app.engine.prompt_builder import build_prompt
import requests

router = APIRouter()

faiss_index = load_faiss_index()

@router.post("/generate-email-response", response_model=EmailResponse)
def generate_email_response(query: EmailQuery):
    results = faiss_index.similarity_search(query.query, k=query.top_k)
    context = "\n---\n".join([doc.page_content for doc in results])
    prompt = build_prompt(context, query.query)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.1:8b", "prompt": prompt, "stream": False}
    )

    answer = response.json()["response"]
    
    return EmailResponse(
        response=answer,
        context_used=[doc.page_content for doc in results]
    )
