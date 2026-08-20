from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.modules.dashboard.schemas import DashboardResponse
from app.modules.dashboard.services import get_dashboard


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/",
    response_model=DashboardResponse
)
def read_dashboard(
    db: Session = Depends(get_db)
):
    return get_dashboard(db)