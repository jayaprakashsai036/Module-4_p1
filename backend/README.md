# Python Backend

## Install

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The API is available at `http://127.0.0.1:8000`.

Interactive API documentation:
- `/docs`
- `/redoc`

Android Emulator uses `http://10.0.2.2:8000/` to reach the host computer.

## Endpoints

- `GET /health`
- `POST /chat`

Example request:

```json
{
  "user_id": "user_123",
  "message": "Hello"
}
```
