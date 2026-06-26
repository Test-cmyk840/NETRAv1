from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):

    username: str

    email: EmailStr

    password: str


class UserResponse(BaseModel):

    id: str

    username: str

    email: EmailStr

    role: str

    is_active: bool

    model_config = {
        "from_attributes": True
    }
