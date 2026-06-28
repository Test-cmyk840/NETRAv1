from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.agents.repository import AgentRepository

from app.modules.telemetry.telemetry_session import TelemetrySession
from app.modules.telemetry.system_snapshot import SystemSnapshot
from app.modules.telemetry.process_event import ProcessEvent
from app.modules.telemetry.network_event import NetworkEvent
from app.modules.telemetry.alert_event import AlertEvent

from app.modules.telemetry.repository import TelemetryRepository
from app.modules.telemetry.schemas import TelemetryUpload


class TelemetryService:

    @staticmethod
    async def upload(
        db: AsyncSession,
        data: TelemetryUpload,
    ) -> TelemetrySession | None:

        #
        # Validate agent
        #
        agent = await AgentRepository.get_by_token(
            db,
            data.agent_token,
        )

        if agent is None:
            return None

        #
        # Create telemetry session
        #
        session = TelemetrySession(
            agent_id=agent.id,
        )

        await TelemetryRepository.create_session(
            db,
            session,
        )

        #
        # System Snapshot
        #
        snapshot = SystemSnapshot(
            session_id=session.id,
            hostname=data.system.hostname,
            ip=data.system.ip,
            mac=data.system.mac,
            os=data.system.os,
            platform=data.system.platform,
            kernel=data.system.kernel,
            architecture=data.system.architecture,
            cpu=data.system.cpu,
            physical_cores=data.system.physical_cores,
            logical_cores=data.system.logical_cores,
            memory_total_gb=data.system.memory_total_gb,
            memory_available_gb=data.system.memory_available_gb,
            memory_percent=data.system.memory_percent,
            disk_total_gb=data.system.disk_total_gb,
            disk_used_gb=data.system.disk_used_gb,
            disk_free_gb=data.system.disk_free_gb,
            disk_percent=data.system.disk_percent,
            boot_time=data.system.boot_time,
        )

        await TelemetryRepository.add_system_snapshot(
            db,
            snapshot,
        )

        #
        # Processes
        #
        process_events = []

        for process in data.processes:

            process_events.append(
                ProcessEvent(
                    session_id=session.id,
                    pid=process.pid,
                    name=process.name,
                    username=process.username,
                    cpu_percent=process.cpu_percent,
                    memory_percent=process.memory_percent,
                )
            )

        await TelemetryRepository.add_process_events(
            db,
            process_events,
        )

        #
        # Network Connections
        #
        network_events = []

        for connection in data.connections:

            network_events.append(
                NetworkEvent(
                    session_id=session.id,
                    process=connection.process,
                    pid=connection.pid,
                    local_ip=connection.local_ip,
                    local_port=connection.local_port,
                    remote_ip=connection.remote_ip,
                    remote_port=connection.remote_port,
                    status=connection.status,
                )
            )

        await TelemetryRepository.add_network_events(
            db,
            network_events,
        )

        #
        # IDS Alerts
        #
        alert_events = []

        for alert in data.alerts:

            alert_events.append(
                AlertEvent(
                    session_id=session.id,
                    rule=alert.rule,
                    severity=alert.severity,
                    message=alert.message,
                    process=alert.process,
                    pid=alert.pid,
                    remote_ip=alert.remote_ip,
                    remote_port=alert.remote_port,
                )
            )

        await TelemetryRepository.add_alert_events(
            db,
            alert_events,
        )

        #
        # Single Commit
        #
        await TelemetryRepository.commit(db)

        await TelemetryRepository.refresh(
            db,
            session,
        )

        return session
