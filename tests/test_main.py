from fastapi.testclient import TestClient
from test_app.main import app

client = TestClient(app)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
