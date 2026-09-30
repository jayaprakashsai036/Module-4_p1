from app.services.ai_service import AIService
from app.services.memory_store import MemoryStore

class AIWorkflow(AIService):
    """Backward-compatible wrapper for the original project API."""
    def __init__(self):
        super().__init__(MemoryStore())

    def retrieve_context(self, user_id: str, query: str):
        return self.store.get_recent(user_id)

    def generate_response(self, query: str, context: list):
        return super().generate_response(query, context)

    def process(self, user_id: str, message: str):
        return super().process(user_id, message)
