from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.modules.agents.schemas import (
    AgentRegisterRequest,
    AgentRegistrationResponse,
    AgentResponse,
    HeartbeatRequest,
)
from app.modules.agents.service import AgentService
from app.modules.auth.dependencies import require_role

router = APIRouter(
    prefix="/agents",
    tags=["Agents"],
)


@router.post(
    "/register",
    response_model=AgentRegistrationResponse,
)
async def register_agent(
    request: AgentRegisterRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(require_role("admin")),
):
    agent = await AgentService.register_agent(
        db,
        request,
    )

    return AgentRegistrationResponse(
        agent_id=agent.id,
        agent_token=agent.agent_token,
        status=agent.status,
    )

@router.post("/heartbeat")
async def heartbeat(
    data: HeartbeatRequest,
    db: AsyncSession = Depends(get_db),
):
    agent = await AgentService.heartbeat(
        db,
        data.agent_token,
    )

    if agent is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid agent token",
        )

    return {
        "status": "ok",
        "last_seen": agent.last_seen,
    }


@router.get(
    "",
    response_model=list[AgentResponse],
    dependencies=[Depends(require_role("admin"))],
)
async def list_agents(
    db: AsyncSession = Depends(get_db),
):
    return await AgentService.list_agents(db)


@router.get(
    "/{agent_id}",
    response_model=AgentResponse,
    dependencies=[Depends(require_role("admin"))],
)
async def get_agent(
    agent_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    agent = await AgentService.get_agent(
        db,
        agent_id,
    )

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    return agent


@router.delete(
    "/{agent_id}",
    dependencies=[Depends(require_role("admin"))],
)
async def delete_agent(
    agent_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    deleted = await AgentService.delete_agent(
        db,
        agent_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    return {
        "message": "Agent deleted successfully",
        }    
