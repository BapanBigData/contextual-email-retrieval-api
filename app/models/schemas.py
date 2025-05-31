from pydantic import BaseModel

class EmailQuery(BaseModel):
    query: str
    top_k: int = 3

class EmailResponse(BaseModel):
    response: str
    context_used: list[str]
