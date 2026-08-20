from datetime import date

from pydantic import BaseModel, EmailStr


# Dados para criar cliente
class ClientCreate(BaseModel):

    name: str

    phone: str

    email: EmailStr | None = None

    address: str | None = None



# Dados para atualizar cliente
class ClientUpdate(BaseModel):

    name: str | None = None

    phone: str | None = None

    email: EmailStr | None = None

    address: str | None = None

    is_active: bool | None = None



# Dados retornados pela API
class ClientResponse(BaseModel):

    code: str

    name: str

    phone: str

    email: EmailStr | None

    address: str | None

    is_active: bool

    created_at: date


    class Config:
        from_attributes = True