from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_model import BaseModel


if TYPE_CHECKING:
    from app.modules.users.model import User


class Role(BaseModel):

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="role"
    )
