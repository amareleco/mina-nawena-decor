from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.product.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.services.product import (
    create_product,
    get_products,
    get_product_by_code,
    update_product,
    delete_product
)

from app.services.auth import RoleChecker

from app.utils.utils import UserRole


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)



@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):

    new_product = create_product(
        db,
        product
    )


    if not new_product:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )


    return new_product



@router.get(
    "/",
    response_model=list[ProductResponse]
)
def read_all(
    db: Session = Depends(get_db)
):

    return get_products(
        db
    )



@router.get(
    "/{code}",
    response_model=ProductResponse
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db)
):

    product = get_product_by_code(
        db,
        code
    )


    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )


    return product



@router.put(
    "/{code}",
    response_model=ProductResponse
)
def update(
    code: str,
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):

    product = update_product(
        db,
        code,
        product_data
    )


    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )


    return product



@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    code: str,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN]))
):

    product = delete_product(
        db,
        code
    )


    if not product:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )


    return None