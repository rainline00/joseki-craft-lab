import os

from dotenv import load_dotenv
from gqlalchemy import Memgraph

load_dotenv()


class MemgraphConnection:
    _connection = None

    @classmethod
    async def connect(cls) -> Memgraph:
        if cls._connection is None:
            cls._connection = Memgraph(
                host=os.getenv("MEMGRAPH_HOST", "localhost"),
                port=int(os.getenv("MEMGRAPH_PORT", 7687)),
                username=os.getenv("MEMGRAPH_USER", ""),
                password=os.getenv("MEMGRAPH_PASSWORD", ""),
                encrypted=False,
            )
        return cls._connection

    @classmethod
    async def close(cls) -> None:
        cls._connection = None

    @classmethod
    async def get_connection(cls) -> Memgraph:
        if cls._connection is None:
            await cls.connect()
        if cls._connection is None:
            raise ValueError
        return cls._connection
