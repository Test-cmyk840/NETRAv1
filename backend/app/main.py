from fastapi import FastAPI
from app.db import models

from app.api.v1 import api_router

app = FastAPI(
    title="NETRA IDS",
    version="1.0.0",
)

app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/")
async def root():
    return {
        "project": "NETRA",
        "version": "1.0.0",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.get("/ready")
async def ready():
    return {"ready": True}
