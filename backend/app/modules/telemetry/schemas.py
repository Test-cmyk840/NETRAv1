from pydantic import BaseModel


class SystemInfo(BaseModel):
    hostname: str
    ip: str
    mac: str | None = None
    os: str | None = None
    platform: str | None = None
    kernel: str | None = None
    architecture: str | None = None
    cpu: str | None = None
    physical_cores: int | None = None
    logical_cores: int | None = None
    memory_total_gb: float | None = None
    memory_available_gb: float | None = None
    memory_percent: float | None = None
    disk_total_gb: float | None = None
    disk_used_gb: float | None = None
    disk_free_gb: float | None = None
    disk_percent: float | None = None
    boot_time: str | None = None


class ProcessEvent(BaseModel):
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float
    username: str


class NetworkEvent(BaseModel):
    local_ip: str
    local_port: int
    remote_ip: str | None = None
    remote_port: int | None = None
    status: str
    process: str
    pid: int


class AlertEvent(BaseModel):
    rule: str
    severity: str
    message: str

    process: str | None = None
    pid: int | None = None

    remote_ip: str | None = None
    remote_port: int | None = None


class TelemetryUpload(BaseModel):
    agent_token: str

    system: SystemInfo

    processes: list[ProcessEvent]

    connections: list[NetworkEvent]

    alerts: list[AlertEvent]
