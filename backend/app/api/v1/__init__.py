from fastapi import APIRouter
from app.modules.telemetry.router import router as telemetry_router
from app.api.v1.auth.router import router as auth_router
from app.modules.agents.router import router as agents_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(agents_router)
api_router.include_router(telemetry_router)
