from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.db.memgraph_db import MemgraphConnection


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup の処理
    await MemgraphConnection.connect()
    yield
    # shutdown の処理
    await MemgraphConnection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome to Joseki Craft Lab API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
