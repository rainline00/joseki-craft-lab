import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
async def memgraph_connection(monkeypatch):
    # Memgraphへの接続をモック化
    class MockMemgraph:
        async def connect(self):
            pass

        async def close(self):
            pass

    monkeypatch.setattr("app.db.memgraph_db.MemgraphConnection._connection", MockMemgraph())
