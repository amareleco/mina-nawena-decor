from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.modules.product.models import Product
from app.modules.category.models import Category
from app.modules.client.models import Client
from app.modules.supplier.models import Supplier
from app.modules.event.models import Event
from app.modules.movement.models import StockMovement

from app.modules.dashboard.schemas import (
    DashboardResponse,
    DashboardTotals,
    LowStockProduct,
    RecentMovement,
    RecentEvent
)


def get_dashboard(db: Session):

    # Totais gerais
    totals = DashboardTotals(
        products=db.query(Product).count(),
        categories=db.query(Category).count(),
        clients=db.query(Client).count(),
        suppliers=db.query(Supplier).count(),
        events=db.query(Event).count()
    )


    # Produtos com estoque baixo
    low_stock = (
        db.query(Product)
        .filter(Product.quantity <= 5)
        .order_by(Product.quantity.asc())
        .limit(10)
        .all()
    )


    low_stock_data = [
        LowStockProduct(
            code=item.code,
            name=item.name,
            quantity=item.quantity
        )
        for item in low_stock
    ]


    # Últimas movimentações
    movements = (
        db.query(StockMovement)
        .join(Product)
        .order_by(desc(StockMovement.created_at))
        .limit(10)
        .all()
    )


    movement_data = [
        RecentMovement(
            code=item.code,

            product_code=item.product.code,
            product_name=item.product.name,

            movement_type=item.movement_type,
            quantity=item.quantity,

            created_at=item.created_at.strftime("%d/%m/%Y %H:%M")
        )
        for item in movements
    ]


    # Últimos eventos
    events = (
        db.query(Event)
        .join(Client)
        .order_by(desc(Event.created_at))
        .limit(10)
        .all()
    )


    event_data = [
        RecentEvent(
            code=item.code,

            client_code=item.client.code,
            client_name=item.client.name,

            event_date=item.event_date
        )
        for item in events
    ]


    return DashboardResponse(
        totals=totals,
        low_stock=low_stock_data,
        recent_movements=movement_data,
        recent_events=event_data
    )