from datetime import date

from pydantic import BaseModel


# Criar evento
class EventCreate(BaseModel):

    client_id: int

    name: str

    event_type: str

    event_date: date

    location: str

    description: str | None = None



# Atualizar evento
class EventUpdate(BaseModel):

    name: str | None = None

    event_type: str | None = None

    event_date: date | None = None

    location: str | None = None

    status: str | None = None

    description: str | None = None



# Retorno da API
class EventResponse(BaseModel):

    code: str

    name: str

    event_type: str

    event_date: date

    location: str

    status: str

    description: str | None

    client_id: int

    created_at: date


    class Config:
        from_attributes = True