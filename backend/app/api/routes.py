from fastapi import APIRouter
from ..core.config import APP_NAME
from ..models.chat import ChatRequest, ChatResponse, HealthResponse
from ..services.ai_service import AIService
from ..services.memory_store import MemoryStore

router = APIRouter()
store = MemoryStore()
ai_service = AIService(store)

@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok", service=APP_NAME)

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply, context = ai_service.process(request.user_id, request.message)
    return ChatResponse(reply=reply, context_used=context)
