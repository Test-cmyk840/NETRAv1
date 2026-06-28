from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.telemetry.telemetry_session import TelemetrySession


class AlertEvent(BaseModel):

    __tablename__ = "alert_events"

    session_id = mapped_column(
        ForeignKey("telemetry_sessions.id"),
        nullable=False,
    )

    rule: Mapped[str] = mapped_column(String(255))

    severity: Mapped[str] = mapped_column(String(50))

    message: Mapped[str] = mapped_column(String(500))

    process: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    pid: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    remote_ip: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    remote_port: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    session: Mapped["TelemetrySession"] = relationship(
        back_populates="alerts",
    )
