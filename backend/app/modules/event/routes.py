from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.event.schemas import (
    EventCreate,
    EventUpdate,
    EventResponse
)

from app.services.event import (
    create_event,
    get_events,
    get_event_by_code,
    update_event,
    delete_event
)



router = APIRouter(
    prefix="/events",
    tags=["Events"]
)



@router.post(
    "/",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    event: EventCreate,
    db: Session = Depends(get_db)
):

    new_event = create_event(
        db,
        event
    )


    if not new_event:

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )


    return new_event



@router.get(
    "/",
    response_model=list[EventResponse]
)
def read_all(
    db: Session = Depends(get_db)
):

    return get_events(
        db
    )



@router.get(
    "/{code}",
    response_model=EventResponse
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db)
):

    event = get_event_by_code(
        db,
        code
    )


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Evento não encontrado"
        )


    return event



@router.put(
    "/{code}",
    response_model=EventResponse
)
def update(
    code: str,
    event_data: EventUpdate,
    db: Session = Depends(get_db)
):

    event = update_event(
        db,
        code,
        event_data
    )


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Evento não encontrado"
        )


    return event



@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    code: str,
    db: Session = Depends(get_db)
):

    event = delete_event(
        db,
        code
    )


    if not event:

        raise HTTPException(
            status_code=404,
            detail="Evento não encontrado"
        )


    return None