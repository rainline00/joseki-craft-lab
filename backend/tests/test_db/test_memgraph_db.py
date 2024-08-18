import pytest
from src.db.memgraph_db import MemgraphConnection


@pytest.mark.asyncio
async def test_memgraph_connection():
    connection = await MemgraphConnection.connect()
    assert connection is not None
    await MemgraphConnection.close()


@pytest.mark.asyncio
async def test_memgraph_get_connection():
    connection1 = await MemgraphConnection.get_connection()
    connection2 = await MemgraphConnection.get_connection()
    assert connection1 is connection2
    await MemgraphConnection.close()
