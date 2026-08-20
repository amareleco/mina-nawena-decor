from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


# ==========================
# Cabeçalho do relatório
# ==========================

class ReportHeader(BaseModel):
    company: str
    report_name: str
    generated_at: datetime
    total_records: int


# ==========================
# Produto
# ==========================

class ProductReportItem(BaseModel):
    code: str
    name: str

    category_code: str | None = None
    category_name: str | None = None


    quantity: int
    minimum_stock: int

    stock_status: str


# ==========================
# Relatório de Produtos
# ==========================

class ProductReportResponse(BaseModel):
    header: ReportHeader
    data: list[ProductReportItem]