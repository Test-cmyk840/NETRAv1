from app.core.security import hash_password

from .model import User
from .repository import UserRepository
from .schemas import UserCreate


class UserService:

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    async def create_user(
        self,
        data: UserCreate,
    ):

        existing = await self.repository.get_by_email(
            data.email
        )

        if existing:
            raise ValueError(
                "Email already exists."
            )

        user = User(
            username=data.username,
            email=data.email,
            password_hash=hash_password(
                data.password
            ),
        )

        return await self.repository.create(
            user
        )
