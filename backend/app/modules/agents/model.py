from datetime import datetime
from uuid import uuid4
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.telemetry.telemetry_session import TelemetrySession


class Agent(BaseModel):
    __tablename__ = "agents"

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    ip_address: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
    )

    operating_system: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    version: Mapped[str] = mapped_column(
        String(20),
        default="1.0.0",
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="offline",
    )

    last_seen: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    agent_token: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid4()),
        unique=True,
    )

    telemetry_sessions: Mapped[list["TelemetrySession"]] = relationship(
        "TelemetrySession",
        back_populates="agent",
        cascade="all, delete-orphan",
    )
