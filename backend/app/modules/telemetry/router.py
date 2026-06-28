from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.modules.telemetry.schemas import TelemetryUpload
from app.modules.telemetry.service import TelemetryService

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"],
)


@router.post("")
async def upload_telemetry(
    data: TelemetryUpload,
    db: AsyncSession = Depends(get_db),
):
    session = await TelemetryService.upload(
        db,
        data,
    )

    if session is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid agent token",
        )

    return {
        "message": "Telemetry received",
        "session_id": session.id,
    }
