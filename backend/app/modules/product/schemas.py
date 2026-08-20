from datetime import date

from pydantic import BaseModel


# Dados para criar produto
class ProductCreate(BaseModel):

    name: str

    description: str | None = None

    category_id: int

    quantity: int = 0

    minimum_stock: int = 0

    is_active: bool


# Dados para atualizar produto
class ProductUpdate(BaseModel):

    name: str | None = None

    description: str | None = None

    category_id: int | None = None

    quantity: int | None = None

    minimum_stock: int | None = None

    is_active: bool | None = None



# Categoria retornada junto com produto
class CategorySimple(BaseModel):

    id: int

    code: str

    name: str


    class Config:
        from_attributes = True



# Dados retornados pela API
class ProductResponse(BaseModel):

    id: int

    code: str

    name: str

    description: str | None

    category: CategorySimple

    quantity: int

    minimum_stock: int

    is_active: bool

    created_at: date


    class Config:
        from_attributes = True