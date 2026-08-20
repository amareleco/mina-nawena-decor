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

class MovementReportItem(BaseModel):
    code: str

    product_code: str
    product_name: str

    movement_type: str

    quantity: int

    reason: str | None = None

    created_at: datetime

# ==========================
# Relatório de Produtos
# ==========================

class MovementReportResponse(BaseModel):
    header: ReportHeader
    data: list[MovementReportItem]