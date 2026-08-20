from datetime import datetime
from pydantic import BaseModel







class ReportHeader(BaseModel):
    company: str
    report_name: str
    generated_at: datetime
    total_records: int


class StockReportItem(BaseModel):
    product_code: str
    product_name: str

    category_name: str | None = None

    quantity: int
    minimum_stock: int

    status: str


class StockReportResponse(BaseModel):
    header: ReportHeader
    data: list[StockReportItem]