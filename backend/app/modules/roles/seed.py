import asyncio

from sqlalchemy import select

from app.db import models
from app.db.database import SessionLocal
from app.modules.roles.model import Role


ROLES = [
    {
        "name": "admin",
        "description": "Full system access",
    },
    {
        "name": "analyst",
        "description": "SOC analyst access",
    },
    {
        "name": "viewer",
        "description": "Read only access",
    },
]


async def seed_roles():

    async with SessionLocal() as session:

        for item in ROLES:

            result = await session.execute(
                select(Role).where(
                    Role.name == item["name"]
                )
            )

            existing = result.scalar_one_or_none()

            if existing is None:
                session.add(
                    Role(**item)
                )

        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed_roles())
