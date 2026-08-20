from pydantic import BaseModel
from datetime import date
from datetime import datetime


class DashboardTotals(BaseModel):
    products: int
    categories: int
    clients: int
    suppliers: int
    events: int


class LowStockProduct(BaseModel):
    code: str
    name: str
    quantity: int


class RecentMovement(BaseModel):
    code: str

    product_code: str
    product_name: str

    movement_type: str
    quantity: int

    created_at: str

class RecentEvent(BaseModel):
    code: str

    client_code: str
    client_name: str

    event_date: date


class DashboardResponse(BaseModel):
    totals: DashboardTotals
    low_stock: list[LowStockProduct]
    recent_movements: list[RecentMovement]
    recent_events: list[RecentEvent]