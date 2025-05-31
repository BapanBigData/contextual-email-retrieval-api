from fastapi import FastAPI
from app.routers.gen import router as email_router

app = FastAPI(
    title="Email Response RAG API"
)

app.include_router(email_router)
