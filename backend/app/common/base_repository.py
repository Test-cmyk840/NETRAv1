from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(
        self,
        session: AsyncSession,
        model: type[T],
    ):
        self.session = session
        self.model = model

    async def get(self, id_):

        return await self.session.get(
            self.model,
            id_,
        )

    async def get_all(self):

        result = await self.session.execute(
            select(self.model)
        )

        return result.scalars().all()

    async def create(self, obj):

        self.session.add(obj)

        await self.session.commit()

        await self.session.refresh(obj)

        return obj

    async def delete(self, obj):

        await self.session.delete(obj)

        await self.session.commit()
