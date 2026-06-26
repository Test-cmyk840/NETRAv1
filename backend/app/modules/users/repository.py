from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.base_repository import BaseRepository

from .model import User


class UserRepository(
    BaseRepository[User]
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        super().__init__(
            session,
            User,
        )

    async def get_by_email(
        self,
        email: str,
    ):

        result = await self.session.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    async def get_by_username(
        self,
        username: str,
    ):

        result = await self.session.execute(
            select(User).where(
                User.username == username
            )
        )

        return result.scalar_one_or_none()
