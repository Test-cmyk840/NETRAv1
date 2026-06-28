from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.agents.model import Agent
from app.modules.agents.repository import AgentRepository
from app.modules.agents.schemas import AgentRegisterRequest


class AgentService:

    @staticmethod
    async def register_agent(
        db: AsyncSession,
        data: AgentRegisterRequest,
    ) -> Agent:

        existing = await AgentRepository.get_by_hostname(
            db,
            data.hostname,
        )

        if existing:
            return existing

        agent = Agent(
            hostname=data.hostname,
            ip_address=data.ip_address,
            operating_system=data.operating_system,
            version=data.version,
            status="online",
            agent_token=str(uuid4()),
        )

        return await AgentRepository.create(
            db,
            agent,
        )

    @staticmethod
    async def heartbeat(
        db: AsyncSession,
        token: str,
    ) -> Agent | None:

        agent = await AgentRepository.get_by_token(
            db,
            token,
        )

        if agent is None:
            return None

        agent.last_seen = datetime.now(timezone.utc)
        agent.status = "online"

        return await AgentRepository.update(
            db,
            agent,
        )

    @staticmethod
    async def list_agents(
        db: AsyncSession,
    ) -> list[Agent]:

        return await AgentRepository.get_all(db)

    @staticmethod
    async def get_agent(
        db: AsyncSession,
        agent_id,
    ) -> Agent | None:

        return await AgentRepository.get_by_id(
            db,
            agent_id,
        )

    @staticmethod
    async def delete_agent(
        db: AsyncSession,
        agent_id,
    ) -> bool:

        agent = await AgentRepository.get_by_id(
            db,
            agent_id,
        )

        if agent is None:
            return False

        await AgentRepository.delete(
            db,
            agent,
        )

        return True
