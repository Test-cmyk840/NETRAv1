from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.agents.model import Agent


class AgentRepository:
    @staticmethod
    async def create(
        db: AsyncSession,
        agent: Agent,
    ) -> Agent:
        db.add(agent)
        await db.commit()
        await db.refresh(agent)
        return agent

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ) -> list[Agent]:
        result = await db.execute(
            select(Agent).order_by(Agent.hostname)
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        agent_id: UUID,
    ) -> Agent | None:
        result = await db.execute(
            select(Agent).where(
                Agent.id == agent_id
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_hostname(
        db: AsyncSession,
        hostname: str,
    ) -> Agent | None:
        result = await db.execute(
            select(Agent).where(
                Agent.hostname == hostname
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_token(
        db: AsyncSession,
        token: str,
    ) -> Agent | None:
        result = await db.execute(
            select(Agent).where(
                Agent.agent_token == token
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update(
        db: AsyncSession,
        agent: Agent,
    ) -> Agent:
        await db.commit()
        await db.refresh(agent)
        return agent

    @staticmethod
    async def delete(
        db: AsyncSession,
        agent: Agent,
    ) -> None:
        await db.delete(agent)
        await db.commit()
