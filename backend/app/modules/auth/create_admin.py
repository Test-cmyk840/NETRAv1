import asyncio

from sqlalchemy import select

from app.db import models  # Registers all models
from app.db.database import SessionLocal
from app.modules.auth.security import hash_password
from app.modules.roles.model import Role
from app.modules.users.model import User


async def create_admin():

    async with SessionLocal() as db:

        role = await db.scalar(
            select(Role).where(Role.name == "admin")
        )

        if role is None:
            print("Admin role not found.")
            return

        existing = await db.scalar(
            select(User).where(User.username == "admin")
        )

        if existing:
            print("Admin already exists.")
            return

        admin = User(
            username="admin",
            email="admin@netra.local",
            password_hash=hash_password("ChangeMe123!"),
            role_id=role.id,
            is_active=True,
        )

        db.add(admin)

        await db.commit()

        print("Admin user created successfully.")


if __name__ == "__main__":
    asyncio.run(create_admin())
