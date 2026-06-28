from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.telemetry.telemetry_session import TelemetrySession


class ProcessEvent(BaseModel):

    __tablename__ = "process_events"

    session_id = mapped_column(
        ForeignKey("telemetry_sessions.id"),
        nullable=False,
    )

    pid: Mapped[int] = mapped_column(Integer)

    name: Mapped[str] = mapped_column(String(255))

    username: Mapped[str] = mapped_column(String(255))

    cpu_percent: Mapped[float] = mapped_column(Float)

    memory_percent: Mapped[float] = mapped_column(Float)

    session: Mapped["TelemetrySession"] = relationship(
        back_populates="processes",
    )
