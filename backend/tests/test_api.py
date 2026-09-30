from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat():
    response = client.post(
        "/chat",
        json={"user_id": "test_user", "message": "Hello"}
    )
    assert response.status_code == 200
    assert "reply" in response.json()
