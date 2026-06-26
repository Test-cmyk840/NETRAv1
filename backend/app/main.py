from fastapi import FastAPI

app = FastAPI(
    title="NETRA IDS",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "project": "NETRA",
        "version": "1.0.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
async def ready():
    return {
        "ready": True
    }
