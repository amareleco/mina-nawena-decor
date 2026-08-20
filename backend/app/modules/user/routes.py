from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.user.schemas import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.services.user import (
    create_user,
    get_users,
    get_user_by_code,
    update_user,
    delete_user
)


from app.services.auth import RoleChecker

from app.utils.utils import UserRole


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN]))
):

    return create_user(
        db,
        user
    )



@router.get(
    "/",
    response_model=list[UserResponse]
)
def read_all(
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):

    return get_users(db)



@router.get(
    "/{code}",
    response_model=UserResponse
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):

    user = get_user_by_code(
        db,
        code
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return user



@router.put(
    "/{code}",
    response_model=UserResponse
)
def update(
    code: str,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN]))
):

    user = update_user(
        db,
        code,
        user_data
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return user



@router.delete(
    "/{code}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    code: str,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN]))
):

    user = delete_user(
        db,
        code
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return None