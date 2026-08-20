from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.supplier.schemas import (
    SupplierCreate,
    SupplierUpdate,
    SupplierResponse
)

from app.services.supplier import (
    create_supplier,
    get_suppliers,
    get_supplier_by_code,
    update_supplier,
    delete_supplier
)


router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)



@router.post(
    "/",
    response_model=SupplierResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):

    return create_supplier(
        db,
        supplier
    )



@router.get(
    "/",
    response_model=list[SupplierResponse]
)
def read_all(
    db: Session = Depends(get_db)
):

    return get_suppliers(
        db
    )



@router.get(
    "/{code}",
    response_model=SupplierResponse
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db)
):

    supplier = get_supplier_by_code(
        db,
        code
    )


    if not supplier:

        raise HTTPException(
            status_code=404,
            detail="Fornecedor não encontrado"
        )


    return supplier



@router.put(
    "/{code}",
    response_model=SupplierResponse
)
def update(
    code: str,
    supplier_data: SupplierUpdate,
    db: Session = Depends(get_db)
):

    supplier = update_supplier(
        db,
        code,
        supplier_data
    )


    if not supplier:

        raise HTTPException(
            status_code=404,
            detail="Fornecedor não encontrado"
        )


    return supplier



@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    code: str,
    db: Session = Depends(get_db)
):

    supplier = delete_supplier(
        db,
        code
    )


    if not supplier:

        raise HTTPException(
            status_code=404,
            detail="Fornecedor não encontrado"
        )


    return None