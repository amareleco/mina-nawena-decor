from sqlalchemy.orm import Session

from app.modules.event.models import Event
from app.modules.event.schemas import (
    EventCreate,
    EventUpdate
)

from app.modules.client.models import Client



def generate_event_code(
    db: Session
) -> str:

    last_event = (
        db.query(Event)
        .order_by(Event.id.desc())
        .first()
    )


    if not last_event:
        number = 1
    else:
        number = last_event.id + 1


    return f"EVT-{number:03d}"



def create_event(
    db: Session,
    event: EventCreate
):

    # verificar se cliente existe
    client = (
        db.query(Client)
        .filter(
            Client.id == event.client_id
        )
        .first()
    )


    if not client:
        return None



    new_event = Event(

        code=generate_event_code(db),

        client_id=event.client_id,

        name=event.name,

        event_type=event.event_type,

        event_date=event.event_date,

        location=event.location,

        description=event.description
    )


    db.add(new_event)

    db.commit()

    db.refresh(new_event)


    return new_event



def get_events(
    db: Session
):

    return (
        db.query(Event)
        .all()
    )



def get_event_by_code(
    db: Session,
    code: str
):

    return (
        db.query(Event)
        .filter(
            Event.code == code
        )
        .first()
    )



def update_event(
    db: Session,
    code: str,
    event_data: EventUpdate
):

    event = get_event_by_code(
        db,
        code
    )


    if not event:
        return None


    data = event_data.model_dump(
        exclude_unset=True
    )


    for key, value in data.items():

        setattr(
            event,
            key,
            value
        )


    db.commit()

    db.refresh(event)


    return event



def delete_event(
    db: Session,
    code: str
):

    event = get_event_by_code(
        db,
        code
    )


    if not event:
        return None


    db.delete(event)

    db.commit()


    return event