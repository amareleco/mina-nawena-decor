from datetime import date

from pydantic import BaseModel, EmailStr


# Dados para criar fornecedor
class SupplierCreate(BaseModel):

    name: str

    contact: str

    email: EmailStr | None = None

    address: str | None = None



# Dados para atualizar fornecedor
class SupplierUpdate(BaseModel):

    name: str | None = None

    contact: str | None = None

    email: EmailStr | None = None

    address: str | None = None

    is_active: bool | None = None



# Dados retornados pela API
class SupplierResponse(BaseModel):

    code: str

    name: str

    contact: str

    email: EmailStr | None

    address: str | None

    is_active: bool

    created_at: date


    class Config:
        from_attributes = True