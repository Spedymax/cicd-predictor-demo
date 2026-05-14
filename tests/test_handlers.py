from fastapi.testclient import TestClient

from src.app import app


def test_health() -> None:
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_ready() -> None:
    c = TestClient(app)
    assert c.get("/ready").json() == {"ready": True}
