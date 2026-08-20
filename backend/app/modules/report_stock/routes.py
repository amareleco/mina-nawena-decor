from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.report_stock.schemas import StockReportResponse
from app.modules.report_stock.services import get_stock_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]

)

@router.get(
    "/stock",
    response_model=StockReportResponse
)
def stock_report(
    db: Session = Depends(get_db)
):
    return get_stock_report(db)