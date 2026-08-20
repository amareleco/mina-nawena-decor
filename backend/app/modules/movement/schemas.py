from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class MovementType(str, Enum):
    ENTRADA = "ENTRADA"
    SAIDA = "SAIDA"
    DEVOLUCAO = "DEVOLUCAO"
    DANIFICADO = "DANIFICADO"


class StockMovementCreate(BaseModel):

    product_id: int

    movement_type: MovementType

    quantity: int = Field(
        ...,
        gt=0
    )

    reason: str | None = None


class StockMovementUpdate(BaseModel):

    quantity: int | None = Field(
        default=None,
        gt=0
    )

    reason: str | None = None


class StockMovementResponse(BaseModel):

    code: str

    product_code:str

    product_name: str
    movement_type: MovementType

    quantity: int

    reason: str | None = None

    created_at: str

    updated_at: str | None = None


    model_config = {
        "from_attributes": True
    }