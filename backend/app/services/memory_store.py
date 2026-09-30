import json
from pathlib import Path
from threading import Lock
from typing import Dict, List

class MemoryStore:
    def __init__(self, file_path: str = "data/memories.json"):
        self.path = Path(file_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.lock = Lock()
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def _load(self) -> Dict[str, List[str]]:
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save(self, data: Dict[str, List[str]]) -> None:
        self.path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def get_recent(self, user_id: str, limit: int = 3) -> List[str]:
        with self.lock:
            data = self._load()
            return data.get(user_id, [])[-limit:]

    def add(self, user_id: str, message: str) -> None:
        with self.lock:
            data = self._load()
            data.setdefault(user_id, []).append(message)
            self._save(data)
