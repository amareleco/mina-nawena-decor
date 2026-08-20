from sqlalchemy.orm import Session

from app.modules.client.models import Client

from app.modules.client.schemas import (
    ClientCreate,
    ClientUpdate
)



def generate_client_code(
    db: Session
) -> str:

    last_client = (
        db.query(Client)
        .order_by(Client.id.desc())
        .first()
    )


    if not last_client:
        number = 1
    else:
        number = last_client.id + 1


    return f"CLI-{number:03d}"



def create_client(
    db: Session,
    client: ClientCreate
):

    new_client = Client(

        code=generate_client_code(db),

        name=client.name,

        phone=client.phone,

        email=client.email,

        address=client.address
    )


    db.add(new_client)

    db.commit()

    db.refresh(new_client)


    return new_client



def get_clients(
    db: Session
):

    return (
        db.query(Client)
        .all()
    )



def get_client_by_code(
    db: Session,
    code: str
):

    return (
        db.query(Client)
        .filter(
            Client.code == code
        )
        .first()
    )



def update_client(
    db: Session,
    code: str,
    client_data: ClientUpdate
):

    client = get_client_by_code(
        db,
        code
    )


    if not client:
        return None


    data = client_data.model_dump(
        exclude_unset=True
    )


    for key, value in data.items():

        setattr(
            client,
            key,
            value
        )


    db.commit()

    db.refresh(client)


    return client



def delete_client(
    db: Session,
    code: str
):

    client = get_client_by_code(
        db,
        code
    )


    if not client:
        return None


    db.delete(client)

    db.commit()


    return client