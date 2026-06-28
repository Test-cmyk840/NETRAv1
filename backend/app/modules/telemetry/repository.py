from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.telemetry.telemetry_session import TelemetrySession
from app.modules.telemetry.system_snapshot import SystemSnapshot
from app.modules.telemetry.process_event import ProcessEvent
from app.modules.telemetry.network_event import NetworkEvent
from app.modules.telemetry.alert_event import AlertEvent


class TelemetryRepository:

    @staticmethod
    async def create_session(
        db: AsyncSession,
        session: TelemetrySession,
    ) -> TelemetrySession:

        db.add(session)

        # Assign UUID without committing
        await db.flush()

        return session

    @staticmethod
    async def add_system_snapshot(
        db: AsyncSession,
        snapshot: SystemSnapshot,
    ):

        db.add(snapshot)

    @staticmethod
    async def add_process_events(
        db: AsyncSession,
        events: list[ProcessEvent],
    ):

        if events:
            db.add_all(events)

    @staticmethod
    async def add_network_events(
        db: AsyncSession,
        events: list[NetworkEvent],
    ):

        if events:
            db.add_all(events)

    @staticmethod
    async def add_alert_events(
        db: AsyncSession,
        events: list[AlertEvent],
    ):

        if events:
            db.add_all(events)

    @staticmethod
    async def commit(
        db: AsyncSession,
    ):

        await db.commit()

    @staticmethod
    async def refresh(
        db: AsyncSession,
        session: TelemetrySession,
    ):

        await db.refresh(session)

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ) -> list[TelemetrySession]:

        result = await db.execute(
            select(TelemetrySession).order_by(
                TelemetrySession.created_at.desc()
            )
        )

        return list(result.scalars().all())

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        session_id,
    ) -> TelemetrySession | None:

        result = await db.execute(
            select(TelemetrySession).where(
                TelemetrySession.id == session_id
            )
        )

        return result.scalar_one_or_none()
