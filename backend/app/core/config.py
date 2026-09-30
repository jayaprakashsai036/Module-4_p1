import os

APP_NAME = os.getenv("APP_NAME", "Memory Assistant API")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
DATA_FILE = os.getenv("DATA_FILE", "data/memories.json")
