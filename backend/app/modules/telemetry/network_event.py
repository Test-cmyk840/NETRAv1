from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.telemetry.telemetry_session import TelemetrySession


class NetworkEvent(BaseModel):

    __tablename__ = "network_events"

    session_id = mapped_column(
        ForeignKey("telemetry_sessions.id"),
        nullable=False,
    )

    process: Mapped[str] = mapped_column(String(255))

    pid: Mapped[int] = mapped_column(Integer)

    local_ip: Mapped[str] = mapped_column(String(64))

    local_port: Mapped[int] = mapped_column(Integer)

    remote_ip: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    remote_port: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(String(50))

    session: Mapped["TelemetrySession"] = relationship(
        back_populates="connections",
    )
