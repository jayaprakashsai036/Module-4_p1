from pydantic import BaseModel, Field
from typing import List

class ChatRequest(BaseModel):
    user_id: str = Field(min_length=1, max_length=100)
    message: str = Field(min_length=1, max_length=5000)

class ChatResponse(BaseModel):
    reply: str
    context_used: List[str]

class HealthResponse(BaseModel):
    status: str
    service: str
