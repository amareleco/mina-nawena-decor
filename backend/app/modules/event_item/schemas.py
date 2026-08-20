from pydantic import BaseModel
from typing import Optional


# Criar item para evento
class EventItemCreate(BaseModel):

    event_code: str

    product_code: str

    quantity: int



# Atualizar quantidade reservada
class EventItemUpdate(BaseModel):

    quantity: int


# Resposta da API
class EventItemResponse(BaseModel):
    
    code: str

    event_code: str

    product_code: str

    quantity: int


   
    model_config = {
        "from_attributes": True
    }