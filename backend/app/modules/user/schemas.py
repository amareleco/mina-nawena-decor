from pydantic import BaseModel, EmailStr
from datetime import date
from app.utils.utils import UserRole



# Dados recebidos ao criar usuário
class UserCreate(BaseModel):

    name: str

    email: EmailStr

    password: str

    role: UserRole


# Dados para atualização
class UserUpdate(BaseModel):

    name: str | None = None

    email: EmailStr | None = None

    role: UserRole | None = None

    is_active: bool | None = None
    
    password: str | None = None



# Dados retornados pela API
class UserResponse(BaseModel):

    id: int

    code: str

    name: str

    email: EmailStr

    role: UserRole

    is_active: bool

    created_at: date


    class Config:
        from_attributes = True