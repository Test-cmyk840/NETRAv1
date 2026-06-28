from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AgentRegisterRequest(BaseModel):
    hostname: str
    ip_address: str
    operating_system: str
    version: str


class AgentUpdateRequest(BaseModel):
    status: str | None = None


class AgentResponse(BaseModel):
    id: UUID
    hostname: str
    ip_address: str
    operating_system: str
    version: str
    status: str
    last_seen: datetime

    model_config = {
        "from_attributes": True,
    }


class AgentRegistrationResponse(BaseModel):
    agent_id: UUID
    agent_token: str
    status: str


class HeartbeatRequest(BaseModel):
    agent_token: str
