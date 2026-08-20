from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.client.schemas import (
    ClientCreate,
    ClientUpdate,
    ClientResponse
)

from app.services.client import (
    create_client,
    get_clients,
    get_client_by_code,
    update_client,
    delete_client
)


router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)



@router.post(
    "/",
    response_model=ClientResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    client: ClientCreate,
    db: Session = Depends(get_db)
):

    return create_client(
        db,
        client
    )



@router.get(
    "/",
    response_model=list[ClientResponse]
)
def read_all(
    db: Session = Depends(get_db)
):

    return get_clients(
        db
    )



@router.get(
    "/{code}",
    response_model=ClientResponse
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db)
):

    client = get_client_by_code(
        db,
        code
    )


    if not client:

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )


    return client



@router.put(
    "/{code}",
    response_model=ClientResponse
)
def update(
    code: str,
    client_data: ClientUpdate,
    db: Session = Depends(get_db)
):

    client = update_client(
        db,
        code,
        client_data
    )


    if not client:

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )


    return client



@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    code: str,
    db: Session = Depends(get_db)
):

    client = delete_client(
        db,
        code
    )


    if not client:

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )


    return None