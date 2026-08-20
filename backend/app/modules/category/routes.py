from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.category.schemas import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

from app.services.category import (
    create_category,
    get_categories,
    get_category_by_code,
    update_category,
    delete_category
)

from app.services.auth import RoleChecker

from app.utils.utils import UserRole


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)



@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER] ))
):

    return create_category(
        db,
        category
    )



@router.get(
    "/",
    response_model=list[CategoryResponse]
)
def read_all(
    db: Session = Depends(get_db)
):

    return get_categories(
        db
    )



@router.get(
    "/{code}",
    response_model=CategoryResponse
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db)
):

    category = get_category_by_code(
        db,
        code
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )

    return category



@router.put(
    "/{code}",
    response_model=CategoryResponse
)
def update(
    code: str,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):

    category = update_category(
        db,
        code,
        category_data
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )

    return category



@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)

def delete(
    code: str,
    db: Session = Depends(get_db),
     current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):

    category = delete_category(
        db,
        code
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )

    return None