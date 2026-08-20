from datetime import date

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    description: str | None = None


class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class CategoryResponse(BaseModel):
    id: int

    code: str

    name: str

    description: str | None

    created_at: date

    class Config:
        from_attributes = True