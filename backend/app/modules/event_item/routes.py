from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.event_item.schemas import (
    EventItemCreate,
    EventItemUpdate,
    EventItemResponse
)

from app.services.event_item import (
    create_event_item,
    get_event_items,
    get_event_item,
    update_event_item,
    delete_event_item
)



router = APIRouter(
    prefix="/event-items",
    tags=["Event Items"]
)



# Criar reserva de produto no evento

@router.post(
    "/",
    response_model=EventItemResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    data: EventItemCreate,
    db: Session = Depends(get_db)
):

    return create_event_item(
        db,
        data
    )



# Listar todos os itens

@router.get(
    "/",
    response_model=list[EventItemResponse]
)
def read_all(
    db: Session = Depends(get_db)
):

    return get_event_items(
        db
    )



# Buscar por código

@router.get(
    "/{code}",
    response_model=EventItemResponse
)
def read_one(
    code: str,
    db: Session = Depends(get_db)
):

    item = get_event_item(
        db,
        code
    )


    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item do evento não encontrado"
        )


    return item



# Atualizar quantidade

@router.put(
    "/{code}",
    response_model=EventItemResponse
)
def update(
    code: str,
    data: EventItemUpdate,
    db: Session = Depends(get_db)
):

    item = update_event_item(
        db,
        code,
        data
    )


    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item do evento não encontrado"
        )


    return item



# Remover item

@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    code: str,
    db: Session = Depends(get_db)
):

    item = delete_event_item(
        db,
        code
    )


    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item do evento não encontrado"
        )


    return None