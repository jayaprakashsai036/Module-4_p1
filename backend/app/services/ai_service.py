from typing import List
from .memory_store import MemoryStore

class AIService:
    def __init__(self, store: MemoryStore):
        self.store = store

    def generate_response(self, message: str, context: List[str]) -> str:
        if not context:
            return (
                "I don't have previous memories for this user yet. "
                f"You said: {message}"
            )
        joined = "; ".join(context)
        return (
            f"Using your recent memory ({joined}), "
            f"I can help with: {message}"
        )

    def process(self, user_id: str, message: str):
        context = self.store.get_recent(user_id)
        reply = self.generate_response(message, context)
        self.store.add(user_id, message)
        return reply, context
