from sqlalchemy import select

from app.db.database import AsyncSessionLocal
from app.modules.roles.model import Role


ROLES = [
    {
        "name": "admin",
        "description": "Full system access"
    },
    {
        "name": "analyst",
        "description": "SOC analyst access"
    },
    {
        "name": "viewer",
        "description": "Read only access"
    }
]


async def seed_roles():

    async with AsyncSessionLocal() as session:

        for role_data in ROLES:

            result = await session.execute(
                select(Role).where(
                    Role.name == role_data["name"]
                )
            )

            existing = result.scalar_one_or_none()

            if not existing:

                role = Role(
                    **role_data
                )

                session.add(role)

        await session.commit()


if __name__ == "__main__":

    import asyncio

    asyncio.run(seed_roles())
