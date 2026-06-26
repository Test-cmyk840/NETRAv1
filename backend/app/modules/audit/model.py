from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.users.model import User


class AuditLog(BaseModel):
    """
    Audit log model.

    Records all important user actions performed within NETRA
    for accountability, traceability, and forensic analysis.
    """

    __tablename__ = "audit_logs"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    resource: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    details: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="audit_logs",
    )

    def __repr__(self) -> str:
        return (
            f"<AuditLog(action='{self.action}', "
            f"resource='{self.resource}')>"
        )
