from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.movement.schemas import (
    StockMovementCreate,
    StockMovementUpdate,
    StockMovementResponse,
)

from app.services.movement import (
    create_stock_movement,
    get_stock_movements,
    get_stock_movement_by_code,
    update_stock_movement,
    delete_stock_movement,
)

from app.services.auth import RoleChecker

from app.utils.utils import UserRole

router = APIRouter(
    prefix="/stock-movements",
    tags=["Stock Movements"],
)


@router.post(
    "/",
    response_model=StockMovementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    movement: StockMovementCreate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER, UserRole.EMPLOYEE]))
):
    return create_stock_movement(db, movement)


@router.get(
    "/",
    response_model=List[StockMovementResponse],
)
def read_all(
    db: Session = Depends(get_db),
):
    return get_stock_movements(db)


@router.get(
    "/{code}",
    response_model=StockMovementResponse,
)
def read_by_code(
    code: str,
    db: Session = Depends(get_db)
):
    return get_stock_movement_by_code(db, code)


@router.put(
    "/{code}",
    response_model=StockMovementResponse
)

def update(
    code: str,
    movement: StockMovementUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):


    return update_stock_movement(
        db,
        code,
        movement,
    )

@router.delete(
    "/{code}",
    status_code=status.HTTP_200_OK,
)

def delete(
    code: str,
    db: Session = Depends(get_db),
    current_user = Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
):
    return delete_stock_movement(
        db,
        code,
    )
