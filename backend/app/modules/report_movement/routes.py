from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.report_movement.schemas import MovementReportResponse
from app.modules.report_movement.services import get_movements_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/movements",
    response_model=MovementReportResponse
)
def movements_report(
    db: Session = Depends(get_db)
):
    return get_movements_report(db)