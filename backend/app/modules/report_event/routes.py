from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.report_event.schemas import EventReportResponse
from app.modules.report_event.services import get_events_report



router = APIRouter(
    prefix = "/reports",
    tags=["Reports"]
)



@router.get(
    "/events",
    response_model=EventReportResponse
)
def events_report(
    db: Session = Depends(get_db)
):
    return get_events_report(db)