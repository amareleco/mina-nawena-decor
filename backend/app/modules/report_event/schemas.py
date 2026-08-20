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
#Eventos
# ==========================
from datetime import date, datetime
from pydantic import BaseModel


class EventItemReport(BaseModel):
    product_code: str
    product_name: str
    quantity: int


class EventReportItem(BaseModel):
    event_code: str
    event_name: str

    client_code: str
    client_name: str

    event_date: date
    location: str | None = None

    status: str

    items: list[EventItemReport]

# ==========================
# Relatório de Eventos
# ==========================

class EventReportResponse(BaseModel):
    header: ReportHeader
    data: list[EventReportItem]