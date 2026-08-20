from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.modules.event_item.models import EventItem
from app.modules.event_item.schemas import (
    EventItemCreate,
    EventItemUpdate
)

from app.modules.event.models import Event
from app.modules.product.models import Product

from app.utils.utils import serialize_event_item



def generate_event_item_code(db: Session):

    last_item = (
        db.query(EventItem)
        .order_by(EventItem.id.desc())
        .first()
    )

    if not last_item:
        number = 1
    else:
        number = last_item.id + 1

    return f"EVTI-{number:03d}"



def create_event_item(
    db: Session,
    data: EventItemCreate
):

    event = (
        db.query(Event)
        .filter(
            Event.code == data.event_code
        )
        .first()
    )


    if not event:
        raise HTTPException(
            status_code=404,
            detail="Evento não encontrado"
        )



    product = (
        db.query(Product)
        .filter(
            Product.code == data.product_code
        )
        .first()
    )


    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )



    if data.quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Quantidade inválida"
        )



    new_item = EventItem(

        code=generate_event_item_code(db),

        event_id=event.id,

        product_id=product.id,

        quantity=data.quantity
    )


    db.add(new_item)

    db.commit()

    db.refresh(new_item)


    return serialize_event_item(new_item)




def get_event_items(
    db: Session
):

    return (
        db.query(EventItem)
        .all()
    )




def get_event_item(
    db: Session,
    code: str
):

    return (
        db.query(EventItem)
        .filter(
            EventItem.code == code
        )
        .first()
    )




def update_event_item(
    db: Session,
    code: str,
    data: EventItemUpdate
):

    item = get_event_item(
        db,
        code
    )


    if not item:
        return None



    if data.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantidade inválida"
        )



    item.quantity = data.quantity


    db.commit()

    db.refresh(item)


    return item




def delete_event_item(
    db: Session,
    code: str
):

    item = get_event_item(
        db,
        code
    )


    if not item:
        return None



    db.delete(item)

    db.commit()


    return item