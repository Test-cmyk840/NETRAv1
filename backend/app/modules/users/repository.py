from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.modules.users.model import User


class UserRepository:

    @staticmethod
    async def get_by_username(
        db: AsyncSession,
        username: str,
    ) -> User | None:

        result = await db.execute(
            select(User)
            .options(
                selectinload(User.role)
            )
            .where(
                User.username == username
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_email(
        db: AsyncSession,
        email: str,
    ) -> User | None:

        result = await db.execute(
            select(User)
            .options(
                selectinload(User.role)
            )
            .where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def create(
        db: AsyncSession,
        user: User,
    ) -> User:

        db.add(user)

        await db.commit()

        await db.refresh(user)

        return user
