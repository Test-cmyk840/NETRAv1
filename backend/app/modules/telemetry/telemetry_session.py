from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel
from app.modules.telemetry.system_snapshot import SystemSnapshot
if TYPE_CHECKING:
    from app.modules.agents.model import Agent
    from app.modules.telemetry.process_event import ProcessEvent
    from app.modules.telemetry.network_event import NetworkEvent
    from app.modules.telemetry.alert_event import AlertEvent


class TelemetrySession(BaseModel):

    __tablename__ = "telemetry_sessions"

    agent_id = mapped_column(
        ForeignKey("agents.id"),
        nullable=False,
    )

    agent: Mapped["Agent"] = relationship(
        back_populates="telemetry_sessions",
    )
    system_snapshot: Mapped["SystemSnapshot"] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
        uselist=False,
    )   
    processes: Mapped[list["ProcessEvent"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )

    connections: Mapped[list["NetworkEvent"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )

    alerts: Mapped[list["AlertEvent"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )

