from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.telemetry.telemetry_session import TelemetrySession


class SystemSnapshot(BaseModel):

    __tablename__ = "system_snapshots"

    session_id = mapped_column(
        ForeignKey("telemetry_sessions.id"),
        nullable=False,
        unique=True,
    )

    hostname: Mapped[str] = mapped_column(String(255))
    ip: Mapped[str] = mapped_column(String(64))

    mac: Mapped[str | None] = mapped_column(String(64))
    os: Mapped[str | None] = mapped_column(String(100))
    platform: Mapped[str | None] = mapped_column(String(255))
    kernel: Mapped[str | None] = mapped_column(String(100))
    architecture: Mapped[str | None] = mapped_column(String(50))
    cpu: Mapped[str | None] = mapped_column(String(255))

    physical_cores: Mapped[int | None] = mapped_column(Integer)
    logical_cores: Mapped[int | None] = mapped_column(Integer)

    memory_total_gb: Mapped[float | None] = mapped_column(Float)
    memory_available_gb: Mapped[float | None] = mapped_column(Float)
    memory_percent: Mapped[float | None] = mapped_column(Float)

    disk_total_gb: Mapped[float | None] = mapped_column(Float)
    disk_used_gb: Mapped[float | None] = mapped_column(Float)
    disk_free_gb: Mapped[float | None] = mapped_column(Float)
    disk_percent: Mapped[float | None] = mapped_column(Float)

    boot_time: Mapped[str | None] = mapped_column(String(100))

    session: Mapped["TelemetrySession"] = relationship(
        back_populates="system_snapshot",
    )
