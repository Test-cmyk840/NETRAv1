from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.modules.auth.schemas import LoginRequest, TokenResponse
from app.modules.auth.security import (
    verify_password,
    create_access_token,
)
from app.modules.auth.dependencies import (
    get_current_user,
    require_role,
)


from app.modules.users.repository import UserRepository

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    credentials: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    user = await UserRepository.get_by_username(
        db,
        credentials.username,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    if not verify_password(
        credentials.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "username": user.username,
            "role": user.role.name,
        }
    )

    return TokenResponse(
        access_token=token,
    )
@router.get("/me")
async def me(
    current_user=Depends(get_current_user),
):
    return {
        "id": str(current_user.id),
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role.name,
    }

@router.get("/admin")
async def admin_only(
    current_user=Depends(require_role("admin")),
):
    return {
        "message": "Welcome Admin",
        "user": current_user.username,
    }
