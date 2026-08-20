from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.report_product.schemas import ProductReportResponse
from app.modules.report_product.services import get_products_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/products",
    response_model=ProductReportResponse
)
def products_report(
    db: Session = Depends(get_db)
):
    return get_products_report(db)