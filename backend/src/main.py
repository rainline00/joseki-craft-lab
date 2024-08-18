from fastapi import FastAPI
from src.db.memgraph_db import MemgraphConnection

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await MemgraphConnection.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await MemgraphConnection.close()

@app.get("/")
async def root():
    return {"message": "Welcome to Joseki Craft Lab API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
